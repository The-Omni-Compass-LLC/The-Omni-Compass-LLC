# Preregistration: the decision pace of the Kubernetes governor (omni-v16)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written and committed before the runs, on the founder's word of 22 October ("Go"). The runs' commit is the one that
carries this file; nothing in the engine, the harness or this rule changes after the first run starts.

## The question

How often should the Kubernetes governor take its full decision? Every engine through omni-v15 decided every 60 s: the
period was written into the first harness on 26 September, with no reason recorded, and never measured against another.
Native's pod autoscaler checks every 15 s (the controller manager's `--horizontal-pod-autoscaler-sync-period`), the
metrics it reads refresh every 15 s, the Cluster Autoscaler scans every 10 s and KEDA every 30 s. The founder asked for
15, 10 and 5 s on 14 October; until now the period was not a clean setting, because rules counted in decisions changed
their meaning with it.

omni-v16 (`docs/OMNI_V16.md`, on main since 22 October) counts every clock of the governor in seconds, so the period changes
only how often it looks: the brain's own minute (its blending of each reading, its inner time, its dwell and waits, its
machines added or removed a minute), the compass's damping and smoothing, the edge's window and rates, the coast per
raise, the additions past the scheduling floor (a step a minute), a command's minute to land, the host's busy share
over a minute, the heat law's minute, one batch job a minute, the conveyance every 15 s whichever check falls due, and
the loop that keeps its own schedule (`tests/test_pace_clocks.py`, `tests/test_loop_schedule.py`). At 60 s it makes
exactly omni-v15's decisions (the model cluster, 4,578 records, none different); the conveyance's 15 s and the loop's
schedule are the only changes a run at 60 s can see.

## What was read first, in our own models (class S)

The model gate, before any run (`results/model_gate/V16_VS_V15.md`, `results/model_gate/V16_PACE.md`): omni-v16 against omni-v15
on every model, and omni-v16 alone at 60, 15, 10 and 5 s on a plant that moves every 5 s, in the cloud's
setting and in this benchmark's. A pace that reads a LOSS there is not run here.

## What is run

Workflow `benchmark-reps` on `main` (omni-v16), three runs (A, B and C) of 10 repetitions each, on GitHub's own
machines (no cost), released by the grid conductor as the campaign's entry `kubernetes decision pace`
(`scripts/reruns.txt`, in the first block, right after the steady test: its A with the first pass, its B and C with the
next two). Each repetition runs five arms back to back on the same runner, each on a fresh kind cluster, in an
order rotated by repetition (`scripts/kind_paired.sh`):

| Arm | What governs |
|---|---|
| native | Kubernetes alone (the HPA at its target, the scheduler); Omni-Compass not started |
| compass | Omni-Compass on top of native, the compass law at the max, at its default heartbeat: a full decision every 15 s (amendment 2) |
| compass60 | the same, a full decision every 60 s, every engine's period before omni-v16 |
| compass10 | the same, a full decision every 10 s |
| compass5 | the same, a full decision every 5 s |

The fast checks (the scheduling floor, the pod reflex, and the conveyance every 15 s) run every 5 s in every Omni arm.
The load is the reruns' steady scenario: 900 measured seconds an arm, a fixed rate (`loadgen=open`), the same work in
every arm; the line 500 ms at the 95th percentile. Each Omni arm ends with the reset, which must return every setting to
native with no record left (`scripts/kind_bench.sh`).

## How each pace is read

By the one key (`tools/readings.py`), from the three runs' receipts (`tools/live_reps.py`, `tools/confirm_abc.py`): each
pace against native, and each other pace against the compass arm at its default of 15 s, paired within the repetition. A row reads GAIN or LOSS
only when all three runs agree in sign with every 95% interval clear of zero; EVEN when an interval includes zero; and
"the runs disagree" when clear runs point different ways. A resource that rises (pods, machines, energy, the settings
commands, the governor's own processor) is power given, never a LOSS; it is shown and named.

## The rule that picks the default (frozen now)

The default becomes the fastest pace that meets all four:

1. In the model gate, no LOSS at that pace.
2. Against native: no row reads LOSS.
3. Against the 60 s arm: no row of work done, time waited, missed or failed reads LOSS or "the runs disagree".
4. Omni-Compass's own processor at that pace (the receipt's "Omni's own CPU (cores)", from the overhead record every
   Omni arm writes) stays under 0.1 of one core, a fortieth of the runner's four.

If no faster pace meets all four, the default stays 60 s, as omni-v16 landed it. A faster default is the next version,
omni-v17, under the standing rule (tested in the model first, told, not asked), and every benchmark runs again on it.

## What does not change

