# Six organisms at 10x size, work waiting in line (25% of the run's own work at the start), up to 1000 runs (pooled from 60 shards)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (models). Engine not recorded, commit(s) e29133537123. Native: each organism's own controllers. Omni: the v5 law on every muscle (`realms/compass_arm_v5.py`, engine omni-v5). Each block is the first N runs (seeds 7000 on), so 1, 10, 100 and 1,000 are nested; a block short of a run says so (Runs column: finished of the block). Band first: no win unless the time over the service line is no higher than native's.

## 1 run

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 5300 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.052 | +0.064% | -0.064% | True |
| 2 | Physics / Robotics / Autonomous | 3940 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.052 | +0.051% | -0.051% | True |
| 3 | Energy / Facility / Industrial | 4700 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.007 | +0.000% | -0.000% | True |
| 4 | Distribution / Specialized | 4740 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.052 | +0.015% | -0.015% | True |
| 5 | The four stacked, duplicates kept | 18680 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.041 | +0.000% | -0.000% | True |
| 6 | The whole tower, every muscle once | 10970 | 1 | **ONE RUN (no label)** | held | +0.000% | -0.003 | +0.000% | -0.000% | True |

## 10 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 5300 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.053 (-0.053 to -0.052) | +0.064% (+0.064 to +0.064) | -0.064% (-0.064 to -0.064) | True |
| 2 | Physics / Robotics / Autonomous | 3940 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.053 (-0.055 to -0.052) | +0.051% (+0.051 to +0.051) | -0.051% (-0.051 to -0.051) | True |
| 3 | Energy / Facility / Industrial | 4700 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.007 (-0.009 to -0.006) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 4740 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.051 (-0.052 to -0.050) | +0.015% (+0.015 to +0.016) | -0.015% (-0.016 to -0.015) | True |
| 5 | The four stacked, duplicates kept | 18680 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.041 (-0.042 to -0.040) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 10970 | 10 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.003 (-0.004 to -0.003) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

## 100 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 5300 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.052 (-0.053 to -0.052) | +0.064% (+0.064 to +0.064) | -0.064% (-0.064 to -0.064) | True |
| 2 | Physics / Robotics / Autonomous | 3940 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.055 (-0.056 to -0.054) | +0.051% (+0.051 to +0.051) | -0.051% (-0.051 to -0.051) | True |
| 3 | Energy / Facility / Industrial | 4700 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.008 (-0.008 to -0.008) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 4740 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.051 (-0.051 to -0.051) | +0.015% (+0.015 to +0.015) | -0.015% (-0.015 to -0.015) | True |
| 5 | The four stacked, duplicates kept | 18680 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.041 (-0.042 to -0.041) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 10970 | 100 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.003 (-0.004 to -0.003) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

## 1000 runs

| # | Organism | Muscles | Runs | Label | Band first | Work | Misses (pp) | Power given | Work per energy | Knobs handed back |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 5300 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.052 (-0.053 to -0.052) | +0.064% (+0.064 to +0.064) | -0.064% (-0.064 to -0.064) | True |
| 2 | Physics / Robotics / Autonomous | 3940 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.055 (-0.055 to -0.055) | +0.051% (+0.051 to +0.051) | -0.051% (-0.051 to -0.051) | True |
| 3 | Energy / Facility / Industrial | 4700 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.008 (-0.008 to -0.008) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 4 | Distribution / Specialized | 4740 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.051 (-0.051 to -0.051) | +0.015% (+0.015 to +0.015) | -0.015% (-0.015 to -0.015) | True |
| 5 | The four stacked, duplicates kept | 18680 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.041 (-0.041 to -0.041) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |
| 6 | The whole tower, every muscle once | 10970 | 1000 | **FEWER MISSES** | held | +0.000% (+0.000 to +0.000) | -0.003 (-0.004 to -0.003) | +0.000% (+0.000 to +0.000) | -0.000% (-0.000 to -0.000) | True |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
