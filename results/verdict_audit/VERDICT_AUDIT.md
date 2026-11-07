# The verdict audit: every row recomputed from its stored values, every count from one selection

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

Written by `tools/verdict_audit.py` from the three-run tables as they stand (digest `a09678d9af2f9f0d`). The engine that stands is omni-v26. The rule: tools/readings.py three_run_reading: a change of 0.5% or more, the mean of the three runs' changes in percent of native, reads by the gauge's aim; under it STEADY, under the floor; every run's two values equal to 1e-09 of the value, STEADY, the same; runs that moved 0.5% or more in opposite directions, the runs disagree. Evidence strength is shown beside the word and never changes it: strong, every run the mean's way and beyond its noise (its 95% interval clear of zero); moderate, all but one; weak, one run beyond its noise; inconclusive, no run beyond its noise (a mean of 0.5% or more, not a change any one run could tell from its noise). STEADY is of three kinds: exactly the same (every run's values equal to nine decimal places), under the floor (a measured change, the three runs' mean under 0.5%) and no difference beyond the noise (a table read by an older key). The runs disagree is unresolved, never a final word: opposite directions each beyond its noise, or opposite directions inside overlapping noise.

## The counts

| What | Count |
|---|---|
| Three-run tables | 340: 100 standing, 178 superseded, 60 the road, 2 taken out |
| Standing tables, Omni-Compass against its native | 63 |
| Standing tables on the engine that stands (omni-v26) | 0 |
| Standing tables not yet run again on omni-v26 | 100 |
| Rows recomputed from their stored values | 10598 of 14630 |
| Stored readings the key reads otherwise | 0 |
| Markdown readings unlike their JSON twin | 0 |

### Standing tables: Omni-Compass against its native (the readings do no harm is judged by)

Every word: 486 GAIN, 181 power given, 584 STEADY, 287 LOSS, 188 the runs disagree, 30 the runs differ, 655 shown, 201 tuning. The four categories are exclusive: each row has one word.

| Engine | Words |
|---|---|
| omni-v25 | 473 GAIN, 181 power given, 574 STEADY, 281 LOSS, 173 the runs disagree, 30 the runs differ, 637 shown, 201 tuning |
| omni-v12 | 13 GAIN, 10 STEADY, 6 LOSS, 15 the runs disagree, 18 shown |

| Evidence class | Words |
|---|---|
| L (the real software) | 389 GAIN, 171 power given, 423 STEADY, 287 LOSS, 188 the runs disagree, 598 shown, 189 tuning |
| S (an outside simulator driven by our own runner) | 97 GAIN, 10 power given, 161 STEADY, 30 the runs differ, 57 shown, 12 tuning |

Useful work, time waited and resources apart (item 8 of the work order): a resource spent or held that rose is power given, shown beside what it bought, never a gain in work.

| The gauge's direction | Words |
|---|---|
| a count that must never rise | 6 GAIN, 82 STEADY, 14 tuning |
| resource spent or held | 267 GAIN, 181 power given, 230 STEADY, 62 the runs disagree, 6 the runs differ, 63 tuning |
| shown | 6 STEADY, 19 the runs differ, 655 shown, 56 tuning |
| time waited, missed or failed | 182 GAIN, 185 STEADY, 282 LOSS, 120 the runs disagree, 2 the runs differ, 39 tuning |
| work done | 31 GAIN, 81 STEADY, 5 LOSS, 6 the runs disagree, 3 the runs differ, 29 tuning |

Evidence strength beside the word (it never changes the word):

| Word | Strength |
|---|---|
| GAIN | 198 strong, 94 deterministic, reproduced in all three runs, 92 inconclusive, 55 weak, 44 moderate, 3 not recomputable from runs |
| LOSS | 95 inconclusive, 86 strong, 57 weak, 49 moderate |
| power given | 101 strong, 26 moderate, 24 inconclusive, 20 weak, 10 deterministic, reproduced in all three runs |

| STEADY of each kind | 231 under the floor, 353 exactly the same |
|---|---|
| The runs disagree, by cause | 188 opposite directions inside overlapping noise |

### Every comparison and status

| Status, comparison | Words |
|---|---|
| standing | against its native | 486 GAIN, 181 power given, 584 STEADY, 287 LOSS, 188 the runs disagree, 30 the runs differ, 655 shown, 201 tuning |
| standing | in place of a controller | 108 GAIN, 29 power given, 69 STEADY, 76 LOSS, 17 the runs disagree, 137 shown |
| standing | the orchestrator's own | 31 GAIN, 11 power given, 85 STEADY, 76 LOSS, 32 the runs disagree, 99 shown |
| standing | two changes at once | 61 GAIN, 25 power given, 45 STEADY, 95 LOSS, 9 the runs disagree, 99 shown |
| superseded | against its native | 1266 GAIN, 445 power given, 2024 STEADY, 340 LOSS, 1089 the runs disagree, 50 the runs differ, 1271 shown, 1020 tuning |
| superseded | in place of a controller | 100 GAIN, 9 power given, 40 STEADY, 22 LOSS, 20 the runs disagree, 81 shown |
| superseded | the orchestrator's own | 26 GAIN, 12 power given, 70 STEADY, 61 LOSS, 22 the runs disagree, 81 shown |
| superseded | two changes at once | 47 GAIN, 21 power given, 38 STEADY, 72 LOSS, 13 the runs disagree, 81 shown |
| taken out | against its native | 15 GAIN, 5 power given, 1 LOSS, 3 the runs disagree |
| the road | against its native | 590 GAIN, 114 power given, 949 STEADY, 55 LOSS, 133 the runs disagree, 17 the runs differ, 519 shown, 192 tuning |

The orchestrator's own rows (ORCH) carry no Omni-Compass in either arm; two changes at once (BOTH) and in place of a controller (VS) are shown, never a reading of Omni-Compass against its native.

## Every LOSS row of Omni-Compass against its native (287)

