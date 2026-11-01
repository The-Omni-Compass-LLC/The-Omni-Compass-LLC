# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-urban--1-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9913, 1.025), (7905, 1.0, 0.9754, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 3.5e+00 MW.

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

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9912, 1.025), (7905, 1.0, 0.9753, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 3.5e+00 MW.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
