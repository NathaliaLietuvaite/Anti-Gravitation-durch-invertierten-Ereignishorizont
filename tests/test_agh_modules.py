"""
tests/test_agh_modules.py
Comprehensive Verification Suite for Anti-Gravitation-durch-invertierten-Ereignishorizont
(Revision V2.0-AGH: Hygiene + M-01 IceCat-1 Cold Spot + M-02 Analog Horizon +
M-03 Impulse Conservation + M-04 Portable/Full RTL Audit).
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import unittest

from rtl.run_rtl_audit import resolve_eda_env, run_rtl_audit
from scripts.verify_repo_hygiene import run_hygiene_audit
from sim.analog_horizon_sim import analog_hawking_temp_k, run_analog_horizon_simulation
from sim.impulse_conservation_audit import (
    evaluate_appendix_b_codata_scales,
    evaluate_real_momentum_mechanisms,
    evaluate_tmfe_dimensional_bound,
    run_impulse_conservation_audit,
)
from sim.neutrino_coldspot_audit import (
    COLDSPOT_DEC_DEG,
    COLDSPOT_RA_DEG,
    EXPECTED_CATALOG_SHA256,
    angular_separation_deg,
    load_icecat1_catalog,
    run_neutrino_coldspot_audit,
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _has_full_eda_stack() -> bool:
    env = resolve_eda_env()
    path = env.get("PATH")
    return all(shutil.which(tool, path=path) is not None for tool in ("verilator", "iverilog", "yosys", "make")) and (
        importlib.util.find_spec("cocotb") is not None or shutil.which("cocotb-config", path=path) is not None
    )


class TestAghModules(unittest.TestCase):
    def test_01_repo_hygiene_zero_errors(self) -> None:
        res = run_hygiene_audit(REPO_ROOT)
        self.assertTrue(res["passed"], msg=f"Hygiene errors: {res['errors']}")
        self.assertEqual(res["error_count"], 0)

    def test_02_m01_icecat1_catalog_sha256_and_geometry(self) -> None:
        events, sha = load_icecat1_catalog()
        self.assertEqual(sha, EXPECTED_CATALOG_SHA256)
        self.assertEqual(len(events), 348)
        # Exact zero-separation identity at Cold Spot center
        import numpy as np

        sep0 = angular_separation_deg(
            np.array([COLDSPOT_RA_DEG]),
            np.array([COLDSPOT_DEC_DEG]),
            COLDSPOT_RA_DEG,
            COLDSPOT_DEC_DEG,
        )
        self.assertLess(float(sep0[0]), 1e-9)

    def test_03_m01_neutrino_coldspot_ra_scramble_null_verdict(self) -> None:
        rep = run_neutrino_coldspot_audit(out_path="", n_trials=2000, seed=20261120)
        self.assertTrue(rep["catalog_provenance"]["matches_expected_sha256"])
        self.assertEqual(rep["all_events_results"]["radius_5deg"]["observed_events"], 0)
        self.assertEqual(rep["gold_only_results"]["radius_15deg"]["observed_events"], 0)
        self.assertEqual(rep["empirical_verdict"], "CONSISTENT_WITH_ISOTROPIC_RA_NULL_NO_COLDSPOT_EXCESS")
        # Also verify committed telemetry file matches schema
        tel_path = os.path.join(REPO_ROOT, "telemetry", "NEUTRINO_COLDSPOT_AUDIT.json")
        self.assertTrue(os.path.isfile(tel_path))
        with open(tel_path, encoding="utf-8") as fh:
            saved = json.load(fh)
        self.assertEqual(saved["empirical_verdict"], "CONSISTENT_WITH_ISOTROPIC_RA_NULL_NO_COLDSPOT_EXCESS")

    def test_04_m02_black_hole_vs_inverted_white_hole_horizon(self) -> None:
        rep = run_analog_horizon_simulation(out_path="")
        bh_out = rep["black_hole_horizon"]["ray_outside_subsonic"]
        bh_in = rep["black_hole_horizon"]["ray_inside_supersonic_trapped"]
        wh_sub = rep["inverted_white_hole_horizon"]["ray_from_subsonic_repelled"]
        wh_sup = rep["inverted_white_hole_horizon"]["ray_from_supersonic_stalled"]

        # Black hole: outside escapes (+), inside trapped (-), both redshift (k/k0 < 1)
        self.assertGreater(bh_out["x_final_m"], bh_out["x0_m"])
        self.assertLess(bh_in["x_final_m"], bh_in["x0_m"])
        self.assertLess(bh_out["wavenumber_ratio_k_over_k0"], 0.5)

        # Inverted / white-hole horizon: rays stall near x=0 and exponentially blueshift (k/k0 > 10)
        self.assertLess(abs(wh_sub["x_final_m"]), 0.01)
        self.assertLess(abs(wh_sup["x_final_m"]), 0.01)
        self.assertGreater(wh_sub["wavenumber_ratio_k_over_k0"], 10.0)
        self.assertEqual(wh_sub["spectral_behavior"], "BLUESHIFT_PILEUP")
        self.assertGreater(analog_hawking_temp_k(666.67), 0.0)

    def test_05_m03_tmfe_dimensional_bound_and_real_momentum(self) -> None:
        tmfe = evaluate_tmfe_dimensional_bound()
        self.assertEqual(tmfe["closed_system_net_thrust_n"], 0.0)
        self.assertGreater(tmfe["shortfall_orders_of_magnitude"], 13.0)
        self.assertEqual(tmfe["verdict"], "DIMENSIONAL_BOUND_EXCEEDED_AND_CLOSED_MOMENTUM_ZERO")

        mech = evaluate_real_momentum_mechanisms(power_w=10.0)
        self.assertTrue(mech["momentum_conserved"])
        self.assertAlmostEqual(mech["photon_thruster_n_per_w"], 1.0 / 299_792_458.0, places=12)
        self.assertGreater(mech["acoustic_over_photon_ratio"], 800_000.0)

        codata = evaluate_appendix_b_codata_scales()
        self.assertAlmostEqual(codata["e_proj_min_ev"], 6.5821e-6, places=9)
        self.assertGreater(codata["scale_gap_min_factor"], 1e15)

        full = run_impulse_conservation_audit(out_path="")
        self.assertEqual(full["schema"], "AGH_M03_IMPULSE_CONSERVATION_AUDIT_V1")

    def test_06_m04_sealed_rtl_report_matches_source_sha256(self) -> None:
        import hashlib

        sv_path = os.path.join(REPO_ROOT, "rtl", "qrad_dds_phase_core.sv")
        rep_path = os.path.join(REPO_ROOT, "telemetry", "QRAD_DDS_RTL_REPORT.json")
        self.assertTrue(os.path.isfile(sv_path))
        self.assertTrue(os.path.isfile(rep_path))
        with open(sv_path, "rb") as fh:
            sv_sha = hashlib.sha256(fh.read()).hexdigest()
        with open(rep_path, encoding="utf-8") as fh:
            rep = json.load(fh)
        self.assertEqual(rep["source_sha256"], sv_sha)
        self.assertEqual(rep["verilator_wall_warnings"], 0)
        self.assertEqual(rep["cocotb_tests_passed"], 5)
        self.assertGreater(rep["yosys_post_techmap_gates"]["total_cells"], 400)
        self.assertEqual(rep["yosys_post_techmap_gates"]["flip_flops"], 47)

    @unittest.skipUnless(_has_full_eda_stack(), "Verilator/Icarus/Yosys/cocotb not installed in this environment")
    def test_07_m04_live_eda_verilator_icarus_cocotb_yosys(self) -> None:
        rep = run_rtl_audit(out_path="")
        self.assertEqual(rep["verilator_wall_warnings"], 0)
        self.assertEqual(rep["cocotb_tests_passed"], 5)
        self.assertTrue(rep["toolchains"]["icarus_g2012_clean"])
        self.assertEqual(rep["verified_properties"]["ab_180deg_inversion_max_err_lsb"], 0)
        self.assertEqual(rep["yosys_post_techmap_gates"]["flip_flops"], 47)


if __name__ == "__main__":
    unittest.main(verbosity=2)
