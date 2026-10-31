# The orchestrators on the same organisms, with the same injection: preregistration

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written on 25 October 2026, before the recorded run. Our own models, evidence class S: a reading here is a model's, never a
benchmark result.

The founder's order of 25 October: "all the orchestrators to have the same injection ran through. Those orchestrators sit on the
same organism. And there lies the third arm. The third arm is the same organisms with the Kubernetes bin pack, Volcano, Kueue,
Koordinator, KAI ... and all the other orchestrators that are to have the same injection and see how they orchestrate and govern.
And of course then OmniCompass on top of that same stack ... So the orchestrators get thrown in as showing what they do against all
the same organisms."

## 1. The question

On one organism, under one injection of work: what does each orchestrator do against Kubernetes alone, and what does Omni-Compass
do on top of each orchestrator? Every orchestrator meets the same machines, the same clients, the same jobs and the same random
numbers, so a difference between two arms is a difference between what they decided.

## 2. The three arms

| Arm | What runs on the organism |
|---|---|
| native | Kubernetes alone: its default scheduler places every pod, the service's HPA, and in the cloud the Cluster Autoscaler |
| the orchestrator | the same organism and the same work, every pod sent to the orchestrator the way its project documents it for that work, its shipped rule deciding what is admitted and where it goes |
| Omni-Compass on top | the orchestrator's arm with the shipped Kubernetes governor of the engine that stands (`omni_controller/`) on top, at the factory flags the kind rig runs it with (on-site: the compass law at the max, the service sensed and its processor limit conveyed; in the cloud: the tune-down, the machines alone, give-back only); it writes only what it writes on a real cluster and never an orchestrator's own objects |

## 3. The orchestrators and their rules

Each rule is written by us from the project's own release files and documentation; no orchestrator's code is in the model.

| Orchestrator | Its rule | Read from |
|---|---|---|
| the Kubernetes scheduler as shipped (native) | NodeResourcesFit LeastAllocated (weight 1), PodTopologySpread's default constraints (2), TaintToleration (3), each normalised over the feasible machines; ties at random | Kubernetes 1.35's default plugin weights |
| the bin-packing profile | NodeResourcesFit MostAllocated, every other plugin as shipped | `deploy/kind/binpack-scheduler.yaml` |
| Volcano v1.16.0 | actions enqueue, allocate, backfill; a plain Job's or Deployment's pods each in a PodGroup of one; overcommit's enqueue gate at 1.2 times the room; jobs in DRF order; nodeorder's leastrequested and binpack at weight 1 each, which on the processor cancel, so the best machines tie and one is taken at random; tainttoleration at 1 | `installer/volcano-development.yaml` at v1.16.0, its `volcano-scheduler.conf` |
| Kueue v0.20.2 | the operator's one ClusterQueue, nominal quota the workers' allocatable processor read at install (in the cloud the pool's largest size), BestEffortFIFO; a Job admitted whole (parallelism times its pod's request), its quota given back as its pods finish; the service's pods admitted one by one as workloads of one; admitted pods placed by the default scheduler | `scripts/kind_batch_queue.sh` (the ClusterQueue), Kueue's documentation |
| the KAI scheduler v0.18.6 | placement strategy binpack for the processor; a plain Job's pods scheduled one by one (no min-member set); its default queue; no PreferNoSchedule scoring in its default plugins | its `pkg/apis/kai/v1/schedulingshard_types.go` and its batch scheduling guide (in its repository, docs/batch) at v0.18.6 |
| Koordinator 1.8.0 | the operator's colocation profile: the batch pods best effort (BE) on batch resources, the service latency-sensitive (LS) through koord-scheduler; batch allocatable = the processor the machine reports x 60% less the LS pods' use, refreshed when it moves 10% or every 300 s; the BE pods held to 65% less the LS use on each machine and at the least processor weight (cpu.shares 2); LoadAwareScheduling's filter at 65% busy and least estimated use | `pkg/util/sloconfig/colocation_config.go`, `nodeslo_config.go`, `pkg/scheduler/apis/config/v1/defaults.go` at v1.8.0; `deploy/kind/koordinator-colocation.yaml` |

The Gödel scheduler, KubeRay, Crane, Karmada, Open Cluster Management and Armada run on GitHub's machines four ways
(`results/live/GOVERNORS.md`); each joins this model once its shipped default is read from its release, and nothing is written for
it here before that.

## 4. The organisms

Twelve injections, each from the benchmark that carries it, each run in two settings (24 organisms in all):

| Organism | The benchmark it carries | Window | Clients over the window |
|---|---|---:|---|
| steady | kubernetes steady | 900 s | 1 2 3 1 2 1 |
| wandering | kubernetes wandering | 2700 s | 1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1 |
| all_four | kubernetes all four | 2700 s | 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 |
| google_2011 | kubernetes google 2011 trace | 2592 s | the trace's 24 steps |
| climb | the founder's traffic rule | 1800 s | 1 2 3 2 3 4 3 4 5 4 5 6 5 6 7 6 7 8 |
| burst_1419 | the cloud's burst | 1800 s | 1 4 1 6 1 9 |
| burst_1618 | the cloud's burst | 1800 s | 1 6 1 8 1 6 |
| real_day | the cloud's real day (Google 2011) on 1 to 9 | 2592 s | its 24 steps |
| fairness | kubernetes fairness | 900 s | two services, each 1 2 3 1 2 1 |
| faults | kubernetes faults | 900 s | 1 2 3 1 2 1, the drill of `scripts/kind_faults.sh`: a machine down for 120 s at 15% of the window, the traffic x3 for 120 s at 35%, a runaway pod for 120 s at 55% |
| batch | kubernetes batch | 1500 s | the batch stream; the service deployed with its clients at zero, as the rig leaves it |
| one_body | the batch stream beside the service | 1800 s | the climb, with the stream |

