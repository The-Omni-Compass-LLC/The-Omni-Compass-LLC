# Six organisms at 1000x size, work waiting in line (25% of the run's own work at the start), up to 10 runs (pooled from 10 shards)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Engine omni-v6, commit(s) 22f892673de6. Native: each organism's own controllers. Omni: the v5 muscle law (`realms/compass_arm_v5.py`); engine identity recorded above. Each block is the first N runs (seeds 7000 on), so 1, 10, 100 and 1,000 are nested; a block short of a run says so (Runs column: finished of the block). Band first: no win unless the time over the service line is no higher than native's.

## 1 run

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 2 | Physics / Robotics / Autonomous | 404000 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.106 | +0.051% | -0.051% | True |

## 10 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 2 | Physics / Robotics / Autonomous | 404000 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.106 (-0.106 to -0.105) | +0.051% (+0.051 to +0.051) | -0.051% (-0.051 to -0.051) | True |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
