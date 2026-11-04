# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-comm--2-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9913, 1.025), (7905, 1.0, 0.9722, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.2e+01 MW.

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

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9912, 1.025), (7905, 1.0, 0.9718, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.2e+01 MW.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
