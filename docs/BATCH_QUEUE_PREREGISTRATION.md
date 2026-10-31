# Kueue and Volcano: Omni-Compass on top of a batch stream admitted by a queueing system of its own (preregistration)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on the night of 19 October 2026, before any run of this test, at the founder's order of that night: the governors
and orchestrators he named (Kueue, Volcano, Crane, Open Cluster Management, CruiseKube, Gödel, Armada, Karmada, the
Kubernetes scheduler as shipped, the KAI scheduler, Nephio, KubeEdge, KubeRay, and Koordinator) are each benchmarked with
the organism native under them, then Omni-Compass on top of them. This page is the first two, register row 63. Every
other Kubernetes set stays as it is; this is a new set beside them, on the engine that stands at the run's commit
(`python3 tools/omni_version.py`, recorded in every run).

## The question

When a stream of batch jobs is admitted by Kueue (Kubernetes SIG Scheduling; Apache-2.0) or placed by Volcano (the CNCF;
Apache-2.0), each as its project ships it, does Omni-Compass on top shorten the jobs' wait and turnaround, or hold fewer
machines or less energy, with no LOSS anywhere?

## What Kueue and Volcano are, and so what native is

- **Kueue** admits work a whole job at a time. A job carrying a queue's name is created suspended; Kueue admits it when its
  ClusterQueue has quota for every pod it asks for, and the Kubernetes scheduler then places the pods. Native is Kueue's
  release applied as published, with the operator's queue written as Kueue's own single-ClusterQueue example writes it:
  one ResourceFlavor, one ClusterQueue whose nominal quota is the workers' allocatable CPU and memory, read live from the
  cluster before the arms are told apart, and one LocalQueue in the namespace the jobs run in.
- **Volcano** is a batch scheduler of its own. Pods that name it (`schedulerName: volcano`) are grouped by its controllers
  and placed by its scheduler according to its queues, with its default queue and its default scheduling policy as
  shipped. Native is Volcano's release applied as published.
- In both arms the rest of the cluster is the batch test's (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendment 8): six
  workers, the service and its autoscaler (HPA target 50) beside the jobs, the service's load generator at zero.

## The arms (two, as always)

