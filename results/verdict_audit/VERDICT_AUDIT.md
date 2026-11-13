# The verdict audit: every row recomputed from its stored values, every count from one selection

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

Written by `tools/verdict_audit.py` from the three-run tables as they stand (digest `287061c8bc13fc03`). The engine that stands is omni-v26. The rule: tools/readings.py three_run_reading: a change of 0.5% or more, the mean of the three runs' changes in percent of native, reads by the gauge's aim; under it STEADY, under the floor; every run's two values equal to 1e-09 of the value, STEADY, the same; runs that moved 0.5% or more in opposite directions, the runs disagree. Evidence strength is shown beside the word and never changes it: strong, every run the mean's way and beyond its noise (its 95% interval clear of zero); moderate, all but one; weak, one run beyond its noise; inconclusive, no run beyond its noise (a mean of 0.5% or more, not a change any one run could tell from its noise). STEADY is of three kinds: exactly the same (every run's values equal to nine decimal places), under the floor (a measured change, the three runs' mean under 0.5%) and no difference beyond the noise (a table read by an older key). The runs disagree is unresolved, never a final word: opposite directions each beyond its noise, or opposite directions inside overlapping noise.

## The counts

| What | Count |
|---|---|
| Three-run tables | 422: 101 standing, 259 superseded, 60 the road, 2 taken out |
| Standing tables, Omni-Compass against its native | 64 |
| Standing tables on the engine that stands (omni-v26) | 81 |
| Standing tables not yet run again on omni-v26 | 20 |
| Rows recomputed from their stored values | 12842 of 17779 |
| Stored readings the key reads otherwise | 0 |
| Markdown readings unlike their JSON twin | 0 |

### Standing tables: Omni-Compass against its native (the readings do no harm is judged by)

Every word: 484 GAIN, 197 power given, 567 STEADY, 288 LOSS, 206 the runs disagree, 32 the runs differ, 661 shown, 201 tuning. The four categories are exclusive: each row has one word.

| Engine | Words |
|---|---|
| omni-v26 | 444 GAIN, 185 power given, 527 STEADY, 227 LOSS, 184 the runs disagree, 32 the runs differ, 589 shown, 201 tuning |
| omni-v25 | 27 GAIN, 12 power given, 30 STEADY, 55 LOSS, 7 the runs disagree, 54 shown |
| omni-v12 | 13 GAIN, 10 STEADY, 6 LOSS, 15 the runs disagree, 18 shown |

| Evidence class | Words |
|---|---|
| L (the real software) | 387 GAIN, 187 power given, 407 STEADY, 288 LOSS, 206 the runs disagree, 605 shown, 189 tuning |
| S (an outside simulator driven by our own runner) | 97 GAIN, 10 power given, 160 STEADY, 32 the runs differ, 56 shown, 12 tuning |

Useful work, time waited and resources apart (item 8 of the work order): a resource spent or held that rose is power given, shown beside what it bought, never a gain in work.

| The gauge's direction | Words |
|---|---|
| a count that must never rise | 6 GAIN, 82 STEADY, 14 tuning |
| resource spent or held | 271 GAIN, 197 power given, 217 STEADY, 62 the runs disagree, 6 the runs differ, 63 tuning |
| shown | 6 STEADY, 20 the runs differ, 661 shown, 56 tuning |
| time waited, missed or failed | 178 GAIN, 182 STEADY, 285 LOSS, 133 the runs disagree, 3 the runs differ, 39 tuning |
| work done | 29 GAIN, 80 STEADY, 3 LOSS, 11 the runs disagree, 3 the runs differ, 29 tuning |

Evidence strength beside the word (it never changes the word):

| Word | Strength |
|---|---|
| GAIN | 210 strong, 94 deterministic, reproduced in all three runs, 92 inconclusive, 43 moderate, 42 weak, 3 not recomputable from runs |
| LOSS | 115 inconclusive, 65 strong, 55 moderate, 53 weak |
| power given | 94 strong, 39 inconclusive, 30 moderate, 24 weak, 10 deterministic, reproduced in all three runs |

| STEADY of each kind | 215 under the floor, 352 exactly the same |
|---|---|
| The runs disagree, by cause | 204 opposite directions inside overlapping noise, 2 opposite directions, each beyond its noise |

### Every comparison and status

| Status, comparison | Words |
|---|---|
| standing | against its native | 484 GAIN, 197 power given, 567 STEADY, 288 LOSS, 206 the runs disagree, 32 the runs differ, 661 shown, 201 tuning |
| standing | in place of a controller | 110 GAIN, 29 power given, 72 STEADY, 70 LOSS, 18 the runs disagree, 137 shown |
| standing | the orchestrator's own | 28 GAIN, 10 power given, 86 STEADY, 76 LOSS, 35 the runs disagree, 99 shown |
| standing | two changes at once | 57 GAIN, 25 power given, 43 STEADY, 96 LOSS, 14 the runs disagree, 99 shown |
| superseded | against its native | 1713 GAIN, 622 power given, 2568 STEADY, 572 LOSS, 1258 the runs disagree, 80 the runs differ, 1861 shown, 1221 tuning |
| superseded | in place of a controller | 172 GAIN, 31 power given, 94 STEADY, 75 LOSS, 31 the runs disagree, 182 shown |
| superseded | the orchestrator's own | 37 GAIN, 20 power given, 126 STEADY, 111 LOSS, 45 the runs disagree, 144 shown |
| superseded | two changes at once | 78 GAIN, 39 power given, 68 STEADY, 133 LOSS, 21 the runs disagree, 144 shown |
| taken out | against its native | 15 GAIN, 5 power given, 1 LOSS, 3 the runs disagree |
| the road | against its native | 590 GAIN, 114 power given, 949 STEADY, 55 LOSS, 133 the runs disagree, 17 the runs differ, 519 shown, 192 tuning |

The orchestrator's own rows (ORCH) carry no Omni-Compass in either arm; two changes at once (BOTH) and in place of a controller (VS) are shown, never a reading of Omni-Compass against its native.

## Every LOSS row of Omni-Compass against its native (288)

