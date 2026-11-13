# The realms on Omni v5 at the max: 1107 muscles and six organisms, native against Omni on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (modelled). Run 2026-10-12 23:07 UTC, commit `a39fbbd1bdb4`, seeds 3000-3009 (10 paired seeds per muscle, per organism and per load), catalog `realms/catalog_v5.csv`. The engine is **omni-v5** (`tools/omni_version.py`, `OMNI_V5.json`) at its default, **the max** (`realms/compass_arm_v5.py`, `V5CFG`), on top of each plant's own native controller. Harness `realms/`.

**The max.** Every muscle is pushed toward its own limit for the most work, faster: a pool's machines are started before the rush lands (the recent peak arrivals widened by the largest rise the pool has shown within one machine start, at 95% utilisation), never fewer than its twin runs (the brain's model of native: the same pool under its own autoscaler alone, on the same arrivals); a room is cooled ahead of the heat as it nears its limit or its cooling nears flat out; a battery's line is clipped from its charge, a UPS lending only the charge above its outage floor. Work waiting in line is cleared within one machine start, and the machines it no longer needs go back at once (never below the twin). A muscle native already runs flat out (full clock, full speed, full actuator, nothing turned away) is wired, watched and native: there is nothing above native to give it. Nothing is taken from one muscle to give to another; the max never shaves. The energy the max takes is reported as **power given**, beside the work and the speed it bought.

**The line.** Under the line load, every plant starts with work already waiting, a 25% share of the work its own run brings: a pool's jobs submitted before the start (its machines take them from what the requests leave them), an axis's tasks queued, a site's flexible load held over. A room's heat and a loop's demand cannot wait, so they have none. Both arms start with the same line; the one that clears it sooner is **faster**.