Native's own clocks, the harness, the scenario and every other rule. The cloud sets (Azure, Google, Amazon) are not part
of this choice, because they cost money; they run at whatever default lands.

## Threats to validity

- One scenario (steady, fixed-rate load) on kind: one runner whose nodes are containers on one host. A pace chosen here
  is the default everywhere until a scenario reads a LOSS at it, and then it is root-caused like any other.
- Below 15 s the processor numbers the governor reads repeat (metrics-server refreshes every 15 s): part of what is
  measured, not corrected for.
- The runs share GitHub's runners with the campaign; each repetition pairs its five arms on one runner at one time, so
  the queue changes no comparison.

## Amendment 1 (22 October, written before any run): how rule 1 reads the model

Rule 1 reads each pace as every model gate reads a candidate: against the engine that stands at its default, here omni-v16
deciding every 60 s, paired by seed (`results/model_gate/`); the paired reading is what says whether a pace adds anything. The
model's rows against native are printed beside them in full (`results/model_gate/V16_PACE.md`), and a row there that reads LOSS
goes to the next version's list (`docs/CHANGE_CONTROL.md`) to be root-caused as the engine's: it is the engine's trade at
every pace, the default included. Written once the model had read, before the first run, because "no LOSS at that pace" could
be read either way: in the cloud's setting the pods wait for a machine longer than native's at every pace, the default
included (pending pod minutes an hour: native 8.2, every 60 s 20.9, every 15, 10 and 5 s 18.4, 15.9 and 16.5), a reading of
EVEN at 60 and 10 s and of LOSS at 15 and 5 s only because the seeds' spread differs, while against the 60 s default each
faster pace reads EVEN. The reading kept is the model gate's own, the one every version since 15 October was landed by.

## Amendment 2 (22 October, written before any run): the founder sets the heartbeat at 15 s

Once the model had read (`results/model_gate/V16_PACE.md`: against 60 s, no LOSS at any pace in either setting; at 15 s the alert
minutes 14.7% fewer in this benchmark's setting and energy per core 2.6% less in the cloud's), the founder's word was "15 sec
all over heart beat fix update code". The default is therefore 15 s from omni-v16 on, set by him and not by this rule, and the
rule above no longer picks it: omni-v16 lands with its full decision every 15 s, not at the 60 s the rule above first left it. The runs stay as written, with the arms around the default: native, the compass arm at 15 s,
and the same at 60, 10 and 5 s (the table above, written before the first run). They read the heartbeat he set: each pace
against native, and 60, 10 and 5 s against 15 s. A row that reads LOSS at 15 s, against native or (on work done, time waited,
missed or failed) against 60 s, is root-caused and fixed in the next version, and he hears it, as every other.

## Amendment 3 (22 October, afternoon, written before any omni-v17 run): the beat a dial, the main engine at 60 s

The founder's word the same afternoon, once he had read the reads a day in the pace study (about 86,000 at 5 s against 39,700
at 60 s): the heartbeat is a dial. Any beat can be set, and every setting is shown beside native with what it buys and what
it costs, because an operator may want a fast beat for its reads and accept what it costs, or a slow one, and each beat may
want its own combination of the other knobs. The main engine decides every 60 s (omni-v17, `docs/OMNI_V17.md`). No rule picks
a default from these runs: he set it. No omni-v16 run of this entry had started when this was written.

The runs on omni-v17 carry eight arms in every repetition, in an order rotated by repetition, on the same runner:

| Arm | What governs |
|---|---|
| native | Kubernetes alone (the HPA at its target, the scheduler); Omni-Compass not started |
| compass | Omni-Compass on top of native, the compass law at the max, at the main engine's beat: a full decision every 60 s |
| compass5, compass15, compass30 | the same, a full decision every 5, 15 and 30 s |
| compass75, compass90, compass120 | the same, a full decision every 75, 90 and 120 s |

