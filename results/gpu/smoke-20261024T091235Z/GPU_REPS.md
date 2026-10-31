# GPU bench: native vs Omni-Compass, metered by the device

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

GPU NVIDIA A100-SXM4-40GB, driver 570.148.08, persistence mode Enabled, start power limit 400.00 W, workload tools/gpu_workload.py (seeded fp16 matmul request stream).
3 repetitions, order rotated, 180.0 s per arm plus 30.0 s drain, 30.0 s idle before each arm.

Phase: **smoke**. Omni frozen at commit e3b05dc22181; file hashes in FREEZE.json, rechecked at the end.

## Every column, mean over repetitions

| Gauge | native | omni, watching (writes nothing) | omni |
|---|---:|---:|---:|
| work per energy (served requests per kJ) | 37.73 | 38.32 | 37.59 |
| work per wall energy (served requests per kJ, whole machine) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, whole machine at the wall (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, GPU (J) | 5.026e+04 | 4.949e+04 | 5.045e+04 |
| energy per served request (J) | 26.51 | 26.1 | 26.61 |
| power, GPU mean (W) | 236.7 | 233 | 237.5 |
| requests served | 1896 | 1896 | 1896 |
| requests not served | 0 | 0 | 0 |
| response time, mean (ms) | 92.47 | 91.57 | 92.32 |
| response time, 95th percentile (ms) | 288.6 | 284.9 | 288.1 |
| response time, 99th percentile (ms) | 508.5 | 502.3 | 506.7 |
| temperature, peak (C) | 79.33 | 77.67 | 79 |
| temperature, mean (C) | 67.49 | 65.04 | 67.27 |
| energy, CPU package (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, DRAM (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, platform psys (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, rest of the machine (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, GPU device counter (J) | 5.004e+04 | 4.973e+04 | 5.001e+04 |
| power-capped share of samples | 0.6429 | 0.6451 | 0.6404 |

## Total: Omni governs against native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Verdict |
|---|---:|---:|---:|---:|---|
| **work per energy (served requests per kJ) (primary)** | 37.73 | 37.59 | -0.4% | -1.081 to +0.8065 | STEADY, no difference beyond the noise |
| work per wall energy (served requests per kJ, whole machine) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, whole machine at the wall (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU (J) | 5.026e+04 | 5.045e+04 | +0.4% | -1084 to +1451 | STEADY, no difference beyond the noise |
| energy per served request (J) | 26.51 | 26.61 | +0.4% | -0.5718 to +0.7655 | STEADY, no difference beyond the noise |
| power, GPU mean (W) | 236.7 | 237.5 | +0.4% | -5.025 to +6.762 | STEADY, no difference beyond the noise |
| requests served | 1896 | 1896 | +0.0% | +0 to +0 | STEADY, the same |
| requests not served | 0 | 0 | +0 | +0 to +0 | STEADY, the same |
| response time, mean (ms) | 92.47 | 92.32 | -0.2% | -0.9416 to +0.6387 | STEADY, no difference beyond the noise |
| response time, 95th percentile (ms) | 288.6 | 288.1 | -0.2% | -6.732 to +5.718 | STEADY, no difference beyond the noise |
| response time, 99th percentile (ms) | 508.5 | 506.7 | -0.4% | -6.683 to +3.04 | STEADY, no difference beyond the noise |
| temperature, peak (C) | 79.33 | 79 | -0.4% | -1.768 to +1.101 | STEADY, no difference beyond the noise |
| temperature, mean (C) | 67.49 | 67.27 | -0.3% | -1.327 to +0.8838 | STEADY, no difference beyond the noise |
| energy, CPU package (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, DRAM (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, platform psys (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, rest of the machine (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU device counter (J) | 5.004e+04 | 5.001e+04 | -0.1% | -246.3 to +184.9 | STEADY, no difference beyond the noise |
| power-capped share of samples | 0.6429 | 0.6404 | -0.4% | -0.02312 to +0.01807 | STEADY, no difference beyond the noise |

## Observation: omni watching (writes nothing) against native, 3 paired repetitions

| Gauge | native | omni, watching (writes nothing) | Change | 95% interval of the difference | Verdict |
|---|---:|---:|---:|---:|---|
| **work per energy (served requests per kJ) (primary)** | 37.73 | 38.32 | +1.6% | -0.1992 to +1.387 | STEADY, no difference beyond the noise |
| work per wall energy (served requests per kJ, whole machine) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, whole machine at the wall (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU (J) | 5.026e+04 | 4.949e+04 | -1.5% | -1788 to +241.4 | STEADY, no difference beyond the noise |
| energy per served request (J) | 26.51 | 26.1 | -1.5% | -0.9432 to +0.1273 | STEADY, no difference beyond the noise |
| power, GPU mean (W) | 236.7 | 233 | -1.5% | -8.388 to +1.131 | STEADY, no difference beyond the noise |
| requests served | 1896 | 1896 | +0.0% | +0 to +0 | STEADY, the same |
| requests not served | 0 | 0 | +0 | +0 to +0 | STEADY, the same |
| response time, mean (ms) | 92.47 | 91.57 | -1.0% | -3.5 to +1.699 | STEADY, no difference beyond the noise |
| response time, 95th percentile (ms) | 288.6 | 284.9 | -1.3% | -14.31 to +6.903 | STEADY, no difference beyond the noise |
| response time, 99th percentile (ms) | 508.5 | 502.3 | -1.2% | -27.36 to +14.87 | STEADY, no difference beyond the noise |
| temperature, peak (C) | 79.33 | 77.67 | -2.1% | -6.838 to +3.505 | STEADY, no difference beyond the noise |
| temperature, mean (C) | 67.49 | 65.04 | -3.6% | -9.781 to +4.883 | STEADY, no difference beyond the noise |
| energy, CPU package (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, DRAM (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, platform psys (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, rest of the machine (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU device counter (J) | 5.004e+04 | 4.973e+04 | -0.6% | -1368 to +741.5 | STEADY, no difference beyond the noise |
| power-capped share of samples | 0.6429 | 0.6451 | +0.3% | -0.04867 to +0.05292 | STEADY, no difference beyond the noise |

## Authority: Omni governs against Omni watching, 3 paired repetitions

| Gauge | omni, watching (writes nothing) | omni | Change | 95% interval of the difference | Verdict |
|---|---:|---:|---:|---:|---|
| **work per energy (served requests per kJ) (primary)** | 38.32 | 37.59 | -1.9% | -1.532 to +0.06979 | STEADY, no difference beyond the noise |
| work per wall energy (served requests per kJ, whole machine) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, whole machine at the wall (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU (J) | 4.949e+04 | 5.045e+04 | +1.9% | -29.88 to +1944 | STEADY, no difference beyond the noise |
| energy per served request (J) | 26.1 | 26.61 | +1.9% | -0.01576 to +1.025 | STEADY, no difference beyond the noise |
| power, GPU mean (W) | 233 | 237.5 | +1.9% | -0.09415 to +9.088 | STEADY, no difference beyond the noise |
| requests served | 1896 | 1896 | +0.0% | +0 to +0 | STEADY, the same |
| requests not served | 0 | 0 | +0 | +0 to +0 | STEADY, the same |
| response time, mean (ms) | 91.57 | 92.32 | +0.8% | -2.416 to +3.915 | STEADY, no difference beyond the noise |
| response time, 95th percentile (ms) | 284.9 | 288.1 | +1.1% | -13.37 to +19.77 | STEADY, no difference beyond the noise |
| response time, 99th percentile (ms) | 502.3 | 506.7 | +0.9% | -19.4 to +28.25 | STEADY, no difference beyond the noise |
| temperature, peak (C) | 77.67 | 79 | +1.7% | -4.919 to +7.585 | STEADY, no difference beyond the noise |
| temperature, mean (C) | 65.04 | 67.27 | +3.4% | -6.051 to +10.51 | STEADY, no difference beyond the noise |
| energy, CPU package (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, DRAM (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, platform psys (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, rest of the machine (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU device counter (J) | 4.973e+04 | 5.001e+04 | +0.6% | -925.6 to +1491 | STEADY, no difference beyond the noise |
| power-capped share of samples | 0.6451 | 0.6404 | -0.7% | -0.0425 to +0.03319 | STEADY, no difference beyond the noise |

## Verdict on the preregistered question

Work per energy under Omni against native: 37.73 -> 37.59 served requests per kJ, difference -0.1375 (95% interval -1.081 to +0.8065).
Guardrails: requests served held (not below -1%), 95th-percentile response time held (not above +10%), requests not served held (not above +1% of native served).
Observation (watch against native) on the same outcome: STEADY, no difference beyond the noise. Authority (omni against watch): STEADY, no difference beyond the noise.
**Result, by rule: STEADY (inside the noise, within the guardrails).**

## Actuator fidelity (receipt B: requested against read back from the device)

| Arm | Rep | Writes | Refused | mean abs(read back − requested) W | max W | delay median s | delay max s | enforced under requested | total variation W | reversals | restored |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 2 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 3 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 1 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 2 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 3 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |

## Control effort (receipt A)

| Arm | Rep | Decisions | J_u = sum abs(u) dt | mean abs(u) | max abs(u) | saturations | shield interventions | holds |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| omni | 1 | 103 | 0 | n/a | n/a | 0 | 103 | 0 |
| omni | 2 | 103 | 0 | n/a | n/a | 0 | 103 | 0 |
| omni | 3 | 104 | 0 | n/a | n/a | 0 | 104 | 0 |
| watch | 1 | 103 | 0 | n/a | n/a | 0 | 103 | 0 |
| watch | 2 | 103 | 0 | n/a | n/a | 0 | 103 | 0 |
| watch | 3 | 104 | 0 | n/a | n/a | 0 | 104 | 0 |

## Representation fidelity (the engine's projection against the telemetry at the next decision)

R_int: weighted root-mean-square of h(z next) − F_h(h(z), u) over E, U, I_U, S, B (weights 1). Directional accuracy: the share of movements the projection called in the right direction, movements under 0.01 excluded.

| Arm | Rep | Pairs | R_int | directional accuracy | valid directions | by predicted size |
|---|---|---:|---:|---:|---:|---|
| omni | 1 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 2 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 3 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 1 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 2 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 3 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |

## The control

- Writes executed (power limit and clock ceiling): native 0, omni, watching (writes nothing) 0, omni 0.
- Every arm ended at the start limit.
- Energy is the device's own power.draw integrated over time; no number here is modelled.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
