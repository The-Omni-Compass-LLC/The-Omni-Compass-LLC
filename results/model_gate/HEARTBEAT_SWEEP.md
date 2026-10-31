# The heartbeat sweep: a decision every 5, 10, 15, 20, 30, 60, 75, 90 and 120 seconds

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Our own model (evidence class S): what each beat of the governor does against native, in the cloud and on-site, and what it costs the engine; never a benchmark result. The founder's questions of 22 October: does a decision every 10 or 5 seconds do better than 15, is 20 different, what does a faster beat cost, and what a beat slower than 60 seconds does (75, 90 and 120), to show whether, and why, it gains or loses. Run by `tools/heartbeat_sweep.py` (the shipped controller of each checkout on one 5-second plant, eight seeds of a day each, paired by seed; each row named by the engine it ran on: omni-v16, omni-v15). Each reading is the gate's rule (`tools/model_gate.py`): the mean change over the seeds with its 95% interval, the word by the gauge's aim (`tools/readings.py`). The engine's own cost is a mean a day: its decisions, its processor time, its reads of the cluster and its writes; the fast check's rescues are the pool commands its 5-second check wrote because a pod already waited for a place, apart from the full decision's own, which size the pool ahead of the load (`rescues`). Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## On-site: native is the pod autoscaler with the cluster autoscaler; with Omni-Compass the governor sizes the pool on top of the pod autoscaler (the max)

### omni-v16 against native

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line | Decisions a day | Governor CPU a day | Cluster reads a day | Writes a day | The fast check's rescues a day |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 s | 3.8% power given | 2.8% power given | 83.5% GAIN | 0.3% STEADY | 2.1% GAIN | identical | 17,280 | 51.7 s | 86,412 | 906 | 0.0 |
| 10 s | 3.4% power given | 2.5% power given | 83.5% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 8,640 | 36.1 s | 60,540 | 547 | 0.0 |
| 15 s | 2.9% power given | 2.2% power given | 83.5% GAIN | 0.3% STEADY | 2.1% GAIN | identical | 5,760 | 31.4 s | 51,915 | 420 | 0.0 |
| 20 s | 2.7% power given | 2.0% power given | 79.8% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 4,320 | 28.5 s | 47,616 | 350 | 0.0 |
| 30 s | 1.6% power given | 1.3% power given | 80.7% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 2,880 | 26.2 s | 43,306 | 264 | 0.1 |
| 60 s | 0.3% STEADY | 0.4% STEADY | 72.9% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 1,440 | 23.6 s | 39,026 | 190 | 0.4 |
| 75 s | 0.0% STEADY | 0.2% STEADY | 69.3% GAIN | 0.2% STEADY | 1.8% GAIN | identical | 1,152 | 22.7 s | 38,144 | 177 | 0.8 |
| 90 s | 0.1% STEADY | 0.1% STEADY | 63.1% GAIN | 0.2% STEADY | 1.8% GAIN | identical | 960 | 22.3 s | 37,522 | 130 | 1.4 |
| 120 s | 0.2% STEADY | 0.1% STEADY | 57.0% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 720 | 21.7 s | 36,733 | 120 | 3.0 |

#### omni-v16 at each beat against itself at 15 s (the factory's beat)

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | 0.9% power given | 0.6% power given | identical | identical | identical | identical |
| 10 s | 0.5% STEADY | 0.3% STEADY | 0.2% STEADY | 0.0% STEADY | 0.0% STEADY | identical |
| 20 s | 0.3% STEADY | 0.2% STEADY | 22.2% LOSS | 0.0% STEADY | 0.0% STEADY | identical |
| 30 s | 1.3% GAIN | 0.9% GAIN | 16.4% LOSS | 0.0% STEADY | 0.0% STEADY | identical |
| 60 s | 2.6% GAIN | 1.7% GAIN | 63.7% LOSS | 0.0% STEADY | 0.0% STEADY | identical |
| 75 s | 2.8% GAIN | 1.9% GAIN | 85.5% LOSS | 0.0% STEADY | 0.3% STEADY | identical |
| 90 s | 2.9% GAIN | 2.0% GAIN | 122.9% LOSS | 0.0% STEADY | 0.3% STEADY | identical |
| 120 s | 3.0% GAIN | 2.1% GAIN | 160.1% LOSS | 0.0% STEADY | 0.0% STEADY | identical |

