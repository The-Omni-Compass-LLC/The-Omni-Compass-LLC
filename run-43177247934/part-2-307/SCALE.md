# Seven organisms, 9 runs, 500x size, work waiting in line (25% of the run's own work at the start)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Commit `2438623f09a9`, seeds 7307-7315, 500 copies of each organism on one clock, 13512 s on 3 workers. Native: each organism's own controllers. Omni: the v5 muscle law (`realms/compass_arm_v5.py`), engine omni-v26, catalog `realms/catalog_v5.csv`, the four stacked as each realm's own body on one clock (the native identical to each realm's). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 2 | Physics / Robotics / Autonomous | 202000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.106 (-0.106 to -0.106) | +0.051% (+0.051 to +0.051) | -0.051% (-0.051 to -0.051) | True |

## The stack cut down: the same 500-copy runs read at their first 1, 10 and 100 copies

The stack of copies is one organism; the first m copies of it are read from the same run, plant for plant, so a rung holds those copies and no others (the founder's order of 25 October).

| # | Organism | Copies | Work | Misses (pp) | Power given | Work per energy |
|---|---|---|---:|---:|---:|---:|
| 2 | Physics / Robotics / Autonomous | the first 1 of 500 | +0.000% (+0.000 to +0.000) | -0.199 (-0.229 to -0.169) | +0.023% (+0.019 to +0.027) | -0.023% (-0.027 to -0.019) |
| 2 | Physics / Robotics / Autonomous | the first 10 of 500 | +0.000% (+0.000 to +0.000) | -0.115 (-0.119 to -0.110) | +0.048% (+0.047 to +0.048) | -0.048% (-0.048 to -0.047) |
| 2 | Physics / Robotics / Autonomous | the first 100 of 500 | +0.000% (+0.000 to +0.000) | -0.107 (-0.108 to -0.107) | +0.051% (+0.051 to +0.051) | -0.051% (-0.051 to -0.051) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
