# Drone swarms: Omni-Compass on top of each drone's own autopilot (gym-pybullet-drones, Crazyflie 2.x)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

native: every drone's shipped position controller at the planner's cruise; omni: the same, with the compass law on the cruise override inside the autopilot's limits, spending tracking slack as speed. Energy is a declared model (evidence class S) computed the same way for both arms. A cell with a collision in either arm is void. Every row is reported.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
