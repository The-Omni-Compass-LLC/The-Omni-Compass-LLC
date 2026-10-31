# Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

pandapower (Fraunhofer IEE, University of Kassel) solves every AC power flow; SimBench gives the grids and their year of measured-shape profiles. Native: the substation's tap changer holding its busbar at 1.00 per unit. Omni: the compass law on top of that setpoint, inside [0.97, 1.03], reading the worst voltage margin in the grid. Evidence class: an independent recognized simulator and data set (not our model).

## 1-MV-semiurb--1-sw, loads ZIP (40% Z, 30% I, 30% P)

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9938, 1.025), (4864, 0.97, 0.9768, 1.025), (5030, 0.985, 0.9591, 1.025), (5224, 0.97, 0.9798, 1.025), (5227, 0.985, 0.9598, 1.025), (5444, 0.97, 0.9788, 1.025), (5483, 0.985, 0.9592, 1.025), (7905, 1.0, 0.9757, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.1e+01 MW.

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

8784 steps of 1 h. Omni handed the setpoint back: yes. Setpoint changes Omni made (hour, new setpoint, lowest and highest bus): [(168, 0.985, 0.9938, 1.025), (4865, 0.97, 0.9789, 1.025), (5030, 0.985, 0.9584, 1.025), (5224, 0.97, 0.9797, 1.025), (5227, 0.985, 0.9593, 1.025), (5471, 0.97, 0.9805, 1.025), (5480, 0.985, 0.96, 1.025), (7905, 1.0, 0.9754, 1.025)]; each change is one tap on each of the 2 substation transformers, the hand-back at 90% of the year included. Worst power balance of any solved step: 1.1e+01 MW.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
