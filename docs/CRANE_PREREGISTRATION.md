# Crane: Omni-Compass on top of a service scaled by Crane's Effective HPA, four ways (preregistration)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on 20 October 2026, before any run of this test. It is register row 90, one of the governors and orchestrators the
founder listed on 19 October, night, each to be benchmarked on the organism natively and with Omni-Compass on top, and run
the four ways of his order of 20 October ("show what they do natively on top of the system organism ... show what
OmniCompass does on the organism without the orchestrator ... put OmniCompass on top of the orchestrator that's on top of the
whole organism"). Every earlier Kubernetes set stays as it is; this is a new set beside them.

## The question

When Crane owns the service's autoscaler through its Effective HPA, what does Crane do to the organism on its own, what does
Omni-Compass do to the organism without Crane, and does Omni-Compass on top of Crane make the service faster, use fewer
machines or less energy, with no LOSS anywhere?

## What Crane is, and so what native is

Crane (`gocrane/crane`, Tencent, Apache-2.0; "Cloud Resource Analytics and Economics") is a resource governor for
Kubernetes: recommendations for requests and replicas, quality-of-service ensurance through an agent on every node, and the
Effective HPA (EHPA), the piece that governs a service's replicas. The operator writes an EHPA in place of an HPA. In auto
mode Crane builds the service's HPA from it (named `ehpa-<name>`), owns it (a controller reference) and writes it back
whenever it differs from the one it builds. With a forecast configured, Crane's DSP algorithm reads the scaled metric's
history from Prometheus and, once its forecast is ready, Crane adds the forecast to the HPA as an external metric, so the
HPA scales ahead of a load it has seen before (its code: `pkg/controller/ehpa/hpa.go`, `GetHPAMetrics`).

Native is therefore Crane as its installation guide installs it and as its own documentation uses it on this very service:

- **Crane 0.11.0**, its last release (25 July 2023), from its chart (`gocrane/helm-charts`, release `crane-0.11.0`); its
  controller (craned), its metric adapter, its dashboard and its node agent (crane-agent, on every node), each as the chart
  ships it.
- **The Prometheus it reads**, the prometheus-community chart with Crane's own override values (its recording rules), the
  alert manager, the push gateway and the server's volume left out, exactly as Crane's installation guide installs it.
- **The service's autoscaler handed to Crane**: the service's HPA deleted and an EHPA applied in its place
  (`deploy/kind/crane-ehpa.yaml`): auto mode, the operator's own settings of the HPA it replaces (one to ten replicas, the
  processor held at 50%; deploy/kind/demo.yaml), and the forecast as Crane's documentation writes it for this service (the DSP
  algorithm, a 60 s sample, seven days of history, an hour ahead).

## Why this test runs Kubernetes 1.25

Crane 0.11.0 builds its HPA as `autoscaling/v2beta2`, an API Kubernetes removed in 1.26: on the Kubernetes 1.35 every other
kind set runs, its EHPA cannot build an HPA at all. This test alone therefore runs Kubernetes **1.25.16**, the last release
that serves `autoscaling/v2beta2`, in all four arms: kind v0.24.0 with its own node image for 1.25.16
(`kindest/node:v1.25.16@sha256:6110314339b3b44d10da7d27881849a87e092124afab5956f2e10ecdb463b025`), kubectl v1.25.16 and
metrics-server v0.6.4, the line metrics-server's own compatibility table gives for 1.25 (its manifest's SHA-256
`42e764a5ce56a88a9fd0e1995db34f0e37ec8845313454881c88500d507623af`).

Kubernetes 1.25 cannot resize a running pod in place: the `pods/resize` subresource that Omni-Compass's power cap and
processor conveyance write is not served. Those two levers do not exist on this cluster. The bench reads the cluster's own
API for it before every arm and leaves both off in every arm (`scripts/kind_bench.sh`; every arm's `preflight.txt` carries
`in_place_resize=not served by this cluster`). This test's tables are read among its own four arms, never beside the 1.35
sets'.

## The arms: the four ways, all four in every repetition

- **nativebare**, the organism alone: the same 1.25 cluster with the service's HPA as Kubernetes ships it, no Crane and no
  Prometheus; Omni-Compass is not started.
