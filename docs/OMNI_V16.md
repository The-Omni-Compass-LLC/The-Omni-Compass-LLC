# Omni v16: every clock of the governor in seconds; the heartbeat at 15 s

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v16 (`OMNI_V16.json`, digest `5c5502f12b1c0ce4`, 55 files) stood on main on 22 October, from the morning until omni-v17
landed that evening (`docs/OMNI_V17.md`: the same engine with the heartbeat a dial, the main engine at 60 s, and the cruise
wait never under two readings at a slow beat). Two words of the founder's
made it. That night ("Go"), on the plan put to him: put every clock of the Kubernetes governor in seconds, read the decision
pace at 60, 15, 10 and 5 s in our own models, and run each pace three times on GitHub's own machines
(`docs/PACE_PREREGISTRATION.md`). Then, once the models had read: "15 sec all over heart beat fix update code". So the
governor's heartbeat, its full decision, comes every 15 s by default, native's own pod autoscaler's pace, where every engine
before it decided every 60 s; the fast checks stay every 5 s. It is omni-v15 (`docs/OMNI_V15.md`) with the clocks changed and
the heartbeat set, and nothing else: every gain, guard, preset and muscle is omni-v15's, and 50 of its 55 files are
omni-v15's bytes (the five changed: `omnicompass/adapter.py`, `omnicompass/edge.py`, `omni_controller/controller.py`,
`omni_controller/muscles.py`, `omni_controller/capacity.py`; the brain's C++ twin `cpp/src/governor.cpp` with it, sealed).
Read in the model gate against omni-v15 on the same seeds before it was pushed (`results/model_gate/V16_VS_V15.md`), and the
pace read alone on a plant that moves every 5 s (`results/model_gate/V16_PACE.md`). The readings from the model gate are our own
models (evidence class S), never a benchmark result. Run and scored by The Omni-Compass LLC's own code. No outside party has
reviewed or approved these results.

## Why

Every engine through omni-v15 took its full decision every 60 s. The number was written into the first harness on 26
September, with no reason recorded, and never measured against another; the engine was then tuned at 60 s and several of
its rules were written in decisions, which locked 60 s in. Native's pod autoscaler checks every 15 s, the metrics it reads
refresh every 15 s, the Cluster Autoscaler scans every 10 s, KEDA every 30 s. The founder asked for 15, 10 and 5 s on 14
October; six rules moved to seconds on 16 October (omni-v7) and the rest did not, so turning the period also changed what
the remaining rules meant. omni-v16 finishes the job: turning the period changes only how often the governor looks. The
cushion each muscle keeps is set by its own climb, wobble and reaction time in seconds, and is the same at any pace; the pace
sets only how soon trouble is seen (within 15 s at 15 s, within a minute at 60 s), and so the default moves to native's 15 s.

The founder asked, before the default was set, whether a longer period would make a larger cushion and a stronger engine.
It would not: a longer period leaves the governor blind for longer between looks (up to two minutes at 120 s, while native
checks every 15 s), and to stay as safe while blind longer it would have to hold more back, which is less work done. The
cushion has its own setting (each muscle's z of 3.09, 99.9% of steps inside it, and the dial's tune-down), and the period is
not it.

## What counted in decisions, and what it counts now

Every value below is the one omni-v15 used when a decision comes every 60 s (the reference step; `REF_PERIOD_S`).

