# Preregistration: Omni-Compass on top of a distribution grid's own voltage control (pandapower, SimBench)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Frozen 2026-10-05, before any counted grid was run. The tool is `tools/run_pandapower.py`, and the workflow is
`.github/workflows/pandapower.yml`.

## What is someone else's

- **pandapower** 3.5 (Fraunhofer IEE and the University of Kassel; BSD) solves every AC power flow.
- **SimBench** (the German benchmark grids) supplies the grids and a year of 15-minute load, solar and wind profiles.

Nothing here models the grid. Omni only moves the busbar setpoint of the grid's own substation tap changer.

## Arms

| | |
|---|---|
| native | The substation tap changer holds its medium-voltage busbar at 1.00 per unit. Its deadband is half a tap step (tap 1.5%). It makes at most one tap per transformer per step. This is the grid running on its own. |
| omni | The same tap changer, with the compass law on top of its setpoint, inside the cover [0.97, 1.03] per unit. |

## The omni rule (frozen)

1. **It reads the worst margin anywhere in the grid:** the bus nearest 0.95 or 1.05 per unit.
2. **Every move is one whole tap (1.5%)**, so it never hunts.
3. **Away from a limit, at once.** When the lowest bus is within MARGIN = 0.01 of 0.95 (or the highest within 0.01 of
   1.05), the setpoint moves one tap away. It moves only if the other side keeps a tap plus MARGIN of room, and only
   once the utility's tap changer has reached the present setpoint.
4. **Toward saving, only on a week of evidence.** The setpoint steps down one tap (conservation voltage reduction)
   only when all three hold:
   - the compass law is calm;
   - a full week (WINDOW_H = 168 h) has been seen under the present setpoint;
   - the worst moment of that week would still leave every bus MARGIN after one more tap.
5. **Hand-back.** At 90% of the year the setpoint is handed back to 1.00.

## The tuning grid, and what tuning found

The tuning grid is 1-MV-rural--0-sw. It is the only grid looked at before this freeze. Tuning found and fixed three
things.

- **Tap hunting.** An earlier continuous rule made 168 tap operations a year against native's 4. The week-of-evidence
  rule replaced it.
- **Start-up transient.** Omni reacted to the native tap changer still travelling to its setpoint in the first
  hours. The settled gate (rule 3) fixed it.
- **ZIP loads.** pandapower applies a bus's ZIP shares to the whole bus demand, solar on that bus included, so the
  solved balance came out backwards. ZIP is now applied per load by hand: p0 (z V² + i V + p) at the load's own
  voltage, solved again until the voltages move less than 1e-5. Every step's balance (import + solar = load + losses)
  is checked; the worst is reported, and on the tuning grid it is 5e-9 MW.

## Loads

The run is made with two load models:

- **ZIP:** 40% constant impedance, 30% constant current, 30% constant power. This is a common residential mix, and
  declared here.
- **Constant power:** SimBench as shipped. Only losses can change.

## Counted grids (untouched)

The counted grids are the SimBench medium-voltage grids rural, semiurb, urban and comm, in scenarios 0, 1 and 2
(today, and two future scenarios with more solar), minus the tuning grid. All of them are hourly (every 4th quarter
hour), for a full year, with both load models.

## Readings

| Metric | Direction |
|---|---|
| energy the loads drew, line and transformer losses, net import | the aim is lower |
| bus-steps outside 0.95–1.05 | the aim is lower; any increase is marked |
| tap operations | the aim is lower |

Lowest and highest voltage, solar fed in and the mean setpoint are shown, not judged. A change smaller than one part in
a million reads "same".

**Tap operations are declared in advance as the expected cost.** Each Omni setpoint change is one tap on each substation
transformer, the hand-back included. Native SimBench grids barely tap, about 4 a year, so the count will read higher. It
is reported as measured, next to the energy, never hidden. For scale, a substation tap changer is built for hundreds of
thousands of operations.

## The wiring check, before any counted grid is read (2026-10-05)

Written after the tuning grid and before any untouched grid's result was looked at, as the founder asked: if Omni comes
out behind, the first suspect is our own wiring, not Omni. Three things were checked on the runner (`tools/run_pandapower.py`)
against pandapower's own grid data, and what was found is recorded here whether or not it flatters Omni.

1. **Omni reaches the right knob, the right way.** One tap step up on the substation transformer lowers the
   medium-voltage busbar by 1.55% on every one of the four grid types (the SimBench transformers' tap step), so the sign
   and the size of the move are right, and nothing is clipped or ignored on the way. Both parallel transformers of the
   substation are controlled together and both are counted in the tap operations, so the count is not understated.
2. **Native runs as a utility runs it.** The native arm is the grid exactly as SimBench ships it, with its own tap
   position held for the year; it is not weakened to make Omni look a GAIN.
3. **The simulator scores right.** The energy balance closes at every step (generation equals load plus losses plus net
   import, to about a billionth of a megawatt) once solar on a load bus was accounted as generation rather than a
   voltage-dependent load (that fix is in the runner and applies to both arms alike).

Two things found that do not change the rules, stated so a reader knows them:

- Omni's margin reading includes the high-voltage bus, which is fixed at 1.025 per unit and cannot be moved by the tap.
  It never binds (the medium-voltage buses always sit closer to a limit), so it changes no decision. Harmless, and left
  as frozen rather than changed after the fact.
- On the grid the compass's force decides only *when* to step down; the guard rules (a whole week of margin before a
  step, one whole tap per move, an immediate step back up when any bus nears a limit, the hand-back at 90% of the year)
  decide everything else. That is less of the law and more of the guard than on Kubernetes, and the report says so.

The tap-operation count stays as frozen above (about 8 a year against native's about 4). Capping Omni at 4 after seeing
the tuning grid would be tuning on the test; the cost was declared before the untouched grids ran and is reported next to
the energy, never hidden.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
