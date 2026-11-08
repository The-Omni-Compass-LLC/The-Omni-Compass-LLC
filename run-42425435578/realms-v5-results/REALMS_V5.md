# The realms on omni-v26 at the max: 1107 muscles and seven organisms, three ways: native, Omni-Compass and native, and Omni-Compass by itself

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Evidence class **S** (modelled). Run 2026-11-07 23:30 UTC, commit `84462b32eacc`, seeds 3000-3009 (10 paired seeds per muscle, per organism and per load), catalog `realms/catalog_v5.csv`. The engine is **omni-v26** (`tools/omni_version.py`) at its default, **the max** (`realms/compass_arm_v5.py`, `V5CFG`), on top of each plant's own native controller. Harness `realms/`.

**The max.** Every muscle is pushed toward its own limit for the most work, faster: a pool's machines are started before the rush lands (the recent peak arrivals widened by the largest rise the pool has shown within one machine start, at 95% utilisation), never fewer than its twin runs (the brain's model of native: the same pool under its own autoscaler alone, on the same arrivals); a room is cooled ahead of the heat as it nears its limit or its cooling nears flat out; a battery's line is clipped from its charge, a UPS lending only the charge above its outage floor. Work waiting in line is cleared within one machine start, and the machines it no longer needs go back at once (never below the twin). A muscle native already runs flat out (full clock, full speed, full actuator, nothing turned away) is wired, watched and native: there is nothing above native to give it. Nothing is taken from one muscle to give to another; the max never shaves. The energy the max takes is reported as **power given**, beside the work and the speed it bought.

**The line.** Under the line load, every plant starts with work already waiting, a 25% share of the work its own run brings: a pool's jobs submitted before the start (its machines take them from what the requests leave them), an axis's tasks queued, a site's flexible load held over. A room's heat and a loop's demand cannot wait, so they have none. Both arms start with the same line; the one that clears it sooner is **faster**.

**The bone.** Inside an organism the max may give only the power the body can carry: a site's grid line and a room's cooling are loaded by the whole body (the machines' power is heat in every room, the body's power swing is load on every site's line), so machines and cooling are granted out of the room the most loaded line has left, read one decision ahead (its latest reading plus the larger of 3.09 of its own step-to-step wobbles and the largest single climb it has shown, the wobbles counted on the line without the max's own machines: its own steps are not the line's). A site with flexible load waiting gives its catch-up the room first. With no room, what the max added goes back, as much as the shortfall needs (the pools holding the most extra machines first, the machines started last first), never below a pool's twin: nothing native has is taken. The organisms run the hour around each battery site's daily peak, where the UPS lines carry most of their rating: the bone is tight there, and the max gives only what it can carry.

**The lease.** At 80% of every run the brain is cut; the plug walks every setting back to native over 24 decisions (a jump the body would have to absorb at once is the swing the founder ordered gone), and the run goes on native until it ends; every knob must be back at the operator's own before then (valid). A floor that only held a pool at its twin's count adds nothing to walk back and is let go at once (a walking floor would hold machines native had already released). The security kill switch is instant (`omnicompass/master.py`).

These are models; a model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test. What a row shows is whether the max, applied to that knob, helps or hurts the model.

## The seven organisms: the organism's own load

Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant decisions over their line, native → Omni-Compass and native (the change in misses). Power given: the organism's energy against native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals over seeds.

| Organism | Muscles | Reading | Work | Misses, native → Omni-Compass and native | Misses (pp) | Power given | Wear | Work per energy | Valid |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| The spine, the muscles every stack runs on | 267 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 2.39% → 2.25% (−6.1%) | -0.15 (-0.18 to -0.11) | +0.01% (+0.01 to +0.01) | +0.12% | -0.01% (-0.01 to -0.01) | yes |
| Compute / AI / Cloud | 540 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 1.97% → 1.90% (−3.6%) | -0.07 (-0.08 to -0.06) | +0.01% (+0.01 to +0.01) | +0.06% | -0.01% (-0.01 to -0.01) | yes |
| Physics / Robotics / Autonomous | 404 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 4.88% → 4.76% (−2.5%) | -0.12 (-0.14 to -0.10) | +0.01% (+0.01 to +0.01) | +0.11% | -0.01% (-0.01 to -0.01) | yes |
| Energy / Facility / Industrial | 480 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 1.58% → 1.47% (−7.5%) | -0.12 (-0.14 to -0.09) | +0.00% (+0.00 to +0.00) | +0.09% | -0.00% (-0.00 to -0.00) | yes |
| Distribution / Specialized | 484 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 2.36% → 2.30% (−2.8%) | -0.07 (-0.08 to -0.05) | +0.00% (+0.00 to +0.00) | +0.06% | -0.00% (-0.00 to -0.00) | yes |
| The four stacked, every shared muscle in each | 1908 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 2.59% → 2.50% (−3.6%) | -0.09 (-0.11 to -0.08) | +0.00% (+0.00 to +0.00) | +0.08% | -0.00% (-0.00 to -0.00) | yes |
| The whole tower, every muscle once | 1107 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 2.73% → 2.67% (−1.9%) | -0.05 (-0.06 to -0.04) | +0.00% (+0.00 to +0.00) | +0.04% | -0.00% (-0.00 to -0.00) | yes |

**Omni-Compass by itself**, the organism's own load (the founder's order of 23 October, `docs/SOLO_PREREGISTRATION.md`): every pool's own autoscaler switched off and the brain the only controller of its count; every other muscle as in Omni-Compass and native, because its native is a setting native holds still or its own actuator. Read against native and against Omni-Compass and native, on the same seeds.