| Clock | omni-v15 (per decision) | omni-v16 (per second) | Where |
|---|---|---|---|
| the brain's blending of each reading | 0.339 of the state a decision | 1 − (1 − 0.339)^k a decision, k = period / 60 s: 0.339 a minute | `omnicompass/adapter.py` (`Governor.step`, `period_s`) |
| the brain's inner time | 0.1 of its macro interval a decision | 0.1 k a decision | the same |
| the brain's dwell and wait before giving a machine back | 1 and 5 decisions (the fleet law) | the same seconds: 60 and 300 s | the same |
| the brain's machines added or removed | up to 8 and 1 a decision | up to 8 and 1 over the last minute's decisions | the same; the C++ twin `cpp/src/governor.cpp` identically |
| the compass's damping (kd) | critical damping for the decision period | critical damping at the minute, so the law's push and pull per second are the same at any period | `omni_controller/controller.py` |
| the compass's velocity smoothing | 0.3 a decision | 0.3 a minute | the same |
| the edge's window, narrowing, the floor's forgetting, memory, wobble step | 20 decisions; 0.05, 0.9995 a decision; one decision's change | 20 minutes; 0.05, 0.9995 a minute; a minute's change | `omnicompass/edge.py` (`pace`) |
| what a breach teaches the edge | 0.1 a decision of breach | 0.1 a minute of breach | `omni_controller/controller.py` |
| machines added past the scheduling floor | one step a decision | one step a minute (the release has been one a minute since v7); the floor's machines at once | the same (`ADD_PERIOD_S`) |
| a command's time to land (proprioception) | the next decision | a minute, every decision reading it until it lands | the same (`LAND_S`) |
| the host's busy share (kind's shared runner) | since the last decision | over the last minute | `omni_controller/capacity.py` (`span`) |
| the heat law | 0.86 of the heat kept a decision | 0.86 a minute | `omni_controller/muscles.py` |
| held batch jobs admitted; jobs paused or resumed | one a decision | one a minute | the same |
| a quiet deployment scaled to zero | 3 idle decisions | 180 idle seconds (`--coldstart-idle-s`) | the same |
| the coast toward fewer pods | coast step × period / 60 a raise | the coast step a raise (a raise comes at most once a window) | `omni_controller/controller.py` |
| the conveyance | every third fast check, never at a decision (so never at a decision every 5 s) | every 15 s, whichever check falls due (`--convey-every-s`) | the same |
| the loop | each wait began when the step ended (a 60 s decision came every 62 to 67 s on kind) | keeps its own schedule; a missed slot is skipped, never run in a burst | the same (`main`) |

Six rules already counted seconds since omni-v7 and stay as they were: the line's clear time, cruise, the strict window,
the trial spacing, the wait after a refusal, and a trial's length; so does the release of one machine a minute.

## The heartbeat: a full decision every 15 s

The default `--interval` is 15 s and `--floor-interval` 5 s (`omni_controller/controller.py`; before, 60 s and 15 s, every rig
and install file setting the fast checks to 5 s). Every place that starts the governor carries it: the rigs
(`scripts/kind_bench.sh`, `kind_paired.sh`, `kind_robust.sh`, `kind_full.sh`, `kind_pilot.sh`), the install files
(`deploy/install/omni-compass.yaml`, `omni-compass-cloud.yaml`, `deploy/controller.yaml`), the cloud runs (which start it
through `kind_bench.sh`), the alert rules' staleness bound (`deploy/prometheus/omni-compass-rules.yaml`: three intervals, 45 s)
and the manuals. Each run writes its period beside its files (`omni_interval.txt`), and the receipts read each run at its own
(`tools/live_reps.py`; the robustness runs before it at 60 s). The page's controller trace and the modelled traces in the
manuals keep the 60 s step they were drawn at, and say so. The levers rig (`scripts/kind_levers.sh`) was left at three, two
and three decisions of 5 s when omni-v16 landed: under omni-v14 each of them was a minute of the brain's, under omni-v16 they
are 15 s, and the two levers that give back (rightsize, coldstart), which wait for the brain's calm (its contraction authority,
about a minute after it starts on an idle reading, `tests/test_pace_clocks.py`), failed three of the rig's 19 checks in the
first omni-v16 run (22 October, 13:50 UTC). The rig now runs at the default 15 s for the 3, 2 and 3 minutes its checks were
written for, with the idle time before cold start in seconds (120 s), and the levers check runs again, A, B and C
(`scripts/reruns.txt`).

## At 60 s it is omni-v15

