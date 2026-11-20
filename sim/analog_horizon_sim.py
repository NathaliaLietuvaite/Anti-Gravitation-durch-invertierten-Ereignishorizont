#!/usr/bin/env python3
"""
sim/analog_horizon_sim.py
Module M-02 (WORK-ORDER-AGH-02): Numerical Analog-Gravity Event Horizon &
Inverted (White-Hole) Horizon Geodesic Simulator (Unruh 1981 Acoustic Metric).

Epistemic Register: REGISTER_T (established curved-spacetime acoustic analog
kinematics — Weinfurtner 2011, Steinhauer 2016; does NOT modify Newtonian gravity).
"""
from __future__ import annotations

import json
import math
import os
from typing import Any, Dict, List

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUT = os.path.join(REPO_ROOT, "telemetry", "ANALOG_HORIZON_REPORT.json")

HBAR_J_S: float = 1.054571817e-34
K_B_J_K: float = 1.380649e-23


def flow_velocity(x: float, c_s: float, dv: float, width_l: float, horizon_type: str) -> float:
    """
    Smooth acoustic background flow v(x) crossing -c_s at x_H = 0:
    - black_hole: v(x) = -c_s + dv * tanh(x / L)
        x > 0: subsonic (-c_s < v < 0), x < 0: supersonic (v < -c_s) -> traps outgoing rays (dx/dt = v + c_s).
    - white_hole (inverted horizon): v(x) = -c_s - dv * tanh(x / L)
        x < 0: subsonic (-c_s < v < 0), x > 0: supersonic (v < -c_s) -> stalls & repels rays at x = 0.
    """
    sign = 1.0 if horizon_type == "black_hole" else -1.0
    return -c_s + sign * dv * math.tanh(x / width_l)


def flow_velocity_grad(x: float, dv: float, width_l: float, horizon_type: str) -> float:
    """Exact analytic dv/dx."""
    sign = 1.0 if horizon_type == "black_hole" else -1.0
    sech = 1.0 / math.cosh(x / width_l)
    return sign * (dv / width_l) * sech * sech


def analog_hawking_temp_k(kappa_s_inv: float) -> float:
    """Unruh analog Hawking temperature T_H = hbar * |kappa| / (2 * pi * k_B)."""
    return (HBAR_J_S * abs(kappa_s_inv)) / (2.0 * math.pi * K_B_J_K)


