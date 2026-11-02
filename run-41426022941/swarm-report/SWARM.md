# Drone swarms: Omni-Compass on top of each drone's own autopilot (gym-pybullet-drones, Crazyflie 2.x)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

native: every drone's shipped position controller at the planner's cruise; omni: the same, with the compass law on the cruise override inside the autopilot's limits, spending tracking slack as speed. Energy is a declared model (evidence class S) computed the same way for both arms. A cell where native itself collides is void; a collision with Omni-Compass on top is a judged row, any increase a LOSS (amendment 2). Every row is reported.

## long-316: 20 drones x 4 missions, 8 to 8 m

Paired physics trial (native, uncounted): 548 J a mission at the planner's cruise, 487 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 548.4 | 454.8 | -17.07% | spent |
| fleet energy over the window (J, declared model) | 4.387e+04 | 3.638e+04 | -17.07% | spent |
| missions per charge at the autopilot's reserve | 4.858 | 5.858 | +20.58% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.3216 | 0.328 | +1.99% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.06567 | 0.1085 | +65.28% | shown |
| mission time (s) | 23.29 | 18.3 | -21.44% | shown |
| seconds airborne per mission | 23.27 | 18.27 | -21.46% | shown |
| cruise override, mean | 1 | 1.394 | +39.45% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

## long: 20 drones x 4 missions, 8 to 8 m

Paired physics trial (native, uncounted): 548 J a mission at the planner's cruise, 487 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 548.5 | 468.9 | -14.50% | spent |
| fleet energy over the window (J, declared model) | 4.388e+04 | 3.751e+04 | -14.50% | spent |
| missions per charge at the autopilot's reserve | 4.857 | 5.681 | +16.96% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.46 | 0.3304 | -28.18% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.06622 | 0.1076 | +62.44% | shown |
| mission time (s) | 23.29 | 18.29 | -21.45% | shown |
| seconds airborne per mission | 23.27 | 18.27 | -21.47% | shown |
| cruise override, mean | 1 | 1.395 | +39.55% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

## mixed-315: 20 drones x 4 missions, 3 to 8 m

Paired physics trial (native, uncounted): 471 J a mission at the planner's cruise, 420 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 451.7 | 387.2 | -14.28% | spent |
| fleet energy over the window (J, declared model) | 3.613e+04 | 3.097e+04 | -14.28% | spent |
| missions per charge at the autopilot's reserve | 5.898 | 6.881 | +16.66% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.3037 | 0.2877 | -5.28% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07537 | 0.1166 | +54.75% | shown |
| mission time (s) | 17.68 | 14.91 | -15.67% | shown |
| seconds airborne per mission | 17.66 | 14.89 | -15.68% | shown |
| cruise override, mean | 1 | 1.326 | +32.63% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

## mixed: 20 drones x 4 missions, 3 to 8 m

Paired physics trial (native, uncounted): 491 J a mission at the planner's cruise, 441 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 499.3 | 418.4 | -16.20% | spent |
| fleet energy over the window (J, declared model) | 3.994e+04 | 3.347e+04 | -16.20% | spent |
| missions per charge at the autopilot's reserve | 5.336 | 6.367 | +19.33% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.3003 | 0.3259 | +8.52% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07469 | 0.1171 | +56.76% | shown |
| mission time (s) | 18.19 | 15.17 | -16.62% | shown |
| seconds airborne per mission | 18.17 | 15.15 | -16.64% | shown |
| cruise override, mean | 1 | 1.347 | +34.70% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

## short-314: 20 drones x 4 missions, 3 to 3 m

Paired physics trial (native, uncounted): 337 J a mission at the planner's cruise, 317 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 337.7 | 321 | -4.96% | spent |
| fleet energy over the window (J, declared model) | 2.702e+04 | 2.568e+04 | -4.96% | spent |
| missions per charge at the autopilot's reserve | 7.889 | 8.3 | +5.21% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.3152 | 0.3028 | -3.91% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.08513 | 0.1291 | +51.65% | shown |
| mission time (s) | 13.29 | 12.1 | -8.96% | shown |
| seconds airborne per mission | 13.27 | 12.08 | -8.97% | shown |
| cruise override, mean | 1 | 1.283 | +28.25% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

## short: 20 drones x 4 missions, 3 to 3 m

Paired physics trial (native, uncounted): 337 J a mission at the planner's cruise, 318 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 337.7 | 320.5 | -5.09% | spent |
| fleet energy over the window (J, declared model) | 2.702e+04 | 2.564e+04 | -5.09% | spent |
| missions per charge at the autopilot's reserve | 7.888 | 8.312 | +5.37% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.307 | 0.324 | +5.53% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.08475 | 0.1252 | +47.77% | shown |
| mission time (s) | 13.29 | 12.16 | -8.52% | shown |
| seconds airborne per mission | 13.27 | 12.13 | -8.53% | shown |
| cruise override, mean | 1 | 1.263 | +26.28% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

## tuning: 5 drones x 4 missions, 3 to 8 m (the tuning swarm)

Paired physics trial (native, uncounted): 498 J a mission at the planner's cruise, 446 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 456.3 | 398.1 | -12.74% | spent |
| fleet energy over the window (J, declared model) | 9125 | 7962 | -12.74% | spent |
| missions per charge at the autopilot's reserve | 5.839 | 6.692 | +14.60% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.3717 | 0.3984 | +7.19% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07381 | 0.1177 | +59.49% | shown |
| mission time (s) | 18.46 | 15.38 | -16.70% | shown |
| seconds airborne per mission | 18.44 | 15.36 | -16.72% | shown |
| cruise override, mean | 1 | 1.345 | +34.53% | shown |

Missions flown: native 20, omni 20; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
