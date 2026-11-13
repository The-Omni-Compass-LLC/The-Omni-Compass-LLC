# Seven organisms, 90 runs, 10x size, work waiting in line (25% of the run's own work at the start)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Commit `b55ebc064166`, seeds 7010-7099, 10 copies of each organism on one clock, 733 s on 4 workers. Native: each organism's own controllers. Omni: the v5 muscle law (`realms/compass_arm_v5.py`), engine omni-v6, catalog `realms/catalog_v5.csv`, the four stacked as each realm's own body on one clock (the native identical to each realm's). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 7 | The spine, the muscles every stack runs on | 2670 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.283 (-0.284 to -0.281) | +0.068% (+0.068 to +0.069) | -0.068% (-0.069 to -0.068) | True |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
