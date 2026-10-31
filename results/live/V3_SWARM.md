# Drone swarms, gym-pybullet-drones: the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

gym-pybullet-drones (University of Toronto) integrates every Crazyflie 2.x quadrotor and flies it with the position controller it ships with; that autopilot at the planner's cruise is native. Omni sits on top of it on one knob, the cruise override, inside the autopilot's own limits, spending tracking slack as speed (`docs/SWARM_PREREGISTRATION.md`). Energy is a declared model from the simulator's own motor constants, the same in both arms, with the avionics draw charged over the whole fleet window. Three separate GitHub runs on the same frozen engine: PyBullet reproduces to about one part in a thousand across GitHub's machines (disclosed in the preregistration's amendment 1, made after the first three runs were seen), so a gauge reads **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)) when all three runs reproduce to that tolerance and give the same sign, **STEADY, the same** under one part in a million, and **the runs differ** when they do not reproduce. A cell whose paired physics trial found a faster mission no cheaper, or not inside the safe tracking error, is listed as nothing for Omni to move; a cell with a collision in either arm is void. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Cells in the run |
|---|---|---|---|---:|
| A | 38013432603 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 38013437505 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 38013442794 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## Cells where Omni moved the cruise

### tuning: 5 drones x 4 missions, 3 to 8 m (the tuning swarm); handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 456.3 | 384.3 | -15.77% | -15.77% | -15.83% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 9125 | 7686 | -15.77% | -15.77% | -15.83% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 5.839 | 6.932 | +18.72% | +18.72% | +18.80% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.3717 | 0.1829 | -50.80% | -50.80% | -45.49% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07381 | 0.1409 | +90.85% | +90.85% | +87.59% | **the runs differ** |
| mission time (s) | 18.46 | 14.54 | -21.22% | -21.22% | -21.22% | shown, not judged |
| seconds airborne per mission | 18.44 | 14.52 | -21.24% | -21.24% | -21.24% | shown, not judged |
| cruise override, mean | 1 | 1.488 | +48.84% | +48.84% | +48.65% | **the runs differ** |

### long: 20 drones x 4 missions, 8 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 548.4 | 439.6 | -19.84% | -19.79% | -19.79% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 4.387e+04 | 3.517e+04 | -19.84% | -19.79% | -19.79% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 4.858 | 6.06 | +24.76% | +24.67% | +24.67% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.451 | 0.4442 | -1.50% | -5.68% | -5.68% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.0659 | 0.1264 | +91.84% | +93.16% | +93.16% | **the runs differ** |
| mission time (s) | 23.29 | 17.43 | -25.17% | -25.21% | -25.21% | shown, not judged |
| seconds airborne per mission | 23.27 | 17.41 | -25.19% | -25.23% | -25.23% | shown, not judged |
| cruise override, mean | 1 | 1.516 | +51.65% | +51.98% | +51.98% | **the runs differ** |

### mixed: 20 drones x 4 missions, 3 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 499.3 | 410.3 | -17.82% | -17.79% | -17.79% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 3.994e+04 | 3.282e+04 | -17.82% | -17.79% | -17.79% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 5.336 | 6.493 | +21.68% | +21.64% | +21.64% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.3003 | 0.1608 | -46.46% | -41.96% | -41.96% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07469 | 0.1367 | +83.00% | +86.02% | +86.02% | **the runs differ** |
| mission time (s) | 18.19 | 14.37 | -21.01% | -20.94% | -20.94% | shown, not judged |
| seconds airborne per mission | 18.17 | 14.35 | -21.03% | -20.96% | -20.96% | shown, not judged |
| cruise override, mean | 1 | 1.486 | +48.58% | +48.32% | +48.32% | **the runs differ** |

### short: 20 drones x 4 missions, 3 to 3 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 337.7 | 312.6 | -7.42% | -7.43% | -7.42% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 2.702e+04 | 2.501e+04 | -7.42% | -7.43% | -7.42% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 7.888 | 8.521 | +8.02% | +8.03% | +8.02% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.307 | 0.2264 | -26.26% | -48.77% | -26.26% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.08475 | 0.1524 | +79.79% | +77.74% | +79.79% | shown, not judged |
| mission time (s) | 13.29 | 11.45 | -13.84% | -13.87% | -13.84% | shown, not judged |
| seconds airborne per mission | 13.27 | 11.43 | -13.87% | -13.89% | -13.87% | shown, not judged |
| cruise override, mean | 1 | 1.445 | +44.53% | +44.54% | +44.53% | shown, not judged |

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
