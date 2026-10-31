# The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

One row of the Kubernetes add-on test read LOSS on the engines that stood on 18 October: the mean wait for a serving pod to
start under KEDA's HTTP add-on. This page is that row's root cause, measured from the runs' own files. It sets out the
mechanism and its exact decomposition, says what it predicts on a fleet of separate machines, and records the rig amendment
that takes the test machine's own limit out of both arms. The engine is not changed. The row is never cut: every table that
read it stands as recorded, and every page names it.

## 1. The row

The test (`.github/workflows/kind-addons.yml`, `docs/K8S_COMPASS_PREREGISTRATION.md`) runs native as KEDA with its HTTP add-on.
In the http setup the add-on scales php-apache on the requests in flight. The omni arm is Omni-Compass on top of the same. On
omni-v10, the three-run table of the http setup read the mean pod start wait **LOSS in all three of our runs** (+13.0%, +14.1%,
+21.1% a pod). In the same three runs the total start wait read STEADY, pods started fell 24%, the response time fell 57% (mean)
and 72% (95th percentile), and CPU used rose 50 to 54% (power given). On omni-v11, two runs of the same setup have landed. The
third runs to its end on the rig it started on. Under the other setup, both (the CPU target and the requests in flight), the
mean pod start wait, pooled over the repetitions, was lower in the omni arm on both engines (−7.8% on omni-v10, −6.3% on
omni-v11; section 3).

## 2. What a pod start is made of

From Kubernetes' own timestamps in each repetition's pod watch (`pod_watch.json`), every serving pod created and made Ready
inside the measured window splits into three phases:

- **scheduling**, created → PodScheduled: the scheduler's choice of a node.
- **node side**, PodScheduled → container running: the kubelet, the pod's sandbox and network, and the image.
- **app and probe**, container running → Ready: php-apache's start and its readiness probe (TCP on port 80, every 2 s).

`tools/pod_phases.py` reads them and places each start by two things: the host's busy share over that start (`host_cpu.csv`,
the real machine under kind) and whether its node already carried a Ready serving pod when the pod was created. The receipt
is `results/live/POD_START_PHASES.md`: 741 starts in five runs, three on omni-v10 (39108180989, 39115242861, 39123583570) and
two on omni-v11 (39148024948, 39157778756). Kubernetes stamps these times in whole seconds, so one start is read to ±1 s and
the ranges below are over every stratum holding more than one start:

| Phase | Node already serving | Empty node |
|---|---:|---:|
| scheduling | 0.00 to 0.02 s | 0.00 to 0.20 s |
| node side | 0.72 to 0.94 s | 6.94 to 11.86 s |
| app and probe | 0.49 to 0.86 s | 0.40 to 0.91 s |

The whole difference is the node side on an empty node. php-apache runs `registry.k8s.io/hpa-example`, named without a tag,
so its pull policy is Always. On a node that already serves, the kubelet asks the registry for the image's digest, finds
every layer on the node, and starts the container in under a second. On a node that never served, it downloads the image
and unpacks it, and that takes 7 to 12 s.

## 3. Why the omni arm's starts took longer: the exact decomposition

Let s run over strata, each a band b of the host's busy share (0 to 0.5, 0.5 to 0.7, 0.7 to 1) paired with the node's state
(empty or already serving). For arm a, let p[a,s] be the share of its starts in stratum s and W[a,s] their mean wait. Then the
change in the mean wait splits exactly in two:

ΔW̄ = W̄[omni] − W̄[native] = Σₛ (p[omni,s] − p[native,s]) · W[native,s] + Σₛ p[omni,s] · (W[omni,s] − W[native,s])

The first term is the shift of starts into other strata, a busier host or an empty node. The second is the wait at the same
host load on the same kind of node. Where native has no start in a stratum, the first term takes the omni arm's own wait there
(W[native,s] := W[omni,s]), and the two terms still add to ΔW̄ exactly. `tests/test_pod_phases.py` checks the identity on a
constructed run.

| Engine, setup | Native W̄ | Omni W̄ | ΔW̄ | Shift into other strata | Same stratum |
|---|---:|---:|---:|---:|---:|
| omni-v10, http | 8.52 s | 9.94 s | +1.42 s (+16.7%) | +1.57 s | −0.14 s |
| omni-v11, http | 8.62 s | 9.27 s | +0.65 s (+7.6%) | +1.64 s | −0.98 s |
| omni-v10, both | 2.64 s | 2.43 s | −0.21 s (−7.8%) | −0.35 s | +0.14 s |
| omni-v11, both | 2.99 s | 2.80 s | −0.19 s (−6.3%) | −0.26 s | +0.07 s |

Under the http setup, every rise in the mean is the shift: 21 of the omni arm's 68 starts on omni-v10, and 11 of its 44 on
omni-v11, began while the host was at least 70% busy. Native's starts never did. At the same host load on the same kind of
node, the omni arm's starts were as fast as native's or faster (−0.14 s and −0.98 s). These numbers are pooled over the runs'
repetitions, so they differ a little from the table's paired means. They are shown, never judged. The judged row stays the
three-run table's.

## 4. The mechanism on one machine

