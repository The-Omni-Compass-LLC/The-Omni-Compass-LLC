# The group of clusters: Omni-Compass on top of the clusters a group orchestrator governs, four ways (preregistration)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on 20 October 2026, before any run of this test. It holds the governors on the founder's list of 19 October, night,
whose organism is not one cluster but several: Karmada (register row 95) first; Open Cluster Management (row 96) and Armada
(row 94) join it, each by an amendment written before its first run. Each runs the four ways of the founder's order of 20
October. This is the level "a group of clusters" of `docs/LEVELS.md`, measured live for the first time.

## The question

When a group orchestrator places a stream of batch jobs across a group of clusters, what does it do to the group on its own,
what does Omni-Compass do to the group without it, and does Omni-Compass on top of each member, under the orchestrator, make
the group's work faster or use fewer machines or less energy, with no LOSS anywhere?

## The organism: a group of two clusters

Two of the batch rig's clusters (each `deploy/kind/cluster-full.yaml`: one control plane and six workers, Kubernetes 1.35 on
kind v0.31.0), `omni-m1` and `omni-m2`, on one GitHub runner. Each member runs the batch rig's bench unchanged
(`scripts/kind_bench.sh`, `BATCH_QUEUE=group`): its service and probe, its metrics-server, its own default scheduler, its
capture, and, in the Omni-Compass arms, its own governor on the runner's last core (`docs/BATCH_QUEUE_PREREGISTRATION.md`,
amendment 5). The members open their measured windows together (`GROUP_BARRIER`), and the stream starts once both are open.

## The stream, the same work

The batch rig's stream unchanged: 24 jobs of 10 pods, 5 at a time, one job every 30 s, each pod hashing 3,000 MB
(`deploy/kind/batch-stream-job.yaml`), sent to the group (`scripts/kind_group_orch.sh`): to the orchestrator, which places
each job, or, on the group alone, by the harness to the members in turn (job 1 to `omni-m1`, job 2 to `omni-m2`, and so on),
the simplest placement a group without an orchestrator has.

## The arms: the four ways, all four in every repetition

- **nativebare**, the group alone: no orchestrator; the jobs go to the members in turn; Omni-Compass is not started.
- **native**, the orchestrator as its project ships it, on a one-node cluster of its own beside the members
  (`deploy/kind/cluster-host.yaml`; OCM's agents also in the members, amendment 1), every job sent to it; Omni-Compass is
  not started.
- **compassbare**, Omni-Compass on top of each member of the group alone (one governor per member, each wired to its own
  cluster only, as on one cluster).
- **compass**, Omni-Compass on top of each member, the orchestrator on top of the group.

Each comparison is the first arm against the second, paired within the repetition, read by the one key for the first arm:
compass against native (Omni-Compass on top of the orchestrated group), native against nativebare (what the orchestrator does
on its own), compassbare against nativebare (what Omni-Compass does without it), compassbare against native, and compass
against nativebare. Omni-Compass never writes the orchestrator's objects and never sends, holds or places a job; in each member
it works the same levers as on one cluster, on top of what the orchestrator sends there.

## Karmada, frozen

- **Karmada v1.19.0** (`karmada-io/karmada`, the CNCF, Apache-2.0), installed as its own CLI installs it (`karmadactl init` on
  the orchestrator's cluster; its images `docker.io/karmada/*:v1.19.0` and the Kubernetes images it names, each recorded with
  its digest in `orch.txt`), from its release: `karmadactl-linux-amd64.tgz` (SHA-256
  `cf690eacc25ed13b6a27366c1b0b33e0e6edd2833e379922d420a5355550ef3d`) and `crds.tar.gz` (SHA-256
  `e8d225a910924432f90d0e0397890d7d94b5a444b32e4586343570feeeafe100`); a file that does not match its pin fails the arm.
- Both members joined in push mode (`karmadactl join`), by the address its pods reach them at; the arm waits until Karmada
  reports both Ready.
- **The operator's one setting**, a propagation policy for the stream (`deploy/kind/karmada-propagation.yaml`): every job may go
  to either member, divided among them by Karmada's Aggregated preference, which its documentation gives for work that should
  run on as few clusters as its available resources allow. Which member each job goes to, and how, is Karmada's.
- Its own record of every job (`orch_jobs.json`), where it placed each (`orch_end.json`) and its scheduler's and controller
  manager's last words are kept in every arm. Its certificates and the members' credentials stay outside the run's files.

## The measure, merged from the members

Every member's record is merged into the arm's own files (`tools/merge_group.py`), read by `tools/live_reps.py` as any arm:
the window opens when the stream starts and closes with the first member's window; every job once, submitted when it was sent
(to Karmada, or to its member) and done when every member's part of it is done (a part not done leaves its job unfinished at
the window's end); the members' machines in service, processors and modelled watts summed at each moment; every member's
probe, governor record and pod record. The gauges are the batch rig's: job wait (mean, 95th percentile), turnaround, jobs
unfinished, machines in service, energy, and every other gauge of the table, losses included, each with its paired 95%
interval. Ten repetitions a run, three runs (A, B and C) started together (`kind-group.yml`), each comparison's three-run table
by `tools/confirm_abc.py --pair`.

## Tried first

One repetition (`kind-group.yml`, label `trial`), never counted in any table, to see the group stand: both members' windows
open together, Karmada places the jobs, the records merge. A trial that shows a fault in the rig is fixed in the rig, and the
fix is written here as an amendment before the counted runs.

## Known limits, said before the result

- Two members of six workers each, fifteen kind nodes on one runner's four processors (three for the clusters, one for the
  governors): the group shares one machine, as every kind cluster here does; the work is the same in every arm.
