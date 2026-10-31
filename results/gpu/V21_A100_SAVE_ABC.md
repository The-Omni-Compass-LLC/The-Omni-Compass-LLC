# The card on omni-v21, the tune-down (dial save): three runs on an A100

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three runs on rented cards (A, B and C), NVIDIA A100-SXM4-40GB, 10 paired repetitions each; engine omni-v21 (digest b658f05d43c1e602, 63 files); dial: save (the card governor's dial: max, the factory tune; save, the tune-down). Runs: A 40485597269, B 40485602065, C 40485605739 (their files on the branch `raw`, `run-<id>/`). Each run's own verdict (tools/gpu_reps.py): A NONINFERIOR / INCONCLUSIVE; B SUPERIOR WITHIN GUARDRAILS; C NONINFERIOR / INCONCLUSIVE.

| Gauge | Three runs | A | B | C |
|---|---|---|---|---|
| work per energy (served requests per kJ) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, +0.84% | GAIN, +0.71% | GAIN, +0.69% |
| energy, GPU (J) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, +0.85% | GAIN, +0.70% | GAIN, +0.68% |
| energy per served request (J) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, +0.85% | GAIN, +0.70% | GAIN, +0.68% |
| power, GPU mean (W) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, +0.86% | GAIN, +0.70% | GAIN, +0.68% |
| requests served | STEADY, the same | STEADY, =0.00% | STEADY, =0.00% | STEADY, =0.00% |
| requests not served | STEADY, the same | — | — | — |
| response time, mean (ms) | STEADY, under the floor (the three runs' mean 0.19%) | STEADY, =0.25% | STEADY, =0.13% | STEADY, =0.19% |
| response time, 95th percentile (ms) | STEADY, under the floor (the three runs' mean 0.04%) | STEADY, =0.03% | STEADY, =0.10% | STEADY, =0.04% |
| response time, 99th percentile (ms) | STEADY, under the floor (the three runs' mean 0.02%) | STEADY, =0.06% | STEADY, =0.24% | STEADY, =0.12% |
| temperature, peak (C) | STEADY, under the floor (the three runs' mean 0.22%) | power given, +0.79% | STEADY, =0.00% | STEADY, =0.14% |
| temperature, mean (C) | **the runs disagree** | power given, +0.77% | STEADY, =0.36% | GAIN, +0.52% |
| energy, GPU device counter (J) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** | STEADY, =0.33% | GAIN, +0.84% | GAIN, +1.15% |
| power-capped share of samples | **GAIN in all three of our runs** | GAIN, +7.00% | GAIN, +16.90% | GAIN, +18.23% |

Each arm's means in each run (native, then Omni-Compass on top of native):

| Run | Gauge | Native | Omni-Compass on top of native |
|---|---|---:|---:|
| A | work per energy (served requests per kJ) | 43.52 | 43.88 |
| A | requests served | 6,843.00 | 6,843.00 |
| A | requests not served | 0.00 | 0.00 |
| A | energy, GPU (J) | 157,325.42 | 155,983.00 |
| A | response time, 95th percentile (ms) | 264.84 | 264.91 |
| B | work per energy (served requests per kJ) | 41.53 | 41.83 |
| B | requests served | 6,458.00 | 6,458.00 |
| B | requests not served | 0.00 | 0.00 |
| B | energy, GPU (J) | 155,498.60 | 154,408.72 |
| B | response time, 95th percentile (ms) | 241.25 | 241.02 |
| C | work per energy (served requests per kJ) | 42.09 | 42.38 |
| C | requests served | 6,502.00 | 6,502.00 |
| C | requests not served | 0.00 | 0.00 |
| C | energy, GPU (J) | 154,478.19 | 153,426.05 |
| C | response time, 95th percentile (ms) | 245.72 | 245.61 |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
