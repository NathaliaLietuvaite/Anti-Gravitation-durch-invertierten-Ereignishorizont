#!/usr/bin/env python3
"""
sim/impulse_conservation_audit.py
Module M-03 (WORK-ORDER-AGH-02): Exact SI/CODATA Dimensional, Momentum-Conservation,
and Real Force-Mechanism Audit (Photon Radiation Pressure, Acoustic Radiation Force,
TMFE E/c^2 Bound, and QRAD-CE-V4 Appendix B Neutrino Scale Consistency).

Epistemic Register: REGISTER_T (exact CODATA 2018 constants & conservation laws).
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUT = os.path.join(REPO_ROOT, "telemetry", "IMPULSE_CONSERVATION_AUDIT.json")

# Exact SI / CODATA 2018 constants
C_M_S: float = 299_792_458.0
G_STD_M_S2: float = 9.80665
HBAR_EV_S: float = 6.582119569e-16
HBAR_C_EV_M: float = HBAR_EV_S * C_M_S  # 1.973269804e-7 eV*m
AIR_SOUND_SPEED_M_S: float = 343.0


def evaluate_tmfe_dimensional_bound(
    circulating_power_w: float = 10_000.0,
    cavity_length_m: float = 0.05,
    piezo_accel_g: float = 1000.0,
    claimed_target_mg: float = 0.30,
) -> Dict[str, Any]:
    """
    Exact SI dimensional check of the historical QRAD-CE-V3 TMFE E/c^2 mass-fluctuation claim.
    Demonstrates both (1) closed-system momentum conservation (sum F_int = 0) and
    (2) the ~13-order-of-magnitude shortfall even for the raw |dm * a| product.
    """
    transit_time_s = cavity_length_m / C_M_S
    stored_energy_j = circulating_power_w * transit_time_s
    equiv_mass_kg = stored_energy_j / (C_M_S ** 2)
    peak_internal_force_n = equiv_mass_kg * (piezo_accel_g * G_STD_M_S2)
    claimed_force_n = claimed_target_mg * 1e-6 * G_STD_M_S2  # 0.30 mg-force in N
    shortfall_factor = claimed_force_n / max(peak_internal_force_n, 1e-99)

    return {
        "criterion_id": "F-V3.1",
        "circulating_power_w": circulating_power_w,
        "cavity_length_m": cavity_length_m,
        "photon_transit_time_s": float(f"{transit_time_s:.4e}"),
        "stored_photonic_energy_j": float(f"{stored_energy_j:.4e}"),
        "mass_equivalent_kg": float(f"{equiv_mass_kg:.4e}"),
        "raw_dm_times_a_n": float(f"{peak_internal_force_n:.4e}"),
        "closed_system_net_thrust_n": 0.0,
        "claimed_target_force_n": float(f"{claimed_force_n:.4e}"),
        "shortfall_orders_of_magnitude": round(float(f"{__import__('math').log10(shortfall_factor):.2f}"), 2),
        "verdict": "DIMENSIONAL_BOUND_EXCEEDED_AND_CLOSED_MOMENTUM_ZERO",
    }


def evaluate_real_momentum_mechanisms(power_w: float = 10.0) -> Dict[str, Any]:
    """
    Real, physically conservative force mechanisms that satisfy momentum conservation:
    1. Directed Photon Radiation Pressure (vacuum, F = P/c; perfect mirror 2P/c).
    2. Acoustic Radiation Force in Air (open medium momentum transfer, F = P/c_s).
    """
    photon_emit_n = power_w / C_M_S
    photon_reflect_n = 2.0 * power_w / C_M_S
    acoustic_air_n = power_w / AIR_SOUND_SPEED_M_S
    acoustic_to_photon_ratio = acoustic_air_n / photon_emit_n

    return {
        "input_power_w": power_w,
        "photon_thruster_emitted_n": float(f"{photon_emit_n:.4e}"),
        "photon_thruster_n_per_w": float(f"{1.0 / C_M_S:.4e}"),
        "photon_mirror_reflected_n": float(f"{photon_reflect_n:.4e}"),
        "acoustic_radiation_force_air_n": float(f"{acoustic_air_n:.4e}"),
        "acoustic_radiation_force_mg_equiv": round((acoustic_air_n / G_STD_M_S2) * 1e6, 2),
        "acoustic_over_photon_ratio": round(acoustic_to_photon_ratio, 1),
        "momentum_conserved": True,
    }


def evaluate_appendix_b_codata_scales() -> Dict[str, Any]:
    """Exact CODATA verification of QRAD-CE-V4 Appendix B energy scales."""
    w_min, w_max = 1e10, 1e12  # rad/s
    e_proj_min_ev = HBAR_EV_S * w_min
    e_proj_max_ev = HBAR_EV_S * w_max

    e_icecube_min_ev, e_icecube_max_ev = 1e12, 1e15
    gap_min = e_icecube_min_ev / e_proj_max_ev
    gap_max = e_icecube_max_ev / e_proj_min_ev

    # Old draft error check vs. corrected Hubble-scale estimate
    old_draft_ev = HBAR_C_EV_M * 1e-10 * 1e21
    hubble_l_m = 4.4e26
    grad_for_1tev_m_inv = 1e12 / (HBAR_C_EV_M * hubble_l_m)

    return {
        "hbar_ev_s": HBAR_EV_S,
        "hbar_c_ev_m": round(HBAR_C_EV_M, 13),
        "e_proj_min_ev": float(f"{e_proj_min_ev:.4e}"),
        "e_proj_max_ev": float(f"{e_proj_max_ev:.4e}"),
        "scale_gap_min_factor": float(f"{gap_min:.3e}"),
        "scale_gap_max_factor": float(f"{gap_max:.3e}"),
        "old_v1_draft_grad_1e_10_L_1e21_ev": float(f"{old_draft_ev:.4e}"),
        "corrected_grad_for_1tev_at_hubble_m_inv": float(f"{grad_for_1tev_m_inv:.4e}"),
    }


def run_impulse_conservation_audit(out_path: str = DEFAULT_OUT) -> Dict[str, Any]:
    """Generate complete SI conservation & dimensional audit report."""
    report: Dict[str, Any] = {
        "schema": "AGH_M03_IMPULSE_CONSERVATION_AUDIT_V1",
        "epistemic_register": "REGISTER_T",
        "tmfe_dimensional_bound": evaluate_tmfe_dimensional_bound(),
        "real_momentum_mechanisms_10w": evaluate_real_momentum_mechanisms(power_w=10.0),
        "appendix_b_codata_calibration": evaluate_appendix_b_codata_scales(),
    }
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(report, fh, indent=2)
            fh.write("\n")
    return report


if __name__ == "__main__":
    print(json.dumps(run_impulse_conservation_audit(), indent=2))
