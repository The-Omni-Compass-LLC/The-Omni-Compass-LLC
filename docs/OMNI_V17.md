# Omni v17: the heartbeat a dial; the main engine at 60 s

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v17 (`OMNI_V17.json`, digest `7c937d09e4031cc7`, 55 files) stood on main on 23 October, from the afternoon until omni-v18 landed that night (`docs/OMNI_V18.md`). The founder's order of the afternoon
before (22 October), once he had read the reads of the cluster a day in the pace study (about 86,000 at 5 s against 39,700 at 60 s): the
governor's heartbeat, its full decision, is a dial, "5, 15, 30, 60, 75, 90, 120 ... Heartbeat scaled in its monitors. And you're
going to set OmniCompass is main engine", because "who knows if maybe the purpose is somebody wants to set it at 5 seconds"; and
before it, "we are going to write the engine to have the 60 ... we have to actually have to be able to show the same 15 second
beats". So the main engine takes its full decision every 60 s; any beat can be set (`--interval`, 5 to 120 s and every value
between), the fast checks every 5 s at every beat; and every beat is shown beside native with what it buys and what it costs,
because an operator may want a fast beat for its reads and accept what it costs, or a slow one, and at each beat the other knobs
may want their own combination. It is omni-v16 (`docs/OMNI_V16.md`) with two changes, both in `omni_controller/controller.py`
(54 of its 55 files are omni-v16's bytes): the parser's default period moved from 15 to 60 s; and the cruise rule's wait never
fewer than two readings, a fault the dial's own ladder found at 90 and 120 s before the version landed (below, "The fault the ladder found"). Every clock
of the governor counts seconds since omni-v16, so the dial changes only how often it looks. Read in the model gate against
omni-v16 on the same seeds (`results/model_gate/V17_VS_V16.md`), and every beat read beside native and beside 60 s on a plant
that moves every 5 s (`results/model_gate/V17_LADDER.md`), before it was pushed. The readings from the model gate are our own
models (evidence class S), never a benchmark result. Run and scored by The Omni-Compass LLC's own code. No outside party has
reviewed or approved these results.

## Why a dial, and why 60 s for the main engine

Through omni-v15 the governor decided every 60 s, a number written into the first harness on 26 September and tuned around;
omni-v16 put every clock in seconds so that the period became a clean setting, and set it at 15 s, native's own pod
autoscaler's pace, on the founder's word that morning. The models then showed what each pace buys and costs: a faster beat
reads the cluster more often (about 39,700 reads a day at 60 s, 52,500 at 15 s, 86,400 at 5 s), spends more of the governor's
own processor (1.6 to 1.7 s an hour at 60 s, 2.7 at 15 s, 5.5 at 5 s, under a thousandth of one core at any beat), and in the
kind benchmark's setting sees trouble sooner (the minutes over the line 14.7% fewer at 15 s than at 60 s); against native the
same rows read at every pace. No one beat is right for every operator. The founder's order makes the beat the operator's
setting, as the tune-down is, and sets the main engine, the one the company ships and benchmarks first, at 60 s, the period
every engine through omni-v15 decided at; 15 s, native's own pace, is one setting of the dial, run and shown beside it.

## The dial in our own models (`results/model_gate/V17_LADDER.md`)

The engine alone on a plant that moves every 5 s, the fast checks every 5 s at every beat, eight seeds of a day each, the same
seeds and plant at every beat: 5, 10, 15 and 60 s from the pace study of omni-v16 (`results/model_gate/V16_PACE.json`, read
before omni-v16 landed, each run setting its period on the command line, so it reads the same on omni-v17), and 30, 75, 90 and
120 s run the same way for omni-v17; the native and 60 s runs the two share read the same seed by seed on every modelled gauge
to the twelfth digit (the two were run under Python 3.11 and 3.12, whose float sums differ in the last bits of one gauge, the
power cap's travel; `tools/beat_ladder.py` refuses a ladder where any shared reading differs by more). The governor's own
processor is timed, not modelled, so each beat's is paired only with the 60 s of its own run. Each beat is paired by seed
against native and against the main engine's 60 s.

In the cloud's setting (the compass law at the tune-down, the machines alone), each beat's mean over the eight seeds and its word against native:

| Beat | Reads a day | Omni's own processor (s an hour) | Pods waiting (min an hour) | 95th percentile (ms) | Minutes over the line (a day) | Autoscaler short (min an hour) | Machine-hours (a day) | Energy per core-hour (kWh) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| native | | | 8.18 | 79.94 | 27.00 | 1.20 | 133.08 | 0.0357 |
| every 5 s | 86,412 | 5.51 | 16.52 LOSS | 80.18 STEADY | 27.50 STEADY | 1.20 STEADY | 129.67 STEADY | 0.0344 GAIN |
| every 10 s | 60,924 | 3.38 | 15.92 STEADY | 80.11 STEADY | 27.12 STEADY | 1.20 STEADY | 133.40 STEADY | 0.0346 GAIN |
| every 15 s | 52,545 | 2.68 | 18.36 LOSS | 80.31 LOSS | 27.62 LOSS | 1.20 STEADY | 131.48 STEADY | 0.0341 GAIN |
| every 30 s | 44,009 | 2.07 | 18.59 LOSS | 80.22 LOSS | 27.38 STEADY | 1.20 STEADY | 132.19 STEADY | 0.0347 GAIN |
| **every 60 s (the main engine)** | 39,691 | 1.69 | 20.88 STEADY | 80.33 STEADY | 27.50 STEADY | 1.20 STEADY | 131.98 STEADY | 0.0350 STEADY |
| every 75 s | 38,928 | 1.66 | 19.30 STEADY | 80.20 STEADY | 27.38 STEADY | 1.20 STEADY | 131.21 GAIN | 0.0350 GAIN |
| every 90 s | 38,396 | 1.60 | 18.27 STEADY | 80.35 STEADY | 27.62 STEADY | 1.20 STEADY | 131.29 GAIN | 0.0350 GAIN |
| every 120 s | 37,415 | 1.58 | 14.01 STEADY | 80.08 STEADY | 27.12 STEADY | 1.20 STEADY | 130.93 STEADY | 0.0352 STEADY |

In the kind benchmark's setting (the compass law at the max, every autoscaler sensed):

| Beat | Reads a day | Omni's own processor (s an hour) | Pods waiting (min an hour) | 95th percentile (ms) | Minutes over the line (a day) | Autoscaler short (min an hour) | Machine-hours (a day) | Energy per core-hour (kWh) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| native | | | 8.18 | 79.94 | 27.00 | 1.20 | 133.08 | 0.0357 |
| every 5 s | 86,412 | 5.55 | 28.55 LOSS | 76.88 GAIN | 19.38 GAIN | 1.12 GAIN | 149.67 power given | 0.0385 power given |
| every 10 s | 60,942 | 3.43 | 28.80 LOSS | 76.85 GAIN | 19.38 GAIN | 1.12 GAIN | 149.17 power given | 0.0384 power given |
| every 15 s | 52,490 | 2.66 | 33.51 LOSS | 76.93 GAIN | 20.25 GAIN | 1.14 GAIN | 151.78 power given | 0.0389 power given |
| every 30 s | 43,869 | 2.01 | 34.09 LOSS | 76.99 GAIN | 21.25 GAIN | 1.16 GAIN | 151.78 power given | 0.0389 power given |
| **every 60 s (the main engine)** | 39,444 | 1.58 | 31.96 LOSS | 77.18 GAIN | 23.75 GAIN | 1.19 STEADY | 151.29 power given | 0.0388 power given |
| every 75 s | 38,836 | 1.66 | 29.15 LOSS | 77.17 GAIN | 21.75 GAIN | 1.19 STEADY | 149.50 power given | 0.0384 power given |
| every 90 s | 38,254 | 1.52 | 28.10 LOSS | 77.01 GAIN | 22.62 GAIN | 1.20 STEADY | 148.78 power given | 0.0383 power given |
| every 120 s | 37,536 | 1.47 | 22.51 LOSS | 76.99 GAIN | 22.88 GAIN | 1.24 STEADY | 148.18 power given | 0.0382 power given |

Each beat against the main engine's 60 s, and every gauge in full, is on the ladder's page.

## The fault the ladder found: cruise on one reading at 90 and 120 s

The ladder's first reading of 90 and 120 s (kept on its page, "The first reading of every 90 and 120 s, before the fix") put the
kind benchmark's setting in another regime from 75 s down: against 60 s the machine-hours +17.1% and +21.4%, the minutes over
the line −71.6% at both, the pods waiting for a place −59.4% and −70.7%, the 95th percentile −15.4% and −21.3%, and the machines
parked over the eight days 82 and 46 against 329. A jump that sharp between two neighbouring beats is a rule's count crossing a
threshold, not a pace. The cause is the cruise rule (rule 7: work waiting for a place decision after decision puts every machine
in service until the line has been empty as long). Its wait is written in seconds, `--cruise-after-s 120`, and v7 converts every
such wait to decisions as n = max(1, round(seconds / period)): 2 at 60 and 75 s, but round(1.33) = 1 at 90 s and round(1.0) = 1
at 120 s. With one decision, a single reading with one pod waiting set every machine in service and a single empty reading let
them go: the rule no longer asked for work that waits "decision after decision", the words it is written by. The fix
(`omni_controller/controller.py`): the cruise wait is never fewer than two readings, `max(2, round(120 / period))`, when it
is derived from seconds; a count an operator sets by hand (`--cruise-after`) stands as set. At every beat up to 80 s the count
is what it was (24 at 5 s, 8 at 15 s, 4 at 30 s, 2 at 60 and 75 s), so nothing below 80 s moves; at 90 and 120 s it is 2
(`tests/test_pace_clocks.py`, which fails on the unfixed rule). Corrected, the kind benchmark's setting reads at 90 s, against 60 s, the machine-hours down 1.7%, STEADY, the minutes over the line down 4.7%, STEADY, the pods waiting down 12.1%, STEADY, the 95th percentile down 0.2%, STEADY; at 120 s the machine-hours down 2.1%, STEADY, the minutes over the line down 3.7%, STEADY, the pods waiting down 29.6%, GAIN; machines parked over the eight days 190 and 119 against 329 at 60 s. No other count of the
governor's falls to a single reading between 5 and 120 s: the breach's clear time (180 s) is 2 decisions at 120 s, the strict
window (300 s) 2, the trial's phase (1,200 s) 10; the brain's dwell is one step by design and its waits round to the nearest
step. In the cloud's setting (the machines alone, at the tune-down) every service, machine-hour and energy reading at 90 and
120 s is the same before and after the fix, seed by seed; what moves is the governor's own reads of the cluster, 1.9% and 1.2%
more (cruise pauses the five-second floor reads, and it now pauses less often), and the machines parked on three seed-beats
(128 against 126, 148 against 147, 83 against 80).

## What the slower main engine costs against 15 s

Set at 60 s, the main engine gives up what 15 s bought in the models, and it is disclosed here as the price of the founder's
setting: in the kind benchmark's setting the minutes over the line are 23.75 a day at 60 s against 20.25 at 15 s (+17.3%: read
the other way, 15 s against 60 s, −14.7%, GAIN, so 60 s against 15 s is a LOSS by the key), still 12.0% fewer than native's
27.0 (GAIN against native); in the cloud's setting the energy per core-hour is 2.6% more at 60 s than at 15 s (power given).
Every other row reads STEADY between the two. The model gate's own models read the change as shipped (`cluster_shipped`, each
checkout started without a period, as an install file starts it: omni-v17 at its 60 s against omni-v16 at its 15 s): every gauge reads STEADY: the machine-hours −2.3%, the energy per core-hour +0.5%, pods waiting for a place +39.8%, the autoscaler's shortfall +0.2%, the 95th percentile +0.3%, the minutes over the line +0.9%; no LOSS against omni-v16.

