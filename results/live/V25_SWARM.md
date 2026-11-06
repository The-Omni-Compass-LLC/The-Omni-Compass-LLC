# Drone swarms, gym-pybullet-drones: the A/B/C three-run table (Omni v25)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

gym-pybullet-drones (University of Toronto) integrates every Crazyflie 2.x quadrotor and flies it with the position controller it ships with; that autopilot at the planner's cruise is native. Omni sits on top of it on one knob, the cruise override, inside the autopilot's own limits, spending tracking slack as speed (`docs/SWARM_PREREGISTRATION.md`). Energy is a declared model from the simulator's own motor constants, the same in both arms, with the avionics draw charged over the whole fleet window. Three separate GitHub runs on the same frozen engine: PyBullet reproduces to about one part in a thousand across GitHub's machines (disclosed in the preregistration's amendment 1, made after the first three runs were seen), so a gauge reads **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; energy is a resource spent, so a rise reads **power given**) when all three runs reproduce to that tolerance and give the same sign, **STEADY, the same** under one part in a billion (nine decimal places), and **the runs differ** when they do not reproduce. A cell whose paired physics trial found a faster mission no cheaper, or not inside the safe tracking error, is listed as nothing for Omni to move; a cell where native itself collides is void, and a collision with Omni-Compass on top is a judged row, any increase a **LOSS** (the preregistration's amendment 2, written before omni-v12's runs). Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Cells in the run |
|---|---|---|---|---:|
| A | 41760291699 | `e391835931e7` | omni-v25 (digest cf56fc0a7b707452, 65 files) | 7 |
| B | 41773750511 | `db6e040b4584` | omni-v25 (digest cf56fc0a7b707452, 65 files) | 7 |
| C | 41788841783 | `0a92e09fe669` | omni-v25 (digest cf56fc0a7b707452, 65 files) | 7 |

## Cells where Omni moved the cruise

### tuning: 5 drones x 4 missions, 3 to 8 m (the tuning swarm); handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 456.1 | 398.4 | -12.66% | -12.74% | -12.74% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 9123 | 7968 | -12.66% | -12.74% | -12.74% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 5.84 | 6.687 | +14.50% | +14.60% | +14.60% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.3574 | 0.3755 | +5.05% | +7.19% | +7.19% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07384 | 0.1158 | +56.85% | +59.49% | +59.49% | **the runs differ** |
| mission time (s) | 18.46 | 15.44 | -16.38% | -16.70% | -16.70% | **the runs differ** |
| seconds airborne per mission | 18.44 | 15.42 | -16.40% | -16.72% | -16.72% | **the runs differ** |
| cruise override, mean | 1 | 1.335 | +33.52% | +34.53% | +34.53% | **the runs differ** |

### long: 20 drones x 4 missions, 8 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 548.5 | 468.9 | -14.50% | -14.50% | -14.50% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 4.388e+04 | 3.751e+04 | -14.50% | -14.50% | -14.50% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 4.857 | 5.681 | +16.96% | +16.96% | +16.96% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.46 | 0.3304 | -28.18% | -28.18% | -28.18% | shown, not judged |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.06622 | 0.1076 | +62.44% | +62.44% | +62.44% | shown, not judged |
| mission time (s) | 23.29 | 18.29 | -21.45% | -21.45% | -21.45% | shown, not judged |
| seconds airborne per mission | 23.27 | 18.27 | -21.47% | -21.47% | -21.47% | shown, not judged |
| cruise override, mean | 1 | 1.395 | +39.55% | +39.55% | +39.55% | shown, not judged |

### long-316: 20 drones x 4 missions, 8 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 548.4 | 454.8 | -17.07% | -17.07% | -17.07% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 4.387e+04 | 3.638e+04 | -17.07% | -17.07% | -17.07% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 4.858 | 5.858 | +20.58% | +20.58% | +20.58% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.3216 | 0.328 | +1.99% | +9.35% | +1.99% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.06567 | 0.1085 | +65.28% | +63.20% | +65.28% | **the runs differ** |
| mission time (s) | 23.29 | 18.3 | -21.44% | -21.11% | -21.44% | **the runs differ** |
| seconds airborne per mission | 23.27 | 18.27 | -21.46% | -21.13% | -21.46% | **the runs differ** |
| cruise override, mean | 1 | 1.394 | +39.45% | +38.58% | +39.45% | **the runs differ** |

### mixed: 20 drones x 4 missions, 3 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 499.3 | 417.8 | -16.32% | -16.20% | -16.20% | **the runs differ** |
| fleet energy over the window (J, declared model) | 3.994e+04 | 3.342e+04 | -16.32% | -16.20% | -16.20% | **the runs differ** |
| missions per charge at the autopilot's reserve | 5.336 | 6.377 | +19.51% | +19.33% | +19.33% | **the runs differ** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.2999 | 0.3223 | +7.45% | +8.52% | +8.52% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07449 | 0.1171 | +57.17% | +56.76% | +56.76% | shown, not judged |
| mission time (s) | 18.19 | 15.19 | -16.50% | -16.62% | -16.62% | **the runs differ** |
| seconds airborne per mission | 18.17 | 15.17 | -16.52% | -16.64% | -16.64% | **the runs differ** |
| cruise override, mean | 1 | 1.344 | +34.39% | +34.70% | +34.70% | **the runs differ** |

### mixed-315: 20 drones x 4 missions, 3 to 8 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 451.7 | 387.2 | -14.27% | -14.27% | -14.28% | **GAIN in all three of our runs** |
| fleet energy over the window (J, declared model) | 3.614e+04 | 3.098e+04 | -14.27% | -14.27% | -14.28% | **GAIN in all three of our runs** |
| missions per charge at the autopilot's reserve | 5.898 | 6.879 | +16.65% | +16.65% | +16.66% | **GAIN in all three of our runs** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.3043 | 0.3145 | +3.34% | +3.34% | -5.28% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07569 | 0.1171 | +54.65% | +54.65% | +54.75% | shown, not judged |
| mission time (s) | 17.68 | 14.91 | -15.67% | -15.67% | -15.67% | shown, not judged |
| seconds airborne per mission | 17.66 | 14.89 | -15.69% | -15.69% | -15.68% | shown, not judged |
| cruise override, mean | 1 | 1.323 | +32.32% | +32.32% | +32.63% | **the runs differ** |

### short: 20 drones x 4 missions, 3 to 3 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 337.7 | 320 | -5.26% | -5.09% | -5.26% | **the runs differ** |
| fleet energy over the window (J, declared model) | 2.702e+04 | 2.56e+04 | -5.26% | -5.09% | -5.26% | **the runs differ** |
| missions per charge at the autopilot's reserve | 7.888 | 8.326 | +5.55% | +5.37% | +5.55% | **the runs differ** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.3047 | 0.3256 | +6.87% | +5.53% | +6.87% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.08571 | 0.1244 | +45.20% | +47.77% | +45.20% | shown, not judged |
| mission time (s) | 13.29 | 12.19 | -8.28% | -8.52% | -8.28% | **the runs differ** |
| seconds airborne per mission | 13.27 | 12.17 | -8.29% | -8.53% | -8.29% | **the runs differ** |
| cruise override, mean | 1 | 1.26 | +25.98% | +26.28% | +25.98% | **the runs differ** |

### short-314: 20 drones x 4 missions, 3 to 3 m; handed back: yes

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 337.7 | 321 | -4.96% | -5.26% | -5.26% | **the runs differ** |
| fleet energy over the window (J, declared model) | 2.702e+04 | 2.568e+04 | -4.96% | -5.26% | -5.26% | **the runs differ** |
| missions per charge at the autopilot's reserve | 7.889 | 8.3 | +5.21% | +5.55% | +5.55% | **the runs differ** |
| missions over their deadline (share) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| drones that broke the battery reserve | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | +0.000 | +0.000 | STEADY, the same |
| closest two drones ever came (m) | 0.3152 | 0.3028 | -3.91% | +0.52% | +0.52% | **the runs differ** |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.08513 | 0.1291 | +51.65% | +50.37% | +50.37% | shown, not judged |
| mission time (s) | 13.29 | 12.1 | -8.96% | -8.68% | -8.68% | **the runs differ** |
| seconds airborne per mission | 13.27 | 12.08 | -8.97% | -8.69% | -8.69% | **the runs differ** |
| cruise override, mean | 1 | 1.283 | +28.25% | +28.04% | +28.04% | **the runs differ** |

## Across the untouched cells Omni moved

| Gauge | GAIN in all three of our runs | LOSS in all three of our runs | Power given in all three of our runs | STEADY | The runs differ |
|---|---:|---:|---:|---:|---:|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 3 | 0 | 0 | 0 | 3 |
| fleet energy over the window (J, declared model) | 3 | 0 | 0 | 0 | 3 |
| missions per charge at the autopilot's reserve | 3 | 0 | 0 | 0 | 3 |
| missions over their deadline (share) | 0 | 0 | 0 | 6 | 0 |
| drones that broke the battery reserve | 0 | 0 | 0 | 6 | 0 |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | 0 | 6 | 0 |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | 0 | 6 | 0 |

## Cells where the paired trial left the cruise native: nothing for Omni to move

In native mode, before the counted missions, one mission at the planner's cruise and one at 1.25 x showed a faster mission no cheaper on the simulator's own figures, or not inside the safe tracking error, so Omni left the cruise at the planner's and both arms are the same.

| Cell | Energy a mission at the planner's cruise (J) | At the trial speed (J) | Reproduced over A, B, C |
|---|---:|---:|---|

## Void cells

| Cell | Why |
|---|---|

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
