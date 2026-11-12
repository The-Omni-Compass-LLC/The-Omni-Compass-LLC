# Change control: how the engine changes, and how a result stays tied to the engine it ran on

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The engine is the set of files whose bytes decide what Omni-Compass does: the brain, the compass law, the verdict, the live
governors, the harness the models run in, and the wires that fasten the brain to an outside simulator. Their SHA-256
digests together make the engine's fingerprint (the engine that stands, `OMNI_V26.json`: 65 files, digest `75d3c22eed4473b9`).
`python3 tools/omni_version.py` reads the tree and names the engine it holds, or says which file differs from every
declared engine.

## The rules

1. **Any change to a rule, a gain, a guard, a preset or a muscle makes the next version.** No engine file changes inside a
   version. A fix to a fault found in the engine is the next version, never a patch to the one that stands.
2. **Every change goes through the model gate first** (`tools/model_gate.py`, `results/model_gate/`): the shipped controller on
   the model cluster in the cloud setting, conveyance on one kind host set to a real run's own regime, the verdict on noisy
   work, the same seeds, paired against the engine that stands. A LOSS there is root-caused and fixed in the model; a
   change that reads no LOSS and shows promise goes to its GitHub trials; nothing is dispatched before.
3. **A version lands in one command**, `python3 tools/land_engine.py vN --since <UTC>`: the fingerprint, the version list,
   the conductor's campaign (`scripts/reruns.txt`), the grid's manifest and workflows, the package version (0.N.0), the
   root list and a release group. `tools/land_engine.py --check`, run by `verify.py`, refuses a push in which any of those
   places still names an older engine.
4. **Every benchmark runs again on the new version**, A, B and C, released by the conductor in a fixed order; a run is
   counted on the engine its own commit carries, read from GitHub at its head commit.
5. **No result is read across versions.** A three-run table is one engine's three runs (the table tools refuse to call
   runs on two engines one table); an older table stays its own engine's record, in `results/live/` until each
   benchmark's three runs on the new version land, then the newest table is the one shown.