| Table | Engine | Class | Gauge | Native → Omni-Compass, raw change, each run | Evidence |
|---|---|---|---|---|---|
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | L | response time (ms), 95th percentile | 536.2 → 567.1 (+5.8%); 1283 → 1372 (+6.9%); 863.2 → 913.5 (+5.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | L | response time (ms), 99th percentile | 767.9 → 818.7 (+6.6%); 1874 → 2010 (+7.3%); 1252 → 1296 (+3.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_BARE.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 38.07 → 40.1 (+5.3%); 85.79 → 89.12 (+3.9%); 55.45 → 59.44 (+7.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.0; 0.1 → 0.2 (+100.0%); 0.1 → 0.1 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | L | batch: queue finished (s) | 1290 → 1313 (+1.8%); 1421 → 1421 (−0.0%); 1396 → 1421 (+1.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V12_KOORDINATOR_4W_TOP.md` | omni-v12 | L | queue: job turnaround, submitted to done, mean (s) | 614 → 650.2 (+5.9%); 799.3 → 814.5 (+1.9%); 763.3 → 789 (+3.4%) | inconclusive; 0 of 3 beyond the noise |
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
| `results/live/V26_AKS_FULL_BURST.md` | omni-v26 | L | response time (ms), mean | 565.2 → 663.5 (+17.4%); 464.7 → 619.3 (+33.3%); 501.2 → 752.9 (+50.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_AKS_FULL_BURST.md` | omni-v26 | L | response time (ms), 95th percentile | 1257 → 2354 (+87.3%); 1074 → 1480 (+37.9%); 1542 → 3729 (+141.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_AKS_FULL_BURST.md` | omni-v26 | L | response time (ms), 99th percentile | 4764 → 6624 (+39.0%); 2533 → 5842 (+130.6%); 4233 → 8091 (+91.1%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_AKS_FULL_BURST.md` | omni-v26 | L | pods with no machine to take them (unschedulable) | 2.333 → 20.67 (+785.7%); 2.333 → 21.67 (+828.6%); 2.667 → 22.33 (+737.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_AKS_FULL_BURST.md` | omni-v26 | L | time pods had no machine to take them, pod-minutes | 2.133 → 40.31 (+1789.3%); 2.933 → 39.82 (+1257.4%); 2.794 → 44.82 (+1504.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_AKS_FULL_BURST.md` | omni-v26 | L | pod start wait, total (s) | 58.33 → 2501 (+4186.9%); 38 → 2555 (+6623.7%); 87 → 2667 (+2965.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_AKS_FULL_BURST.md` | omni-v26 | L | pod start wait, mean (s) | 19.27 → 103.5 (+437.0%); 7.6 → 95.33 (+1154.4%); 29.67 → 109.3 (+268.5%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_ALL_FOUR.md` | omni-v26 | L | pod start wait, total (s) | 7.6 → 17.8 (+134.2%); 7.8 → 20.8 (+166.7%); 7.3 → 15.1 (+106.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_ALL_FOUR.md` | omni-v26 | L | pod start wait, mean (s) | 1.406 → 1.76 (+25.2%); 1.399 → 1.888 (+35.0%); 1.325 → 1.528 (+15.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_BATCH.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 → 11 (+2.8%); 9.7 → 9.8 (+1.0%); 11.2 → 11.6 (+3.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_BATCH.md` | omni-v26 | L | pod start wait, total (s) | 0.0; 0.7 → 1.6 (+128.6%); 0.1 → 1.8 (+1700.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BATCH.md` | omni-v26 | L | pod start wait, mean (s) | 0.0; 0.7 → 0.8 (+14.3%); 0.1 → 0.9 (+800.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BATCH.md` | omni-v26 | L | batch: queue finished (s) | 633.6 → 649.1 (+2.4%); 561.1 → 578.5 (+3.1%); 662.2 → 682.9 (+3.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_BINPACK.md` | omni-v26 | L | response time (ms), 95th percentile | 1579 → 1717 (+8.8%); 2154 → 2350 (+9.1%); 1149 → 1276 (+11.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_BINPACK.md` | omni-v26 | L | response time (ms), 99th percentile | 2235 → 2419 (+8.2%); 3139 → 3222 (+2.7%); 1678 → 1844 (+9.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 → 8 (+5.3%); 11.9 → 12.3 (+3.4%); 7.3 → 7.7 (+5.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK.md` | omni-v26 | L | pod start wait, total (s) | 0.4 → 1 (+150.0%); 0.2 → 3 (+1400.0%); 0.1 → 2.6 (+2500.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_BINPACK.md` | omni-v26 | L | pod start wait, mean (s) | 0.4 → 0.5 (+25.0%); 0.2 → 1.417 (+608.3%); 0.1 → 1.583 (+1483.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_BINPACK.md` | omni-v26 | L | batch: queue finished (s) | 807.3 → 818.7 (+1.4%); 841.9 → 853.1 (+1.3%); 776.6 → 786.3 (+1.2%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_BINPACK.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.2333 → 0.3875 (+66.1%); 0.1 → 0.2333 (+133.3%); 0.06667 → 0.1625 (+143.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 → 2.7 (+68.8%); 0.6 → 1.1 (+83.3%); 0.5 → 0.6 (+20.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 115.5 → 125.6 (+8.7%); 149.3 → 162.3 (+8.7%); 84.68 → 94.56 (+11.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | response time (ms), 95th percentile | 980.5 → 1099 (+12.0%); 980.5 → 1062 (+8.3%); 754.8 → 848.8 (+12.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | response time (ms), 99th percentile | 1381 → 1619 (+17.2%); 1349 → 1462 (+8.4%); 1077 → 1248 (+15.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | time over the response line (% of samples) | 10.5 → 10.62 (+1.1%); 11.16 → 11.63 (+4.2%); 7.223 → 7.232 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 → 6.1 (+5.2%); 7.9 → 8.4 (+6.3%); 4 → 4.6 (+15.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | pod start wait, total (s) | 0.5 → 3.3 (+560.0%); 3.3; 0.2 → 1.5 (+650.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | pod start wait, mean (s) | 0.25 → 1.45 (+480.0%); 1.5; 0.2 → 0.625 (+212.5%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | batch: queue finished (s) | 771.2 → 776.8 (+0.7%); 765.4 → 771.8 (+0.8%); 755.1 → 757.6 (+0.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.03333 → 0.05 (+50.0%); 0.04167 → 0.075 (+80.0%); 0.03333 → 0.03333 (+0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 → 0.3 (+50.0%); 0.3 → 0.6 (+100.0%); 0.1 → 0.3 (+200.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 75.52 → 81.56 (+8.0%); 73.41 → 79.65 (+8.5%); 59.86 → 62.91 (+5.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_TOP.md` | omni-v26 | L | response time (ms), 95th percentile | 1077 → 1122 (+4.2%); 958.9 → 1164 (+21.4%); 797.5 → 802.2 (+0.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_TOP.md` | omni-v26 | L | response time (ms), 99th percentile | 1528 → 1552 (+1.6%); 1515 → 1637 (+8.1%); 1120 → 1151 (+2.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_TOP.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 → 4.7 (+2.2%); 6 → 6.4 (+6.7%); 3.2 → 3.3 (+3.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_TOP.md` | omni-v26 | L | pod start wait, total (s) | 0.5 → 0.7 (+40.0%); 0.9 → 1.5 (+66.7%); 1.1 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_TOP.md` | omni-v26 | L | batch: queue finished (s) | 773 → 777.4 (+0.6%); 770.5 → 781.8 (+1.5%); 755.8 → 758.5 (+0.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_TOP.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 → 0.5 (+150.0%); 0.3 → 0.7 (+133.3%); 0.1 → 0.1 (±0.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_BINPACK_4W_TOP.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 79.44 → 83.83 (+5.5%); 75.99 → 87.45 (+15.1%); 62.11 → 65.18 (+5.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_CAPACITY.md` | omni-v26 | L | 1500:work | 4019 → 4002 (−0.4%); 9244 → 9200 (−0.5%); 8087 → 8021 (−0.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_CAPACITY.md` | omni-v26 | L | 1500:capacity | 6.8 → 6 (−11.8%); 12.4 → 12 (−3.2%); 11.2 → 10.8 (−3.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_CAPACITY.md` | omni-v26 | L | 2000:work | 1.03e+04 → 1.007e+04 (−2.3%); 9325 → 9061 (−2.8%); 9960 → 9704 (−2.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_CRANE_4W_BARE.md` | omni-v26 | L | pod start wait, total (s) | 8 → 10.7 (+33.8%); 7.5 → 9.3 (+24.0%); 7.4 → 11.2 (+51.4%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_CRANE_4W_TOP.md` | omni-v26 | L | response time (ms), mean | 137.6 → 138 (+0.3%); 137.8 → 140.5 (+1.9%); 151.3 → 151.5 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_CRANE_4W_TOP.md` | omni-v26 | L | pod start wait, total (s) | 7.9 → 12.6 (+59.5%); 7.5 → 12.2 (+62.7%); 7 → 12.6 (+80.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_CRUISEKUBE.md` | omni-v26 | L | response time (ms), mean | 79.44 → 80.85 (+1.8%); 75.67 → 76.07 (+0.5%); 74.11 → 75.15 (+1.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_CRUISEKUBE.md` | omni-v26 | L | response time (ms), 95th percentile | 117.8 → 119.8 (+1.7%); 114.1 → 117.6 (+3.1%); 105.4 → 106.1 (+0.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_CRUISEKUBE.md` | omni-v26 | L | response time (ms), 99th percentile | 131.2 → 141.1 (+7.6%); 128.8 → 140.2 (+8.9%); 116.3 → 123.1 (+5.8%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_CRUISEKUBE.md` | omni-v26 | L | failed requests (%) | 0.0; 0.012269938650306749; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_CRUISEKUBE.md` | omni-v26 | L | pod start wait, total (s) | 1.7 → 1.9 (+11.8%); 2.1 → 2.4 (+14.3%); 2.1 → 2.1 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_CRUISEKUBE_RECORDER.md` | omni-v26 | L | response time (ms), mean | 69.17 → 71.38 (+3.2%); 79.83 → 81.08 (+1.6%); 73.59 → 74.97 (+1.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_CRUISEKUBE_RECORDER.md` | omni-v26 | L | response time (ms), 95th percentile | 103.7 → 107 (+3.2%); 119.9 → 119.6 (−0.3%); 114 → 115.9 (+1.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_CRUISEKUBE_RECORDER.md` | omni-v26 | L | response time (ms), 99th percentile | 115.1 → 124.9 (+8.6%); 136.8 → 137.4 (+0.5%); 127 → 137.6 (+8.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_CRUISEKUBE_RECORDER.md` | omni-v26 | L | pod start wait, total (s) | 2.1 → 2.5 (+19.0%); 1.5 → 2.1 (+40.0%); 1.5 → 2.2 (+46.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_FAIRNESS.md` | omni-v26 | L | response time (ms), 95th percentile | 2072 → 2246 (+8.4%); 1918 → 2132 (+11.2%); 1822 → 1908 (+4.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_FAIRNESS.md` | omni-v26 | L | pod start wait, total (s) | 8.4 → 10.3 (+22.6%); 8.8 → 10.5 (+19.3%); 9.3 → 10.2 (+9.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_FAIRNESS.md` | omni-v26 | L | second app: response time (ms), 95th percentile | 239.9 → 240.7 (+0.4%); 272.6 → 296.7 (+8.8%); 372.8 → 417 (+11.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_FAIRNESS.md` | omni-v26 | L | second app: failed requests (%) | 12.08 → 12.48 (+3.3%); 10.23 → 10.43 (+2.0%); 10.22 → 10.46 (+2.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_FAULTS.md` | omni-v26 | L | pod start wait, total (s) | 8.6 → 16.3 (+89.5%); 9 → 17.3 (+92.2%); 17.5 → 29.2 (+66.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_FAULTS_EXTENDED.md` | omni-v26 | L | pod start wait, total (s) | 15.8 → 19.2 (+21.5%); 13.1 → 18.3 (+39.7%); 13.4 → 20 (+49.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_FAULTS_EXTENDED.md` | omni-v26 | L | pod start wait, mean (s) | 1.626 → 1.626 (−0.0%); 1.536 → 1.716 (+11.7%); 1.538 → 1.641 (+6.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | response time (ms), mean | 505.6 → 526.9 (+4.2%); 399 → 417.1 (+4.5%); 270.8 → 293.8 (+8.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | response time (ms), 95th percentile | 1996 → 2065 (+3.5%); 1491 → 1582 (+6.2%); 916.5 → 1025 (+11.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | response time (ms), 99th percentile | 2833 → 2957 (+4.3%); 2119 → 2270 (+7.1%); 1355 → 1445 (+6.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | time over the response line (% of samples) | 21.67 → 22.58 (+4.2%); 15.67 → 15.85 (+1.1%); 8.888 → 10.44 (+17.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 → 12.3 (+5.1%); 10.8 → 11 (+1.9%); 7.8 → 8.6 (+10.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | pod start wait, total (s) | 2.3; 2.0; 0.2 → 3.1 (+1450.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | pod start wait, mean (s) | 1.5333333333333334; 0.5866666666666667; 0.2 → 1.317 (+558.3%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | batch: queue finished (s) | 847.5 → 852.8 (+0.6%); 806.7 → 813.3 (+0.8%); 767.5 → 775.9 (+1.1%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 → 3.3 (+135.7%); 0.9 → 1.2 (+33.3%); 0.4 → 1.2 (+200.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 151.9 → 158.3 (+4.2%); 112 → 118.7 (+5.9%); 71.98 → 78.88 (+9.6%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_TOP.md` | omni-v26 | L | response time (ms), mean | 509.8 → 530.7 (+4.1%); 399.3 → 430 (+7.7%); 280.2 → 297.6 (+6.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_TOP.md` | omni-v26 | L | response time (ms), 95th percentile | 2130 → 2224 (+4.4%); 1526 → 1671 (+9.5%); 1021 → 1100 (+7.8%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_TOP.md` | omni-v26 | L | time over the response line (% of samples) | 20.46 → 21.43 (+4.7%); 14.86 → 15.77 (+6.1%); 8.498 → 10.08 (+18.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_TOP.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 → 11.8 (+3.5%); 10.3 → 11 (+6.8%); 7.5 → 8.4 (+12.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_TOP.md` | omni-v26 | L | pod start wait, total (s) | 1.1; 0.3 → 0.4 (+33.3%); 0.2 → 0.8 (+300.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_TOP.md` | omni-v26 | L | pod start wait, mean (s) | 0.6; 0.3 → 0.4 (+33.3%); 0.1 → 0.65 (+550.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_TOP.md` | omni-v26 | L | batch: queue finished (s) | 854.7 → 861.3 (+0.8%); 813.6 → 820.6 (+0.9%); 770.6 → 777 (+0.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_GODEL_4W_TOP.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 161.7 → 168.5 (+4.2%); 120.4 → 126.3 (+4.9%); 77.81 → 82.86 (+6.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_GOLDILOCKS.md` | omni-v26 | L | pod start wait, total (s) | 4.7 → 11.7 (+148.9%); 5.1 → 10 (+96.1%); 5.2 → 10.4 (+100.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_GOLDILOCKS.md` | omni-v26 | L | pod start wait, mean (s) | 1.433 → 1.744 (+21.7%); 1.542 → 1.738 (+12.8%); 1.425 → 1.596 (+12.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KAI.md` | omni-v26 | L | response time (ms), 95th percentile | 1593 → 1762 (+10.6%); 950.7 → 1038 (+9.2%); 1225 → 1266 (+3.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KAI.md` | omni-v26 | L | response time (ms), 99th percentile | 2279 → 2383 (+4.6%); 1384 → 1519 (+9.7%); 1715 → 1860 (+8.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KAI.md` | omni-v26 | L | failed requests (%) | 0.0; 0.0; 0.011560693641618497 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KAI.md` | omni-v26 | L | pod start wait, total (s) | 0.4 → 1.5 (+275.0%); 1.3; 0.0 | weak; 1 of 3 beyond the noise |
| `results/live/V26_KAI.md` | omni-v26 | L | pod start wait, mean (s) | 0.4 → 0.7667 (+91.7%); 1.0333333333333332; 0.0 | weak; 1 of 3 beyond the noise |
| `results/live/V26_KAI.md` | omni-v26 | L | batch: queue finished (s) | 825.8 → 838.7 (+1.6%); 773.7 → 784.3 (+1.4%); 791.7 → 795.4 (+0.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KAI.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 126.5 → 138.3 (+9.3%); 79.49 → 88.21 (+11.0%); 96.72 → 101.6 (+5.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KAI_4W_BARE.md` | omni-v26 | L | response time (ms), 95th percentile | 797.8 → 885.7 (+11.0%); 1415 → 1574 (+11.3%); 877.8 → 952.3 (+8.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_KAI_4W_BARE.md` | omni-v26 | L | response time (ms), 99th percentile | 1108 → 1244 (+12.3%); 2003 → 2223 (+10.9%); 1207 → 1326 (+9.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KAI_4W_BARE.md` | omni-v26 | L | time over the response line (% of samples) | 8.227 → 9.6 (+16.7%); 17.22 → 17.35 (+0.7%); 8.548 → 9.797 (+14.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KAI_4W_BARE.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 → 7 (+34.6%); 9.2 → 9.6 (+4.3%); 5.6 → 7.1 (+26.8%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KAI_4W_BARE.md` | omni-v26 | L | pod start wait, total (s) | 0.3 → 4 (+1233.3%); 3.8; 0.2 → 2.8 (+1300.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KAI_4W_BARE.md` | omni-v26 | L | pod start wait, mean (s) | 0.3 → 1.883 (+527.8%); 1.2583333333333333; 0.2 → 1.183 (+491.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KAI_4W_BARE.md` | omni-v26 | L | batch: queue finished (s) | 755.4 → 759.6 (+0.6%); 798.1 → 807.9 (+1.2%); 759.7 → 762 (+0.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KAI_4W_BARE.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 61.04 → 66.06 (+8.2%); 105.2 → 112.3 (+6.8%); 65.84 → 68.63 (+4.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | L | response time (ms), 95th percentile | 967.1 → 1100 (+13.7%); 1858 → 1973 (+6.2%); 1050 → 1220 (+16.1%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | L | response time (ms), 99th percentile | 1390 → 1545 (+11.2%); 2579 → 2759 (+7.0%); 1521 → 1748 (+14.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | L | time over the response line (% of samples) | 7.746 → 8.843 (+14.2%); 14.35 → 15.22 (+6.1%); 8.52 → 9.671 (+13.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 → 6.3 (+28.6%); 9 → 10.9 (+21.1%); 7.1 → 8.3 (+16.9%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | L | pod start wait, total (s) | 0.5 → 1.6 (+220.0%); 0.3 → 1.7 (+466.7%); 0.2 → 1.1 (+450.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | L | pod start wait, mean (s) | 0.5 → 0.6 (+20.0%); 0.3 → 0.65 (+116.7%); 0.2 → 0.9 (+350.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | L | batch: queue finished (s) | 776.8 → 784.7 (+1.0%); 836 → 854.1 (+2.2%); 777.8 → 793.6 (+2.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.8667 → 0.9333 (+7.7%); 0.9833 → 1.15 (+16.9%); 0.8333 → 0.8667 (+4.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 82.29 → 87.46 (+6.3%); 137.4 → 155.5 (+13.2%); 84.99 → 96.85 (+14.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_KEDA_CPU_REQUESTS.md` | omni-v26 | L | pod start wait, total (s) | 6.5 → 13.8 (+112.3%); 8.3 → 11.3 (+36.1%); 6.1 → 11.8 (+93.4%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR.md` | omni-v26 | L | response time (ms), 95th percentile | 220.9 → 235.4 (+6.6%); 189 → 191.6 (+1.4%); 260.9 → 275.6 (+5.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR.md` | omni-v26 | L | response time (ms), 99th percentile | 322.7 → 353.7 (+9.6%); 275.7 → 294.9 (+6.9%); 380.8 → 408.4 (+7.3%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR.md` | omni-v26 | L | batch: queue finished (s) | 1408 → 1449 (+2.9%); 1360 → 1420 (+4.4%); 1507 → 1508 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 101 → 172.8 (+71.1%); 112.4 → 135.3 (+20.4%); 157.6 → 218.1 (+38.4%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 504.5 → 763.5 (+51.3%); 557.2 → 638.2 (+14.5%); 696 → 869.6 (+24.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | L | response time (ms), 95th percentile | 224.5 → 236.7 (+5.4%); 260 → 270.6 (+4.1%); 244.1 → 261.2 (+7.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | L | response time (ms), 99th percentile | 340.3 → 366.9 (+7.8%); 374.7 → 392.3 (+4.7%); 343.5 → 398 (+15.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | L | time over the response line (% of samples) | 0.1615 → 0.3919 (+142.7%); 0.2765 → 0.2849 (+3.1%); 0.1694 → 0.545 (+221.7%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | L | pod start wait, total (s) | 3.2; 0.2 → 2 (+900.0%); 2.9 | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | L | pod start wait, mean (s) | 1.0916666666666666; 0.2 → 0.775 (+287.5%); 0.95 | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | L | batch: queue finished (s) | 1433 → 1457 (+1.7%); 1508 → 1512 (+0.2%); 1447 → 1448 (+0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 162.1 → 185.1 (+14.2%); 162.6 → 205.5 (+26.4%); 146.5 → 191.8 (+30.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 690.1 → 782.5 (+13.4%); 720.8 → 856.4 (+18.8%); 677.4 → 791.7 (+16.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 832.5 → 847.6 (+1.8%); 920.4 → 958.9 (+4.2%); 876.9 → 902.3 (+2.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | L | response time (ms), 95th percentile | 1066 → 1194 (+12.0%); 1233 → 1333 (+8.1%); 1504 → 1690 (+12.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | L | response time (ms), 99th percentile | 1445 → 1614 (+11.6%); 1688 → 1937 (+14.7%); 2082 → 2298 (+10.4%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 → 7.2 (+5.9%); 6.6 → 7.3 (+10.6%); 8.2 → 8.4 (+2.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | L | pod start wait, total (s) | 0.2 → 2.2 (+1000.0%); 0.1 → 0.8 (+700.0%); 0.2 → 4 (+1900.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | L | pod start wait, mean (s) | 0.2 → 1.283 (+541.7%); 0.1 → 0.4 (+300.0%); 0.2 → 1.6 (+700.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | L | batch: queue finished (s) | 773.5 → 779.8 (+0.8%); 786.7 → 795.4 (+1.1%); 805.3 → 815.8 (+1.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.05 → 0.2167 (+333.3%); 0.07083 → 0.1 (+41.2%); 0.07917 → 0.2875 (+263.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 → 0.5 (+150.0%); 0.5 → 0.7 (+40.0%); 0.6 → 0.8 (+33.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 79.67 → 85 (+6.7%); 92.78 → 99.66 (+7.4%); 110.6 → 120.8 (+9.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_TOP.md` | omni-v26 | L | response time (ms), 99th percentile | 1661 → 1720 (+3.6%); 1638 → 1660 (+1.4%); 1777 → 1790 (+0.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_TOP.md` | omni-v26 | L | time over the response line (% of samples) | 51.69 → 52.98 (+2.5%); 48.63 → 48.85 (+0.5%); 52.79 → 53.4 (+1.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_TOP.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24 → 24 (±0.0%); 22.5 → 23 (+2.2%); 22.5 → 22.5 (±0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_TOP.md` | omni-v26 | L | pod start wait, total (s) | 4.3; 0.2 → 3.4 (+1600.0%); 0.9 → 1.7 (+88.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_TOP.md` | omni-v26 | L | pod start wait, mean (s) | 2.04; 0.2 → 2.35 (+1075.0%); 0.75 → 1.7 (+126.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_TOP.md` | omni-v26 | L | batch: queue finished (s) | 1455 → 1462 (+0.5%); 1364 → 1388 (+1.8%); 1363 → 1360 (−0.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUBERAY_4W_TOP.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 998.2 → 1057 (+5.9%); 870.3 → 888 (+2.0%); 878.9 → 877.2 (−0.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | response time (ms), 95th percentile | 1153 → 1308 (+13.5%); 1080 → 1187 (+9.9%); 1575 → 1669 (+6.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | response time (ms), 99th percentile | 1611 → 1856 (+15.2%); 1495 → 1641 (+9.8%); 2270 → 2386 (+5.1%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | failed requests (%) | 0.011299435028248588; 0.0; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 → 9.6 (+21.5%); 8.3 → 9.8 (+18.1%); 8.9 → 9.3 (+4.5%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | pod start wait, total (s) | 4.8; 3.5; 0.3 → 2 (+566.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | pod start wait, mean (s) | 1.8499999999999996; 2.15; 0.3 → 1.15 (+283.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | batch: queue finished (s) | 781.1 → 791.4 (+1.3%); 774.7 → 783.4 (+1.1%); 812.4 → 819.6 (+0.9%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.1417 → 0.7292 (+414.7%); 0.1542 → 0.2958 (+91.9%); 0.35 → 0.5583 (+59.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 → 4.5 (+462.5%); 0.9 → 1.6 (+77.8%); 1.5 → 1.8 (+20.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 84.98 → 95.59 (+12.5%); 79.76 → 86.92 (+9.0%); 117 → 124.4 (+6.3%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | L | response time (ms), 95th percentile | 1428 → 1578 (+10.5%); 1121 → 1251 (+11.6%); 1193 → 1339 (+12.2%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | L | response time (ms), 99th percentile | 1949 → 2257 (+15.8%); 1633 → 1782 (+9.1%); 1686 → 1883 (+11.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | L | time over the response line (% of samples) | 17.32 → 17.71 (+2.2%); 13.26 → 15.14 (+14.2%); 13.46 → 13.55 (+0.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 → 10 (+7.5%); 7.7 → 8.5 (+10.4%); 6.6 → 7 (+6.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | L | pod start wait, total (s) | 0.4 → 3.3 (+725.0%); 0.9 → 2.4 (+166.7%); 3.4 | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | L | pod start wait, mean (s) | 0.4 → 1.383 (+245.8%); 0.45 → 1 (+122.2%); 1.25 | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | L | batch: queue finished (s) | 801.3 → 811.3 (+1.2%); 776.6 → 787.7 (+1.4%); 783.4 → 795.8 (+1.6%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.05 → 0.05417 (+8.3%); 0.1042 → 0.1292 (+24.0%); 0.03333 → 0.1792 (+437.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 105.7 → 116.2 (+9.9%); 81.04 → 91.89 (+13.4%); 88.5 → 99.51 (+12.4%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | L | response time (ms), 95th percentile | 1549 → 1674 (+8.1%); 1228 → 1399 (+14.0%); 1274 → 1344 (+5.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | L | response time (ms), 99th percentile | 2202 → 2427 (+10.2%); 1723 → 2056 (+19.3%); 1787 → 1894 (+6.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | L | time over the response line (% of samples) | 17.7 → 17.77 (+0.4%); 15.43 → 16.33 (+5.8%); 13.73 → 13.82 (+0.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 → 10.5 (+6.1%); 8.5 → 9.1 (+7.1%); 6.7 → 7.1 (+6.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | L | pod start wait, total (s) | 0.3 → 2.9 (+866.7%); 0.5 → 2.9 (+480.0%); 0.5 → 2.4 (+380.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | L | pod start wait, mean (s) | 0.3 → 1.183 (+294.4%); 0.5 → 1.15 (+130.0%); 0.5 → 1.225 (+145.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | L | batch: queue finished (s) | 809.4 → 820 (+1.3%); 786.9 → 798.7 (+1.5%); 788.6 → 797.2 (+1.1%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.1833 → 0.3167 (+72.7%); 0.2333 → 0.6167 (+164.3%); 0.15 → 0.3417 (+127.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 112.1 → 123.5 (+10.2%); 90.55 → 102.6 (+13.3%); 93.47 → 101.6 (+8.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | response time (ms), mean | 659.9 → 737.2 (+11.7%); 482.7 → 538.9 (+11.6%); 642.6 → 770.9 (+20.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | response time (ms), 95th percentile | 2618 → 3053 (+16.6%); 1828 → 2234 (+22.2%); 2608 → 3333 (+27.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | response time (ms), 99th percentile | 3522 → 4091 (+16.2%); 2479 → 2966 (+19.6%); 3457 → 4424 (+28.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | time over the response line (% of samples) | 22.58 → 25.32 (+12.2%); 18.65 → 22.09 (+18.5%); 23.58 → 25.95 (+10.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | failed requests (%) | 0.06204249821119181; 0.0; 0.01408 → 0.02992 (+112.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 → 13 (+13.0%); 10.5 → 11.9 (+13.3%); 11.4 → 12.6 (+10.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | pod start wait, total (s) | 0.2 → 9 (+4400.0%); 0.5 → 3.7 (+640.0%); 7.2 | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | pod start wait, mean (s) | 0.2 → 2.551 (+1175.4%); 0.3 → 1.367 (+355.6%); 1.788095238095238 | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | batch: queue finished (s) | 895.2 → 934.5 (+4.4%); 835.7 → 865.8 (+3.6%); 891.9 → 944 (+5.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 199.2 → 234.8 (+17.8%); 144.7 → 169.8 (+17.3%); 197.6 → 243.7 (+23.3%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | response time (ms), mean | 901.3 → 1155 (+28.2%); 703.3 → 809.9 (+15.2%); 911.8 → 1068 (+17.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | response time (ms), 95th percentile | 3171 → 4179 (+31.8%); 2521 → 3121 (+23.8%); 3332 → 3764 (+13.0%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | response time (ms), 99th percentile | 4305 → 5460 (+26.8%); 3317 → 4248 (+28.1%); 4495 → 4885 (+8.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | time over the response line (% of samples) | 31.55 → 40.39 (+28.0%); 27.06 → 34.18 (+26.3%); 30.92 → 35.73 (+15.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.2 → 18.1 (+27.5%); 13.2 → 15.4 (+16.7%); 12.9 → 15.2 (+17.8%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | pod start wait, total (s) | 0.7 → 10.8 (+1442.9%); 0.5 → 6.3 (+1160.0%); 0.6 → 8.5 (+1316.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | pod start wait, mean (s) | 0.7 → 2.544 (+263.5%); 0.5 → 2.323 (+364.7%); 0.3 → 1.74 (+480.2%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | batch: queue finished (s) | 1003 → 1079 (+7.6%); 919.6 → 1015 (+10.4%); 997.2 → 1060 (+6.3%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 275.9 → 368 (+33.4%); 210.6 → 265.6 (+26.1%); 282.6 → 341.1 (+20.7%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | L | queue: jobs unfinished at the window's end | 0.0; 0.2; 0.0 | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_PGBENCH.md` | omni-v26 | L | select: p95_ms | 0.8437 → 0.8417 (−0.2%); 1.306 → 1.456 (+11.5%); 0.8637 → 0.8787 (+1.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_PGBENCH.md` | omni-v26 | L | select: mean_ms | 0.4229 → 0.4238 (+0.2%); 0.3935 → 1.071 (+172.3%); 0.4299 → 0.4325 (+0.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_PGBENCH_SERVICE.md` | omni-v26 | L | select: p95_ms | 0.9473 → 0.955 (+0.8%); 1.106 → 1.131 (+2.3%); 0.901 → 0.8967 (−0.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_PGBENCH_SERVICE.md` | omni-v26 | L | simple_update: p50_ms | 1.365 → 1.375 (+0.7%); 1.425 → 1.422 (−0.2%); 0.6507 → 0.664 (+2.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_PGBENCH_SERVICE.md` | omni-v26 | L | tpcb_hot: mean_ms | 2.134 → 2.275 (+6.6%); 2.136 → 2.131 (−0.2%); 2.181 → 2.312 (+6.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_ROBUST_KILL.md` | omni-v26 | L | pod start wait, total (s) | 7.9 → 22.2 (+181.0%); 8.9 → 18.2 (+104.5%); 8.7 → 21.5 (+147.1%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_ROBUST_KILL.md` | omni-v26 | L | robust: failed requests in the 300 s after the kill (%) | 43.09 → 46.98 (+9.0%); 42.7 → 44.37 (+3.9%); 45.22 → 49.06 (+8.5%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_ROBUST_LONG.md` | omni-v26 | L | pod start wait, total (s) | 12.67 → 48 (+278.9%); 7.333 → 26.67 (+263.6%); 19.67 → 70.33 (+257.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_ROBUST_LONG.md` | omni-v26 | L | pod start wait, mean (s) | 1.562 → 1.619 (+3.6%); 1.567 → 1.915 (+22.3%); 1.304 → 1.451 (+11.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_SYSBENCH_SHIPPED.md` | omni-v26 | L | burst: p95_ms | 2.666 → 3.009 (+12.9%); 2.898 → 2.896 (−0.1%); 4.078 → 4.103 (+0.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_SYSBENCH_SHIPPED.md` | omni-v26 | L | burst: p99_ms | 4.129 → 4.725 (+14.4%); 4.36 → 4.543 (+4.2%); 5.672 → 5.92 (+4.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_SYSBENCH_SHIPPED.md` | omni-v26 | L | read_only: p95_ms | 3.038 → 3.208 (+5.6%); 3.405 → 3.428 (+0.7%); 4.004 → 4.101 (+2.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_SYSBENCH_SHIPPED.md` | omni-v26 | L | read_only: p99_ms | 4.101 → 4.411 (+7.6%); 4.461 → 4.683 (+5.0%); 5.309 → 5.57 (+4.9%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_TRACE_GOOGLE2011.md` | omni-v26 | L | pod start wait, total (s) | 10.4 → 28.4 (+173.1%); 10.4 → 27.8 (+167.3%); 9.1 → 23.9 (+162.6%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_VANILLA.md` | omni-v26 | L | response time (ms), 95th percentile | 1223 → 1406 (+15.0%); 1625 → 1801 (+10.8%); 1160 → 1285 (+10.8%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_VANILLA.md` | omni-v26 | L | response time (ms), 99th percentile | 1753 → 1900 (+8.4%); 2273 → 2553 (+12.3%); 1629 → 1756 (+7.8%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_VANILLA.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 → 6.3 (+1.6%); 10.7 → 10.9 (+1.9%); 7.7 → 8.7 (+13.0%) | weak; 1 of 3 beyond the noise |
| `results/live/V26_VANILLA.md` | omni-v26 | L | pod start wait, total (s) | 4.0; 4.2; 0.1 → 3.2 (+3100.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_VANILLA.md` | omni-v26 | L | pod start wait, mean (s) | 1.5733333333333335; 1.675; 0.1 → 1.5 (+1400.0%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_VANILLA.md` | omni-v26 | L | batch: queue finished (s) | 792.1 → 799.1 (+0.9%); 810.4 → 820.6 (+1.3%); 776.1 → 786.4 (+1.3%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_VANILLA.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.1667 → 0.2083 (+25.0%); 0.04583 → 0.1125 (+145.5%); 0.07083 → 0.225 (+217.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_VANILLA.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 → 1.3 (+44.4%); 0.4 → 0.9 (+125.0%); 0.2 → 1.7 (+750.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_VANILLA.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 97.71 → 105.6 (+8.1%); 116.7 → 126.4 (+8.3%); 81.89 → 90.47 (+10.5%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_VOLCANO.md` | omni-v26 | L | response time (ms), 95th percentile | 703.2 → 880.6 (+25.2%); 473.4 → 536.4 (+13.3%); 1099 → 1331 (+21.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_VOLCANO.md` | omni-v26 | L | response time (ms), 99th percentile | 1167 → 1404 (+20.3%); 729.5 → 808.8 (+10.9%); 1740 → 1975 (+13.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_VOLCANO.md` | omni-v26 | L | time over the response line (% of samples) | 6.358 → 7.332 (+15.3%); 2.679 → 2.948 (+10.1%); 11.27 → 11.89 (+5.5%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_VOLCANO.md` | omni-v26 | L | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 → 5.5 (+12.2%); 2 → 2.5 (+25.0%); 7 → 7.8 (+11.4%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_VOLCANO.md` | omni-v26 | L | pod start wait, total (s) | 0.9; 1.0; 0.4 → 0.9 (+125.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_VOLCANO.md` | omni-v26 | L | pod start wait, mean (s) | 0.45; 0.7333333333333333; 0.4 → 0.7 (+75.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_VOLCANO.md` | omni-v26 | L | batch: queue finished (s) | 772.8 → 782.1 (+1.2%); 745.7 → 750.3 (+0.6%); 805 → 814.1 (+1.1%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_VOLCANO.md` | omni-v26 | L | queue: job wait, submitted to its first pod running, mean (s) | 0.7292 → 0.75 (+2.9%); 0.6833 → 0.7167 (+4.9%); 0.7833 → 0.875 (+11.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_VOLCANO.md` | omni-v26 | L | queue: job turnaround, submitted to done, mean (s) | 83.83 → 92.07 (+9.8%); 51.27 → 57.43 (+12.0%); 114.1 → 125.1 (+9.7%) | moderate; 2 of 3 beyond the noise |
| `results/live/V26_WANDERING.md` | omni-v26 | L | pod start wait, total (s) | 7.5 → 15.7 (+109.3%); 7.2 → 16.8 (+133.3%); 7.3 → 15.2 (+108.2%) | strong; 3 of 3 beyond the noise |
| `results/live/V26_WANDERING.md` | omni-v26 | L | pod start wait, mean (s) | 1.325 → 1.544 (+16.6%); 1.577 → 1.714 (+8.7%); 1.396 → 1.684 (+20.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_YCSB.md` | omni-v26 | L | b: p99_ms | 0.4953 → 0.4983 (+0.6%); 0.394 → 0.3987 (+1.2%); 0.3697 → 0.3743 (+1.3%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_YCSB.md` | omni-v26 | L | burst: p95_ms | 0.3517 → 0.3547 (+0.9%); 0.468 → 0.4737 (+1.2%); 0.336 → 0.3413 (+1.6%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_YCSB.md` | omni-v26 | L | burst: p99_ms | 0.5087 → 0.514 (+1.0%); 0.6503 → 0.6793 (+4.5%); 0.5463 → 0.5473 (+0.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_YCSB.md` | omni-v26 | L | c: mean_ms | 0.05854 → 0.05973 (+2.0%); 0.1108 → 0.1105 (−0.3%); 0.1339 → 0.134 (+0.1%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_YCSB_SERVICE.md` | omni-v26 | L | c: p95_ms | 0.308 → 0.3087 (+0.2%); 0.3127 → 0.312 (−0.2%); 0.07833 → 0.07967 (+1.7%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_YCSB_SHIPPED.md` | omni-v26 | L | b: p95_ms | 0.093 → 0.09633 (+3.6%); 0.3043 → 0.31 (+1.9%); 0.127 → 0.128 (+0.8%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_YCSB_SHIPPED.md` | omni-v26 | L | b: p99_ms | 0.2353 → 0.2503 (+6.4%); 0.468 → 0.4767 (+1.9%); 0.3023 → 0.321 (+6.2%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_YCSB_SHIPPED.md` | omni-v26 | L | b: mean_ms | 0.05044 → 0.05121 (+1.5%); 0.1514 → 0.1527 (+0.9%); 0.05914 → 0.05914 (+0.0%) | inconclusive; 0 of 3 beyond the noise |
| `results/live/V26_YCSB_SHIPPED.md` | omni-v26 | L | burst: p95_ms | 0.316 → 0.3277 (+3.7%); 0.5253 → 0.526 (+0.1%); 0.328 → 0.332 (+1.2%) | inconclusive; 0 of 3 beyond the noise |

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
| `results/live/V25_AKS_FULL_BURST.md` | omni-v25 | superseded | against its native | L | A 41756593448 (3 reps, `198314d551ea`), B 41928730439 (3 reps, `488442cffa76`), C 42175112195 (3 reps, `869cb06c6488`) |
| `results/live/V25_ALL_FOUR.md` | omni-v25 | superseded | against its native | L | A 41751114338 (10 reps, `63fc4dc666d3`), B 41768859003 (10 reps, `db6e040b4584`), C 41780376170 (10 reps, `0a92e09fe669`) |
| `results/live/V25_ARMADA_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_ARMADA_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_ARMADA_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_ARMADA_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_ARMADA_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41828277526 (10 reps, `f79d0dcabf73`), B 41830587387 (10 reps, `f79d0dcabf73`), C 41830595635 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_BATCH.md` | omni-v25 | superseded | against its native | L | A 41753030885 (10 reps, `63fc4dc666d3`), B 41768876462 (10 reps, `db6e040b4584`), C 41781968016 (10 reps, `0a92e09fe669`) |
| `results/live/V25_BINPACK.md` | omni-v25 | superseded | against its native | L | A 41802308779 (10 reps, `7d379c6ebae3`), B 41802323140 (10 reps, `7d379c6ebae3`), C 41804425696 (10 reps, `1e2cfe68bf59`) |
| `results/live/V25_BINPACK_4W_BARE.md` | omni-v25 | superseded | against its native | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_BINPACK_4W_BOTH.md` | omni-v25 | superseded | two changes at once | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_BINPACK_4W_ORCH.md` | omni-v25 | superseded | the orchestrator's own | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_BINPACK_4W_TOP.md` | omni-v25 | superseded | against its native | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_BINPACK_4W_VS.md` | omni-v25 | superseded | in place of a controller | L | A 41810750964 (10 reps, `43b93436c26b`), B 41812549051 (10 reps, `43b93436c26b`), C 41814375146 (10 reps, `43b93436c26b`) |
| `results/live/V25_CAPACITY.md` | omni-v25 | superseded | against its native | L | in its own Markdown |
| `results/live/V25_CITYLEARN.md` | omni-v25 | superseded | against its native | S | in its own Markdown |
| `results/live/V25_COST_TO_MATCH.md` | omni-v25 | superseded | against its native | L | A 41798197387 (10 reps, `473c170f787e`), B 41798204788 (10 reps, `473c170f787e`), C 41798211646 (10 reps, `473c170f787e`) |
| `results/live/V25_CRANE_4W_BARE.md` | omni-v25 | superseded | against its native | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRANE_4W_BOTH.md` | omni-v25 | superseded | two changes at once | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRANE_4W_ORCH.md` | omni-v25 | superseded | the orchestrator's own | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRANE_4W_TOP.md` | omni-v25 | superseded | against its native | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRANE_4W_VS.md` | omni-v25 | superseded | in place of a controller | L | A 41816152588 (10 reps, `43b93436c26b`), B 41821621221 (10 reps, `92dda68811ad`), C 41828241662 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_CRUISEKUBE.md` | omni-v25 | superseded | against its native | L | A 41747200129 (10 reps, `ee22662430a9`), B 41765479982 (10 reps, `479d719fc787`), C 41777088814 (10 reps, `0a92e09fe669`) |
| `results/live/V25_CRUISEKUBE_RECORDER.md` | omni-v25 | superseded | against its native | L | A 42173265097 (10 reps, `869cb06c6488`), B 42173285642 (10 reps, `869cb06c6488`), C 42185619972 (10 reps, `869cb06c6488`) |
| `results/live/V25_FAIRNESS.md` | omni-v25 | superseded | against its native | L | A 41751121984 (10 reps, `63fc4dc666d3`), B 41768864707 (10 reps, `db6e040b4584`), C 41780381804 (10 reps, `0a92e09fe669`) |
| `results/live/V25_FAULTS.md` | omni-v25 | superseded | against its native | L | A 41753024820 (10 reps, `63fc4dc666d3`), B 41768870890 (10 reps, `db6e040b4584`), C 41781962156 (10 reps, `0a92e09fe669`) |
| `results/live/V25_FAULTS_EXTENDED.md` | omni-v25 | superseded | against its native | L | A 41792496184 (10 reps, `05092772357b`), B 41794354171 (10 reps, `05092772357b`), C 41796185630 (10 reps, `473c170f787e`) |
| `results/live/V25_GODEL_4W_BARE.md` | omni-v25 | superseded | against its native | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GODEL_4W_BOTH.md` | omni-v25 | superseded | two changes at once | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GODEL_4W_ORCH.md` | omni-v25 | superseded | the orchestrator's own | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GODEL_4W_TOP.md` | omni-v25 | superseded | against its native | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GODEL_4W_VS.md` | omni-v25 | superseded | in place of a controller | L | A 41816164023 (10 reps, `43b93436c26b`), B 41823813742 (10 reps, `92dda68811ad`), C 41828251636 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_GOLDILOCKS.md` | omni-v25 | superseded | against its native | L | A 41749168920 (10 reps, `ee22662430a9`), B 41765485855 (10 reps, `479d719fc787`), C 41777095500 (10 reps, `0a92e09fe669`) |
| `results/live/V25_KAFKA.md` | omni-v25 | superseded | against its native | L | A 41756685178 (? reps, `198314d551ea`), B 41770452498 (? reps, `db6e040b4584`), C 41783615016 (? reps, `0a92e09fe669`) |
| `results/live/V25_KAFKA_SERVICE.md` | omni-v25 | superseded | against its native | L | A 41758475899 (? reps, `e29ad045b2ac`), B 41772114283 (? reps, `db6e040b4584`), C 41785350365 (? reps, `0a92e09fe669`) |
| `results/live/V25_KAI.md` | omni-v25 | superseded | against its native | L | A 41800238758 (10 reps, `7d379c6ebae3`), B 41800247331 (10 reps, `7d379c6ebae3`), C 41800254736 (10 reps, `7d379c6ebae3`) |
| `results/live/V25_KAI_4W_BARE.md` | omni-v25 | superseded | against its native | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KAI_4W_BOTH.md` | omni-v25 | superseded | two changes at once | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KAI_4W_ORCH.md` | omni-v25 | superseded | the orchestrator's own | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KAI_4W_TOP.md` | omni-v25 | superseded | against its native | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KAI_4W_VS.md` | omni-v25 | superseded | in place of a controller | L | A 41809041712 (10 reps, `46a18f6329e6`), B 41810759693 (10 reps, `43b93436c26b`), C 41812560443 (10 reps, `43b93436c26b`) |
| `results/live/V25_KARMADA_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KARMADA_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KARMADA_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KARMADA_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KARMADA_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41816173049 (10 reps, `43b93436c26b`), B 41823821537 (10 reps, `92dda68811ad`), C 41828260509 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KEDA_CPU_REQUESTS.md` | omni-v25 | superseded | against its native | L | A 41753044221 (10 reps, `63fc4dc666d3`), B 41770442526 (10 reps, `db6e040b4584`), C 41781979744 (10 reps, `0a92e09fe669`) |
| `results/live/V25_KEDA_REQUESTS.md` | omni-v25 | superseded | against its native | L | A 41753044221 (10 reps, `63fc4dc666d3`), B 41770442526 (10 reps, `db6e040b4584`), C 41781979744 (10 reps, `0a92e09fe669`) |
| `results/live/V25_KOORDINATOR.md` | omni-v25 | superseded | against its native | L | A 41800261877 (10 reps, `7d379c6ebae3`), B 41800269022 (10 reps, `7d379c6ebae3`), C 41802293120 (10 reps, `7d379c6ebae3`) |
| `results/live/V25_KOORDINATOR_CGROUP.md` | omni-v25 | superseded | against its native | L | A 42173258848 (10 reps, `869cb06c6488`), B 42173278954 (10 reps, `869cb06c6488`), C 42185612749 (10 reps, `869cb06c6488`) |
| `results/live/V25_KUBERAY_4W_BARE.md` | omni-v25 | superseded | against its native | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUBERAY_4W_BOTH.md` | omni-v25 | superseded | two changes at once | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUBERAY_4W_ORCH.md` | omni-v25 | superseded | the orchestrator's own | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUBERAY_4W_TOP.md` | omni-v25 | superseded | against its native | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUBERAY_4W_VS.md` | omni-v25 | superseded | in place of a controller | L | A 41816118654 (10 reps, `43b93436c26b`), B 41821612423 (10 reps, `92dda68811ad`), C 41828233886 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_KUEUE.md` | omni-v25 | superseded | against its native | L | A 41762066634 (10 reps, `e391835931e7`), B 41775363004 (10 reps, `db6e040b4584`), C 41788859873 (10 reps, `0a92e09fe669`) |
| `results/live/V25_KUEUE_4W_BARE.md` | omni-v25 | superseded | against its native | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_KUEUE_4W_BOTH.md` | omni-v25 | superseded | two changes at once | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_KUEUE_4W_ORCH.md` | omni-v25 | superseded | the orchestrator's own | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_KUEUE_4W_TOP.md` | omni-v25 | superseded | against its native | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_KUEUE_4W_VS.md` | omni-v25 | superseded | in place of a controller | L | A 41809077335 (10 reps, `46a18f6329e6`), B 41810798821 (10 reps, `43b93436c26b`), C 41812580198 (10 reps, `43b93436c26b`) |
| `results/live/V25_MUJOCO.md` | omni-v25 | superseded | against its native | S | in its own Markdown |
| `results/live/V25_OCM_4W_BARE.md` | omni-v25 | superseded | against its native | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_OCM_4W_BOTH.md` | omni-v25 | superseded | two changes at once | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_OCM_4W_ORCH.md` | omni-v25 | superseded | the orchestrator's own | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_OCM_4W_TOP.md` | omni-v25 | superseded | against its native | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_OCM_4W_VS.md` | omni-v25 | superseded | in place of a controller | L | A 41816181570 (10 reps, `43b93436c26b`), B 41823829193 (10 reps, `92dda68811ad`), C 41828268372 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_PANDAPOWER.md` | omni-v25 | superseded | against its native | S | in its own Markdown |
| `results/live/V25_PGBENCH.md` | omni-v25 | superseded | against its native | L | A 41756691131 (? reps, `198314d551ea`), B 41770457639 (? reps, `db6e040b4584`), C 41783620506 (? reps, `0a92e09fe669`) |
| `results/live/V25_PGBENCH_SERVICE.md` | omni-v25 | superseded | against its native | L | A 41790655143 (? reps, `0a92e09fe669`), B 41792513596 (? reps, `05092772357b`), C 41794373430 (? reps, `05092772357b`) |
| `results/live/V25_REDIS.md` | omni-v25 | superseded | against its native | L | A 41756679520 (? reps, `198314d551ea`), B 41770447406 (? reps, `db6e040b4584`), C 41781985238 (? reps, `0a92e09fe669`) |
| `results/live/V25_REDIS_SERVICE.md` | omni-v25 | superseded | against its native | L | A 41756709406 (? reps, `198314d551ea`), B 41772107768 (? reps, `db6e040b4584`), C 41783637007 (? reps, `0a92e09fe669`) |
| `results/live/V25_REDIS_SHIPPED.md` | omni-v25 | superseded | against its native | L | A 41758488505 (? reps, `e29ad045b2ac`), B 41772126598 (? reps, `db6e040b4584`), C 41785361755 (? reps, `0a92e09fe669`) |
| `results/live/V25_ROBUST_KILL.md` | omni-v25 | superseded | against its native | L | A 41760298127 (10 reps, `e391835931e7`), B 41775351685 (10 reps, `db6e040b4584`), C 41788847807 (10 reps, `0a92e09fe669`) |
| `results/live/V25_ROBUST_LONG.md` | omni-v25 | superseded | against its native | L | A 41762060399 (3 reps, `e391835931e7`), B 41775357254 (3 reps, `db6e040b4584`), C 41788854067 (3 reps, `0a92e09fe669`) |
| `results/live/V25_SOLO.md` | omni-v25 | superseded | in place of a controller | L | A 41751093197 (10 reps, `63fc4dc666d3`), B 41767225693 (10 reps, `479d719fc787`), C 41780359295 (10 reps, `0a92e09fe669`) |
| `results/live/V25_SOLO_2.md` | omni-v25 | superseded | in place of a controller | L | A 41832884727 (10 reps, `f79d0dcabf73`), B 41832892271 (10 reps, `f79d0dcabf73`), C 41832900683 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_SOLO_2_VS_ON_NATIVE.md` | omni-v25 | superseded | in place of a controller | L | A 41832884727 (10 reps, `f79d0dcabf73`), B 41832892271 (10 reps, `f79d0dcabf73`), C 41832900683 (10 reps, `f79d0dcabf73`) |
| `results/live/V25_SOLO_VS_ON_NATIVE.md` | omni-v25 | superseded | in place of a controller | L | A 41751093197 (10 reps, `63fc4dc666d3`), B 41767225693 (10 reps, `479d719fc787`), C 41780359295 (10 reps, `0a92e09fe669`) |
| `results/live/V25_STEADY.md` | omni-v25 | superseded | against its native | L | A 41751085804 (10 reps, `63fc4dc666d3`), B 41767220817 (10 reps, `479d719fc787`), C 41778758086 (10 reps, `0a92e09fe669`) |
| `results/live/V25_SWARM.md` | omni-v25 | superseded | against its native | S | in its own Markdown |
| `results/live/V25_SYSBENCH.md` | omni-v25 | superseded | against its native | L | A 41756697077 (? reps, `198314d551ea`), B 41770463075 (? reps, `db6e040b4584`), C 41783625994 (? reps, `0a92e09fe669`) |
| `results/live/V25_SYSBENCH_SERVICE.md` | omni-v25 | superseded | against its native | L | A 41790642021 (? reps, `0a92e09fe669`), B 41792502265 (? reps, `05092772357b`), C 41794360552 (? reps, `05092772357b`) |
| `results/live/V25_SYSBENCH_SHIPPED.md` | omni-v25 | superseded | against its native | L | A 41758482144 (? reps, `e29ad045b2ac`), B 41772120161 (? reps, `db6e040b4584`), C 41785356237 (? reps, `0a92e09fe669`) |
| `results/live/V25_TRACE_GOOGLE2011.md` | omni-v25 | superseded | against its native | L | A 41753037941 (10 reps, `63fc4dc666d3`), B 41768881626 (10 reps, `db6e040b4584`), C 41781973989 (10 reps, `0a92e09fe669`) |
| `results/live/V25_VANILLA.md` | omni-v25 | superseded | against its native | L | A 41802300531 (10 reps, `7d379c6ebae3`), B 41802315329 (10 reps, `7d379c6ebae3`), C 41804417539 (10 reps, `1e2cfe68bf59`) |
| `results/live/V25_VOLCANO.md` | omni-v25 | superseded | against its native | L | A 41762072500 (10 reps, `e391835931e7`), B 41775368304 (10 reps, `db6e040b4584`), C 41790635305 (10 reps, `0a92e09fe669`) |
| `results/live/V25_VOLCANO_4W_BARE.md` | omni-v25 | standing | against its native | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_VOLCANO_4W_BOTH.md` | omni-v25 | standing | two changes at once | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_VOLCANO_4W_ORCH.md` | omni-v25 | standing | the orchestrator's own | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_VOLCANO_4W_TOP.md` | omni-v25 | standing | against its native | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_VOLCANO_4W_VS.md` | omni-v25 | standing | in place of a controller | L | A 41809087487 (10 reps, `46a18f6329e6`), B 41812541481 (10 reps, `43b93436c26b`), C 41814366715 (10 reps, `43b93436c26b`) |
| `results/live/V25_WANDERING.md` | omni-v25 | superseded | against its native | L | A 41751107237 (10 reps, `63fc4dc666d3`), B 41768852229 (10 reps, `db6e040b4584`), C 41780370478 (10 reps, `0a92e09fe669`) |
| `results/live/V25_YCSB.md` | omni-v25 | superseded | against its native | L | A 41756703640 (? reps, `198314d551ea`), B 41770468145 (? reps, `db6e040b4584`), C 41783631371 (? reps, `0a92e09fe669`) |
| `results/live/V25_YCSB_SERVICE.md` | omni-v25 | superseded | against its native | L | A 41790648692 (? reps, `0a92e09fe669`), B 41792507887 (? reps, `05092772357b`), C 41794367186 (? reps, `05092772357b`) |
| `results/live/V25_YCSB_SHIPPED.md` | omni-v25 | superseded | against its native | L | A 41758494688 (? reps, `e29ad045b2ac`), B 41772133244 (? reps, `db6e040b4584`), C 41785367418 (? reps, `0a92e09fe669`) |
| `results/live/V26_AKS_FULL_BURST.md` | omni-v26 | standing | against its native | L | A 42416651121 (3 reps, `84462b32eacc`), B 42483841896 (3 reps, `c53a301d3751`), C 42651049003 (3 reps, `9a219c92c8c4`) |
| `results/live/V26_ALL_FOUR.md` | omni-v26 | standing | against its native | L | A 42406258911 (10 reps, `b806aadd5bbb`), B 42415420145 (10 reps, `84462b32eacc`), C 42427795427 (10 reps, `84462b32eacc`) |
| `results/live/V26_BATCH.md` | omni-v26 | standing | against its native | L | A 42407546216 (10 reps, `b806aadd5bbb`), B 42417953886 (10 reps, `84462b32eacc`), C 42427808988 (10 reps, `84462b32eacc`) |
| `results/live/V26_BINPACK.md` | omni-v26 | standing | against its native | L | A 42439660401 (10 reps, `f11b1b18673c`), B 42440706098 (10 reps, `f11b1b18673c`), C 42440713360 (10 reps, `f11b1b18673c`) |
| `results/live/V26_BINPACK_4W_BARE.md` | omni-v26 | standing | against its native | L | A 42444100547 (10 reps, `f11b1b18673c`), B 42445172518 (10 reps, `f11b1b18673c`), C 42446289715 (10 reps, `f11b1b18673c`) |
| `results/live/V26_BINPACK_4W_BOTH.md` | omni-v26 | standing | two changes at once | L | A 42444100547 (10 reps, `f11b1b18673c`), B 42445172518 (10 reps, `f11b1b18673c`), C 42446289715 (10 reps, `f11b1b18673c`) |
| `results/live/V26_BINPACK_4W_ORCH.md` | omni-v26 | standing | the orchestrator's own | L | A 42444100547 (10 reps, `f11b1b18673c`), B 42445172518 (10 reps, `f11b1b18673c`), C 42446289715 (10 reps, `f11b1b18673c`) |
| `results/live/V26_BINPACK_4W_TOP.md` | omni-v26 | standing | against its native | L | A 42444100547 (10 reps, `f11b1b18673c`), B 42445172518 (10 reps, `f11b1b18673c`), C 42446289715 (10 reps, `f11b1b18673c`) |
| `results/live/V26_BINPACK_4W_VS.md` | omni-v26 | standing | in place of a controller | L | A 42444100547 (10 reps, `f11b1b18673c`), B 42445172518 (10 reps, `f11b1b18673c`), C 42446289715 (10 reps, `f11b1b18673c`) |
| `results/live/V26_CAPACITY.md` | omni-v26 | standing | against its native | L | in its own Markdown |
| `results/live/V26_CITYLEARN.md` | omni-v26 | standing | against its native | S | in its own Markdown |
| `results/live/V26_COST_TO_MATCH.md` | omni-v26 | standing | against its native | L | A 42437385663 (10 reps, `bf9868379271`), B 42437389486 (10 reps, `bf9868379271`), C 42437393561 (10 reps, `bf9868379271`) |
| `results/live/V26_CRANE_4W_BARE.md` | omni-v26 | standing | against its native | L | A 42447367322 (10 reps, `f11b1b18673c`), B 42450499095 (10 reps, `f11b1b18673c`), C 42452540225 (10 reps, `f11b1b18673c`) |
| `results/live/V26_CRANE_4W_BOTH.md` | omni-v26 | standing | two changes at once | L | A 42447367322 (10 reps, `f11b1b18673c`), B 42450499095 (10 reps, `f11b1b18673c`), C 42452540225 (10 reps, `f11b1b18673c`) |
| `results/live/V26_CRANE_4W_ORCH.md` | omni-v26 | standing | the orchestrator's own | L | A 42447367322 (10 reps, `f11b1b18673c`), B 42450499095 (10 reps, `f11b1b18673c`), C 42452540225 (10 reps, `f11b1b18673c`) |
| `results/live/V26_CRANE_4W_TOP.md` | omni-v26 | standing | against its native | L | A 42447367322 (10 reps, `f11b1b18673c`), B 42450499095 (10 reps, `f11b1b18673c`), C 42452540225 (10 reps, `f11b1b18673c`) |
| `results/live/V26_CRANE_4W_VS.md` | omni-v26 | standing | in place of a controller | L | A 42447367322 (10 reps, `f11b1b18673c`), B 42450499095 (10 reps, `f11b1b18673c`), C 42452540225 (10 reps, `f11b1b18673c`) |
| `results/live/V26_CRUISEKUBE.md` | omni-v26 | standing | against its native | L | A 42403615734 (10 reps, `5d13597b94dc`), B 42413970707 (10 reps, `0d5b2754d310`), C 42425416413 (10 reps, `84462b32eacc`) |
| `results/live/V26_CRUISEKUBE_RECORDER.md` | omni-v26 | standing | against its native | L | A 42436262163 (10 reps, `bf9868379271`), B 42436265627 (10 reps, `bf9868379271`), C 42437381465 (10 reps, `bf9868379271`) |
| `results/live/V26_FAIRNESS.md` | omni-v26 | standing | against its native | L | A 42406263563 (10 reps, `b806aadd5bbb`), B 42417945882 (10 reps, `84462b32eacc`), C 42427800113 (10 reps, `84462b32eacc`) |
| `results/live/V26_FAULTS.md` | omni-v26 | standing | against its native | L | A 42407542058 (10 reps, `b806aadd5bbb`), B 42417949915 (10 reps, `84462b32eacc`), C 42427804535 (10 reps, `84462b32eacc`) |
| `results/live/V26_FAULTS_EXTENDED.md` | omni-v26 | standing | against its native | L | A 42433917965 (10 reps, `bf9868379271`), B 42435068170 (10 reps, `bf9868379271`), C 42436258993 (10 reps, `bf9868379271`) |
| `results/live/V26_GODEL_4W_BARE.md` | omni-v26 | standing | against its native | L | A 42447370557 (10 reps, `f11b1b18673c`), B 42451531911 (10 reps, `f11b1b18673c`), C 42452543740 (10 reps, `f11b1b18673c`) |
| `results/live/V26_GODEL_4W_BOTH.md` | omni-v26 | standing | two changes at once | L | A 42447370557 (10 reps, `f11b1b18673c`), B 42451531911 (10 reps, `f11b1b18673c`), C 42452543740 (10 reps, `f11b1b18673c`) |
| `results/live/V26_GODEL_4W_ORCH.md` | omni-v26 | standing | the orchestrator's own | L | A 42447370557 (10 reps, `f11b1b18673c`), B 42451531911 (10 reps, `f11b1b18673c`), C 42452543740 (10 reps, `f11b1b18673c`) |
| `results/live/V26_GODEL_4W_TOP.md` | omni-v26 | standing | against its native | L | A 42447370557 (10 reps, `f11b1b18673c`), B 42451531911 (10 reps, `f11b1b18673c`), C 42452543740 (10 reps, `f11b1b18673c`) |
| `results/live/V26_GODEL_4W_VS.md` | omni-v26 | standing | in place of a controller | L | A 42447370557 (10 reps, `f11b1b18673c`), B 42451531911 (10 reps, `f11b1b18673c`), C 42452543740 (10 reps, `f11b1b18673c`) |
| `results/live/V26_GOLDILOCKS.md` | omni-v26 | standing | against its native | L | A 42404915439 (10 reps, `5d13597b94dc`), B 42413975817 (10 reps, `0d5b2754d310`), C 42425420205 (10 reps, `84462b32eacc`) |
| `results/live/V26_KAFKA.md` | omni-v26 | standing | against its native | L | A 42407564542 (? reps, `b806aadd5bbb`), B 42419219065 (? reps, `84462b32eacc`), C 42429039058 (? reps, `25130545f054`) |
| `results/live/V26_KAFKA_SERVICE.md` | omni-v26 | standing | against its native | L | A 42408820342 (? reps, `e81cb06c22b0`), B 42419242767 (? reps, `84462b32eacc`), C 42430252207 (? reps, `25130545f054`) |
| `results/live/V26_KAI.md` | omni-v26 | standing | against its native | L | A 42438540677 (10 reps, `f11b1b18673c`), B 42438544638 (10 reps, `f11b1b18673c`), C 42438548043 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KAI_4W_BARE.md` | omni-v26 | standing | against its native | L | A 42442968048 (10 reps, `f11b1b18673c`), B 42444104246 (10 reps, `f11b1b18673c`), C 42445176352 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KAI_4W_BOTH.md` | omni-v26 | standing | two changes at once | L | A 42442968048 (10 reps, `f11b1b18673c`), B 42444104246 (10 reps, `f11b1b18673c`), C 42445176352 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KAI_4W_ORCH.md` | omni-v26 | standing | the orchestrator's own | L | A 42442968048 (10 reps, `f11b1b18673c`), B 42444104246 (10 reps, `f11b1b18673c`), C 42445176352 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KAI_4W_TOP.md` | omni-v26 | standing | against its native | L | A 42442968048 (10 reps, `f11b1b18673c`), B 42444104246 (10 reps, `f11b1b18673c`), C 42445176352 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KAI_4W_VS.md` | omni-v26 | standing | in place of a controller | L | A 42442968048 (10 reps, `f11b1b18673c`), B 42444104246 (10 reps, `f11b1b18673c`), C 42445176352 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KEDA_CPU_REQUESTS.md` | omni-v26 | standing | against its native | L | A 42407555127 (10 reps, `b806aadd5bbb`), B 42417962056 (10 reps, `84462b32eacc`), C 42427818792 (10 reps, `84462b32eacc`) |
| `results/live/V26_KEDA_REQUESTS.md` | omni-v26 | standing | against its native | L | A 42407555127 (10 reps, `b806aadd5bbb`), B 42417962056 (10 reps, `84462b32eacc`), C 42427818792 (10 reps, `84462b32eacc`) |
| `results/live/V26_KOORDINATOR.md` | omni-v26 | standing | against its native | L | A 42438551739 (10 reps, `f11b1b18673c`), B 42439648015 (10 reps, `f11b1b18673c`), C 42439651965 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KOORDINATOR_CGROUP.md` | omni-v26 | standing | against its native | L | A 42440716851 (10 reps, `f11b1b18673c`), B 42441844056 (10 reps, `f11b1b18673c`), C 42441848181 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUBERAY_4W_BARE.md` | omni-v26 | standing | against its native | L | A 42447364135 (10 reps, `f11b1b18673c`), B 42450495106 (10 reps, `f11b1b18673c`), C 42452536842 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUBERAY_4W_BOTH.md` | omni-v26 | standing | two changes at once | L | A 42447364135 (10 reps, `f11b1b18673c`), B 42450495106 (10 reps, `f11b1b18673c`), C 42452536842 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUBERAY_4W_ORCH.md` | omni-v26 | standing | the orchestrator's own | L | A 42447364135 (10 reps, `f11b1b18673c`), B 42450495106 (10 reps, `f11b1b18673c`), C 42452536842 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUBERAY_4W_TOP.md` | omni-v26 | standing | against its native | L | A 42447364135 (10 reps, `f11b1b18673c`), B 42450495106 (10 reps, `f11b1b18673c`), C 42452536842 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUBERAY_4W_VS.md` | omni-v26 | standing | in place of a controller | L | A 42447364135 (10 reps, `f11b1b18673c`), B 42450495106 (10 reps, `f11b1b18673c`), C 42452536842 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUEUE.md` | omni-v26 | standing | against its native | L | A 42412690276 (10 reps, `e81cb06c22b0`), B 42422950496 (10 reps, `84462b32eacc`), C 42432716761 (10 reps, `bf9868379271`) |
| `results/live/V26_KUEUE_4W_BARE.md` | omni-v26 | standing | against its native | L | A 42442976725 (10 reps, `f11b1b18673c`), B 42445165273 (10 reps, `f11b1b18673c`), C 42445184360 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUEUE_4W_BOTH.md` | omni-v26 | standing | two changes at once | L | A 42442976725 (10 reps, `f11b1b18673c`), B 42445165273 (10 reps, `f11b1b18673c`), C 42445184360 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUEUE_4W_ORCH.md` | omni-v26 | standing | the orchestrator's own | L | A 42442976725 (10 reps, `f11b1b18673c`), B 42445165273 (10 reps, `f11b1b18673c`), C 42445184360 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUEUE_4W_TOP.md` | omni-v26 | standing | against its native | L | A 42442976725 (10 reps, `f11b1b18673c`), B 42445165273 (10 reps, `f11b1b18673c`), C 42445184360 (10 reps, `f11b1b18673c`) |
| `results/live/V26_KUEUE_4W_VS.md` | omni-v26 | standing | in place of a controller | L | A 42442976725 (10 reps, `f11b1b18673c`), B 42445165273 (10 reps, `f11b1b18673c`), C 42445184360 (10 reps, `f11b1b18673c`) |
| `results/live/V26_MUJOCO.md` | omni-v26 | standing | against its native | S | in its own Markdown |
| `results/live/V26_OCM_4W_BARE.md` | omni-v26 | standing | against its native | L | A 42447377308 (10 reps, `f11b1b18673c`), B 42452533513 (10 reps, `f11b1b18673c`), C 42453594917 (10 reps, `f11b1b18673c`) |
| `results/live/V26_OCM_4W_BOTH.md` | omni-v26 | standing | two changes at once | L | A 42447377308 (10 reps, `f11b1b18673c`), B 42452533513 (10 reps, `f11b1b18673c`), C 42453594917 (10 reps, `f11b1b18673c`) |
| `results/live/V26_OCM_4W_ORCH.md` | omni-v26 | standing | the orchestrator's own | L | A 42447377308 (10 reps, `f11b1b18673c`), B 42452533513 (10 reps, `f11b1b18673c`), C 42453594917 (10 reps, `f11b1b18673c`) |
| `results/live/V26_OCM_4W_TOP.md` | omni-v26 | standing | against its native | L | A 42447377308 (10 reps, `f11b1b18673c`), B 42452533513 (10 reps, `f11b1b18673c`), C 42453594917 (10 reps, `f11b1b18673c`) |
| `results/live/V26_OCM_4W_VS.md` | omni-v26 | standing | in place of a controller | L | A 42447377308 (10 reps, `f11b1b18673c`), B 42452533513 (10 reps, `f11b1b18673c`), C 42453594917 (10 reps, `f11b1b18673c`) |
| `results/live/V26_PANDAPOWER.md` | omni-v26 | standing | against its native | S | in its own Markdown |
| `results/live/V26_PGBENCH.md` | omni-v26 | standing | against its native | L | A 42408804202 (? reps, `e81cb06c22b0`), B 42419223817 (? reps, `84462b32eacc`), C 42429043967 (? reps, `25130545f054`) |
| `results/live/V26_PGBENCH_SERVICE.md` | omni-v26 | standing | against its native | L | A 42433914189 (? reps, `bf9868379271`), B 42435063823 (? reps, `bf9868379271`), C 42435151691 (? reps, `bf9868379271`) |
| `results/live/V26_REDIS.md` | omni-v26 | standing | against its native | L | A 42407559889 (? reps, `b806aadd5bbb`), B 42417966267 (? reps, `84462b32eacc`), C 42429034428 (? reps, `25130545f054`) |
| `results/live/V26_REDIS_SERVICE.md` | omni-v26 | standing | against its native | L | A 42408816232 (? reps, `e81cb06c22b0`), B 42419237751 (? reps, `84462b32eacc`), C 42429058867 (? reps, `25130545f054`) |
| `results/live/V26_REDIS_SHIPPED.md` | omni-v26 | standing | against its native | L | A 42410139533 (? reps, `e81cb06c22b0`), B 42420505631 (? reps, `84462b32eacc`), C 42430260591 (? reps, `25130545f054`) |
| `results/live/V26_ROBUST_KILL.md` | omni-v26 | standing | against its native | L | A 42411433795 (10 reps, `e81cb06c22b0`), B 42421747995 (10 reps, `84462b32eacc`), C 42431521983 (10 reps, `25130545f054`) |
| `results/live/V26_ROBUST_LONG.md` | omni-v26 | standing | against its native | L | A 42411438422 (3 reps, `e81cb06c22b0`), B 42422946374 (3 reps, `84462b32eacc`), C 42432712342 (3 reps, `bf9868379271`) |
| `results/live/V26_SOLO.md` | omni-v26 | standing | in place of a controller | L | A 42406245967 (10 reps, `b806aadd5bbb`), B 42415405827 (10 reps, `84462b32eacc`), C 42426635223 (10 reps, `84462b32eacc`) |
| `results/live/V26_SOLO_2.md` | omni-v26 | standing | in place of a controller | L | A 42457064085 (10 reps, `f11b1b18673c`), B 42457069917 (10 reps, `f11b1b18673c`), C 42457074398 (10 reps, `f11b1b18673c`) |
| `results/live/V26_SOLO_2_VS_ON_NATIVE.md` | omni-v26 | standing | in place of a controller | L | A 42457064085 (10 reps, `f11b1b18673c`), B 42457069917 (10 reps, `f11b1b18673c`), C 42457074398 (10 reps, `f11b1b18673c`) |
| `results/live/V26_SOLO_VS_ON_NATIVE.md` | omni-v26 | standing | in place of a controller | L | A 42406245967 (10 reps, `b806aadd5bbb`), B 42415405827 (10 reps, `84462b32eacc`), C 42426635223 (10 reps, `84462b32eacc`) |
| `results/live/V26_STEADY.md` | omni-v26 | standing | against its native | L | A 42406241542 (10 reps, `b806aadd5bbb`), B 42415400880 (10 reps, `84462b32eacc`), C 42426631088 (10 reps, `84462b32eacc`) |
| `results/live/V26_SWARM.md` | omni-v26 | standing | against its native | S | in its own Markdown |
| `results/live/V26_SYSBENCH.md` | omni-v26 | standing | against its native | L | A 42408808035 (? reps, `e81cb06c22b0`), B 42419228266 (? reps, `84462b32eacc`), C 42429048986 (? reps, `25130545f054`) |
| `results/live/V26_SYSBENCH_SERVICE.md` | omni-v26 | standing | against its native | L | A 42433905637 (? reps, `bf9868379271`), B 42435054949 (? reps, `bf9868379271`), C 42435143553 (? reps, `bf9868379271`) |
| `results/live/V26_SYSBENCH_SHIPPED.md` | omni-v26 | standing | against its native | L | A 42408824241 (? reps, `e81cb06c22b0`), B 42420501775 (? reps, `84462b32eacc`), C 42430256512 (? reps, `25130545f054`) |
| `results/live/V26_TRACE_GOOGLE2011.md` | omni-v26 | standing | against its native | L | A 42407550879 (10 reps, `b806aadd5bbb`), B 42417958110 (10 reps, `84462b32eacc`), C 42427813944 (10 reps, `84462b32eacc`) |
| `results/live/V26_VANILLA.md` | omni-v26 | standing | against its native | L | A 42439656396 (10 reps, `f11b1b18673c`), B 42439664303 (10 reps, `f11b1b18673c`), C 42440709856 (10 reps, `f11b1b18673c`) |
| `results/live/V26_VOLCANO.md` | omni-v26 | standing | against its native | L | A 42412695021 (10 reps, `e81cb06c22b0`), B 42422954360 (10 reps, `84462b32eacc`), C 42432720979 (10 reps, `bf9868379271`) |
| `results/live/V26_WANDERING.md` | omni-v26 | standing | against its native | L | A 42406254590 (10 reps, `b806aadd5bbb`), B 42415415600 (10 reps, `84462b32eacc`), C 42426642847 (10 reps, `84462b32eacc`) |
| `results/live/V26_YCSB.md` | omni-v26 | standing | against its native | L | A 42408812057 (? reps, `e81cb06c22b0`), B 42419232825 (? reps, `84462b32eacc`), C 42429053789 (? reps, `25130545f054`) |
| `results/live/V26_YCSB_SERVICE.md` | omni-v26 | standing | against its native | L | A 42433909760 (? reps, `bf9868379271`), B 42435059254 (? reps, `bf9868379271`), C 42435147369 (? reps, `bf9868379271`) |
| `results/live/V26_YCSB_SHIPPED.md` | omni-v26 | standing | against its native | L | A 42410144402 (? reps, `e81cb06c22b0`), B 42420509695 (? reps, `84462b32eacc`), C 42430264345 (? reps, `25130545f054`) |
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
