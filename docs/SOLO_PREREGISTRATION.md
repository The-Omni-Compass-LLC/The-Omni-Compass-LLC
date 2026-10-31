# Preregistration: Omni-Compass by itself, the third arm

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written and committed before any run of the arm, on the founder's order of 23 October: "a whole other Omni-Compass by itself,
without any Kubernetes or any schedulers or any governors, running direct muscles ... there's native, there's Omni and native,
and then there's Omni by itself, which we're going to add. That means the one that said Omni before is going to have to add the
words 'and native' ... a whole new set of monitors for every gauge and dashboard and Grafana ... so that the metrics are
following with real benchmarks." Nothing in the rules below changes after the first run of the arm starts; a change is an
amendment, written and dated here before the run it governs.

## The three arms

| Arm | Its words on every page | Its key in the records | What governs every muscle |
|---|---|---|---|
| native | native | `native` | the organism's own controllers, as shipped |
| Omni-Compass and native | Omni-Compass and native | `omni` (unchanged, so every record already written reads as it did) | Omni-Compass on top of the native controllers: the arm every table has carried since 26 September |
| Omni-Compass by itself | Omni-Compass by itself | `solo` | each muscle's own native controller switched off; Omni-Compass the only controller that moves the knob |

**What "by itself" switches off.** The controller of each muscle's own knob: on Kubernetes the pod autoscaler and the Cluster
Autoscaler; in our models each plant's own loop (a pool's autoscaler, a room's PI loop and its staging, a battery's dispatch, an
axis's PID). What stays is the organism itself: on Kubernetes the API server, the scheduler and the kubelet place and run the
pods in every arm, because without them there are no pods; "without any Kubernetes" holds only in our models. Omni-Compass never
touches the output directly: it moves knobs, and the muscles make the output, in every arm.

**The knob's setting with native off** is the operator's own, as the system starts: a pool's starting size, a workload's
replica count as its manifest ships it, a service's configured setting. **Never below**, with no live native to stand on: never
below the operator's own setting and never below the floor (two machines a pool, one replica a workload). The max is still the
default brain; the dial's tune-down is the only arm that may give back below the operator's setting, and only above the floor.

## Where by itself is the same arm, and where it is not run

- **The same arm, native being a setting and not a controller**: Redis (the memory ceiling), MySQL (the buffer pool), MongoDB
  (the storage engine's cache), the PostgreSQL pooler (its pool size), Kafka (the consumer group's size), and in our models
  every power cap, admission limit, setpoint and speed scale. Each table says so in one line; no run is repeated for it.
- **Native's own loop is the actuator and cannot be switched off**: the GPU's firmware, the robot's servo, the drone's
  autopilot, the grid's tap changer, and in our models the batteries' dispatch and the cooling units' staging. Each is labelled
  "native's own loop is the actuator: the same arm".
- **Not run: the cloud.** By itself, Omni-Compass would have to make machines with the cloud's autoscaler off; the order of 14
  October is that in a cloud it never adds a machine and only parks one the cloud made (`--give-back-only`), and every set costs
  money. A cloud arm by itself waits for the founder's word.

## What the engine that stands does by itself (read first, our own model)

On omni-v16 the governor moves a workload's pods only through the pod autoscaler's own object (its range and its target); with the
autoscaler switched off it has no pod muscle of its own: by itself it holds every workload at the operator's count and moves the
machines alone. `tools/solo_study.py` reads it on the toy cluster (class S), on the machines as the kind rig has them (every worker
made at the start, no cluster autoscaler), eight seeds of a day, the three arms on the same seeds; its page is written with the
version it reads, in `results/model_gate/`.

## The next engine version: a pod muscle of its own, and the arm in our models

1. **A pod muscle of its own** (`omni_controller/`): for a workload the operator names (`--own-replicas namespace/name`) and that
   no autoscaler governs, the governor sets the replica count itself through the workload's own scale, with the compass law on the
   pods' busy share inside the cover the pod autoscaler's target would have had (the operator's target, from the workload's
   annotation, down to 60% of it), more pods at once when the response line is crossed, fewer only after the workload's own
   window and never below the operator's count; restored to the snapshot at the end, every write audited and read back.
