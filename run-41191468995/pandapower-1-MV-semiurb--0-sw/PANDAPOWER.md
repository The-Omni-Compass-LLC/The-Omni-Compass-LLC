# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-semiurb--0-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9937, 1.025), (7905, 1.0, 0.9745, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.6e-08 MW.

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

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9937, 1.025), (7905, 1.0, 0.9742, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 4.9e-09 MW.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