6. **Every fix lands as the next version, and the founder is told.** A change that reads no LOSS in the model gate lands at once
   as the next version (the founder's order of 19 October, night: "Of course I want you to land version 12 ... every time you
   do that ... it becomes a new version"); he is told what it changes, why and what it read, and is not asked whether to land
   it. A change that reads a LOSS anywhere is root-caused and fixed in the model first and never lands as it stands.

## The record

| Version | Landed (UTC) | Digest | Files | What changed, and why |
|---|---|---|---:|---|
| omni-v5 | 11 Oct 22:40 | `6093b2b88aa911b9` | 44 | the max as the default brain on the 1,107-muscle catalog; re-declared while in development |
| omni-v6 | 15 Oct 06:18 | `df6147466ef18046` | 45 | shared-host capacity: on kind the host's processor counted once |
| omni-v7 | 15 Oct 15:25 | `d6d467b824c585f1` | 46 | conveyance bounded by the namespace's CPU quota; every rule in seconds |
| omni-v8 | 17 Oct 15:39 | `f93d233136a1f902` | 46 | CityLearn: a battery whose building has outages stays native (its charge is the building's reserve) |
| omni-v9 | 17 Oct 22:21 | `7379f3a79ff2c475` | 47 | CityLearn: the battery wire reads the coming hour; the exact Student t |
| omni-v10 | 18 Oct 04:23 | `4bf39b0d707784de` | 47 | CityLearn: the battery glide that cuts the bill most with no LOSS |
| omni-v11 | 18 Oct 16:03 | `745aa53ec8eeb67b` | 47 | Kubernetes: a reading with no machine in service is held, never read as an overload |
| omni-v12 | 20 Oct 00:30 | `d38b58fbe28939b8` | 47 | Kubernetes: a raise the cluster's admission refused is held, not written again at every check; the swarm's proximity reflex at once (its wire outside the digest, declared with the version) |
| omni-v13 | 20 Oct 20:31 | `0088837333c6f0fc` | 47 | Kubernetes: the CPU limits the conveyance gave go back to the operator's on a shared host at its top beside another workload's room; every other pod counted by its own limit |
| omni-v14 | 21 Oct 04:47 | `7afba44615fcff8f` | 47 | Kubernetes: a knob that leaves any one muscle native; the operator's own commands run without a shell |
| omni-v15 | 22 Oct 02:30 | `0a53cdd7a558f803` | 55 | the brain: the power cap's request trims only while the response line has been clean for the governor's own clear time (the omni-v11 long run's 126 switches in 350 decisions); every wire that holds a governor's rules in the fingerprint (eight taken in, their bytes as they stood) |
| omni-v16 | 22 Oct 07:30 | `5c5502f12b1c0ce4` | 55 | the Kubernetes governor: every clock in seconds (the brain's minute and its C++ twin, the compass's damping and smoothing, the edge, the additions past the floor, a command's minute to land, the host's busy share, the heat law, one batch job a minute, the conveyance every 15 s, the loop's own schedule), so the decision period is a clean setting; the heartbeat, the full decision, every 15 s by default (the founder's word, "15 sec all over"), the fast checks every 5 s; at 60 s exactly omni-v15's decisions; the pace read by its own runs (`docs/PACE_PREREGISTRATION.md`) |
| omni-v17 | 23 Oct 17:00 | `7c937d09e4031cc7` | 55 | the Kubernetes governor's heartbeat a dial, the main engine every 60 s (the parser's default; omni-v16's was 15 s), any beat from 5 to 120 s, every beat shown beside native (`results/model_gate/V17_LADDER.md`, the live engine page's 1j); the monitors scale with the beat (`omni_heartbeat_seconds`, the alert at three beats, the panel's `/v1/beat`); the cruise wait never under two readings (at 90 and 120 s it had rounded to one, found by the dial's own ladder before it landed); the founder's order of 22 October, afternoon |
| omni-v18 | 24 Oct 02:51 | `1cb92edb64c4391d` | 62 | Omni direct taken into the engine: the seven rule files of Omni-Compass's own orchestrator fingerprinted, the three arms shown together (`docs/OMNI_V18.md`) |
| omni-v19 | 24 Oct 16:54 | `36ee67284c035235` | 62 | the pod muscle of its own (`--own-replicas`) for a workload no autoscaler governs; the models' arm by itself (`docs/OMNI_V19.md`) |
| omni-v20 | 25 Oct 13:24 | `1df07f8e36a97985` | 62 | the five data stores' wires fixed at their causes (sysbench's own statements, Kafka's hand-back within a poll round, YCSB's cache growing back while it misses) (`docs/OMNI_V20.md`) |
| omni-v21 | 25 Oct 17:30 | `b658f05d43c1e602` | 63 | the immune system knows itself, knob by knob: a knob redlining past its line that Omni-Compass cannot bring back goes to native when native's twin reads it lower (`docs/OMNI_V21.md`) |
| omni-v22 | 30 Oct 18:30 | `0e23a0bc561b900a` | 65 | the five data stores' wires at the max, through each store's own account of a miss; the governor's hand-back tried five times against a transient failure of the cluster's API (`docs/OMNI_V22.md`) |
| omni-v23 | 31 Oct 20:00 | `c96ea4105d8747db` | 65 | Omni direct keeps every muscle Omni-Compass cannot be: a workload's own scale write the cluster refuses three times in a row hands the knob back to native's own pod autoscaler, made from the operator's target and range (the founder's order of 31 October; `docs/OMNI_V23.md`) |
| omni-v24 | 2 Nov 01:30 | `66c8f2d94b3e4725` | 65 | the factory beat for its place: with no beat set, the Kubernetes governor reads the cluster's nodes at its start and decides every 10 s on site and every 60 s through a cloud (a reading that fails keeps 60 s, a beat set by hand always wins), the pick of a rule frozen before any reading (docs/PACE_PREREGISTRATION.md, amendments 4 to 6); the model gate against omni-v23: no LOSS; eleven of twelve models identical; on site the minutes over the line down 60.7% and the 95th percentile down 8.2% (GAIN) |
| omni-v25 | 3 Nov 21:00 | `cf56fc0a7b707452` | 65 | the Kafka wire's producer started before the governor's thread: from omni-v22 the forked producer inherited a lock that thread held and never sent a message, so every Kafka run on GitHub stopped at the job's 150-minute limit; a producer that overruns its schedule now stops its workload with the reason; the governor's decisions byte for byte omni-v24's (`docs/OMNI_V25.md`) |
| omni-v26 | 7 Nov 14:31 | `75d3c22eed4473b9` | 65 | another workload's waiting pods hold native's target: when a service's target stood below native's and pods waited, the decision returned native's target without starting the immune hand-back's hold, so a batch queue's normal waiting flipped the web service's target every one or two decisions and the flips kept extra web pods in room the queue was owed; the decision now starts the hold when the waiting pods include a workload's no autoscaler governs (`docs/OMNI_V26.md`; the model gate identical on all 104 readings, no LOSS) |

