# Drone swarms, gym-pybullet-drones: the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

gym-pybullet-drones (University of Toronto) integrates every Crazyflie 2.x quadrotor and flies it with the position controller it ships with; that autopilot at the planner's cruise is native. Omni sits on top of it on one knob, the cruise override, inside the autopilot's own limits, spending tracking slack as speed (`docs/SWARM_PREREGISTRATION.md`). Energy is a declared model from the simulator's own motor constants, the same in both arms, with the avionics draw charged over the whole fleet window. Three separate GitHub runs on the same frozen engine: PyBullet reproduces to about one part in a thousand across GitHub's machines (disclosed in the preregistration's amendment 1, made after the first three runs were seen), so a gauge reads **confirmed better** or **confirmed WORSE** when all three runs reproduce to that tolerance and give the same sign, **same** under one part in a million, and **the runs differ** when they do not reproduce. A cell whose paired physics trial found a faster mission no cheaper, or not inside the safe tracking error, is listed as nothing for Omni to move; a cell with a collision in either arm is void. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Cells in the run |
|---|---|---|---|---:|
| A | 37677964512 | `ec6d992f269a` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 37677984739 | `ec6d992f269a` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 37678005151 | `ec6d992f269a` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## Cells where Omni moved the cruise

### tuning: 5 drones x 4 missions, 3 to 8 m (the tuning swarm); handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 456.1 | 384 | -15.83% | -15.77% | -15.83% | **confirmed better** |
| fleet energy over the window (J, declared model) | 9123 | 7679 | -15.83% | -15.77% | -15.83% | **confirmed better** |
| missions per charge at the autopilot's reserve | 5.84 | 6.938 | +18.80% | +18.72% | +18.80% | **confirmed better** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| closest two drones ever came (m) | 0.3574 | 0.1948 | -45.49% | -50.80% | -45.49% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07384 | 0.1385 | +87.59% | +90.85% | +87.59% | **the runs differ** |
| mission time (s) | 18.46 | 14.54 | -21.22% | -21.22% | -21.22% | shown, not judged |
| seconds airborne per mission | 18.44 | 14.52 | -21.24% | -21.24% | -21.24% | shown, not judged |
| cruise override, mean | 1 | 1.487 | +48.65% | +48.84% | +48.65% | **the runs differ** |

### long: 20 drones x 4 missions, 8 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 548.5 | 439.9 | -19.79% | -19.84% | -19.84% | **confirmed better** |
| fleet energy over the window (J, declared model) | 4.388e+04 | 3.519e+04 | -19.79% | -19.84% | -19.84% | **confirmed better** |
| missions per charge at the autopilot's reserve | 4.857 | 6.056 | +24.67% | +24.76% | +24.76% | **confirmed better** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| closest two drones ever came (m) | 0.46 | 0.4339 | -5.68% | -1.50% | -1.50% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.06622 | 0.1279 | +93.16% | +91.84% | +91.84% | **the runs differ** |
| mission time (s) | 23.29 | 17.42 | -25.21% | -25.17% | -25.17% | shown, not judged |
| seconds airborne per mission | 23.27 | 17.4 | -25.23% | -25.19% | -25.19% | shown, not judged |
| cruise override, mean | 1 | 1.52 | +51.98% | +51.65% | +51.65% | **the runs differ** |

### mixed: 20 drones x 4 missions, 3 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 499.3 | 410.5 | -17.79% | -17.79% | -17.82% | **confirmed better** |
| fleet energy over the window (J, declared model) | 3.994e+04 | 3.284e+04 | -17.79% | -17.79% | -17.82% | **confirmed better** |
| missions per charge at the autopilot's reserve | 5.336 | 6.49 | +21.64% | +21.64% | +21.68% | **confirmed better** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| closest two drones ever came (m) | 0.2999 | 0.1741 | -41.96% | -41.96% | -46.46% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07449 | 0.1386 | +86.02% | +86.02% | +83.00% | **the runs differ** |
| mission time (s) | 18.19 | 14.38 | -20.94% | -20.94% | -21.01% | shown, not judged |
| seconds airborne per mission | 18.17 | 14.36 | -20.96% | -20.96% | -21.03% | shown, not judged |
| cruise override, mean | 1 | 1.483 | +48.32% | +48.32% | +48.58% | **the runs differ** |

### short: 20 drones x 4 missions, 3 to 3 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 337.7 | 312.6 | -7.43% | -7.43% | -7.43% | **confirmed better** |
| fleet energy over the window (J, declared model) | 2.702e+04 | 2.501e+04 | -7.43% | -7.43% | -7.43% | **confirmed better** |
| missions per charge at the autopilot's reserve | 7.888 | 8.522 | +8.03% | +8.03% | +8.03% | **confirmed better** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | same |
| closest two drones ever came (m) | 0.3047 | 0.1561 | -48.77% | -48.77% | -48.77% | shown, not judged |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.08571 | 0.1523 | +77.74% | +77.74% | +77.74% | shown, not judged |
| mission time (s) | 13.29 | 11.44 | -13.87% | -13.87% | -13.87% | shown, not judged |
| seconds airborne per mission | 13.27 | 11.42 | -13.89% | -13.89% | -13.89% | shown, not judged |
| cruise override, mean | 1 | 1.445 | +44.54% | +44.54% | +44.54% | shown, not judged |

## Across the untouched cells Omni moved

| Gauge | Confirmed better | Confirmed worse | Same | The runs differ |
|---|---:|---|---:|---:|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 3 | 0 | 0 | 0 |
| fleet energy over the window (J, declared model) | 3 | 0 | 0 | 0 |
| missions per charge at the autopilot's reserve | 3 | 0 | 0 | 0 |
| missions over their deadline (share) | 0 | 0 | 3 | 0 |
| drones that broke the battery reserve | 0 | 0 | 3 | 0 |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | 3 | 0 |

## Cells where the paired trial left the cruise native: nothing for Omni to move

In native mode, before the counted missions, one mission at the planner's cruise and one at 1.25 x showed a faster mission no cheaper on the simulator's own figures, or not inside the safe tracking error, so Omni left the cruise at the planner's and both arms are the same.

| Cell | Energy a mission at the planner's cruise (J) | At the trial speed (J) | Reproduced over A, B, C |
|---|---:|---:|---|

## Void cells

| Cell | Why |
|---|---|

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