| Table | Engine | Class | Gauge | Native → Omni-Compass, raw change, each run | Evidence |
|---|---|---|---|---|---|
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 536.2 → 567.1 (+5.8%); 1283 → 1372 (+6.9%); 863.2 → 913.5 (+5.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | L | response time (ms), 99th percentile | 767.9 → 818.7 (+6.6%); 1874 → 2010 (+7.3%); 1252 → 1296 (+3.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 38.07 → 40.1 (+5.3%); 85.79 → 89.12 (+3.9%); 55.45 → 59.44 (+7.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.0; 0.1 → 0.2 (+100.0%); 0.1 → 0.1 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | L | batch: queue finished (s) | 1290 → 1313 (+1.8%); 1421 → 1421 (−0.0%); 1396 → 1421 (+1.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 614 → 650.2 (+5.9%); 799.3 → 814.5 (+1.9%); 763.3 → 789 (+3.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ALL_FOUR.md` | omni-v25 | L | failed requests (%) | 9.719 → 10.23 (+5.3%); 8.765 → 8.883 (+1.3%); 12.03 → 12.24 (+1.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ALL_FOUR.md` | omni-v25 | L | pod start wait, total (s) | 8.4 → 18.2 (+116.7%); 7.5 → 14.8 (+97.3%); 8.9 → 17.3 (+94.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | response time (ms), mean | 760.4 → 857.7 (+12.8%); 768.3 → 850.7 (+10.7%); 728.8 → 840.4 (+15.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | response time (ms), 95th percentile | 3024 → 3616 (+19.6%); 3087 → 3386 (+9.7%); 2963 → 3466 (+17.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | response time (ms), 99th percentile | 4046 → 4772 (+17.9%); 4201 → 4622 (+10.0%); 4015 → 4663 (+16.2%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | time over the response line (% of samples) | 27.13 → 29.93 (+10.3%); 27.14 → 30.97 (+14.1%); 24.39 → 28.8 (+18.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | failed requests (%) | 0.02241947029348604; 0.022518382352941176; 0.06890149077649078 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 → 14.8 (+10.4%); 13.3 → 14.7 (+10.5%); 12.3 → 13.9 (+13.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 0.5 → 5.3 (+960.0%); 0.4 → 8 (+1900.0%); 0.2 → 9.9 (+4850.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | pod start wait, mean (s) | 0.5 → 1.592 (+218.3%); 0.4 → 1.808 (+352.1%); 0.2 → 2.198 (+998.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | batch: queue finished (s) | 929.4 → 981.1 (+5.6%); 932.5 → 987.3 (+5.9%); 916.1 → 972.2 (+6.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.09167 → 0.125 (+36.4%); 0.1042 → 0.1917 (+84.0%); 0.1208 → 0.1833 (+51.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 → 0.8 (+33.3%); 0.5 → 0.8 (+60.0%); 0.7 → 0.9 (+28.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 238.8 → 276.1 (+15.6%); 237.8 → 294.4 (+23.8%); 222.5 → 273.7 (+23.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_TOP.md` | omni-v25 | L | time over the response line (% of samples) | 0.0036101083032490976; 0.0; 0.007259743339745448 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 0.3 → 4.3 (+1333.3%); 0.7 → 2.8 (+300.0%); 0.6 → 2.2 (+266.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_ARMADA_4W_TOP.md` | omni-v25 | L | pod start wait, mean (s) | 0.3 → 1.465 (+388.3%); 0.65 → 1.467 (+125.6%); 0.4 → 0.775 (+93.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_BATCH.md` | omni-v25 | L | time over the response line (% of samples) | 19.32 → 19.41 (+0.4%); 18.24 → 18.65 (+2.3%); 18.29 → 18.21 (−0.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BATCH.md` | omni-v25 | L | failed requests (%) | 0.0; 0.01092896174863388; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BATCH.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 → 11.7 (+0.9%); 11.1 → 11.1 (±0.0%); 10.7 → 11.1 (+3.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_BATCH.md` | omni-v25 | L | batch: queue finished (s) | 678.5 → 696.1 (+2.6%); 651.3 → 669.1 (+2.7%); 631.9 → 650.2 (+2.9%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | response time (ms), 95th percentile | 2164 → 2323 (+7.3%); 2037 → 2274 (+11.6%); 2299 → 2500 (+8.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | response time (ms), 99th percentile | 3052 → 3213 (+5.3%); 2956 → 3259 (+10.3%); 3344 → 3551 (+6.2%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | failed requests (%) | 0.011049723756906077; 0.0; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 → 12 (+2.6%); 11.7 → 11.9 (+1.7%); 12 → 12.2 (+1.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | pod start wait, total (s) | 0.3 → 3.3 (+1000.0%); 3.1; 0.8 → 2.6 (+225.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | pod start wait, mean (s) | 0.3 → 1.15 (+283.3%); 1.4; 0.6 → 1.133 (+88.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | batch: queue finished (s) | 843 → 856 (+1.5%); 832.9 → 846.1 (+1.6%); 847.4 → 867.6 (+2.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.1917 → 0.3458 (+80.4%); 0.075 → 0.1333 (+77.8%); 0.1 → 0.1375 (+37.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 → 2.5 (+56.2%); 0.5 → 0.8 (+60.0%); 0.6 → 0.9 (+50.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_BINPACK.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 151.8 → 164.5 (+8.4%); 142.6 → 155.2 (+8.8%); 155.7 → 174.3 (+12.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | L | response time (ms), 95th percentile | 1169 → 1352 (+15.6%); 1738 → 1925 (+10.8%); 1882 → 2154 (+14.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | L | response time (ms), 99th percentile | 1675 → 1917 (+14.4%); 2408 → 2691 (+11.7%); 2694 → 3032 (+12.6%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | L | failed requests (%) | 0.0; 0.011695906432748537; 0.022042749574933202 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 → 7.6 (+4.1%); 10.7 → 11.5 (+7.5%); 11.7 → 12.3 (+5.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 3.6; 5.4; 3.5 | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | L | pod start wait, mean (s) | 1.7666666666666664; 2.103333333333333; 1.7166666666666668 | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | L | batch: queue finished (s) | 782.3 → 793.6 (+1.4%); 825.2 → 837.9 (+1.5%); 832.7 → 853 (+2.4%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 → 1.9 (+533.3%); 1 → 1 (±0.0%); 0.6 → 1.8 (+200.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 87.73 → 98.31 (+12.1%); 130.7 → 145.4 (+11.3%); 138.7 → 157.6 (+13.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | L | response time (ms), 95th percentile | 1279 → 1377 (+7.6%); 1867 → 1866 (−0.1%); 2114 → 2297 (+8.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | L | response time (ms), 99th percentile | 1828 → 1960 (+7.2%); 2696 → 2735 (+1.4%); 2985 → 3106 (+4.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 → 7.5 (+21.0%); 10.3 → 10.8 (+4.9%); 10.9 → 11 (+0.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 3.3; 0.4 → 5 (+1150.0%); 0.6 → 3.4 (+466.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | L | pod start wait, mean (s) | 1.2166666666666668; 0.3 → 1.732 (+477.2%); 0.45 → 1.242 (+175.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | L | batch: queue finished (s) | 785.6 → 794.6 (+1.1%); 825.9 → 839 (+1.6%); 836.7 → 850 (+1.6%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.0375 → 0.125 (+233.3%); 0.225 → 0.3917 (+74.1%); 0.075 → 0.1833 (+144.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5; 1.2 → 2 (+66.7%); 0.4 → 1.1 (+175.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 93.63 → 103.7 (+10.7%); 133.8 → 144.6 (+8.1%); 144.8 → 156.6 (+8.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_CAPACITY.md` | omni-v25 | L | 2000:capacity | 10.8 → 10.4 (−3.7%); 8.4 → 8.4 (±0.0%); 8.8 → 8.8 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_CAPACITY.md` | omni-v25 | L | 3000:work | 1.153e+04 → 1.135e+04 (−1.5%); 1.224e+04 → 1.213e+04 (−0.9%); 1.285e+04 → 1.287e+04 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_CAPACITY.md` | omni-v25 | L | 3000:capacity | 12.8 → 11.6 (−9.4%); 15.6 → 15.2 (−2.6%); 16.8 → 16 (−4.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_CRANE_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 7.5 → 10.4 (+38.7%); 6.3 → 11.4 (+81.0%); 7.6 → 12.4 (+63.2%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_CRANE_4W_TOP.md` | omni-v25 | L | response time (ms), mean | 141.1 → 142.3 (+0.8%); 147.3 → 148.3 (+0.7%); 144.2 → 145.6 (+1.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_CRANE_4W_TOP.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.0; 0.1; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_CRANE_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 5.6 → 10.3 (+83.9%); 7.3 → 12.6 (+72.6%); 7.4 → 11.6 (+56.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_CRUISEKUBE.md` | omni-v25 | L | response time (ms), mean | 76.07 → 79.08 (+4.0%); 87.47 → 90.32 (+3.2%); 82.57 → 84.86 (+2.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_CRUISEKUBE.md` | omni-v25 | L | response time (ms), 95th percentile | 114.3 → 117.4 (+2.7%); 135.8 → 138.8 (+2.2%); 127.3 → 129.1 (+1.4%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_CRUISEKUBE.md` | omni-v25 | L | response time (ms), 99th percentile | 127.5 → 137.3 (+7.7%); 155.1 → 166.5 (+7.3%); 147.1 → 147.2 (+0.1%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_CRUISEKUBE_RECORDER.md` | omni-v25 | L | response time (ms), mean | 72.94 → 74.39 (+2.0%); 75.02 → 77.37 (+3.1%); 80.02 → 81.15 (+1.4%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_CRUISEKUBE_RECORDER.md` | omni-v25 | L | response time (ms), 95th percentile | 105.8 → 109.1 (+3.1%); 112 → 116.6 (+4.1%); 120.8 → 122.1 (+1.1%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_CRUISEKUBE_RECORDER.md` | omni-v25 | L | response time (ms), 99th percentile | 117.7 → 127.8 (+8.6%); 125.5 → 136.6 (+8.8%); 133.3 → 141.9 (+6.5%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_CRUISEKUBE_RECORDER.md` | omni-v25 | L | pod start wait, mean (s) | 1.617 → 1.75 (+8.2%); 1.4 → 1.55 (+10.7%); 1.3 → 1.45 (+11.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_FAIRNESS.md` | omni-v25 | L | response time (ms), 95th percentile | 2042 → 2033 (−0.5%); 2123 → 2474 (+16.5%); 2428 → 2590 (+6.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_FAIRNESS.md` | omni-v25 | L | pod start wait, total (s) | 9.9 → 10.8 (+9.1%); 8.2 → 10.2 (+24.4%); 8.3 → 10.9 (+31.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_FAIRNESS.md` | omni-v25 | L | pod start wait, mean (s) | 1.66 → 1.684 (+1.4%); 1.519 → 1.833 (+20.7%); 1.521 → 1.912 (+25.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_FAIRNESS.md` | omni-v25 | L | second app: response time (ms), 95th percentile | 399.6 → 453.1 (+13.4%); 263 → 284.1 (+8.0%); 246.2 → 255 (+3.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_FAIRNESS.md` | omni-v25 | L | second app: time over the response line (% of samples) | 13.69 → 14.1 (+3.0%); 14.32 → 14.34 (+0.1%); 15.08 → 15.21 (+0.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_FAULTS.md` | omni-v25 | L | pod start wait, total (s) | 16.2 → 32.4 (+100.0%); 8.5 → 16.8 (+97.6%); 18.1 → 38.6 (+113.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_FAULTS_EXTENDED.md` | omni-v25 | L | pod start wait, total (s) | 14.6 → 24 (+64.4%); 13 → 19.3 (+48.5%); 12.5 → 20 (+60.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_FAULTS_EXTENDED.md` | omni-v25 | L | pod start wait, mean (s) | 1.671 → 1.933 (+15.7%); 1.524 → 1.599 (+4.9%); 1.509 → 1.661 (+10.1%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | L | response time (ms), mean | 412.5 → 426.6 (+3.4%); 422 → 443.8 (+5.2%); 511.9 → 537.3 (+5.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | L | response time (ms), 95th percentile | 1511 → 1574 (+4.2%); 1610 → 1697 (+5.4%); 2033 → 2088 (+2.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | L | time over the response line (% of samples) | 17.68 → 18.28 (+3.4%); 19.15 → 19.57 (+2.2%); 21.65 → 22.6 (+4.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 → 9.1 (+4.6%); 10.3 → 10.5 (+1.9%); 11.9 → 12.1 (+1.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 0.4 → 2.8 (+600.0%); 2.5; 0.2 → 2.8 (+1300.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | L | pod start wait, mean (s) | 0.2 → 1.25 (+525.0%); 0.775; 0.2 → 1.208 (+504.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | L | batch: queue finished (s) | 817.3 → 821.7 (+0.5%); 814.4 → 822.4 (+1.0%); 845.5 → 853.7 (+1.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.2667 → 0.4542 (+70.3%); 0.225 → 0.6875 (+205.6%); 0.725 → 0.8875 (+22.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 123.3 → 125.6 (+1.8%); 120.1 → 128.4 (+7.0%); 151.8 → 157.9 (+4.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | L | response time (ms), mean | 414.7 → 426.1 (+2.7%); 423.9 → 459.4 (+8.4%); 517 → 523.7 (+1.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | L | response time (ms), 95th percentile | 1641 → 1686 (+2.7%); 1671 → 1889 (+13.0%); 2105 → 2133 (+1.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | L | response time (ms), 99th percentile | 2284 → 2368 (+3.7%); 2409 → 2605 (+8.1%); 2977 → 3053 (+2.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | L | failed requests (%) | 0.0; 0.0; 0.011764705882352941 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 → 8.7 (±0.0%); 10 → 10.4 (+4.0%); 11.3 → 11.7 (+3.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 0.4 → 2.5 (+525.0%); 0.4; 2.6 | weak; 1 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | L | pod start wait, mean (s) | 0.2 → 1.02 (+410.0%); 0.2; 1.3 | weak; 1 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | L | batch: queue finished (s) | 822.3 → 828.9 (+0.8%); 821.1 → 833 (+1.4%); 852.7 → 860.9 (+1.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 129.4 → 136.5 (+5.5%); 129.9 → 138.7 (+6.8%); 162.1 → 165.9 (+2.3%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_GOLDILOCKS.md` | omni-v25 | L | pod start wait, total (s) | 3.7 → 12.1 (+227.0%); 3.5 → 10.9 (+211.4%); 4.1 → 12.5 (+204.9%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_GOLDILOCKS.md` | omni-v25 | L | pod start wait, mean (s) | 1.35 → 1.673 (+23.9%); 1.225 → 1.636 (+33.5%); 1.283 → 1.586 (+23.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KAI.md` | omni-v25 | L | response time (ms), 95th percentile | 1443 → 1573 (+9.1%); 1996 → 2179 (+9.1%); 2901 → 3072 (+5.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KAI.md` | omni-v25 | L | response time (ms), 99th percentile | 2042 → 2360 (+15.6%); 2763 → 2980 (+7.9%); 3912 → 4234 (+8.2%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KAI.md` | omni-v25 | L | time over the response line (% of samples) | 11.88 → 12.44 (+4.7%); 16.67 → 16.94 (+1.6%); 24.22 → 24.29 (+0.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KAI.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 → 8.5 (+6.2%); 10 → 10.5 (+5.0%); 13.6 → 14.5 (+6.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KAI.md` | omni-v25 | L | pod start wait, total (s) | 0.3 → 0.4 (+33.3%); 1.6; 3.4 | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KAI.md` | omni-v25 | L | pod start wait, mean (s) | 0.2 → 0.25 (+25.0%); 0.9333333333333332; 1.125 | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KAI.md` | omni-v25 | L | batch: queue finished (s) | 807.9 → 823.6 (+1.9%); 855.1 → 871.6 (+1.9%); 932.7 → 951.1 (+2.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KAI.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 111.6 → 123.6 (+10.8%); 154.8 → 167.7 (+8.3%); 225.6 → 241.1 (+6.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | response time (ms), 95th percentile | 1259 → 1475 (+17.2%); 1548 → 1648 (+6.4%); 1850 → 2106 (+13.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | response time (ms), 99th percentile | 1707 → 2040 (+19.5%); 2202 → 2253 (+2.3%); 2645 → 3050 (+15.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | time over the response line (% of samples) | 16.97 → 19.28 (+13.6%); 17.61 → 17.86 (+1.4%); 23.59 → 23.54 (−0.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 → 10.7 (+7.0%); 9.7 → 10.1 (+4.1%); 11.1 → 11.9 (+7.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 2.4; 4.3; 0.4 → 4.7 (+1075.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | pod start wait, mean (s) | 1.4; 1.775; 0.2 → 1.883 (+841.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | batch: queue finished (s) | 783.3 → 794.8 (+1.5%); 809.9 → 818.1 (+1.0%); 832.9 → 849.9 (+2.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.05833 → 0.1625 (+178.6%); 0.1583 → 0.3375 (+113.2%); 0.1 → 0.2167 (+116.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 → 1 (+100.0%); 1.4 → 1.4 (±0.0%); 0.5 → 1.2 (+140.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 89.07 → 101.6 (+14.1%); 116 → 121.9 (+5.1%); 137.9 → 153.6 (+11.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | L | response time (ms), 95th percentile | 1785 → 1891 (+5.9%); 2033 → 2186 (+7.5%); 2632 → 2681 (+1.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | L | response time (ms), 99th percentile | 2517 → 2713 (+7.8%); 2734 → 2917 (+6.7%); 3576 → 3694 (+3.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | L | failed requests (%) | 0.0; 0.011627906976744186; 0.02326 → 0.1163 (+400.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 → 11.5 (+4.5%); 10.7 → 11.3 (+5.6%); 12 → 13.3 (+10.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 1.2; 0.3 → 2 (+566.7%); 0.4 → 3.1 (+675.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | L | pod start wait, mean (s) | 0.6666666666666667; 0.3 → 0.7833 (+161.1%); 0.2 → 1.267 (+533.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | L | batch: queue finished (s) | 828.8 → 841.4 (+1.5%); 861.1 → 875.1 (+1.6%); 890.3 → 915.1 (+2.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 1.113 → 1.208 (+8.6%); 1.317 → 1.554 (+18.0%); 1.233 → 1.421 (+15.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 133.1 → 142.5 (+7.1%); 161.3 → 171.1 (+6.1%); 190.9 → 209.8 (+9.9%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | response time (ms), mean | 612.3 → 721.5 (+17.8%); 698.4 → 786.2 (+12.6%); 868.3 → 994.7 (+14.6%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | response time (ms), 95th percentile | 2280 → 2978 (+30.6%); 2746 → 3269 (+19.0%); 3593 → 4258 (+18.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | response time (ms), 99th percentile | 3162 → 3978 (+25.8%); 3609 → 4307 (+19.3%); 4813 → 5759 (+19.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | time over the response line (% of samples) | 21.67 → 24.99 (+15.3%); 25.55 → 29.77 (+16.5%); 31.78 → 34.29 (+7.9%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | failed requests (%) | 0.007168458781362007; 0.007067 → 0.01545 (+118.7%); 0.02302686350879122 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 → 13.8 (+35.3%); 13.4 → 15 (+11.9%); 14.9 → 15.9 (+6.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 0.8 → 7.6 (+850.0%); 0.2 → 10 (+4900.0%); 0.2 → 10.6 (+5200.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | pod start wait, mean (s) | 0.6 → 2.31 (+285.0%); 0.2 → 1.986 (+892.9%); 0.2 → 2.517 (+1158.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | batch: queue finished (s) | 876 → 924.1 (+5.5%); 907.8 → 950 (+4.6%); 956.1 → 1020 (+6.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 → 0.6 (+20.0%); 0.6 → 0.7 (+16.7%); 0.9 → 0.9 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 184.5 → 225.8 (+22.4%); 213.6 → 252.8 (+18.3%); 260.7 → 317.7 (+21.9%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | response time (ms), mean | 759.6 → 830.1 (+9.3%); 851.2 → 974.1 (+14.4%); 1121 → 1211 (+8.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | response time (ms), 95th percentile | 3110 → 3443 (+10.7%); 3624 → 4317 (+19.1%); 5012 → 5472 (+9.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | response time (ms), 99th percentile | 4327 → 4818 (+11.3%); 4963 → 6020 (+21.3%); 6650 → 7177 (+7.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | time over the response line (% of samples) | 24.81 → 29.46 (+18.8%); 28.55 → 34.6 (+21.2%); 33.37 → 38.95 (+16.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | failed requests (%) | 0.03524 → 0.1576 (+347.2%); 0.04997 → 0.1297 (+159.5%); 0.06418 → 0.3481 (+442.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.7 → 16.4 (+11.6%); 17 → 18.1 (+6.5%); 17.3 → 18.4 (+6.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 0.2 → 9.1 (+4450.0%); 0.3 → 11.8 (+3833.3%); 0.2 → 15.3 (+7550.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | pod start wait, mean (s) | 0.2 → 2.096 (+947.9%); 0.3 → 2.268 (+656.1%); 0.2 → 2.751 (+1275.6%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | batch: queue finished (s) | 974.1 → 1020 (+4.7%); 1018 → 1086 (+6.7%); 1100 → 1163 (+5.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 5.846 → 12.73 (+117.7%); 8.633 → 17.99 (+108.4%); 7.446 → 15.43 (+107.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 33 → 66.3 (+100.9%); 65 → 159.4 (+145.2%); 34.6 → 129.2 (+273.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 286.1 → 330.5 (+15.5%); 321.1 → 384.1 (+19.6%); 400.6 → 468.9 (+17.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KEDA_CPU_REQUESTS.md` | omni-v25 | L | pod start wait, total (s) | 8.5 → 13.9 (+63.5%); 6.6 → 12.2 (+84.8%); 7.4 → 10.9 (+47.3%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KEDA_REQUESTS.md` | omni-v25 | L | pod start wait, mean (s) | 1.367 → 1.65 (+20.7%); 1.35 → 1.45 (+7.4%); 1.383 → 1.667 (+20.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | response time (ms), 95th percentile | 245.5 → 257.5 (+4.9%); 248.2 → 254.6 (+2.6%); 259.4 → 277.3 (+6.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | response time (ms), 99th percentile | 358.3 → 377.5 (+5.4%); 363.4 → 376 (+3.5%); 385.4 → 405.6 (+5.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | time over the response line (% of samples) | 0.2785 → 0.3855 (+38.5%); 0.2464 → 0.2715 (+10.2%); 0.317 → 0.3769 (+18.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 → 0.2 (±0.0%); 0.0; 0.2 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | pod start wait, total (s) | 0.1 → 3.9 (+3800.0%); 1.3; 0.2 → 3.6 (+1700.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | pod start wait, mean (s) | 0.1 → 1.448 (+1348.3%); 0.85; 0.2 → 1.353 (+576.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | batch: queue finished (s) | 1458 → 1474 (+1.1%); 1464 → 1508 (+3.0%); 1490 → 1512 (+1.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 162.4 → 217.1 (+33.7%); 166.7 → 175.8 (+5.4%); 172.1 → 210.5 (+22.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 732.6 → 889.7 (+21.4%); 816.7 → 848.1 (+3.8%); 818.2 → 848.1 (+3.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 843.7 → 877.8 (+4.0%); 898.3 → 933.6 (+3.9%); 933 → 983.9 (+5.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | L | queue: jobs unfinished at the window's end | 9.8 → 11.7 (+19.4%); 13 → 14.9 (+14.6%); 15 → 16.4 (+9.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | response time (ms), 95th percentile | 209.9 → 226.6 (+8.0%); 248.4 → 259.4 (+4.4%); 219.3 → 233.3 (+6.4%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | response time (ms), 99th percentile | 302.8 → 339.3 (+12.0%); 360.2 → 383.9 (+6.6%); 324.7 → 356 (+9.6%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | time over the response line (% of samples) | 0.092 → 0.1204 (+30.8%); 0.27 → 0.4154 (+53.9%); 0.2152 → 0.2709 (+25.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | pod start wait, total (s) | 0.8; 3.4; 0.6 → 1.5 (+150.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | pod start wait, mean (s) | 0.45; 1.1833333333333333; 0.6 → 0.7 (+16.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | batch: queue finished (s) | 1442 → 1475 (+2.2%); 1452 → 1466 (+0.9%); 1443 → 1480 (+2.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 118 → 171.7 (+45.4%); 161.8 → 204.9 (+26.6%); 133.8 → 183.7 (+37.3%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 569.3 → 734.6 (+29.0%); 779.2 → 805 (+3.3%); 612 → 738.4 (+20.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 766.7 → 805.2 (+5.0%); 852.1 → 909.7 (+6.8%); 811.9 → 877.1 (+8.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | L | queue: jobs unfinished at the window's end | 6.8 → 8.1 (+19.1%); 12.8 → 14.2 (+10.9%); 9.9 → 12.2 (+23.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KUBERAY_4W_BARE.md` | omni-v25 | L | response time (ms), 95th percentile | 1973 → 2096 (+6.2%); 1176 → 1315 (+11.8%); 1405 → 1575 (+12.1%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUBERAY_4W_BARE.md` | omni-v25 | L | response time (ms), 99th percentile | 2686 → 2882 (+7.3%); 1667 → 1897 (+13.8%); 2040 → 2169 (+6.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KUBERAY_4W_BARE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.8 → 12 (+1.7%); 8 → 8.7 (+8.8%); 9.3 → 9.4 (+1.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KUBERAY_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 2.8; 2.7; 2.5 | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUBERAY_4W_BARE.md` | omni-v25 | L | pod start wait, mean (s) | 1.5; 1.1; 1.3166666666666667 | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUBERAY_4W_BARE.md` | omni-v25 | L | batch: queue finished (s) | 839 → 850.5 (+1.4%); 780.6 → 791.4 (+1.4%); 801.1 → 808.5 (+0.9%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUBERAY_4W_BARE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 144 → 154.5 (+7.3%); 86.83 → 95.32 (+9.8%); 105.8 → 113.5 (+7.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KUBERAY_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 3.0; 0.1 → 1.4 (+1300.0%); 4.0 | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUBERAY_4W_TOP.md` | omni-v25 | L | pod start wait, mean (s) | 0.95; 0.1 → 0.7333 (+633.3%); 1.3716666666666666 | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUEUE.md` | omni-v25 | L | response time (ms), 95th percentile | 2256 → 2395 (+6.1%); 1720 → 1931 (+12.3%); 1676 → 1910 (+13.9%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUEUE.md` | omni-v25 | L | response time (ms), 99th percentile | 3152 → 3412 (+8.2%); 2411 → 2615 (+8.4%); 2345 → 2518 (+7.4%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUEUE.md` | omni-v25 | L | failed requests (%) | 0.0; 0.0; 0.01081 → 0.01117 (+3.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KUEUE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.1 → 13.4 (+2.3%); 10.2 → 11 (+7.8%); 9.4 → 10.5 (+11.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUEUE.md` | omni-v25 | L | pod start wait, total (s) | 0.3 → 2.4 (+700.0%); 0.3 → 3.2 (+966.7%); 6.5 | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUEUE.md` | omni-v25 | L | pod start wait, mean (s) | 0.3 → 1.067 (+255.6%); 0.3 → 1.093 (+264.4%); 2.0799999999999996 | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUEUE.md` | omni-v25 | L | batch: queue finished (s) | 862.8 → 878.5 (+1.8%); 818.4 → 830.6 (+1.5%); 821.1 → 829.4 (+1.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KUEUE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.8 → 7 (+84.2%); 3.4 → 7.4 (+117.6%); 8.3 → 10.4 (+25.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KUEUE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 167.1 → 181.9 (+8.9%); 122.4 → 134.1 (+9.6%); 122.6 → 131.8 (+7.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | L | response time (ms), 95th percentile | 2182 → 2472 (+13.3%); 1558 → 1782 (+14.3%); 1586 → 1755 (+10.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | L | response time (ms), 99th percentile | 3046 → 3450 (+13.3%); 2181 → 2516 (+15.3%); 2208 → 2440 (+10.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | L | failed requests (%) | 0.0; 0.011299435028248588; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 → 12.4 (+3.3%); 9.3 → 10.1 (+8.6%); 9.6 → 10.3 (+7.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 2.4; 0.4 → 4.1 (+925.0%); 2.6 | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | L | pod start wait, mean (s) | 1.3166666666666669; 0.2 → 2.017 (+908.3%); 1.4166666666666665 | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | L | batch: queue finished (s) | 857.9 → 872.4 (+1.7%); 812.7 → 826.3 (+1.7%); 812.3 → 824.9 (+1.6%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.1917 → 0.2917 (+52.2%); 0.3 → 0.3458 (+15.3%); 0.1917 → 0.4833 (+152.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 164.1 → 176.1 (+7.4%); 117.4 → 130.1 (+10.9%); 117.2 → 128.6 (+9.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | response time (ms), 95th percentile | 2249 → 2534 (+12.7%); 1706 → 1893 (+11.0%); 1648 → 1782 (+8.2%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | response time (ms), 99th percentile | 3135 → 3556 (+13.4%); 2401 → 2636 (+9.8%); 2341 → 2447 (+4.5%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | time over the response line (% of samples) | 27.03 → 27.08 (+0.2%); 19.74 → 20.02 (+1.4%); 17.79 → 18.13 (+1.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | failed requests (%) | 0.0; 0.011363636363636364; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.2 → 12.5 (+2.5%); 9.5 → 10.1 (+6.3%); 9.2 → 10.3 (+12.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 2.9; 0.3 → 3.3 (+1000.0%); 2.6 | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | pod start wait, mean (s) | 1.0333333333333334; 0.3 → 1.475 (+391.7%); 1.7 | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | batch: queue finished (s) | 866.5 → 883.2 (+1.9%); 820 → 836.1 (+2.0%); 819.6 → 831.7 (+1.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.6708 → 1.554 (+131.7%); 0.7833 → 1.883 (+140.4%); 0.5125 → 1.367 (+166.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.3 → 11.2 (+239.4%); 3.8 → 11.5 (+202.6%); 3.2 → 9.5 (+196.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 169.7 → 186.1 (+9.7%); 125.9 → 138.5 (+10.1%); 123.8 → 134 (+8.2%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | response time (ms), mean | 756.3 → 857.9 (+13.4%); 487.8 → 566.2 (+16.1%); 775.8 → 872.5 (+12.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | response time (ms), 95th percentile | 2938 → 3443 (+17.2%); 1846 → 2270 (+23.0%); 3104 → 3688 (+18.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | response time (ms), 99th percentile | 3840 → 4696 (+22.3%); 2388 → 2917 (+22.2%); 4122 → 4905 (+19.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | time over the response line (% of samples) | 24.57 → 28.59 (+16.4%); 17.31 → 21.38 (+23.5%); 26.55 → 29.06 (+9.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | failed requests (%) | 0.0; 0.008368200836820083; 0.024402941367866207 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 → 14.4 (+17.1%); 9.4 → 11.2 (+19.1%); 13.2 → 15 (+13.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 0.8 → 6.7 (+737.5%); 0.2 → 8.6 (+4200.0%); 0.6 → 8.2 (+1266.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | pod start wait, mean (s) | 0.8 → 2.215 (+176.9%); 0.2 → 1.848 (+824.0%); 0.6 → 2.777 (+362.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | batch: queue finished (s) | 924.1 → 978.4 (+5.9%); 836.4 → 875.8 (+4.7%); 934.7 → 975.7 (+4.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 229.6 → 282.2 (+22.9%); 145.7 → 182.1 (+25.0%); 240.9 → 275.6 (+14.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | response time (ms), mean | 1046 → 1247 (+19.2%); 661.1 → 846.4 (+28.0%); 1088 → 1256 (+15.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | response time (ms), 95th percentile | 3606 → 4271 (+18.5%); 2275 → 2990 (+31.4%); 3912 → 4261 (+8.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | response time (ms), 99th percentile | 4689 → 5732 (+22.3%); 2995 → 4117 (+37.5%); 5170 → 5461 (+5.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | time over the response line (% of samples) | 36.32 → 43.09 (+18.6%); 26.83 → 34.38 (+28.1%); 35.18 → 43.53 (+23.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.6 → 18.4 (+17.9%); 12.1 → 15.2 (+25.6%); 16.5 → 18.5 (+12.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 11.5; 0.7 → 8.3 (+1085.7%); 14.9 | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | pod start wait, mean (s) | 2.912857142857143; 0.7 → 2.268 (+224.0%); 2.567738095238095 | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | batch: queue finished (s) | 1052 → 1118 (+6.3%); 921.3 → 1004 (+9.0%); 1043 → 1114 (+6.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 17.64 → 25.17 (+42.7%); 3.425 → 15.7 (+358.5%); 15.42 → 19 (+23.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 323.6 → 390.5 (+20.7%); 220.3 → 286.2 (+29.9%); 315.8 → 392.1 (+24.2%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_PGBENCH.md` | omni-v25 | L | simple_update: p50_ms | 1.121 → 1.141 (+1.8%); 1.393 → 1.4 (+0.5%); 0.6277 → 0.628 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_PGBENCH_SERVICE.md` | omni-v25 | L | tpcb_hot: p99_ms | 430.2 → 463.9 (+7.8%); 6.789 → 6.783 (−0.1%); 6.744 → 7.3 (+8.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_REDIS_SHIPPED.md` | omni-v25 | L | large: p95_ms | 0.2414 → 0.2437 (+1.0%); 0.2025 → 0.2025 (+0.0%); 0.2298 → 0.2317 (+0.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ROBUST_KILL.md` | omni-v25 | L | pod start wait, total (s) | 8.1 → 21.4 (+164.2%); 8 → 18.4 (+130.0%); 8.6 → 19.4 (+125.6%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_ROBUST_KILL.md` | omni-v25 | L | pod start wait, mean (s) | 1.489 → 1.727 (+16.0%); 1.44 → 1.673 (+16.2%); 1.489 → 1.706 (+14.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ROBUST_KILL.md` | omni-v25 | L | robust: failed requests in the 300 s after the kill (%) | 49.16 → 56.58 (+15.1%); 60.16 → 68.92 (+14.5%); 46.99 → 52.13 (+10.9%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_ROBUST_KILL.md` | omni-v25 | L | robust: time over the line in the 300 s after the kill (% of samples) | 71.25 → 73.72 (+3.5%); 69.59 → 70.74 (+1.7%); 61.02 → 63.66 (+4.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ROBUST_LONG.md` | omni-v25 | L | pod start wait, total (s) | 7.667 → 25.67 (+234.8%); 8.333 → 18 (+116.0%); 12.67 → 54 (+326.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_ROBUST_LONG.md` | omni-v25 | L | pod start wait, mean (s) | 1.456 → 1.779 (+22.2%); 1.667 → 1.795 (+7.7%); 1.25 → 1.916 (+53.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_SYSBENCH_SHIPPED.md` | omni-v25 | L | burst: p99_ms | 6.67 → 7.098 (+6.4%); 7.387 → 7.893 (+6.8%); 4.491 → 4.871 (+8.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_SYSBENCH_SHIPPED.md` | omni-v25 | L | read_only: p99_ms | 4.103 → 4.11 (+0.2%); 4.543 → 4.569 (+0.6%); 53.52 → 66.46 (+24.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_TRACE_GOOGLE2011.md` | omni-v25 | L | pod start wait, total (s) | 10.6 → 25.3 (+138.7%); 9.6 → 238.2 (+2381.2%); 8.8 → 27.4 (+211.4%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_TRACE_GOOGLE2011.md` | omni-v25 | L | pod start wait, mean (s) | 1.454 → 1.613 (+11.0%); 1.544 → 10.44 (+576.3%); 1.428 → 1.783 (+24.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VANILLA.md` | omni-v25 | L | response time (ms), 95th percentile | 1774 → 1923 (+8.4%); 1895 → 2055 (+8.4%); 1456 → 1636 (+12.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_VANILLA.md` | omni-v25 | L | response time (ms), 99th percentile | 2498 → 2718 (+8.8%); 2618 → 2914 (+11.3%); 2019 → 2282 (+13.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_VANILLA.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 → 11.5 (+10.6%); 11.3 → 11.7 (+3.5%); 8.5 → 8.7 (+2.4%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VANILLA.md` | omni-v25 | L | pod start wait, total (s) | 0.4 → 1.9 (+375.0%); 0.2 → 2 (+900.0%); 0.5 → 2.3 (+360.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VANILLA.md` | omni-v25 | L | pod start wait, mean (s) | 0.4 → 1.183 (+195.8%); 0.2 → 1.25 (+525.0%); 0.5 → 1.2 (+140.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VANILLA.md` | omni-v25 | L | batch: queue finished (s) | 827.1 → 838.5 (+1.4%); 832.7 → 842.8 (+1.2%); 805.4 → 819 (+1.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_VANILLA.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.1125 → 0.375 (+233.3%); 0.1333 → 0.9375 (+603.1%); 0.1 → 0.2875 (+187.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VANILLA.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 → 2.1 (+320.0%); 0.7 → 2.8 (+300.0%); 0.7 → 1.9 (+171.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VANILLA.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 132.2 → 141.3 (+6.9%); 134.9 → 146.4 (+8.5%); 111.5 → 122.9 (+10.2%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_VOLCANO.md` | omni-v25 | L | response time (ms), 95th percentile | 1424 → 1589 (+11.6%); 1674 → 1920 (+14.6%); 1842 → 2064 (+12.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VOLCANO.md` | omni-v25 | L | response time (ms), 99th percentile | 2182 → 2355 (+7.9%); 2648 → 2786 (+5.2%); 2665 → 2955 (+10.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VOLCANO.md` | omni-v25 | L | time over the response line (% of samples) | 13.12 → 13.42 (+2.3%); 15.76 → 16.22 (+2.9%); 16.05 → 16.77 (+4.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VOLCANO.md` | omni-v25 | L | pod start wait, total (s) | 2.2; 0.9; 0.4 → 2.8 (+600.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VOLCANO.md` | omni-v25 | L | pod start wait, mean (s) | 0.8666666666666666; 0.45; 0.4 → 1.467 (+266.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_VOLCANO.md` | omni-v25 | L | batch: queue finished (s) | 824.9 → 833.9 (+1.1%); 845.6 → 856.5 (+1.3%); 843.8 → 861.5 (+2.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_VOLCANO.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.8917 → 1.05 (+17.8%); 0.9583 → 1.046 (+9.1%); 0.8125 → 1.167 (+43.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_VOLCANO.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 → 3.5 (+66.7%); 2.6 → 3.5 (+34.6%); 1.6 → 2.9 (+81.2%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_VOLCANO.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 134.6 → 142.8 (+6.1%); 157 → 166.6 (+6.1%); 157.7 → 173.1 (+9.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | L | response time (ms), 95th percentile | 1741 → 1923 (+10.5%); 1282 → 1418 (+10.7%); 1682 → 1750 (+4.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | L | response time (ms), 99th percentile | 2437 → 2660 (+9.1%); 1777 → 1923 (+8.3%); 2367 → 2403 (+1.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | L | failed requests (%) | 0.023121387283236993; 0.011173184357541898; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 → 10.9 (+3.8%); 7.7 → 8.6 (+11.7%); 10.8 → 10.8 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | L | pod start wait, total (s) | 4.6; 4.1; 0.1 → 2.6 (+2500.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | L | pod start wait, mean (s) | 1.5666666666666667; 1.5083333333333333; 0.1 → 1.5 (+1400.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | L | batch: queue finished (s) | 822.4 → 835.4 (+1.6%); 793.2 → 801.9 (+1.1%); 813.2 → 821.7 (+1.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 → 3.2 (+540.0%); 0.4 → 1 (+150.0%); 1 → 1.4 (+40.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 126.9 → 139.5 (+9.9%); 99.18 → 107.3 (+8.2%); 119 → 126.7 (+6.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | L | response time (ms), 95th percentile | 1570 → 2085 (+32.8%); 1216 → 1322 (+8.7%); 1478 → 1768 (+19.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | L | response time (ms), 99th percentile | 2506 → 2953 (+17.8%); 1848 → 1960 (+6.1%); 2369 → 2617 (+10.4%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 → 9.9 (+6.5%); 6 → 6.3 (+5.0%); 9.7 → 9.9 (+2.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | L | pod start wait, total (s) | 2.1; 1.1; 2.6 | weak; 1 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | L | pod start wait, mean (s) | 0.9666666666666666; 0.5; 1.05 | weak; 1 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | L | batch: queue finished (s) | 833.9 → 852.6 (+2.2%); 804.8 → 814.5 (+1.2%); 830.7 → 841.7 (+1.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.7875 → 1.075 (+36.5%); 0.7833 → 0.8292 (+5.9%); 0.9 → 0.925 (+2.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | L | queue: job turnaround, submitted to done, mean (s) | 143.4 → 162.9 (+13.6%); 115.3 → 123.4 (+7.0%); 145.8 → 155.8 (+6.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_WANDERING.md` | omni-v25 | L | failed requests (%) | 12.16 → 12.18 (+0.2%); 12.16 → 12.69 (+4.4%); 11.76 → 12.21 (+3.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_WANDERING.md` | omni-v25 | L | pod start wait, total (s) | 7.1 → 19.6 (+176.1%); 7.3 → 16.8 (+130.1%); 9.2 → 16 (+73.9%) | strong; 3 of 3 beyond the noise |
| `results/live/V25_YCSB.md` | omni-v25 | L | burst: p99_ms | 0.568 → 0.573 (+0.9%); 0.5917 → 0.602 (+1.7%); 0.5623 → 0.5597 (−0.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_YCSB.md` | omni-v25 | L | burst: mean_ms | 0.2094 → 0.2127 (+1.6%); 0.2149 → 0.2191 (+1.9%); 0.2142 → 0.2136 (−0.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_YCSB_SERVICE.md` | omni-v25 | L | burst: p95_ms | 0.2347 → 0.2407 (+2.6%); 0.433 → 0.4333 (+0.1%); 0.411 → 0.411 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_YCSB_SERVICE.md` | omni-v25 | L | burst: mean_ms | 0.07617 → 0.07848 (+3.0%); 0.2175 → 0.2191 (+0.8%); 0.2157 → 0.2148 (−0.4%) | weak; 1 of 3 beyond the noise |
| `results/live/V25_YCSB_SERVICE.md` | omni-v25 | L | f: work_inside_line_ops | 5693 → 5695 (+0.0%); 5677 → 5683 (+0.1%); 5712 → 5570 (−2.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_YCSB_SERVICE.md` | omni-v25 | L | f: ops | 5716 → 5720 (+0.1%); 5693 → 5699 (+0.1%); 5730 → 5590 (−2.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_YCSB_SHIPPED.md` | omni-v25 | L | b: p95_ms | 0.308 → 0.3157 (+2.5%); 0.3173 → 0.3277 (+3.3%); 0.325 → 0.3253 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_YCSB_SHIPPED.md` | omni-v25 | L | b: mean_ms | 0.1855 → 0.188 (+1.3%); 0.1906 → 0.193 (+1.2%); 0.1909 → 0.1917 (+0.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V25_YCSB_SHIPPED.md` | omni-v25 | L | f: p99_ms | 0.6383 → 0.6373 (−0.2%); 0.6343 → 0.6323 (−0.3%); 0.376 → 0.3853 (+2.5%) | inconclusive; 0 of 3 beyond the noise |

## Stored readings the key reads otherwise (0)

None: every stored reading is the key's reading of its stored values, and every Markdown table prints its JSON's.

## Every table

| Table | Engine | Status | Comparison | Class | Runs |
|---|---|---|---|---|---|
| `results/live/V10_ALL_FOUR.md` | omni-v10 | superseded | against its native | L | A 39107187219 (10 reps, `6d871e2baad1`), B 39114214725 (10 reps, `3b9fc76017ad`), C 39122525181 (10 reps, `faaaff3142e1`) |
| `results/live/V10_BATCH.md` | omni-v10 | superseded | against its native | L | A 39107196814 (10 reps, `6d871e2baad1`), B 39115235566 (10 reps, `f09db2756842`), C 39122536157 (10 reps, `faaaff3142e1`) |
| `results/live/V10_CAPACITY.md` | omni-v10 | superseded | against its native | L | in its own Markdown |
| `results/live/V10_CITYLEARN.md` | omni-v10 | superseded | against its native | S | in its own Markdown |
| `results/live/V10_CRUISEKUBE.md` | omni-v10 | superseded | against its native | L | A 39102512170 (10 reps, `959cb4725a7e`), B 39113183694 (10 reps, `3b9fc76017ad`), C 39120444653 (10 reps, `faaaff3142e1`) |
| `results/live/V10_FAIRNESS.md` | omni-v10 | superseded | against its native | L | A 39107190192 (10 reps, `6d871e2baad1`), B 39114217887 (10 reps, `3b9fc76017ad`), C 39122528801 (10 reps, `faaaff3142e1`) |
| `results/live/V10_FAULTS.md` | omni-v10 | superseded | against its native | L | A 39107193417 (10 reps, `6d871e2baad1`), B 39115232348 (10 reps, `f09db2756842`), C 39122532509 (10 reps, `faaaff3142e1`) |
| `results/live/V10_GOLDILOCKS.md` | omni-v10 | superseded | against its native | L | A 39106189778 (10 reps, `0454fdb0089f`), B 39113187123 (10 reps, `3b9fc76017ad`), C 39120448390 (10 reps, `faaaff3142e1`) |
| `results/live/V10_KAFKA.md` | omni-v10 | superseded | against its native | L | A 39108188053 (? reps, `6d871e2baad1`), B 39116273889 (? reps, `f09db2756842`), C 39123591485 (? reps, `faaaff3142e1`) |
| `results/live/V10_KAFKA_SERVICE.md` | omni-v10 | superseded | against its native | L | A 39109170592 (? reps, `6d871e2baad1`), B 39116292836 (? reps, `f09db2756842`), C 39124642737 (? reps, `8b902df8d857`) |
| `results/live/V10_KEDA_CPU_REQUESTS.md` | omni-v10 | superseded | against its native | L | A 39108180989 (10 reps, `6d871e2baad1`), B 39115242861 (10 reps, `f09db2756842`), C 39123583570 (10 reps, `faaaff3142e1`) |
| `results/live/V10_KEDA_REQUESTS.md` | omni-v10 | superseded | against its native | L | A 39108180989 (10 reps, `6d871e2baad1`), B 39115242861 (10 reps, `f09db2756842`), C 39123583570 (10 reps, `faaaff3142e1`) |
| `results/live/V10_MUJOCO.md` | omni-v10 | superseded | against its native | S | in its own Markdown |
| `results/live/V10_PANDAPOWER.md` | omni-v10 | superseded | against its native | S | in its own Markdown |
| `results/live/V10_PGBENCH.md` | omni-v10 | superseded | against its native | L | A 39108191914 (? reps, `6d871e2baad1`), B 39116277778 (? reps, `f09db2756842`), C 39123595298 (? reps, `faaaff3142e1`) |
| `results/live/V10_REDIS.md` | omni-v10 | superseded | against its native | L | A 39108184403 (? reps, `6d871e2baad1`), B 39115246841 (? reps, `f09db2756842`), C 39123587108 (? reps, `faaaff3142e1`) |
| `results/live/V10_REDIS_SERVICE.md` | omni-v10 | superseded | against its native | L | A 39109167603 (? reps, `6d871e2baad1`), B 39116289213 (? reps, `f09db2756842`), C 39124638850 (? reps, `8b902df8d857`) |
| `results/live/V10_ROBUST_LONG.md` | omni-v10 | superseded | against its native | L | A 39111154503 (3 reps, `13f22e8141c4`), B 39119406616 (3 reps, `faaaff3142e1`), C 39126745660 (3 reps, `56e00223da79`) |
| `results/live/V10_STEADY.md` | omni-v10 | superseded | against its native | L | A 39107180703 (10 reps, `6d871e2baad1`), B 39114207589 (10 reps, `3b9fc76017ad`), C 39121472594 (10 reps, `faaaff3142e1`) |
| `results/live/V10_SWARM.md` | omni-v10 | superseded | against its native | S | in its own Markdown |
| `results/live/V10_SYSBENCH.md` | omni-v10 | superseded | against its native | L | A 39108195807 (? reps, `6d871e2baad1`), B 39116281643 (? reps, `f09db2756842`), C 39123599130 (? reps, `faaaff3142e1`) |
| `results/live/V10_TRACE_GOOGLE2011.md` | omni-v10 | superseded | against its native | L | A 39108177259 (10 reps, `6d871e2baad1`), B 39115239009 (10 reps, `f09db2756842`), C 39122539586 (10 reps, `faaaff3142e1`) |
| `results/live/V10_WANDERING.md` | omni-v10 | superseded | against its native | L | A 39107183748 (10 reps, `6d871e2baad1`), B 39114211206 (10 reps, `3b9fc76017ad`), C 39122521784 (10 reps, `faaaff3142e1`) |
| `results/live/V10_YCSB.md` | omni-v10 | superseded | against its native | L | A 39109164668 (? reps, `6d871e2baad1`), B 39116285471 (? reps, `f09db2756842`), C 39124635012 (? reps, `8b902df8d857`) |
| `results/live/V11_CAPACITY.md` | omni-v11 | superseded | against its native | L | in its own Markdown |
| `results/live/V11_CITYLEARN.md` | omni-v11 | superseded | against its native | S | in its own Markdown |
| `results/live/V11_GOLDILOCKS.md` | omni-v11 | superseded | against its native | L | A 39171064099 (10 reps, `f445e205073f`), B 39175675418 (10 reps, `df871e4396dc`), C 39177950720 (10 reps, `0d11e5ab281c`) |
| `results/live/V11_KAFKA.md` | omni-v11 | superseded | against its native | L | A 39149249969 (? reps, `d44261ca0c5c`), B 39157787056 (? reps, `5031411ae285`), C 39166374877 (? reps, `8472aaad2bf4`) |
| `results/live/V11_KAFKA_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39150481307 (? reps, `c1c1b59711b1`), B 39159000835 (? reps, `3cb376bb3284`), C 39167574190 (? reps, `e2d5958834f5`) |
| `results/live/V11_KEDA_CPU_REQUESTS.md` | omni-v11 | superseded | against its native | L | A 39173411511 (10 reps, `8de24035ac07`), B 39176842679 (10 reps, `2a2cfc67147e`), C 39180252225 (10 reps, `7b7dd69870e7`) |
| `results/live/V11_KEDA_REQUESTS.md` | omni-v11 | superseded | against its native | L | A 39173411511 (10 reps, `8de24035ac07`), B 39176842679 (10 reps, `2a2cfc67147e`), C 39180252225 (10 reps, `7b7dd69870e7`) |
| `results/live/V11_MUJOCO.md` | omni-v11 | superseded | against its native | S | in its own Markdown |
| `results/live/V11_PANDAPOWER.md` | omni-v11 | superseded | against its native | S | in its own Markdown |
| `results/live/V11_PGBENCH.md` | omni-v11 | superseded | against its native | L | A 39149254727 (? reps, `d44261ca0c5c`), B 39157791268 (? reps, `5031411ae285`), C 39166378754 (? reps, `8472aaad2bf4`) |
| `results/live/V11_PGBENCH_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39182915425 (? reps, `bc2eb38f4ca8`), B 39184166001 (? reps, `75478eb28444`), C 39185403353 (? reps, `ce92ff888e73`) |
| `results/live/V11_REDIS.md` | omni-v11 | superseded | against its native | L | A 39149244903 (? reps, `d44261ca0c5c`), B 39157782849 (? reps, `5031411ae285`), C 39166371110 (? reps, `8472aaad2bf4`) |
| `results/live/V11_REDIS_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39149267883 (? reps, `d44261ca0c5c`), B 39158996767 (? reps, `3cb376bb3284`), C 39167569649 (? reps, `e2d5958834f5`) |
| `results/live/V11_REDIS_SHIPPED.md` | omni-v11 | superseded | against its native | L | A 39150490855 (? reps, `c1c1b59711b1`), B 39159008310 (? reps, `3cb376bb3284`), C 39167582853 (? reps, `e2d5958834f5`) |
| `results/live/V11_ROBUST_KILL.md` | omni-v11 | superseded | against its native | L | A 39173416105 (10 reps, `8de24035ac07`), B 39177935888 (10 reps, `0d11e5ab281c`), C 39182898753 (10 reps, `bc2eb38f4ca8`) |
| `results/live/V11_ROBUST_LONG.md` | omni-v11 | superseded | against its native | L | A 39173420146 (3 reps, `8de24035ac07`), B 39177939062 (3 reps, `0d11e5ab281c`), C 39182902844 (3 reps, `bc2eb38f4ca8`) |
| `results/live/V11_SWARM.md` | omni-v11 | superseded | against its native | S | in its own Markdown |
| `results/live/V11_SYSBENCH.md` | omni-v11 | superseded | against its native | L | A 39149259396 (? reps, `d44261ca0c5c`), B 39157795408 (? reps, `5031411ae285`), C 39166382450 (? reps, `8472aaad2bf4`) |
| `results/live/V11_SYSBENCH_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39182906799 (? reps, `bc2eb38f4ca8`), B 39184157413 (? reps, `75478eb28444`), C 39184175254 (? reps, `75478eb28444`) |
| `results/live/V11_SYSBENCH_SHIPPED.md` | omni-v11 | superseded | against its native | L | A 39150486066 (? reps, `c1c1b59711b1`), B 39159004803 (? reps, `3cb376bb3284`), C 39167578494 (? reps, `e2d5958834f5`) |
| `results/live/V11_YCSB.md` | omni-v11 | superseded | against its native | L | A 39149263618 (? reps, `d44261ca0c5c`), B 39158992412 (? reps, `3cb376bb3284`), C 39167564949 (? reps, `e2d5958834f5`) |
| `results/live/V11_YCSB_SERVICE.md` | omni-v11 | superseded | against its native | L | A 39182911063 (? reps, `bc2eb38f4ca8`), B 39184161631 (? reps, `75478eb28444`), C 39184179710 (? reps, `75478eb28444`) |
| `results/live/V11_YCSB_SHIPPED.md` | omni-v11 | superseded | against its native | L | A 39150495654 (? reps, `c1c1b59711b1`), B 39160201436 (? reps, `773cd59cfdd2`), C 39169863638 (? reps, `2b4c11e3aee0`) |
| `results/live/V12_ARMADA_4W_BARE.md` | omni-v12 | superseded | against its native | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_ARMADA_4W_BOTH.md` | omni-v12 | superseded | two changes at once | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_ARMADA_4W_ORCH.md` | omni-v12 | superseded | the orchestrator's own | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_ARMADA_4W_TOP.md` | omni-v12 | superseded | against its native | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_ARMADA_4W_VS.md` | omni-v12 | superseded | in place of a controller | L | A 39482335827 (9 reps, `adfabdc8355f`), B 39482351075 (10 reps, `adfabdc8355f`), C 39482365814 (10 reps, `adfabdc8355f`) |
| `results/live/V12_BINPACK.md` | omni-v12 | superseded | against its native | L | A 39356578556 (10 reps, `1ca982cf97db`), B 39356594135 (10 reps, `1ca982cf97db`), C 39356608147 (10 reps, `1ca982cf97db`) |
| `results/live/V12_BINPACK_4W_BARE.md` | omni-v12 | superseded | against its native | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_BINPACK_4W_BOTH.md` | omni-v12 | superseded | two changes at once | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_BINPACK_4W_ORCH.md` | omni-v12 | superseded | the orchestrator's own | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_BINPACK_4W_TOP.md` | omni-v12 | superseded | against its native | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_BINPACK_4W_VS.md` | omni-v12 | superseded | in place of a controller | L | A 39368428763 (10 reps, `cf4235e29cb4`), B 39368435483 (10 reps, `cf4235e29cb4`), C 39368442002 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_CRANE_4W_BARE.md` | omni-v12 | superseded | against its native | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_CRANE_4W_BOTH.md` | omni-v12 | superseded | two changes at once | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_CRANE_4W_ORCH.md` | omni-v12 | superseded | the orchestrator's own | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_CRANE_4W_TOP.md` | omni-v12 | superseded | against its native | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_CRANE_4W_VS.md` | omni-v12 | superseded | in place of a controller | L | A 39438326588 (10 reps, `b1e552d38424`), B 39438344234 (10 reps, `b1e552d38424`), C 39438362894 (10 reps, `b1e552d38424`) |
| `results/live/V12_KAFKA.md` | omni-v12 | superseded | against its native | L | A 39379918375 (? reps, `690b955b1c2a`), B 39410587818 (? reps, `690b955b1c2a`), C 39459233023 (? reps, `6f4be24ffb43`) |
| `results/live/V12_KAFKA_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39381455200 (? reps, `690b955b1c2a`), B 39412428649 (? reps, `690b955b1c2a`), C 39461523366 (? reps, `6f4be24ffb43`) |
| `results/live/V12_KAI.md` | omni-v12 | superseded | against its native | L | A 39350900880 (10 reps, `7dee891c54d1`), B 39350907916 (10 reps, `7dee891c54d1`), C 39350915166 (10 reps, `7dee891c54d1`) |
| `results/live/V12_KAI_4W_BARE.md` | omni-v12 | superseded | against its native | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KAI_4W_BOTH.md` | omni-v12 | superseded | two changes at once | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KAI_4W_ORCH.md` | omni-v12 | superseded | the orchestrator's own | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KAI_4W_TOP.md` | omni-v12 | superseded | against its native | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KAI_4W_VS.md` | omni-v12 | superseded | in place of a controller | L | A 39368344021 (10 reps, `cf4235e29cb4`), B 39368351097 (10 reps, `cf4235e29cb4`), C 39368358521 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KARMADA_4W_BARE.md` | omni-v12 | superseded | against its native | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KARMADA_4W_BOTH.md` | omni-v12 | superseded | two changes at once | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KARMADA_4W_ORCH.md` | omni-v12 | superseded | the orchestrator's own | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KARMADA_4W_TOP.md` | omni-v12 | superseded | against its native | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KARMADA_4W_VS.md` | omni-v12 | superseded | in place of a controller | L | A 39438525862 (9 reps, `b1e552d38424`), B 39438541616 (10 reps, `b1e552d38424`), C 39438559009 (10 reps, `b1e552d38424`) |
| `results/live/V12_KOORDINATOR.md` | omni-v12 | superseded | against its native | L | A 39359085965 (10 reps, `28a65e160d68`), B 39359094679 (10 reps, `28a65e160d68`), C 39359103518 (10 reps, `28a65e160d68`) |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | standing | against its native | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KOORDINATOR_4W_BOTH.md` | omni-v12 | standing | two changes at once | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KOORDINATOR_4W_ORCH.md` | omni-v12 | standing | the orchestrator's own | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | standing | against its native | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KOORDINATOR_4W_VS.md` | omni-v12 | standing | in place of a controller | L | A 39368366066 (10 reps, `cf4235e29cb4`), B 39368373713 (10 reps, `cf4235e29cb4`), C 39368380786 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_KUBERAY_4W_BARE.md` | omni-v12 | superseded | against its native | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUBERAY_4W_BOTH.md` | omni-v12 | superseded | two changes at once | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUBERAY_4W_ORCH.md` | omni-v12 | superseded | the orchestrator's own | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUBERAY_4W_TOP.md` | omni-v12 | superseded | against its native | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUBERAY_4W_VS.md` | omni-v12 | superseded | in place of a controller | L | A 39438462925 (9 reps, `b1e552d38424`), B 39438478652 (10 reps, `b1e552d38424`), C 39438494234 (10 reps, `b1e552d38424`) |
| `results/live/V12_KUEUE_4W_BARE.md` | omni-v12 | superseded | against its native | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_KUEUE_4W_BOTH.md` | omni-v12 | superseded | two changes at once | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_KUEUE_4W_ORCH.md` | omni-v12 | superseded | the orchestrator's own | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_KUEUE_4W_TOP.md` | omni-v12 | superseded | against its native | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_KUEUE_4W_VS.md` | omni-v12 | superseded | in place of a controller | L | A 39368387821 (10 reps, `cf4235e29cb4`), B 39368394823 (10 reps, `cf4235e29cb4`), C 39368401852 (9 reps, `cf4235e29cb4`) |
| `results/live/V12_OCM_4W_BARE.md` | omni-v12 | superseded | against its native | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_OCM_4W_BOTH.md` | omni-v12 | superseded | two changes at once | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_OCM_4W_ORCH.md` | omni-v12 | superseded | the orchestrator's own | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_OCM_4W_TOP.md` | omni-v12 | superseded | against its native | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_OCM_4W_VS.md` | omni-v12 | superseded | in place of a controller | L | A 39479807336 (10 reps, `00ec0be44be7`), B 39479824367 (10 reps, `00ec0be44be7`), C 39479840381 (10 reps, `00ec0be44be7`) |
| `results/live/V12_PGBENCH.md` | omni-v12 | superseded | against its native | L | A 39379923601 (? reps, `690b955b1c2a`), B 39410594381 (? reps, `690b955b1c2a`), C 39459241206 (? reps, `6f4be24ffb43`) |
| `results/live/V12_PGBENCH_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39473169216 (? reps, `ac0eeaef8ecc`), B 39477818906 (? reps, `fb90309cad0d`), C 39491674383 (? reps, `de8da62736d4`) |
| `results/live/V12_REDIS.md` | omni-v12 | superseded | against its native | L | A 39367385496 (? reps, `15654388e112`), B 39408770553 (? reps, `690b955b1c2a`), C 39459224023 (? reps, `6f4be24ffb43`) |
| `results/live/V12_REDIS_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39381449955 (? reps, `690b955b1c2a`), B 39412421481 (? reps, `690b955b1c2a`), C 39461515383 (? reps, `6f4be24ffb43`) |
| `results/live/V12_REDIS_SHIPPED.md` | omni-v12 | superseded | against its native | L | A 39382995467 (? reps, `690b955b1c2a`), B 39414279979 (? reps, `690b955b1c2a`), C 39461540163 (? reps, `6f4be24ffb43`) |
| `results/live/V12_SYSBENCH.md` | omni-v12 | superseded | against its native | L | A 39379929041 (? reps, `690b955b1c2a`), B 39410600428 (? reps, `690b955b1c2a`), C 39461498952 (? reps, `6f4be24ffb43`) |
| `results/live/V12_SYSBENCH_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39468576581 (? reps, `80843e7684b3`), B 39473186537 (? reps, `ac0eeaef8ecc`), C 39477834359 (? reps, `fb90309cad0d`) |
| `results/live/V12_SYSBENCH_SHIPPED.md` | omni-v12 | superseded | against its native | L | A 39382990197 (? reps, `690b955b1c2a`), B 39412436421 (? reps, `690b955b1c2a`), C 39461531771 (? reps, `6f4be24ffb43`) |
| `results/live/V12_VANILLA.md` | omni-v12 | superseded | against its native | L | A 39356571014 (10 reps, `1ca982cf97db`), B 39356586356 (10 reps, `1ca982cf97db`), C 39356601235 (10 reps, `1ca982cf97db`) |
| `results/live/V12_VOLCANO_4W_BARE.md` | omni-v12 | superseded | against its native | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_VOLCANO_4W_BOTH.md` | omni-v12 | superseded | two changes at once | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_VOLCANO_4W_ORCH.md` | omni-v12 | superseded | the orchestrator's own | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_VOLCANO_4W_TOP.md` | omni-v12 | superseded | against its native | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_VOLCANO_4W_VS.md` | omni-v12 | superseded | in place of a controller | L | A 39368409208 (10 reps, `cf4235e29cb4`), B 39368415819 (10 reps, `cf4235e29cb4`), C 39368422189 (10 reps, `cf4235e29cb4`) |
| `results/live/V12_YCSB.md` | omni-v12 | superseded | against its native | L | A 39379934444 (? reps, `690b955b1c2a`), B 39410606870 (? reps, `690b955b1c2a`), C 39461506751 (? reps, `6f4be24ffb43`) |
| `results/live/V12_YCSB_SERVICE.md` | omni-v12 | superseded | against its native | L | A 39470845655 (? reps, `ac0eeaef8ecc`), B 39475514914 (? reps, `fb90309cad0d`), C 39477842603 (? reps, `fb90309cad0d`) |
| `results/live/V12_YCSB_SHIPPED.md` | omni-v12 | superseded | against its native | L | A 39383000915 (? reps, `690b955b1c2a`), B 39414286889 (? reps, `690b955b1c2a`), C 39463721089 (? reps, `6f4be24ffb43`) |
| `results/live/V14_PGBENCH_SERVICE.md` | omni-v14 | superseded | against its native | L | A 39625603596 (? reps, `e32bbb605501`), B 39628245625 (? reps, `990711a99dc4`), C 39630669154 (? reps, `67b7cd6bf1e8`) |
| `results/live/V14_SYSBENCH_SERVICE.md` | omni-v14 | superseded | against its native | L | A 39623235693 (? reps, `e32bbb605501`), B 39625624640 (? reps, `e32bbb605501`), C 39630651710 (? reps, `67b7cd6bf1e8`) |
| `results/live/V14_YCSB_SERVICE.md` | omni-v14 | superseded | against its native | L | A 39623244880 (? reps, `e32bbb605501`), B 39628035584 (? reps, `990711a99dc4`), C 39630660108 (? reps, `67b7cd6bf1e8`) |
| `results/live/V14_YCSB_SHIPPED.md` | omni-v14 | superseded | against its native | L | A 39562510452 (? reps, `418f860a4da6`), B 39590117126 (? reps, `e997ca0d9f65`), C 39616239634 (? reps, `63a093f13de0`) |
| `results/live/V16_KAFKA.md` | omni-v16 | superseded | against its native | L | A 39821402572 (? reps, `611aad4666db`), B 39840024618 (? reps, `d27db5f66c71`), C 39860244280 (? reps, `15915c961cd2`) |
| `results/live/V16_KAFKA_SERVICE.md` | omni-v16 | superseded | against its native | L | A 39823828673 (? reps, `611aad4666db`), B 39844651167 (? reps, `d27db5f66c71`), C 39864227589 (? reps, `681ff70efadd`) |
| `results/live/V16_PGBENCH.md` | omni-v16 | superseded | against its native | L | A 39842347137 (? reps, `d27db5f66c71`), B 39851575564 (? reps, `36cb1cc37947`), C 39860251731 (? reps, `15915c961cd2`) |
| `results/live/V16_PGBENCH_SERVICE.md` | omni-v16 | superseded | against its native | L | A 39869913163 (? reps, `464fb9e27535`), B 39871667274 (? reps, `464fb9e27535`), C 39873437772 (? reps, `a9694fbc7d2a`) |
| `results/live/V16_REDIS.md` | omni-v16 | superseded | against its native | L | A 39821393310 (? reps, `611aad4666db`), B 39840016313 (? reps, `d27db5f66c71`), C 39860237154 (? reps, `15915c961cd2`) |
| `results/live/V16_REDIS_SERVICE.md` | omni-v16 | superseded | against its native | L | A 39823820262 (? reps, `611aad4666db`), B 39844642925 (? reps, `d27db5f66c71`), C 39862248686 (? reps, `681ff70efadd`) |
| `results/live/V16_REDIS_SHIPPED.md` | omni-v16 | superseded | against its native | L | A 39826081107 (? reps, `611aad4666db`), B 39846960314 (? reps, `d27db5f66c71`), C 39866161041 (? reps, `5f430c111d90`) |
| `results/live/V16_SYSBENCH.md` | omni-v16 | superseded | against its native | L | A 39823802516 (? reps, `611aad4666db`), B 39842355356 (? reps, `d27db5f66c71`), C 39862234914 (? reps, `15915c961cd2`) |
| `results/live/V16_SYSBENCH_SERVICE.md` | omni-v16 | superseded | against its native | L | A 39869901058 (? reps, `464fb9e27535`), B 39869925397 (? reps, `464fb9e27535`), C 39871679567 (? reps, `464fb9e27535`) |
| `results/live/V16_SYSBENCH_SHIPPED.md` | omni-v16 | superseded | against its native | L | A 39826073316 (? reps, `611aad4666db`), B 39846952545 (? reps, `d27db5f66c71`), C 39864234559 (? reps, `681ff70efadd`) |
| `results/live/V16_YCSB.md` | omni-v16 | superseded | against its native | L | A 39823811507 (? reps, `611aad4666db`), B 39842363997 (? reps, `d27db5f66c71`), C 39862241743 (? reps, `681ff70efadd`) |
| `results/live/V16_YCSB_SERVICE.md` | omni-v16 | superseded | against its native | L | A 39869906902 (? reps, `464fb9e27535`), B 39871660953 (? reps, `464fb9e27535`), C 39871685303 (? reps, `464fb9e27535`) |
| `results/live/V16_YCSB_SHIPPED.md` | omni-v16 | superseded | against its native | L | A 39826088859 (? reps, `611aad4666db`), B 39846968680 (? reps, `d27db5f66c71`), C 39866167058 (? reps, `5f430c111d90`) |
| `results/live/V17_KAFKA.md` | omni-v17 | superseded | against its native | L | A 40003710547 (? reps, `b525b7a07a0c`), B 40020507060 (? reps, `6fcdf41aad34`), C 40035619419 (? reps, `6e4b64630bfc`) |
| `results/live/V17_KAFKA_SERVICE.md` | omni-v17 | superseded | against its native | L | A 40005908588 (? reps, `b525b7a07a0c`), B 40022521256 (? reps, `6fcdf41aad34`), C 40037209884 (? reps, `6e4b64630bfc`) |
| `results/live/V17_PGBENCH.md` | omni-v17 | superseded | against its native | L | A 40003718316 (? reps, `b525b7a07a0c`), B 40022493643 (? reps, `6fcdf41aad34`), C 40037187971 (? reps, `6e4b64630bfc`) |
| `results/live/V17_PGBENCH_SERVICE.md` | omni-v17 | superseded | against its native | L | A 40043218026 (? reps, `f22776e60a87`), B 40044599601 (? reps, `0d532c7a2dbd`), C 40045930230 (? reps, `e4a97f22dce1`) |
| `results/live/V17_REDIS.md` | omni-v17 | superseded | against its native | L | A 39999416157 (? reps, `9678c8ad4325`), B 40020500663 (? reps, `6fcdf41aad34`), C 40035613178 (? reps, `6e4b64630bfc`) |
| `results/live/V17_REDIS_SERVICE.md` | omni-v17 | superseded | against its native | L | A 40005899721 (? reps, `b525b7a07a0c`), B 40022515018 (? reps, `6fcdf41aad34`), C 40037204297 (? reps, `6e4b64630bfc`) |
| `results/live/V17_REDIS_SHIPPED.md` | omni-v17 | superseded | against its native | L | A 40005925354 (? reps, `b525b7a07a0c`), B 40024478954 (? reps, `6fcdf41aad34`), C 40038802348 (? reps, `d02c7052ae50`) |
| `results/live/V17_SYSBENCH.md` | omni-v17 | superseded | against its native | L | A 40003726359 (? reps, `b525b7a07a0c`), B 40022500639 (? reps, `6fcdf41aad34`), C 40037193927 (? reps, `6e4b64630bfc`) |
| `results/live/V17_SYSBENCH_SERVICE.md` | omni-v17 | superseded | against its native | L | A 40043207507 (? reps, `f22776e60a87`), B 40044589141 (? reps, `0d532c7a2dbd`), C 40045921684 (? reps, `e4a97f22dce1`) |
| `results/live/V17_SYSBENCH_SHIPPED.md` | omni-v17 | superseded | against its native | L | A 40005917048 (? reps, `b525b7a07a0c`), B 40024472453 (? reps, `6fcdf41aad34`), C 40038796458 (? reps, `d02c7052ae50`) |
| `results/live/V17_YCSB.md` | omni-v17 | superseded | against its native | L | A 40003734350 (? reps, `b525b7a07a0c`), B 40022507977 (? reps, `6fcdf41aad34`), C 40037199208 (? reps, `6e4b64630bfc`) |
| `results/live/V17_YCSB_SERVICE.md` | omni-v17 | superseded | against its native | L | A 40043212711 (? reps, `f22776e60a87`), B 40044594345 (? reps, `0d532c7a2dbd`), C 40045925918 (? reps, `e4a97f22dce1`) |
| `results/live/V17_YCSB_SHIPPED.md` | omni-v17 | superseded | against its native | L | A 40008048292 (? reps, `b525b7a07a0c`), B 40024485005 (? reps, `6fcdf41aad34`), C 40038808111 (? reps, `d02c7052ae50`) |
| `results/live/V18_KAFKA.md` | omni-v18 | superseded | against its native | L | A 40062228122 (? reps, `bbf7e12f0467`), B 40067527221 (? reps, `dadeec62a61a`), C 40130177581 (? reps, `791ad0fd93b1`) |
| `results/live/V18_KAFKA_SERVICE.md` | omni-v18 | superseded | against its native | L | A 40062235164 (? reps, `bbf7e12f0467`), B 40067533814 (? reps, `dadeec62a61a`), C 40131354530 (? reps, `791ad0fd93b1`) |
| `results/live/V18_PGBENCH_SERVICE.md` | omni-v18 | superseded | against its native | L | A 40135948429 (? reps, `19db275eb391`), B 40137076834 (? reps, `19db275eb391`), C 40138213124 (? reps, `96ebf29137fe`) |
| `results/live/V18_REDIS.md` | omni-v18 | superseded | against its native | L | A 40062224314 (? reps, `bbf7e12f0467`), B 40067523758 (? reps, `dadeec62a61a`), C 40130173076 (? reps, `791ad0fd93b1`) |
| `results/live/V18_REDIS_SERVICE.md` | omni-v18 | superseded | against its native | L | A 40062231655 (? reps, `bbf7e12f0467`), B 40067530395 (? reps, `dadeec62a61a`), C 40131350933 (? reps, `791ad0fd93b1`) |
| `results/live/V18_REDIS_SHIPPED.md` | omni-v18 | superseded | against its native | L | A 40062238903 (? reps, `bbf7e12f0467`), B 40068587953 (? reps, `dadeec62a61a`), C 40132491116 (? reps, `791ad0fd93b1`) |
| `results/live/V18_SYSBENCH_SERVICE.md` | omni-v18 | superseded | against its native | L | A 40134818204 (? reps, `7743f2e82851`), B 40135957187 (? reps, `19db275eb391`), C 40137084068 (? reps, `19db275eb391`) |
| `results/live/V18_YCSB_SERVICE.md` | omni-v18 | superseded | against its native | L | A 40135943683 (? reps, `19db275eb391`), B 40137072959 (? reps, `19db275eb391`), C 40138209461 (? reps, `96ebf29137fe`) |
| `results/live/V1_ALL_FOUR.md` | omni-v1 | the road | against its native | L | A 37384945573 (10 reps, `f162ce8d74e8`), B 37385646550 (10 reps, `f162ce8d74e8`), C 37394444337 (10 reps, `68d9bd172605`) |
| `results/live/V1_BATCH.md` | omni-v1 | the road | against its native | L | A 37385637932 (10 reps, `f162ce8d74e8`), B 37385654462 (10 reps, `f162ce8d74e8`), C 37394452486 (10 reps, `68d9bd172605`) |
| `results/live/V1_CITYLEARN.md` | omni-v1 | the road | against its native | S | in its own Markdown |
| `results/live/V1_FAIRNESS.md` | omni-v1 | the road | against its native | L | A 37384948340 (10 reps, `f162ce8d74e8`), B 37385649261 (10 reps, `f162ce8d74e8`), C 37391303438 (10 reps, `029340abf30c`) |
| `results/live/V1_FAULTS.md` | omni-v1 | the road | against its native | L | A 37384951397 (10 reps, `f162ce8d74e8`), B 37385651747 (10 reps, `f162ce8d74e8`), C 37391310157 (10 reps, `029340abf30c`) |
| `results/live/V1_MUJOCO.md` | omni-v1 | the road | against its native | S | in its own Markdown |
| `results/live/V1_MUJOCO_PANDA.md` | omni-v1 | the road | against its native | S | in its own Markdown |
| `results/live/V1_PANDAPOWER.md` | omni-v1 | the road | against its native | S | in its own Markdown |
| `results/live/V1_STEADY.md` | omni-v1 | the road | against its native | L | A 37384939815 (10 reps, `f162ce8d74e8`), B 37385640601 (10 reps, `f162ce8d74e8`), C 37391296025 (10 reps, `029340abf30c`) |
| `results/live/V1_WANDERING.md` | omni-v1 | the road | against its native | L | A 37384942870 (10 reps, `f162ce8d74e8`), B 37385643291 (10 reps, `f162ce8d74e8`), C 37394436586 (10 reps, `68d9bd172605`) |
| `results/live/V21_ALL_FOUR.md` | omni-v21 | superseded | against its native | L | A 40227146512 (10 reps, `433bcf30d2ad`), B 40250382783 (10 reps, `ddc44f445d06`), C 40272629580 (10 reps, `b659f0eebc58`) |
| `results/live/V21_BATCH.md` | omni-v21 | superseded | against its native | L | A 40230821800 (10 reps, `277a6f3e33c0`), B 40251625381 (10 reps, `ddc44f445d06`), C 40274018452 (10 reps, `b659f0eebc58`) |
| `results/live/V21_CAPACITY.md` | omni-v21 | superseded | against its native | L | in its own Markdown |
| `results/live/V21_CITYLEARN.md` | omni-v21 | superseded | against its native | S | in its own Markdown |
| `results/live/V21_CRUISEKUBE.md` | omni-v21 | superseded | against its native | L | A 40220956277 (10 reps, `f0c1c431231c`), B 40245486755 (10 reps, `22138ecd5b5a`), C 40267226299 (10 reps, `b659f0eebc58`) |
| `results/live/V21_FAIRNESS.md` | omni-v21 | superseded | against its native | L | A 40227151053 (10 reps, `433bcf30d2ad`), B 40250387280 (10 reps, `ddc44f445d06`), C 40272634568 (10 reps, `b659f0eebc58`) |
| `results/live/V21_FAULTS.md` | omni-v21 | superseded | against its native | L | A 40229598467 (10 reps, `277a6f3e33c0`), B 40250391552 (10 reps, `ddc44f445d06`), C 40272639170 (10 reps, `b659f0eebc58`) |
| `results/live/V21_GOLDILOCKS.md` | omni-v21 | superseded | against its native | L | A 40222183655 (10 reps, `f0c1c431231c`), B 40245490699 (10 reps, `22138ecd5b5a`), C 40267231266 (10 reps, `b659f0eebc58`) |
| `results/live/V21_KAFKA.md` | omni-v21 | superseded | against its native | L | A 40256717947 (? reps, `a9f3cc761821`), B 40279909158 (? reps, `796063486f34`), C 40400868003 (? reps, `5e222aa21371`) |
| `results/live/V21_KAFKA_SERVICE.md` | omni-v21 | superseded | against its native | L | A 40236926576 (? reps, `23c7e8eb27be`), B 40259312876 (? reps, `b659f0eebc58`), C 40283010023 (? reps, `b11b4d3825b1`) |
| `results/live/V21_KEDA_CPU_REQUESTS.md` | omni-v21 | superseded | against its native | L | A 40232040937 (10 reps, `5ce458c7e7d2`), B 40254201062 (10 reps, `babd7a2ceac0`), C 40276902708 (10 reps, `796063486f34`) |
| `results/live/V21_KEDA_REQUESTS.md` | omni-v21 | superseded | against its native | L | A 40232040937 (10 reps, `5ce458c7e7d2`), B 40254201062 (10 reps, `babd7a2ceac0`), C 40276902708 (10 reps, `796063486f34`) |
| `results/live/V21_MUJOCO.md` | omni-v21 | superseded | against its native | S | in its own Markdown |
| `results/live/V21_PANDAPOWER.md` | omni-v21 | superseded | against its native | S | in its own Markdown |
| `results/live/V21_PGBENCH.md` | omni-v21 | superseded | against its native | L | A 40258014810 (? reps, `b659f0eebc58`), B 40281459100 (? reps, `fa6da97bbaa6`), C 40400963499 (? reps, `5e222aa21371`) |
| `results/live/V21_PGBENCH_SERVICE.md` | omni-v21 | superseded | against its native | L | A 40289615442 (? reps, `b11b4d3825b1`), B 40293188618 (? reps, `2d426169d766`), C 40295032874 (? reps, `c8b8e2af081f`) |
| `results/live/V21_REDIS.md` | omni-v21 | superseded | against its native | L | A 40254205224 (? reps, `babd7a2ceac0`), B 40276907808 (? reps, `796063486f34`), C 40400989005 (? reps, `5e222aa21371`) |
| `results/live/V21_REDIS_SERVICE.md` | omni-v21 | superseded | against its native | L | A 40236922598 (? reps, `23c7e8eb27be`), B 40259308169 (? reps, `b659f0eebc58`), C 40281475145 (? reps, `fa6da97bbaa6`) |
| `results/live/V21_REDIS_SHIPPED.md` | omni-v21 | superseded | against its native | L | A 40238126261 (? reps, `2d40c4c64109`), B 40260615533 (? reps, `b659f0eebc58`), C 40283020884 (? reps, `b11b4d3825b1`) |
| `results/live/V21_ROBUST_KILL.md` | omni-v21 | superseded | against its native | L | A 40240618830 (10 reps, `4a294bb71d0f`), B 40261931876 (10 reps, `b659f0eebc58`), C 40286252440 (10 reps, `b11b4d3825b1`) |
| `results/live/V21_ROBUST_LONG.md` | omni-v21 | superseded | against its native | L | A 40240697625 (3 reps, `4a294bb71d0f`), B 40261936964 (3 reps, `b659f0eebc58`), C 40286258686 (3 reps, `b11b4d3825b1`) |
| `results/live/V21_STEADY.md` | omni-v21 | superseded | against its native | L | A 40223431219 (10 reps, `433bcf30d2ad`), B 40246652453 (10 reps, `22138ecd5b5a`), C 40269968227 (10 reps, `b659f0eebc58`) |
| `results/live/V21_SWARM.md` | omni-v21 | superseded | against its native | S | in its own Markdown |
| `results/live/V21_SYSBENCH.md` | omni-v21 | superseded | against its native | L | A 40258018856 (? reps, `b659f0eebc58`), B 40281464587 (? reps, `fa6da97bbaa6`), C 40401032384 (? reps, `5e222aa21371`) |
| `results/live/V21_SYSBENCH_SERVICE.md` | omni-v21 | superseded | against its native | L | A 40286351408 (? reps, `b11b4d3825b1`), B 40291369516 (? reps, `f70084ae1bb3`), C 40293202427 (? reps, `2d426169d766`) |
| `results/live/V21_SYSBENCH_SHIPPED.md` | omni-v21 | superseded | against its native | L | A 40236930776 (? reps, `23c7e8eb27be`), B 40259317345 (? reps, `b659f0eebc58`), C 40283015397 (? reps, `b11b4d3825b1`) |
| `results/live/V21_TRACE_GOOGLE2011.md` | omni-v21 | superseded | against its native | L | A 40232036723 (10 reps, `5ce458c7e7d2`), B 40252903510 (10 reps, `babd7a2ceac0`), C 40275448206 (10 reps, `b659f0eebc58`) |
| `results/live/V21_WANDERING.md` | omni-v21 | superseded | against its native | L | A 40227141899 (10 reps, `433bcf30d2ad`), B 40250378687 (10 reps, `ddc44f445d06`), C 40271292066 (10 reps, `b659f0eebc58`) |
| `results/live/V21_YCSB.md` | omni-v21 | superseded | against its native | L | A 40259304209 (? reps, `b659f0eebc58`), B 40281469940 (? reps, `fa6da97bbaa6`), C 40401042132 (? reps, `5e222aa21371`) |
| `results/live/V21_YCSB_SERVICE.md` | omni-v21 | superseded | against its native | L | A 40287958759 (? reps, `b11b4d3825b1`), B 40291376191 (? reps, `f70084ae1bb3`), C 40293208904 (? reps, `2d426169d766`) |
| `results/live/V21_YCSB_SHIPPED.md` | omni-v21 | superseded | against its native | L | A 40238131083 (? reps, `2d40c4c64109`), B 40260620209 (? reps, `b659f0eebc58`), C 40284624594 (? reps, `b11b4d3825b1`) |
| `results/live/V25_ALL_FOUR.md` | omni-v25 | standing | against its native | L | A 41751114338 (10 reps, `63fc4dc666d3`), B 41768859003 (10 reps, `db6e040b4584`), C 41780376170 (10 reps, `0a92e09fe669`) |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_ARMADA_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_ARMADA_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_ARMADA_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_ARMADA_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_BATCH.md` | omni-v25 | standing | against its native | L | A 41753030885 (10 reps, `63fc4dc666d3`), B 41768876462 (10 reps, `db6e040b4584`), C 41781968016 (10 reps, `0a92e09fe669`) |
| `results/live/V25_BINPACK.md` | omni-v25 | standing | against its native | L | A 41802308779 (10 reps, `7d379c6ebae3`), B 41802323140 (10 reps, `7d379c6ebae3`), C 41804425696 (10 reps, `1e2cfe68bf59`) |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_BINPACK_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_BINPACK_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_BINPACK_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_CAPACITY.md` | omni-v25 | standing | against its native | L | in its own Markdown |
| `results/live/V25_CITYLEARN.md` | omni-v25 | standing | against its native | S | in its own Markdown |
| `results/live/V25_COST_TO_MATCH.md` | omni-v25 | standing | against its native | L | A 41798197387 (10 reps, `473c170f787e`), B 41798204788 (10 reps, `473c170f787e`), C 41798211646 (10 reps, `473c170f787e`) |
| `results/live/V25_CRANE_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRANE_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRANE_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRANE_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRANE_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRUISEKUBE.md` | omni-v25 | standing | against its native | L | A 41747200129 (10 reps, `ee22662430a9`), B 41765479982 (10 reps, `479d719fc787`), C 41777088814 (10 reps, `0a92e09fe669`) |
| `results/live/V25_CRUISEKUBE_RECORDER.md` | omni-v25 | standing | against its native | L | A 42173265097 (10 reps, `869cb06c6488`), B 42173285642 (10 reps, `869cb06c6488`), C 42185619972 (10 reps, `869cb06c6488`) |
| `results/live/V25_FAIRNESS.md` | omni-v25 | standing | against its native | L | A 41751121984 (10 reps, `63fc4dc666d3`), B 41768864707 (10 reps, `db6e040b4584`), C 41780381804 (10 reps, `0a92e09fe669`) |
| `results/live/V25_FAULTS.md` | omni-v25 | standing | against its native | L | A 41753024820 (10 reps, `63fc4dc666d3`), B 41768870890 (10 reps, `db6e040b4584`), C 41781962156 (10 reps, `0a92e09fe669`) |
| `results/live/V25_FAULTS_EXTENDED.md` | omni-v25 | standing | against its native | L | A 41792496184 (10 reps, `05092772357b`), B 41794354171 (10 reps, `05092772357b`), C 41796185630 (10 reps, `473c170f787e`) |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GODEL_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GODEL_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GODEL_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GOLDILOCKS.md` | omni-v25 | standing | against its native | L | A 41749168920 (10 reps, `ee22662430a9`), B 41765485855 (10 reps, `479d719fc787`), C 41777095500 (10 reps, `0a92e09fe669`) |
| `results/live/V25_KAFKA.md` | omni-v25 | standing | against its native | L | A 41756685178 (? reps, `198314d551ea`), B 41770452498 (? reps, `db6e040b4584`), C 41783615016 (? reps, `0a92e09fe669`) |
| `results/live/V25_KAFKA_SERVICE.md` | omni-v25 | standing | against its native | L | A 41758475899 (? reps, `e29ad045b2ac`), B 41772114283 (? reps, `db6e040b4584`), C 41785350365 (? reps, `0a92e09fe669`) |
| `results/live/V25_KAI.md` | omni-v25 | standing | against its native | L | A 41800238758 (10 reps, `7d379c6ebae3`), B 41800247331 (10 reps, `7d379c6ebae3`), C 41800254736 (10 reps, `7d379c6ebae3`) |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KAI_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KAI_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KAI_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KARMADA_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KARMADA_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KARMADA_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KEDA_CPU_REQUESTS.md` | omni-v25 | standing | against its native | L | A 41753044221 (10 reps, `63fc4dc666d3`), B 41770442526 (10 reps, `db6e040b4584`), C 41781979744 (10 reps, `0a92e09fe669`) |
| `results/live/V25_KEDA_REQUESTS.md` | omni-v25 | standing | against its native | L | A 41753044221 (10 reps, `63fc4dc666d3`), B 41770442526 (10 reps, `db6e040b4584`), C 41781979744 (10 reps, `0a92e09fe669`) |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | standing | against its native | L | A 41800261877 (10 reps, `7d379c6ebae3`), B 41800269022 (10 reps, `7d379c6ebae3`), C 41802293120 (10 reps, `7d379c6ebae3`) |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | standing | against its native | L | A 42173258848 (10 reps, `869cb06c6488`), B 42173278954 (10 reps, `869cb06c6488`), C 42185612749 (10 reps, `869cb06c6488`) |
| `results/live/V25_KUBERAY_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUBERAY_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUBERAY_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUBERAY_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUBERAY_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUEUE.md` | omni-v25 | standing | against its native | L | A 41762066634 (10 reps, `e391835931e7`), B 41775363004 (10 reps, `db6e040b4584`), C 41788859873 (10 reps, `0a92e09fe669`) |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_KUEUE_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_KUEUE_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_KUEUE_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_MUJOCO.md` | omni-v25 | standing | against its native | S | in its own Markdown |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_OCM_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_OCM_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_OCM_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_PANDAPOWER.md` | omni-v25 | standing | against its native | S | in its own Markdown |
| `results/live/V25_PGBENCH.md` | omni-v25 | standing | against its native | L | A 41756691131 (? reps, `198314d551ea`), B 41770457639 (? reps, `db6e040b4584`), C 41783620506 (? reps, `0a92e09fe669`) |
| `results/live/V25_PGBENCH_SERVICE.md` | omni-v25 | standing | against its native | L | A 41790655143 (? reps, `0a92e09fe669`), B 41792513596 (? reps, `05092772357b`), C 41794373430 (? reps, `05092772357b`) |
| `results/live/V25_REDIS.md` | omni-v25 | standing | against its native | L | A 41756679520 (? reps, `198314d551ea`), B 41770447406 (? reps, `db6e040b4584`), C 41781985238 (? reps, `0a92e09fe669`) |
| `results/live/V25_REDIS_SERVICE.md` | omni-v25 | standing | against its native | L | A 41756709406 (? reps, `198314d551ea`), B 41772107768 (? reps, `db6e040b4584`), C 41783637007 (? reps, `0a92e09fe669`) |
| `results/live/V25_REDIS_SHIPPED.md` | omni-v25 | standing | against its native | L | A 41758488505 (? reps, `e29ad045b2ac`), B 41772126598 (? reps, `db6e040b4584`), C 41785361755 (? reps, `0a92e09fe669`) |
| `results/live/V25_ROBUST_KILL.md` | omni-v25 | standing | against its native | L | A 41760298127 (10 reps, `e391835931e7`), B 41775351685 (10 reps, `db6e040b4584`), C 41788847807 (10 reps, `0a92e09fe669`) |
| `results/live/V25_ROBUST_LONG.md` | omni-v25 | standing | against its native | L | A 41762060399 (3 reps, `e391835931e7`), B 41775357254 (3 reps, `db6e040b4584`), C 41788854067 (3 reps, `0a92e09fe669`) |
| `results/live/V25_SOLO.md` | omni-v25 | standing | in place of a controller | L | A 41751093197 (10 reps, `63fc4dc666d3`), B 41767225693 (10 reps, `479d719fc787`), C 41780359295 (10 reps, `0a92e09fe669`) |
| `results/live/V25_SOLO_2.md` | omni-v25 | standing | in place of a controller | L | A 41832884727 (10 reps, `f79d0dcabf73`), B 41832892271 (10 reps, `f79d0dcabf73`), C 41832900683 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_SOLO_2_VS_ON_NATIVE.md` | omni-v25 | standing | in place of a controller | L | A 41832884727 (10 reps, `f79d0dcabf73`), B 41832892271 (10 reps, `f79d0dcabf73`), C 41832900683 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_SOLO_VS_ON_NATIVE.md` | omni-v25 | standing | in place of a controller | L | A 41751093197 (10 reps, `63fc4dc666d3`), B 41767225693 (10 reps, `479d719fc787`), C 41780359295 (10 reps, `0a92e09fe669`) |
| `results/live/V25_STEADY.md` | omni-v25 | standing | against its native | L | A 41751085804 (10 reps, `63fc4dc666d3`), B 41767220817 (10 reps, `479d719fc787`), C 41778758086 (10 reps, `0a92e09fe669`) |
| `results/live/V25_SWARM.md` | omni-v25 | standing | against its native | S | in its own Markdown |
| `results/live/V25_SYSBENCH.md` | omni-v25 | standing | against its native | L | A 41756697077 (? reps, `198314d551ea`), B 41770463075 (? reps, `db6e040b4584`), C 41783625994 (? reps, `0a92e09fe669`) |
| `results/live/V25_SYSBENCH_SERVICE.md` | omni-v25 | standing | against its native | L | A 41790642021 (? reps, `0a92e09fe669`), B 41792502265 (? reps, `05092772357b`), C 41794360552 (? reps, `05092772357b`) |
| `results/live/V25_SYSBENCH_SHIPPED.md` | omni-v25 | standing | against its native | L | A 41758482144 (? reps, `e29ad045b2ac`), B 41772120161 (? reps, `db6e040b4584`), C 41785356237 (? reps, `0a92e09fe669`) |
| `results/live/V25_TRACE_GOOGLE2011.md` | omni-v25 | standing | against its native | L | A 41753037941 (10 reps, `63fc4dc666d3`), B 41768881626 (10 reps, `db6e040b4584`), C 41781973989 (10 reps, `0a92e09fe669`) |
| `results/live/V25_VANILLA.md` | omni-v25 | standing | against its native | L | A 41802300531 (10 reps, `7d379c6ebae3`), B 41802315329 (10 reps, `7d379c6ebae3`), C 41804417539 (10 reps, `1e2cfe68bf59`) |
| `results/live/V25_VOLCANO.md` | omni-v25 | standing | against its native | L | A 41762072500 (10 reps, `e391835931e7`), B 41775368304 (10 reps, `db6e040b4584`), C 41790635305 (10 reps, `0a92e09fe669`) |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_VOLCANO_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_VOLCANO_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_VOLCANO_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_WANDERING.md` | omni-v25 | standing | against its native | L | A 41751107237 (10 reps, `63fc4dc666d3`), B 41768852229 (10 reps, `db6e040b4584`), C 41780370478 (10 reps, `0a92e09fe669`) |
| `results/live/V25_YCSB.md` | omni-v25 | standing | against its native | L | A 41756703640 (? reps, `198314d551ea`), B 41770468145 (? reps, `db6e040b4584`), C 41783631371 (? reps, `0a92e09fe669`) |
| `results/live/V25_YCSB_SERVICE.md` | omni-v25 | standing | against its native | L | A 41790648692 (? reps, `0a92e09fe669`), B 41792507887 (? reps, `05092772357b`), C 41794367186 (? reps, `05092772357b`) |
| `results/live/V25_YCSB_SHIPPED.md` | omni-v25 | standing | against its native | L | A 41758494688 (? reps, `e29ad045b2ac`), B 41772133244 (? reps, `db6e040b4584`), C 41785367418 (? reps, `0a92e09fe669`) |
| `results/live/V3_ALL_FOUR.md` | omni-v3 | the road | against its native | L | A 38013221512 (10 reps, `3aac0ab7d384`), B 38013226173 (10 reps, `3aac0ab7d384`), C 38013230522 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_BATCH.md` | omni-v3 | the road | against its native | L | A 38013261196 (10 reps, `3aac0ab7d384`), B 38013265986 (10 reps, `3aac0ab7d384`), C 38013269850 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_CITYLEARN.md` | omni-v3 | the road | against its native | S | in its own Markdown |
| `results/live/V3_FAIRNESS.md` | omni-v3 | the road | against its native | L | A 38013235441 (10 reps, `3aac0ab7d384`), B 38013239864 (10 reps, `3aac0ab7d384`), C 38013244591 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_FAULTS.md` | omni-v3 | the road | against its native | L | A 38013248544 (10 reps, `3aac0ab7d384`), B 38013252615 (10 reps, `3aac0ab7d384`), C 38013257029 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_KAFKA.md` | omni-v3 | the road | against its native | L | A 38054742933 (? reps, `ca745467845c`), B 38054746778 (? reps, `ca745467845c`), C 38054750788 (? reps, `ca745467845c`) |
| `results/live/V3_KAFKA_SERVICE.md` | omni-v3 | the road | against its native | L | A 38054804459 (? reps, `ca745467845c`), B 38054808912 (? reps, `ca745467845c`), C 38054812962 (? reps, `ca745467845c`) |
| `results/live/V3_KEDA_CPU_REQUESTS.md` | omni-v3 | the road | against its native | L | A 38096663118 (9 reps, `175cc0feda00`), B 38099655092 (10 reps, `85b150889152`), C 38099656930 (10 reps, `85b150889152`) |
| `results/live/V3_KEDA_REQUESTS.md` | omni-v3 | the road | against its native | L | A 38096663118 (10 reps, `175cc0feda00`), B 38099655092 (10 reps, `85b150889152`), C 38099656930 (10 reps, `85b150889152`) |
| `results/live/V3_MUJOCO.md` | omni-v3 | the road | against its native | S | in its own Markdown |
| `results/live/V3_PANDAPOWER.md` | omni-v3 | the road | against its native | S | in its own Markdown |
| `results/live/V3_PGBENCH.md` | omni-v3 | the road | against its native | L | A 38054754511 (? reps, `ca745467845c`), B 38054758150 (? reps, `ca745467845c`), C 38054761503 (? reps, `ca745467845c`) |
| `results/live/V3_REDIS.md` | omni-v3 | the road | against its native | L | A 38054731163 (? reps, `ca745467845c`), B 38054735302 (? reps, `ca745467845c`), C 38054739168 (? reps, `ca745467845c`) |
| `results/live/V3_REDIS_SERVICE.md` | omni-v3 | the road | against its native | L | A 38054791688 (? reps, `ca745467845c`), B 38054795871 (? reps, `ca745467845c`), C 38054800068 (? reps, `ca745467845c`) |
| `results/live/V3_ROBUST_KILL.md` | omni-v3 | the road | against its native | L | A 38013447217 (10 reps, `3aac0ab7d384`), B 38013451990 (10 reps, `3aac0ab7d384`), C 38013456955 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_ROBUST_LONG.md` | omni-v3 | the road | against its native | L | A 38013462081 (3 reps, `3aac0ab7d384`), B 38013467123 (3 reps, `3aac0ab7d384`), C 38013471943 (3 reps, `3aac0ab7d384`) |
| `results/live/V3_STEADY.md` | omni-v3 | the road | against its native | L | A 38013195851 (10 reps, `3aac0ab7d384`), B 38013200499 (10 reps, `3aac0ab7d384`), C 38013204648 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_SWARM.md` | omni-v3 | the road | against its native | S | in its own Markdown |
| `results/live/V3_SYSBENCH.md` | omni-v3 | the road | against its native | L | A 38054765202 (? reps, `ca745467845c`), B 38054768832 (? reps, `ca745467845c`), C 38054773573 (? reps, `ca745467845c`) |
| `results/live/V3_TRACE_GOOGLE2011.md` | omni-v3 | the road | against its native | L | A 38013274685 (10 reps, `3aac0ab7d384`), B 38013279107 (10 reps, `3aac0ab7d384`), C 38013283518 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_WANDERING.md` | omni-v3 | the road | against its native | L | A 38013208955 (10 reps, `3aac0ab7d384`), B 38013212780 (10 reps, `3aac0ab7d384`), C 38013217100 (10 reps, `3aac0ab7d384`) |
| `results/live/V3_YCSB.md` | omni-v3 | the road | against its native | L | A 38054777807 (? reps, `ca745467845c`), B 38054782696 (? reps, `ca745467845c`), C 38054787517 (? reps, `ca745467845c`) |
| `results/live/V5_CAPACITY.md` | omni-v5 | the road | against its native | L | in its own Markdown |
| `results/live/V5_GOLDILOCKS.md` | omni-v5 | the road | against its native | L | A 38339821941 (10 reps, `148565d2550d`), B 38339828150 (10 reps, `148565d2550d`), C 38339834658 (10 reps, `148565d2550d`) |
| `results/live/V6_CRUISEKUBE.md` | omni-v6 | the road | against its native | L | A 38695794476 (10 reps, `9a499b137e78`), B 38708509996 (10 reps, `afbac134f8a1`), C 38721988615 (10 reps, `63f29c3e20a5`) |
| `results/live/V6_GOLDILOCKS.md` | omni-v6 | the road | against its native | L | A 38697567716 (10 reps, `9a499b137e78`), B 38708517967 (10 reps, `afbac134f8a1`), C 38721995611 (10 reps, `63f29c3e20a5`) |
| `results/live/V6_KEDA_CPU_REQUESTS.md` | omni-v6 | the road | against its native | L | A 38701101796 (10 reps, `9a499b137e78`), B 38712444594 (10 reps, `afbac134f8a1`), C 38725705826 (10 reps, `63f29c3e20a5`) |
| `results/live/V6_KEDA_REQUESTS.md` | omni-v6 | the road | against its native | L | A 38701101796 (10 reps, `9a499b137e78`), B 38712444594 (10 reps, `afbac134f8a1`), C 38725705826 (10 reps, `63f29c3e20a5`) |
| `results/live/V7_ALL_FOUR.md` | omni-v7 | the road | against its native | L | A 38931373773 (10 reps, `ccce256f4079`), B 38943562450 (10 reps, `cf8dccec0604`), C 38953643978 (10 reps, `cf8dccec0604`) |
| `results/live/V7_BATCH.md` | omni-v7 | the road | against its native | L | A 38933427756 (10 reps, `1ccba53a74fe`), B 38943582904 (10 reps, `cf8dccec0604`), C 38955582904 (10 reps, `cf8dccec0604`) |
| `results/live/V7_CAPACITY.md` | omni-v7 | the road | against its native | L | in its own Markdown |
| `results/live/V7_CITYLEARN.md` | omni-v7 | the road | against its native | S | in its own Markdown |
| `results/live/V7_CRUISEKUBE.md` | omni-v7 | the road | against its native | L | A 38843284578 (10 reps, `b1eb8294f4a7`), B 38843287341 (10 reps, `b1eb8294f4a7`), C 38843289946 (10 reps, `b1eb8294f4a7`) |
| `results/live/V7_FAIRNESS.md` | omni-v7 | the road | against its native | L | A 38933412682 (10 reps, `1ccba53a74fe`), B 38943569010 (10 reps, `cf8dccec0604`), C 38955570717 (10 reps, `cf8dccec0604`) |
| `results/live/V7_FAULTS.md` | omni-v7 | the road | against its native | L | A 38933419908 (10 reps, `1ccba53a74fe`), B 38943575598 (10 reps, `cf8dccec0604`), C 38955576606 (10 reps, `cf8dccec0604`) |
| `results/live/V7_GOLDILOCKS.md` | omni-v7 | the road | against its native | L | A 38843260818 (10 reps, `b1eb8294f4a7`), B 38843263401 (10 reps, `b1eb8294f4a7`), C 38843266098 (10 reps, `b1eb8294f4a7`) |
| `results/live/V7_KAFKA.md` | omni-v7 | the road | against its native | L | A 38933446756 (? reps, `1ccba53a74fe`), B 38945593946 (? reps, `cf8dccec0604`), C 38955602669 (? reps, `cf8dccec0604`) |
| `results/live/V7_KAFKA_SERVICE.md` | omni-v7 | the road | against its native | L | A 38935449417 (? reps, `1ccba53a74fe`), B 38947629506 (? reps, `cf8dccec0604`), C 38957543812 (? reps, `cf8dccec0604`) |
| `results/live/V7_KEDA_CPU_REQUESTS.md` | omni-v7 | the road | against its native | L | A 38843268161 (10 reps, `b1eb8294f4a7`), B 38843270386 (10 reps, `b1eb8294f4a7`), C 38843272786 (10 reps, `b1eb8294f4a7`) |
| `results/live/V7_KEDA_REQUESTS.md` | omni-v7 | the road | against its native | L | A 38843268161 (10 reps, `b1eb8294f4a7`), B 38843270386 (10 reps, `b1eb8294f4a7`), C 38843272786 (10 reps, `b1eb8294f4a7`) |
| `results/live/V7_MUJOCO.md` | omni-v7 | the road | against its native | S | in its own Markdown |
| `results/live/V7_PANDAPOWER.md` | omni-v7 | the road | against its native | S | in its own Markdown |
| `results/live/V7_PGBENCH.md` | omni-v7 | the road | against its native | L | A 38935420705 (? reps, `1ccba53a74fe`), B 38945602041 (? reps, `cf8dccec0604`), C 38957516288 (? reps, `cf8dccec0604`) |
| `results/live/V7_REDIS.md` | omni-v7 | the road | against its native | L | A 38933440763 (? reps, `1ccba53a74fe`), B 38945586160 (? reps, `cf8dccec0604`), C 38955596458 (? reps, `cf8dccec0604`) |
| `results/live/V7_REDIS_SERVICE.md` | omni-v7 | the road | against its native | L | A 38935442398 (? reps, `1ccba53a74fe`), B 38947622681 (? reps, `cf8dccec0604`), C 38957537624 (? reps, `cf8dccec0604`) |
| `results/live/V7_ROBUST_LONG.md` | omni-v7 | the road | against its native | L | A 38937561382 (3 reps, `1ccba53a74fe`), B 38949637918 (3 reps, `cf8dccec0604`), C 38961359324 (3 reps, `cf8dccec0604`) |
| `results/live/V7_SWARM.md` | omni-v7 | the road | against its native | S | in its own Markdown |
| `results/live/V7_SYSBENCH.md` | omni-v7 | the road | against its native | L | A 38935427838 (? reps, `1ccba53a74fe`), B 38945609870 (? reps, `cf8dccec0604`), C 38957523334 (? reps, `cf8dccec0604`) |
| `results/live/V7_TRACE_GOOGLE2011.md` | omni-v7 | the road | against its native | L | A 38933435153 (10 reps, `1ccba53a74fe`), B 38945578014 (10 reps, `cf8dccec0604`), C 38955589372 (10 reps, `cf8dccec0604`) |
| `results/live/V7_YCSB.md` | omni-v7 | the road | against its native | L | A 38935435045 (? reps, `1ccba53a74fe`), B 38947615453 (? reps, `cf8dccec0604`), C 38957530830 (? reps, `cf8dccec0604`) |
| `results/orchestrator/V18_THREE_ARMS_ABC.md` | omni-v18 | taken out | against its native | L | in its own Markdown |
| `results/orchestrator/V21_THREE_ARMS_ABC.md` | omni-v21 | taken out | against its native | L | in its own Markdown |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
