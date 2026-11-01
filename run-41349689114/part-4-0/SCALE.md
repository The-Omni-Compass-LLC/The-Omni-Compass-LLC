# Seven organisms, 10 runs, 10x size, work waiting in line (25% of the run's own work at the start)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Commit `34cd628a8a4b`, seeds 7000-7009, 10 copies of each organism on one clock, 160 s on 4 workers. Native: each organism's own controllers. Omni: the v5 muscle law (`realms/compass_arm_v5.py`), engine omni-v23, catalog `realms/catalog_v5.csv`, the four stacked as each realm's own body on one clock (the native identical to each realm's). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 4 | Distribution / Specialized | 4840 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.068 (-0.071 to -0.065) | +0.015% (+0.014 to +0.015) | -0.015% (-0.015 to -0.014) | True |

## The stack cut down: the same 10-copy runs read at their first 1, 10 and 100 copies

The stack of copies is one organism; the first m copies of it are read from the same run, plant for plant, so a rung holds those copies and no others (the founder's order of 25 October).

| # | Organism | Copies | Work | Misses (pp) | Power given | Work per energy |
|---|---|---|---:|---:|---:|---:|
| 4 | Distribution / Specialized | the first 1 of 10 | +0.000% (+0.000 to +0.000) | -0.173 (-0.195 to -0.150) | +0.007% (+0.006 to +0.008) | -0.007% (-0.008 to -0.006) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