Everything else stands as written above: the fast checks every 5 s in every Omni arm, the steady load, the line, the reset.
Each beat is read against native and against the compass arm at 60 s, paired within the repetition, by the one key, three
runs of 10 repetitions; a repetition's job may run four hours (`.github/workflows/benchmark-reps.yml`). A row that reads LOSS
at any beat against native is the engine's at that beat: it is named on the dial's page (the live engine page, "The heartbeat
dial") and root-caused like any other, in the model first. The seven beats were read first in our own models
(`results/model_gate/V17_LADDER.md`), and that reading found one fault before the version landed: at 90 and 120 s the cruise
wait (120 s) had rounded to one decision, so one reading with a pod waiting put every machine in service. omni-v17 carries the
fix (the cruise wait never fewer than two readings; `docs/OMNI_V17.md`, section 3), so the compass90 and compass120 arms run
the corrected rule; every other arm's counts are unchanged by it.

## Amendment 4 (31 October, written before any reading of the ladder was seen): the factory beat read again on the engine that stands

The founder's words of 31 October ("60 seconds is a disadvantage, it's not a benefit ... we have to have the basic line engine
tuned to what we call the basic setting, and then we lock that, and anybody can turn and tweak it to another scenario"), under
his rule of 23 October that the factory beat is the best beat the sweeps read. The one ladder on record
(`results/model_gate/V17_LADDER.md`) read omni-v17, seeds 1 to 8, one day; on it every beat read pods waiting for a place LOSS
against native in both settings, the engine's fault fixed in omni-v21 (the immune hand-back on a waiting pod), so no beat was
admissible there and it picks none. On its service gauges 10 s read strongest against 60 s (the kind setting: the minutes
over the line down 18.4%, pods waiting down 9.9%, machine-hours down 1.4%; 20 s: down 14.7%, 6.8% and 0.8%), and that is a
reading of an engine that no longer stands, written here so the pick below is not steered by it.

**The run** (our own models, class S): `tools/model_gate.py --models pace_cloud,pace_kind --pace-periods 60,5,10,15,20,30,40,45,50,75,90,120
--seeds 101-108 --days 1` on the omni-v23 tree (the engine that stands from 31 October, evening), the tune study's development
seeds (`docs/THE_TUNE.md`, rule 4), the page written by `tools/beat_ladder.py` beside the gate's other records in `results/model_gate/`. Seeds 109 to 116 are
added in a second report only if the rule below leaves two beats that neither dominates; nothing else about the run changes
after it starts. Written at 16:40 UTC; the ladder's kind setting started at 16:47 UTC (its cloud setting, started with it, was
stopped at 16:47 when the founder struck the cloud's rule of 14 October, before any of its readings was written); this amendment
was committed before any reading of either was seen.

**The rule that picks the factory beat** (frozen now):

1. Admissible: a beat at which no gauge reads LOSS against native in either setting (`docs/THE_TUNE.md`, the admissible set;
   in the cloud setting the machine-hours stand for the bill and may not read power given).
2. Among the admissible beats, the one no other admissible beat dominates on the service gauges (pods waiting for a place, the
   95th percentile response, the minutes over the line, the pod autoscaler short of its target; the machine-hours in the cloud
   setting), each pair read against each other seed by seed by the one key (`docs/THE_TUNE.md`, dominance: no service gauge
   LOSS, one GAIN; nothing traded).
3. Where two or more beats remain and none dominates another, the one with the fewest reads of the cluster a day stands: the
   governor's own cost is the only tie-break, and the service is never traded for it.
4. If no beat is admissible, the factory beat stays at 60 s, every LOSS row goes on the next version's list with its cause, and
   nothing is picked from a faulty reading.

The beat picked is a candidate, not a result: it is read in the model gate on the untouched seeds 1 to 8 against omni-v23 at its
shipped 60 s (`--pace-periods 60,<beat>`), lands as the next version only where it reads no LOSS there against native and
against 60 s, and then the real runs of this preregistration read it: amendment 3's arms, the compass arm at the new factory
beat and 60 s one of the dial's arms. The development reading is written on the ladder's page before the gate runs, and the
seeds are not changed after.

## Amendment 5 (31 October, written before the ladder's cloud half runs on it): the cloud setting at the max

The founder's order of 31 October (no hard rule; the cloud at the max; `CLAUDE.md`, Orders of 31 October) struck the cloud's
tune-down on the machines alone of 14 October. From this amendment the model gate's cloud setting is the max with every muscle
on top of the cloud's own autoscaler (`tools/model_gate.py`: the compass law at the max, the service sensed, the lever parking
and waking what exists, the autoscaler alone adding machines), and the ladder's cloud half (amendment 4) is read on it; a cloud
half read at the tune-down on 31 October before this amendment is not used for the pick. Rule 1 of amendment 4 reads the cloud
setting's machine-hours as the bill, aim lower. At the max the two settings are one model: the same plant (the 5 s plant with
the cloud's own autoscaler) and the same law; one seed (101) at 60 s read every model gauge identical in the two, only the
governor's own processor time differing (a measured time). So the kind setting's ladder, started at 16:47 UTC on the omni-v23
tree, is the reading of both, and nothing is run twice. The kind rig's own machines (every worker made at the start, no
cluster autoscaler: on site, machines already paid for) are a plant of their own; its ladder is written into the gate and
read under the same rule before the on-site factory beat is picked. The real runs of this preregistration are on kind and do not change; the Azure
sets take the same change in `docs/K8S_COMPASS_PREREGISTRATION.md` (the amendment of 31 October).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
