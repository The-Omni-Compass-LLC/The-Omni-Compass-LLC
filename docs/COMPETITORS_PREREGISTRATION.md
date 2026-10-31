# Every product Omni-Compass competes with, run against it on the same machines (preregistration)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on 24 October 2026, before any run of this test. It is the founder's order of the same night: "benchmark all this ...
defensibly or not to see if it's better than OmniCompass or not, and OmniCompass has to sit on it if it's in the world, and
it's something OmniCompass is competing on, and you need to find out whatever other [products] you didn't tell me". Every
earlier set stays as it is. The governors and orchestrators already run four ways (`results/live/GOVERNORS.md`,
`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6); this page adds every other product that decides, or helps a person
decide, what a cluster runs on.

## The question

For each product: does Omni-Compass on the organism alone (on native, the product absent) do more for the organism than the product does, and does Omni-Compass on top of
the product do more than the product alone? Each is answered by the one key (`tools/readings.py`), gauge by gauge, with
every row shown, LOSS rows included.

## The four ways, in every repetition

Each product runs four ways, back to back on one runner, each way on a fresh cluster of the same configuration, the order
rotated by repetition, the governor on its own core (the rig of `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendments 5 and 6):

| Way | What runs | Machine key |
|---|---|---|
| the organism alone | Kubernetes with its own autoscalers (the HPA, the node pool's own autoscaler), nothing added | `nativebare` |
| the product as it ships | the organism with the product installed and set as its own documentation sets it | `native` |
| Omni-Compass on the organism alone | the organism with Omni-Compass on top of its own autoscalers, the product absent | `compassbare` |
| Omni-Compass on top of the product | the product as it ships, with Omni-Compass on top | `compass` |

Four comparisons are read in every run: the product against the organism alone (what the product does); Omni-Compass on the organism alone against the product (which does more on the same native); Omni-Compass on top of the product against the product (what
Omni-Compass adds); and Omni-Compass on top of the product against the organism alone. Omni-Compass never replaces the
product: on top, it writes only its own muscles, and every reset check reads the product's own settings back after the run.

## The gauges and the rule

The gauges of every Kubernetes set (`tools/live_reps.py`): the response time's mean, 95th and 99th percentiles, the time over
the response line, failed requests, alert minutes, pods waiting for a place, the machines in service, machine-hours, energy
by the declared model, the governor's own processor, and the settings commands written with no person touching either arm.
Each comparison is paired within its repetition. Three runs, A, B and C (`tools/confirm_abc.py`); every row reads GAIN,
STEADY, LOSS or power given by the one key (a change of 0.5% or more is a change). Run and scored by The Omni-Compass LLC's own
code. No outside party has reviewed or approved these results.

## The products, and what each decides on its own

Each product is pinned to one release, every file it is installed from SHA-256 checked, its image pinned to its full tag,
its license read from the project's own LICENSE file and written in the run's receipt. Each runs unchanged, as a separate
service under its own license; nothing of its code is copied into Omni-Compass. Where a product's supported Kubernetes
versions do not include the kind node image of every set (v1.35.0), its four ways run on the newest node image it supports,
the same image in all four.

| Product | Who makes it | What it decides on its own | What native is for it |
|---|---|---|---|
| Rancher | SUSE | nothing on its own: a console where a person sees and acts on clusters; the autoscaling under it is Kubernetes' own HPA and Cluster Autoscaler, with rules a person writes | Rancher's server installed on the cluster and the cluster managed by it, its monitoring on |
| Portainer (Community Edition) | Portainer.io | nothing on its own: a console for containers and clusters | Portainer's server and agent installed, the cluster managed by it |
| Vertical Pod Autoscaler, in place | Kubernetes SIG Autoscaling | each pod's processor and memory requests, changed in place while the pod runs (update mode InPlaceOrRecreate) | the recommender, the updater and the admission controller (release 1.7.1, where the in-place mode is always on), the service's VPA in that mode on its memory beside the service's HPA on its processor: the pairing the VPA's documentation allows (it forbids the two on the same resource), the one a cluster that runs both runs. A second configuration, the VPA on the processor with no HPA, is its own row when its rig is built |
| Descheduler | Kubernetes SIGs | which running pods to evict so the scheduler places them again (its LowNodeUtilization policy) | the descheduler as a Deployment on its default interval with that policy |
| KRR | Robusta | nothing live: a recommendation of each workload's requests from its Prometheus history, applied by a person | the recommendation read after a learning window and applied once, as Goldilocks is |
| Knative Serving | the Knative project (CNCF) | the replicas of a request-driven service (its own autoscaler, the KPA, by requests in flight), down to zero | the service as a Knative Service on the KPA's defaults |
| kube-green | the kube-green project | which workloads sleep, on a schedule a person writes | a schedule that puts the service to sleep in the load's quiet steps |

Knative's service is a Knative Service, not a Deployment with an HPA, so Omni-Compass on top of it needs a muscle for the
KPA's own settings (its target and its panic window). That muscle is engine work: it is built through the model gate and
lands as the next version before Knative's four ways are run; until then Knative's row reads not yet run.

## The products that cannot be run here, and why

StormForge Optimize Live, Cast AI, ScaleOps, PerfectScale, Sedai, IBM Turbonomic, Spot Ocean and Akamas are commercial
services: each needs an account of its own, most run a component in the vendor's own cloud, and their terms of service may
forbid publishing a benchmark of the product. None is run until the founder opens an account and each one's terms have been
read for such a clause; where the terms allow it, the product runs four ways on the same harness, and where they forbid it,
its row says so and it is not run. Each row stands in the register as not yet run, never with a result before one exists.

## What counts

A run counts only on a commit that carries this page and the product's installer, with every reset check passing and every
pinned file matching its checksum. An arm whose product fails to install or start is INVALID, named with its reason, never
counted. The first repetition of each product's first run is a shakedown.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