- On the group alone the harness places the jobs in turn, without regard to how busy each member is; that is the group
  without an orchestrator, not a scheduler of the harness's own.
- Karmada's own cluster runs on the cluster cores in its two arms only; what it costs the group is part of "the orchestrator on
  its own".

## What it is not

A contest between Omni-Compass and the orchestrator for the same job: Omni-Compass places no job and writes nothing of the
orchestrator's; on the group alone it sits on top of each member's own scheduler, under the orchestrator on top of the same.

## Amendment 1: Open Cluster Management, frozen (written before its first run, 20 October 2026)

The founder's list names Open Cluster Management (`open-cluster-management-io/ocm`, the CNCF, Apache-2.0), a hub that
registers clusters, decides placements and distributes work to them. Register row 96. It runs on this rig as its second
orchestrator (`kind-group.yml`, `orch=ocm`), the four ways above, with the same stream, members, measure and tables.

- **OCM as its project ships it**: its hub (the cluster manager) installed by its own CLI on the orchestrator's cluster
  (`clusteradm init` on `omni-host`, the components of its default bundle 1.4.0; `clusteradm` v1.4.0 from its release,
  `clusteradm_linux_amd64.tar.gz`, SHA-256 `aa94241caf353a515a0778e0ce608b4c68ced9b3e7f6fb5fe23f48393926153b`, a file that
  does not match its pin fails the arm); each member registered by `clusteradm join` (its klusterlet, the registration and
  work agents, in the member's own namespaces `open-cluster-management` and `open-cluster-management-agent`, on the workers
  as OCM places them) by the address its agents reach the hub at, and accepted on the hub (`clusteradm accept`); the arm
  waits until the hub reports both members Available. The bootstrap token stays outside the run's files. Every image, with
  the digest it resolved to, is recorded in `orch.txt` (the hub's, and one member's agents').
- **The operator's one setting**: the default cluster set (every joined cluster is in it) bound to the `default` namespace,
  and for every job of the stream a Placement of its own in that namespace, asking for one cluster of the set with OCM's
  default prioritizers (Steady, which keeps a decision once made, and Balance, which spreads the decisions among the
  clusters), the way OCM's documentation distributes workloads: a Placement each, the hub deciding. Once OCM has decided
  (`PlacementDecision`), the harness writes the job as a `ManifestWork` in the chosen member's namespace on the hub, and
  OCM's work agent applies it in that member. Which member each job goes to is OCM's; the harness waits up to 120 s for a
  decision and tries a job's placement twice.
- **What runs in the members is part of "the orchestrator on its own"**: OCM's klusterlet runs in each member in both of
  its arms (`native`, `compass`), on the workers, as Karmada in push mode runs nothing there; its cost to the group is
  OCM's, and "OCM as shipped against the group alone" shows it.
- **Its records**: every `ManifestWork` as sent (`orch_jobs.json`: the job's name and the moment it was sent to the hub),
  every `PlacementDecision` (`orch_end.json`: each job and the member OCM chose), and the hub's placement, registration and
  work controllers' last words; a job is done when its Job in the member is done, as on the group alone.
- **Known limit, said before the result**: OCM is a placement engine, not a job scheduler. Its decision reads what it
  knows of each cluster (its allocatable resources, and the balance of decisions already made), never the member's live
  load; on two identical members, Balance alternates the jobs between them much as the group alone does in turn. Where
  that is what OCM does, the tables will say so, and "Omni-Compass on top of OCM against OCM as shipped" is read on the
  same placements.
- **Tried first**: one repetition (`kind-group.yml`, `orch=ocm`, label `trial`), never counted; a fault in the rig is
  fixed in the rig and written here before the counted runs.

## Amendment 2: Armada, frozen (written before its first run, 20 October 2026)

The founder's list names Armada (`armadaproject/armada`, G-Research, the CNCF, Apache-2.0), a multi-cluster batch scheduler:
jobs are submitted to its queues, its scheduler assigns each to a cluster and a node, and an executor in each cluster creates
the pods. Register row 94. It runs on this rig as its third orchestrator (`kind-group.yml`, `orch=armada`), the four ways
above, with the same stream, members, measure and tables.

- **Armada as its project ships it**: release v0.22.14 (its images tagged `0.22.14`, each pinned here by its digest;
  `armadactl_0.22.14_linux_amd64.tar.gz`, SHA-256 `38fb81fe5b372400baa9c65096013fd44de0d1ab9e7178eb51f4c569bc40280e`), run
  as its own local stack runs it (`_local/compose` at v0.22.14): Redis 7.4, PostgreSQL 17 and a Pulsar 4.1.0 standalone
  broker, the scheduler and lookout databases laid out by its own migrations, then its scheduler, scheduler ingester, server
  and event ingester from its bundle image, every one a container on the runner's own network (so its local configuration,
  which names every service at localhost, stands unchanged) and on the cluster cores; its components' settings are its local
  stack's (`deploy/kind/armada/*.yaml`: anonymous access, the executor list read every second as its containerized stack
  sets it, tracing off because there is no collector here). Armada's control plane needs no cluster of its own; `omni-host`
  is not created in its arms.
