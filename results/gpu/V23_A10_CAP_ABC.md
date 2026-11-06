# The card on omni-v23, the power cap at 70% of the card's top (cap): three runs on an A10

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three runs on rented cards (A, B and C), NVIDIA A10, 5 paired repetitions each; engine omni-v23 (digest c96ea4105d8747db, 65 files); dial: max (the card governor's dial: max, the factory tune; save, the tune-down). Runs: A 41243352339, B 41243355485, C 41243358705 (their files on the branch `raw`, `run-<id>/`). Each run's own verdict (tools/gpu_reps.py): A NONINFERIOR / INCONCLUSIVE; B SUPERIOR WITHIN GUARDRAILS; C NONINFERIOR / INCONCLUSIVE.

| Gauge | Three runs | A | B | C |
|---|---|---|---|---|
| work per energy (served requests per kJ) | STEADY, under the floor (the three runs' mean 0.38%) | STEADY, 0.36% | GAIN, 0.61% | STEADY, 0.19% |
| energy, GPU (J) | STEADY, under the floor (the three runs' mean 0.38%) | STEADY, 0.35% | GAIN, 0.60% | STEADY, 0.18% |
| energy per served request (J) | STEADY, under the floor (the three runs' mean 0.38%) | STEADY, 0.35% | GAIN, 0.60% | STEADY, 0.18% |
| power, GPU mean (W) | STEADY, under the floor (the three runs' mean 0.42%) | STEADY, 0.48% | GAIN, 0.60% | STEADY, 0.19% |
| requests served | STEADY, the same | STEADY, 0.00% | STEADY, 0.00% | STEADY, 0.00% |
| requests not served | STEADY, the same | — | — | — |
| response time, mean (ms) | **the runs disagree** | GAIN, 1.08% | GAIN, 0.50% | LOSS, 2.20% |
| response time, 95th percentile (ms) | **the runs disagree** | GAIN, 2.67% | GAIN, 3.31% | LOSS, 1.95% |
| response time, 99th percentile (ms) | **the runs disagree** | GAIN, 3.83% | GAIN, 2.15% | LOSS, 2.74% |
| temperature, peak (C) | STEADY, under the floor (the three runs' mean 0.38%) | STEADY, 0.00% | GAIN, 0.76% | STEADY, 0.37% |
| temperature, mean (C) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** | GAIN, 0.65% | GAIN, 0.53% | STEADY, 0.46% |
| energy, GPU device counter (J) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** | STEADY, 0.37% | GAIN, 0.72% | STEADY, 0.45% |
| power-capped share of samples | **GAIN in all three of our runs** | GAIN, 2.63% | GAIN, 2.47% | GAIN, 2.25% |

Each arm's means in each run (native, then Omni-Compass on top of native):

| Run | Gauge | Native | Omni-Compass on top of native |
|---|---|---:|---:|
| A | work per energy (served requests per kJ) | 37.54 | 37.68 |
| A | requests served | 1,032.00 | 1,032.00 |
| A | requests not served | 0.00 | 0.00 |
| A | energy, GPU (J) | 27,490.26 | 27,392.80 |
| A | response time, 95th percentile (ms) | 730.22 | 710.71 |
| B | work per energy (served requests per kJ) | 37.97 | 38.20 |
| B | requests served | 1,023.00 | 1,023.00 |
| B | requests not served | 0.00 | 0.00 |
| B | energy, GPU (J) | 26,945.62 | 26,783.45 |
| B | response time, 95th percentile (ms) | 862.30 | 833.72 |
| C | work per energy (served requests per kJ) | 41.87 | 41.95 |
| C | requests served | 1,134.00 | 1,134.00 |
| C | requests not served | 0.00 | 0.00 |
| C | energy, GPU (J) | 27,085.43 | 27,036.12 |
| C | response time, 95th percentile (ms) | 681.47 | 694.77 |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