#### omni-v16 at each beat against itself at 60 s

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | 3.5% power given | 2.3% power given | 38.9% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 10 s | 3.1% power given | 2.0% power given | 39.1% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 15 s | 2.6% power given | 1.7% power given | 38.9% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 20 s | 2.4% power given | 1.6% power given | 25.4% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 30 s | 1.3% power given | 0.8% power given | 28.9% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 75 s | 0.3% STEADY | 0.2% STEADY | 13.3% LOSS | 0.0% STEADY | 0.3% STEADY | identical |
| 90 s | 0.4% STEADY | 0.3% STEADY | 36.2% LOSS | 0.0% STEADY | 0.3% STEADY | identical |
| 120 s | 0.5% STEADY | 0.4% STEADY | 58.8% LOSS | 0.0% STEADY | identical | identical |

### omni-v15 against native

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line | Decisions a day | Governor CPU a day | Cluster reads a day | Writes a day | The fast check's rescues a day |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 s | 1.1% GAIN | 0.6% GAIN | 87.4% GAIN | 0.3% STEADY | 2.1% GAIN | identical | 17,280 | 50.6 s | 86,412 | 1,013 | 0.0 |
| 10 s | 0.1% STEADY | 0.1% STEADY | 86.5% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 8,640 | 35.7 s | 60,530 | 598 | 0.0 |
| 15 s | 0.8% power given | 0.8% power given | 87.4% GAIN | 0.3% STEADY | 2.1% GAIN | identical | 5,760 | 30.6 s | 51,899 | 459 | 0.0 |
| 20 s | 1.2% power given | 1.1% power given | 83.0% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 4,320 | 28.3 s | 47,601 | 380 | 0.0 |
| 30 s | 1.4% power given | 1.2% power given | 83.7% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 2,880 | 25.7 s | 43,290 | 281 | 0.1 |
| 60 s | 0.3% STEADY | 0.4% STEADY | 72.9% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 1,440 | 23.3 s | 39,026 | 190 | 0.4 |
| 75 s | 0.3% STEADY | 0.3% STEADY | 69.3% GAIN | 0.2% STEADY | 1.8% GAIN | identical | 1,152 | 22.7 s | 38,144 | 177 | 0.8 |
| 90 s | 0.7% power given | 0.7% power given | 63.1% GAIN | 0.2% STEADY | 1.8% GAIN | identical | 960 | 22.3 s | 37,522 | 130 | 1.4 |
| 120 s | 0.8% power given | 0.7% power given | 57.0% GAIN | 0.2% STEADY | 2.1% GAIN | identical | 720 | 22.0 s | 36,733 | 118 | 3.0 |

#### omni-v15 at each beat against itself at 15 s (the factory's beat)

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | 1.9% GAIN | 1.3% GAIN | identical | identical | identical | identical |
| 10 s | 0.9% GAIN | 0.6% GAIN | 7.1% LOSS | 0.0% STEADY | 0.0% STEADY | identical |
| 20 s | 0.4% STEADY | 0.3% STEADY | 34.7% LOSS | 0.0% STEADY | 0.0% STEADY | identical |
| 30 s | 0.6% power given | 0.4% STEADY | 28.8% LOSS | 0.0% STEADY | 0.0% STEADY | identical |
| 60 s | 0.5% GAIN | 0.4% STEADY | 114.5% LOSS | 0.0% STEADY | 0.0% STEADY | identical |
| 75 s | 0.6% GAIN | 0.4% STEADY | 143.0% LOSS | 0.0% STEADY | 0.3% STEADY | identical |
| 90 s | 0.1% STEADY | 0.1% STEADY | 192.1% LOSS | 0.0% STEADY | 0.3% STEADY | identical |
| 120 s | 0.0% STEADY | 0.0% STEADY | 240.8% LOSS | 0.0% STEADY | 0.0% STEADY | identical |

#### omni-v15 at each beat against itself at 60 s

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | 1.4% GAIN | 1.0% GAIN | 53.4% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 10 s | 0.4% STEADY | 0.3% STEADY | 50.1% GAIN | 0.0% STEADY | identical | identical |
| 15 s | 0.5% power given | 0.4% STEADY | 53.4% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 20 s | 1.0% power given | 0.7% power given | 37.2% GAIN | 0.0% STEADY | identical | identical |
| 30 s | 1.1% power given | 0.8% power given | 40.0% GAIN | 0.0% STEADY | identical | identical |
| 75 s | 0.0% STEADY | 0.1% STEADY | 13.3% LOSS | 0.0% STEADY | 0.3% STEADY | identical |
| 90 s | 0.4% STEADY | 0.3% STEADY | 36.2% LOSS | 0.0% STEADY | 0.3% STEADY | identical |
| 120 s | 0.5% power given | 0.3% STEADY | 58.8% LOSS | 0.0% STEADY | identical | identical |

Native's means over the seeds: machine-hours 133.076; energy per used core-hour 0.036; pods waiting for a place 7.311; 95th percentile response 79.914; 99th percentile response 153.537; minutes over the line 27.000.