Each version through omni-v15 was a fault found in a real run and fixed, omni-v16 made the decision pace a clean setting
and set the heartbeat at 15 s on the founder's word, and omni-v17 made the heartbeat a dial with the main engine at 60 s on his
word the same afternoon; each version since, omni-v18 to omni-v25, is the row above it in the table: the record is in
`docs/OMNI_V6.md` through `docs/OMNI_V26.md`, and each model gate's reading in `results/model_gate/`. Twelve versions in twelve days is the cost of fixing every fault the day it is
found (the founder's order of 18 October: every fault fixed, none set aside); the rules above are what keep that pace from
mixing results.

## What stability means here

A version is stable for a benchmark when its three runs on that version have landed with no change in between. omni-v25
has stood since 3 November 21:00 UTC, when its campaign opened; its three-run tables go into `results/live/V25_*.md` as they
land. Every older engine's tables stay its own record under its own name (`results/live/V<n>_*.md`), never read as omni-v25's. The engine's proofs (`docs/ENGINE_PROOFS.md`), its coverage
(`docs/ENGINE_COVERAGE.md`) and its reproducibility check (`tools/reproduce.py`) are run on every push, so a version that
stands is also a version that is re-proved, re-tested and re-built from its receipts each time anything else changes.

## Gaps this page names

- Up to omni-v14 the fingerprint held three of the outside-simulator wires (`tools/run_citylearn.py`, `tools/run_pandapower.py`,
  `tools/run_kil.py`); the other wires that hold a governor's rules (the data stores' `tools/run_redis.py`,
  `run_kafka.py`, `run_pgbench.py`, `run_sysbench.py`, `run_ycsb.py`, and `tools/run_swarm.py`, `run_mujoco.py`,
  `run_cpu_power.py`) were versioned by git and tested, but a change to them did not move the digest. Closed in omni-v15
  (21 October): every one of them is in the scope (`tools/omni_version.py`, 55 files), and a version declared before them is
  read without those eight wires and only those: any other file its list does not name still makes the tree a different engine.
- A wire outside the fingerprint carried a fault: the swarm's proximity reflex (`tools/run_swarm.py`) slowed a drone over a
  second where its own comment says at once, and on a mission draw outside the preregistered seeds it let drones collide
  (`results/model_gate/V12_SWARM_REFLEX.md`). Its fix is a change to a guard, so by rule 1 it was a version, not a patch: it
  landed as part of omni-v12 and is declared in `docs/OMNI_V12.md`, although the file's bytes do not move the digest; a
  swarm table counts only on a commit that carries it.

## The next version's list

Each change below was found in a real run or in our own reading of the code, and each has its evidence written down. Each
goes through the model gate against the engine that stands and, when it reads no LOSS there, lands at once as the next version
with `tools/land_engine.py`; the founder is told what it changed (rule 6). Landed in omni-v25, under the standing order that every fault found is fixed: the Kafka wire's producer started before the governor's thread, so the runs that had stopped at the job's limit since 30 October hand in their files again (`docs/OMNI_V25.md`); in omni-v24, on the founder's orders of 23 and 31 October and his word of 1 November: the factory beat for its place,
10 s on site and 60 s through a cloud, the pick of the pace preregistration's frozen rule (`docs/OMNI_V24.md`); in omni-v23, on the founder's order of 31 October: a knob whose
own-scale writes the cluster refuses handed back to native's own autoscaler, so the organism never runs with a knob nobody moves
(`docs/OMNI_V23.md`); in omni-v17, on the founder's word of 22 October, afternoon: the
heartbeat a dial, the main engine every 60 s, every beat shown beside native (`docs/OMNI_V17.md`); in omni-v16, on his word that morning: every clock of the
Kubernetes governor in seconds, the decision pace a clean setting, the heartbeat every 15 s (`docs/OMNI_V16.md`); in omni-v15, from this list: the power cap's
request through the line's own clear time, every wire in the fingerprint, and the kill test's 300 s reading declared
(`docs/OMNI_V15.md`; a dwell with a glide was refused by the gate and is not in it); in omni-v14: the operator's commands
without a shell, beside the founder's knob for every muscle; refused there by the gate and kept on the branch
`v14-convey-study`: no conveyance raise on a reading that leaves out another workload's starting pods (`docs/OMNI_V14.md`,
section 3); in omni-v13: the conveyance's hand-back on a shared host at its top, found on KubeRay's rig
(`docs/OMNI_V13.md`); in omni-v12, from this list: the refused raise held and the swarm's reflex at once (`docs/OMNI_V12.md`). The kind rig's governor role still does not read the namespace's
quotas, a grant the Operator's Manual, section 5.5, makes optional, so the omni-v12 capacity runs read the hold in the real
cluster.

