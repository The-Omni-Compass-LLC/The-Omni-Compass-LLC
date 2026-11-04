# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-urban--0-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9925, 1.025), (7905, 1.0, 0.9754, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.2e-08 MW.

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

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9924, 1.025), (7905, 1.0, 0.9752, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 4.9e-09 MW.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
