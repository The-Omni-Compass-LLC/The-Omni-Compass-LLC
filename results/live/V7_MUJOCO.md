# Robot arms, MuJoCo Menagerie: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MuJoCo (Google DeepMind) integrates each arm; MuJoCo Menagerie supplies the robot as its maker describes it, with the position servos it ships with as native. Omni sits on top of that servo on one knob, the speed override, inside the task's takt (`docs/ROBOTICS_PREREGISTRATION.md`). Energy is a declared model from MuJoCo's own torques and velocities, the same in both arms, with the standing draw charged for the whole takt. Three separate GitHub runs on the same frozen engine: MuJoCo is deterministic, so a gauge reads **GAIN** or **LOSS in all three of our runs** when all three runs give the same sign, judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**), **STEADY, the same** under one part in a million, and **the runs differ** when they do not reproduce. A robot whose paired physics trial found a slower cycle no cheaper is listed as nothing for Omni to move. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Robots in the run |
|---|---|---|---|---:|
| A | 38935456828 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 3 |
| B | 38947636137 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 3 |
| C | 38959431162 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 3 |

## Robots where Omni moved the override

### kinova_gen3: 7 joints, planned 8 s, takt 12 s, 10 cycles per arm; handed back every cycle: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per takt (J, declared model: motion plus the standing draw for the whole takt) | 482.3 | 478.3 | -0.82% | -0.82% | -0.82% | **GAIN in all three of our runs** |
| copper heating per cycle (J, I²R, declared model) | 13.68 | 12.14 | -11.27% | -11.27% | -11.27% | **GAIN in all three of our runs** |
| mechanical work per cycle (J) | 36.6 | 34.17 | -6.62% | -6.62% | -6.62% | **GAIN in all three of our runs** |
| standing draw per takt (J, declared model; the same in both arms) | 432 | 432 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| peak joint torque (N m) | 21.74 | 15.52 | -28.63% | -28.63% | -28.63% | **GAIN in all three of our runs** |
| mean |torque| (N m) | 2.687 | 2.338 | -13.01% | -13.01% | -13.01% | **GAIN in all three of our runs** |
| cycle time (s) | 8.01 | 10.21 | +27.47% | +27.47% | +27.47% | shown, not judged |
| cycles over the time line (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| tracking error, RMS (rad) | 0.01707 | 0.01344 | -21.28% | -21.28% | -21.28% | **GAIN in all three of our runs** |
| end-point error at the waypoints (rad) | 0.002418 | 0.002153 | -10.97% | -10.97% | -10.97% | **GAIN in all three of our runs** |
| speed override, mean | 1 | 0.7839 | -21.61% | -21.61% | -21.61% | shown, not judged |

## Across the robots Omni moved

| Gauge | GAIN in all three of our runs | LOSS in all three of our runs | Power given in all three of our runs | STEADY | The runs differ |
|---|---:|---:|---:|---:|---:|
| energy per takt (J, declared model: motion plus the standing draw for the whole takt) | 1 | 0 | 0 | 0 | 0 |
| copper heating per cycle (J, I²R, declared model) | 1 | 0 | 0 | 0 | 0 |
| mechanical work per cycle (J) | 1 | 0 | 0 | 0 | 0 |
| standing draw per takt (J, declared model; the same in both arms) | 0 | 0 | 0 | 1 | 0 |
| peak joint torque (N m) | 1 | 0 | 0 | 0 | 0 |
| mean |torque| (N m) | 1 | 0 | 0 | 0 | 0 |
| cycles over the time line (share) | 0 | 0 | 0 | 1 | 0 |
| tracking error, RMS (rad) | 1 | 0 | 0 | 0 | 0 |
| end-point error at the waypoints (rad) | 1 | 0 | 0 | 0 | 0 |

## Robots where the paired trial left the override native: nothing for Omni to move

In native mode, before the counted cycles, one cycle at full speed and one at override 0.8 showed a slower cycle no cheaper on the robot's own figures (the gravity-holding torque is paid for longer), so Omni left the override at 1.0 and both arms are the same. Reproduced over A, B, C is whether the three runs agree on every gauge.

| Robot | Full-speed cycle (J, motion) | Override 0.8 cycle (J, motion) | Reproduced over A, B, C |
|---|---:|---:|---|
| kuka_iiwa_14 | 3157.3 | 3757.3 | yes |
| universal_robots_ur5e | 189.9 | 210.5 | yes |

## Robots the task could not be run on

| Robot | The runner's reason |
|---|---|

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