| Change | Why | Evidence so far |
|---|---|---|
| The Redis harness's brain in its own process, as a deployment runs it | the brain thread shares the load generator's interpreter lock | `docs/TAIL_LATENCY.md`, section 4 |
| The verdict keeps a step only when the upper end of every 95% interval of its change in cost is inside the allowance (`omnicompass/verdict.py`), its reference measured long enough, from its own spread, to show a free step within the allowance; a trial that could not be read in its time is never started | today a step is kept when its estimated cost is within the 2% allowance even if the interval reaches past it: at the noise measured on the omni-v10 tables (the spread of the log response time 0.43 to 0.46), a give-back that truly costs 3% is kept about 31% of the time, 5% about 15% (found by the live-engine session, 19 October) | 89 kept steps on the omni-v10 data-store tables had an interval reaching past 2%, none read LOSS in a table. The strict form was built and read in the model gate (branch `v12-verdict-study`): on work fast enough to read a step (200 pieces a decision) a free step was kept 98% of the time against omni-v11's 66%, a 3% step 0% against 26%; but on the model cluster set from a real run's regime (about 80 requests a decision, about 4,000 needed a phase) no give-back trial started and the governor read identical to native, the machine-hour cut gone, and on the data stores (one sample a second, 40 to 120 a phase; 432 to 23,430 needed, read from the omni-v11 audits) every knob would stay native. Refused as written; the row stays open until a trial design that reads a 2% step in a trial's time is shown in the model gate |
| The Kubernetes governor counting a worker an add-on marks while it serves, and keeping its clock under load | the CruiseKube runs of 18 and 19 October | the recorder's fix of 19 October (`CHANGELOG.md`) |
| The governor's other costs on a saturated shared host | one saturated KubeRay repetition with no raise during its queue still read +4.0% on the batch pods' hashing; the governor's decisions (every 60 s then and again from omni-v17, every 15 s on omni-v16) and their reads run on cores the kind nodes share through the control plane | one repetition is not a reading: the omni-v13 runs of the batch rig read it, pod by pod, before any change |
| The pods that wait for a place, in the cloud's setting and in the kind benchmark's | in the model's cloud setting (the tune-down, machines alone) the pods wait for a woken machine longer than native's at every decision pace, the old 60 s default included: pending pod minutes an hour native 8.2, every 60 s 20.9, every 15, 10 and 5 s 18.4, 15.9 and 16.5: more pods waiting, LOSS against native at every pace (up 95% to 155%); the omni-v15 gate read the same row at 15 s up 111.7%, LOSS; in the kind benchmark's setting (the compass law at the max) about four times native's at every pace (32.0 at 60 s, 33.5 at 15 s, 28.8 and 28.6 at 10 and 5 s) | `results/model_gate/V16_PACE.md`, `results/model_gate/V16_VS_V15.md` (cluster15); the real cloud sets' pod start waits to be read beside it when their tables land |
| The cloud setting's small cost in response time and alert minutes | in the model's cloud setting (the tune-down, machines alone), against native, read by the one key: at 15 s the 95th percentile up 0.47% on the 5 s plant and up 0.36% on the gate's 15 s plant (STEADY, under the 0.5% floor) and the alert minutes up 2.31% on the 5 s plant (LOSS, more minutes over the line); at 60 s the 95th percentile up 0.49% on the 5 s plant (STEADY) and up 0.63% on the gate's plant (LOSS), the alert minutes up 1.85% (LOSS); against 60 s each reads STEADY, so the engine's, not the pace's; the blink model's alert minutes read up 2.35% against native at 60 s (LOSS) in the gates from omni-v13 on (on omni-v25's gate they read GAIN, the row below) | `results/model_gate/V16_PACE.md`, `results/model_gate/V16_VS_V15.md` (cluster15, cluster_shipped, cluster_blink); the cloud sets' alert minutes are a judged row of every receipt |
| The model's web model brought to the batch rig's 3-core host from a real run's files | in `convey_batch` both engines read 2% to 3% fewer requests served than native, with no batch at all as well, while KubeRay's real runs read 4% more after the queue; the same model reads the alert minutes 9.8% and the job turnaround 0.05% above native's (LOSS) in every gate since omni-v13's | `results/model_gate/V13_VS_V12.md` to `V17_VS_V16.md`; the regime to be set from the KubeRay runs' own after-queue files before the model is read for that gauge |
| The pod start wait in the convey models | against native the pods start 8.99% slower, 10.0% at the 95th percentile (LOSS), in every gate since omni-v8's, while the host serves 64% more requests at a 53% lower 95th percentile; omni-v7's page wrote it as the price of the busier host's work, but a wait that rose is a LOSS by the key | `results/model_gate/V8_VS_V7.md` to `V17_VS_V16.md` (convey, convey_unreadable_quota); the KEDA real runs' start wait, read with the rig's pre-puller (`docs/POD_START_WAIT.md`) |
| The card models' 95th percentile | on the modelled card the 95th percentile reads 2.38% above native's where the voltage falls with the clock and 5.78% near the voltage floor (LOSS), in every gate since omni-v15's, where the models were added; the 99th percentile STEADY, the card's energy 4.7% and 1.3% lower (GAIN), the limit written 17 and 35 times a run | `results/model_gate/V15_VS_V14.md` to `V17_VS_V16.md` (card, card_floor); the GPU runs on Lambda read the real card |
| The brain's dwell and its wait after an addition at the fast beats | omni-v16 restated both in seconds (at 15 s, 4 and 20 steps for the 1 and 5 a minute); the live-engine session (branch `claude/interactive-animated-charts-icvnsw`, 22 October) reports on its own sweep, on-site at 5, 10 and 15 s, machine-hours up 3.8%, 3.4% and 2.9% against native (more machines put in, power given) where a build counting them as readings that agree read from down 1.0% to up 0.9%, the pods waiting the same; the main engine's 60 s is untouched by it | not yet reproduced here; a search of the dwell counted in readings at each beat, in the tune study's rule (`docs/THE_TUNE.md`, section 4) |
| The cloud's floor check and a warm reserve | the same session reports two faults under `--give-back-only`: a floor that orders machines the cloud has already deleted is read as a command that did not land and holds every give-back, and give-backs made before the largest requests of the last hours are read leave too few machines; with both fixed its build read identical to native in the cloud setting at every beat, where the engine that stands reads the pods waiting, the 95th percentile and the alert minutes LOSS at some beats | not yet reproduced here; candidates for the cloud setting's LOSS rows (the rows above), through the model gate |