2. **The arm in our models** (`realms/`): a switch on each plant that holds its knob at the operator's setting with no native
   loop, and the arm `solo` in the harness beside `native` and `v5`, the bodies' twins static with it.
3. **The toy gate first** (the order of 15 October), against the engine that stands, on the same seeds: every existing toy must
   read identical (the new muscle acts only where the operator names a workload, the switch only in the arm `solo`), native and
   `v5` byte-identical on the development seeds of the realms (7100 and up), and the toy cluster read by itself against this page.
   A LOSS anywhere is root-caused and fixed in the model before anything is run.
4. **Landed** with `tools/land_engine.py` as the next version, and, by the standing rule, every benchmark run again on it.

## What is run once it lands

- **Real Kubernetes, on GitHub's own machines ($0)**: `ARM=solo` on the kind rig (`scripts/kind_bench.sh`): the pod autoscaler
  removed after the deploy, the workload at its manifest's count, the governor with its own pod muscle on it; in
  `benchmark-reps` beside native and Omni-Compass and native, the arms rotated by repetition, three runs (A, B and C) through a
  new block in `scripts/reruns.txt`.
- **Our models (class S)**: the realms (the seven organisms), the orchestra (the eighth), the grid with a third value in every
  square, and the whole stack's composition (the ninth body) with a third total.

## How it is read

Every comparison is paired within its repetition and read by the one key (`tools/readings.py`): Omni-Compass by itself against
native, Omni-Compass by itself against Omni-Compass and native, and Omni-Compass and native against native as before. GAIN, EVEN
or LOSS by the gauge's aim, power given for a resource spent that rose, the floor of half of one percent, the three-run rule.
Every row is reported, LOSS included; a LOSS is answered by finding where the mechanism or its wiring is wrong.

## Threats to validity

- The operator's own setting decides much of what by itself reads: a workload shipped at one replica starts far below its load.
  The setting is the one the rig's manifest and the toy's scenario already carry, frozen here; it is never tuned to a result.
- The muscle cards were found on top of native; by itself they run as they are, and a card found for by itself is its own
  version.
- Kind has no cluster autoscaler: on kind, native's machine count is static, so the machine muscle is the same in both
  Omni-Compass arms there; only the pods differ.

## Amendment 1 (31 October 2026, written before the runs it governs): the arm's pod writes were refused by the rig's own identity

**What the runs' own files read.** In every solo arm run on kind from omni-v19 to omni-v22 the governor's pod muscle wrote
nothing: each of its 15 decisions a window (one every 60 s over 900 s) ended in `kubectl scale deployment php-apache
--replicas=N` refused, `User "system:serviceaccount:omni-compass:omni-compass" cannot patch resource "deployments/scale" in API
group "apps"` (`controller.log` and `audit.jsonl`, `consecutive_failures` 1 to 15, in every repetition). The rig's identity
(`deploy/kind/rbac-omni.yaml`) granted `patch` on `deployments` by name; under Kubernetes' RBAC the scale subresource,
`deployments/scale`, is a resource of its own, and `kubectl scale` patches it. The preflight proved `patch deployment/php-apache`
and never the subresource, so it passed. The machine and conveyance muscles wrote as always (69 writes a window), so the window's
no-write check did not fire either. The workload stayed at the operator's count, one replica, in every solo window.

- omni-v21's three runs of the entry `kubernetes by itself` (benchmark-reps 40224674073, 40247823226 and 40269972665, 25 and 26
  October) were admitted by the rig of their day and are read in no table: their solo arm is void (an arm whose governor could not
  move the knob it is there to move), their native and Omni-Compass and native arms stand only as those runs' own record.
- omni-v22's first two runs (41115877114 and 41153103781, 30 and 31 October) were marked invalid in every repetition by a second
  fault in the rig itself: the end-of-window record added on 29 October reads the pod autoscaler (`hpa_end.json`), which the solo
  arm removes by design; the read failed six times over a minute and ended the arm with exit 1, so the arm's own words were never
  printed (`end_reads.err`: `horizontalpodautoscalers.autoscaling "php-apache" not found`). Both runs count as started in the
  campaign and are read in no table.

