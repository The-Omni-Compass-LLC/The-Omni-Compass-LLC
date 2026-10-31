# The card on omni-v21, the power cap at 70% of the card's top (cap-full): three runs on an A100

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three runs on rented cards (A, B and C), NVIDIA A100-SXM4-40GB, 5 paired repetitions each; engine omni-v21 (digest b658f05d43c1e602, 63 files); dial: max (the card governor's dial: max, the factory tune; save, the tune-down). Runs: A 40485609401, B 40485613546, C 40485617318 (their files on the branch `raw`, `run-<id>/`). Each run's own verdict (tools/gpu_reps.py): A NOT ESTABLISHED; B NONINFERIOR / INCONCLUSIVE; C NONINFERIOR / INCONCLUSIVE.

| Gauge | Three runs | A | B | C |
|---|---|---|---|---|
| work per energy (served requests per kJ) | STEADY, under the floor (the three runs' mean 0.07%) | STEADY, =0.03% | STEADY, =0.23% | STEADY, =0.02% |
| energy, GPU (J) | STEADY, under the floor (the three runs' mean 0.23%) | STEADY, =0.43% | STEADY, =0.21% | STEADY, =0.04% |
| energy per served request (J) | STEADY, under the floor (the three runs' mean 0.07%) | STEADY, =0.03% | STEADY, =0.23% | STEADY, =0.02% |
| power, GPU mean (W) | STEADY, under the floor (the three runs' mean 0.26%) | STEADY, =0.47% | STEADY, =0.25% | STEADY, =0.04% |
| requests served | STEADY, under the floor (the three runs' mean 0.15%) | STEADY, =0.46% | STEADY, =0.03% | STEADY, =0.02% |
| requests not served | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** | LOSS, −2.18% | STEADY, =0.13% | STEADY, =0.11% |
| response time, mean (ms) | STEADY, under the floor (the three runs' mean 0.47%) | LOSS, −1.32% | STEADY, =0.12% | STEADY, =0.03% |
| response time, 95th percentile (ms) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** | LOSS, −1.50% | STEADY, =0.06% | STEADY, =0.11% |
| response time, 99th percentile (ms) | STEADY, under the floor (the three runs' mean 0.50%) | LOSS, −1.43% | STEADY, =0.03% | STEADY, =0.09% |
| temperature, peak (C) | STEADY, under the floor (the three runs' mean 0.23%) | power given, +1.00% | STEADY, =0.30% | STEADY, =0.00% |
| temperature, mean (C) | STEADY, under the floor (the three runs' mean 0.25%) | STEADY, =0.44% | GAIN, +1.31% | STEADY, =0.13% |
| energy, GPU device counter (J) | STEADY, under the floor (the three runs' mean 0.23%) | STEADY, =0.45% | STEADY, =0.24% | STEADY, =0.01% |
| power-capped share of samples | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** | GAIN, +58.31% | GAIN, +25.41% | STEADY, =0.07% |

Each arm's means in each run (native, then Omni-Compass on top of native):

| Run | Gauge | Native | Omni-Compass on top of native |
|---|---|---:|---:|
| A | work per energy (served requests per kJ) | 62.36 | 62.34 |
| A | requests served | 5,765.00 | 5,738.20 |
| A | requests not served | 1,232.00 | 1,258.80 |
| A | energy, GPU (J) | 92,451.28 | 92,050.10 |
| A | response time, 95th percentile (ms) | 77,938.00 | 79,109.35 |
| B | work per energy (served requests per kJ) | 68.23 | 68.38 |
| B | requests served | 6,296.20 | 6,297.80 |
| B | requests not served | 1,207.80 | 1,206.20 |
| B | energy, GPU (J) | 92,286.00 | 92,096.59 |
| B | response time, 95th percentile (ms) | 73,001.85 | 73,042.79 |
| C | work per energy (served requests per kJ) | 65.86 | 65.87 |
| C | requests served | 6,101.00 | 6,099.60 |
| C | requests not served | 1,220.00 | 1,221.40 |
| C | energy, GPU (J) | 92,638.28 | 92,600.76 |
| C | response time, 95th percentile (ms) | 73,845.85 | 73,926.52 |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