## The rows against native that read LOSS (the engine's, at every beat)

Read by the one key, these rows read LOSS against native in our models (every seed's paired interval clear of zero):

- the cloud's setting, every 5 s: pods waiting for a place +101.8%.
- the cloud's setting, every 15 s: pods waiting for a place +124.4%; the 95th percentile +0.5%; the minutes over the line +2.3%.
- the cloud's setting, every 30 s: pods waiting for a place +127.1%; the 95th percentile +0.4%.
- the kind benchmark's setting, every 5 s: pods waiting for a place +248.9%.
- the kind benchmark's setting, every 10 s: pods waiting for a place +251.9%.
- the kind benchmark's setting, every 15 s: pods waiting for a place +309.5%.
- the kind benchmark's setting, every 30 s: pods waiting for a place +316.5%.
- the kind benchmark's setting, every 60 s: pods waiting for a place +290.6%.
- the kind benchmark's setting, every 75 s: pods waiting for a place +256.2%.
- the kind benchmark's setting, every 90 s: pods waiting for a place +243.4%.
- the kind benchmark's setting, every 120 s: pods waiting for a place +175.1%.

They are the engine's at every beat, the main engine's included, and stay on the next version's list (`docs/CHANGE_CONTROL.md`)
to be root-caused, beside the blink model's alert minutes (LOSS against native at 60 s in every gate since omni-v13).

## The monitors scale with the beat

- The exporter (`tools/omni_exporter.py`) serves `omni_heartbeat_seconds`: the beat the governor runs at, measured as the median
  time between its last eleven full decisions, so a skipped slot moves it little (`tests/test_omni_exporter.py`, every beat from 5
  to 120 s).
- The governor's Grafana screen (`deploy/grafana/omni-compass.json`, eighteen panels) shows the beat and counts the time since the
  last decision in beats of that setting (yellow past one and a half, red past three).
- The staleness alert (`OmniGovernorStale`, `deploy/prometheus/omni-compass-rules.yaml`) fires after three beats as measured: 180 s
  at the main engine's 60 s, 45 s at 15 s, 360 s at 120 s; the other rules count in minutes and hours, not decisions.
- The live engine page carries the dial (the page's section 2d, "The heartbeat dial"): every beat beside native, from the ladder, with the
  real runs' place; its manual reads it (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, section 7.4).
- The control panel (`tools/omni_control.py`) carries the dial as a button: `POST /v1/beat {"seconds": 5 to 120}`, role
  operator, one console button for each stop (5, 15, 30, 60, 75, 90, 120 s); like a dial press it hands every setting back
  and starts the governor again at the new beat, and it serves the beat as `omni_control_beat_seconds`
  (`tests/test_omni_control.py`).
- Every run writes its beat beside its files (`omni_interval.txt`); the receipts read each arm at its own and record it
  (`tools/live_reps.py`, `"beats"`), and a three-run table names the beat its compass arm ran at (`tools/confirm_abc.py`).

## Every place that starts the governor

The parser's default (`--interval 60`, `--floor-interval 5`); the rigs (`scripts/kind_bench.sh` `OMNI_INTERVAL`, `kind_paired.sh`,
`kind_robust.sh`, `kind_levers.sh`, `kind_full.sh`, `kind_pilot.sh`); the install files (`deploy/install/omni-compass.yaml`,
`omni-compass-cloud.yaml`, `deploy/controller.yaml`); the cloud runs, which start it through `kind_bench.sh`; and all three
manuals. The levers rig gives each phase the 3, 2 and 3 minutes its checks were written for, three, two and three decisions at
60 s (`tests/test_pace_clocks.py`).

## At 60 s it is omni-v16 at 60 s

omni-v17 changes no gain, preset or muscle, and one rule only at beats slower than 80 s: at any beat up to 80 s set on the
command line it makes omni-v16's decisions at that beat (the cruise wait's count is unchanged there), and at 60 s those are
omni-v15's (4,578 audit records on the model cluster, none different, `results/model_gate/V16_VS_V15.md`). The model gate against
omni-v16 (every model that sets its own period reads identical to omni-v16 on every gauge and every seed (9 models and the verdict); as shipped, omni-v17 at its 60 s against omni-v16 at its 15 s, every gauge reads STEADY; no LOSS against omni-v16.). The brain's C++ twin takes the period on every call and is unchanged (`results/SEAL.json`); the brain's
lock takes no amendment.

