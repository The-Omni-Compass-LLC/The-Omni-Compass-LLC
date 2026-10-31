# Drone swarms, gym-pybullet-drones: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

gym-pybullet-drones (University of Toronto) integrates every Crazyflie 2.x quadrotor and flies it with the position controller it ships with; that autopilot at the planner's cruise is native. Omni sits on top of it on one knob, the cruise override, inside the autopilot's own limits, spending tracking slack as speed (`docs/SWARM_PREREGISTRATION.md`). Energy is a declared model from the simulator's own motor constants, the same in both arms, with the avionics draw charged over the whole fleet window. Three separate GitHub runs on the same frozen engine: PyBullet reproduces to about one part in a thousand across GitHub's machines (disclosed in the preregistration's amendment 1, made after the first three runs were seen), so a gauge reads **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; energy is a resource spent, so a rise reads **power given**) when all three runs reproduce to that tolerance and give the same sign, **STEADY, the same** under one part in a million, and **the runs differ** when they do not reproduce. A cell whose paired physics trial found a faster mission no cheaper, or not inside the safe tracking error, is listed as nothing for Omni to move; a cell with a collision in either arm is void. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Cells in the run |
|---|---|---|---|---:|
| A | 38937547494 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| B | 38949624815 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| C | 38959451476 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |

## Cells where Omni moved the cruise

### tuning: 5 drones x 4 missions, 3 to 8 m (the tuning swarm); handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 456.1 | 384 | -15.83% | -15.77% | -15.83% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 9123 | 7679 | -15.83% | -15.77% | -15.83% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 5.84 | 6.938 | +18.80% | +18.72% | +18.80% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.3574 | 0.1948 | -45.49% | -50.80% | -45.49% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07384 | 0.1385 | +87.59% | +90.85% | +87.59% | **the runs differ** |
| mission time (s) | 18.46 | 14.54 | -21.22% | -21.22% | -21.22% | shown, not judged |
| seconds airborne per mission | 18.44 | 14.52 | -21.24% | -21.24% | -21.24% | shown, not judged |
| cruise override, mean | 1 | 1.487 | +48.65% | +48.84% | +48.65% | **the runs differ** |

### long: 20 drones x 4 missions, 8 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 548.4 | 439.6 | -19.84% | -19.84% | -19.79% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 4.387e+04 | 3.517e+04 | -19.84% | -19.84% | -19.79% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 4.858 | 6.06 | +24.76% | +24.76% | +24.67% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.451 | 0.4442 | -1.50% | -1.50% | -5.68% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.0659 | 0.1264 | +91.84% | +91.84% | +93.16% | **the runs differ** |
| mission time (s) | 23.29 | 17.43 | -25.17% | -25.17% | -25.21% | shown, not judged |
| seconds airborne per mission | 23.27 | 17.41 | -25.19% | -25.19% | -25.23% | shown, not judged |
| cruise override, mean | 1 | 1.516 | +51.65% | +51.65% | +51.98% | **the runs differ** |

### mixed: 20 drones x 4 missions, 3 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 499.3 | 410.5 | -17.79% | -17.79% | -17.82% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 3.994e+04 | 3.284e+04 | -17.79% | -17.79% | -17.82% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 5.336 | 6.49 | +21.64% | +21.64% | +21.68% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.2999 | 0.1741 | -41.96% | -41.96% | -46.46% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07449 | 0.1386 | +86.02% | +86.02% | +83.00% | **the runs differ** |
| mission time (s) | 18.19 | 14.38 | -20.94% | -20.94% | -21.01% | shown, not judged |
| seconds airborne per mission | 18.17 | 14.36 | -20.96% | -20.96% | -21.03% | shown, not judged |
| cruise override, mean | 1 | 1.483 | +48.32% | +48.32% | +48.58% | **the runs differ** |

### short: 20 drones x 4 missions, 3 to 3 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 337.7 | 312.6 | -7.43% | -7.43% | -7.43% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 2.702e+04 | 2.501e+04 | -7.43% | -7.43% | -7.43% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 7.888 | 8.522 | +8.03% | +8.03% | +8.03% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.3047 | 0.1561 | -48.77% | -48.77% | -48.77% | shown, not judged |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.08571 | 0.1523 | +77.74% | +77.74% | +77.74% | shown, not judged |
| mission time (s) | 13.29 | 11.44 | -13.87% | -13.87% | -13.87% | shown, not judged |
| seconds airborne per mission | 13.27 | 11.42 | -13.89% | -13.89% | -13.89% | shown, not judged |
| cruise override, mean | 1 | 1.445 | +44.54% | +44.54% | +44.54% | shown, not judged |

## Across the untouched cells Omni moved

| Gauge | GAIN in all three of our runs | LOSS in all three of our runs | Power given in all three of our runs | STEADY | The runs differ |
|---|---:|---:|---:|---:|---:|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 3 | 0 | 0 | 0 | 0 |
| fleet energy over the window (J, declared model) | 3 | 0 | 0 | 0 | 0 |
| missions per charge at the autopilot's reserve | 3 | 0 | 0 | 0 | 0 |
| missions over their deadline (share) | 0 | 0 | 0 | 3 | 0 |
| drones that broke the battery reserve | 0 | 0 | 0 | 3 | 0 |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | 0 | 3 | 0 |

## Cells where the paired trial left the cruise native: nothing for Omni to move

In native mode, before the counted missions, one mission at the planner's cruise and one at 1.25 x showed a faster mission no cheaper on the simulator's own figures, or not inside the safe tracking error, so Omni left the cruise at the planner's and both arms are the same.

| Cell | Energy a mission at the planner's cruise (J) | At the trial speed (J) | Reproduced over A, B, C |
|---|---:|---:|---|

## Void cells

| Cell | Why |
|---|---|

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
