# CruiseKube: Omni-Compass on top of a service right-sized live by CruiseKube (preregistration)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on 13 October 2026, before any counted run of this test. It is register row 81, the second of the nine pieces the
founder listed on 12 October (`docs/THE_SEAT.md`) to be built as a benchmark with Omni-Compass on top. Every earlier
Kubernetes set stays as it is; this is a new set beside them.

## The question

When the service's CPU and memory are right-sized live by CruiseKube (TrueFoundry), on the running pods and at admission,
does Omni-Compass on top still make the service faster, use fewer machines or less energy, without a LOSS anywhere?

## What CruiseKube is, and so what native is

CruiseKube is a Kubernetes controller that right-sizes each workload's CPU and memory itself from what Prometheus shows of
its use: in place on the running pods (Kubernetes' in-place resize, 1.33 or later) and at admission through its own
webhook. Per workload the operator turns it on or off (Cruise mode) and sets an eviction rank and disruption windows; how
it right-sizes is its own. As shipped it acts only on workloads older than an hour, builds its statistics every 15
minutes and applies them every 5 minutes, and it sets a running pod's CPU limit to its machine's allocatable CPU. By its
own design it leaves alone any workload whose horizontal autoscaler scales on CPU or memory, so that the two controllers
do not fight over the same signal.

Every Kubernetes set here scales the service on CPU, which CruiseKube would leave alone. This set therefore runs it beside
the autoscaler of row 68's KEDA set with its profile http (`docs/ADDONS_PREREGISTRATION.md`): KEDA 2.21.0 and its HTTP
add-on 0.16.0 (pinned as in that set, `scripts/kind_addons.sh`) scale the service on the requests in flight, the load
and the probe enter through the add-on's interceptor, and
CruiseKube right-sizes the pods underneath, the combination its documentation allows. Native is therefore KEDA's HTTP
add-on and CruiseKube in Cruise mode on the service, both as shipped and as used, running through the measured window.

CruiseKube is source-available under the Business Source License 1.1, which grants non-production use; a benchmark is
non-production use. Its usage reports to its maker are switched off in every run.

## The arms (two, as always)

- **native**: the kind cluster with KEDA's HTTP add-on and CruiseKube in Cruise mode on the service; Omni-Compass is not
  started.
- **omni**: the same cluster, the same KEDA, the same CruiseKube, with Omni-Compass on top (`ARM=compass`): its live
  muscles as in row 68's http set (the autoscaler's replica range, carried to KEDA's ScaledObject by the plug,
  `scripts/kubectl_keda.py`; the node pool; the rollout guard), the engine that stands at the run's commit
  (`python3 tools/omni_version.py`, recorded in every run). The power cap is left out of this set: it writes the
  service's CPU limit, which CruiseKube resizes in place itself, and one knob has one writer. Omni-Compass writes nothing
  to CruiseKube, its settings or its database: its identity cannot (`kubectl auth can-i` receipts in every run's
  `rbac_omni.txt`), and every reset check reads back the operator's settings after the run (the autoscaler's range on the
  ScaledObject and the HPA, the workers in service, the operator's CPU limit on the Deployment, no Omni-Compass record
  left). The pods' own CPU limits are CruiseKube's; they are recorded at the start and the end of the window
  (`cruisekube_resources_start.json`, `cruisekube_resources_end.json`), never judged as a reset.

## CruiseKube and its inputs, frozen

- CruiseKube **0.3.4** (chart and application), from its maker's own chart; the chart archive's SHA-256 is recorded by
  the shakedown run and pinned in the workflow (`CK_CHART_SHA256`) before the first counted run; a counted run whose chart
  does not match fails. Every image the add-ons run is recorded with its digest as the cluster resolved it
  (`cruisekube_pins.txt`).
- Its settings as shipped, with only what a benchmark run needs changed (`deploy/kind/cruisekube-values.yaml`): the
  Prometheus it reads is ours; its usage reports are off; its dashboard and its login are left out (its API answers inside
  the cluster only, read by the harness through a port-forward); the Prometheus Operator's ServiceMonitors are left out (no
  operator runs here); its PostgreSQL is its own chart's, without a volume. Its hour before it acts on a new workload is
  kept.
- What CruiseKube reads, pinned: kube-state-metrics **v2.20.0** (the project's standard manifests, five files SHA-256
  checked), node-exporter **v1.12.0**, Prometheus **v3.10.0** with the scrape jobs and labels CruiseKube's queries name
  (`deploy/kind/cruisekube-metrics.yaml`).
- Everything CruiseKube, its database, its Prometheus and kube-state-metrics run is on the control plane beside
  metrics-server, CoreDNS and KEDA, so the six measured workers carry only the service, as in every set; the one exception
  is node-exporter, one small pod per machine (CruiseKube reads every machine's own counters), the same in every arm. A
  run with any other add-on pod on a worker fails (`scripts/kind_addons_cruisekube.sh`).

## The learning, the same in every arm

1. With the load generator running, before the arms are told apart (Omni-Compass not started), the harness waits until
   CruiseKube lists the service (its statistics task, every 15 minutes) and turns Cruise mode on for it through
   CruiseKube's own API (the operator's switch; nothing else is changed).
2. The load steps through the benchmark's own steps (1 2 3 1 2 1), five minutes a step, for 4,500 s (75 minutes, longer
   than CruiseKube's hour), and then until CruiseKube's own audit shows a change applied to the service (a recommendation
   applied in place, or a pod mutated at admission), for at most 30 minutes more. A run in which CruiseKube applied no
   change is invalid: a native that never acted would be plain Kubernetes.
