# Drone swarms: Omni-Compass on top of each drone's own autopilot (gym-pybullet-drones, Crazyflie 2.x)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

native: every drone's shipped position controller at the planner's cruise; omni: the same, with the compass law on the cruise override inside the autopilot's limits, spending tracking slack as speed. Energy is a declared model (evidence class S) computed the same way for both arms. A cell with a collision in either arm is void. Every row is reported.

## long: 20 drones x 4 missions, 8 to 8 m

Paired physics trial (native, uncounted): 548 J a mission at the planner's cruise, 487 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 548.5 | 439.9 | -19.79% | spent |
| fleet energy over the window (J, declared model) | 4.388e+04 | 3.519e+04 | -19.79% | spent |
| missions per charge at the autopilot's reserve | 4.857 | 6.056 | +24.67% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.46 | 0.4339 | -5.68% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.06622 | 0.1279 | +93.16% | shown |
| mission time (s) | 23.29 | 17.42 | -25.21% | shown |
| seconds airborne per mission | 23.27 | 17.4 | -25.23% | shown |
| cruise override, mean | 1 | 1.52 | +51.98% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

## mixed: 20 drones x 4 missions, 3 to 8 m

Paired physics trial (native, uncounted): 491 J a mission at the planner's cruise, 441 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 499.3 | 410.3 | -17.82% | spent |
| fleet energy over the window (J, declared model) | 3.994e+04 | 3.282e+04 | -17.82% | spent |
| missions per charge at the autopilot's reserve | 5.336 | 6.493 | +21.68% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.3003 | 0.1608 | -46.46% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07469 | 0.1367 | +83.00% | shown |
| mission time (s) | 18.19 | 14.37 | -21.01% | shown |
| seconds airborne per mission | 18.17 | 14.35 | -21.03% | shown |
| cruise override, mean | 1 | 1.486 | +48.58% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

## short: 20 drones x 4 missions, 3 to 3 m

Paired physics trial (native, uncounted): 337 J a mission at the planner's cruise, 317 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 337.7 | 312.6 | -7.43% | spent |
| fleet energy over the window (J, declared model) | 2.702e+04 | 2.501e+04 | -7.43% | spent |
| missions per charge at the autopilot's reserve | 7.888 | 8.522 | +8.03% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.3047 | 0.1561 | -48.77% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.08571 | 0.1523 | +77.74% | shown |
| mission time (s) | 13.29 | 11.44 | -13.87% | shown |
| seconds airborne per mission | 13.27 | 11.42 | -13.89% | shown |
| cruise override, mean | 1 | 1.445 | +44.54% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

## tuning: 5 drones x 4 missions, 3 to 8 m (the tuning swarm)

Paired physics trial (native, uncounted): 498 J a mission at the planner's cruise, 447 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 456.1 | 384 | -15.83% | spent |
| fleet energy over the window (J, declared model) | 9123 | 7679 | -15.83% | spent |
| missions per charge at the autopilot's reserve | 5.84 | 6.938 | +18.80% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.3574 | 0.1948 | -45.49% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07384 | 0.1385 | +87.59% | shown |
| mission time (s) | 18.46 | 14.54 | -21.22% | shown |
| seconds airborne per mission | 18.44 | 14.52 | -21.24% | shown |
| cruise override, mean | 1 | 1.487 | +48.65% | shown |

Missions flown: native 20, omni 20; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