| Organism | Against native | Work | Misses, native → by itself | Misses (pp) | Power given | Wear | Against Omni-Compass and native | Valid |
|---|---|---:|---|---:|---:|---:|---|---|
| The spine, the muscles every stack runs on | **LOSS** | -1.35% (-1.43 to -1.28) | 2.39% → 13.45% (+462.1%) | +11.05 (+10.55 to +11.55) | -1.11% (-1.16 to -1.06) | -14.96% | LOSS | yes |
| Compute / AI / Cloud | **LOSS** | -1.62% (-1.74 to -1.50) | 1.97% → 12.90% (+554.9%) | +10.93 (+10.62 to +11.24) | -2.25% (-2.35 to -2.15) | -15.88% | LOSS | yes |
| Physics / Robotics / Autonomous | **LOSS** | -2.85% (-2.94 to -2.77) | 4.88% → 15.34% (+214.3%) | +10.46 (+10.12 to +10.80) | -2.15% (-2.25 to -2.05) | -12.44% | LOSS | yes |
| Energy / Facility / Industrial | **LOSS** | -0.75% (-0.79 to -0.71) | 1.58% → 7.77% (+390.2%) | +6.18 (+5.90 to +6.46) | -0.00% (-0.00 to -0.00) | -8.26% | LOSS | yes |
| Distribution / Specialized | **LOSS** | -2.40% (-2.56 to -2.24) | 2.36% → 15.78% (+568.1%) | +13.42 (+12.96 to +13.88) | -1.87% (-2.23 to -1.51) | -16.29% | LOSS | yes |
| The four stacked, every shared muscle in each | **LOSS** | -1.86% (-1.93 to -1.79) | 2.59% → 12.86% (+396.6%) | +10.27 (+9.99 to +10.55) | -0.02% (-0.02 to -0.02) | -13.34% | LOSS | yes |
| The whole tower, every muscle once | **LOSS** | -2.23% (-2.33 to -2.13) | 2.73% → 12.43% (+356.2%) | +9.71 (+9.52 to +9.89) | -0.01% (-0.02 to -0.01) | -12.17% | LOSS | yes |

## The seven organisms: the climb (1 2 3 2 3 4 ..., level 4 = own load, 8 = twice it)

Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant decisions over their line, native → Omni-Compass and native (the change in misses). Power given: the organism's energy against native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals over seeds.

