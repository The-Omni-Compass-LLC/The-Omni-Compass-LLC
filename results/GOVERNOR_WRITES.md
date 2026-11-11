# What the governor wrote and what it cost on every batch-stream rig: omni-v25 against omni-v26

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Read from the governor's own audit (`audit.jsonl`) in every repetition of the three runs each rig's table was written from (`results/live/RECIPES.json`), on the branch `raw`, by `tools/governor_writes.py`. Each cell is the mean an arm a repetition (Omni-Compass's arms only: on top of the scheduler, and on the organism alone in the four ways), with its range. It reads what the governor did; it judges nothing: the readings stand in each rig's own three-run table.

## Web target writes

| Rig | omni-v25 | omni-v26 |
|---|---:|---:|
| the batch stream alone | 0.3 (0 to 3) | 0.0 (0 to 0) |
| the default scheduler | 10.0 (2 to 22) | 4.5 (2 to 13) |
| the bin-packing profile | 10.2 (2 to 22) | 3.4 (0 to 7) |
| KAI | 7.3 (1 to 21) | 2.8 (0 to 7) |
| Kueue | 10.1 (2 to 27) | 3.9 (2 to 8) |
| Volcano | 7.0 (1 to 23) | 2.7 (0 to 8) |
| Koordinator | 1.7 (0 to 6) | 1.5 (0 to 6) |
| Koordinator, cgroup root | 1.9 (0 to 7) | 1.1 (0 to 4) |
| KAI, four ways | 9.3 (1 to 26) | 4.0 (0 to 11) |
| Kueue, four ways | 9.8 (2 to 23) | 4.5 (1 to 13) |
| Volcano, four ways | 8.7 (1 to 21) | not run |
| bin-packing, four ways | 10.9 (2 to 26) | 4.0 (0 to 13) |
| KubeRay, four ways | 6.6 (0 to 25) | 2.9 (0 to 9) |
| Crane, four ways | 1.6 (0 to 5) | 1.6 (0 to 6) |
| Gödel, four ways | 8.9 (0 to 32) | 2.8 (0 to 6) |
| Open Cluster Management, four ways | 21.8 (8 to 41) | 7.9 (1 to 14) |

## Limit raises

| Rig | omni-v25 | omni-v26 |
|---|---:|---:|
| the batch stream alone | 1.6 (1 to 6) | 1.9 (1 to 5) |
| the default scheduler | 41.0 (1 to 129) | 62.0 (1 to 173) |
| the bin-packing profile | 20.0 (1 to 105) | 33.1 (1 to 121) |
| KAI | 27.1 (5 to 92) | 40.2 (5 to 119) |
| Kueue | 37.7 (1 to 191) | 50.8 (2 to 139) |
| Volcano | 43.1 (6 to 154) | 59.2 (6 to 172) |
| Koordinator | 53.2 (28 to 81) | 50.8 (33 to 70) |
| Koordinator, cgroup root | 49.2 (33 to 78) | 50.7 (30 to 77) |
| KAI, four ways | 32.0 (1 to 134) | 53.0 (1 to 151) |
| Kueue, four ways | 43.3 (1 to 177) | 59.1 (1 to 171) |
| Volcano, four ways | 41.3 (1 to 138) | not run |
| bin-packing, four ways | 36.3 (1 to 142) | 68.0 (1 to 163) |
| KubeRay, four ways | 26.3 (1 to 159) | 36.6 (1 to 142) |
| Crane, four ways | 0.0 (0 to 0) | 0.0 (0 to 0) |
| Gödel, four ways | 0.0 (0 to 0) | 0.0 (0 to 0) |
| Open Cluster Management, four ways | 34.1 (2 to 199) | 33.4 (2 to 156) |

## Limit hand-backs

| Rig | omni-v25 | omni-v26 |
|---|---:|---:|
| the batch stream alone | 0.4 (0 to 1) | 0.3 (0 to 1) |
| the default scheduler | 38.0 (0 to 120) | 57.5 (0 to 164) |
| the bin-packing profile | 18.8 (0 to 104) | 31.0 (0 to 119) |
| KAI | 25.7 (4 to 91) | 38.1 (4 to 118) |
| Kueue | 29.9 (0 to 110) | 45.4 (1 to 129) |
| Volcano | 38.8 (5 to 143) | 55.6 (5 to 161) |
| Koordinator | 47.0 (24 to 70) | 45.5 (29 to 69) |
| Koordinator, cgroup root | 43.8 (29 to 69) | 44.7 (25 to 68) |
| KAI, four ways | 29.6 (0 to 123) | 50.3 (0 to 140) |
| Kueue, four ways | 38.8 (0 to 159) | 46.6 (0 to 144) |
| Volcano, four ways | 39.0 (0 to 137) | not run |
| bin-packing, four ways | 30.4 (0 to 99) | 62.4 (0 to 148) |
| KubeRay, four ways | 24.6 (0 to 152) | 29.9 (0 to 134) |
| Crane, four ways | 0.0 (0 to 0) | 0.0 (0 to 0) |
| Gödel, four ways | 0.0 (0 to 0) | 0.0 (0 to 0) |
| Open Cluster Management, four ways | 27.7 (0 to 148) | 24.8 (0 to 105) |

## Pool writes

| Rig | omni-v25 | omni-v26 |
|---|---:|---:|
| the batch stream alone | 3.1 (0 to 5) | 3.2 (0 to 5) |
| the default scheduler | 3.5 (0 to 12) | 3.2 (0 to 10) |
| the bin-packing profile | 1.7 (0 to 6) | 2.7 (0 to 8) |
| KAI | 4.2 (0 to 14) | 5.0 (0 to 14) |
| Kueue | 3.7 (0 to 9) | 5.2 (0 to 14) |
| Volcano | 3.6 (0 to 12) | 4.6 (0 to 10) |
| Koordinator | 0.1 (0 to 3) | 0.6 (0 to 4) |
| Koordinator, cgroup root | 0.3 (0 to 4) | 0.4 (0 to 4) |
| KAI, four ways | 3.2 (0 to 14) | 4.5 (0 to 12) |
| Kueue, four ways | 3.0 (0 to 14) | 3.6 (0 to 10) |
| Volcano, four ways | 3.4 (0 to 12) | not run |
| bin-packing, four ways | 2.7 (0 to 10) | 4.8 (0 to 14) |
| KubeRay, four ways | 2.1 (0 to 12) | 2.0 (0 to 10) |
| Crane, four ways | 0.0 (0 to 0) | 0.0 (0 to 0) |
| Gödel, four ways | 4.1 (0 to 14) | 4.3 (0 to 14) |
| Open Cluster Management, four ways | 4.6 (0 to 22) | 5.8 (0 to 26) |

## Own processor (cores)

| Rig | omni-v25 | omni-v26 |
|---|---:|---:|
| the batch stream alone | 0.086 (0.062 to 0.103) | 0.083 (0.059 to 0.105) |
| the default scheduler | 0.077 (0.057 to 0.089) | 0.071 (0.053 to 0.087) |
| the bin-packing profile | 0.076 (0.050 to 0.085) | 0.075 (0.056 to 0.086) |
| KAI | 0.082 (0.066 to 0.095) | 0.076 (0.054 to 0.094) |
| Kueue | 0.079 (0.055 to 0.092) | 0.076 (0.059 to 0.091) |
| Volcano | 0.078 (0.054 to 0.096) | 0.074 (0.054 to 0.087) |
| Koordinator | 0.073 (0.051 to 0.085) | 0.069 (0.051 to 0.086) |
| Koordinator, cgroup root | 0.069 (0.051 to 0.087) | 0.072 (0.053 to 0.085) |
| KAI, four ways | 0.078 (0.053 to 0.094) | 0.073 (0.053 to 0.096) |
| Kueue, four ways | 0.075 (0.049 to 0.089) | 0.072 (0.051 to 0.089) |
| Volcano, four ways | 0.075 (0.054 to 0.089) | not run |
| bin-packing, four ways | 0.073 (0.048 to 0.085) | 0.069 (0.046 to 0.086) |
| KubeRay, four ways | 0.058 (0.028 to 0.085) | 0.054 (0.029 to 0.084) |
| Crane, four ways | 0.041 (0.020 to 0.060) | 0.040 (0.020 to 0.060) |
| Gödel, four ways | 0.065 (0.039 to 0.080) | 0.063 (0.043 to 0.081) |
| Open Cluster Management, four ways | 0.057 (0.038 to 0.069) | 0.055 (0.040 to 0.067) |

The runs each rig was read from are its tables' own (`results/live/V<n>_<TABLE>.md`). Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
