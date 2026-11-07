# Drone swarms: Omni-Compass on top of each drone's own autopilot, preregistered

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-07, before any counted run. The rules below were set on the tuning swarm (five drones, run on one machine,
never counted) and are then applied unchanged to the untouched swarms; every row is reported, losses included; the readings
are the three-run readings of `docs/OMNI_V1.md`. The runner is `tools/run_swarm.py`, the workflow
`.github/workflows/swarm.yml`, the three-run table `tools/swarm_abc.py`. This is the first item of register row 23 (drone
swarms, aircraft, defense: gym-pybullet-drones first, then PX4 and ArduPilot multi-vehicle simulation with the shipped
flight code).

## Why this benchmark

A delivery or inspection swarm flies missions from a depot on a battery. Each drone has its own autopilot, which holds a
position and flies a path; the fleet's planner tells it where to go and how fast. Nothing in that stack decides how fast
to fly from the drone's own margins: the planner's cruise is a number set once. That fixed number is the native controller
here, and Omni-Compass sits on top of it: it reads how well each drone is holding its path and spends the slack as speed,
inside the autopilot's own limits, so a charge flies more missions.

## What is someone else's

- **gym-pybullet-drones 2.2.0** (University of Toronto, Dynamic Systems Lab; MIT License; installed from its repository at
  commit `7ebad1ec`, as it is not on PyPI): PyBullet integrates every quadrotor from the **Crazyflie 2.x model the package
  ships** (mass 27 g, its inertia, thrust and torque constants, maximum speed 30 km/h, drag coefficients), and its shipped
  **position controller** (`DSLPIDControl`, one per drone, with its gains and limits) flies it. That autopilot is native.
  The package's downwash term is off: it models drones stacked vertically, which this fleet never is, and its near-field
  term is unbounded for two drones at the same height, which made drones crash on takeoff in the first smoke; drag is on.
- **The task**: N drones at a depot, five spots a depot 0.6 m apart, one cruise altitude per spot (0.8, 1.1, 1.4, 1.7,
  2.0 m), depots 20 m apart; each drone flies K = 4 missions from a fixed, seeded list: climb to its altitude at 0.5 m/s,
  cruise to a target 3 to 8 m out, hover 2 s (the delivery), cruise back, descend, land, next mission. The planner's cruise is
  **1.0 m/s**. A path that would pass within 0.3 m of another spot's column (where that drone climbs and lands) is drawn
  again, so the fleet is kept apart by the task, as a planner would; the autopilots fly it blind. A mission's **deadline**
  (the service line) is 1.5 times its planned time (climb, cruise there and back at the planner's cruise, hover, 1 s to
  settle). The fleet's window is the sum of its drones' deadlines, the same in both arms.

## Arms

- **native**: every drone's shipped position controller flying the planner's path at the planner's cruise.
- **omni**: the same controllers, paths and missions, with the compass law (`omnicompass/compass_law.py`) on **one knob,
  the cruise override** (the fraction of the planner's cruise the carrot moves at), never under 1.0 (the planner's cruise)
  and never over 2.0 (2 m/s, a quarter of the autopilot's own speed limit). Gains, limits, altitudes and missions stay the
  fleet's own.

## The omni rule (frozen on the tuning swarm)

- **Reading.** Each drone's tracking error: the distance between the drone and the point its autopilot was told to be at,
  on a band from 0 to the **declared safe error, 0.25 m** (under the 0.3 m keep-out and the 0.3 m altitude stagger).
- **The compass** holds that reading in the middle of its band with its usual gains (`CompassLaw`, kp 1.0, response time
  1 s, smoothing 0.5): with slack it spends it as speed (the override rises); as the error grows it eases; at 95% of the
  safe error the cruise is the planner's at once (fail up). The override's target is the middle of its range minus half
  the force, so it sits between 1.0 and 2.0; it moves by at most 0.01 per control tick (48 Hz).
- **The separation wall.** A drone with another drone within 0.5 m flies the planner's cruise at once, whatever the
  error reads (a safety reflex native does not have; Omni adds it because it is the one spending the margin).
- **The paired physics trial, before the counted missions.** In native mode, one mission per drone at the planner's
  cruise and one at 1.25 times it, neither counted, ask the simulator's own figures whether a faster mission costs less
  energy at all and whether the tracking error stays under the safe error with no collision. A quadrotor's power is nearly
  flat with speed at these speeds, so fewer seconds airborne should mean less energy a mission; where the trial says
  otherwise, **the override is left native for that cell and its result reads "nothing for Omni to move"**. This is the
  do-no-harm gate of `docs/MECHANISM_OF_ACTION.md` 9.6 applied to the fleet's own figures.
- **Reset.** At every landing and at the end of the run the override is handed back to the planner's cruise and read
  back; the report says whether every drone was handed back.

## Energy

The simulator has no watt-meter. Energy is a **declared model**, computed the same way for both arms from the simulator's
own motor constants, and said to be a model wherever it is printed (evidence class S):

- each motor's mechanical power: torque × angular speed, with torque = KM × rpm² (the package's own constant) and angular
  speed 2π rpm / 60, divided by a declared motor efficiency of 0.5 (small brushed motors);