| Organism | Muscles | Reading | Work | Misses, native → Omni-Compass and native | Misses (pp) | Power given | Wear | Work per energy | Valid |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| The spine, the muscles every stack runs on | 267 | **GAIN (more work + fewer misses)** | +0.00% (+0.00 to +0.01) | 8.00% → 7.37% (−7.9%) | -0.63 (-0.70 to -0.57) | +0.04% (+0.03 to +0.04) | +0.45% | -0.04% (-0.04 to -0.03) | yes |
| Compute / AI / Cloud | 540 | **GAIN (more work + fewer misses)** | +0.00% (+0.00 to +0.00) | 5.59% → 5.20% (−7.0%) | -0.39 (-0.42 to -0.36) | +0.05% (+0.04 to +0.05) | +0.31% | -0.04% (-0.05 to -0.04) | yes |
| Physics / Robotics / Autonomous | 404 | **GAIN (more work + fewer misses)** | +0.00% (+0.00 to +0.00) | 9.82% → 9.50% (−3.2%) | -0.32 (-0.36 to -0.27) | +0.02% (+0.02 to +0.02) | +0.23% | -0.02% (-0.02 to -0.02) | yes |
| Energy / Facility / Industrial | 480 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 8.07% → 7.86% (−2.7%) | -0.22 (-0.25 to -0.19) | +0.00% (+0.00 to +0.00) | +0.20% | -0.00% (-0.00 to -0.00) | yes |
| Distribution / Specialized | 484 | **GAIN (more work + fewer misses)** | +0.00% (+0.00 to +0.00) | 6.43% → 5.97% (−7.2%) | -0.46 (-0.49 to -0.43) | +0.03% (+0.02 to +0.03) | +0.46% | -0.02% (-0.03 to -0.02) | yes |
| The four stacked, every shared muscle in each | 1908 | **GAIN (more work + fewer misses)** | +0.00% (+0.00 to +0.00) | 7.32% → 6.97% (−4.8%) | -0.35 (-0.37 to -0.33) | +0.00% (+0.00 to +0.00) | +0.30% | +0.00% (+0.00 to +0.00) | yes |
| The whole tower, every muscle once | 1107 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 6.91% → 6.82% (−1.4%) | -0.09 (-0.11 to -0.08) | +0.00% (+0.00 to +0.00) | +0.09% | -0.00% (-0.00 to -0.00) | yes |

