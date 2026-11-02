# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-rural--1-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9929, 1.025), (7905, 1.0, 0.9768, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 3.6e+00 MW.

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

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9928, 1.025), (7905, 1.0, 0.9764, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 3.6e+00 MW.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
