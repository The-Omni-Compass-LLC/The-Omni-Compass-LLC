# The realms on Omni v5 at the max: 1097 muscles and six organisms, native against Omni on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (modelled). Run 2026-10-12 11:41 UTC, commit `3132004c90de`, seeds 3000-3009 (10 paired seeds per muscle, per organism and per load), catalog `realms/catalog_v5.csv`. The engine is **omni-v5** (`tools/omni_version.py`, `OMNI_V5.json`) at its default, **the max** (`realms/compass_arm_v5.py`, `V5CFG`), on top of each plant's own native controller. Harness `realms/`.

**The max.** Every muscle is pushed toward its own limit for the most work, faster: a pool's machines are started before the rush lands (the recent peak arrivals widened by the largest rise the pool has shown within one machine start, at 95% utilisation), never fewer than its twin runs (the brain's model of native: the same pool under its own autoscaler alone, on the same arrivals); a room is cooled ahead of the heat as it nears its limit or its cooling nears flat out; a battery's line is clipped from its charge, a UPS lending only the charge above its outage floor. Work waiting in line is cleared within one machine start, and the machines it no longer needs go back at once (never below the twin). A muscle native already runs flat out (full clock, full speed, full actuator, nothing turned away) is wired, watched and native: there is nothing above native to give it. Nothing is taken from one muscle to give to another; the max never shaves. The energy the max takes is reported as **power given**, beside the work and the speed it bought.

**The line.** Under the line load, every plant starts with work already waiting, a 25% share of the work its own run brings: a pool's jobs submitted before the start (its machines take them from what the requests leave them), an axis's tasks queued, a site's flexible load held over. A room's heat and a loop's demand cannot wait, so they have none. Both arms start with the same line; the one that clears it sooner is **faster**.

