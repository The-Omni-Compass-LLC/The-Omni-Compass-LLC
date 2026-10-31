# The card on omni-v21, the power cap at 70% of the card's top (cap): three runs on an A100

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three runs on rented cards (A, B and C), NVIDIA A100-SXM4-40GB, 5 paired repetitions each; engine omni-v21 (digest b658f05d43c1e602, 63 files); dial: max (the card governor's dial: max, the factory tune; save, the tune-down). Runs: A 40485609401, B 40485613546, C 40485617318 (their files on the branch `raw`, `run-<id>/`). Each run's own verdict (tools/gpu_reps.py): A NOT ESTABLISHED; B NONINFERIOR / INCONCLUSIVE; C NONINFERIOR / INCONCLUSIVE.

| Gauge | Three runs | A | B | C |
|---|---|---|---|---|
| work per energy (served requests per kJ) | STEADY, under the floor (the three runs' mean 0.11%) | STEADY, =0.14% | STEADY, =0.21% | STEADY, =0.40% |
| energy, GPU (J) | STEADY, under the floor (the three runs' mean 0.12%) | STEADY, =0.14% | STEADY, =0.22% | STEADY, =0.44% |
| energy per served request (J) | STEADY, under the floor (the three runs' mean 0.12%) | STEADY, =0.14% | STEADY, =0.22% | STEADY, =0.44% |
| power, GPU mean (W) | STEADY, under the floor (the three runs' mean 0.15%) | STEADY, =0.17% | STEADY, =0.14% | STEADY, =0.43% |
| requests served | STEADY, the same | STEADY, =0.00% | STEADY, =0.00% | STEADY, =0.00% |
| requests not served | STEADY, the same | — | — | — |
| response time, mean (ms) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** | LOSS, −1.87% | STEADY, =0.07% | LOSS, −0.79% |
| response time, 95th percentile (ms) | **the runs disagree** | LOSS, −3.21% | GAIN, +1.20% | STEADY, =0.38% |
| response time, 99th percentile (ms) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** | LOSS, −1.72% | STEADY, =0.25% | LOSS, −0.52% |
| temperature, peak (C) | STEADY, under the floor (the three runs' mean 0.25%) | STEADY, =0.00% | STEADY, =0.29% | power given, +1.04% |
| temperature, mean (C) | STEADY, under the floor (the three runs' mean 0.21%) | STEADY, =0.23% | STEADY, =0.34% | power given, +1.21% |
| energy, GPU device counter (J) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, +0.73% | STEADY, =0.49% | STEADY, =0.33% |
| power-capped share of samples | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** | GAIN, +6.16% | GAIN, +2.94% | GAIN, +4.25% |

Each arm's means in each run (native, then Omni-Compass on top of native):

| Run | Gauge | Native | Omni-Compass on top of native |
|---|---|---:|---:|
| A | work per energy (served requests per kJ) | 41.67 | 41.61 |
| A | requests served | 2,611.00 | 2,611.00 |
| A | requests not served | 0.00 | 0.00 |
| A | energy, GPU (J) | 62,658.96 | 62,745.32 |
| A | response time, 95th percentile (ms) | 363.41 | 375.07 |
| B | work per energy (served requests per kJ) | 44.74 | 44.84 |
| B | requests served | 2,835.00 | 2,835.00 |
| B | requests not served | 0.00 | 0.00 |
| B | energy, GPU (J) | 63,372.60 | 63,235.81 |
| B | response time, 95th percentile (ms) | 311.54 | 307.80 |
| C | work per energy (served requests per kJ) | 44.34 | 44.17 |
| C | requests served | 2,749.00 | 2,749.00 |
| C | requests not served | 0.00 | 0.00 |
| C | energy, GPU (J) | 61,994.47 | 62,264.19 |
| C | response time, 95th percentile (ms) | 315.91 | 317.12 |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
