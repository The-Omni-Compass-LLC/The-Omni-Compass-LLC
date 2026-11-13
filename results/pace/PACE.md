# The heartbeat dial on real Kubernetes: every beat against native and against the factory beat (omni-v26, three runs)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The decision pace's real runs (`docs/PACE_PREREGISTRATION.md`, amendment 3; `scripts/reruns.txt`, "kubernetes decision pace"): the steady load, native and Omni-Compass on top of native at the factory beat (10 s on site since omni-v24) and at 5, 15, 30, 75, 90 and 120 s, every arm in every repetition, ten paired repetitions a run, three runs (A, B and C) on GitHub's machines, class L. A beat other than the factory's is a changed tune: its readings show the engine's range, never a benchmark result (the founder's order of 22 October), and every row of every table is shown, LOSS included. Each table was written by `tools/confirm_abc.py --pair` from the archived runs on the branch `raw`; each reading is the one key's (`tools/readings.py`); this page is written from the tables by `tools/pace_index.py`.

| Beat | Against | GAIN | LOSS | power given | STEADY | runs disagree | Table |
|---:|---|---:|---:|---:|---:|---:|---|
| 5 s | native | 8 | 0 | 0 | 7 | 1 | [V26_PACE_5.md](V26_PACE_5.md) |
| 5 s | the factory beat (10 s) | 0 | 1 | 0 | 8 | 7 | [V26_PACE_5_VS_FACTORY.md](V26_PACE_5_VS_FACTORY.md) |
| 15 s | native | 7 | 0 | 1 | 7 | 1 | [V26_PACE_15.md](V26_PACE_15.md) |
| 15 s | the factory beat (10 s) | 3 | 2 | 0 | 8 | 3 | [V26_PACE_15_VS_FACTORY.md](V26_PACE_15_VS_FACTORY.md) |
| 30 s | native | 8 | 1 | 0 | 7 | 0 | [V26_PACE_30.md](V26_PACE_30.md) |
| 30 s | the factory beat (10 s) | 5 | 1 | 0 | 9 | 1 | [V26_PACE_30_VS_FACTORY.md](V26_PACE_30_VS_FACTORY.md) |
| 75 s | native | 8 | 0 | 0 | 7 | 1 | [V26_PACE_75.md](V26_PACE_75.md) |
| 75 s | the factory beat (10 s) | 5 | 2 | 0 | 8 | 1 | [V26_PACE_75_VS_FACTORY.md](V26_PACE_75_VS_FACTORY.md) |
| 90 s | native | 9 | 0 | 0 | 7 | 0 | [V26_PACE_90.md](V26_PACE_90.md) |
| 90 s | the factory beat (10 s) | 5 | 0 | 0 | 9 | 2 | [V26_PACE_90_VS_FACTORY.md](V26_PACE_90_VS_FACTORY.md) |
| 120 s | native | 7 | 0 | 0 | 7 | 2 | [V26_PACE_120.md](V26_PACE_120.md) |
| 120 s | the factory beat (10 s) | 4 | 1 | 0 | 8 | 3 | [V26_PACE_120_VS_FACTORY.md](V26_PACE_120_VS_FACTORY.md) |

The runs: A [42406250358](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42406250358), B [42415410932](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42415410932), C [42426638780](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42426638780); every one on omni-v26 (digest 75d3c22eed4473b9, 65 files).

## The rows a reader looks at first

### 5 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.03%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |

### 5 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.07%) |
| response time (ms), 95th percentile | the runs disagree |
| time over the response line (% of samples) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | STEADY, the same |
| pod start wait, total (s) | the runs disagree |

### 15 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.06%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |

### 15 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.03%) |
| response time (ms), 95th percentile | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| time over the response line (% of samples) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | STEADY, the same |
| pod start wait, total (s) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |

### 30 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.10%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |

### 30 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.00%) |
| response time (ms), 95th percentile | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| time over the response line (% of samples) | STEADY, the same |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | STEADY, the same |
| pod start wait, total (s) | the runs disagree |

### 75 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.03%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |

### 75 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.06%) |
| response time (ms), 95th percentile | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| time over the response line (% of samples) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | STEADY, the same |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |

### 90 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.00%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |

### 90 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.09%) |
| response time (ms), 95th percentile | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| time over the response line (% of samples) | STEADY, the same |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | STEADY, the same |
| pod start wait, total (s) | the runs disagree |

### 120 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.04%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | the runs disagree |

### 120 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.05%) |
| response time (ms), 95th percentile | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| time over the response line (% of samples) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | STEADY, the same |
| pod start wait, total (s) | the runs disagree |

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
