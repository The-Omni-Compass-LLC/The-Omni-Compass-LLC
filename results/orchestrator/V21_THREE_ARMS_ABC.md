# Omni direct's three arms: three runs on GitHub's machines

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni direct's three arms, three runs on GitHub's own machines (A, B and C from one commit), the full form: 18 steps of 25 s, clients 1 2 3 2 3 4 ..., the busy room rule. Commit `9d2bea96a878`, engine omni-v21 (digest b658f05d43c1e602, 63 files); runs A 40474220398, B 40474223636, C 40474227699 (their files on the branch `raw`, `run-<id>/`). Native is Kubernetes' published autoscaling rule on the muscles, written by us; Omni on native is Omni-Compass on top of that rule; Omni direct is Omni-Compass alone on the muscles, no Kubernetes. Each run reads every pair by the one key, paired by step; the three runs are combined by the one rule (tools/readings.py, the founder's order of 24 October 2026): a change of 0.5% or more, the mean of the three runs, reads GAIN, LOSS or power given by the gauge's aim, in all three of our runs where every run moved the same way clear of zero, otherwise by the mean of our three runs with the count of runs beyond the noise; STEADY under 0.5%; the runs disagree when runs moved 0.5% or more in opposite directions. Each run's own word stands beside its number by the same floor.

| Pair | Gauge | Three runs | A | B | C |
|---|---|---|---|---|---|
| Omni on native against native | Work (requests a step) | **GAIN in all three of our runs** | GAIN, up 10.3% | GAIN, up 8.2% | GAIN, up 7.0% |
| Omni on native against native | The 95th percentile (ms) | **GAIN in all three of our runs** | GAIN, down 12.6% | GAIN, down 14.2% | GAIN, down 12.0% |
| Omni on native against native | Machines | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, down 2.0% | GAIN, down 2.8% | GAIN, down 4.8% |
| Omni on native against native | Units | **power given by the mean of our three runs, beyond the noise in 1 of 3** | power given, up 3.3% | power given, up 5.0% | power given, up 3.7% |
| Omni direct against native | Work (requests a step) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** | GAIN, up 10.0% | GAIN, up 5.3% | GAIN, up 2.8% |
| Omni direct against native | The 95th percentile (ms) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** | GAIN, down 14.3% | GAIN, down 7.6% | GAIN, down 7.6% |
| Omni direct against native | Machines | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** | GAIN, down 3.0% | GAIN, down 2.8% | GAIN, down 2.6% |
| Omni direct against native | Units | **power given by the mean of our three runs, beyond the noise in 1 of 3** | power given, up 4.6% | power given, up 4.0% | power given, up 1.8% |
| Omni direct against Omni on native | Work (requests a step) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** | STEADY, down 0.3% | LOSS, down 2.6% | LOSS, down 4.0% |
| Omni direct against Omni on native | The 95th percentile (ms) | **the runs disagree** | GAIN, down 2.0% | LOSS, up 7.8% | LOSS, up 5.0% |
| Omni direct against Omni on native | Machines | **the runs disagree** | GAIN, down 0.9% | STEADY, unchanged | power given, up 2.3% |
| Omni direct against Omni on native | Units | **the runs disagree** | power given, up 1.3% | GAIN, down 1.0% | GAIN, down 1.9% |

Each arm's totals in each run (requests answered, failed, wrong, the 95th percentile in ms, machine-minutes, unit-minutes):

| Run | Arm | Answered | Failed | Wrong | 95th percentile (ms) | Machine-minutes | Unit-minutes |
|---|---|---:|---:|---:|---:|---:|---:|
| A | native | 10,113 | 0 | 0 | 171.8 | 45.0 | 59.6 |
| A | Omni on native | 11,156 | 0 | 0 | 142.6 | 44.1 | 61.5 |
| A | Omni direct | 11,120 | 0 | 0 | 146.5 | 43.7 | 62.3 |
| A | the batch job beside the service | 2,429 | 0 | 0 | 165.0 | 12.0 | 17.8 |
| A | the drills | 3,574 | 0 | 0 | 200.8 | 14.5 | 20.7 |
| B | native | 9,254 | 0 | 0 | 203.7 | 45.0 | 60.3 |
| B | Omni on native | 10,008 | 0 | 0 | 191.2 | 43.8 | 63.4 |
| B | Omni direct | 9,749 | 0 | 0 | 192.0 | 43.8 | 62.8 |
| B | the batch job beside the service | 2,219 | 0 | 0 | 203.1 | 12.0 | 17.5 |
| B | the drills | 3,170 | 0 | 0 | 223.7 | 14.5 | 20.1 |
| C | native | 9,160 | 0 | 0 | 202.7 | 45.0 | 61.1 |
| C | Omni on native | 9,803 | 0 | 0 | 196.4 | 42.8 | 63.3 |
| C | Omni direct | 9,413 | 0 | 0 | 210.4 | 43.8 | 62.1 |
| C | the batch job beside the service | 2,174 | 0 | 0 | 205.7 | 12.0 | 19.2 |
| C | the drills | 3,306 | 0 | 0 | 209.9 | 14.5 | 19.6 |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