**What changes, in the rig only (no engine file moved; omni-v22 stood).** (1) The identity gains `get`, `patch` and `update` on
`deployments/scale` for the named workload alone (`deploy/kind/rbac-omni.yaml`; for a licensee `deploy/rbac-own-pods.yaml`, the
Operator's Manual, chapter 14). (2) The preflight proves the scale write by name in the "can" list and proves that the load
generator's scale is refused in the "cannot" list. (3) The end-of-window record of the solo arm reads the workload's own object
(`workload_end.json`) in place of the autoscaler it has removed. (4) `tests/test_kind_rig_rbac.py` fails a rig without any of
the three. The entry is queued again, A, B and C, in a new block of `scripts/reruns.txt` behind every entry of the campaign (the
rule of 18 October); its C of the first block runs on the amended rig. Under the founder's order of 25 October (Omni-Compass is
never by itself) the arm's table, when its three runs land, stays in the record (`results/live/`) and is not carried on the
front page or the benefit board, as the orchestrator's third arm is kept.

## Amendment 2 (31 October 2026, written before the runs it governs): Omni direct keeps every muscle Omni-Compass cannot be

**The founder's order of 31 October**, on reading that the arm by itself had read like native: "Omni direct is directly to
muscles, but Omni direct still might need an autoscaler like Kubernetes ... we still might need a muscle or two we're using. We're
going straight into all the muscles as the brain and orchestrator, scheduler and all that, but what Omni-Compass can't do and
needs the muscle for has to be achieved even in direct, so that it can work and do everything else ... Don't just embed some
shit and fail the whole system because we don't have the muscle to do something ... Direct means we directly talk to and
receive from the muscle, and give and use all; but any muscle that we don't have, Omni-Compass cannot be it: it has to be there,
if that's Kubernetes or whatever."

**What "by itself" means from this amendment on.** Omni-Compass talks to the muscles directly and is the brain, the
orchestrator and the scheduler wherever it carries those muscles itself. On a Kubernetes stack it carries none of those organs
(the founder's analysis of 31 October: "Omni-Compass is only a brain. It has no organs ... Omni-Compass would have to become the
Kubernetes mechanism to be what's considered direct"), so on Kubernetes the arm by itself is Omni-Compass's own pod rule in place
of the autoscaler's arithmetic and nothing else, never called direct, a mechanism test kept in the record and not a product arm;
the one test where the word holds is the orchestrator showing without Kubernetes. A knob's native controller is switched off in this arm
only where Omni-Compass carries that muscle and has proven, before the window, that it can move the knob (amendment 1's probe,
by name). Every muscle Omni-Compass cannot be stays in the arm, native, under it: on Kubernetes the API server, the scheduler
and the kubelet, and any autoscaler Omni-Compass has no muscle for on that platform (on kind the pod autoscaler is removed
because Omni-Compass's own pod muscle takes the workload; kind has no cluster autoscaler; in a cloud the arm is not run). A knob
left with no working controller fails the whole system and is never a result.

**What the rig does.** (1) The preflight proves the pod write by name before the window (amendment 1). (2) A window in which
any decision of Omni-Compass by itself failed is refused: by itself, a knob Omni-Compass owns has no other controller, so a
failed decision left that knob unmoved (`scripts/kind_bench.sh`, `INVALID RUN: by itself ...`; `tests/test_kind_rig_rbac.py`).
The three omni-v21 runs and the two omni-v22 runs of amendment 1 would have been refused by this rule at their first repetition.
(3) The engine's own answer, a knob whose writes Omni-Compass finds refused handed back to native's own controller so the
organism never runs with a hole, is omni-v23's guard (`docs/OMNI_V23.md`, landed 31 October through the model gate against
omni-v22, `results/model_gate/V23_VS_V22.md`, identical on every gauge): at three refusals in a row the governor makes native's own
pod autoscaler from the operator's target and range recorded on the workload and leaves the workload to it; the rig refuses such a
window as a result of the arm by itself (the organism kept a controller; Omni-Compass did not run the arm by itself), and the
identity may create an autoscaler in the workload's namespace for that hand-back alone.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
