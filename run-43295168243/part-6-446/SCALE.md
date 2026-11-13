# Seven organisms, 1 runs, 500x size, work waiting in line (25% of the run's own work at the start)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Commit `2e6aef998148`, seeds 7446-7446, 500 copies of each organism on one clock, 7709 s on 1 workers. Native: each organism's own controllers. Omni: the v5 muscle law (`realms/compass_arm_v5.py`), engine omni-v26, catalog `realms/catalog_v5.csv`, the four stacked as each realm's own body on one clock (the native identical to each realm's). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 6 | The whole tower, every muscle once | 553500 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.036 (-0.036 to -0.036) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

## The stack cut down: the same 500-copy runs read at their first 1, 10 and 100 copies

The stack of copies is one organism; the first m copies of it are read from the same run, plant for plant, so a rung holds those copies and no others (the founder's order of 25 October).

| # | Organism | Copies | Work | Misses (pp) | Power given | Work per energy |
|---|---|---|---:|---:|---:|---:|
| 6 | The whole tower, every muscle once | the first 1 of 500 | +0.000% (+0.000 to +0.000) | -0.040 (-0.040 to -0.040) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) |
| 6 | The whole tower, every muscle once | the first 10 of 500 | +0.000% (+0.000 to +0.000) | -0.035 (-0.035 to -0.035) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) |
| 6 | The whole tower, every muscle once | the first 100 of 500 | +0.000% (+0.000 to +0.000) | -0.035 (-0.035 to -0.035) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