## The real runs

`docs/PACE_PREREGISTRATION.md`, amendment 3 (written before any omni-v17 run): workflow `benchmark-reps`, eight arms in every
repetition on the same runner in an order rotated by repetition (native; Omni-Compass on top at the main engine's 60 s; the same
deciding every 5, 15, 30, 75, 90 and 120 s), the reruns' steady scenario, three runs of 10 repetitions on GitHub's own machines
at no cost, released by the conductor as the campaign's entry `kubernetes decision pace`. Each beat is read against native and
against 60 s by the one key; a row that reads LOSS at any beat against native is named on the dial's page and root-caused like
any other. Every benchmark runs again on omni-v17 at 60 s (`scripts/reruns.txt`), and the Kubernetes preregistration takes its
amendment of the same day (`docs/K8S_COMPASS_PREREGISTRATION.md`).

## Next: each beat's own combination

The founder's words: the engine "can always be tweaked, tuned, and turned with any knob, any button", and "when you do this inside,
you might need to click and change and turn certain things to achieve a more optimal state with a different combination of
buttons". The per-beat tuning is the next study, in the model first, on development seeds: at each beat, the combination of the
other settings that reads GAIN with no LOSS against the main engine's tune at that beat; a combination that does lands as the
next version, as that beat's card, never forced.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