## In the cloud: the cloud's own autoscaler makes and deletes machines in every arm; the governor on the machines alone (--give-back-only)

### omni-v16 against native

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line | Decisions a day | Governor CPU a day | Cluster reads a day | Writes a day | The fast check's rescues a day |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 s | 1.6% GAIN | 0.9% GAIN | 15.1% LOSS | 0.0% STEADY | 0.7% LOSS | 0.9% LOSS | 17,280 | 92.7 s | 86,412 | 5,805 | 0.0 |
| 10 s | 1.5% GAIN | 0.9% GAIN | 15.9% LOSS | 0.0% STEADY | 0.7% LOSS | 0.9% LOSS | 8,640 | 56.4 s | 60,682 | 2,884 | 1.2 |
| 15 s | 1.8% GAIN | 1.0% GAIN | 16.8% LOSS | 0.0% STEADY | 0.0% STEADY | identical | 5,760 | 44.4 s | 52,122 | 1,964 | 0.0 |
| 20 s | 1.0% GAIN | 0.5% GAIN | 9.2% LOSS | 0.0% STEADY | identical | identical | 4,320 | 38.1 s | 47,797 | 1,431 | 3.9 |
| 30 s | 1.4% GAIN | 0.8% GAIN | 11.0% LOSS | 0.0% STEADY | identical | identical | 2,880 | 32.3 s | 43,515 | 988 | 2.5 |
| 60 s | 1.0% GAIN | 0.5% GAIN | 7.5% LOSS | 0.0% STEADY | identical | identical | 1,440 | 26.3 s | 39,091 | 538 | 5.5 |
| 75 s | 1.4% GAIN | 0.7% GAIN | 9.5% LOSS | 0.0% STEADY | identical | identical | 1,152 | 25.3 s | 38,292 | 429 | 6.8 |
| 90 s | 0.8% GAIN | 0.4% STEADY | 8.2% LOSS | 0.0% STEADY | 0.6% LOSS | 0.5% STEADY | 960 | 24.6 s | 37,462 | 360 | 6.0 |
| 120 s | 0.7% GAIN | 0.4% STEADY | 4.9% LOSS | 0.0% STEADY | identical | identical | 720 | 23.7 s | 36,702 | 285 | 5.4 |

#### omni-v16 at each beat against itself at 15 s (the factory's beat)

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | 0.2% STEADY | 0.1% STEADY | 1.5% GAIN | 0.0% STEADY | 0.6% LOSS | 0.9% LOSS |
| 10 s | 0.3% STEADY | 0.1% STEADY | 0.7% GAIN | 0.0% STEADY | 0.6% LOSS | 0.9% LOSS |
| 20 s | 0.8% power given | 0.5% STEADY | 6.5% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 30 s | 0.5% STEADY | 0.2% STEADY | 5.0% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 60 s | 0.9% power given | 0.5% STEADY | 7.9% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 75 s | 0.5% STEADY | 0.3% STEADY | 6.3% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 90 s | 1.0% power given | 0.5% power given | 7.3% GAIN | 0.0% STEADY | 0.6% LOSS | 0.5% STEADY |
| 120 s | 1.2% power given | 0.6% power given | 10.2% GAIN | 0.0% STEADY | 0.0% STEADY | identical |

#### omni-v16 at each beat against itself at 60 s

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | 0.6% GAIN | 0.4% STEADY | 7.0% LOSS | 0.0% STEADY | 0.7% LOSS | 0.9% LOSS |
| 10 s | 0.6% GAIN | 0.3% STEADY | 7.8% LOSS | 0.0% STEADY | 0.7% LOSS | 0.9% LOSS |
| 15 s | 0.9% GAIN | 0.5% STEADY | 8.6% LOSS | 0.0% STEADY | 0.0% STEADY | identical |
| 20 s | 0.1% STEADY | 0.0% STEADY | 1.6% LOSS | 0.0% STEADY | identical | identical |
| 30 s | 0.4% STEADY | 0.3% STEADY | 3.2% LOSS | 0.0% STEADY | identical | identical |
| 75 s | 0.4% STEADY | 0.2% STEADY | 1.8% LOSS | 0.0% STEADY | identical | identical |
| 90 s | 0.2% STEADY | 0.1% STEADY | 0.7% LOSS | 0.0% STEADY | 0.6% LOSS | 0.5% STEADY |
| 120 s | 0.3% STEADY | 0.1% STEADY | 2.4% GAIN | 0.0% STEADY | identical | identical |

