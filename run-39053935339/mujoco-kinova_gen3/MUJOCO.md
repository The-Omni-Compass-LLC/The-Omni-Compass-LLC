# Omni-Compass on top of a robot arm's own servos (MuJoCo, MuJoCo Menagerie)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MuJoCo (Google DeepMind) integrates each arm; MuJoCo Menagerie supplies the robot as its maker describes it, with the position servos the model ships with. Native: that servo tracks a pick-and-place cycle at its planned speed. Omni: the same servo and trajectory with the compass law on the speed override, inside the cycle's time line (`docs/ROBOTICS_PREREGISTRATION.md`). Energy is a declared model from MuJoCo's own torques and velocities, the same in both arms. Evidence class: S, our model on an independent simulator. Each reading is GAIN, EVEN or LOSS by what the gauge is for, never by its sign; energy, force and copper heating are resources spent, so a rise reads power given (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). Every row is shown, LOSS included.

## kinova_gen3: 7 joints, 10 cycles per arm, planned 8 s (segment 2.0 s, the fastest the robot's own servo tracks within 0.05 rad: 0.0171), takt 12 s

The task: 4 segments between joint-space waypoints 25% of each joint's own range either side of home (at most 0.6 rad), a minimum-jerk trajectory; the same for both arms.

Paired physics trial (native mode, not counted): a cycle at full speed cost 482.3 J, at override 0.8 478.6 J, standing draw 36.0 W included: a slower cycle is cheaper, so omni moves the override.

Omni handed the override back at the end of every cycle: yes.

| Gauge | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| energy per takt (J, declared model: motion plus the standing draw for the whole takt) | 482.3 | 478.3 | -0.82% | GAIN |
| copper heating per cycle (J, I²R, declared model) | 13.68 | 12.14 | -11.27% | GAIN |
| mechanical work per cycle (J) | 36.6 | 34.17 | -6.62% | GAIN |
| standing draw per takt (J, declared model; the same in both arms) | 432 | 432 | +0.00% | EVEN, the same |
| peak joint torque (N m) | 21.74 | 15.52 | -28.63% | GAIN |
| mean |torque| (N m) | 2.687 | 2.338 | -13.01% | GAIN |
| cycle time (s) | 8.01 | 10.21 | +27.47% | shown, not judged |
| cycles over the time line (share) | 0 | 0 |  | EVEN, the same |
| tracking error, RMS (rad) | 0.01707 | 0.01344 | -21.28% | GAIN |
| end-point error at the waypoints (rad) | 0.002418 | 0.002153 | -10.97% | GAIN |
| speed override, mean | 1 | 0.7839 | -21.61% | shown, not judged |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