| Setting | The machines |
|---|---|
| on-site | the kind rig: six workers that are containers on one runner, each reporting the runner's 4 cores, the pods sharing the 3 cores the governor's own leaves; no cluster autoscaler |
| cloud | machines of 2 cores of their own (1.9 allocatable), the Cluster Autoscaler at its defaults (10 s scan, a machine under 50% requested for 10 minutes removed when its pods fit elsewhere), 2 to 9 machines, 90 s to boot |

The service is the rig's php-apache (200m request, 500m limit, its HPA at 50%, 1 to 10 pods, the HPA's 300 s scale-down window),
60 ms of processor a request (the model gate's calibration), open-loop clients at 6 requests a second each; a request unanswered
in 10 s fails. The batch stream is the rig's: 24 jobs of 10 pods, 5 at a time, one every 30 s, 500m request and 1 core limit, 8.1
core-seconds of hashing a pod. The processor on a host is shared as the kernel shares it between cgroups, by the weight of each
pod's request (`tools/model_gate.py`, `water_fill`).

## 5. The injection and the repetitions

Eight repetitions on every organism. Repetition k takes its seed from the engine's jump generator, seed_k = (20261025 + k ·
0x9E3779B9) mod 2³² (`tools/engine_runs.py`), and every random number of the run (the clients' noise, every pod's work, every
response time's spread, every tie a scheduler breaks) is drawn before any arm runs; every arm of repetition k meets the same
numbers at the same moment, whatever it decides.

## 6. The gauges and the reading

| Gauge | Aim |
|---|---|
| the 95th percentile response time | time: a fall is a GAIN |
| minutes over the line (500 ms) | time over the line: a fall is a GAIN |
| requests failed | failed: a fall is a GAIN |
| requests served | work: a rise is a GAIN |
| pods waiting for a place (pod-minutes) | time waited: a fall is a GAIN |
| a job's turnaround; the stream's makespan | time: a fall is a GAIN |
| batch pods done | work: a rise is a GAIN |
| machine-hours; energy | a resource spent: a fall is a cut (GAIN), a rise is power given |

Every comparison is paired by repetition and read by the one key (`tools/readings.py`): the mean change, its 95% interval over the
eight repetitions (Student's t), the word by the gauge's aim, and under 0.5% STEADY. Three comparisons on every organism: each
orchestrator against native; Omni-Compass on top of each orchestrator against that orchestrator alone; and Omni-Compass on top of
each against native. Every row is shown, LOSS included; a run that fails is listed with its error.

## Amendment 1: the response time and the pods waiting, corrected in the model (written before the second run, 25 October 2026)

The first recorded run (kept whole: `docs/history/ORCHESTRATORS_FIRST_RUN_2026-10-25.json.gz` and `.md`) read Omni-Compass on top LOSS
in 26 rows on-site, on every orchestrator alike: the 95th percentile, the minutes over the line and the pods waiting rose wherever
the governor raised the service's pod ceiling (10 to 19) on a host already full. The fault was in the model, in two places, the
same in every arm:

- **The response time.** Each serving pod was read as a queue of its own on a fixed slice of the host, so on a full host every pod
  added made every answer slower. The kernel shares the processor without leaving any of it idle (work-conserving): a request
  alone runs at its pod's limit, or at what the host leaves, and never faster than one core (php-apache answers a request on one
  thread); the queue is the whole service's, on all the processor its pods can get together, however many pods it is split into:
  T = S/r₁ + (S/Cₛ)·ρ/(1 − ρ) + the backlog's wait, with S the 60 ms a request, r₁ = min(the pod's limit, Cₛ, one core), Cₛ the
  processor the service's pods can get together and ρ = λS/Cₛ. On a full host more pods neither speed an answer nor slow it, as
  the kind rig's own replica-room run found (`results/live/REPLICA_ROOM.md`: the cap raised to 30 served no more requests).
- **The pods waiting.** Every new pod was counted as waiting for its first 5 s step, because the HPA made it after the scheduler's
  pass. A pod waiting for a place is one the scheduler could not place, with no machine that has room: the HPA now acts before
  the scheduler's pass in each step, and a pod is counted only while it stays unplaced after it.

Nothing else changes: the organisms, the orchestrators' rules, the injection, the gauges and the reading stand as written above.

## Amendment 2: the Cluster Autoscaler acts after the scheduler's pass (written before the third run, 25 October 2026)

The second recorded run (kept whole: `docs/history/ORCHESTRATORS_SECOND_RUN_2026-10-25.json.gz` and `.md`) read Kueue in the cloud
using 11% to 35% fewer machine-hours than Kubernetes alone on organisms where nothing else differed. The fault was in the model:
amendment 1 moved the HPA before the scheduler's pass, and the Cluster Autoscaler, run between them, read every pod the HPA had
just made as one that could not be placed and added a machine for it, in every arm but Kueue's (whose new pods were not yet
admitted). The Cluster Autoscaler acts only on pods the scheduler has tried and could not place: it now runs after the
scheduler's pass. Nothing else changes.

## 7. Where it lives

`tools/orchestrators_arm.py` (the model), `tools/orchestrators_report.py` (the record and its page), `results/orchestrators/`
(`ORCHESTRATORS.json`, every run's gauges and every reading; `ORCHESTRATORS.md`, the page). The live counterpart is the four ways
on GitHub's machines (`kind-orchestrators.yml`, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6), where the batch stream goes
through each orchestrator on the same kind rig.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the
rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
