# Omni direct's three arms: three runs on GitHub's machines

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni direct's three arms, three runs on GitHub's own machines (A, B and C from one commit), the full form: 18 steps of 25 s, clients 1 2 3 2 3 4 ..., the busy room rule. Commit `0ca2bbdac97f`, engine omni-v18 (digest 1cb92edb64c4391d, 62 files); runs A 40023524338, B 40023529155, C 40023534013 (their files on the branch `raw`, `run-<id>/`). Native is Kubernetes' published autoscaling rule on the muscles, written by us; Omni on native is Omni-Compass on top of that rule; Omni direct is Omni-Compass alone on the muscles, no Kubernetes. Each run reads every pair by the one key, paired by step; the three runs are combined by the one rule (tools/readings.py, the founder's order of 24 October 2026): a change of 0.5% or more, the mean of the three runs, reads GAIN, LOSS or power given by the gauge's aim, in all three of our runs where every run moved the same way clear of zero, otherwise by the mean of our three runs with the count of runs beyond the noise; STEADY under 0.5%; the runs disagree when runs moved 0.5% or more in opposite directions. Each run's own word stands beside its number by the same floor.

| Pair | Gauge | Three runs | A | B | C |
|---|---|---|---|---|---|
| Omni on native against native | Work (requests a step) | **GAIN in all three of our runs** | GAIN, up 5.2% | GAIN, up 5.3% | GAIN, up 7.4% |
| Omni on native against native | The 95th percentile (ms) | **GAIN in all three of our runs** | GAIN, down 9.0% | GAIN, down 12.1% | GAIN, down 7.5% |
| Omni on native against native | Machines | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, down 2.2% | GAIN, down 4.6% | GAIN, down 2.4% |
| Omni on native against native | Units | **power given in all three of our runs** | power given, up 11.0% | power given, up 8.9% | power given, up 10.8% |
| Omni direct against native | Work (requests a step) | **GAIN in all three of our runs** | GAIN, up 7.3% | GAIN, up 5.7% | GAIN, up 9.4% |
| Omni direct against native | The 95th percentile (ms) | **GAIN in all three of our runs** | GAIN, down 9.8% | GAIN, down 15.7% | GAIN, down 10.8% |
| Omni direct against native | Machines | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** | GAIN, down 2.2% | GAIN, down 3.1% | GAIN, down 2.2% |
| Omni direct against native | Units | **power given by the mean of our three runs, beyond the noise in 2 of 3** | power given, up 6.9% | STEADY, down 0.3% | power given, up 9.0% |
| Omni direct against Omni on native | Work (requests a step) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, up 2.0% | STEADY, up 0.4% | GAIN, up 1.9% |
| Omni direct against Omni on native | The 95th percentile (ms) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** | GAIN, down 0.9% | GAIN, down 4.0% | GAIN, down 3.6% |
| Omni direct against Omni on native | Machines | **power given by the mean of our three runs, beyond the noise in 0 of 3** | STEADY, unchanged | power given, up 1.6% | STEADY, up 0.2% |
| Omni direct against Omni on native | Units | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, down 3.7% | GAIN, down 8.5% | GAIN, down 1.7% |

Each arm's totals in each run (requests answered, failed, wrong, the 95th percentile in ms, machine-minutes, unit-minutes):

| Run | Arm | Answered | Failed | Wrong | 95th percentile (ms) | Machine-minutes | Unit-minutes |
|---|---|---:|---:|---:|---:|---:|---:|
| A | native | 9,128 | 0 | 0 | 205.0 | 45.0 | 59.8 |
| A | Omni on native | 9,603 | 0 | 0 | 202.3 | 44.0 | 66.4 |
| A | Omni direct | 9,797 | 0 | 0 | 194.0 | 44.0 | 64.0 |
| A | the batch job beside the service | 2,180 | 0 | 0 | 199.7 | 12.0 | 18.4 |
| A | the drills | 3,091 | 0 | 0 | 295.8 | 14.5 | 20.4 |
| B | native | 11,202 | 0 | 0 | 135.7 | 45.0 | 57.1 |
| B | Omni on native | 11,796 | 0 | 0 | 124.1 | 42.9 | 62.2 |
| B | Omni direct | 11,839 | 0 | 0 | 117.7 | 43.6 | 56.9 |
| B | the batch job beside the service | 2,606 | 0 | 0 | 136.8 | 12.0 | 18.7 |
| B | the drills | 3,899 | 0 | 0 | 156.9 | 14.5 | 19.8 |
| C | native | 9,159 | 0 | 0 | 203.4 | 45.0 | 58.8 |
| C | Omni on native | 9,838 | 0 | 0 | 197.3 | 43.9 | 65.2 |
| C | Omni direct | 10,022 | 0 | 0 | 188.3 | 44.0 | 64.1 |
| C | the batch job beside the service | 2,083 | 0 | 0 | 210.7 | 12.0 | 18.0 |
| C | the drills | 3,342 | 0 | 0 | 208.0 | 14.5 | 18.6 |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