- **native**: Kubernetes with the queueing system; Omni-Compass is not started.
- **omni**: the same cluster and the same queueing system with Omni-Compass on top (`ARM=compass`), with the live muscles
  of the batch test: the node pool (a worker idled with the prefer-not mark, a pod that finds the open workers full lands
  on it at once, and nothing is evicted or moved), the service's autoscaler target and CPU limit, the rollout guard and
  the security hold, cruise (rule 7) and idle (rule 8). Omni-Compass writes nothing to Kueue's or Volcano's objects or to
  the jobs: its identity can read jobs and cannot write them, and has no rule at all for either project's resources
  (`deploy/kind/rbac-omni.yaml`; the `kubectl auth can-i` receipts in every run's `rbac_omni.txt`).

## The queueing systems, frozen

- Kueue **v0.20.2** (`manifests.yaml` from the release, SHA-256 `1ab14ecd590575ac57f50fa4cbcf529766bc2c32ba974bda1614381281ec52b4`)
  and Volcano **v1.16.0** (`installer/volcano-development.yaml` at the tag, SHA-256
  `9aa62e15541f5e955d73353da9321ab233a2cbe0f8fbac4b4a4d38ba497303ee`), fetched in every arm and refused unless the hash
  matches; kind v0.31.0 with Kubernetes v1.35.0, as every set.
- The release file is applied as published but for one thing, the same in both arms: every Deployment and Job of the
  queueing system is placed on the control plane, beside metrics-server and CoreDNS, before the file is applied, so the
  six measured workers carry only the work (Volcano's certificate Job ships with no placement). The run checks every pod
  of the queueing system is on the control plane (`scripts/kind_batch_queue.sh`).
- The stream's image (busybox 1.36) is pulled onto every worker before the arm begins and the puller removed before the
  window opens, as the served image is (`deploy/kind/prepull.yaml`), so a job's wait is the queueing system's and the
  scheduler's, never a download on the one machine all kind nodes share.
- `batch_queue.txt` records the release, the hash, the quota and every image the queueing system runs.

## The workload and the measure

- The stream (`deploy/kind/batch-stream-job.yaml`): 24 Jobs, one every 30 s from the window's opening, the same schedule
  in every arm; each Job runs 10 pods, 5 at a time, each pod hashing 3,000 MB (requests 500m CPU and 64 Mi, limit one
  CPU). The total is the batch test's: 240 pods of 3,000 MB.
- The six-worker kind cluster, a fresh cluster per arm, both arms back to back on the same runner in an order rotated by
  repetition; 120 s warm-up, 1,500 s measured; ten paired repetitions a run (`benchmark-reps.yml`, `workload=batch`,
  `batch_queue=kueue` or `volcano`).
- The four queue gauges (`tools/live_reps.py`, `job_stream`), each judged by its aim, a fall a GAIN:
  - a job's wait, from its submission to its first pod running, mean and 95th percentile (the queueing system's
    admission and the scheduler's placement together: the same measure for Kueue, which holds the job, and Volcano, which
    holds its pods);
  - a job's turnaround, from its submission to its last pod done, mean;
  - the jobs unfinished at the window's end.
  A job not started or not done by the window's end counts the window's end, never less.
- Beside them, every gauge of `tools/live_reps.py`, losses included: when the last job finished, the worker machines in
  service after it, machines in service and energy over the window, CPU with Omni-Compass's own, pods started, the
  service's response times.

## How it is read

- Each gauge's paired mean difference with its 95% interval: one whose interval is clear of zero is a difference in this
  run; one whose interval includes zero is no difference beyond the noise, and that is the result.
- One run (A) is a first reading. Runs B and C on the same commit make the three-run reading (`tools/confirm_abc.py`):
  GAIN or LOSS in all three of our runs, judged by what the gauge is for (a resource spent that rose reads power given), no
  difference beyond the noise, or the runs disagree.
- Wait, turnaround and response times are class L (measured on live software); machines are counted live; the watts are
  the declared model (class S), as in every kind set.
- A run is invalid, kept in the raw files and not counted, when a release file does not match its hash, a pod of the
  queueing system is off the control plane, Kueue refuses the operator's queue, Volcano's default queue never appears, the
  image is not on every worker, or a reset does not hand back the operator's settings.

## Known limits, said before the result

- No accelerators: GitHub's machines have none. The first plan for row 63 named KWOK-simulated accelerators, but a KWOK
  node runs no pod, so a job's wait there would measure no real work. This test runs real CPU work; the accelerators wait
  for a machine with cards (the GPU kit on Lambda, after the CPU side).
- Kueue holds a job whole and suspended until it is admitted, so its waiting work is invisible to anything that reads
  pods; Omni-Compass reads pods and never Kueue's own objects. Volcano holds pods, which wait Pending where the governor
  sees them. The difference is the systems', and the receipts show what each arm did with it.
- Kueue's quota is the workers' allocatable resources as kind reports them (each kind node reports the runner's
  processors), the same in both arms; on kind there is no node autoscaler for native, so native keeps all six workers.
- The other orchestrators of the founder's list take this rig one at a time, each with its own page before its runs
  (register rows 88 to 98).

## Amendment 1: the KAI scheduler (written before its first run, 20 October 2026)

The KAI scheduler (`NVIDIA/KAI-Scheduler`, NVIDIA, from Run:ai; Apache-2.0; register row 91) joins the rig as a third
queueing system (`batch_queue=kai`). It places pods by its own queues: a pod that names it (`schedulerName:
kai-scheduler`) and carries a queue's label (`kai.scheduler/queue`) is grouped with its job's other pods and placed by
KAI's scheduler under the queue's quota, limit and over-quota weight.

- **Native** is KAI's chart as published, installed by Helm, with the two default queues its chart makes on install
  (`default-parent-queue` and `default-queue`: quota 0, no limit, over-quota weight 1). The jobs go to `default-queue`.
- **Frozen**: the chart `oci://ghcr.io/kai-scheduler/kai-scheduler/kai-scheduler` at v0.18.6 (released 15 October 2026),
  its archive's SHA-256 `dff53248c4a044249a1f62ca8d35bd8dfc02719b99e302b35c69f946f4c5b7ff` pinned and refused otherwise.
- **Placement**: the chart's own setting places KAI's components (its operator applies it to the scheduler, the binder,
  the pod grouper, the queue and pod-group controllers and the admission webhook): every one on the control plane
  (`deploy/kind/kai-values.yaml`); any deployment the setting does not reach is placed there after install; the run checks
  every serving pod of KAI is on the control plane.
- **What it is not**: KAI's GPU sharing and topology placement need cards; this test is its queues and gang placement on
  CPU work. The cards wait for the GPU kit on Lambda.

- **Its runs**: in a workflow of its own (`kind-orchestrators.yml`, the same rig), whose A, B and C are started together,
  so they never take the place of a campaign run of `benchmark-reps.yml` (`scripts/reruns.txt` reads runs back by their
  count in a workflow).

Everything else is as written above: the stream, the window, the gauges and how they are read.

## Amendment 2: Koordinator (written before its first run, 20 October 2026)

Koordinator (`koordinator-sh/koordinator`, the CNCF; Apache-2.0; register row 89) joins the rig as a fourth system
(`batch_queue=koordinator`). It runs work by quality of service: its manager computes, on every node, the batch processor
and memory the latency-sensitive pods leave unused (its colocation, on by default); its scheduler places best-effort pods
on those batch resources; its node agent, koordlet, holds each node's best-effort work back when the latency-sensitive
pods need the processor.

- **Native** is Koordinator's chart as published, installed by Helm as its own guide installs it, colocation on as
  shipped, with the operator's two settings for a cluster with one control plane (`deploy/kind/koordinator-values.yaml`):
  its images from its GitHub registry (the chart's default is its Beijing registry; the same images), and its manager,
  scheduler and descheduler one replica each on the control plane (two each would ask the one control-plane node for three
  processors, more than it has free). koordlet runs on every node, the measured workers included, as shipped, in both arms.
  The jobs reach it by the operator's colocation profile, as Koordinator's colocation guide writes it
  (`deploy/kind/koordinator-colocation.yaml`): a labelled pod in a labelled namespace becomes best effort at the batch
  priority, for its scheduler, on batch resources. The service is not labelled and is not touched.
- **Checked before the window**: a server-side dry run of a labelled pod must come back best effort, for koord-scheduler,
  asking batch processor (its webhook fails open, so an unready one would let the stream through as ordinary pods); the
  answer is kept in the run's record.
- **Frozen**: the chart 1.8.0 from its charts repository's release, the archive's SHA-256
  `766011e7c797a5b2ea0ed2091b31efb4eb16ba14699189db304022336fc48e06` pinned and refused otherwise (the repository's index
  lists another digest for the same version; the archive the release serves is the one pinned and recorded).
- **What it is not**: Koordinator's purpose is a loaded latency-sensitive service and best-effort work on the same
  machines. Here the service stands idle, as in every batch test; the colocation of the two under load is its own test,
  written before it runs (register row 89).
- **Its runs**: in `kind-orchestrators.yml`, its A, B and C started together, as the KAI scheduler's.

Everything else is as written above: the stream, the window, the gauges and how they are read.

## Amendment 3: the Kubernetes scheduler alone, as shipped and with its bin-packing profile (written before its first run, 20 October 2026)

The Kubernetes scheduler (kube-scheduler, `kubernetes/kubernetes`, Kubernetes SIG Scheduling; Apache-2.0; register row 88)
places every pod of every Kubernetes set in the register; here it places the stream alone, with no queueing system between
the jobs and the nodes, in two settings, each its own table.

- **Native, as shipped** (`batch_queue=vanilla`): the cluster's own default scheduler, the image the kind node image carries
  for Kubernetes v1.35.0, its default profile untouched (its NodeResourcesFit scores a node higher the emptier it is, so the
  stream is spread). Nothing is installed; the jobs name no scheduler. The image is read from the control plane and kept in
  the run's record.
- **Native, the operator's bin-packing profile** (`batch_queue=binpack`): a second scheduler from the cluster's own release,
  as Kubernetes' own pages write one ("Configure Multiple Schedulers", "Resource Bin Packing";
  `deploy/kind/binpack-scheduler.yaml`): the kube-scheduler image the control plane runs, read from it on each fresh
  cluster; one profile, `binpack-scheduler`, whose NodeResourcesFit scores a node higher the fuller it is (MostAllocated,
  processor and memory weighted alike); every other plugin the release's default; one replica, so no leader election; on
  the control plane. The jobs name it (`schedulerName: binpack-scheduler`); every other pod, the service's included, is
  placed by the default scheduler as shipped.
- **Frozen**: the default scheduler is the node image's (kind v0.31.0, Kubernetes v1.35.0, as in every kind set); the
  bin-packing profile is the manifest above, its SHA-256 kept in each run's record with the image it ran.
- **Checked before the window**: the bin-packing scheduler stands (its rollout completes within five minutes) and is on the
  control plane, or the run is invalid, kept in the raw files and not counted.
- **Recorded at the end**: where the scheduler put every pod, node by node (`batch_queue_end.json`).
- **What it is not**: a scheduler places; it does not queue. Every job's pods are created as its parallelism allows and
  wait Pending only for room, so a job's wait here is the scheduler's alone. Each table is native against Omni-Compass on
  top for its own setting; the tables of different settings and different systems are not a ranking of the systems.
- **Its runs**: in `kind-orchestrators.yml`, the A, B and C of both settings started together, as the KAI scheduler's.

Everything else is as written above: the stream, the window, the gauges and how they are read.

## Amendment 4: Koordinator's runs repeated on the kubelet's cgroup root its own tests use (written before they were repeated, 20 October 2026)

Koordinator's first three runs (A 39352904186, B 39352911037 and C 39352918048, at commit 99c3002b3) are invalid, kept in the
raw files and not counted: in every repetition, in both arms, koordlet, Koordinator's node agent, crash-looped on every node,
its chart's install ran out of its fifteen minutes and no window opened, so nothing was measured. The cause is the cluster,
not Koordinator's setting: kind starts each node's kubelet with its cgroup root at `/kubelet`, where koordlet does not find the
pods' cgroups it reads; Koordinator's own tests on kind set the kubelet's cgroup root to `/` (`test/kind-conf.yaml` at v1.8.0).

- Koordinator's runs are repeated on that cluster (`deploy/kind/cluster-koordinator.yaml`: the same control plane and six
  workers, Koordinator's two patches copied as written), in both arms; every other set keeps kind's default. Each arm's files
  name the cluster it ran on (`kind_cluster.txt`).
- When koordlet does not stand, its own log is kept in the run's files (`koordlet.log`).
- Everything else is as amendment 2 writes it.

## Amendment 5: the governor's own core (written before any run on it, 20 October 2026)

The first three-run tables of the batch rig on omni-v12 carry one row against Omni-Compass. A job's mean turnaround rose
0.9% to 1.4% in all three runs of the Kubernetes scheduler as shipped and of its bin-packing profile (`results/live/V12_VANILLA.md`,
`V12_BINPACK.md`: LOSS), and 1.5% in run A of the KAI scheduler (`V12_KAI.md`; within the noise in B and C). The raw files
give the cause. In both arms the stream's pods went to the same nodes (six of six in the scheduler as shipped) and waited
the same 0.03 s to start; what grew was each pod's hashing, 1.3% to 1.5% longer with Omni-Compass on top (10.56 s → 10.70 s,
9.59 s → 9.74 s, 10.14 s → 10.28 s, the mean over each run's 2,400 pods), while the runner's processors were 1.3% to 2.8% busier.
On kind every node is a container on the one runner, and the governor, a process on that runner, competes with the node
containers as a peer group: its niceness ranks it only inside its own group. Its own work, its commands and the API
server's answers to them came out of the measured pods' processor time. On a real cluster the governor runs on its own
machine, and none of that reaches the workers.

- **The change, on the batch rig, the same in every arm**: the kind nodes on every core of the runner but the last (Docker's
  processor set, written once each node stands) and the governor alone on the last (`taskset`); in a native arm that core
  carries no governor. Each arm's preflight names the cores (`scripts/kind_bench.sh`, "the governor's own core"), and the
  three-run tool names a table's rig from it, so runs on the two rigs are never one table.
- **The runs before it stand as their own record**, read as written, LOSS rows included: the scheduler's two settings and
  the KAI scheduler (three runs each), and Koordinator's repeated runs. The governors' runs from here on are on this rig.

## Amendment 6: the four ways (written before their first run, 20 October 2026)

The founder's order of 20 October: "We can show what they do natively on top of the system organism. And show what
OmniCompass does on the organism without the orchestrator compare that. As well as put OmniCompass on top of the
orchestrator that's on top of the whole organism and benchmark that." Each orchestrator now runs four ways, all four in
every repetition, each on a fresh cluster of the same configuration, in an order rotated by repetition, on the governor's
own core (amendment 5):

- **nativebare**, the organism alone: the stream placed by the cluster's own default scheduler, no orchestrator installed;
- **native**, the orchestrator on the organism as its project ships it;
- **compassbare**, Omni-Compass on top of the organism alone (the default scheduler still places every pod; Omni-Compass
  works its own levers on top of it, as everywhere);
- **compass**, Omni-Compass on top of the orchestrator on top of the organism.

Each comparison is the first arm against the second, paired within the repetition, read by the one key for the first arm:

| Comparison | What it shows |
|---|---|
| compass against native | Omni-Compass on top of the orchestrator (the benchmark of the two-arm runs) |
| native against nativebare | what the orchestrator does on its own, natively, on the organism |
| compassbare against nativebare | what Omni-Compass does on the organism without the orchestrator |
| compassbare against native | Omni-Compass on the organism without the orchestrator, against the orchestrator |
| compass against nativebare | the two together, against the organism alone |

- **The systems**: the KAI scheduler, Koordinator (on its own kind configuration, amendment 4, in all four arms), Kueue,
  Volcano and the scheduler's bin-packing profile; the scheduler as shipped is the organism alone itself.
- **Its runs**: `kind-orchestrators.yml` with the arms `nativebare native compassbare compass`, ten repetitions a run, A, B
  and C started together, each orchestrator's in a block of its own in `scripts/reruns.txt`; one job holds the four arms
  (up to 330 minutes). The three-run tables are written per comparison (`tools/confirm_abc.py --pair first|second`).
- **What it is not**: a contest between Omni-Compass and an orchestrator for the same job. Omni-Compass never places a pod
  or admits a job; on the organism alone it sits on top of Kubernetes' own scheduler, and on the orchestrator it sits on top
  of the orchestrator. The comparisons show what each layer adds to the organism, each against the same organism.

Everything else is as written above: the stream, the window, the gauges and how they are read.

## Amendment 7: KubeRay (written before its first run, 20 October 2026)

The founder's list names KubeRay, the Ray project's operator for Ray clusters on Kubernetes (`ray-project/kuberay`,
Apache-2.0). The governor it brings is the Ray autoscaler: it adds Ray worker pods while tasks wait for processors and gives
back a worker left idle for its timeout. Register row 92.

- **Native, as its project ships it**: KubeRay 1.7.1, its operator's chart archive checked against its pinned SHA-256
  (`fd057c207a6be038f2fe1475abb87f43a8c091b77f1f563b4e8547a2404b5bc8`) and installed on the control plane by the chart's own
  placement settings (`deploy/kind/kuberay-values.yaml`); one Ray cluster (Ray 2.52.0, its image pinned by its index digest
  `sha256:5c31da4180403f2d5f4590d05fbd46c1345e91e8d33dd4ff616de2702b611b31`, pulled once by each runner and loaded into every node
  of each arm's fresh cluster, so no node downloads it inside an arm), from KubeRay's own autoscaling sample at v1.7.1
  (`ray-cluster.autoscaler.yaml`: the autoscaler in the head, upscaling Default, an idle worker given back after 60 s, the
  head taking no task) with the operator's three settings and nothing else changed (`deploy/kind/kuberay-cluster.yaml`): the
  head on the control plane beside the other systems' controllers; each worker pod the processor size of one pod of the
  Kubernetes stream (half a processor asked, one at most; its memory the sample's 1 GiB, which Ray's own processes need) and
  one Ray processor, so one task runs on one worker pod as one job's pod runs on Kubernetes; and the worker group's ceiling the
  workers' allocatable processors over half a processor, read live, as Kueue's queue is sized to the workers (the sample's 10
  was written for no cluster in particular).
- **The stream, the same work**: 24 jobs, one every 30 s from the window's opening, each of 10 units, 5 at a time, each unit
  hashing 3,000 MB: each job a RayJob (`deploy/kind/kuberay-job.yaml`) sent by KubeRay's operator to the one cluster over its
  own job API (HTTPMode: no submitter pod on the measured workers), its driver on the head (`deploy/kind/kuberay_stream_job.py`),
  its 10 tasks one Ray processor each on the worker pods the autoscaler adds.
- **The gauges, read the same way**: a job's wait from its submission (the RayJob's creation) to its first task begun (its own
  driver's record, the last line of its log), its turnaround to its end as KubeRay recorded it, and a job that has not
  succeeded by the window's end counted unfinished at the window's end (`tools/live_reps.py`, from `ray_times.json`); every
  other gauge of the batch rig unchanged.
- **The four ways**: the organism alone is the same work as Kubernetes Jobs placed by the cluster's own scheduler (amendment
  6), so "KubeRay as shipped against the organism alone" reads the same work run the Ray way against the Kubernetes way, in
  the same repetition.
- **Tried first**: one repetition through `kind-trial.yml`, never counted in any table, to see the rig stand before its A, B
  and C are started; a trial that shows a fault in the rig is fixed in the rig, the fix written here before the runs.
- **The runner's disk**: seven copies of the Ray image (about 2.5 GB each, unpacked) do not fit beside the runner's own
  toolchains, so a KubeRay job removes the toolchains it never uses before its first arm (`kind-orchestrators.yml`), the same
  for every arm of the job.
- **What it is not**: a test of Ray's own scheduling against Kubernetes'; Omni-Compass never writes KubeRay's or Ray's
  objects, never submits or holds a job, and sits on top with its own levers, as everywhere.

## Amendment 8: the Gödel scheduler (written before its first run, 20 October 2026)

The founder's list names the Gödel scheduler (`kubewharf/godel-scheduler`, ByteDance, Apache-2.0), a unified scheduler for
online and offline work: its dispatcher hands each pod to a scheduler, its scheduler matches pods and nodes with optimistic
concurrency, and its binder binds them, with units and gangs (PodGroups) as its own scheduling unit. Register row 93.

- **Native, as its project ships it**: Gödel publishes no release and no image, so each runner builds its image once, before
  the first arm, from its source at the pinned commit `90de2d0dd7e8e4dc99ef36b34b91a30fc171b368` (its main branch on 20
  October 2026) with the project's own Dockerfile (`docker/godel-local.Dockerfile`), as its setup guide builds it
  (`scripts/kind_godel_build.sh`); the image is loaded into each arm's control plane and its own manifests are applied from
  the same source as its guide applies them (kustomize, `manifests/base`: its CRDs, roles, and its scheduler, dispatcher,
  binder and controller manager, all on the control plane by the manifests' own placement), with nothing changed. The arm
  checks the source's commit and the image's ID before it loads it.
- **Kubernetes 1.24 for this system alone**: Gödel supports Kubernetes 1.21.4 to 1.24.6. Its four arms run kind v0.22.0, the
  last kind whose own node images include 1.24, with its image for 1.24.17
  (`kindest/node:v1.24.17@sha256:bad10f9b98d54586cba05a7eaa1b61c6b90bfc4ee174fdc43a7b75ca75c95e51`), the last patch release
  of the 1.24 line (patch releases change no API), kubectl v1.24.17, and metrics-server v0.5.2, the line metrics-server's own
  compatibility table gives below 1.25 (its manifest's SHA-256 `64bbd06c1b72cb08cffa9ebbe4cb4cfe61607e764a02e2ede573e7673fc0c401`,
  its image pulled through the old registry's own redirect). Kubernetes 1.24 resizes no pod in place, so Omni-Compass's power
  cap and processor conveyance do not exist on this cluster and are off in all four arms, as on Crane's 1.25
  (`docs/CRANE_PREREGISTRATION.md`; `scripts/kind_bench.sh` reads the cluster's API for it); this system's tables are read
  among its own four arms, never beside the 1.35 systems'.
- **The stream, the same work**: the same 24 jobs of 10 pods, each pod sent to Gödel by its scheduler's name with the three
  annotations its own guide puts on every pod it schedules (`godel.bytedance.com/pod-state: pending`,
  `pod-resource-type: guaranteed`, `pod-launcher: kubelet`); each pod is its own unit, as in Gödel's basic pod scheduling
  (the stream's jobs need no gang). The organism alone is the same stream placed by the 1.24 cluster's own default scheduler
  (amendment 6).
- **The gauges** are the batch rig's, unchanged; where Gödel put every pod and its components' last words are kept in every
  arm's record (`batch_queue_end.json`, `godel_*.log`).
- **Its runs**: `kind-godel.yml`, the four arms in every repetition, the governor on its own core (amendment 5); one trial
  repetition first (label `trial`, never counted), then A, B and C started together.
- **What it is not**: a test of Gödel's scale (its optimistic concurrency is built for thousands of nodes; here there are six)
  or of its quotas; Omni-Compass never writes Gödel's objects, never places or binds a pod, and sits on top with its own
  levers, as everywhere.

## Amendment 9: what the trials of 20 October found in the rigs (written after the trials, before the counted runs)

Three rigs were tried once each on 20 October (label `trial`, never counted); two faults were in the rig and one in the test
machine. Each is fixed where it was found, the same in every arm, before the counted runs start.

- **Gödel's rig: metrics-server rolled out twice** (run 39376949793, both arms). The bench applied metrics-server's pinned
  manifest and then patched the deployment twice (the kubelet's certificate unverified; the server on the control plane), two
  rollouts in a row; on Kubernetes 1.24 the first pod, deleted while its image was still coming through k8s.gcr.io's redirect,
  stayed terminating past the five-minute wait, and both arms were marked invalid before any stream ran. The bench now writes
  the rig's three settings into the pinned manifest and applies it once (one rollout; `scripts/kind_bench.sh`), naming the
  image by the registry that serves it (`registry.k8s.io`, the same image the old name redirects to). The manifest's SHA-256
  is checked on the file as fetched, as before; every rig, 1.35 included, applies metrics-server this way from now on.
- **KubeRay's rig: more workers than the machine holds** (run 39371908460). The trial's runner died 58 minutes in, mid-arm,
  and GitHub kept no log of it. The worker group's ceiling was the workers' allocatable processors over half a processor, 48 on
  this rig; each worker is 1 GiB, and a kind node reports the whole machine's memory as its own, so Kubernetes would admit 48
  workers of 1 GiB on a 16 GiB machine. The ceiling is now also bounded by the machine: no more 1 GiB workers than it has free
  at install, less 3 GiB kept for the head and the systems, both read live (`scripts/kind_batch_queue.sh`,
  `deploy/kind/kuberay-cluster.yaml`); the processor bound stands where it is the smaller. Where the ceiling bites, the Ray
  stream queues tasks in Ray rather than pods in Kubernetes, and the tables say which bound stood in each arm
  (`batch_queue.txt`).
- **The test machine: a runner lost mid-repetition** (Kueue C, run 39368401852, repetition 5; its runner died 80 minutes in,
  no log). The run's other nine repetitions landed whole and are read; its three-run table says C carries nine. No rig changed
  for it.

## Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again)

- **Gödel's rig: metrics-server never came up on Kubernetes 1.24** (runs 39438395275, 39438412522 and 39438430198, A, B
  and C; every arm of every repetition marked invalid before any stream ran: "0 of 1 updated replicas are available" for the
  whole five-minute wait, the same in all forty arms). The cause is in the rig, not in Gödel: kubeadm 1.24 taints the control
  plane twice, `node-role.kubernetes.io/control-plane:NoSchedule` and the older `node-role.kubernetes.io/master:NoSchedule`
  (1.25 drops the second), and the rig's metrics-server pod, pinned to the control plane, tolerated only the first, so it
  stayed Pending and the rollout never finished. On 1.25 (Crane) and 1.35 (every other rig) only the first taint exists, and
  the same pod ran. The pod now tolerates both (`scripts/kind_bench.sh`, the manifest patch and the coredns pin alike), the
  same in every arm and on every rig; nothing else of the rig changes. Gödel's three runs start again on the fixed rig; the
  three that failed stand as the record of the fault and count in no table. **The same taint, found again on the trial of the
  fixed rig** (run 39479725812, 19:00 UTC; the runs 39479741832, 39479757911 and 39479773633 started with it): metrics-server
  rolled out, and then the load generator, pinned to the control plane with the same single toleration, stayed Pending in both
  arms ("1 node(s) had taint {node-role.kubernetes.io/master: }, that the pod didn't tolerate"). Every pod the rig pins to the
  control plane now tolerates both taints: the load generators (`deploy/kind/loadgen*.yaml`), the noisy neighbour, the
  orchestrators' own deployments the batch rig moves onto the control plane (`scripts/kind_batch_queue.sh`), and the chart
  values of Crane, KAI, Koordinator, KubeRay, CruiseKube and the bin-packing profile; on 1.25 and 1.35, where the second taint
  does not exist, a toleration for it changes nothing. Gödel's trial runs first on this rig and its A, B and C start only once
  the trial has run both arms whole; the second set of three stands as the record of the second fault and counts in no table.
- **The test machine, twice more** (no rig changed for either): KubeRay A (run 39438462925, repetition 2) lost its runner
  three hours in, no log kept, after the memory bound of amendment 9 was in place; the other nine repetitions landed whole and
  are read, and the table says A carries nine. Karmada A (run 39438525862, repetition 3) never started: GitHub's checkout of
  the repository failed after seven minutes, before any cluster was made; the other nine landed whole and are read, and the
  table says A carries nine.
- **Two LOSS rows, reported as they stand, their mechanism named, nothing re-aimed after the fact.** (1) Crane, Omni-Compass
  on top of it against it as shipped (`results/live/V12_CRANE_4W_TOP.md`): the total pod start wait rose 54% to 104% in all
  three runs, LOSS, while the pods started rose 50% to 67% (power given), the replicas 14% to 18% (power given) and the wait per
  pod read STEADY (+0.9% to +21%, intervals across zero in two runs): the total is the per-pod wait, unchanged, summed over the
  pods Omni-Compass chose to start; the same gauge read the same way in the KEDA runs of 18 October (`docs/POD_START_WAIT.md`).
  Whether a sum of a resource (pods started) and a wait (the wait per pod) is a wait or a resource is for the metric-aims audit
  to decide in writing before any run is read by it; this table is read by the key as it stands, and the row stays LOSS. (2)
  KubeRay's rig, Omni-Compass on the organism alone against the organism alone (`results/live/V12_KUBERAY_4W_BARE.md`): the
  queue finished 0.6% to 0.8% later and the 99th percentile rose 4% to 13% in all three runs, LOSS, while the machines in
  service fell 14% to 19%, the machines left after the queue 25% to 33% and the mean response 7% to 10% (GAIN), the 95th
  percentile, the time over the line, the failures and the jobs unfinished STEADY. The governor gave machines back during the
  queue on its trial's own gauges, and the queue's last jobs and the tail paid for it. On the engine that stands no muscle may
  fall below native, so this is the engine's to fix, not the table's: the give-back trial on a batch queue must count the
  queue's finish and the tail among the gauges it judges before a machine is parked, in the next version, through the model gate
  first (`docs/CHANGE_CONTROL.md`). The rows stand until that version's three runs replace them.

## Amendment 11: KubeRay's two LOSS rows root-caused (written from the runs' own files, 20 October 2026, before any run on the engine that fixes them)

Amendment 10 put KubeRay's two LOSS rows (the organism alone: the queue 0.6% to 0.8% later, the 99th percentile 4% to 13%
higher) down to the give-back. The 29 paired repetitions' own files, read job by job and pod by pod, say otherwise. The
mechanism is named here as they show it (`docs/OMNI_V13.md`, section 1):

- The cost sits in the 16 repetitions whose native queue ran past 760 s, where a slower runner's kind cores were saturated
  through the queue (the host's busy share 0.78, 95% of readings at or over 0.75). There each batch pod hashed its work 7.6%
  slower with Omni-Compass on top (63.1 s against 59.2 s), and the queue finished 1.1% later. In the other 13 the same pods
  read +0.3%.
- No machine was parked during a saturated queue: six workers were in service through it in both arms. The machines given
  back were given back after the queue, so the give-back is not the mechanism.
- In 15 of those 16 the conveyance raised the web pods' limits to 3,700m at 33 s (one at 65 s) and kept them for 92% to 96% of
  the queue. The raise came on the governor's reading of the host's busy share over the 15 s since its previous reading, which
  caught the dip as the stream's first pods started. omni-v7's guard holds a new raise at the host's top, never one already
  given.
- The web gained nothing while the queue ran: its median was 266 ms against 253 ms natively, its 99th percentile 3,429 ms
  against 3,226 ms, and it served the same requests. After the queue, with the host free, its median fell from 114 ms to 69 ms.

The fault is the engine's: on a host with no idle processor a limit above the operator's conveys nothing and costs the muscle
beside it. omni-v13 hands such limits back while another workload on the shared host has room of its own, and counts every
other pod by its limit (`docs/OMNI_V13.md`). The rows of amendment 10 stand as omni-v12's record. The four ways run again on
omni-v13, A, B and C, and its tables replace none of omni-v12's.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
