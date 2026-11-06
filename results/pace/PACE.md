# The heartbeat dial on real Kubernetes: every beat against native and against the factory beat (omni-v25, three runs)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The decision pace's real runs (`docs/PACE_PREREGISTRATION.md`, amendment 3; `scripts/reruns.txt`, "kubernetes decision pace"): the steady load, native and Omni-Compass on top of native at the factory beat (10 s on site since omni-v24) and at 5, 15, 30, 75, 90 and 120 s, every arm in every repetition, ten paired repetitions a run, three runs (A, B and C) on GitHub's machines, class L. A beat other than the factory's is a changed tune: its readings show the engine's range, never a benchmark result (the founder's order of 22 October), and every row of every table is shown, LOSS included. Each table was written by `tools/confirm_abc.py --pair` from the archived runs on the branch `raw`; each reading is the one key's (`tools/readings.py`).

| Beat | Against | GAIN | LOSS | power given | STEADY | runs disagree | Table |
|---:|---|---:|---:|---:|---:|---:|---|
| 5 s | native | 7 | 0 | 1 | 7 | 1 | [V25_PACE_5.md](V25_PACE_5.md) |
| 5 s | the factory beat (10 s) | 1 | 2 | 0 | 7 | 6 | [V25_PACE_5_VS_FACTORY.md](V25_PACE_5_VS_FACTORY.md) |
| 15 s | native | 8 | 0 | 1 | 7 | 0 | [V25_PACE_15.md](V25_PACE_15.md) |
| 15 s | the factory beat (10 s) | 5 | 0 | 0 | 7 | 4 | [V25_PACE_15_VS_FACTORY.md](V25_PACE_15_VS_FACTORY.md) |
| 30 s | native | 8 | 0 | 0 | 7 | 1 | [V25_PACE_30.md](V25_PACE_30.md) |
| 30 s | the factory beat (10 s) | 6 | 0 | 0 | 7 | 3 | [V25_PACE_30_VS_FACTORY.md](V25_PACE_30_VS_FACTORY.md) |
| 75 s | native | 9 | 0 | 0 | 7 | 0 | [V25_PACE_75.md](V25_PACE_75.md) |
| 75 s | the factory beat (10 s) | 6 | 0 | 0 | 7 | 3 | [V25_PACE_75_VS_FACTORY.md](V25_PACE_75_VS_FACTORY.md) |
| 90 s | native | 8 | 0 | 0 | 7 | 1 | [V25_PACE_90.md](V25_PACE_90.md) |
| 90 s | the factory beat (10 s) | 6 | 0 | 0 | 7 | 3 | [V25_PACE_90_VS_FACTORY.md](V25_PACE_90_VS_FACTORY.md) |
| 120 s | native | 8 | 0 | 0 | 7 | 1 | [V25_PACE_120.md](V25_PACE_120.md) |
| 120 s | the factory beat (10 s) | 6 | 0 | 0 | 7 | 3 | [V25_PACE_120_VS_FACTORY.md](V25_PACE_120_VS_FACTORY.md) |

The runs: A [41751100166](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/41751100166), B [41767230735](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/41767230735), C [41780364813](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/41780364813).

## The rows a reader looks at first

### 5 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.11%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN in all three of our runs |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN in all three of our runs |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |

### 5 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.03%) |
| response time (ms), 95th percentile | LOSS by the mean of our three runs, beyond the noise in 1 of 3 |
| time over the response line (% of samples) | the runs disagree |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | the runs disagree |

### 15 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.08%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN in all three of our runs |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN in all three of our runs |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |

### 15 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.00%) |
| response time (ms), 95th percentile | the runs disagree |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | the runs disagree |

### 30 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.00%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN in all three of our runs |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN in all three of our runs |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |

### 30 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.08%) |
| response time (ms), 95th percentile | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | the runs disagree |

### 75 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.01%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN in all three of our runs |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN in all three of our runs |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |

### 75 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.09%) |
| response time (ms), 95th percentile | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | the runs disagree |

### 90 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.03%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN in all three of our runs |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN in all three of our runs |
| pod start wait, total (s) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |

### 90 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.05%) |
| response time (ms), 95th percentile | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | the runs disagree |

### 120 s against native

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.04%) |
| response time (ms), 95th percentile | GAIN in all three of our runs |
| time over the response line (% of samples) | GAIN in all three of our runs |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN in all three of our runs |
| pod start wait, total (s) | GAIN in all three of our runs |

### 120 s against the factory beat (10 s)

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | STEADY, the same |
| node-hours | STEADY, under the floor (the three runs' mean 0.03%) |
| response time (ms), 95th percentile | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| time over the response line (% of samples) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| pod start wait, total (s) | the runs disagree |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