- **One executor per member**, run as its local stack runs it, on the runner, reaching its member by the member's own
  kubeconfig (`clusterId omni-m1`, `omni-m2`; pool `default`), so each member is one of Armada's worker clusters; Armada's
  two priority classes (`armada-default`, `armada-preemptible`, as its local kind setup applies them) are applied in every
  member before its executor starts. The kubeconfigs stay outside the run's files.
- **The operator's one setting**: one queue, `omni`, created with `armadactl create queue` and nothing else set (its priority
  factor the default, 1).
- **The stream, the same work, as Armada takes work**: Armada's unit is a pod, not a Kubernetes Job, so each batch of the
  stream (10 pods hashing 3,000 MB) is submitted as one job set (`jobSetId` the batch's name) of 10 jobs, each the batch's pod
  with the stream's labels (`app`, `job-name`, `omni-stream`), by `armadactl submit`, one batch every 30 s as on every other
  system. Two things differ, both Armada's own and said here: Armada requires a pod's requests to equal its limits, so its
  pods ask for the stream pod's limit, one processor (the Kubernetes Job's pods ask for half and may use one); and a job set
  has no "5 at a time", so how many of a batch's pods run at once is Armada's scheduler's decision within the members'
  capacity, as on every system the pods' admission is the orchestrator's. A batch is done when 10 of its pods have
  succeeded; `job wait` is the batch's first pod running after it was submitted, as everywhere.
- **Its records**: every batch as it was sent (`orch_jobs.json`: the job set's name and the moment `armadactl submit`
  returned, done when its tenth pod ended, read from the members' pods), where its pods ran (`orch_end.json`), its scheduler's
  and server's last words, and every image by the digest it was pulled by (`orch.txt`); the merger reads a batch's end from
  Armada's record where a member has no Job of that name (`tools/merge_group.py`).
- **What runs on the runner is part of "the orchestrator on its own"**: Armada's control plane and its two executors take
  processor time on the cluster cores in its two arms (`native`, `compass`); its cost to the group is Armada's, and "Armada as
  shipped against the group alone" shows it. Pulsar's heap is bounded (1 GiB) so the stack fits beside fifteen kind nodes;
  a stack that does not come up fails the arm (marked invalid), never the measure.
- **Known limit, said before the result**: Armada is built for many clusters and long queues; here it has two members and 24
  job sets. Its fair share and preemption never engage (one queue, one priority); what is measured is its placement and the
  path a pod takes through it (submit, Pulsar, scheduler, lease, executor, pod), against the group alone and with
  Omni-Compass on top of each member.
- **Tried first**: one repetition (`kind-group.yml`, `orch=armada`, label `trial`), never counted; a fault in the rig is fixed
  in the rig and written here before the counted runs.

## Amendment 3: what the counted runs of OCM and Armada found (written after those runs, 21 October 2026)

- **Their tables, on omni-v12**: OCM's A, B and C (runs 39479807336, 39479824367, 39479840381) and Armada's (39482335827,
  39482351075, 39482365814) ran on omni-v12, the engine that stood when they started, ten repetitions each, every arm on the
  pre-pulled rig with the governor on its own core; their five tables each are `results/live/V12_OCM_4W_*.md` and
  `V12_ARMADA_4W_*.md`, every row shown. They stand as omni-v12's record; both systems run again on the engine that stands
  (`scripts/reruns.txt`) and their tables on it replace these on the page when they land.
- **The test machine, once more**: Armada A's repetition 3 lost its runner 81 minutes in, no log kept; the other nine landed
  whole and are read, and the table says A carries nine. No rig changed for it.
- **Two LOSS rows on Omni-Compass's side, reported as they stand**: on top of OCM against OCM as shipped, the alert minutes
  rose in all three runs (+5.7%, +6.1%, +45.5%); on the group alone, Omni-Compass against the group alone, the job turnaround
  rose in all three (+5.1%, +8.9%, +9.1%). Both runs put three kind clusters on one runner, a shared host at its top while
  the batch queue runs, and both show the mechanism omni-v13 fixed on KubeRay's rig the same day (`docs/OMNI_V13.md`): the
  serving pods' limits raised beside the batch pods' room and kept through a saturated queue, so the batch pods ran slower
  and the host's processor, busier by 4% to 16% in the omni arms, slowed the service it was meant to help. The cause is in
  the engine, not in the rig; the fix is omni-v13's hand-back, and the raise on the reading that opens the queue is the next
  version's (`docs/CHANGE_CONTROL.md`). Neither row is cut; each is read again on the engine that stands.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