- avionics: a declared 0.5 W per drone **for the whole fleet window in both arms**, flying or landed.

The battery is the Crazyflie's, 250 mAh at 3.7 V (11,988 J); the autopilot's own reserve rule is 20% left at landing, so a
drone whose energy over the window exceeds 80% of the battery has **broken the reserve**. **Missions per charge** is 80% of
the battery over the energy per mission.

## Readings

| Gauge | Direction |
|---|---|
| energy per mission, fleet energy over the window (declared model) | the aim is lower |
| missions per charge at the autopilot's reserve | **the aim is higher** (the product number) |
| missions over their deadline (share), drones that broke the reserve, near misses (control ticks with two drones under 0.15 m apart) | **any increase is marked** |
| collisions (two drones under two collision radii) | **zero in both arms, or the cell is void** |
| closest two drones ever came, tracking error (the compass's reading), mission time, seconds airborne, cruise override | shown, not judged |

A change under one part in a million reads "same". PyBullet is deterministic for a fixed step, so the three runs must
reproduce each other; a gauge that does not reads "the runs differ", which is a finding about the simulator or the harness.

## Cells

- **Tuning swarm:** 5 drones (one depot), 4 missions each, 3 to 8 m, seed 1. The band, the override's range and target, the
  slew, the separation wall and the energy model above were set on it; nothing else is tuned. It is run and shown, and
  not counted in the across-cells tally.
- **Untouched swarms:** 20 drones (four depots), 4 missions each: **short** (3 m, seed 11), **mixed** (3 to 8 m, seed
  12), **long** (8 m, seed 13).
- At 100 drones and more the swarm runs on a rented machine (`docs/PROOF_PROGRAM.md`), later.

## Runs

Each cell is one GitHub Actions job, native and omni on the same missions, its JSON and per-mission records archived with the
code. Three separate runs on the frozen engine (A, B, C); the table (`tools/swarm_abc.py`) reads GAIN in all three of our runs or
GAIN or LOSS by each gauge's own aim when the runs reproduce, same under one part in a million, and "the runs differ" when
they do not. `tests/test_run_swarm.py` and `tests/test_swarm_abc.py`, run by `verify.py`, prove the rules without the
simulator: the task keeps the fleet apart, a perfect autopilot finishes every mission inside its deadline, the override
stays inside its guards and is handed back, the energy model is the declared formula.

## Amendment 1 (2026-10-07 20:40 UTC, after the first A, B and C were seen; said so)

The three counted runs (37677964512, 37677984739, 37678005151) gave every gauge the same sign and the same size to within
a few parts in ten thousand, and not to the bit: PyBullet's floating point differs from one GitHub machine to the next
(the runs' energy per mission in the mixed cell: −17.79%, −17.79%, −17.82%). The table tool had demanded bit-exact
reproduction, as MuJoCo gives, and so read every row "the runs differ". The reproduction tolerance is set to **one part in a
thousand** (`tools/swarm_abc.py`, `REPRO_REL`), the readings stay by the sign of all three runs, and this change, its
timing and its reason are stated here and in the table. Nothing in the task, the omni rule or the gauges changes; the runs
are not rerun.

## Amendment 2 (2026-10-19, before omni-v12's runs; written after the omni-v11 runs and the reflex study were seen, and said so)

On a mission draw outside the counted cells the omni-v11 wire let two drones collide where native flew the same draw with
none (`results/model_gate/V12_SWARM_REFLEX.md`): a collision voided the cell under the rule above, so a collision Omni-Compass
caused could only ever be read as a void cell, and a fixed set of seeds could not show it at all. From omni-v12's runs on,
two readings change, nothing else:

- **A judged collision row.** Control ticks with two drones under two collision radii are a judged gauge, any increase
  marked: a collision with Omni-Compass on top where native has none reads **LOSS**. A cell is void only when native itself
  collides (its task unsafe before Omni-Compass touches it). `tools/run_swarm.py` (`COLLISIONS`) and `tools/swarm_abc.py`
  apply it to runs on omni-v12 and later; the earlier tables are rebuilt as they were scored.
- **Draws never flown.** The three untouched swarms run also on fresh mission draws, the cell's seed plus 303 (**short-314**,
  **mixed-315**, **long-316**), counted beside the first three. No wire was ever run on them: the reflex study used the seed
  plus 101 and 202.

The omni rule, its guards, the energy model and every other gauge stay as above.

## What the tuning swarm showed, said before the counted runs

On one machine, five drones, four missions each: a faster mission is cheaper (498 J at the planner's cruise, 446 J at
1.25 times it), so omni moved; energy per mission 456 → 384 J (−16%), missions per charge 5.8 → 6.9, no late mission in
either arm, no collision, no near miss, every override handed back; the tracking error rose from 0.07 to 0.14 m (inside the
0.25 m band, as the rule intends) and the closest approach fell from 0.37 to 0.18 m, which is shown, not judged, and is why
the near-miss count is a judged gauge. The first smoke, with the package's downwash term on and drones at a common
altitude, crashed four of five drones on takeoff; the second, with targets allowed near other spots' columns, collided in
both arms. Both are task and simulator settings fixed before any counted run, and said here. The counted runs will show
whatever they show.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