**Read again on omni-v25 (4 November; the model gate `results/model_gate/V25_VS_V24.md`, class S).** Three rows above were read on
older settings and stand corrected here, and six open items named on other pages join the list:

| Change | Why | Evidence so far |
|---|---|---|
| The pods that wait for a place, at the max (the cloud's setting from 31 October) | against native, native's 7.311 pending pod-minutes an hour against 8.247 at the main engine's 60 s and 11.565 at 15 s: up 12.80% and 58.18%, LOSS; the row above reads the struck tune-down | `results/model_gate/V25_VS_V24.md`, the cluster models |
| The card's 99th percentile | against native, up 0.94% on the modelled card and 4.59% near the voltage floor, LOSS (the row above reads it STEADY) | `results/model_gate/V25_VS_V24.md`, `card` and `card_floor` |
| The blink model's alert minutes | now GAIN against native, down 22.54% (26.625 to 20.625 minutes over the line, fewer minutes a person is paged): the LOSS the cloud-cost row names (up 2.35%) no longer stands | `results/model_gate/V25_VS_V24.md`, `cluster_blink` |
| The verdict's false acceptance | at 20 pieces of work a decision a give-back step that truly costs 3% is kept 28% of the time and one costing 5% 14%, a free step 60%; at 200 pieces 26%, 7% and 66% | `results/model_gate/V25_VS_V24.md`, the verdict model; the strict form refused on 19 October (`v12-verdict-study`) |
| The trade between muscles judged on the organism | the founder's order of 19 October (`DISCLOSURES.md`, section 3): no code, model or row yet | `omnicompass/verdict.py` (each muscle judged on itself) |
| The immune system on every knob | the founder's order of 24 October: it stands on two knobs, the Kubernetes autoscaler's target and the Kafka wire | `omni_controller/controller.py` (`_immune_native`), `tools/run_kafka.py` |
| `--give-back-only` leaves the engine | the order of 31 October struck the cloud's rule and said the flag leaves with the next version; it is still in the governor | `omni_controller/controller.py` (`apply_give_back_only`) |
| The cloud's beat and the work per dollar in the cloud model | through a cloud no beat was admissible on the corrected ladder (every beat raised the machine-hours, every beat but 90 s the pods waiting); the cloud model sends a fixed load and reads no bill, so it cannot read the work per dollar a cloud tune is judged by | `results/model_gate/V23_LADDER_CORRECTED.md`, `docs/PACE_PREREGISTRATION.md` amendments 4 to 6, `docs/THE_TUNE.md` |
| Kafka's 20 s notch | the burst's peak queue up 30.6% at run C's setting, inside the seeds' spread | `docs/OMNI_V22.md` |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
