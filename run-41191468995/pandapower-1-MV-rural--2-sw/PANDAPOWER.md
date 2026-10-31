# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-rural--2-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(2, 0.985, 0.9913, 1.0489), (115, 1.0, 0.9581, 1.025), (116, 0.985, 0.9809, 1.0413), (667, 1.0, 0.9596, 1.025), (835, 0.985, 0.9794, 1.025), (4956, 0.97, 0.9913, 1.0441), (4962, 0.985, 0.9588, 1.025), (7905, 1.0, 0.9778, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 7.9e+00 MW.

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

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(2, 0.985, 0.9912, 1.049), (44, 1.0, 0.9593, 1.025), (118, 0.985, 0.9838, 1.0439), (493, 1.0, 0.959, 1.025), (580, 0.985, 0.9941, 1.0442), (739, 1.0, 0.9597, 1.025), (932, 0.985, 0.9816, 1.025), (1219, 1.0, 0.9596, 1.025), (1295, 0.985, 0.9886, 1.0413), (4956, 0.97, 0.9914, 1.0451), (4962, 0.985, 0.9582, 1.025), (7905, 1.0, 0.9775, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 7.9e+00 MW.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