def integrate_counter_ray_rk4(
    x0: float,
    c_s: float,
    dv: float,
    width_l: float,
    horizon_type: str,
    dt: float,
    n_steps: int,
) -> Dict[str, Any]:
    """
    Integrate a counter-propagating null acoustic ray dx/dt = v(x) + c_s
    plus its WKB eikonal wavenumber magnification dk/dt = -k * dv/dx (redshift vs. blueshift).
    """
    x = x0
    log_k_ratio = 0.0  # ln(k(t) / k(0))
    traj_x: List[float] = [x]
    traj_t: List[float] = [0.0]

    def rhs_x(pos: float) -> float:
        return flow_velocity(pos, c_s, dv, width_l, horizon_type) + c_s

    def rhs_logk(pos: float) -> float:
        return -flow_velocity_grad(pos, dv, width_l, horizon_type)

    for step in range(1, n_steps + 1):
        k1x = rhs_x(x)
        k1l = rhs_logk(x)
        k2x = rhs_x(x + 0.5 * dt * k1x)
        k2l = rhs_logk(x + 0.5 * dt * k1x)
        k3x = rhs_x(x + 0.5 * dt * k2x)
        k3l = rhs_logk(x + 0.5 * dt * k2x)
        k4x = rhs_x(x + dt * k3x)
        k4l = rhs_logk(x + dt * k3x)

        x += (dt / 6.0) * (k1x + 2.0 * k2x + 2.0 * k3x + k4x)
        log_k_ratio += (dt / 6.0) * (k1l + 2.0 * k2l + 2.0 * k3l + k4l)
        if step % max(1, n_steps // 20) == 0 or step == n_steps:
            traj_x.append(round(x, 6))
            traj_t.append(round(step * dt, 6))

    # Clamp exponent for JSON serialization when extreme pile-up occurs
    clamped_logk = max(-50.0, min(50.0, log_k_ratio))
    return {
        "x0_m": x0,
        "x_final_m": round(x, 6),
        "delta_x_m": round(x - x0, 6),
        "log_wavenumber_shift": round(log_k_ratio, 4),
        "wavenumber_ratio_k_over_k0": float(f"{math.exp(clamped_logk):.4e}"),
        "spectral_behavior": "BLUESHIFT_PILEUP" if log_k_ratio > 0.5 else ("REDSHIFT_ESCAPE" if log_k_ratio < -0.5 else "NEUTRAL"),
        "sample_t": traj_t[:6] + traj_t[-3:],
        "sample_x": traj_x[:6] + traj_x[-3:],
    }


def run_analog_horizon_simulation(out_path: str = DEFAULT_OUT) -> Dict[str, Any]:
    """Compare Black-Hole vs. Inverted (White-Hole) analog acoustic horizons across media."""
    # Normalized dimensionless/laboratory channel: c_s = 1.0 m/s, dv = 0.5 m/s, L = 0.25 m
    c_s, dv, width_l = 1.0, 0.5, 0.25
    kappa_bh = flow_velocity_grad(0.0, dv, width_l, "black_hole")  # +2.0 s^-1
    kappa_wh = flow_velocity_grad(0.0, dv, width_l, "white_hole")  # -2.0 s^-1

    # Black-hole horizon: ray outside (x0 > 0) escapes + redshifts; ray inside (x0 < 0) is trapped inward
    bh_outside = integrate_counter_ray_rk4(0.10, c_s, dv, width_l, "black_hole", dt=0.01, n_steps=150)
    bh_inside = integrate_counter_ray_rk4(-0.10, c_s, dv, width_l, "black_hole", dt=0.01, n_steps=150)

    # Inverted (White-Hole) horizon: ray from subsonic side (x0 < 0) stalls & exponentially blueshifts at x=0;
    # ray from supersonic side (x0 > 0) is also driven back to x=0 -> impenetrable repulsive pile-up barrier!
    wh_subsonic = integrate_counter_ray_rk4(-0.10, c_s, dv, width_l, "white_hole", dt=0.01, n_steps=150)
    wh_supersonic = integrate_counter_ray_rk4(0.10, c_s, dv, width_l, "white_hole", dt=0.01, n_steps=150)

    # Physical analog-gravity reference regimes (Unruh 1981; Steinhauer 2016; STAM concept)
    regimes = []
    for name, cs_val, dv_val, l_val in (
        ("Rubidium_87_BEC_Steinhauer_Scale", 2.0e-3, 1.0e-3, 1.5e-6),
        ("Water_Flume_Weinfurtner_Scale", 0.5, 0.25, 0.05),
        ("Air_Ultrasonic_STAM_40kHz_Scale", 343.0, 100.0, 0.01),
    ):
        kap = dv_val / l_val
        regimes.append(
            {
                "regime": name,
                "sound_speed_m_s": cs_val,
                "surface_gravity_kappa_s_inv": round(kap, 4),
                "analog_hawking_temp_k": float(f"{analog_hawking_temp_k(kap):.4e}"),
            }
        )

    report: Dict[str, Any] = {
        "schema": "AGH_M02_ANALOG_HORIZON_REPORT_V1",
        "epistemic_register": "REGISTER_T",
        "physical_scope": (
            "Unruh (1981) acoustic analog-gravity metric ds^2 = -(c_s^2 - v^2)dt^2 - 2v dxdt + dx^2. "
            "Models exact horizon kinematics (trapping vs. inverted white-hole repulsion/blueshift) "
            "without claiming modification of Newtonian gravitational fields."
        ),
        "channel_parameters": {"c_s_m_s": c_s, "dv_m_s": dv, "width_l_m": width_l},
        "black_hole_horizon": {
            "surface_gravity_kappa_s_inv": kappa_bh,
            "ray_outside_subsonic": bh_outside,
            "ray_inside_supersonic_trapped": bh_inside,
        },
        "inverted_white_hole_horizon": {
            "surface_gravity_kappa_s_inv": kappa_wh,
            "ray_from_subsonic_repelled": wh_subsonic,
            "ray_from_supersonic_stalled": wh_supersonic,
        },
        "physical_analog_regimes": regimes,
    }

    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(report, fh, indent=2)
            fh.write("\n")
    return report


if __name__ == "__main__":
    print(json.dumps(run_analog_horizon_simulation(), indent=2))
