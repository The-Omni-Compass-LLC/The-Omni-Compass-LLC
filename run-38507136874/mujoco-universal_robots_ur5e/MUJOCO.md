# Omni-Compass on top of a robot arm's own servos (MuJoCo, MuJoCo Menagerie)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MuJoCo (Google DeepMind) integrates each arm; MuJoCo Menagerie supplies the robot as its maker describes it, with the position servos the model ships with. Native: that servo tracks a pick-and-place cycle at its planned speed. Omni: the same servo and trajectory with the compass law on the speed override, inside the cycle's time line (`docs/ROBOTICS_PREREGISTRATION.md`). Energy is a declared model from MuJoCo's own torques and velocities, the same in both arms. Evidence class: S, our model on an independent simulator. Each reading is GAIN, EVEN or LOSS by what the gauge is for, never by its sign; energy, force and copper heating are resources spent, so a rise reads power given (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). Every row is shown, LOSS included.

## universal_robots_ur5e: 6 joints, 10 cycles per arm, planned 16 s (segment 4.0 s, the fastest the robot's own servo tracks within 0.05 rad: 0.0442), takt 24 s

The task: 4 segments between joint-space waypoints 25% of each joint's own range either side of home (at most 0.6 rad), a minimum-jerk trajectory; the same for both arms.

Paired physics trial (native mode, not counted): a cycle at full speed cost 2349.9 J, at override 0.8 2370.5 J, standing draw 90.0 W included: **a slower cycle is not cheaper, so omni leaves the override native: nothing for Omni to move.**

Omni handed the override back at the end of every cycle: yes.

| Gauge | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy per takt (J, declared model: motion plus the standing draw for the whole takt) | 2350 | 2350 | +0.00% | EVEN, the same |
| copper heating per cycle (J, I²R, declared model) | 93.19 | 93.19 | +0.00% | EVEN, the same |
| mechanical work per cycle (J) | 96.75 | 96.75 | +0.00% | EVEN, the same |
| standing draw per takt (J, declared model; the same in both arms) | 2160 | 2160 | +0.00% | EVEN, the same |
| peak joint torque (N m) | 37.71 | 37.71 | +0.00% | EVEN, the same |
| mean |torque| (N m) | 5.495 | 5.495 | +0.00% | EVEN, the same |
| cycle time (s) | 16.01 | 16.01 | +0.00% | shown, not judged |
| cycles over the time line (share) | 0 | 0 |  | EVEN, the same |
| tracking error, RMS (rad) | 0.04415 | 0.04415 | +0.00% | EVEN, the same |
| end-point error at the waypoints (rad) | 0.005395 | 0.005395 | +0.00% | EVEN, the same |
| speed override, mean | 1 | 1 | +0.00% | shown, not judged |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
