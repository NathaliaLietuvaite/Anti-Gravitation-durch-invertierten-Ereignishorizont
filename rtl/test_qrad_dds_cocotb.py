"""
rtl/test_qrad_dds_cocotb.py
cocotb 2.1.0 Verification Suite for rtl/qrad_dds_phase_core.sv (WORK-ORDER-AGH-03).
"""
from __future__ import annotations

import math

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


def _rfft_magnitudes(samples: list[int]) -> list[float]:
    """Exact pure-Python real DFT magnitudes for bins 0..N//2 (zero external deps)."""
    n = len(samples)
    mags: list[float] = []
    two_pi_over_n = 2.0 * math.pi / n
    for k in range(n // 2 + 1):
        re_s = 0.0
        im_s = 0.0
        w = two_pi_over_n * k
        for t_idx, val in enumerate(samples):
            ang = w * t_idx
            re_s += val * math.cos(ang)
            im_s -= val * math.sin(ang)
        mags.append(math.hypot(re_s, im_s))
    return mags


def _signed14(val: int) -> int:
    val &= 0x3FFF
    return val - 0x4000 if (val & 0x2000) else val


async def _reset_dut(dut) -> None:
    dut.rst_ni.value = 0
    dut.enable_i.value = 0
    dut.ext_gate_pass_i.value = 0
    dut.phase_offset_i.value = 0
    for _ in range(3):
        await RisingEdge(dut.clk_i)


@cocotb.test()
async def t_dds_01_fail_closed_reset(dut) -> None:
    """Reset must hold veto_pin_o=1 and dac_data_o=0."""
    cocotb.start_soon(Clock(dut.clk_i, 10, unit="ns").start())
    await _reset_dut(dut)
    assert int(dut.veto_pin_o.value) == 1
    assert _signed14(int(dut.dac_data_o.value)) == 0
    dut.rst_ni.value = 1
    await RisingEdge(dut.clk_i)
    await RisingEdge(dut.clk_i)
    # Still fail-closed while enable_i=0 / ext_gate_pass_i=0
    assert int(dut.veto_pin_o.value) == 1
    assert _signed14(int(dut.dac_data_o.value)) == 0


@cocotb.test()
async def t_dds_02_pure_20mhz_sine_fft(dut) -> None:
    """Verify exact 20.000 MHz fundamental frequency at 100 MHz clock with high SFDR (not sawtooth)."""
    cocotb.start_soon(Clock(dut.clk_i, 10, unit="ns").start())
    await _reset_dut(dut)
    dut.rst_ni.value = 1
    dut.enable_i.value = 1
    dut.ext_gate_pass_i.value = 1
    dut.phase_offset_i.value = 0x00000000

    await RisingEdge(dut.clk_i)
    samples = []
    n_samples = 500  # Exactly 100 full periods of 20 MHz at 100 MHz clock!
    for _ in range(n_samples):
        await RisingEdge(dut.clk_i)
        assert int(dut.veto_pin_o.value) == 0
        samples.append(_signed14(int(dut.dac_data_o.value)))

    # Exact DFT frequency & SFDR check (pure stdlib)
    mag = _rfft_magnitudes(samples)
    peak_idx = max(range(1, len(mag)), key=lambda k: mag[k])
    peak_mhz = (peak_idx * 100.0) / n_samples
    assert abs(peak_mhz - 20.0) < 0.01, f"Expected 20.0 MHz peak, got {peak_mhz}"

    # Spurious-Free Dynamic Range (SFDR) must exceed 45 dB (real sine LUT vs ~12 dB sawtooth)
    fund = mag[peak_idx]
    max_spur = max(mag[k] for k in range(1, len(mag)) if k != peak_idx)
    sfdr_db = 20.0 * math.log10(fund / max(max_spur, 1e-12))
    assert sfdr_db > 45.0, f"Expected SFDR > 45 dB, got {sfdr_db:.2f} dB"


@cocotb.test()
async def t_dds_03_exact_180deg_ab_antisymmetry(dut) -> None:
    """Verify 0x00000000 vs 0x80000000 produces exact 0-LSB sign inversion across 256 samples."""
    cocotb.start_soon(Clock(dut.clk_i, 10, unit="ns").start())

    async def capture(offset: int) -> list[int]:
        await _reset_dut(dut)
        dut.rst_ni.value = 1
        dut.enable_i.value = 1
        dut.ext_gate_pass_i.value = 1
        dut.phase_offset_i.value = offset
        await RisingEdge(dut.clk_i)
        out = []
        for _ in range(256):
            await RisingEdge(dut.clk_i)
            out.append(_signed14(int(dut.dac_data_o.value)))
        return out

    s_a = await capture(0x00000000)
    s_b = await capture(0x80000000)
    max_err = max(abs(a + b) for a, b in zip(s_a, s_b))
    assert max_err == 0, f"Expected exact 0-LSB 180-deg inversion, got max_err={max_err}"


@cocotb.test()
async def t_dds_04_external_odos_veto_one_cycle_clamp(dut) -> None:
    """Dropping ext_gate_pass_i=0 must clamp dac_data_o=0 and assert veto_pin_o=1 on the next edge."""
    cocotb.start_soon(Clock(dut.clk_i, 10, unit="ns").start())
    await _reset_dut(dut)
    dut.rst_ni.value = 1
    dut.enable_i.value = 1
    dut.ext_gate_pass_i.value = 1
    dut.phase_offset_i.value = 0

    for _ in range(5):
        await RisingEdge(dut.clk_i)
    assert int(dut.veto_pin_o.value) == 0

    # Assert external ODOS hardware VETO
    dut.ext_gate_pass_i.value = 0
    await RisingEdge(dut.clk_i)
    await RisingEdge(dut.clk_i)
    assert int(dut.veto_pin_o.value) == 1
    assert _signed14(int(dut.dac_data_o.value)) == 0


@cocotb.test()
async def t_dds_05_dc_bound_and_ab_lockin_zero_dc(dut) -> None:
    """Single-phase 8-bit LUT DC bias stays <0.5% FS, and A/B 0/180-deg lock-in sum cancels to exact 0.0 LSB."""
    cocotb.start_soon(Clock(dut.clk_i, 10, unit="ns").start())

    async def sample_500(offset: int) -> list[int]:
        await _reset_dut(dut)
        dut.rst_ni.value = 1
        dut.enable_i.value = 1
        dut.ext_gate_pass_i.value = 1
        dut.phase_offset_i.value = offset
        await RisingEdge(dut.clk_i)
        out = []
        for _ in range(500):
            await RisingEdge(dut.clk_i)
            out.append(_signed14(int(dut.dac_data_o.value)))
        return out

    vals_a = await sample_500(0x00000000)
    vals_b = await sample_500(0x80000000)
    mean_dc_single = abs(sum(vals_a) / len(vals_a))
    mean_dc_ab = abs(sum(a + b for a, b in zip(vals_a, vals_b)) / (2 * len(vals_a)))
    assert mean_dc_single < 41.0, f"Expected single-phase DC bias < 0.5% FS (41 LSB), got {mean_dc_single:.4f}"
    assert mean_dc_ab == 0.0, f"Expected exact 0.0 LSB A/B lock-in DC cancellation, got {mean_dc_ab}"