**The bone.** Inside an organism the max may give only the power the body can carry: a site's grid line and a room's cooling are loaded by the whole body (the machines' power is heat in every room, the body's power swing is load on every site's line), so machines and cooling are granted out of the room the most loaded line has left, read one decision ahead (its latest reading plus the larger of 3.09 of its own step-to-step wobbles and the largest single climb it has shown, the wobbles counted on the line without the max's own machines: its own steps are not the line's). A site with flexible load waiting gives its catch-up the room first. With no room, what the max added goes back, as much as the shortfall needs (the pools holding the most extra machines first, the machines started last first), never below a pool's twin: nothing native has is taken. The organisms run the hour around each battery site's daily peak, where the UPS lines carry most of their rating: the bone is tight there, and the max gives only what it can carry.

**The lease.** At 80% of every run the brain is cut; the plug walks every setting back to native over 24 decisions (a jump the body would have to absorb at once is the swing the founder ordered gone), and the run goes on native until it ends; every knob must be back at the operator's own before then (valid). A floor that only held a pool at its twin's count adds nothing to walk back and is let go at once (a walking floor would hold machines native had already released). The security kill switch is instant (`omnicompass/master.py`).

These are models; a model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test. What a row shows is whether the max, applied to that knob, helps or hurts the model.

## The six organisms: the organism's own load

Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant decisions over their line, native → omni (the change in misses). Power given: the organism's energy against native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals over seeds.

| Organism | Muscles | Label | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Work per energy | Valid |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 540 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 1.97% → 1.90% (−3.5%) | -0.07 (-0.08 to -0.06) | +0.06% (+0.05 to +0.06) | +0.35% | -0.06% (-0.06 to -0.05) | yes |
| Physics / Robotics / Autonomous | 404 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 4.88% → 4.79% (−1.9%) | -0.09 (-0.11 to -0.08) | +0.05% (+0.05 to +0.05) | +0.53% | -0.05% (-0.05 to -0.05) | yes |
| Energy / Facility / Industrial | 480 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 1.58% → 1.48% (−6.4%) | -0.10 (-0.12 to -0.09) | +0.00% (+0.00 to +0.00) | +0.43% | -0.00% (-0.00 to -0.00) | yes |
| Distribution / Specialized | 484 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 2.36% → 2.29% (−2.9%) | -0.07 (-0.08 to -0.06) | +0.01% (+0.01 to +0.02) | +0.37% | -0.01% (-0.02 to -0.01) | yes |
| The four stacked, every shared muscle in each | 1908 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 2.59% → 2.51% (−3.2%) | -0.08 (-0.09 to -0.07) | +0.00% (+0.00 to +0.00) | +0.41% | -0.00% (-0.00 to -0.00) | yes |
| The whole tower, every muscle once | 1107 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 2.73% → 2.68% (−1.6%) | -0.04 (-0.05 to -0.04) | +0.00% (+0.00 to +0.00) | +0.19% | -0.00% (-0.00 to -0.00) | yes |

## The six organisms: the climb (1 2 3 2 3 4 ..., level 4 = own load, 8 = twice it)

Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant decisions over their line, native → omni (the change in misses). Power given: the organism's energy against native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals over seeds.

| Organism | Muscles | Label | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Work per energy | Valid |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 540 | **MORE WORK + FEWER MISSES** | +0.00% (+0.00 to +0.00) | 5.59% → 5.40% (−3.5%) | -0.19 (-0.21 to -0.18) | +0.07% (+0.07 to +0.07) | +0.46% | -0.07% (-0.07 to -0.07) | yes |
| Physics / Robotics / Autonomous | 404 | **MORE WORK + FEWER MISSES** | +0.00% (+0.00 to +0.00) | 9.82% → 9.65% (−1.8%) | -0.17 (-0.19 to -0.16) | +0.06% (+0.06 to +0.06) | +0.58% | -0.05% (-0.06 to -0.05) | yes |
| Energy / Facility / Industrial | 480 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 8.07% → 7.93% (−1.7%) | -0.14 (-0.15 to -0.13) | +0.00% (+0.00 to +0.00) | +0.47% | -0.00% (-0.00 to -0.00) | yes |
| Distribution / Specialized | 484 | **MORE WORK + FEWER MISSES** | +0.00% (+0.00 to +0.00) | 6.43% → 6.23% (−3.1%) | -0.20 (-0.22 to -0.18) | +0.03% (+0.02 to +0.03) | +0.51% | -0.03% (-0.03 to -0.02) | yes |
| The four stacked, every shared muscle in each | 1908 | **MORE WORK + FEWER MISSES** | +0.00% (+0.00 to +0.00) | 7.32% → 7.15% (−2.4%) | -0.18 (-0.19 to -0.16) | +0.00% (+0.00 to +0.00) | +0.50% | +0.00% (+0.00 to +0.00) | yes |
| The whole tower, every muscle once | 1107 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 6.91% → 6.85% (−0.9%) | -0.06 (-0.07 to -0.06) | +0.00% (+0.00 to +0.00) | +0.21% | -0.00% (-0.00 to -0.00) | yes |

## The six organisms: work waiting in line (a 25% share of the run's own work waiting when it starts)

Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant decisions over their line, native → omni (the change in misses). Power given: the organism's energy against native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals over seeds.

| Organism | Muscles | Label | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Work per energy | Valid |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 540 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 2.47% → 2.34% (−5.3%) | -0.13 (-0.14 to -0.12) | +0.07% (+0.07 to +0.07) | +0.43% | -0.07% (-0.07 to -0.07) | yes |
| Physics / Robotics / Autonomous | 404 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 10.87% → 10.76% (−1.0%) | -0.11 (-0.12 to -0.10) | +0.05% (+0.05 to +0.05) | +0.58% | -0.05% (-0.05 to -0.05) | yes |
| Energy / Facility / Industrial | 480 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 1.41% → 1.31% (−7.2%) | -0.10 (-0.12 to -0.09) | +0.00% (+0.00 to +0.00) | +0.43% | -0.00% (-0.00 to -0.00) | yes |
| Distribution / Specialized | 484 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 3.00% → 2.94% (−1.7%) | -0.05 (-0.06 to -0.05) | +0.02% (+0.02 to +0.02) | +0.48% | -0.02% (-0.02 to -0.02) | yes |
| The four stacked, every shared muscle in each | 1908 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 4.12% → 4.02% (−2.4%) | -0.10 (-0.10 to -0.09) | +0.00% (+0.00 to +0.00) | +0.47% | -0.00% (-0.00 to -0.00) | yes |
| The whole tower, every muscle once | 1107 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 4.62% → 4.58% (−1.0%) | -0.04 (-0.05 to -0.04) | +0.00% (+0.00 to +0.00) | +0.19% | -0.00% (-0.00 to -0.00) | yes |

## Inside the organisms: every plant that did worse than native

A stricter look than an organism's total: every plant inside each organism, over all seeds, that did less work than native or spent more decisions over its own line, under each load. Reported whatever it shows.

| Load | Organism | Plants | Plants worse | The plants (work change, extra decisions over the line, all seeds) |
|---|---|---:|---:|---|
| normal | Compute / AI / Cloud | 540 | 0 | none |
| normal | Physics / Robotics / Autonomous | 404 | 0 | none |
| normal | Energy / Facility / Industrial | 480 | 0 | none |
| normal | Distribution / Specialized | 484 | 0 | none |
| normal | The four stacked, every shared muscle in each | 1908 | 0 | none |
| normal | The whole tower, every muscle once | 1107 | 0 | none |
| climb | Compute / AI / Cloud | 540 | 0 | none |
| climb | Physics / Robotics / Autonomous | 404 | 0 | none |
| climb | Energy / Facility / Industrial | 480 | 0 | none |
| climb | Distribution / Specialized | 484 | 0 | none |
| climb | The four stacked, every shared muscle in each | 1908 | 0 | none |
| climb | The whole tower, every muscle once | 1107 | 0 | none |
| line | Compute / AI / Cloud | 540 | 0 | none |
| line | Physics / Robotics / Autonomous | 404 | 0 | none |
| line | Energy / Facility / Industrial | 480 | 0 | none |
| line | Distribution / Specialized | 484 | 0 | none |
| line | The four stacked, every shared muscle in each | 1908 | 0 | none |
| line | The whole tower, every muscle once | 1107 | 0 | none |

## Every muscle alone, by home realm

Each muscle runs under 2 loads, its own load (normal) and work waiting in line (25% of the run's own work at the start) (line). **Better**: at least one gain beyond the noise under some load (more work, faster: the line cleared sooner, fewer misses) and no loss under any. **At its limit on native**: native already runs the knob at the top of its range (full clock, full speed, full torque, full battery power, nothing paced or turned away), so the max has nothing above native to give it and writes nothing. **Same as native**: the max acted or could, and the result is no different beyond the noise (native already did all the work that came and was almost never over its line).

| Realm | Muscles | Better | of them: more work | faster | fewer misses | Same as native | At its limit on native | Mixed | Worse | Invalid |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | 444 | 274 | 11 | 274 | 221 | 24 | 146 | 0 | 0 | 0 |
| Physics / Robotics / Autonomous | 137 | 53 | 7 | 51 | 19 | 2 | 82 | 0 | 0 | 0 |
| Energy / Facility / Industrial | 249 | 20 | 0 | 0 | 20 | 132 | 97 | 0 | 0 | 0 |
| Distribution / Specialized | 277 | 170 | 14 | 168 | 138 | 11 | 96 | 0 | 0 | 0 |
| **All** | **1107** | **517** | **32** | **493** | **398** | **169** | **421** | **0** | **0** | **0** |

## Every muscle alone under its own load, by kind of plant and knob

Misses: the share of decisions over the line, native → omni. Line: minutes to clear the work waiting at the start, native → omni (and the share still waiting at the end, where it did not clear). Power given: energy against native's.

| Plant | Knob | Muscles | Omni acts on | Better | At its limit on native | Misses, native → omni | Work | Line, native → omni | Power given | Wear |
|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|
| compute_pool | admission | 195 | 0 | 0 | 195 | 1.68% → 1.68% | +0.000% | no line | +0.00% | +0.00% |
| compute_pool | capacity | 422 | 422 | 329 | 0 | 1.54% → 0.48% | +0.041% | no line | +21.47% | +43.62% |
| compute_pool | power | 42 | 0 | 0 | 42 | 1.61% → 1.61% | +0.000% | no line | +0.00% | +0.00% |
| compute_pool | setpoint | 36 | 36 | 30 | 0 | 1.71% → 0.58% | +0.029% | no line | +21.17% | +44.71% |
| energy_storage | admission | 10 | 0 | 0 | 10 | 14.29% → 14.29% | +0.000% | no line | +0.00% | +0.00% |
| energy_storage | capacity | 13 | 13 | 10 | 0 | 13.37% → 10.05% | +0.000% | no line | +0.21% | +41.67% |
| energy_storage | power | 23 | 23 | 0 | 0 | 14.71% → 14.55% | +0.000% | no line | +0.04% | -0.60% |
| energy_storage | setpoint | 8 | 8 | 7 | 0 | 17.11% → 15.10% | +0.000% | no line | +0.15% | +21.17% |
| motion_axis | admission | 30 | 0 | 0 | 30 | 1.49% → 1.49% | +0.000% | no line | +0.00% | +0.00% |
| motion_axis | capacity | 48 | 37 | 1 | 11 | 1.52% → 0.87% | +0.207% | no line | +0.83% | +2.09% |
| motion_axis | power | 38 | 0 | 0 | 38 | 4.70% → 4.70% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | admission | 33 | 0 | 0 | 33 | 0.03% → 0.03% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | capacity | 39 | 0 | 0 | 39 | 0.03% → 0.03% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | power | 12 | 0 | 0 | 12 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | setpoint | 111 | 0 | 0 | 0 | 0.01% → 0.01% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | admission | 7 | 0 | 0 | 7 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | capacity | 17 | 9 | 0 | 0 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.01% |
| thermal_zone | power | 4 | 0 | 0 | 4 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | setpoint | 19 | 19 | 0 | 0 | 0.00% → 0.00% | +0.000% | no line | +0.09% | -0.01% |

## Every muscle alone under work waiting in line (25% of the run's own work at the start), by kind of plant and knob

Misses: the share of decisions over the line, native → omni. Line: minutes to clear the work waiting at the start, native → omni (and the share still waiting at the end, where it did not clear). Power given: energy against native's.

| Plant | Knob | Muscles | Omni acts on | Better | At its limit on native | Misses, native → omni | Work | Line, native → omni | Power given | Wear |
|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|
| compute_pool | admission | 195 | 0 | 0 | 195 | 1.53% → 1.53% | +0.000% | 13.9 → 13.9 min | +0.00% | +0.00% |
| compute_pool | capacity | 422 | 422 | 422 | 0 | 1.40% → 0.40% | +0.029% | 16.9 → 7.8 min | +21.29% | +43.06% |
| compute_pool | power | 42 | 0 | 0 | 42 | 1.47% → 1.47% | +0.000% | 11.0 → 11.0 min | +0.00% | +0.00% |
| compute_pool | setpoint | 36 | 36 | 36 | 0 | 1.54% → 0.48% | +0.021% | 12.4 → 6.6 min | +20.61% | +42.31% |
| energy_storage | admission | 10 | 0 | 0 | 10 | 14.29% → 14.29% | +0.000% | 391.2 → 391.2 min (0% → 0% left) | +0.00% | +0.00% |
| energy_storage | capacity | 13 | 13 | 13 | 0 | 13.37% → 9.86% | +0.000% | 404.5 → 404.5 min (0% → 0% left) | +0.20% | +41.61% |
| energy_storage | power | 23 | 23 | 1 | 0 | 14.71% → 14.53% | +0.000% | 364.9 → 364.9 min (0% → 0% left) | +0.03% | -0.60% |
| energy_storage | setpoint | 8 | 8 | 8 | 0 | 17.11% → 15.00% | +0.000% | 388.2 → 388.2 min (0% → 0% left) | +0.14% | +21.17% |
| motion_axis | admission | 30 | 0 | 0 | 30 | 6.25% → 6.25% | +0.000% | 3.5 → 3.5 min | +0.00% | +0.00% |
| motion_axis | capacity | 48 | 37 | 37 | 11 | 12.06% → 8.28% | +0.688% | 2.8 → 2.6 min | +1.35% | +3.88% |
| motion_axis | power | 38 | 0 | 0 | 38 | 18.34% → 18.34% | +0.000% | 4.7 → 4.7 min | +0.00% | +0.00% |
| process_loop | admission | 33 | 0 | 0 | 33 | 0.03% → 0.03% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | capacity | 39 | 0 | 0 | 39 | 0.03% → 0.03% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | power | 12 | 0 | 0 | 12 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | setpoint | 111 | 0 | 0 | 0 | 0.01% → 0.01% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | admission | 7 | 0 | 0 | 7 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | capacity | 17 | 9 | 0 | 0 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.01% |
| thermal_zone | power | 4 | 0 | 0 | 4 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | setpoint | 19 | 19 | 0 | 0 | 0.00% → 0.00% | +0.000% | no line | +0.09% | -0.01% |

## No-harm check

- Omni acts on **567** of 1107 muscles alone. **421** are at their limit on native (the knob is already at the top of its range); the rest it could act on show nothing beyond the noise to gain.
- Muscles alone labelled **WORSE** or **MIXED** under any load: **0**.
- The lease hands every knob back to native before each run ends: 1107 of 1107 muscles under every load; 6 of 6 organisms under normal, 6 of 6 organisms under climb, 6 of 6 organisms under line.

## Largest changes (muscles alone, own load, by mean change in misses)

| Muscle | Family | Knob | Label (all loads) | Misses (pp) | Work | Power given |
|---|---|---|---|---:|---:|---:|
| controller_update_rate | Robotics Motion Control | capacity | MORE WORK + FASTER + FEWER MISSES | -8.06 (-18.78 to +2.67) | +1.02% (-0.88 to +2.92) | +0.98% (+0.59 to +1.37) |
| jerk_limit | Robotics Motion Control | capacity | MORE WORK + FASTER + FEWER MISSES | -6.64 (-13.81 to +0.53) | +0.85% (-1.00 to +2.69) | +0.88% (+0.52 to +1.25) |
| io_capacity | Database & Transactions | capacity | MORE WORK + FASTER + FEWER MISSES | -6.60 (-8.46 to -4.73) | +0.35% (+0.06 to +0.63) | +49.59% (+41.17 to +58.01) |
| vacuum_compaction_rate | Database & Transactions | capacity | MORE WORK + FASTER + FEWER MISSES | -6.07 (-8.63 to -3.51) | +0.85% (+0.08 to +1.62) | +48.12% (+37.66 to +58.57) |
| db_failover | Database & Transactions | capacity | MORE WORK + FASTER + FEWER MISSES | -5.90 (-8.80 to -3.00) | +0.44% (+0.06 to +0.82) | +41.14% (+32.86 to +49.42) |
| read_route | Database & Transactions | capacity | MORE WORK + FASTER + FEWER MISSES | -5.69 (-8.06 to -3.33) | +0.35% (+0.08 to +0.62) | +46.18% (+34.84 to +57.51) |
| db_cache | Database & Transactions | capacity | FASTER + FEWER MISSES | -5.60 (-7.95 to -3.24) | +0.37% (-0.04 to +0.78) | +37.30% (+32.21 to +42.39) |
| volt_watt | Energy Storage & Microgrid | capacity | FEWER MISSES | -5.49 (-6.03 to -4.95) | +0.00% (+0.00 to +0.00) | +0.41% (+0.39 to +0.44) |
| facility_peak_guard | Facility & Grid Optimization | capacity | FEWER MISSES | -5.43 (-6.08 to -4.78) | +0.00% (+0.00 to +0.00) | +0.25% (+0.24 to +0.25) |
| renewable_dispatch | Facility & Grid Optimization | capacity | FEWER MISSES | -5.43 (-5.80 to -5.06) | +0.00% (+0.00 to +0.00) | +0.25% (+0.25 to +0.25) |
| nvidia_platform_power_budget | GPU Hardware | power | AT ITS LIMIT ON NATIVE | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) |
| adaptive_gpu_power_cap | GPU Hardware | power | AT ITS LIMIT ON NATIVE | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) |
| k8s_power_manager_core_profile | Host CPU & Memory | power | AT ITS LIMIT ON NATIVE | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) |
| ear_global_energy_budget | Host CPU & Memory | admission | AT ITS LIMIT ON NATIVE | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) |
| ear_cpu_frequency_policy | Host CPU & Memory | power | AT ITS LIMIT ON NATIVE | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) |
| climatik_inference_power_cap | GPU Hardware | power | AT ITS LIMIT ON NATIVE | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) |
| swarm_formation_spacing | Aviation & Autonomous Flight | capacity | FASTER | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.23% (+0.11 to +0.35) |
| ardupilot_atc_accel_r_max | Aviation & Autonomous Flight | power | AT ITS LIMIT ON NATIVE | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) |
| ardupilot_wpnav_speed | Aviation & Autonomous Flight | capacity | FASTER | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.15% (+0.09 to +0.21) |
| px4_mc_rollrate_max | Aviation & Autonomous Flight | capacity | FASTER | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.04% (+0.02 to +0.06) |

Raw per-seed contrasts: `REALMS_V5.json`. One row per muscle: `MUSCLES_V5.csv`. Fingerprints: `RUN.json`, `SHA256SUMS.txt`.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
