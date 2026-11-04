# Seven organisms, 28 runs, 500x size, work waiting in line (25% of the run's own work at the start)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Commit `2d72c397ceef`, seeds 7066-7093, 500 copies of each organism on one clock, 17464 s on 4 workers. Native: each organism's own controllers. Omni: the v5 muscle law (`realms/compass_arm_v5.py`), engine omni-v24, catalog `realms/catalog_v5.csv`, the four stacked as each realm's own body on one clock (the native identical to each realm's). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 7 | The spine, the muscles every stack runs on | 133500 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.274 (-0.274 to -0.274) | +0.073% (+0.073 to +0.073) | -0.073% (-0.073 to -0.073) | True |

## The stack cut down: the same 500-copy runs read at their first 1, 10 and 100 copies

The stack of copies is one organism; the first m copies of it are read from the same run, plant for plant, so a rung holds those copies and no others (the founder's order of 25 October).

| # | Organism | Copies | Work | Misses (pp) | Power given | Work per energy |
|---|---|---|---:|---:|---:|---:|
| 7 | The spine, the muscles every stack runs on | the first 1 of 500 | +0.000% (+0.000 to +0.000) | -0.362 (-0.380 to -0.344) | +0.039% (+0.036 to +0.041) | -0.039% (-0.041 to -0.036) |
| 7 | The spine, the muscles every stack runs on | the first 10 of 500 | +0.000% (+0.000 to +0.000) | -0.283 (-0.285 to -0.280) | +0.069% (+0.068 to +0.069) | -0.069% (-0.069 to -0.068) |
| 7 | The spine, the muscles every stack runs on | the first 100 of 500 | +0.000% (+0.000 to +0.000) | -0.275 (-0.275 to -0.274) | +0.073% (+0.073 to +0.073) | -0.073% (-0.073 to -0.073) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
