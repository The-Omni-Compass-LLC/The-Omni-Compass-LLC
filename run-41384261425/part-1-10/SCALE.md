# Seven organisms, 90 runs, 10x size, work waiting in line (25% of the run's own work at the start)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Commit `cfd01fbb4ae5`, seeds 7010-7099, 10 copies of each organism on one clock, 1887 s on 4 workers. Native: each organism's own controllers. Omni: the v5 muscle law (`realms/compass_arm_v5.py`), engine omni-v23, catalog `realms/catalog_v5.csv`, the four stacked as each realm's own body on one clock (the native identical to each realm's). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 5400 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.142 (-0.143 to -0.141) | +0.062% (+0.062 to +0.062) | -0.062% (-0.062 to -0.062) | True |

## The stack cut down: the same 10-copy runs read at their first 1, 10 and 100 copies

The stack of copies is one organism; the first m copies of it are read from the same run, plant for plant, so a rung holds those copies and no others (the founder's order of 25 October).

| # | Organism | Copies | Work | Misses (pp) | Power given | Work per energy |
|---|---|---|---:|---:|---:|---:|
| 1 | Compute / AI / Cloud | the first 1 of 10 | +0.000% (+0.000 to +0.000) | -0.205 (-0.210 to -0.201) | +0.046% (+0.045 to +0.047) | -0.046% (-0.047 to -0.045) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
