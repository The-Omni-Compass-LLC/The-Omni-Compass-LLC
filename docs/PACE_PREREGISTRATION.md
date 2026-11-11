# Preregistration: the decision pace of the Kubernetes governor (omni-v16)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

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

## Amendment 6 (31 October, night): the model's stand-in corrected; the ladder read again on it, in the cloud and on site

The model's stand-in cluster (`pilot/selfpilot.py`) listed its pods with none of the metadata a real cluster gives every pod and as
one repeated object per workload, and took only the autoscaler's target among the governor's writes: the governor's count of the
room beside a workload failed on its first pod (4 to 7 of its decisions a day lost on the 5 s plant), every running pod of a workload
read as on one machine, and the raise of the autoscaler's range never landed. It is corrected (`tests/test_model_standin.py`). Every
ladder and gate read before the correction ran on the faulty stand-in and stands as its own record, none of them picking the factory
beat: omni-v17's and omni-v23's ladders (`results/model_gate/V17_LADDER.md`, `V23_LADDER.md`), the gates to omni-v23, and the
live-engine session's reading of 31 October, whose 10 s candidate dropped 163 decisions against 23 at 60 s on the gate's seeds (six
times the decisions, six times the drops) and was not landed.

On the founder's words of 31 October, night ("You pick and find out"; "you're supposed to see one in 99, 5 in 95, 10 in 90, and tell
me which one is the best result for an organism"), amendment 4's run is read again on the corrected model, unchanged in every other
way: the same twelve beats, seeds 101 to 108, one day, omni-v23's rules (the candidate tree it runs on decides as omni-v23 at any
beat set on its command line). It is read in both places: in the cloud (`pace_cloud`, the plant with the cloud's own autoscaler, at
the max; amendment 5) and on site (`pace_onsite`, the kind rig's own machines made at the start, no cluster autoscaler; amendment 5).
Amendment 4's frozen rule picks each place's beat. Beside every beat stand the response time's tails read from every request the
model answered, the 90th, 95th and 99th percentiles (the worst 10, 5 and 1 in 100), shown and never added to the rule. The pick is
then read on the untouched seeds 1 to 8 against omni-v23 at its shipped 60 s and lands only through the model gate with no LOSS.
Written while the run was under way (started at 20:27 UTC on the corrected tree): the cloud's rows at 60 s and 5 s had been seen,
and so had readings at 10 s and 20 s taken on the same corrected model by the tune study (`docs/THE_TUNE.md`); the rule was frozen
before any of them, and none of it changes.

**The picks, read and landed (2 November).** By amendment 4's rule on the corrected model: on site every beat was admissible and
10 s the one no other dominated; through a cloud no beat was admissible (every beat raised the machine-hours against native, every
beat but 90 s the pods waiting), so the cloud's factory beat stays 60 s (rule 4). The on-site pick was read on the untouched seeds
1 to 8 against omni-v23 at its shipped 60 s (`results/model_gate/V24_VS_V23.md`, the model `onsite_shipped`: the same seeds, plant
and beats as `--pace-periods 60,10`): no LOSS against native or against 60 s (against 60 s the minutes over the line down 60.7%, the
95th percentile down 8.2%, the autoscaler's shortfall down 5.1%, GAIN; the machines the same). It landed as omni-v24
(`docs/OMNI_V24.md`): the factory beat for its place, read from the cluster's own nodes. The real runs of this preregistration read
it from omni-v24's campaign on: the compass arm on kind at the factory's 10 s, 60 s one of the dial's arms.

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

The record of this amendment's run (written into the repository on 2 November 2026, the founder's order that every number stands on its record): `results/model_gate/V23_LADDER_CORRECTED.md`, rendered by `tools/beat_ladder.py` from `results/model_gate/V23_LADDER_CORRECTED_SOURCE.json`. On site the runs ran on the omni-v23 tree (commit a278eac262); through a cloud on the candidate tree of 31 October (commit ebf83ecaf9), which runs every pace exactly as omni-v23 (it writes the cover's floor as a knob at the factory's 0.6 and strikes the machines-only rule; every run sets its own beat and none passes the machines-only flag).


## Amendment 7 (11 November 2026, 07:20 UTC, written before any reading of its runs): the beat on a moving load, on the engine that stands

What the record shows, all read before this was written. On real Kubernetes the Omni index reads omni-v21 (its compass arm deciding
every 60 s) 28.0% and omni-v25 (every 10 s on site, the factory beat since omni-v24, picked from our own models) 20.5%; all nine
Kubernetes tests read lower on omni-v25, and native's own values in the two campaigns are alike (the 95th percentile on KEDA's live
requests: native 423 to 515 ms on omni-v21, 474 to 508 ms on omni-v25), so the arm on top moved: Omni-Compass's own 95th percentile
went from 115 to 136 ms to 249 to 283 ms there, from 287 to 311 ms to 369 to 457 ms on the wandering demand. On the steady load the two
engines read alike (30.9% and 30.8%), and amendment 3's real runs on omni-v25 (runs 41751100166, 41767230735, 41780364813,
`results/pace/PACE.md`, the steady load only) read every slower beat, 15, 30, 75, 90 and 120 s, GAIN against the 10 s factory beat on
the response time and the time over the line, none LOSS, the machines the same. The beat is the one change to how the Kubernetes
governor acts on kind between the two engines (omni-v23's own-pod guard acts only on a refused write); it is the suspect, not yet the
cause.

**The runs.** `benchmark-reps.yml` on main at the engine that stands (omni-v26), the wandering load of the Kubernetes campaign
(`scripts/reruns.txt`, "kubernetes wandering": `duration_s=2700`, `loadgen=open`, its load steps), four arms in every repetition, in an
order rotated by repetition, on the same runner: native, the compass arm at the factory beat (10 s on site), and the compass arm
deciding every 60 s and every 90 s (`compass60`, `compass90`, `scripts/kind_paired.sh`); ten paired repetitions a run, three runs:
A 42977431782, B 42977442687, C 42977447533, dispatched at 07:09 UTC on 11 November.

**The reading.** Each beat against native and against the factory beat, by the one key (`tools/readings.py`), the tables written by
`tools/confirm_abc.py` from the three archived runs. The pick is amendment 4's frozen rule read on these real runs: admissible, no gauge
LOSS against native; among the admissible, the beat no other dominates on the service gauges (the 95th percentile, the time over
the line, the alert minutes, the pods waiting), pairwise in the same repetitions; a tie goes to the fewest reads of the cluster. If a
beat other than 10 s dominates the factory beat here and on amendment 3's steady runs, it is the on-site factory beat of the next
engine version, landed through the model gate with the model's kind setting set from these runs' own files (the rule of 15 October:
a model's regime is set from a real run's own files, never guessed), and every Kubernetes benchmark runs again on it. If none
dominates, the factory beat stays and the drop from omni-v21 is root-caused elsewhere, written here.

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