A kind cluster is one machine. All seven nodes (a control plane and six workers) are containers on one 4-core GitHub runner,
and they share its processor and its disk. Omni-Compass conveys idle processor to the serving pods: it raises their CPU
limits in place. That is the work behind the response-time GAIN, and it shows as CPU used, power given. On kind, that
processor is the same one on which every node unpacks an image. A pod placed on an empty node therefore unpacks its image on
a processor that the conveyed pods on other nodes are keeping busy. Unpacking is processor and disk work, so it took longer:
the node side on an empty node rose from 6.9 to 7.9 s with the host under half busy to 10.4 to 11.9 s with it at least 70%
busy. omni-v7's shared-host guard (`omni_controller/capacity.py`) already holds every new raise while the runner is 75% busy
or unread. It cannot move the unpacking off the processor the raises already granted are using.

## 5. What it predicts on a fleet of separate machines

This section is a prediction, not a measurement. On a fleet, each node is its own machine. A new pod's image is unpacked on
its own node's processor, and the processor conveyed to pods on other nodes does not touch it. A pod placed beside pods
already serving finds the image on its node and starts in about the time this rig measures for such a pod (1.3 to 1.7 s in
total). So the coupling in section 4 is a property of the single machine. It is a test machine's limit, never Omni's result,
and the row that showed it is reported as measured. The cloud sets (Azure now; Google and Amazon behind their $0 check) run
every node on its own machine, and they measure it.

## 6. The amendment (2026-10-18): the served image pulled onto every worker before each arm

On kind, before each arm and before the governor starts or the window opens, `scripts/kind_bench.sh` applies an image
pre-puller (`deploy/kind/prepull.yaml`). This is a DaemonSet with one pod on every worker, which pulls `registry.k8s.io/hpa-example`
as an operator's image pre-puller does on a production fleet. The bench waits until the pre-puller's pod is ready on every
worker, then deletes it. A pre-puller that does not finish on every worker fails the arm's checks, so the arm is marked
invalid and never runs on the other rig. Each arm's `preflight.txt` records `images=pre-pulled on every worker before the arm`
and the digest each worker pulled.

- **The same in both arms.** Every worker carries the image before either arm is told apart.
- **The operator's manifests are left as written.** `deploy/kind/demo.yaml` still names the image without a tag, so the
  kubelet still asks the registry for its digest at every start, in both arms. It then finds every layer on the node.
- **Not the engine.** No fingerprinted file changes: the pre-puller is the rig's, and it moved no engine's digest (`python3 tools/omni_version.py`).
- **Not the clouds.** On AKS, GKE and EKS every node is its own machine and unpacks on its own processor. Their sets keep
  `demo.yaml` and their rig as their A, B and C started.
- **Never two rigs in one table.** A kind workflow's run on omni-v11 counts toward its three only when the run's own commit
  carries the pre-puller (`RIG_FILE` in `scripts/dispatch_grid.py`, read from GitHub at that commit). That covers the core
  benchmark, the seven Kubernetes repetition sets, the large organisms, fixed capacity, KEDA's add-ons, CruiseKube,
  Goldilocks and the robustness pair. Their omni-v11 runs on the rig before run to their end, since nothing is cancelled, and stay as their own record. `tools/confirm_abc.py` reads the
  rig from every arm's preflight record and heads any table whose A, B and C ran on different rigs with that fact. The
  grid's squares with the real cluster inside count runs by protocol, carried in each run's name. This rig is protocol 4
  (`KUBE_PROTOCOL`), and no omni-v11 run with the cluster inside had started on protocol 3, so all of theirs run on it.

## 7. What the next runs are expected to show (written before any of them)

On the amended rig, a serving pod on an empty node should start in about the time one beside a serving pod takes, about 1.3
to 1.7 s in both arms. The host's busy share should then stop deciding the wait. Whatever the three runs read is the
reading. A LOSS is root-caused again and never cut.

## 8. Threats to validity, and what stays

- **Every worker carries the image**, including workers no serving pod would reach in a given repetition. That costs disk
  before the window and nothing inside it.
- **The registry is still asked for the digest** at every start, in both arms (pull policy Always, as the operator wrote
  it). The round trip is inside the 0.72 to 0.94 s node side measured on nodes already serving.
- **The host still couples the arms' other work.** Conveyed processor still shares the runner with the kubelets, the probes
  and the load generator. omni-v7's shared-host guard and the window's refusal rules stand as before.
- **The batch jobs' small image** (`busybox:1.36`, about 4 MB) is still pulled on first use inside the window, as before. It
  unpacks in well under a second.
- **The model gate carries the old rig.** The conveyance model's pod start time (`start_time` in `tools/model_gate.py`: 8 s up to
  half busy, rising to 12.4 s near the top) was fitted to the omni-v6 KEDA run's 151 starts. That curve is the empty-node
  unpacking of section 4 in model form, and it is why the gate reads the pod start wait under conveyance LOSS (+9.0% on
  omni-v10 and omni-v11, `docs/OMNI_V11.md`). The curve is refit from the first amended-rig KEDA runs' own files, never
  guessed. Until then the model's start-wait row reads this coupling, not the governor.

## 9. Reproduce

```
scripts/raw_archive.sh open /addons-run-39108180989/ /addons-run-39115242861/ /addons-run-39123583570/ \
                            /addons-run-39148024948/ /addons-run-39157778756/
python3 tools/pod_phases.py addons-run-39108180989 addons-run-39115242861 addons-run-39123583570 \
    addons-run-39148024948 addons-run-39157778756 \
    --engine addons-run-39108180989=omni-v10 --engine addons-run-39115242861=omni-v10 \
    --engine addons-run-39123583570=omni-v10 --engine addons-run-39148024948=omni-v11 \
    --engine addons-run-39157778756=omni-v11 --out results/live/POD_START_PHASES.md
```

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
