# Anti-Gravitation durch invertierten Ereignishorizont (`QRAD-CE`)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Revision](https://img.shields.io/badge/Revision-V2.0--AGH%20(WORK--ORDER--AGH--01)-cyan.svg)](#revision-v20-agh-engineering-refactoring)
[![Epistemic Discipline](https://img.shields.io/badge/Epistemic-REGISTER__M%20%7C%20D%20%7C%20T%20%7C%20I-emerald.svg)](#epistemic-register-discipline--physical-conservation-baseline)

**Lead Architect:** Nathália Lietuvaitė  
**Local Systems Engineering & Hygiene Refactoring (`Revision V2.0-AGH`):** `AntiG` (`V-MAX-12 Node Alpha`)  
**Repository Evolution:** Full 2025–2026 conceptual history preserved immutably in Git history (original pre-refactor tip `f93b276c055f328dfdff002d6667cd2921db7e83`).

---

## Epistemic Register Discipline & Physical Conservation Baseline

Consistent with the epistemic hygiene established across the PQMS / `V-MAX-12` ecosystem (see [PQMS-ODOS-MTSC-V-MAX-12-Node-ALPHA-V1.md (Appendix J)](https://github.com/NathaliaLietuvaite/Quantenkommunikation/blob/main/PQMS-ODOS-MTSC-V-MAX-12-Node-ALPHA-V1.md)), every document and executable artifact in this repository is explicitly separated into four epistemic registers:

| Epistemic Register | Scope in This Repository |
| :--- | :--- |
| **`REGISTER_M`** | Empirical observational or hardware measurements (e.g., Planck CMB Cold Spot `-70 uK`, public IceCube TeV–PeV neutrino catalogs, `Verilator` / `Yosys` / `cocotb` hardware synthesis and simulation telemetry). |
| **`REGISTER_D`** | Engineering design parameters, hardware quantization constants, FPGA DDS/NCO timing targets, and experimental error-budget bounds. |
| **`REGISTER_T`** | Established theoretical & mathematical identities: conservation of energy and momentum ($`\sum \vec{F}_{\text{int}} = 0`$), CODATA dimensional analysis, photon radiation pressure ($`F = P/c`$), acoustic radiation force (Gorkov potential), and **Unruh analog-gravity horizons** (black-hole and white-hole / inverted acoustic horizons at $`|v(x)| = c_s`$). |
| **`REGISTER_I`** | Historical conceptual vision and exploratory hypotheses (propellantless antigravity, localized negative effective mass density $`\rho_{\text{eff}} < 0`$, cosmological projection-resonance narratives), strictly excluded from empirical acceptance proofs. |

> **Binding Physical Scope Declaration (`REGISTER_T` / `REGISTER_M`):**
> 1. **No Propellantless Antigravity Claim:** Under established general relativity, quantum field theory, and momentum conservation, no propellantless antigravity drive or reactionless thrust from vacuum modulation has been demonstrated or shown physically feasible. For example, a `5 cm` optical cavity carrying `10 kW` circulating power stores $`E = P_{\text{circ}}(L/c) \approx 1.67 \times 10^{-6}\text{ J}`$, corresponding to $`\Delta m = E/c^2 \approx 1.85 \times 10^{-23}\text{ kg}`$—roughly `13` orders of magnitude below the historical `0.3 mg` conceptual target even under `1000 g` acceleration. Real measurable laboratory thrust requires genuine momentum transfer (directed photon radiation pressure $`F = P/c \approx 3.33\text{ nN/W}`$, acoustic radiation force in air/fluid, or electromagnetic field interaction).
> 2. **Neutrino Channel Boundary (`V-MAX-12 Appendix J.1`):** Per `Appendix J.1` of `PQMS-ODOS-MTSC-V-MAX-12-Node-ALPHA-V1.md`, neutrinos have a weak-interaction cross-section far too small to couple or sustain local macroscopic or biological coherence. In [QRAD-CE-V4-Appendix-B.md](QRAD-CE-V4-Appendix-B.md), IceCube TeV–PeV neutrinos are treated exclusively as an **astrophysical observational channel** for directional hypothesis testing (`F-B.2`) against the Eridanus CMB Cold Spot.
> 3. **Analog Gravity vs. Spacetime Metric Engineering:** Space-Time Acoustic Metasurfaces (STAM) and flowing-medium horizons model **analog event and white-hole horizons** (Unruh 1981; Weinfurtner 2011; Steinhauer 2016), which provide exact mathematical analogs of curved-spacetime kinematics without modifying Newtonian gravity.

---

## Cross-Repository Ecosystem Bridges

This repository forms part of the coordinated PQMS / `V-MAX-12` research suite:

* **Sovereign Core Specification & Appendix I / J:** [NathaliaLietuvaite/Quantenkommunikation](https://github.com/NathaliaLietuvaite/Quantenkommunikation) — `PQMS-ODOS-MTSC-V-MAX-12-Node-ALPHA-V1.md` (host verification, Appendix I CRSI/SIM provenance note, Appendix J information-thermodynamic unification) & `PQMS-ODOS-MTSC-V-MAX-12-RTL-CORE-V2.0-ALPHA.md` (Stage 1 `Q2.30` silicon spec).
* **Production Python/CUDA, Android ARM64 & Synthesizable `Q2.30` RTL Core:** [NathaliaLietuvaite/PQMS-SOVEREIGN-CORE-ANDROID-APP](https://github.com/NathaliaLietuvaite/PQMS-SOVEREIGN-CORE-ANDROID-APP) — `rtl/odos_gate_core.sv` (`195` cycles, `0 LSB` Verilator parity, `Yosys 0.71` `89,609` gates, `7/7` `cocotb` tests) & `bridge/ACE_SYNC_LEDGER.json` (`SYNC-12`).
* **Executable Web Mission Control Demonstrator:** [NathaliaLietuvaite/quantum-city-brain-nexus](https://github.com/NathaliaLietuvaite/quantum-city-brain-nexus) — live browser `BigInt` `Q2.30` RTL simulator (`S-01`–`S-07`), real compiled Verilator VCD logic analyzer, and global Epistemic Truth Lens.

---

## Repository Structure (`Revision V2.0-AGH`)

### Core Specifications (Root)

| File | Register | Scope |
| :--- | :---: | :--- |
| [README.md](README.md) | `M / D / T / I` | Project index, conservation baseline, falsification ledger & roadmap |
| [LICENSE](LICENSE) | — | Standard full-text MIT License |
| [QRAD-CE-V1.md](QRAD-CE-V1.md) | `D / I` | Phase 1 illustrative FPGA control-core blueprint (superseded in RTL by `V-MAX-12` `odos_gate_core.sv` & Phase 3 `qrad_dds_phase_core.sv`) |
| [QRAD-CE-V2.md](QRAD-CE-V2.md) | `T / I` | Space-Time Acoustic Metasurfaces (STAM) & analog-horizon framing |
| [QRAD-CE-V3.md](QRAD-CE-V3.md) | `T / D / I` | Historical TMFE blueprint with `Revision V2.0-AGH` conservation-law & RTL erratum |
| [QRAD-CE-V4.md](QRAD-CE-V4.md) | `M / D / I` | CMB Cold Spot projection-resonance hypothesis & Appendix A (cleaned of foreign `QMK-RVC-V9` / `Bootstrap Loader` tails) |
| [QRAD-CE-V4-Appendix-B.md](QRAD-CE-V4-Appendix-B.md) | `M / T / D / I` | Standalone high-energy neutrino calibration (`IceCube` TeV–PeV) with CODATA dimensional corrections & `F-B.1`–`F-B.5` |

### Early Conceptual Documents (`docs/`, Windows-Safe ASCII Filenames)

All 17 historical 2025–2026 concept essays, formula notes, and early LLM evaluations are preserved with clean, cross-platform ASCII filenames (zero colons, zero spaces, zero broken GFM MathJax or `chartjs` blocks):

* [docs/Formelsammlung-Asymmetrische-Gravitation.md](docs/Formelsammlung-Asymmetrische-Gravitation.md)
* [docs/Emergenz-der-Gravitation-Informationstheoretische-Perspektive.md](docs/Emergenz-der-Gravitation-Informationstheoretische-Perspektive.md) *(renamed from Windows-illegal colon path)*
* [docs/Experiment-Design-NAVKo.md](docs/Experiment-Design-NAVKo.md)
* [docs/Vom-kosmologischen-Rundungsfehler-zur-Antriebsphysik.md](docs/Vom-kosmologischen-Rundungsfehler-zur-Antriebsphysik.md)
* [docs/QHS-Quanten-Helfersystem.md](docs/QHS-Quanten-Helfersystem.md) · [docs/QHS-Prototyp.md](docs/QHS-Prototyp.md) · [docs/QHS-Der-Triple-Alpha-Effekt.md](docs/QHS-Der-Triple-Alpha-Effekt.md) · [docs/QHS-Die-Resonanz-der-Materie.md](docs/QHS-Die-Resonanz-der-Materie.md) · [docs/QHS-Mini-Version-Materialliste.md](docs/QHS-Mini-Version-Materialliste.md)
* [docs/QMS-PQMS-Makro-Implementierung-des-QHS-Prinzips.md](docs/QMS-PQMS-Makro-Implementierung-des-QHS-Prinzips.md)
* [docs/Alpha-Centauri-2025-Symmetrie-V100-Edition.md](docs/Alpha-Centauri-2025-Symmetrie-V100-Edition.md) · [docs/V100-Generator-2026-Anti-G-Drive.md](docs/V100-Generator-2026-Anti-G-Drive.md)
* [docs/Ethik.md](docs/Ethik.md) · [docs/Institute.md](docs/Institute.md) · [docs/Laborausstattung.md](docs/Laborausstattung.md)
* [docs/Grok3-Evaluation-Quanten-Vakuum-Resonanzforschung.md](docs/Grok3-Evaluation-Quanten-Vakuum-Resonanzforschung.md) · [docs/Wissenschaftliche-Gesamtbewertung-des-Repositories.md](docs/Wissenschaftliche-Gesamtbewertung-des-Repositories.md)

### Executable Scientific & Hardware Modules (`sim/`, `rtl/`, `data/`, `telemetry/`, `tests/`)

| Module | Path | Register | Verified Output / Key Metric |
| :--- | :--- | :---: | :--- |
| **M-01 · IceCube × Cold Spot** | [sim/neutrino_coldspot_audit.py](sim/neutrino_coldspot_audit.py) + [data/IceCube_Gold_Bronze_Tracks.csv](data/IceCube_Gold_Bronze_Tracks.csv) | `M / T` | Official **IceCat-1** (`doi:10.7910/DVN/SCRUCD`, `348` tracks / `126` Gold, `54 TeV–20.31 PeV`, SHA-256 `7d5013db...`): **`0` events within `5 deg`** (`p = 1.000`), `2` within `10 deg` (`p = 0.229`), **`0` Gold within `15 deg`** (`p = 1.000`) over `N = 10,000` declination-preserving RA scrambles → **`CONSISTENT_WITH_ISOTROPIC_RA_NULL_NO_COLDSPOT_EXCESS`** ([NEUTRINO_COLDSPOT_AUDIT.json](telemetry/NEUTRINO_COLDSPOT_AUDIT.json)). |
| **M-02 · Analog Horizon Sim** | [sim/analog_horizon_sim.py](sim/analog_horizon_sim.py) | `T` | Unruh (1981) RK4 acoustic geodesic & WKB eikonal integrator: black-hole horizon traps/redshifts (`k/k_0 = 0.383`), while **inverted (white-hole) horizon** stalls rays at `|x| = 0.005 m` with **`18.58x` blueshift pile-up** ([ANALOG_HORIZON_REPORT.json](telemetry/ANALOG_HORIZON_REPORT.json)). |
| **M-03 · Conservation & Force Audit** | [sim/impulse_conservation_audit.py](sim/impulse_conservation_audit.py) | `T` | Proves `13.21`-order-of-magnitude shortfall & `0.0 N` closed-system thrust for TMFE `F-V3.1`, vs. real momentum-conserving forces at `10 W`: photon thruster `33.36 nN` (`3.336 nN/W`) and air acoustic radiation force `29.16 mN` (`2,972.9 mg`-equiv, `874,030x` stronger) ([IMPULSE_CONSERVATION_AUDIT.json](telemetry/IMPULSE_CONSERVATION_AUDIT.json)). |
| **M-04 · Synthesizable 20 MHz DDS RTL** | [rtl/qrad_dds_phase_core.sv](rtl/qrad_dds_phase_core.sv) + [rtl/test_qrad_dds_cocotb.py](rtl/test_qrad_dds_cocotb.py) + [rtl/run_rtl_audit.py](rtl/run_rtl_audit.py) | `D / M` | **`0` Verilator 5.055 `-Wall` warnings**, clean `Icarus -g2012`, **`5/5` `cocotb 2.1.0` tests PASS** (`20.000 MHz` FFT peak `SFDR > 45 dB`, exact **`0 LSB`** `0/180 deg` phase inversion, `1`-cycle fail-closed veto clamp), **`Yosys 0.71`**: `14` coarse cells → **`556` gates (`47` FFs incl. `$_DFF_PN1_` active-high reset veto)** ([QRAD_DDS_RTL_REPORT.json](telemetry/QRAD_DDS_RTL_REPORT.json)). |
| **Hygiene & Unit-Test Suite** | [scripts/verify_repo_hygiene.py](scripts/verify_repo_hygiene.py) + [tests/test_agh_modules.py](tests/test_agh_modules.py) + [.github/workflows/ci.yml](.github/workflows/ci.yml) | `M / T` | Enforces Windows-safe filenames, `0` GFM MathJax errors, `0` dead relative links, and runs `7/7` automated unit tests (`6/7` portable + `1` EDA skipUnless in cloud CI). |

---

## Falsification & Audit Ledger (`Revision V2.0-AGH`)

| ID | Statement / Hypothesis | Register | Current Empirical / Analytical Verdict |
| :--- | :--- | :---: | :--- |
| **F-V3.1** | Cavity $`E/c^2`$ mass fluctuation yields `> 0.3 mg` propellantless thrust | `T / I` | **`FALSIFIED_BY_DIMENSIONAL_AND_CONSERVATION_BOUNDS`** (`13.21` orders of magnitude shortfall + $`\sum \vec{F}_{\text{int}} = 0`$; see [IMPULSE_CONSERVATION_AUDIT.json](telemetry/IMPULSE_CONSERVATION_AUDIT.json)) |
| **F-B.2** | IceCube TeV–PeV neutrino arrival directions correlate with Eridanus CMB Cold Spot (`l = 207.8 deg, b = -56.3 deg`) | `M / T` | **`TESTED_NULL_IN_ICECAT1`** (`0` events within `5 deg` `p = 1.000`, `2` within `10 deg` `p = 0.229`, `0` Gold within `15 deg` `p = 1.000`, `N = 10,000` RA scrambles; see [NEUTRINO_COLDSPOT_AUDIT.json](telemetry/NEUTRINO_COLDSPOT_AUDIT.json)) |
| **F-B.1** | High-energy astrophysical neutrino spectrum exhibits upper cut-off near $`10^{16}\text{ eV}`$ | `M / D` | **`OPEN_OBSERVATIONAL`** (IceCat-1 max event `20.31 PeV`; long-term IceCube-Gen2 / KM3NeT domain) |
| **F-V2.1** | Flowing acoustic / optical metamaterial exhibits inverted (white-hole) analog horizon kinematics at $`|v(x)| = c_s`$ | `T` | **`ANALOG_VERIFIED`** (established Unruh 1981 kinematics reproduced numerically with `18.58x` blueshift pile-up; see [ANALOG_HORIZON_REPORT.json](telemetry/ANALOG_HORIZON_REPORT.json)) |
| **F-V1.1** | Synthesizable `20 MHz` quarter-wave sine DDS with `0 deg / 180 deg` phase toggle and fail-closed interlock | `D / M` | **`VERIFIED_4_EDA_TOOLCHAINS`** (`0` Verilator `-Wall` warnings, `Icarus -g2012` clean, `5/5` cocotb, `556` Yosys 0.71 gates / `47` FFs; see [QRAD_DDS_RTL_REPORT.json](telemetry/QRAD_DDS_RTL_REPORT.json)) |

---

## Revision `V2.0-AGH` Engineering Refactoring & Roadmap

* [x] **Phase 1 (`WORK-ORDER-AGH-01` — Hygiene, Windows Compatibility, GFM MathJax & Errata):**
  * Fixed Windows-NTFS-illegal colon filename (`Emergenz der Gravitation:...`) and standardized all `17` historical essays into clean ASCII filenames under `docs/`.
  * Removed repo-foreign tails (`2,512`-line `QMK-RVC-V9 H.10` + `Bootstrap Loader v24.0` from `QRAD-CE-V4.md`, `765`-line duplicate loader from `QRAD-CE-V3.md`; full original history preserved in Git commit `f93b276`).
  * Extracted standalone [QRAD-CE-V4-Appendix-B.md](QRAD-CE-V4-Appendix-B.md) and corrected CODATA dimensional errors ($`\hbar = 6.582 \times 10^{-16}\text{ eV}\cdot\text{s}`$, $`\hbar c = 1.973 \times 10^{-7}\text{ eV}\cdot\text{m}`$, scale gap $`10^{15}\text{–}10^{20}`$) plus removed unverified 2026 Nobel claims.
  * Migrated `> 215` GitHub-incompatible LaTeX delimiters (`\(...\)` / `\[...\]`) to GFM-safe syntax and replaced `2` non-rendering `chartjs` blocks with native Markdown tables.
  * Added root MIT [LICENSE](LICENSE), automated hygiene checker [scripts/verify_repo_hygiene.py](scripts/verify_repo_hygiene.py), and GitHub Actions CI [.github/workflows/ci.yml](.github/workflows/ci.yml).
* [x] **Phase 2 (`WORK-ORDER-AGH-02` — Executable Scientific Simulation Suite `M-01`–`M-03`):**
  * `M-01`: [sim/neutrino_coldspot_audit.py](sim/neutrino_coldspot_audit.py) — Reproducible IceCube IceCat-1 (`348` events, `doi:10.7910/DVN/SCRUCD`) × Planck CMB Cold Spot directional cross-correlation (`N = 10,000` RA scrambles).
  * `M-02`: [sim/analog_horizon_sim.py](sim/analog_horizon_sim.py) — Numerical black-hole vs. inverted (white-hole) acoustic analog-horizon wave/geodesic simulator (Unruh metric).
  * `M-03`: [sim/impulse_conservation_audit.py](sim/impulse_conservation_audit.py) — Exact SI conservation & dimensional audit comparing photon radiation pressure ($`F = P/c`$), acoustic radiation force, and TMFE $`E/c^2`$ bounds.
* [x] **Phase 3 (`WORK-ORDER-AGH-03` — Synthesizable FPGA Signal Core `M-04`):**
  * `M-04`: [rtl/qrad_dds_phase_core.sv](rtl/qrad_dds_phase_core.sv) — Synthesizable `20 MHz @ 100 MHz` quarter-wave sine DDS with exact `0x00000000 / 0x80000000` `0-LSB` phase toggle and fail-closed interlock, verified cleanly with `Verilator 5.055`, `Icarus -g2012`, `cocotb 2.1.0` (`5/5`), and `Yosys 0.71` (`556` gates / `47` FFs).

### Run Verification Locally

```bash
python3 scripts/verify_repo_hygiene.py
PYTHONPATH=. python3 -m unittest discover -s tests -v
```
