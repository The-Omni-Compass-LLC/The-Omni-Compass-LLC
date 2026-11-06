# The swarm's proximity reflex: the omni-v11 wire against the fix, native beside both

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class S: gym-pybullet-drones, an outside simulator, run on our own machine with the repository's own swarm wire
(`tools/run_swarm.py`, omni-v11) and the same wire with the fix below; one flight per cell, draw and arm. This record says
whether the fix holds before a real run; it is not a benchmark result, and the fix runs A, B and C on GitHub once it lands
in the next engine version. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these
results.

## The fault

The swarm wire moves one knob, the cruise override: how much faster than the planner's own cruise each drone flies,
between 1.0 (native) and 2.0. Its proximity reflex is written to hand back the planner's cruise **at once** when another drone
comes within `SEP_WALL` (0.5 m) or the tracking error reaches 95% of its line. The omni-v11 code did not do that: it set the
target to the planner's cruise and then let the override fall by `SLEW` (0.01) a control tick, so a drone at 1.5 kept flying
fast for about 50 ticks (about one second at 48 Hz) after it saw a neighbour. In the counted cells of the omni-v11 three-run
table (`results/live/V11_SWARM.md`) this spent most of the margin: the closest approach, a gauge shown and not judged, fell
from native's 0.30 to 0.46 m to 0.17 to 0.43 m, with no near miss and no collision. On mission draws outside the counted cells
it was not enough: on the mixed cell with draw 214 two drones came within 0.083 m, with 5 near-miss ticks and 3 collision
ticks, where native flew the same draw with none.

## The fix

```python
# omni-v11 (tools/run_swarm.py, Drone.step)
if err >= 0.95 * E_LINE or nearest < SEP_WALL:
    want = O_MIN                                   # fail up: the planner's cruise at once (...)
self.override += clamp(want - self.override, -SLEW, SLEW)

# the fix
# the stopping distance grows with the square of the speed, so the reflex reaches out with it: at the planner's cruise it is SEP_WALL, as before
if err >= 0.95 * E_LINE or nearest < SEP_WALL * self.override ** 2:
    self.override = O_MIN                          # fail up: the planner's cruise at once, in this tick (...)
else:
    self.override += clamp(want - self.override, -SLEW, SLEW)
```

Two changes, both to the guard: the reflex acts in the tick it is triggered, as written; and its reach grows with the square
of the override, because the distance a drone needs to stop grows with the square of its speed. At the planner's cruise the
reach is 0.5 m, as before; at 1.5 it is 1.125 m. Nothing else in the wire, the brain or the law changes.

## The preregistered cells (seeds as in the table; the tuning cell is shown there and not counted)

| Cell | Arm | Closest approach (m) | Near-miss ticks | Collision ticks | Energy a mission (J) | Against native |
|---|---|---:|---:|---:|---:|---:|
| short | native | 0.307 | 0 | 0 | 337.7 | |
| short | omni-v11 | 0.226 | 0 | 0 | 312.6 | −7.4% |
| short | the fix | 0.324 | 0 | 0 | 320.5 | −5.1% |
| mixed | native | 0.300 | 0 | 0 | 499.3 | |
| mixed | omni-v11 | 0.174 | 0 | 0 | 410.5 | −17.8% |
| mixed | the fix | 0.322 | 0 | 0 | 417.8 | −16.3% |
| long | native | 0.460 | 0 | 0 | 548.5 | |
| long | omni-v11 | 0.434 | 0 | 0 | 439.9 | −19.8% |
| long | the fix | 0.330 | 0 | 0 | 468.9 | −14.5% |
| tuning | native | 0.372 | 0 | 0 | 456.3 | |
| tuning | omni-v11 | 0.183 | 0 | 0 | 384.3 | −15.8% |
| tuning | the fix | 0.398 | 0 | 0 | 398.1 | −12.8% |

## Mission draws the wire was never run on (the cell's seed plus 101 or 202)

| Cell, draw | Arm | Closest approach (m) | Near-miss ticks | Collision ticks | Energy a mission (J) | Against native |
|---|---|---:|---:|---:|---:|---:|
| short, 112 | native | 0.398 | 0 | 0 | 337.7 | |
| short, 112 | omni-v11 | 0.410 | 0 | 0 | 312.0 | −7.6% |
| short, 112 | the fix | 0.340 | 0 | 0 | 325.1 | −3.7% |
| short, 213 | native | 0.313 | 0 | 0 | 337.7 | |
| short, 213 | omni-v11 | 0.297 | 0 | 0 | 313.0 | −7.3% |
| short, 213 | the fix | 0.368 | 0 | 0 | 318.9 | −5.6% |
| mixed, 113 | native | 0.301 | 0 | 0 | 492.0 | |
| mixed, 113 | omni-v11 | 0.238 | 0 | 0 | 404.8 | −17.7% |
| mixed, 113 | the fix | 0.304 | 0 | 0 | 419.9 | −14.7% |
| mixed, 214 | native | 0.207 | 0 | 0 | 470.8 | |
| mixed, 214 | omni-v11 | **0.083** | **5** | **3** | 391.7 | −16.8% |
| mixed, 214 | the fix | 0.304 | 0 | 0 | 400.9 | −14.8% |
| tuning, 102 | native | 0.312 | 0 | 0 | 461.7 | |
| tuning, 102 | omni-v11 | 0.298 | 0 | 0 | 386.6 | −16.3% |
| tuning, 102 | the fix | 0.315 | 0 | 0 | 397.7 | −13.9% |
| long, 114 | native | 0.403 | 0 | 0 | 548.4 | |
| long, 114 | omni-v11 | 0.365 | 0 | 0 | 440.0 | −19.8% |
| long, 114 | the fix | 0.360 | 0 | 0 | 455.5 | −16.9% |

## Reading

- **Safety.** With the fix, no near miss and no collision on any of the ten cells and draws, and every closest approach at
  or outside the full 0.30 m keep-out (the least, 0.304 m). In seven of the ten it is at or beyond native's own; in the other
  three it is below native's and above the keep-out. omni-v11 went under the keep-out in seven of the ten and collided once.
- **The energy cut.** The fix keeps 49% to 92% of omni-v11's cut in energy a mission (3.7% to 16.9% against native), because a
  drone now slows the moment a neighbour is inside its stopping reach instead of a second later.
- **What it does not show.** One flight per cell and draw, on one machine: not a three-run reading. PyBullet reproduces to
  about one part in a thousand across machines, so the closest approach can move by that much on GitHub.
- **Where it goes.** A change to a guard makes the next engine version (`docs/CHANGE_CONTROL.md`). The fix is shown to the
  founder before it is pushed, then the swarm runs A, B and C on it with every other benchmark. A judged row for collisions
  (today the near-miss row carries them, because every collision tick is also a near-miss tick) and draws beyond the
  preregistered seeds are proposed for the same version's preregistration.

Machine record: `results/model_gate/V12_SWARM_REFLEX.json` (every flight's gauges).

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
