# The card on omni-v23, the power cap at 70% of the card's top, the full load (cap-full): three runs on an A10

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three runs on rented cards (A, B and C), NVIDIA A10, 5 paired repetitions each; engine omni-v23 (digest c96ea4105d8747db, 65 files); dial: max (the card governor's dial: max, the factory tune; save, the tune-down). Runs: A 41243352339, B 41243355485, C 41243358705 (their files on the branch `raw`, `run-<id>/`). Each run's own verdict (tools/gpu_reps.py): A SUPERIOR WITHIN GUARDRAILS; B SUPERIOR WITHIN GUARDRAILS; C ENERGY IMPROVEMENT WITH SERVICE TRADEOFF.

| Gauge | Three runs | A | B | C |
|---|---|---|---|---|
| work per energy (served requests per kJ) | **GAIN in all three of our runs** | GAIN, 1.82% | GAIN, 1.37% | GAIN, 0.79% |
| energy, GPU (J) | **GAIN in all three of our runs** | STEADY, 0.31% | GAIN, 0.63% | GAIN, 1.48% |
| energy per served request (J) | **GAIN in all three of our runs** | GAIN, 1.79% | GAIN, 1.35% | GAIN, 0.78% |
| power, GPU mean (W) | **GAIN in all three of our runs** | STEADY, 0.35% | GAIN, 0.63% | GAIN, 1.47% |
| requests served | **the runs disagree** | GAIN, 1.51% | GAIN, 0.73% | LOSS, 0.70% |
| requests not served | **the runs disagree** | GAIN, 6.00% | GAIN, 3.04% | LOSS, 2.81% |
| response time, mean (ms) | **the runs disagree** | GAIN, 2.38% | GAIN, 1.89% | LOSS, 2.18% |
| response time, 95th percentile (ms) | **the runs disagree** | GAIN, 3.68% | GAIN, 1.38% | LOSS, 2.25% |
| response time, 99th percentile (ms) | **the runs disagree** | GAIN, 4.07% | GAIN, 1.86% | LOSS, 1.70% |
| temperature, peak (C) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | STEADY, 0.00% | GAIN, 0.69% | GAIN, 1.67% |
| temperature, mean (C) | STEADY, under the floor (the three runs' mean 0.05%) | STEADY, 0.29% | STEADY, 0.11% | STEADY, 0.35% |
| energy, GPU device counter (J) | **GAIN in all three of our runs** | STEADY, 0.32% | GAIN, 0.62% | GAIN, 1.53% |
| power-capped share of samples | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, 11.23% | GAIN, 2.42% | STEADY, 0.23% |

Each arm's means in each run (native, then Omni-Compass on top of native):

| Run | Gauge | Native | Omni-Compass on top of native |
|---|---|---:|---:|
| A | work per energy (served requests per kJ) | 75.47 | 76.85 |
| A | requests served | 2,616.20 | 2,655.60 |
| A | requests not served | 656.80 | 617.40 |
| A | energy, GPU (J) | 34,663.30 | 34,554.81 |
| A | response time, 95th percentile (ms) | 87,423.95 | 84,203.66 |
| B | work per energy (served requests per kJ) | 65.61 | 66.51 |
| B | requests served | 2,269.60 | 2,286.20 |
| B | requests not served | 546.40 | 529.80 |
| B | energy, GPU (J) | 34,590.73 | 34,373.64 |
| B | response time, 95th percentile (ms) | 82,650.11 | 81,508.74 |
| C | work per energy (served requests per kJ) | 65.14 | 65.65 |
| C | requests served | 2,255.20 | 2,239.40 |
| C | requests not served | 561.80 | 577.60 |
| C | energy, GPU (J) | 34,622.56 | 34,110.19 |
| C | response time, 95th percentile (ms) | 83,498.61 | 85,375.97 |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
