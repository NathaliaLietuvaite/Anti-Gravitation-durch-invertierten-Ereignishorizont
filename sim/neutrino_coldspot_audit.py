#!/usr/bin/env python3
"""
sim/neutrino_coldspot_audit.py
Module M-01 (WORK-ORDER-AGH-02): Empirical Falsification Audit for Criterion F-B.2
(QRAD-CE-V4 Appendix B) — Directional Cross-Correlation between the Official
IceCube Event Catalog of Alert Tracks (IceCat-1, doi:10.7910/DVN/SCRUCD, 2011-2023)
and the Planck/WMAP Eridanus CMB Cold Spot.

Epistemic Registers:
- REGISTER_M: Official IceCat-1 (RA, Dec, Energy, Signal) catalog observations.
- REGISTER_T: Exact spherical geometry & declination-preserving RA-scrambling
              Monte Carlo null hypothesis (standard IceCube Collaboration method).
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
from typing import Any, Dict, List, Tuple

import numpy as np

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CATALOG = os.path.join(REPO_ROOT, "data", "IceCube_Gold_Bronze_Tracks.csv")
DEFAULT_OUT = os.path.join(REPO_ROOT, "telemetry", "NEUTRINO_COLDSPOT_AUDIT.json")

# Canonical Eridanus CMB Cold Spot center (Cruz et al. 2005; Planck 2013):
# Galactic (l = 207.8 deg, b = -56.3 deg) -> Equatorial J2000 (RA = 03h 15m 05s, Dec = -19 deg 35' 02")
COLDSPOT_RA_DEG: float = (3.0 + 15.0 / 60.0 + 5.0 / 3600.0) * 15.0  # 48.770833 deg
COLDSPOT_DEC_DEG: float = -(19.0 + 35.0 / 60.0 + 2.0 / 3600.0)  # -19.583889 deg
COLDSPOT_L_DEG: float = 207.8
COLDSPOT_B_DEG: float = -56.3
EXPECTED_CATALOG_SHA256: str = "7d5013db3f210004b58414badcac739fc4bf6f90c5b5a495347f8a9080767e15"


def angular_separation_deg(
    ra1_deg: np.ndarray,
    dec1_deg: np.ndarray,
    ra2_deg: float,
    dec2_deg: float,
) -> np.ndarray:
    """Exact great-circle angular separation (degrees) via the Haversine formula."""
    ra1 = np.deg2rad(ra1_deg)
    dec1 = np.deg2rad(dec1_deg)
    ra2 = math.radians(ra2_deg)
    dec2 = math.radians(dec2_deg)
    ddec = dec1 - dec2
    dra = ra1 - ra2
    a = np.sin(0.5 * ddec) ** 2 + np.cos(dec1) * math.cos(dec2) * (np.sin(0.5 * dra) ** 2)
    return np.rad2deg(2.0 * np.arcsin(np.sqrt(np.clip(a, 0.0, 1.0))))


def load_icecat1_catalog(path: str = DEFAULT_CATALOG) -> Tuple[List[Dict[str, Any]], str]:
    """Load official IceCat-1 CSV catalog and return (events, sha256)."""
    with open(path, "rb") as fh:
        raw = fh.read()
    sha = hashlib.sha256(raw).hexdigest()

    events: List[Dict[str, Any]] = []
    reader = csv.DictReader(raw.decode("utf-8").splitlines())
    for row in reader:
        try:
            ra = float(row["RA"])
            dec = float(row["DEC"])
            energy_tev = float(row["ENERGY"])
            signal = float(row["SIGNAL"])
        except (KeyError, ValueError):
            continue
        if not (math.isfinite(ra) and math.isfinite(dec) and math.isfinite(energy_tev)):
            continue
        i3_type = row.get("I3TYPE", "").strip().lower()
        events.append(
            {
                "name": row.get("NAME", "").strip(),
                "i3_type": i3_type,
                "is_gold": "gold" in i3_type,
                "ra_deg": ra,
                "dec_deg": dec,
                "energy_tev": energy_tev,
                "signal_prob": signal,
            }
        )
    return events, sha


def _run_ra_scramble_test(
    ra_deg: np.ndarray,
    dec_deg: np.ndarray,
    radii_deg: Tuple[float, ...] = (5.0, 10.0, 15.0),
    n_trials: int = 10_000,
    seed: int = 20261120,
) -> Dict[str, Any]:
    """Declination-preserving RA-scrambling Monte Carlo test (IceCube standard null)."""
    obs_sep = angular_separation_deg(ra_deg, dec_deg, COLDSPOT_RA_DEG, COLDSPOT_DEC_DEG)
    rng = np.random.RandomState(seed)

    # Pre-compute declination terms once for fast exact vectorization
    dec1 = np.deg2rad(dec_deg)
    sin_d1 = np.sin(dec1) * math.sin(math.radians(COLDSPOT_DEC_DEG))
    cos_d1 = np.cos(dec1) * math.cos(math.radians(COLDSPOT_DEC_DEG))
    ra_cs = math.radians(COLDSPOT_RA_DEG)

    cos_thresholds = {r: math.cos(math.radians(r)) for r in radii_deg}
    obs_counts = {r: int(np.sum(obs_sep <= r)) for r in radii_deg}
    ge_counts = {r: 0 for r in radii_deg}
    null_sums = {r: 0.0 for r in radii_deg}

    batch = 500
    done = 0
    while done < n_trials:
        b = min(batch, n_trials - done)
        rand_ra = rng.uniform(0.0, 2.0 * math.pi, size=(b, len(dec_deg)))
        cos_sep = sin_d1[None, :] + cos_d1[None, :] * np.cos(rand_ra - ra_cs)
        for r in radii_deg:
            k_sim = np.sum(cos_sep >= cos_thresholds[r], axis=1)
            null_sums[r] += float(np.sum(k_sim))
            ge_counts[r] += int(np.sum(k_sim >= obs_counts[r]))
        done += b

    results: Dict[str, Any] = {}
    for r in radii_deg:
        key = f"radius_{int(r)}deg"
        mean_null = null_sums[r] / float(n_trials)
        # Standard Phipson-Smyth (k+1)/(N+1) Monte Carlo p-value for excess (>= obs)
        p_excess = (ge_counts[r] + 1.0) / (n_trials + 1.0)
        results[key] = {
            "radius_deg": r,
            "observed_events": obs_counts[r],
            "null_expected_mean": round(mean_null, 4),
            "p_value_excess_one_sided": round(p_excess, 6),
            "statistically_significant_p_lt_001": bool(p_excess < 0.01),
        }
    return results


def run_neutrino_coldspot_audit(
    catalog_path: str = DEFAULT_CATALOG,
    out_path: str = DEFAULT_OUT,
    n_trials: int = 10_000,
    seed: int = 20261120,
) -> Dict[str, Any]:
    """Execute full empirical IceCat-1 x CMB Cold Spot directional audit."""
    events, cat_sha = load_icecat1_catalog(catalog_path)
    ra_all = np.array([e["ra_deg"] for e in events], dtype=np.float64)
    dec_all = np.array([e["dec_deg"] for e in events], dtype=np.float64)
    sep_all = angular_separation_deg(ra_all, dec_all, COLDSPOT_RA_DEG, COLDSPOT_DEC_DEG)

    order = np.argsort(sep_all)
    nearest_5 = [
        {
            "name": events[int(i)]["name"],
            "i3_type": events[int(i)]["i3_type"],
            "ra_deg": events[int(i)]["ra_deg"],
            "dec_deg": events[int(i)]["dec_deg"],
            "energy_tev": events[int(i)]["energy_tev"],
            "signal_prob": events[int(i)]["signal_prob"],
            "angular_sep_deg": round(float(sep_all[int(i)]), 4),
        }
        for i in order[:5]
    ]

    all_tests = _run_ra_scramble_test(ra_all, dec_all, (5.0, 10.0, 15.0), n_trials=n_trials, seed=seed)

    gold_events = [e for e in events if e["is_gold"]]
    ra_gold = np.array([e["ra_deg"] for e in gold_events], dtype=np.float64)
    dec_gold = np.array([e["dec_deg"] for e in gold_events], dtype=np.float64)
    gold_tests = _run_ra_scramble_test(ra_gold, dec_gold, (5.0, 10.0, 15.0), n_trials=n_trials, seed=seed + 1)

    any_sig = any(
        v["statistically_significant_p_lt_001"]
        for v in (*all_tests.values(), *gold_tests.values())
    )
    verdict = (
        "EXCESS_DETECTED_REQUIRES_INDEPENDENT_FOLLOWUP"
        if any_sig
        else "CONSISTENT_WITH_ISOTROPIC_RA_NULL_NO_COLDSPOT_EXCESS"
    )

    energies = [e["energy_tev"] for e in events]
    report: Dict[str, Any] = {
        "schema": "AGH_M01_NEUTRINO_COLDSPOT_AUDIT_V1",
        "epistemic_register": "REGISTER_M",
        "criterion_id": "F-B.2",
        "catalog_provenance": {
            "name": "IceCube Event Catalog of Alert Tracks (IceCat-1, 2011-2023)",
            "doi": "10.7910/DVN/SCRUCD",
            "file": os.path.basename(catalog_path),
            "sha256": cat_sha,
            "matches_expected_sha256": cat_sha == EXPECTED_CATALOG_SHA256,
            "total_events": len(events),
            "gold_events": len(gold_events),
            "energy_min_tev": round(min(energies), 2),
            "energy_median_tev": round(float(np.median(energies)), 2),
            "energy_max_tev": round(max(energies), 2),
        },
        "cold_spot_target": {
            "reference": "Cruz et al. 2005; Planck Collaboration 2013 (Eridanus Cold Spot)",
            "galactic_l_deg": COLDSPOT_L_DEG,
            "galactic_b_deg": COLDSPOT_B_DEG,
            "j2000_ra_deg": round(COLDSPOT_RA_DEG, 4),
            "j2000_dec_deg": round(COLDSPOT_DEC_DEG, 4),
        },
        "null_methodology": {
            "method": "Declination-preserving Right-Ascension scrambling (exact IceCube A_eff(Dec) invariance)",
            "n_monte_carlo_trials": n_trials,
            "seed": seed,
        },
        "all_events_results": all_tests,
        "gold_only_results": gold_tests,
        "nearest_5_events_to_cold_spot": nearest_5,
        "empirical_verdict": verdict,
    }

    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(report, fh, indent=2)
            fh.write("\n")
    return report


if __name__ == "__main__":
    print(json.dumps(run_neutrino_coldspot_audit(), indent=2))