**Omni-Compass by itself**, the climb (1 2 3 2 3 4 ..., level 4 = own load, 8 = twice it) (the founder's order of 23 October, `docs/SOLO_PREREGISTRATION.md`): every pool's own autoscaler switched off and the brain the only controller of its count; every other muscle as in Omni-Compass and native, because its native is a setting native holds still or its own actuator. Read against native and against Omni-Compass and native, on the same seeds.

| Organism | Against native | Work | Misses, native → by itself | Misses (pp) | Power given | Wear | Against Omni-Compass and native | Valid |
|---|---|---:|---|---:|---:|---:|---|---|
| The spine, the muscles every stack runs on | **LOSS** | -4.10% (-4.43 to -3.76) | 8.00% → 22.97% (+187.1%) | +14.97 (+14.54 to +15.39) | -1.88% (-1.95 to -1.80) | -19.52% | LOSS | yes |
| Compute / AI / Cloud | **LOSS** | -4.51% (-4.68 to -4.34) | 5.59% → 20.11% (+259.7%) | +14.52 (+14.27 to +14.77) | -3.23% (-3.31 to -3.14) | -19.85% | LOSS | yes |
| Physics / Robotics / Autonomous | **LOSS** | -5.04% (-5.18 to -4.90) | 9.82% → 22.83% (+132.5%) | +13.01 (+12.72 to +13.31) | -2.42% (-2.50 to -2.34) | -15.34% | LOSS | yes |
| Energy / Facility / Industrial | **LOSS** | -3.07% (-3.19 to -2.95) | 8.07% → 16.94% (+109.8%) | +8.87 (+8.63 to +9.10) | -0.00% (-0.00 to -0.00) | -10.72% | LOSS | yes |
| Distribution / Specialized | **LOSS** | -5.93% (-6.21 to -5.65) | 6.43% → 22.82% (+254.9%) | +16.39 (+15.99 to +16.79) | -2.73% (-3.17 to -2.29) | -19.94% | LOSS | yes |
| The four stacked, every shared muscle in each | **LOSS** | -4.62% (-4.76 to -4.48) | 7.32% → 20.58% (+181.0%) | +13.25 (+13.05 to +13.45) | -0.03% (-0.03 to -0.02) | -16.62% | LOSS | yes |
| The whole tower, every muscle once | **LOSS** | -4.61% (-4.72 to -4.50) | 6.91% → 18.80% (+171.9%) | +11.89 (+11.75 to +12.02) | -0.02% (-0.02 to -0.02) | -14.68% | LOSS | yes |

## The seven organisms: work waiting in line (a 25% share of the run's own work waiting when it starts)

Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant decisions over their line, native → Omni-Compass and native (the change in misses). Power given: the organism's energy against native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals over seeds.

| Organism | Muscles | Reading | Work | Misses, native → Omni-Compass and native | Misses (pp) | Power given | Wear | Work per energy | Valid |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| The spine, the muscles every stack runs on | 267 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 4.23% → 3.86% (−8.8%) | -0.37 (-0.40 to -0.34) | +0.04% (+0.03 to +0.04) | +0.43% | -0.04% (-0.04 to -0.03) | yes |
| Compute / AI / Cloud | 540 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 2.47% → 2.27% (−8.3%) | -0.20 (-0.22 to -0.19) | +0.04% (+0.04 to +0.05) | +0.28% | -0.04% (-0.05 to -0.04) | yes |
| Physics / Robotics / Autonomous | 404 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 10.87% → 10.62% (−2.3%) | -0.25 (-0.28 to -0.22) | +0.03% (+0.03 to +0.03) | +0.33% | -0.03% (-0.03 to -0.03) | yes |
| Energy / Facility / Industrial | 480 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 1.41% → 1.29% (−8.3%) | -0.12 (-0.14 to -0.09) | +0.00% (+0.00 to +0.00) | +0.09% | -0.00% (-0.00 to -0.00) | yes |
| Distribution / Specialized | 484 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 3.00% → 2.85% (−4.7%) | -0.14 (-0.17 to -0.12) | +0.01% (+0.00 to +0.01) | +0.18% | -0.01% (-0.01 to -0.00) | yes |
| The four stacked, every shared muscle in each | 1908 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 4.12% → 3.94% (−4.3%) | -0.18 (-0.19 to -0.16) | +0.00% (+0.00 to +0.00) | +0.22% | -0.00% (-0.00 to -0.00) | yes |
| The whole tower, every muscle once | 1107 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 4.62% → 4.57% (−1.1%) | -0.05 (-0.06 to -0.04) | +0.00% (+0.00 to +0.00) | +0.04% | -0.00% (-0.00 to -0.00) | yes |

**Omni-Compass by itself**, work waiting in line (a 25% share of the run's own work waiting when it starts) (the founder's order of 23 October, `docs/SOLO_PREREGISTRATION.md`): every pool's own autoscaler switched off and the brain the only controller of its count; every other muscle as in Omni-Compass and native, because its native is a setting native holds still or its own actuator. Read against native and against Omni-Compass and native, on the same seeds.

| Organism | Against native | Work | Misses, native → by itself | Misses (pp) | Power given | Wear | Against Omni-Compass and native | Valid |
|---|---|---:|---|---:|---:|---:|---|---|
| The spine, the muscles every stack runs on | **LOSS** | -0.78% (-1.24 to -0.33) | 4.23% → 13.66% (+222.8%) | +9.43 (+8.88 to +9.98) | -2.26% (-2.34 to -2.18) | -28.53% | LOSS | yes |
| Compute / AI / Cloud | **LOSS** | -3.24% (-3.45 to -3.03) | 2.47% → 12.95% (+423.5%) | +10.48 (+10.15 to +10.81) | -4.10% (-4.20 to -4.00) | -28.61% | LOSS | yes |
| Physics / Robotics / Autonomous | **LOSS** | -4.21% (-4.35 to -4.07) | 10.87% → 21.20% (+95.1%) | +10.34 (+9.99 to +10.68) | -3.18% (-3.30 to -3.06) | -21.47% | LOSS | yes |
| Energy / Facility / Industrial | **LOSS** | -1.71% (-1.79 to -1.63) | 1.41% → 7.72% (+448.3%) | +6.31 (+6.03 to +6.60) | -0.00% (-0.00 to -0.00) | -15.85% | LOSS | yes |
| Distribution / Specialized | **LOSS** | -3.98% (-4.18 to -3.77) | 3.00% → 16.14% (+438.7%) | +13.14 (+12.70 to +13.59) | -4.34% (-4.93 to -3.76) | -29.65% | LOSS | yes |
| The four stacked, every shared muscle in each | **LOSS** | -3.25% (-3.38 to -3.12) | 4.12% → 14.19% (+244.9%) | +10.08 (+9.79 to +10.36) | -0.04% (-0.05 to -0.04) | -24.15% | LOSS | yes |
| The whole tower, every muscle once | **LOSS** | -3.90% (-4.02 to -3.77) | 4.62% → 14.46% (+212.9%) | +9.84 (+9.64 to +10.03) | -0.03% (-0.04 to -0.03) | -21.06% | LOSS | yes |

## Inside the organisms: every plant that did less work than native or missed its line more often

A stricter look than an organism's total: every plant inside each organism, over all seeds, that did less work than native or spent more decisions over its own line, under each load. Reported whatever it shows.

| Load | Organism | Plants | Plants with less work or more misses | The plants (work change, extra decisions over the line, all seeds) |
|---|---|---:|---:|---|
| normal | The spine, the muscles every stack runs on | 267 | 0 | none |
| normal | Compute / AI / Cloud | 540 | 0 | none |
| normal | Physics / Robotics / Autonomous | 404 | 0 | none |
| normal | Energy / Facility / Industrial | 480 | 0 | none |
| normal | Distribution / Specialized | 484 | 0 | none |
| normal | The four stacked, every shared muscle in each | 1908 | 0 | none |
| normal | The whole tower, every muscle once | 1107 | 0 | none |
| climb | The spine, the muscles every stack runs on | 267 | 0 | none |
| climb | Compute / AI / Cloud | 540 | 0 | none |
| climb | Physics / Robotics / Autonomous | 404 | 0 | none |
| climb | Energy / Facility / Industrial | 480 | 0 | none |
| climb | Distribution / Specialized | 484 | 0 | none |
| climb | The four stacked, every shared muscle in each | 1908 | 0 | none |
| climb | The whole tower, every muscle once | 1107 | 0 | none |
| line | The spine, the muscles every stack runs on | 267 | 0 | none |
| line | Compute / AI / Cloud | 540 | 0 | none |
| line | Physics / Robotics / Autonomous | 404 | 0 | none |
| line | Energy / Facility / Industrial | 480 | 0 | none |
| line | Distribution / Specialized | 484 | 0 | none |
| line | The four stacked, every shared muscle in each | 1908 | 0 | none |
| line | The whole tower, every muscle once | 1107 | 0 | none |

## Every muscle alone, by home realm

Each muscle runs under 2 loads, its own load (normal) and work waiting in line (25% of the run's own work at the start) (line). Each muscle's word is judged by its three aims, never by the sign of a number (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). **GAIN**: at least one of its three aims moved beyond the noise under some load (more work, faster: the line cleared sooner, fewer misses) and none the other way under any. **GAIN AND LOSS**: one toward its aim and one away (less work, slower or more misses). **LOSS**: one away and none toward. **STEADY, at its limit on native**: native already runs the knob at the top of its range (full clock, full speed, full torque, full battery power, nothing paced or turned away), so the max has nothing above native to give it and writes nothing. **STEADY, the same as native**: the max acted or could, and the result is no different beyond the noise (native already did all the work that came and was almost never over its line). The energy the max takes is power given, shown beside the work, never judged.

| Realm | Muscles | GAIN | of them: more work | faster | fewer misses | STEADY, the same as native | STEADY, at its limit on native | GAIN AND LOSS | LOSS | Invalid |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | 444 | 274 | 12 | 274 | 222 | 24 | 146 | 0 | 0 | 0 |
| Physics / Robotics / Autonomous | 137 | 53 | 7 | 51 | 19 | 2 | 82 | 0 | 0 | 0 |
| Energy / Facility / Industrial | 249 | 30 | 0 | 0 | 30 | 122 | 97 | 0 | 0 | 0 |
| Distribution / Specialized | 277 | 170 | 14 | 168 | 138 | 11 | 96 | 0 | 0 | 0 |
| **All** | **1107** | **527** | **33** | **493** | **409** | **159** | **421** | **0** | **0** | **0** |

**Omni-Compass by itself, every muscle alone.** By itself differs from Omni-Compass and native only where the muscle's own native controller can be switched off: a pool whose knob is its count, its autoscaler off and the brain the only controller. Every other muscle's native is a setting native holds still or its own actuator, so by itself is the same arm there, and is counted so.

| Realm | Muscles | The same arm | By itself | GAIN | STEADY, the same as native | GAIN AND LOSS | LOSS | Invalid | Against Omni-Compass and native: GAIN | STEADY | GAIN AND LOSS or LOSS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | 444 | 170 | 274 | 274 | 0 | 0 | 0 | 0 | 33 | 181 | 60 |
| Physics / Robotics / Autonomous | 137 | 123 | 14 | 14 | 0 | 0 | 0 | 0 | 0 | 14 | 0 |
| Energy / Facility / Industrial | 249 | 249 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Distribution / Specialized | 277 | 107 | 170 | 170 | 0 | 0 | 0 | 0 | 22 | 112 | 36 |
| **All** | **1107** | **649** | **458** | **458** | **0** | **0** | **0** | **0** | **55** | **307** | **96** |

## Every muscle alone under its own load, by kind of plant and knob

Misses: the share of decisions over the line, native → Omni-Compass and native. Line: minutes to clear the work waiting at the start, native → Omni-Compass and native (and the share still waiting at the end, where it did not clear). Power given: energy against native's.

| Plant | Knob | Muscles | Omni-Compass acts on | GAIN | STEADY, at its limit on native | Misses, native → Omni-Compass and native | Work | Line, native → Omni-Compass and native | Power given | Wear |
|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|
| compute_pool | admission | 195 | 0 | 0 | 195 | 1.68% → 1.68% | +0.000% | no line | +0.00% | +0.00% |
| compute_pool | capacity | 422 | 422 | 329 | 0 | 1.54% → 0.36% | +0.043% | no line | +36.67% | +75.63% |
| compute_pool | power | 42 | 0 | 0 | 42 | 1.61% → 1.61% | +0.000% | no line | +0.00% | +0.00% |
| compute_pool | setpoint | 36 | 36 | 31 | 0 | 1.71% → 0.45% | +0.029% | no line | +34.91% | +74.43% |
| energy_storage | admission | 10 | 0 | 0 | 10 | 14.29% → 14.29% | +0.000% | no line | +0.00% | +0.00% |
| energy_storage | capacity | 13 | 13 | 13 | 0 | 13.37% → 7.64% | +0.000% | no line | +0.15% | +29.82% |
| energy_storage | power | 23 | 23 | 10 | 0 | 14.71% → 14.04% | +0.000% | no line | +0.04% | -0.60% |
| energy_storage | setpoint | 8 | 8 | 8 | 0 | 17.11% → 14.04% | +0.000% | no line | +0.15% | +20.33% |
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

Misses: the share of decisions over the line, native → Omni-Compass and native. Line: minutes to clear the work waiting at the start, native → Omni-Compass and native (and the share still waiting at the end, where it did not clear). Power given: energy against native's.

| Plant | Knob | Muscles | Omni-Compass acts on | GAIN | STEADY, at its limit on native | Misses, native → Omni-Compass and native | Work | Line, native → Omni-Compass and native | Power given | Wear |
|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|
| compute_pool | admission | 195 | 0 | 0 | 195 | 1.53% → 1.53% | +0.000% | 13.9 → 13.9 min | +0.00% | +0.00% |
| compute_pool | capacity | 422 | 422 | 422 | 0 | 1.40% → 0.33% | +0.030% | 16.9 → 7.2 min | +33.20% | +68.06% |
| compute_pool | power | 42 | 0 | 0 | 42 | 1.47% → 1.47% | +0.000% | 11.0 → 11.0 min | +0.00% | +0.00% |
| compute_pool | setpoint | 36 | 36 | 36 | 0 | 1.54% → 0.41% | +0.021% | 12.4 → 6.2 min | +30.91% | +63.86% |
| energy_storage | admission | 10 | 0 | 0 | 10 | 14.29% → 14.29% | +0.000% | 391.2 → 391.2 min (0% → 0% left) | +0.00% | +0.00% |
| energy_storage | capacity | 13 | 13 | 13 | 0 | 13.37% → 7.64% | +0.000% | 404.5 → 404.5 min (0% → 0% left) | +0.14% | +29.82% |
| energy_storage | power | 23 | 23 | 11 | 0 | 14.71% → 14.00% | +0.000% | 364.9 → 364.9 min (0% → 0% left) | +0.03% | -0.60% |
| energy_storage | setpoint | 8 | 8 | 8 | 0 | 17.11% → 14.04% | +0.000% | 388.2 → 388.2 min (0% → 0% left) | +0.14% | +20.26% |
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

- Omni acts on **567** of 1107 muscles alone. **421** are at their limit on native (the knob is already at the top of its range: STEADY); the rest it could act on show nothing beyond the noise to gain.
- Muscles alone that read **LOSS** or **GAIN AND LOSS** under any load: **0**.
- Muscles alone by themselves (Omni-Compass with the pool's own autoscaler off) that read **LOSS** or **GAIN AND LOSS** against native under any load: **0**.
- The lease hands every knob back to native before each run ends: 1107 of 1107 muscles under every load; 7 of 7 organisms under normal, 7 of 7 organisms under climb, 7 of 7 organisms under line.

## Largest changes (muscles alone, own load, by mean change in misses)

| Muscle | Family | Knob | Label (all loads) | Misses (pp) | Work | Power given |
|---|---|---|---|---:|---:|---:|
| site_battery_dispatch | Facility & Grid Optimization | capacity | FEWER MISSES | -9.97 (-11.86 to -8.09) | +0.00% (+0.00 to +0.00) | +0.20% (+0.16 to +0.23) |
| renewable_dispatch | Facility & Grid Optimization | capacity | FEWER MISSES | -9.21 (-11.05 to -7.37) | +0.00% (+0.00 to +0.00) | +0.17% (+0.12 to +0.22) |
| generator_start_stop | Facility & Grid Optimization | capacity | FEWER MISSES | -8.83 (-10.65 to -7.01) | +0.00% (+0.00 to +0.00) | +0.16% (+0.12 to +0.19) |
| facility_peak_guard | Facility & Grid Optimization | capacity | FEWER MISSES | -8.67 (-10.11 to -7.23) | +0.00% (+0.00 to +0.00) | +0.15% (+0.12 to +0.19) |
| volt_var | Energy Storage & Microgrid | capacity | FEWER MISSES | -8.64 (-10.55 to -6.72) | +0.00% (+0.00 to +0.00) | +0.31% (+0.25 to +0.37) |
| controller_update_rate | Robotics Motion Control | capacity | MORE WORK + FASTER + FEWER MISSES | -8.06 (-18.78 to +2.67) | +1.02% (-0.88 to +2.92) | +0.98% (+0.59 to +1.37) |
| storage_dispatch | Energy Storage & Microgrid | capacity | FEWER MISSES | -7.62 (-8.29 to -6.96) | +0.00% (+0.00 to +0.00) | +0.32% (+0.28 to +0.37) |
| volt_watt | Energy Storage & Microgrid | capacity | FEWER MISSES | -7.36 (-8.65 to -6.07) | +0.00% (+0.00 to +0.00) | +0.26% (+0.20 to +0.32) |
| peak_shaving | Energy Storage & Microgrid | capacity | FEWER MISSES | -7.28 (-8.34 to -6.22) | +0.00% (+0.00 to +0.00) | +0.31% (+0.23 to +0.39) |
| io_capacity | Database & Transactions | capacity | MORE WORK + FASTER + FEWER MISSES | -6.89 (-8.90 to -4.88) | +0.35% (+0.06 to +0.63) | +96.73% (+82.65 to +110.81) |
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

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
