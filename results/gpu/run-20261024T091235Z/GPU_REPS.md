# GPU bench: native vs Omni-Compass, metered by the device

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

GPU NVIDIA A100-SXM4-40GB, driver 570.148.08, persistence mode Enabled, start power limit 400.00 W, workload tools/gpu_workload.py (seeded fp16 matmul request stream).
10 repetitions, order rotated, 600.0 s per arm plus 30.0 s drain, 60.0 s idle before each arm.

Phase: **confirm**. Omni frozen at commit e3b05dc22181; file hashes in FREEZE.json, rechecked at the end.

## Every column, mean over repetitions

| Gauge | native | omni, watching (writes nothing) | omni |
|---|---:|---:|---:|
| work per energy (served requests per kJ) | 40.48 | 40.51 | 40.56 |
| work per wall energy (served requests per kJ, whole machine) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, whole machine at the wall (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, GPU (J) | 1.6e+05 | 1.598e+05 | 1.596e+05 |
| energy per served request (J) | 24.71 | 24.69 | 24.66 |
| power, GPU mean (W) | 252.9 | 252.7 | 252.3 |
| requests served | 6472 | 6472 | 6472 |
| requests not served | 0 | 0 | 0 |
| response time, mean (ms) | 86.91 | 87.28 | 87.19 |
| response time, 95th percentile (ms) | 252.9 | 254.1 | 253.4 |
| response time, 99th percentile (ms) | 441.8 | 443.1 | 443.6 |
| temperature, peak (C) | 74.9 | 76.3 | 76 |
| temperature, mean (C) | 62.2 | 63.37 | 63.05 |
| energy, CPU package (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, DRAM (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, platform psys (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, rest of the machine (J) | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| energy, GPU device counter (J) | 1.6e+05 | 1.604e+05 | 1.603e+05 |
| power-capped share of samples | 0.7284 | 0.726 | 0.7241 |

## Total: Omni governs against native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Verdict |
|---|---:|---:|---:|---:|---|
| **work per energy (served requests per kJ) (primary)** | 40.48 | 40.56 | +0.2% | -0.4852 to +0.6517 | STEADY, no difference beyond the noise |
| work per wall energy (served requests per kJ, whole machine) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, whole machine at the wall (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU (J) | 1.6e+05 | 1.596e+05 | -0.2% | -2649 to +1884 | STEADY, no difference beyond the noise |
| energy per served request (J) | 24.71 | 24.66 | -0.2% | -0.4094 to +0.291 | STEADY, no difference beyond the noise |
| power, GPU mean (W) | 252.9 | 252.3 | -0.2% | -4.195 to +2.976 | STEADY, no difference beyond the noise |
| requests served | 6472 | 6472 | +0.0% | +0 to +0 | STEADY, the same |
| requests not served | 0 | 0 | +0 | +0 to +0 | STEADY, the same |
| response time, mean (ms) | 86.91 | 87.19 | +0.3% | -0.5502 to +1.103 | STEADY, no difference beyond the noise |
| response time, 95th percentile (ms) | 252.9 | 253.4 | +0.2% | -2.191 to +3.149 | STEADY, no difference beyond the noise |
| response time, 99th percentile (ms) | 441.8 | 443.6 | +0.4% | -4.171 to +7.78 | STEADY, no difference beyond the noise |
| temperature, peak (C) | 74.9 | 76 | +1.5% | -1.223 to +3.423 | STEADY, no difference beyond the noise |
| temperature, mean (C) | 62.2 | 63.05 | +1.4% | -2.119 to +3.821 | STEADY, no difference beyond the noise |
| energy, CPU package (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, DRAM (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, platform psys (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, rest of the machine (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU device counter (J) | 1.6e+05 | 1.603e+05 | +0.2% | -945.4 to +1504 | STEADY, no difference beyond the noise |
| power-capped share of samples | 0.7284 | 0.7241 | -0.6% | -0.009458 to +0.0008552 | STEADY, no difference beyond the noise |

## Observation: omni watching (writes nothing) against native, 10 paired repetitions

| Gauge | native | omni, watching (writes nothing) | Change | 95% interval of the difference | Verdict |
|---|---:|---:|---:|---:|---|
| **work per energy (served requests per kJ) (primary)** | 40.48 | 40.51 | +0.1% | -0.45 to +0.512 | STEADY, no difference beyond the noise |
| work per wall energy (served requests per kJ, whole machine) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, whole machine at the wall (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU (J) | 1.6e+05 | 1.598e+05 | -0.1% | -2082 to +1743 | STEADY, no difference beyond the noise |
| energy per served request (J) | 24.71 | 24.69 | -0.1% | -0.3216 to +0.2693 | STEADY, no difference beyond the noise |
| power, GPU mean (W) | 252.9 | 252.7 | -0.1% | -3.296 to +2.747 | STEADY, no difference beyond the noise |
| requests served | 6472 | 6472 | +0.0% | +0 to +0 | STEADY, the same |
| requests not served | 0 | 0 | +0 | +0 to +0 | STEADY, the same |
| response time, mean (ms) | 86.91 | 87.28 | +0.4% | -0.4137 to +1.152 | STEADY, no difference beyond the noise |
| response time, 95th percentile (ms) | 252.9 | 254.1 | +0.4% | -1.967 to +4.225 | STEADY, no difference beyond the noise |
| response time, 99th percentile (ms) | 441.8 | 443.1 | +0.3% | -4.426 to +7.113 | STEADY, no difference beyond the noise |
| temperature, peak (C) | 74.9 | 76.3 | +1.9% | -0.9891 to +3.789 | STEADY, no difference beyond the noise |
| temperature, mean (C) | 62.2 | 63.37 | +1.9% | -1.449 to +3.799 | STEADY, no difference beyond the noise |
| energy, CPU package (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, DRAM (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, platform psys (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, rest of the machine (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU device counter (J) | 1.6e+05 | 1.604e+05 | +0.3% | -547.4 to +1427 | STEADY, no difference beyond the noise |
| power-capped share of samples | 0.7284 | 0.726 | -0.3% | -0.004807 to +8.307e-05 | STEADY, no difference beyond the noise |

## Authority: Omni governs against Omni watching, 10 paired repetitions

| Gauge | omni, watching (writes nothing) | omni | Change | 95% interval of the difference | Verdict |
|---|---:|---:|---:|---:|---|
| **work per energy (served requests per kJ) (primary)** | 40.51 | 40.56 | +0.1% | -0.2313 to +0.3359 | STEADY, no difference beyond the noise |
| work per wall energy (served requests per kJ, whole machine) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, whole machine at the wall (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU (J) | 1.598e+05 | 1.596e+05 | -0.1% | -1339 to +911.9 | STEADY, no difference beyond the noise |
| energy per served request (J) | 24.69 | 24.66 | -0.1% | -0.2069 to +0.1409 | STEADY, no difference beyond the noise |
| power, GPU mean (W) | 252.7 | 252.3 | -0.1% | -2.116 to +1.446 | STEADY, no difference beyond the noise |
| requests served | 6472 | 6472 | +0.0% | +0 to +0 | STEADY, the same |
| requests not served | 0 | 0 | +0 | +0 to +0 | STEADY, the same |
| response time, mean (ms) | 87.28 | 87.19 | -0.1% | -0.4252 to +0.2394 | STEADY, no difference beyond the noise |
| response time, 95th percentile (ms) | 254.1 | 253.4 | -0.3% | -1.972 to +0.6725 | STEADY, no difference beyond the noise |
| response time, 99th percentile (ms) | 443.1 | 443.6 | +0.1% | -1.109 to +2.03 | STEADY, no difference beyond the noise |
| temperature, peak (C) | 76.3 | 76 | -0.4% | -1.471 to +0.8705 | STEADY, no difference beyond the noise |
| temperature, mean (C) | 63.37 | 63.05 | -0.5% | -1.702 to +1.054 | STEADY, no difference beyond the noise |
| energy, CPU package (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, DRAM (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, platform psys (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, rest of the machine (J) | UNAVAILABLE | UNAVAILABLE | | | no meter |
| energy, GPU device counter (J) | 1.604e+05 | 1.603e+05 | -0.1% | -811.6 to +491.1 | STEADY, no difference beyond the noise |
| power-capped share of samples | 0.726 | 0.7241 | -0.3% | -0.006987 to +0.003108 | STEADY, no difference beyond the noise |

## Verdict on the preregistered question

Work per energy under Omni against native: 40.48 -> 40.56 served requests per kJ, difference +0.08325 (95% interval -0.4852 to +0.6517).
Guardrails: requests served held (not below -1%), 95th-percentile response time held (not above +10%), requests not served held (not above +1% of native served).
Observation (watch against native) on the same outcome: STEADY, no difference beyond the noise. Authority (omni against watch): STEADY, no difference beyond the noise.
**Result, by rule: STEADY (inside the noise, within the guardrails).**

## Actuator fidelity (receipt B: requested against read back from the device)

| Arm | Rep | Writes | Refused | mean abs(read back − requested) W | max W | delay median s | delay max s | enforced under requested | total variation W | reversals | restored |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 2 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 3 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 4 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 5 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 6 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 7 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 8 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 9 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| omni | 10 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 1 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 2 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 3 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 4 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 5 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 6 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 7 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 8 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 9 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |
| watch | 10 | 0 | 0 | n/a | n/a | n/a | n/a | 0 | 0 | 0 | True |

## Control effort (receipt A)

| Arm | Rep | Decisions | J_u = sum abs(u) dt | mean abs(u) | max abs(u) | saturations | shield interventions | holds |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| omni | 1 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| omni | 2 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| omni | 3 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| omni | 4 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| omni | 5 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| omni | 6 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| omni | 7 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| omni | 8 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| omni | 9 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| omni | 10 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 1 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 2 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 3 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 4 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 5 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 6 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 7 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 8 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 9 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |
| watch | 10 | 305 | 0 | n/a | n/a | 0 | 305 | 0 |

## Representation fidelity (the engine's projection against the telemetry at the next decision)

R_int: weighted root-mean-square of h(z next) − F_h(h(z), u) over E, U, I_U, S, B (weights 1). Directional accuracy: the share of movements the projection called in the right direction, movements under 0.01 excluded.

| Arm | Rep | Pairs | R_int | directional accuracy | valid directions | by predicted size |
|---|---|---:|---:|---:|---:|---|
| omni | 1 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 2 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 3 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 4 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 5 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 6 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 7 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 8 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 9 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| omni | 10 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 1 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 2 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 3 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 4 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 5 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 6 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 7 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 8 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 9 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |
| watch | 10 | 0 | n/a | n/a | 0 | 0.01-0.03: n/a of 0, 0.03-0.1: n/a of 0, >=0.1: n/a of 0 |

## The control

- Writes executed (power limit and clock ceiling): native 0, omni, watching (writes nothing) 0, omni 0.
- Every arm ended at the start limit.
- Energy is the device's own power.draw integrated over time; no number here is modelled.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