3. Each arm runs on its own fresh cluster and learns on its own; CruiseKube keeps right-sizing live through the warm-up
   and the window in both arms, as it does in service. Unlike Goldilocks (row 80), there is no single recommendation to
   hand to both arms: CruiseKube is a live controller, and how it answers Omni-Compass's moves is part of what is
   measured.
4. What CruiseKube did is in every run's record: `addons.txt` (versions, the chart's SHA-256, when Cruise mode came on,
   how long the learning took), its audit events at the start and the end of the window, its view of the workload, the
   pods' resources at both ends and its controller's and webhook's last words.

## The workload and the measure

As row 68's http set: the six-worker kind cluster (Kubernetes v1.35.0, kind v0.31.0), a fresh cluster per arm, both arms
back to back on the same GitHub runner in an order rotated by repetition; the closed-loop load generator stepping 1 2 3 1
2 1; 120 s warm-up, 900 s measured; ten paired repetitions per run. Every gauge of `tools/live_reps.py` is reported,
losses included, with the paired mean difference and its 95% interval. A run whose checks fail is invalid, kept in the raw
files and not counted: a pinned file that does not match, CruiseKube not listing the service or applying no change, an
add-on pod on a worker, a move of Omni-Compass that did not reach KEDA whole, a reset that does not hand back the
operator's settings.

The shakedown (`shakedown=yes`) is one repetition that proves the wiring and records the chart's SHA-256 for the pin, with
CruiseKube's hour shortened to none, 1,500 s of learning and a 360 s window. It is never counted.

## How it is read

- A gauge whose 95% interval of the paired difference is clear of zero is a difference in this run; one whose interval
  includes zero is no difference beyond the noise, and that is the result.
- Three separate runs on the same commit, A, B and C (`tools/confirm_abc.py`): GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given),
  no difference beyond the noise, or the runs disagree. The founder hears what the three say before the table goes up.
- Response times and failed requests are class L (measured on live software). Machines in service are counted live; the
  watts are the declared model (class S), as in every kind set.

## Known limits, said before the result

- CruiseKube learns over 75 minutes of this load, not the days an operator would give it; its hour is kept as shipped.
- On kind there is no node autoscaler for native (no cloud to add or remove machines), so native keeps all six workers in
  service; Omni-Compass's machine and energy gauges are measured against that.
- CruiseKube may taint a machine it judges overloaded, in both arms alike; Omni-Compass's node pool counts only its own
  mark, and neither removes the other's.
- The CPU limit is not a knob in this set: CruiseKube owns it on the running pods, so the power cap, which writes it in
  other sets, stays out.

## Amendment 1: the trial run read, the chart pinned, and a decided window with no write counted (13 October, before the counted runs)

- **The trial ran end to end** (run 38412997261, never counted; its files in `results/live/raw/run-38412997261/`).
  CruiseKube installed, learned and applied its own change to the service before the window in both arms. The chart's
  archive SHA-256 was recorded in both arms, `a3c7fa8914d4c29f6c04999fea1fbbe83a6045270ac739ee02a357d14c034ecf`; it is
  now pinned (`CK_CHART_SHA256` in `.github/workflows/kind-cruisekube.yml`), and a counted run whose chart differs stops.
  The images CruiseKube's chart starts are recorded by digest in `cruisekube_pins.txt` (its PostgreSQL comes from the
  chart's own `bitnami/postgresql:latest`; its digest is recorded in every run).
- **What Omni-Compass did in the trial's window.** Its governor decided six times in the 360 s and made no write. The
  service stayed well inside its line (the 95th percentile 133 to 199 ms against the 500 ms line); the authority over
  the pods came once the system had calmed, from the third decision; and on top of CruiseKube, which owns the CPU limit,
  and KEDA's HTTP add-on, which already scales at one request in flight per pod, nothing needed moving. The old rule of
  the rig marked the window invalid (a window with no write proves nothing about the reset).
- **The rule now** (`scripts/kind_bench.sh`, every set): staying native is the governor's own decision, made at every
  step (the founder's order of 10 October). A window in which the governor recorded its decisions (at least one a
  minute, each with its reasons in the audit) and made no write is valid and counts as it ran; the reset still checks
  that every setting is the operator's; the table says in how many repetitions Omni-Compass stayed native
  (`tools/live_reps.py`). A governor that recorded no decisions was not running, and that window is invalid.
- **Nothing else changes**: the load (`1 2 3 1 2 1`, closed loop), 4,500 s of learning, 120 s warm-up, 900 s measured,
  ten pairs a run, three runs. If Omni-Compass stays native throughout, the reading is no difference beyond the noise
  with the count of windows it stayed native: on top of CruiseKube and KEDA at this load the service needed nothing
  more, and Omni-Compass did no harm.

## Amendment 2: a window with no machine in service is refused in either arm (18 October, omni-v10 reruns)

In run 39120444653, repetition 8, every worker of the kind cluster left service for two minutes while the service answered
every probe. The omni arm's governor wrote nothing, and two of its fifteen decisions failed on the empty reading. The rig
refused the window, but its words said the governor was not running. A window in which the capture shows no machine in
service has a wrong machine count, so it is now refused in either arm. A failed decision is named by its error. The capture
keeps each node's taints and conditions at that moment (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendment of 18 October).
The repetition runs again in place. The load, the learning, the window, the pairs and the gauges are unchanged.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