**The bone.** Inside an organism the max may give only the power the body can carry: a site's grid line and a room's cooling are loaded by the whole body (the machines' power is heat in every room, the body's power swing is load on every site's line), so machines and cooling are granted out of the room the most loaded line has left, read one decision ahead (its latest reading plus the larger of 3.09 of its own step-to-step wobbles and the largest single climb it has shown, the wobbles counted on the line without the max's own machines: its own steps are not the line's). A site with flexible load waiting gives its catch-up the room first. With no room, what the max added goes back, as much as the shortfall needs (the pools holding the most extra machines first, the machines started last first), never below a pool's twin: nothing native has is taken. The organisms run the hour around each battery site's daily peak, where the UPS lines carry most of their rating: the bone is tight there, and the max gives only what it can carry.

**The lease.** At 80% of every run the brain is cut; the plug walks every setting back to native over 24 decisions (a jump the body would have to absorb at once is the swing the founder ordered gone), and the run goes on native until it ends; every knob must be back at the operator's own before then (valid). A floor that only held a pool at its twin's count adds nothing to walk back and is let go at once (a walking floor would hold machines native had already released). The security kill switch is instant (`omnicompass/master.py`).

These are models; a model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test. What a row shows is whether the max, applied to that knob, helps or hurts the model.

## The six organisms: the organism's own load

Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant decisions over their line, native → omni (the change in misses). Power given: the organism's energy against native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals over seeds.

| Organism | Muscles | Label | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Work per energy | Valid |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 530 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 1.96% → 1.96% (−0.2%) | -0.00 (-0.01 to -0.00) | +0.07% (+0.07 to +0.07) | +0.44% | -0.07% (-0.07 to -0.07) | yes |
| Physics / Robotics / Autonomous | 394 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 4.95% → 4.94% (−0.1%) | -0.01 (-0.01 to -0.00) | +0.06% (+0.06 to +0.06) | +0.59% | -0.06% (-0.06 to -0.05) | yes |
| Energy / Facility / Industrial | 470 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 1.57% → 1.56% (−0.7%) | -0.01 (-0.02 to -0.00) | +0.00% (+0.00 to +0.00) | +0.50% | -0.00% (-0.00 to -0.00) | yes |
| Distribution / Specialized | 474 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 2.37% → 2.36% (−0.3%) | -0.01 (-0.01 to -0.00) | +0.02% (+0.02 to +0.02) | +0.49% | -0.02% (-0.02 to -0.02) | yes |
| The four stacked, every shared muscle in each | 1868 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 2.60% → 2.59% (−0.3%) | -0.01 (-0.01 to -0.00) | +0.00% (+0.00 to +0.00) | +0.50% | -0.00% (-0.00 to -0.00) | yes |
| The whole tower, every muscle once | 1097 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 2.73% → 2.73% (−0.2%) | -0.00 (-0.01 to -0.00) | +0.00% (+0.00 to +0.00) | +0.21% | -0.00% (-0.00 to -0.00) | yes |

## The six organisms: the climb (1 2 3 2 3 4 ..., level 4 = own load, 8 = twice it)

Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant decisions over their line, native → omni (the change in misses). Power given: the organism's energy against native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals over seeds.

| Organism | Muscles | Label | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Work per energy | Valid |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 530 | **MORE WORK + FEWER MISSES** | +0.00% (+0.00 to +0.00) | 5.60% → 5.49% (−2.1%) | -0.12 (-0.14 to -0.10) | +0.08% (+0.08 to +0.09) | +0.69% | -0.08% (-0.09 to -0.08) | yes |
| Physics / Robotics / Autonomous | 394 | **MORE WORK + FEWER MISSES** | +0.00% (+0.00 to +0.00) | 9.95% → 9.85% (−1.1%) | -0.11 (-0.13 to -0.08) | +0.07% (+0.07 to +0.07) | +0.82% | -0.07% (-0.07 to -0.06) | yes |
| Energy / Facility / Industrial | 470 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 8.16% → 8.16% (−0.0%) | -0.00 (-0.01 to -0.00) | +0.00% (+0.00 to +0.00) | +0.50% | -0.00% (-0.00 to -0.00) | yes |
| Distribution / Specialized | 474 | **MORE WORK + FEWER MISSES** | +0.00% (+0.00 to +0.00) | 6.48% → 6.34% (−2.1%) | -0.14 (-0.17 to -0.10) | +0.08% (+0.07 to +0.09) | +0.74% | -0.08% (-0.09 to -0.07) | yes |
| The four stacked, every shared muscle in each | 1868 | **MORE WORK + FEWER MISSES** | +0.00% (+0.00 to +0.00) | 7.39% → 7.30% (−1.2%) | -0.09 (-0.11 to -0.07) | +0.00% (+0.00 to +0.00) | +0.68% | +0.00% (-0.00 to +0.00) | yes |
| The whole tower, every muscle once | 1097 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 6.94% → 6.94% (−0.0%) | -0.00 (-0.00 to -0.00) | +0.00% (+0.00 to +0.00) | +0.21% | -0.00% (-0.00 to -0.00) | yes |

## The six organisms: work waiting in line (a 25% share of the run's own work waiting when it starts)

Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant decisions over their line, native → omni (the change in misses). Power given: the organism's energy against native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals over seeds.

| Organism | Muscles | Label | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Work per energy | Valid |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 530 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 2.46% → 2.41% (−2.1%) | -0.05 (-0.05 to -0.05) | +0.07% (+0.07 to +0.07) | +0.44% | -0.07% (-0.07 to -0.07) | yes |
| Physics / Robotics / Autonomous | 394 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 11.08% → 11.02% (−0.5%) | -0.06 (-0.06 to -0.05) | +0.05% (+0.05 to +0.05) | +0.59% | -0.05% (-0.05 to -0.05) | yes |
| Energy / Facility / Industrial | 470 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 1.40% → 1.39% (−0.8%) | -0.01 (-0.02 to -0.00) | +0.00% (+0.00 to +0.00) | +0.50% | -0.00% (-0.00 to -0.00) | yes |
| Distribution / Specialized | 474 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 3.02% → 2.97% (−1.5%) | -0.05 (-0.05 to -0.04) | +0.02% (+0.02 to +0.02) | +0.49% | -0.02% (-0.02 to -0.02) | yes |
| The four stacked, every shared muscle in each | 1868 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 4.15% → 4.11% (−1.0%) | -0.04 (-0.04 to -0.04) | +0.00% (+0.00 to +0.00) | +0.50% | -0.00% (-0.00 to -0.00) | yes |
| The whole tower, every muscle once | 1097 | **FEWER MISSES** | +0.00% (+0.00 to +0.00) | 4.65% → 4.64% (−0.1%) | -0.00 (-0.01 to -0.00) | +0.00% (+0.00 to +0.00) | +0.21% | -0.00% (-0.00 to -0.00) | yes |

## Inside the organisms: every plant that did worse than native

A stricter look than an organism's total: every plant inside each organism, over all seeds, that did less work than native or spent more decisions over its own line, under each load. Reported whatever it shows.

| Load | Organism | Plants | Plants worse | The plants (work change, extra decisions over the line, all seeds) |
|---|---|---:|---:|---|
| normal | Compute / AI / Cloud | 530 | 0 | none |
| normal | Physics / Robotics / Autonomous | 394 | 0 | none |
| normal | Energy / Facility / Industrial | 470 | 0 | none |
| normal | Distribution / Specialized | 474 | 0 | none |
| normal | The four stacked, every shared muscle in each | 1868 | 0 | none |
| normal | The whole tower, every muscle once | 1097 | 0 | none |
| climb | Compute / AI / Cloud | 530 | 1 | 547 (-0.083%, +0) |
| climb | Physics / Robotics / Autonomous | 394 | 0 | none |
| climb | Energy / Facility / Industrial | 470 | 0 | none |
| climb | Distribution / Specialized | 474 | 2 | 557 (-0.032%, +0); 543 (+0.000%, +1) |
| climb | The four stacked, every shared muscle in each | 1868 | 3 | 547@compute_ai_cloud (-0.083%, +0); 557@distribution_specialized (-0.032%, +0); 543@distribution_specialized (+0.000%, +1) |
| climb | The whole tower, every muscle once | 1097 | 0 | none |
| line | Compute / AI / Cloud | 530 | 0 | none |
| line | Physics / Robotics / Autonomous | 394 | 0 | none |
| line | Energy / Facility / Industrial | 470 | 0 | none |
| line | Distribution / Specialized | 474 | 0 | none |
| line | The four stacked, every shared muscle in each | 1868 | 0 | none |
| line | The whole tower, every muscle once | 1097 | 0 | none |

## Every muscle alone, by home realm

Each muscle runs under 2 loads, its own load (normal) and work waiting in line (25% of the run's own work at the start) (line). **Better**: at least one gain beyond the noise under some load (more work, faster: the line cleared sooner, fewer misses) and no loss under any. **At its limit on native**: native already runs the knob at the top of its range (full clock, full speed, full torque, full battery power, nothing paced or turned away), so the max has nothing above native to give it and writes nothing. **Same as native**: the max acted or could, and the result is no different beyond the noise (native already did all the work that came and was almost never over its line).

| Realm | Muscles | Better | of them: more work | faster | fewer misses | Same as native | At its limit on native | Mixed | Worse | Invalid |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | 434 | 270 | 11 | 270 | 217 | 24 | 140 | 0 | 0 | 0 |
| Physics / Robotics / Autonomous | 137 | 53 | 7 | 51 | 19 | 2 | 82 | 0 | 0 | 0 |
| Energy / Facility / Industrial | 249 | 11 | 0 | 0 | 11 | 118 | 120 | 0 | 0 | 0 |
| Distribution / Specialized | 277 | 170 | 14 | 168 | 138 | 11 | 96 | 0 | 0 | 0 |
| **All** | **1097** | **504** | **32** | **489** | **385** | **155** | **438** | **0** | **0** | **0** |

## Every muscle alone under its own load, by kind of plant and knob

Misses: the share of decisions over the line, native → omni. Line: minutes to clear the work waiting at the start, native → omni (and the share still waiting at the end, where it did not clear). Power given: energy against native's.

| Plant | Knob | Muscles | Omni acts on | Better | At its limit on native | Misses, native → omni | Work | Line, native → omni | Power given | Wear |
|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|
| compute_pool | admission | 194 | 0 | 0 | 194 | 1.69% → 1.69% | +0.000% | no line | +0.00% | +0.00% |
| compute_pool | capacity | 419 | 419 | 326 | 0 | 1.54% → 0.48% | +0.041% | no line | +21.49% | +43.64% |
| compute_pool | power | 37 | 0 | 0 | 37 | 1.49% → 1.49% | +0.000% | no line | +0.00% | +0.00% |
| compute_pool | setpoint | 35 | 35 | 29 | 0 | 1.72% → 0.58% | +0.029% | no line | +21.28% | +44.90% |
| energy_storage | admission | 10 | 0 | 0 | 10 | 14.29% → 14.29% | +0.000% | no line | +0.00% | +0.00% |
| energy_storage | capacity | 13 | 13 | 8 | 0 | 13.37% → 11.79% | +0.000% | no line | +0.21% | +41.72% |
| energy_storage | power | 23 | 0 | 0 | 23 | 14.71% → 14.71% | +0.000% | no line | +0.00% | +0.00% |
| energy_storage | setpoint | 8 | 8 | 5 | 0 | 17.11% → 15.97% | +0.000% | no line | +0.15% | +21.17% |
| motion_axis | admission | 30 | 0 | 0 | 30 | 1.49% → 1.49% | +0.000% | no line | +0.00% | +0.00% |
| motion_axis | capacity | 48 | 37 | 1 | 11 | 1.52% → 0.87% | +0.207% | no line | +0.83% | +2.09% |
| motion_axis | power | 38 | 0 | 0 | 38 | 4.70% → 4.70% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | admission | 33 | 0 | 0 | 33 | 0.03% → 0.03% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | capacity | 39 | 0 | 0 | 39 | 0.03% → 0.03% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | power | 12 | 0 | 0 | 12 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | setpoint | 111 | 0 | 0 | 0 | 0.01% → 0.01% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | admission | 7 | 0 | 0 | 7 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | capacity | 17 | 0 | 0 | 0 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | power | 4 | 0 | 0 | 4 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | setpoint | 19 | 19 | 0 | 0 | 0.00% → 0.00% | +0.000% | no line | +0.09% | -0.01% |

## Every muscle alone under work waiting in line (25% of the run's own work at the start), by kind of plant and knob

Misses: the share of decisions over the line, native → omni. Line: minutes to clear the work waiting at the start, native → omni (and the share still waiting at the end, where it did not clear). Power given: energy against native's.

| Plant | Knob | Muscles | Omni acts on | Better | At its limit on native | Misses, native → omni | Work | Line, native → omni | Power given | Wear |
|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|
| compute_pool | admission | 194 | 0 | 0 | 194 | 1.53% → 1.53% | +0.000% | 13.9 → 13.9 min | +0.00% | +0.00% |
| compute_pool | capacity | 419 | 419 | 419 | 0 | 1.40% → 0.40% | +0.030% | 17.0 → 7.8 min | +21.31% | +43.10% |
| compute_pool | power | 37 | 0 | 0 | 37 | 1.36% → 1.36% | +0.000% | 11.0 → 11.0 min | +0.00% | +0.00% |
| compute_pool | setpoint | 35 | 35 | 35 | 0 | 1.55% → 0.48% | +0.021% | 12.5 → 6.7 min | +20.71% | +42.48% |
| energy_storage | admission | 10 | 0 | 0 | 10 | 14.29% → 14.29% | +0.000% | 391.2 → 391.2 min (0% → 0% left) | +0.00% | +0.00% |
| energy_storage | capacity | 13 | 13 | 4 | 0 | 13.37% → 12.18% | +0.000% | 404.5 → 404.5 min (0% → 0% left) | +0.20% | +41.72% |
| energy_storage | power | 23 | 0 | 0 | 23 | 14.71% → 14.71% | +0.000% | 364.9 → 364.9 min (0% → 0% left) | +0.00% | +0.00% |
| energy_storage | setpoint | 8 | 8 | 5 | 0 | 17.11% → 15.94% | +0.000% | 388.2 → 388.2 min (0% → 0% left) | +0.14% | +21.17% |
| motion_axis | admission | 30 | 0 | 0 | 30 | 6.25% → 6.25% | +0.000% | 3.5 → 3.5 min | +0.00% | +0.00% |
| motion_axis | capacity | 48 | 37 | 37 | 11 | 12.06% → 8.28% | +0.688% | 2.8 → 2.6 min | +1.35% | +3.88% |
| motion_axis | power | 38 | 0 | 0 | 38 | 18.34% → 18.34% | +0.000% | 4.7 → 4.7 min | +0.00% | +0.00% |
| process_loop | admission | 33 | 0 | 0 | 33 | 0.03% → 0.03% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | capacity | 39 | 0 | 0 | 39 | 0.03% → 0.03% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | power | 12 | 0 | 0 | 12 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| process_loop | setpoint | 111 | 0 | 0 | 0 | 0.01% → 0.01% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | admission | 7 | 0 | 0 | 7 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | capacity | 17 | 0 | 0 | 0 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | power | 4 | 0 | 0 | 4 | 0.00% → 0.00% | +0.000% | no line | +0.00% | +0.00% |
| thermal_zone | setpoint | 19 | 19 | 0 | 0 | 0.00% → 0.00% | +0.000% | no line | +0.09% | -0.01% |

## No-harm check

- Omni acts on **531** of 1097 muscles alone. **438** are at their limit on native (the knob is already at the top of its range); the rest it could act on show nothing beyond the noise to gain.
- Muscles alone labelled **WORSE** or **MIXED** under any load: **0**.
- The lease hands every knob back to native before each run ends: 1097 of 1097 muscles under every load; 6 of 6 organisms under normal, 6 of 6 organisms under climb, 6 of 6 organisms under line.

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
| payment_failover | Commerce & Payment Systems | capacity | MORE WORK + FASTER + FEWER MISSES | -5.29 (-6.33 to -4.25) | +0.16% (+0.06 to +0.27) | +37.80% (+28.52 to +47.07) |
| db_pool_resize | Database & Transactions | capacity | FASTER + FEWER MISSES | -5.15 (-6.98 to -3.33) | +0.29% (-0.09 to +0.67) | +44.81% (+33.42 to +56.21) |
| checkpoint_rate | Database & Transactions | capacity | FASTER + FEWER MISSES | -5.11 (-6.74 to -3.48) | +0.46% (-0.05 to +0.97) | +40.69% (+32.17 to +49.22) |
| swarm_formation_spacing | Aviation & Autonomous Flight | capacity | FASTER | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.23% (+0.11 to +0.35) |
| ardupilot_atc_accel_r_max | Aviation & Autonomous Flight | power | AT ITS LIMIT ON NATIVE | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) |
| ardupilot_wpnav_speed | Aviation & Autonomous Flight | capacity | FASTER | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.15% (+0.09 to +0.21) |
| px4_mc_rollrate_max | Aviation & Autonomous Flight | capacity | FASTER | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.04% (+0.02 to +0.06) |
| px4_mpc_acc_hor | Aviation & Autonomous Flight | capacity | FASTER | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.06% (+0.02 to +0.09) |
| px4_mpc_z_vel_max_up | Aviation & Autonomous Flight | capacity | FASTER | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.07% (+0.05 to +0.10) |
| px4_mpc_xy_vel_max | Aviation & Autonomous Flight | capacity | FASTER | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.15% (+0.11 to +0.19) |
| manipulator_payload_speed_scaling | Robotics Motion Control | capacity | FASTER + FEWER MISSES | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.28% (+0.18 to +0.39) |
| humanoid_joint_torque_limit | Robotics Motion Control | power | AT ITS LIMIT ON NATIVE | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) |
| humanoid_balance_margin | Robotics Motion Control | capacity | FASTER + FEWER MISSES | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.38% (+0.25 to +0.51) |

Raw per-seed contrasts: `REALMS_V5.json`. One row per muscle: `MUSCLES_V5.csv`. Fingerprints: `RUN.json`, `SHA256SUMS.txt`.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
