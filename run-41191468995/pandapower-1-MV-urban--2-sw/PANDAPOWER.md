# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-urban--2-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(170, 0.985, 0.9905, 1.025), (7905, 1.0, 0.9756, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.4e+01 MW.

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

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(170, 0.985, 0.9905, 1.025), (7905, 1.0, 0.9754, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.4e+01 MW.

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
