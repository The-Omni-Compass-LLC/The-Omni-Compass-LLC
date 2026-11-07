# The card's compute run on omni-v23: an A10 at the usual load, the firmware alone against Omni-Compass on top, three runs on rented cards

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three runs on rented cards (A, B and C), NVIDIA A10, 10 paired repetitions each; engine omni-v23 (digest c96ea4105d8747db, 65 files); dial: max (the card governor's dial: max, the factory tune; save, the tune-down). Runs: A 41243361994, B 41243364991, C 41243368008 (their files on the branch `raw`, `run-<id>/`). Each run's own verdict (tools/gpu_reps.py): A NONINFERIOR / INCONCLUSIVE; B NONINFERIOR / INCONCLUSIVE; C NONINFERIOR / INCONCLUSIVE.

| Gauge | Three runs | A | B | C |
|---|---|---|---|---|
| work per energy (served requests per kJ) | STEADY, under the floor (the three runs' mean 0.13%) | STEADY, 0.28% | STEADY, 0.04% | STEADY, 0.16% |
| energy, GPU (J) | STEADY, under the floor (the three runs' mean 0.13%) | STEADY, 0.28% | STEADY, 0.04% | STEADY, 0.15% |
| energy per served request (J) | STEADY, under the floor (the three runs' mean 0.13%) | STEADY, 0.28% | STEADY, 0.04% | STEADY, 0.15% |
| power, GPU mean (W) | STEADY, under the floor (the three runs' mean 0.13%) | STEADY, 0.28% | STEADY, 0.03% | STEADY, 0.15% |
| requests served | STEADY, the same | STEADY, 0.00% | STEADY, 0.00% | STEADY, 0.00% |
| requests not served | STEADY, the same | — | — | — |
| response time, mean (ms) | STEADY, under the floor (the three runs' mean 0.06%) | STEADY, 0.41% | STEADY, 0.02% | STEADY, 0.20% |
| response time, 95th percentile (ms) | **the runs disagree** | GAIN, 0.90% | STEADY, 0.12% | LOSS, 0.80% |
| response time, 99th percentile (ms) | STEADY, under the floor (the three runs' mean 0.25%) | STEADY, 0.20% | STEADY, 0.02% | LOSS, 0.97% |
| temperature, peak (C) | STEADY, under the floor (the three runs' mean 0.09%) | STEADY, 0.14% | STEADY, 0.00% | STEADY, 0.14% |
| temperature, mean (C) | STEADY, under the floor (the three runs' mean 0.08%) | STEADY, 0.20% | STEADY, 0.00% | STEADY, 0.03% |
| energy, GPU device counter (J) | STEADY, under the floor (the three runs' mean 0.02%) | STEADY, 0.10% | STEADY, 0.04% | STEADY, 0.00% |
| power-capped share of samples | STEADY, under the floor (the three runs' mean 0.08%) | STEADY, 0.14% | STEADY, 0.03% | STEADY, 0.08% |

Each arm's means in each run (native, then Omni-Compass on top of native):

| Run | Gauge | Native | Omni-Compass on top of native |
|---|---|---:|---:|
| A | work per energy (served requests per kJ) | 54.98 | 55.13 |
| A | requests served | 3,792.00 | 3,792.00 |
| A | requests not served | 0.00 | 0.00 |
| A | energy, GPU (J) | 68,975.89 | 68,780.88 |
| A | response time, 95th percentile (ms) | 475.21 | 470.94 |
| B | work per energy (served requests per kJ) | 60.10 | 60.08 |
| B | requests served | 4,043.00 | 4,043.00 |
| B | requests not served | 0.00 | 0.00 |
| B | energy, GPU (J) | 67,268.04 | 67,295.31 |
| B | response time, 95th percentile (ms) | 418.80 | 419.29 |
| C | work per energy (served requests per kJ) | 61.35 | 61.44 |
| C | requests served | 4,146.00 | 4,146.00 |
| C | requests not served | 0.00 | 0.00 |
| C | energy, GPU (J) | 67,583.92 | 67,479.62 |
| C | response time, 95th percentile (ms) | 428.63 | 432.04 |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