On the model cluster at a decision every 60 s, omni-v16 makes exactly omni-v15's decisions: 4,578 audit records, none
different (seed 1; the gate's eight seeds read every gauge identical, on every model). The brain's C++ twin equals the Python
at 60, 15, 10 and 5 s (`tests/test_cpp_governor_parity.py`, 4,320 directives each, no difference), and every twin was
sealed again after its parity test passed (`results/SEAL.json`). Two changes can be seen at 60 s on a real cluster and
nowhere else: the conveyance comes every 15 s exactly (omni-v15: about 3.7 passes a minute), and the loop keeps its
schedule (omni-v15's decisions drifted by the steps' own time). The model gate's other columns, each engine against native,
read as they read for omni-v15 (the same rows, the same numbers at 60 s), because nothing but the clocks moved.

At 15 s, where omni-v15's rules counted in decisions ran four times as fast, every gauge reads STEADY against omni-v15, and the
machines parked over the eight days fall from 4,212 to 1,782 (omni-v15 at 60 s: 1,464): the pace no longer changes what a
rule means. As shipped (the model `cluster_shipped`: omni-v16 at its default of 15 s against omni-v15 at its 60 s, each started
without a period, as an install file starts it), every gauge reads STEADY: machine hours +2.4%, energy per core-hour −0.5%, the
pods waiting for a place −28.5%, the 95th percentile −0.3%, the alert minutes −0.9%. No LOSS against the engine it replaces.

The brain's lock (`results/LOCK_AMENDMENTS.json`) takes an amendment for `omnicompass/adapter.py`: the stack simulator steps
at 60 s, so the held-out seeds replay unchanged (`verify.py`).

## The pace in our models (`results/model_gate/V16_PACE.md`)

omni-v16 alone, eight seeds of a day each on a plant that moves every 5 s, at 60, 15, 10 and 5 s, each faster pace paired by
seed against 60 s and against native. In the cloud's setting (the tune-down, machines alone), against 60 s, every service
reading is STEADY at every pace (at 15 s: pending pod minutes −12.1%, the 95th percentile −0.0%, alert minutes +0.5%, machine
hours −0.4%) and energy per core-hour falls 2.6% at 15 s (GAIN); the power cap's request moves more (power given). In the
kind benchmark's setting (the compass law at the max, every autoscaler sensed), against 60 s, the alert minutes fall 14.7% at
15 s and 18.4% at 10 and 5 s (GAIN), the autoscaler's shortfall 6% at 10 and 5 s (GAIN), and every other reading is STEADY.
Omni's own processor: 1.6 to 1.7 s an hour at 60 s, 2.7 at 15 s, 3.4 at 10 s, 5.5 at 5 s (under a thousandth of one core
at 5 s); its reads: 1,650 an hour at 60 s, 2,190 at 15 s, 3,600 at 5 s. No LOSS against 60 s at any pace.

Against native, the rows read as the engine reads them at every pace, the old 60 s default included, and some read LOSS.
The pods waiting for a place: in the kind setting about four times native's at every pace (pending pod minutes an hour:
native 8.2; 32.0 at 60 s, 33.5 at 15 s, 28.8 and 28.6 at 10 and 5 s), LOSS at every pace; in the cloud's setting about twice
(20.9 at 60 s, 18.4 at 15 s), LOSS at 15 and 5 s and STEADY at 60 and 10 s only by the seeds' spread; on the model gate's 15 s
plant, +121.6% at 15 s (LOSS) and +209.8% at 60 s (STEADY by the spread). In the cloud's setting at 15 s two small rows read LOSS
as well: the 95th percentile, +0.47% on the 5 s plant and +0.36% on the gate's (at 60 s +0.49% and +0.63%, STEADY by the
spread), and the alert minutes, +2.31% on the 5 s plant (at 60 s +1.85%, STEADY). Against 60 s every one of them reads STEADY,
the 15 s point estimates the smaller, so they are the engine's and not the pace's: the faster pace narrows the seeds' spread
until the rows clear zero. They are on the next version's list to be root-caused (`docs/CHANGE_CONTROL.md`), beside the
blink model's alert minutes (+2.35% against native at 60 s, LOSS, the same in every gate since omni-v13).

## The real runs

`docs/PACE_PREREGISTRATION.md`: workflow `benchmark-reps`, five arms in every repetition (native; Omni-Compass on top at its
default heartbeat of 15 s; the same deciding every 60, 10 and 5 s), the reruns' steady scenario, three runs of 10
repetitions on GitHub's own machines at no cost, released by the conductor as the campaign's entry `kubernetes decision
pace`. They are the real-run reading of the heartbeat the founder set: a LOSS at 15 s there is root-caused and fixed in the
next version, as any other.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
