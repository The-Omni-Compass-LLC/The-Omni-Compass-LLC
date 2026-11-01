# Drone swarms: Omni-Compass on top of each drone's own autopilot (gym-pybullet-drones, Crazyflie 2.x)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

native: every drone's shipped position controller at the planner's cruise; omni: the same, with the compass law on the cruise override inside the autopilot's limits, spending tracking slack as speed. Energy is a declared model (evidence class S) computed the same way for both arms. A cell where native itself collides is void; a collision with Omni-Compass on top is a judged row, any increase a LOSS (amendment 2). Every row is reported.

## mixed-315: 20 drones x 4 missions, 3 to 8 m

Paired physics trial (native, uncounted): 471 J a mission at the planner's cruise, 420 J at 1.25 x; a faster mission is cheaper and inside the safe error, so omni may move the cruise.

| Gauge | native | omni | change | direction |
|---|---:|---:|---:|---|
| energy per mission (J, declared model: motors and avionics over the fleet window) | 451.7 | 387.2 | -14.27% | spent |
| fleet energy over the window (J, declared model) | 3.614e+04 | 3.098e+04 | -14.27% | spent |
| missions per charge at the autopilot's reserve | 5.898 | 6.879 | +16.65% | higher |
| missions over their deadline (share) | 0 | 0 | +0.000 | never more |
| drones that broke the battery reserve | 0 | 0 | +0.000 | never more |
| control ticks with two drones under half the keep-out apart (near misses) | 0 | 0 | +0.000 | never more |
| control ticks with two drones under two collision radii (collisions) | 0 | 0 | +0.000 | never more |
| closest two drones ever came (m) | 0.3043 | 0.3145 | +3.34% | shown |
| tracking error, RMS (m; the compass's reading, held inside its band) | 0.07569 | 0.1171 | +54.65% | shown |
| mission time (s) | 17.68 | 14.91 | -15.67% | shown |
| seconds airborne per mission | 17.66 | 14.89 | -15.69% | shown |
| cruise override, mean | 1 | 1.323 | +32.32% | shown |

Missions flown: native 80, omni 80; cut off: 0 / 0; every override handed back: native True, omni True; collisions 0 / 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