- **native**, Crane on the organism, as above; Omni-Compass is not started.
- **compassbare**, Omni-Compass on top of the organism alone (the HPA as Kubernetes ships it).
- **compass**, Omni-Compass on top of Crane on top of the organism.

In both Omni-Compass arms its live levers are the autoscaler's processor target and replica range, the node pool and the
rollout guard, the engine that stands at the run's commit (`python3 tools/omni_version.py`, recorded in every run). The
governor runs on its own core in every arm (`GOV_CORE=1`, as amendment 5 of `docs/BATCH_QUEUE_PREREGISTRATION.md` gives
it on the batch rig): the kind nodes on every core of the runner but the last, the governor alone on the last; in a native
arm that core carries nothing.

**The plug.** Crane rebuilds the HPA from its EHPA and undoes any write to the HPA itself, and one knob has one writer. So
in the compass arm Omni-Compass's autoscaler moves reach Crane through a plug that stands where kubectl stands
(`scripts/kubectl_crane.py`, the pattern of the KEDA plug, `scripts/kubectl_keda.py`): each move to the HPA's processor
target or replica range is carried to the same setting of the EHPA, the one place Crane reads it from, and the plug waits
until Crane's rebuilt HPA shows it; a move it cannot carry exactly is refused with the reason, never approximated, and every
carried move is one line of `plug_crane.jsonl`. Omni-Compass's record of the operator's settings (its `omnicompass.io/`
annotations, read back at the reset) is kept on the EHPA and on the HPA, and Crane copies it onto the HPA it builds through
its own operator setting `--ehpa-propagation-annotation-prefixes=omnicompass.io/` (`deploy/kind/crane-values.yaml`). That is
the one setting of Crane's changed from its chart's, and in a native arm, where no such annotation exists, it changes
nothing. Omni-Compass's identity may get and patch that one EHPA and nothing else of Crane's (`deploy/kind/rbac-omni-crane.yaml`;
the `kubectl auth can-i` receipts in every run's `rbac_omni.txt`), and every reset check reads back the operator's settings
on the EHPA and on the HPA Crane built, with no Omni-Compass record left on either.

Each comparison is the first arm against the second, paired within the repetition, read by the one key for the first arm:

| Comparison | What it shows |
|---|---|
| compass against native | Omni-Compass on top of Crane |
| native against nativebare | what Crane does on its own, natively, on the organism |
| compassbare against nativebare | what Omni-Compass does on the organism without Crane |
| compassbare against native | Omni-Compass on the organism without Crane, against Crane |
| compass against nativebare | the two together, against the organism alone |

## Crane and its inputs, frozen

- The Crane chart archive, SHA-256 `1f3f163abc17c373e27380be42cf39d5041090ccad3c7af1597390550a8f7fe9`; its images
  `docker.io/gocrane/{craned,metric-adapter,dashboard,crane-agent}:v0.11.0` as the chart names them, each recorded with the
  digest the cluster resolved (`addons.txt`).
- The prometheus-community chart **25.8.0** (Prometheus v2.48.0), SHA-256
  `9f4fa3cc4e0f9e18b38fd8e754ad9bca36e021e8508b1169d5c6ad849ea37756`, and Crane's override values, SHA-256
  `3fffcad0f166f4fae6f6d1444b65263f553dba4e7a169c692c69f59cf7f39452` (`deploy/kind/crane-prometheus-values.yaml` adds only the
  guide's three settings and the placement below).
- A file that does not match its pin fails the arm before its cluster is used (`scripts/kind_addons_crane.sh`).
- **Placement**: craned, the metric adapter, the dashboard, the Prometheus server and kube-state-metrics on the control plane
  beside the cluster's other controllers, by each chart's own placement settings; Crane's node agent and Prometheus's node
  exporter on every node, as shipped, in the arms that carry Crane. A run with any other Crane pod on a measured worker fails.
- **Crane's checks before the window**: the HPA `ehpa-php-apache` exists, is owned by the EHPA, holds the processor at 50%
  and the range 1 to 10; otherwise the arm is invalid.

## The workload and the measure

As the add-on sets (register rows 68, 80 and 81): the service `php-apache`, the closed-loop load generator stepping 1 2 3 1 2
1, 120 s warm-up, 900 s measured; ten repetitions per run, the four arms back to back on one GitHub runner, each on a fresh
six-worker kind cluster, in an order rotated by repetition (`kind-crane.yml`, `scripts/kind_paired.sh`). Every gauge of
`tools/live_reps.py` is reported, losses included, with the paired mean difference and its 95% interval. A run whose checks
fail is invalid, kept in the raw files and not counted: a pinned file that does not match, Crane not building its HPA with the
operator's settings, a Crane pod on a measured worker, a move of Omni-Compass that did not reach Crane's HPA whole, a reset
that does not hand back the operator's settings. Crane's own record of each arm is kept: the EHPA and its forecast at the
window's end (`ehpa_end.json`, `crane_predictions_end.json`) and craned's last words (`craned.log`).

## How it is read

- A gauge whose 95% interval of the paired difference is clear of zero is a difference in this run; one whose interval
  includes zero is no difference beyond the noise, and that is the result.
- Three separate runs, A, B and C, started together on the same commit, each comparison read by `tools/confirm_abc.py`
  (`--pair first|second`): GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose
  reads power given), no difference beyond the noise, or the runs disagree. The founder hears what the three say before the
  tables go up.
- Response times and failed requests are class L (measured on live software). Machines in service are counted live; the
  watts are the declared model (class S), as in every kind set.

## Tried first

One repetition (`kind-crane.yml` with the label `trial` and one repetition), never counted in any table, to see the rig stand
before A, B and C are started: Crane builds its HPA on 1.25, the plug's moves and records survive Crane's rebuilds, and the
resets hand everything back. A trial that shows a fault in the rig is fixed in the rig, and the fix is written here as an
amendment before the counted runs.

## Known limits, said before the result

- **Crane's forecast needs a history this service does not have.** Crane adds its forecast to the HPA only once the forecast
  is ready, and the forecast reads seven days of the service's history; a service on a fresh cluster has a few minutes. Within
  the window Crane's HPA most likely scales on the processor alone, as the organism's own HPA does. This is Crane as shipped
  on a new service, not Crane after a week; whether its forecast was ready in an arm is in that arm's record.
- **What Crane costs is part of native.** Crane's Prometheus, its controllers and its node agents run beside the service; their
  processor time is part of what Crane as shipped costs the organism, and "Crane against the organism alone" shows it.
- On kind there is no node autoscaler for native (no cloud to add or remove machines), so native keeps all six workers in
  service; Omni-Compass's machine and energy gauges are measured against that.
- The older Kubernetes (above): no in-place resize, so no power cap and no conveyance in any arm; the tables are read among the
  four arms of this test only.

## Amendment 1: what the trial found in the rig (written after the trial of 20 October 2026, before the counted runs)

The trial (run 39376930525, one repetition, native and compass) stood up the 1.25 cluster, its metrics-server and the service
in both arms and failed in both at the same place: the Prometheus install waited ten minutes on kube-state-metrics, in
ImagePullBackOff, while the server and every node exporter ran. Crane's override values name a kube-state-metrics image on
Tencent's registry (`ccr.ccs.tencentyun.com/tkeimages/kube-state-metrics:2.2.4`), and the chart composes that name under its
own registry (`registry.k8s.io`), where no such image exists. The rig's values file (`deploy/kind/crane-prometheus-values.yaml`)
now names the chart's own kube-state-metrics image (`registry.k8s.io/kube-state-metrics/kube-state-metrics`, the chart's
v2.10.1), the same in every arm that carries Crane; nothing else of Crane's override changes, and its SHA-256 pin stands. No
reading was taken; the trial counts in no table.

## What it is not

A contest between Omni-Compass and Crane for the same job. Omni-Compass never builds Crane's HPA and never writes Crane's
forecast, its recommendations or its agents; its moves reach the service's autoscaler through Crane's own EHPA, and Crane
builds the HPA from them as it builds it from the operator's. On the organism alone Omni-Compass sits on top of Kubernetes'
own HPA; on Crane it sits on top of Crane.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
