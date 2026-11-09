# Robot arms: Omni-Compass on top of a robot's own servos, preregistered

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-06, before any counted run. The rules below were set on the tuning robot and are then applied unchanged
to the untouched robots; every row is reported, losses included; the readings are the three-run readings of
`docs/OMNI_V1.md`. The runner is `tools/run_mujoco.py`, the workflow `.github/workflows/mujoco.yml`, the three-run table
`tools/mujoco_abc.py`.

## What is someone else's

- **MuJoCo** (Google DeepMind, Apache 2.0, pinned in `requirements.txt`): the physics engine. It integrates the arm and
  reports every joint's torque, velocity and position. Nothing in it is ours.
- **MuJoCo Menagerie** (Google DeepMind, Apache 2.0 with each robot's own license; the commit is pinned in the workflow):
  the robot models as their makers describe them, with the **position servos the models ship with** (the models'
  `position` or PD `general` actuators, with their gains, control ranges and force limits). That servo is native. The
  models are fetched at run time and are not in this repository.
- **The task**: a pick-and-place cycle of four minimum-jerk segments between fixed joint-space waypoints, the waypoints
  25% of each joint's own range either side of the model's home pose, capped at 0.6 rad (about 34 degrees), the same
  pattern for every arm. The cycle has a **takt**, the slowest cycle the task allows: 1.5 times the planned cycle.

Disclosed: the 0.6 rad cap was set after the first smoke on all four arms, in which the UR5e model's full-turn joint
ranges turned "25% of the range" into 90-degree swings that drove the arm into the floor at any speed. The cap is part of
the task, the same for every arm, and was fixed before any counted run.

## Feasibility, before any Omni run

The planned speed is set per robot, in native mode, as the fastest at which the robot's own servo tracks the task within
0.05 rad RMS, searched from 2.0 s per segment upward in steps of 0.5 s (to 8.0 s). A robot whose servo cannot track the
task at any of those speeds is listed as "the model's servo cannot do the task as modelled", never dropped and never
tuned for.

## Arms

- **native**: the robot's shipped position servo tracks the trajectory at the planned speed (speed override 1.0).
- **omni**: the same servo and trajectory, with the compass law (`omnicompass/compass_law.py`) on **one knob, the speed
  override** (the fraction of planned speed the trajectory is played at, as an industrial controller's speed override),
  inside the takt. Gains, force limits and the trajectory stay the robot's own.

## The omni rule (frozen on the tuning robot)

- **Reading:** the projected cycle time (time used so far plus the time the rest of the trajectory needs at the current
  override), on a band from the planned cycle (position 0) to the takt (position 1).
- **The compass** pulls that position to the middle of its band with its usual gains (`CompassLaw`, kp 1.0, the
  response time 0.5 s, smoothing 0.3): with slack the override eases down (gentler motion, less torque); as the margin
  shrinks it comes back up; past the wall it is full speed at once (fail up). The override's target is 0.75 plus a
  quarter of the force, so it sits between 0.5 and 1.0.
- **Guards:** the override never goes under 0.5 or over 1.0; it moves by at most 0.01 per control tick (100 Hz); a cycle
  that would miss its takt runs at full speed for the rest of the cycle.
- **The paired physics trial, before the counted cycles.** In native mode, one cycle at override 1.0 and one at 0.8,
  neither counted, ask the robot's own figures whether a slower cycle costs less energy at all. Slowing cuts the
  inertial part of the copper loss but pays the gravity-holding part for longer, so on many arms it does not pay. Where
  it does not, **the override is left native for that robot and its result reads "nothing for Omni to move"**. This is
  the do-no-harm gate of `docs/MECHANISM_OF_ACTION.md` 9.6 applied to the arm's own measured figures.
- **Reset:** at the end of every cycle the override is handed back to 1.0 and read back; the report says whether every
  cycle was handed back.

## Energy

MuJoCo has no watt-meter. Energy is a **declared model**, computed the same way for both arms from MuJoCo's own joint
torques and velocities, and said to be a model wherever it is printed (evidence class S):

- mechanical work: the integral of |torque × velocity| over every joint (regenerated energy is not credited);
- copper loss: the integral of torque² × C over every joint, with C = 0.01 W per (N m)² for every arm (a 1-ohm, 0.1 N m/A
  motor behind a 100:1 gear);
- standing draw: a declared idle power per robot (Panda 60 W, UR5e 90 W, iiwa 100 W, Gen3 36 W, from the makers'
  datasheet classes), **drawn for the whole takt in both arms**, moving or waiting, as a robot on a line is.

The unit is **energy per takt**: motion plus the standing draw for the takt. The standing draw is identical in both
arms, so it cannot favour either; it does make every percentage smaller than the motion-only figure, which is also shown.

## Readings (the aim is lower unless said)

| Metric | Direction |
|---|---|
| energy per takt (declared model), copper loss, mechanical work, peak joint torque, mean |torque| | the aim is lower |
| cycles over the takt (share) | **any increase is marked** |
| tracking error (RMS joint error against the trajectory), end-point error at each waypoint | **any increase is marked** |
| cycle time, speed override | shown, not judged |

A change under one part in a million reads "same".

## Robots

- **Tuning robot:** Franka Emika Panda (`franka_emika_panda`). The band mapping, the override target and the guards above
  were set on it; nothing else is tuned.
- **Untouched robots:** Universal Robots UR5e (`universal_robots_ur5e`), KUKA iiwa 14 (`kuka_iiwa_14`), Kinova Gen3
  (`kinova_gen3`).

## Runs

Each robot: 10 cycles per arm in one GitHub Actions job (MuJoCo is deterministic for a fixed timestep, so the cycles
are identical and ten is a check, not a sample), the per-cycle record archived with the code. Three separate runs on
the frozen engine (A, B, C); the table (`tools/mujoco_abc.py`) reads GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given) when the runs
reproduce, same under one part in a million, and "the runs differ" when they do not.

## What the first smoke already showed, said before the counted runs

On the tuning robot the saving is small: a few percent of the motion energy and under one percent of the energy per
takt, because the standing draw and the gravity-holding torque dominate a pick-and-place. On two of the three untouched
arms the paired trial is expected to say a slower cycle is not cheaper, and Omni will leave them native. The counted
runs will show whatever they show.

---

© 2026 Dubra Software Inc. / The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
