# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-comm--0-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9936, 1.025], [7905, 1.0, 0.9711, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.2e-08 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 57370.9 | 56519.3 | -1.48% | lower (toward its aim) |
| line and transformer losses (MWh) | 540.785 | 535.585 | -0.96% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 29232.3 | 28375.4 | -2.93% | lower (toward its aim) |
| solar and wind fed in (MWh) | 28679.4 | 28679.4 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 1728 | 1148 | -33.56% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.977252 | 0.962942 | -1.46% | shown |
| highest voltage seen (per unit) | 1.04699 | 1.04699 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-comm--0-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9936, 1.025], [7905, 1.0, 0.9707, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 5.4e-09 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 57626 | 57626 | +0.00% | same |
| line and transformer losses (MWh) | 542.501 | 539.624 | -0.53% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 29489 | 29486.1 | -0.01% | lower (toward its aim) |
| solar and wind fed in (MWh) | 28679.4 | 28679.4 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 1824 | 1260 | -30.92% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.976803 | 0.962128 | -1.50% | shown |
| highest voltage seen (per unit) | 1.04731 | 1.04731 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-comm--1-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9931, 1.025], [7905, 1.0, 0.9717, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.7e+00 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 58647.5 | 57797.1 | -1.45% | lower (toward its aim) |
| line and transformer losses (MWh) | 570.667 | 565.903 | -0.83% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 5872.8 | 5017.57 | -14.56% | lower (toward its aim) |
| solar and wind fed in (MWh) | 51394.1 | 51394.1 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 1528 | 980 | -35.86% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.977328 | 0.963038 | -1.46% | shown |
| highest voltage seen (per unit) | 1.03228 | 1.03228 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-comm--1-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9931, 1.025], [7905, 1.0, 0.9713, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.7e+00 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 58971.1 | 58971.1 | +0.00% | same |
| line and transformer losses (MWh) | 571.93 | 569.625 | -0.40% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 6197.68 | 6195.38 | -0.04% | lower (toward its aim) |
| solar and wind fed in (MWh) | 51394.1 | 51394.1 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 1660 | 1148 | -30.84% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.976861 | 0.962193 | -1.50% | shown |
| highest voltage seen (per unit) | 1.03235 | 1.03235 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-comm--2-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9913, 1.025], [7905, 1.0, 0.9722, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.2e+01 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 60741.3 | 59871.8 | -1.43% | lower (toward its aim) |
| line and transformer losses (MWh) | 660.947 | 659.064 | -0.28% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -13656.4 | -14527.8 | -6.38% | lower (toward its aim) |
| solar and wind fed in (MWh) | 60049.3 | 60049.3 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 1904 | 1220 | -35.92% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.974539 | 0.960194 | -1.47% | shown |
| highest voltage seen (per unit) | 1.03429 | 1.03429 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-comm--2-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9912, 1.025], [7905, 1.0, 0.9718, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.2e+01 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 61057.9 | 61057.9 | +0.00% | same |
| line and transformer losses (MWh) | 662.17 | 662.035 | -0.02% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -13338.6 | -13338.7 | -0.00% | lower (toward its aim) |
| solar and wind fed in (MWh) | 60049.3 | 60049.3 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 2036 | 1396 | -31.43% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.973767 | 0.959044 | -1.51% | shown |
| highest voltage seen (per unit) | 1.03437 | 1.03437 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-rural--1-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9929, 1.025], [7905, 1.0, 0.9768, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 3.6e+00 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 32149.6 | 31715.4 | -1.35% | lower (toward its aim) |
| line and transformer losses (MWh) | 730.391 | 735.928 | +0.76% | higher (away from its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -29467.5 | -29896.2 | -1.45% | lower (toward its aim) |
| solar and wind fed in (MWh) | 58452.2 | 58452.2 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 2.29987e-06 | 2.29987e-06 | +0.00% | same |
| tap operations (wear) | 4 | 8 | +100.00% | higher (away from its aim) |
| lowest voltage seen (per unit) | 0.976847 | 0.962517 | -1.47% | shown |
| highest voltage seen (per unit) | 1.06134 | 1.06134 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-rural--1-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9928, 1.025], [7905, 1.0, 0.9764, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 3.6e+00 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 32203 | 32203 | +0.00% | same |
| line and transformer losses (MWh) | 732.976 | 737.1 | +0.56% | higher (away from its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -29411.5 | -29407.4 | +0.01% | higher (away from its aim) |
| solar and wind fed in (MWh) | 58452.2 | 58452.2 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 2.29987e-06 | 2.29987e-06 | +0.00% | same |
| tap operations (wear) | 4 | 8 | +100.00% | higher (away from its aim) |
| lowest voltage seen (per unit) | 0.976326 | 0.961594 | -1.51% | shown |
| highest voltage seen (per unit) | 1.06149 | 1.06149 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-rural--2-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[2, 0.985, 0.9913, 1.0489], [115, 1.0, 0.9581, 1.025], [116, 0.985, 0.9809, 1.0413], [667, 1.0, 0.9596, 1.025], [835, 0.985, 0.9794, 1.025], [4956, 0.97, 0.9913, 1.0441], [4962, 0.985, 0.9588, 1.025], [7905, 1.0, 0.9778, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 7.9e+00 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 34802.2 | 34334.6 | -1.34% | lower (toward its aim) |
| line and transformer losses (MWh) | 1144.49 | 1161.16 | +1.46% | higher (away from its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -41253.3 | -41704.3 | -1.09% | lower (toward its aim) |
| solar and wind fed in (MWh) | 68531 | 68531 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0.000154091 | 1.37992e-05 | -91.04% | lower (toward its aim) |
| tap operations (wear) | 88 | 64 | -27.27% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.970881 | 0.956573 | -1.47% | shown |
| highest voltage seen (per unit) | 1.07824 | 1.07824 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986783 | -1.32% | shown |

## 1-MV-rural--2-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[2, 0.985, 0.9912, 1.049], [44, 1.0, 0.9593, 1.025], [118, 0.985, 0.9838, 1.0439], [493, 1.0, 0.959, 1.025], [580, 0.985, 0.9941, 1.0442], [739, 1.0, 0.9597, 1.025], [932, 0.985, 0.9816, 1.025], [1219, 1.0, 0.9596, 1.025], [1295, 0.985, 0.9886, 1.0413], [4956, 0.97, 0.9914, 1.0451], [4962, 0.985, 0.9582, 1.025], [7905, 1.0, 0.9775, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 7.9e+00 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 34832.6 | 34832.6 | +0.00% | same |
| line and transformer losses (MWh) | 1149.51 | 1163.13 | +1.18% | higher (away from its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -41217.9 | -41204.3 | +0.03% | higher (away from its aim) |
| solar and wind fed in (MWh) | 68531 | 68531 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0.000162141 | 1.83989e-05 | -88.65% | lower (toward its aim) |
| tap operations (wear) | 100 | 84 | -16.00% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.970039 | 0.955204 | -1.53% | shown |
| highest voltage seen (per unit) | 1.0784 | 1.0784 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.987228 | -1.28% | shown |

## 1-MV-semiurb--0-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9937, 1.025], [7905, 1.0, 0.9745, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.6e-08 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 45516.4 | 44894.6 | -1.37% | lower (toward its aim) |
| line and transformer losses (MWh) | 475.038 | 470.149 | -1.03% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 9007 | 8380.35 | -6.96% | lower (toward its aim) |
| solar and wind fed in (MWh) | 36984.4 | 36984.4 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 756 | 472 | -37.57% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.977146 | 0.962924 | -1.46% | shown |
| highest voltage seen (per unit) | 1.04896 | 1.04896 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-semiurb--0-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9937, 1.025], [7905, 1.0, 0.9742, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 4.9e-09 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 45772.9 | 45772.9 | +0.00% | same |
| line and transformer losses (MWh) | 476.101 | 471.813 | -0.90% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 9264.58 | 9260.29 | -0.05% | lower (toward its aim) |
| solar and wind fed in (MWh) | 36984.4 | 36984.4 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 808 | 572 | -29.21% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.976599 | 0.961951 | -1.50% | shown |
| highest voltage seen (per unit) | 1.04931 | 1.04931 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-semiurb--1-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9938, 1.025], [4864, 0.97, 0.9768, 1.025], [5030, 0.985, 0.9591, 1.025], [5224, 0.97, 0.9798, 1.025], [5227, 0.985, 0.9598, 1.025], [5444, 0.97, 0.9788, 1.025], [5483, 0.985, 0.9592, 1.025], [7905, 1.0, 0.9757, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.1e+01 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 48206.3 | 47534.8 | -1.39% | lower (toward its aim) |
| line and transformer losses (MWh) | 844.449 | 850.149 | +0.67% | higher (away from its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -60339.2 | -61005 | -1.10% | lower (toward its aim) |
| solar and wind fed in (MWh) | 96533.1 | 96533.1 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 840 | 556 | -33.81% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.973493 | 0.955903 | -1.81% | shown |
| highest voltage seen (per unit) | 1.04893 | 1.04893 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986433 | -1.36% | shown |

## 1-MV-semiurb--1-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9938, 1.025], [4865, 0.97, 0.9789, 1.025], [5030, 0.985, 0.9584, 1.025], [5224, 0.97, 0.9797, 1.025], [5227, 0.985, 0.9593, 1.025], [5471, 0.97, 0.9805, 1.025], [5480, 0.985, 0.96, 1.025], [7905, 1.0, 0.9754, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.1e+01 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 48428.5 | 48428.5 | +0.00% | same |
| line and transformer losses (MWh) | 845.799 | 850.703 | +0.58% | higher (away from its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -60115.6 | -60110.7 | +0.01% | higher (away from its aim) |
| solar and wind fed in (MWh) | 96533.1 | 96533.1 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 888 | 612 | -31.08% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.972884 | 0.958163 | -1.51% | shown |
| highest voltage seen (per unit) | 1.04927 | 1.04927 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986486 | -1.35% | shown |

## 1-MV-semiurb--2-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[285, 0.985, 0.986, 1.025], [4847, 0.97, 0.9787, 1.025], [4943, 0.985, 0.9596, 1.025], [5444, 0.97, 0.9781, 1.025], [5659, 0.985, 0.9597, 1.025], [7905, 1.0, 0.9764, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.9e+01 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 51088.4 | 50375.8 | -1.39% | lower (toward its aim) |
| line and transformer losses (MWh) | 1021.01 | 1031.77 | +1.05% | higher (away from its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -80890.7 | -81592.5 | -0.87% | lower (toward its aim) |
| solar and wind fed in (MWh) | 111101 | 111101 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 1.39971e-05 | 0 | -100.00% | lower (toward its aim) |
| tap operations (wear) | 1988 | 1516 | -23.74% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.96703 | 0.952779 | -1.47% | shown |
| highest voltage seen (per unit) | 1.0519 | 1.04865 | -0.31% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986457 | -1.35% | shown |

## 1-MV-semiurb--2-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[285, 0.985, 0.9859, 1.025], [4847, 0.97, 0.9786, 1.025], [4943, 0.985, 0.9592, 1.025], [5469, 0.97, 0.9797, 1.025], [5566, 0.985, 0.9596, 1.025], [7905, 1.0, 0.9761, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.9e+01 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 51258.3 | 51258.3 | +0.00% | same |
| line and transformer losses (MWh) | 1022.96 | 1032.02 | +0.89% | higher (away from its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | -80718.9 | -80709.8 | +0.01% | higher (away from its aim) |
| solar and wind fed in (MWh) | 111101 | 111101 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 1.67966e-05 | 0 | -100.00% | lower (toward its aim) |
| tap operations (wear) | 2048 | 1616 | -21.09% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.966008 | 0.951174 | -1.54% | shown |
| highest voltage seen (per unit) | 1.05224 | 1.04899 | -0.31% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986658 | -1.33% | shown |

## 1-MV-urban--0-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9925, 1.025], [7905, 1.0, 0.9754, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.2e-08 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 70148.4 | 69068.5 | -1.54% | lower (toward its aim) |
| line and transformer losses (MWh) | 459.381 | 448.436 | -2.38% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 55440.5 | 54349.6 | -1.97% | lower (toward its aim) |
| solar and wind fed in (MWh) | 15167.3 | 15167.3 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 2686 | 1858 | -30.83% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.981024 | 0.964087 | -1.73% | shown |
| highest voltage seen (per unit) | 1.0415 | 1.0415 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-urban--0-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9924, 1.025], [7905, 1.0, 0.9752, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 4.9e-09 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 70273.1 | 70273.1 | +0.00% | same |
| line and transformer losses (MWh) | 459.605 | 450.906 | -1.89% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 55565.5 | 55556.8 | -0.02% | lower (toward its aim) |
| solar and wind fed in (MWh) | 15167.3 | 15167.3 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 2820 | 1986 | -29.57% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.980736 | 0.963393 | -1.77% | shown |
| highest voltage seen (per unit) | 1.04168 | 1.04168 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-urban--1-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9913, 1.025], [7905, 1.0, 0.9754, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 3.5e+00 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 72838.2 | 71718.7 | -1.54% | lower (toward its aim) |
| line and transformer losses (MWh) | 458.004 | 447.035 | -2.39% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 50818.6 | 49688.1 | -2.22% | lower (toward its aim) |
| solar and wind fed in (MWh) | 18582.7 | 18582.7 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 2986 | 2104 | -29.54% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.980876 | 0.963989 | -1.72% | shown |
| highest voltage seen (per unit) | 1.04148 | 1.04148 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-urban--1-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[168, 0.985, 0.9912, 1.025], [7905, 1.0, 0.9753, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 3.5e+00 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 72913.2 | 72913.2 | +0.00% | same |
| line and transformer losses (MWh) | 458.137 | 449.258 | -1.94% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 50893.7 | 50884.8 | -0.02% | lower (toward its aim) |
| solar and wind fed in (MWh) | 18582.7 | 18582.7 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 3114 | 2284 | -26.65% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.980582 | 0.963289 | -1.76% | shown |
| highest voltage seen (per unit) | 1.04167 | 1.04167 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986788 | -1.32% | shown |

## 1-MV-urban--2-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[170, 0.985, 0.9905, 1.025], [7905, 1.0, 0.9756, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.4e+01 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 76578.7 | 75422.3 | -1.51% | lower (toward its aim) |
| line and transformer losses (MWh) | 468.266 | 458.154 | -2.16% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 37570.7 | 36404.3 | -3.10% | lower (toward its aim) |
| solar and wind fed in (MWh) | 24060.2 | 24060.2 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 3821 | 2943 | -22.98% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.978398 | 0.963313 | -1.54% | shown |
| highest voltage seen (per unit) | 1.04151 | 1.04151 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986791 | -1.32% | shown |

## 1-MV-urban--2-sw, loads constant power (SimBench as shipped)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [[170, 0.985, 0.9905, 1.025], [7905, 1.0, 0.9754, 1.025]]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.4e+01 MW.

| | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy the loads drew (MWh) | 76637.8 | 76637.8 | +0.00% | same |
| line and transformer losses (MWh) | 468.546 | 460.006 | -1.82% | lower (toward its aim) |
| net import from the upstream grid (MWh; negative: the grid exports) | 37630.2 | 37621.6 | -0.02% | lower (toward its aim) |
| solar and wind fed in (MWh) | 24060.2 | 24060.2 | +0.00% | shown |
| bus-steps outside 0.95-1.05 per unit (share) | 0 | 0 | +0 | same |
| tap operations (wear) | 3943 | 3091 | -21.61% | lower (toward its aim) |
| lowest voltage seen (per unit) | 0.978015 | 0.962549 | -1.58% | shown |
| highest voltage seen (per unit) | 1.04169 | 1.04169 | +0.00% | shown |
| busbar setpoint, mean over the year (per unit) | 1 | 0.986791 | -1.32% | shown |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
