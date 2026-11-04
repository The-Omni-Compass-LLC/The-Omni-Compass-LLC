# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-semiurb--2-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(285, 0.985, 0.986, 1.025), (4847, 0.97, 0.9787, 1.025), (4943, 0.985, 0.9596, 1.025), (5444, 0.97, 0.9781, 1.025), (5659, 0.985, 0.9597, 1.025), (7905, 1.0, 0.9764, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.9e+01 MW.

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

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(285, 0.985, 0.9859, 1.025), (4847, 0.97, 0.9786, 1.025), (4943, 0.985, 0.9592, 1.025), (5469, 0.97, 0.9797, 1.025), (5566, 0.985, 0.9596, 1.025), (7905, 1.0, 0.9761, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.9e+01 MW.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