### omni-v15 against native

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line | Decisions a day | Governor CPU a day | Cluster reads a day | Writes a day | The fast check's rescues a day |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 s | 2.2% GAIN | 1.2% GAIN | 20.5% LOSS | 0.0% STEADY | 0.7% LOSS | 0.9% LOSS | 17,280 | 91.6 s | 86,412 | 6,516 | 0.0 |
| 10 s | 1.7% GAIN | 0.9% GAIN | 15.9% LOSS | 0.0% STEADY | 0.7% LOSS | 0.9% LOSS | 8,640 | 56.6 s | 60,682 | 3,151 | 1.2 |
| 15 s | 1.9% GAIN | 1.0% GAIN | 22.2% LOSS | 0.0% STEADY | 0.6% LOSS | 0.5% STEADY | 5,760 | 44.4 s | 52,124 | 2,093 | 0.0 |
| 20 s | 1.1% GAIN | 0.5% GAIN | 13.2% LOSS | 0.0% STEADY | 0.6% LOSS | 0.5% STEADY | 4,320 | 39.0 s | 47,792 | 1,572 | 3.8 |
| 30 s | 1.4% GAIN | 0.8% GAIN | 11.0% LOSS | 0.0% STEADY | identical | identical | 2,880 | 33.2 s | 43,515 | 1,045 | 2.5 |
| 60 s | 1.0% GAIN | 0.5% GAIN | 7.5% LOSS | 0.0% STEADY | identical | identical | 1,440 | 26.7 s | 39,091 | 538 | 5.5 |
| 75 s | 1.4% GAIN | 0.7% GAIN | 9.5% LOSS | 0.0% STEADY | identical | identical | 1,152 | 25.7 s | 38,292 | 429 | 6.8 |
| 90 s | 0.8% GAIN | 0.4% STEADY | 8.2% LOSS | 0.0% STEADY | 0.6% LOSS | 0.5% STEADY | 960 | 24.8 s | 37,462 | 360 | 6.0 |
| 120 s | 0.7% GAIN | 0.4% STEADY | 4.9% LOSS | 0.0% STEADY | identical | identical | 720 | 23.9 s | 36,702 | 285 | 5.4 |

#### omni-v15 at each beat against itself at 15 s (the factory's beat)

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | 0.3% STEADY | 0.2% STEADY | 1.3% GAIN | 0.0% STEADY | 0.1% STEADY | 0.5% STEADY |
| 10 s | 0.3% STEADY | 0.1% STEADY | 5.1% GAIN | 0.0% STEADY | 0.1% STEADY | 0.5% STEADY |
| 20 s | 0.9% power given | 0.5% STEADY | 7.3% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 30 s | 0.6% power given | 0.2% STEADY | 9.2% GAIN | 0.0% STEADY | 0.6% GAIN | 0.5% STEADY |
| 60 s | 1.0% power given | 0.5% STEADY | 12.0% GAIN | 0.0% STEADY | 0.6% GAIN | 0.5% STEADY |
| 75 s | 0.5% power given | 0.3% STEADY | 10.4% GAIN | 0.0% STEADY | 0.6% GAIN | 0.5% STEADY |
| 90 s | 1.1% power given | 0.6% power given | 11.4% GAIN | 0.0% STEADY | 0.0% STEADY | identical |
| 120 s | 1.3% power given | 0.6% power given | 14.1% GAIN | 0.0% STEADY | 0.6% GAIN | 0.5% STEADY |

#### omni-v15 at each beat against itself at 60 s

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | 1.2% GAIN | 0.7% GAIN | 12.1% LOSS | 0.0% STEADY | 0.7% LOSS | 0.9% LOSS |
| 10 s | 0.7% GAIN | 0.4% STEADY | 7.8% LOSS | 0.0% STEADY | 0.7% LOSS | 0.9% LOSS |
| 15 s | 0.9% GAIN | 0.5% STEADY | 13.6% LOSS | 0.0% STEADY | 0.6% LOSS | 0.5% STEADY |
| 20 s | 0.1% STEADY | 0.0% STEADY | 5.3% LOSS | 0.0% STEADY | 0.6% LOSS | 0.5% STEADY |
| 30 s | 0.4% STEADY | 0.3% STEADY | 3.2% LOSS | 0.0% STEADY | identical | identical |
| 75 s | 0.4% STEADY | 0.2% STEADY | 1.8% LOSS | 0.0% STEADY | identical | identical |
| 90 s | 0.2% STEADY | 0.1% STEADY | 0.7% LOSS | 0.0% STEADY | 0.6% LOSS | 0.5% STEADY |
| 120 s | 0.3% STEADY | 0.1% STEADY | 2.4% GAIN | 0.0% STEADY | identical | identical |

Native's means over the seeds: machine-hours 133.076; energy per used core-hour 0.036; pods waiting for a place 7.311; 95th percentile response 79.914; 99th percentile response 153.537; minutes over the line 27.000.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
