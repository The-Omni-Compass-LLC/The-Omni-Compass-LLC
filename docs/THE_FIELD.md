# The field: every product that reads, shows or acts on the systems Omni-Compass governs, and the benchmark each one takes

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This page is the map the founder asked for: the products that read, show or act on computing, cloud, AI and GPU, energy,
facility and industrial systems, sorted by what each one does with what it reads, and for each one the benchmark that
would put Omni-Compass on top of it. It is a map, not a result. Every fact about another product is read from that
product's public pages, its documentation, its license file or the press, and numbered to its source at the foot of the
page. A savings figure a vendor publishes is the vendor's claim and is called one. Where no source was found, or two
sources disagree, the row says so. Nothing on this page was measured: no row says how Omni-Compass compares with any
product, because that is what the benchmarks below are for, and each is read by the repository's one key
(`tools/readings.py`) only after its three runs. It is not complete: the field moves weekly, and a product missing here is
missing from this reading, not judged.

The seven-measure grades of the closest products are in `docs/LANDSCAPE.md`; what each native system controls, from its
maker's publications, is in `docs/COMPARISON.md`; the formal seat is in `docs/THE_SEAT.md`. Read on 24 October 2026 by The
Omni-Compass LLC from public material; no outside party has reviewed it.

Omni-Compass, in every row below, is this repository's supervisory governor (omni-v23 stands, `README.md`): it sits on top
of a system's native controllers, reads the whole body each beat (every 60 s on the main engine; a dial from 5 to 120 s, the fast checks every 5 s), decides by the compass law, writes each setting
through a two-way plug that reads every write back, audits every decision, hands every setting back to native gradually
after a crash (the lease), and has a separate, instant kill switch for security. It never replaces native.

## How to read the tables

- **Does**: *reads only* (collects, stores, shows, alerts a person); *a person acts* (a console where a person makes the
  change); *acts automatically* (the product writes settings itself, on its own loop); *recommends, or acts* (both modes,
  the operator's choice).
- **GitHub's free machines**: *yes* (runs in containers or in a kind cluster on a free runner, as every Kubernetes set here
  does, at $0); *yes, with an account* (the in-cluster part runs on the runner but talks to the vendor's service, so it needs
  an account, a key in the repository's secrets and terms that allow the use); *no* (it needs a cloud's managed cluster, a
  GPU, bare metal with power registers, or a real facility).
- **Omni-Compass with it**: *beside* (a reader: a meter both arms share, never an arm); *on top* (Omni-Compass writes the
  product's own targets and bounds, or the muscles the product leaves alone); *on top, the shared knob left native*: where
  the product writes the same knob, Omni-Compass leaves that muscle native with `--native MUSCLE` (omni-v14 on;
  `omni_controller/controller.py` names the muscles machines, replicas, cpu, clock, gpu, rollout, batch, rightsize,
  coldstart, contain and cooling) and governs the rest, or reaches the knob through the product's own object by a plug, as
  it already does on KEDA's ScaledObject and Crane's EHPA.
- **Register row**: a row of `docs/REGISTER.md`, section 4 (the open benchmarks, in order), unless section 2 is named.

**The benchmark every acting product takes** (written once here; each row names only what differs). Native is the product
as its maker ships it, with its documented defaults, on the same organism; omni is Omni-Compass on top of it. Both arms see
the same load (each organism's own, the climb 1 2 3 2 3 4 …, and work waiting in line), back to back on fresh clusters,
paired, preregistered, frozen on one tuning case and run three times (A, B and C). For a product that acts, the founder's
four ways of 20 October (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6) carry the comparison asked for here, "that
product instead of Omni-Compass": the organism alone, the product on it, Omni-Compass on the organism alone, and
Omni-Compass on top of the product, every pair read within the same repetition. Where native's own controllers can be
switched off, Omni-Compass direct (`README.md`) is a fifth way. The gauges: **work** (requests served inside the response
line, jobs done, transactions); **speed** (the 95th percentile, job wait, queue time); **misses and failures** (failed
requests, pods left waiting, out-of-memory kills, CPU throttling, alert minutes, limit excursions); and **what was spent**
(replicas, machines and node-hours, energy, the bill in machine-hours at list price). Every controller's own writes are
counted (`tools/live_reps.py`, the babysitting rows), and the product's own processor and memory are shown.

**Before any vendor's product is run.** A proprietary license can forbid publishing a benchmark without the vendor's
consent (the "DeWitt clause"); open-source licenses generally do not [76]. Each commercial row below is run only after its
terms have been read for evaluation use and for publication, and a trial must be long enough for the tuning case and the
three runs. CruiseKube, under the Business Source License, already runs here for evaluation under its terms.

## 1. Observers: they collect and show

| Product (owner) | What it is | Does | License, access | GitHub's free machines | Omni-Compass with it, and its benchmark |
|---|---|---|---|---|---|
| Prometheus | metrics scraping, time-series storage, queries and alert rules | reads only; alerts go to a person or a webhook | open source, Apache-2.0 [1] | yes | beside: a meter both arms can share. The Kubernetes governor reads the cluster's metrics API and its own response probe, not Prometheus. The pipeline is itself a benchmark: its shipped scrape and queue limits as native (register row 73) |
| Grafana (Grafana Labs) | dashboards and alerting over many data sources | reads only | open source, AGPL-3.0 [2] | yes | beside: can draw both arms' series |
| Grafana Alloy | Grafana's telemetry collector | reads only | Apache-2.0 [3] | yes | beside; the row-73 pattern |
| OpenTelemetry Collector (CNCF) | vendor-neutral receiving, processing and export of traces, metrics and logs | reads only | Apache-2.0 [4] | yes | beside; register row 73: its batch, queue and sampling limits as native, Omni-Compass on top; dropped points (never more), delay, CPU |
| VictoriaMetrics; Thanos; Grafana Mimir | Prometheus-compatible time-series stores | reads only | Apache-2.0 [5]; Apache-2.0 and AGPL-3.0 [6] | yes | beside |
| Zabbix; Netdata | infrastructure monitoring and alerting | reads only | AGPL-3.0; GPL-3.0 [7] | yes | beside |
| Kepler (CNCF) | energy exporter per container, pod and node, from the processor's power registers | reads only | Apache-2.0 [8] | no for a measurement: GitHub's virtual machines have no power registers to read (register row 79) | beside: the shared meter of both arms on bare metal (`docs/METER_PREREGISTRATION.md`) |
| Elasticsearch and Kibana (Elastic) | search, log analytics, dashboards | reads only | AGPL-3.0 added as an option on 29 August 2024, beside SSPL and ELv2 [9] | yes | beside |
| Datadog | observability service: infrastructure, traces, logs | reads; it now also acts (its Kubernetes Autoscaling, section 4a) | commercial; a free plan for up to 5 hosts with 1-day metric retention [10] | yes, with an account | beside as an observer; its autoscaler is benchmarked as an optimizer |
| New Relic | observability service | reads only | commercial; a free plan with 100 GB of ingest a month and one full user, per a comparison site (the vendor's page could not be read from here) [12] | yes, with an account | beside |
| Dynatrace | observability with its Davis AI; workflows triggered by a problem can scale capacity or restart a service, by the vendor's description [14] | reads; acts through workflows a person writes | commercial | yes, with an account | beside; a workflow that scales is an acting controller and would be benchmarked as one, the workflow as written its native. No independent evaluation of its remediation was found [14] |
| Splunk and AppDynamics (Cisco) | logs, security analytics, application monitoring; Cisco closed its purchase of Splunk in March 2024, about $28 billion, and joined AppDynamics to it [15] | reads only | commercial | yes, with an account | beside |
| Honeycomb | event-based observability | reads only | commercial; a free tier of 20 million events a month, per a pricing aggregator [13] | yes, with an account | beside |
| Chronosphere | cloud-native observability platform; Palo Alto Networks agreed to buy it for $3.35 billion (announced late 2025) and said it would pair it with its AgentiX agents to move from monitoring to autonomous remediation [16] | reads only today; acting is the buyer's stated plan, not a shipped feature found here; the closing was not verified | commercial | yes, with an account | beside |

An observer decides nothing, so "instead of Omni-Compass" has no meaning for it. The observability vendors are moving
toward acting (Datadog's autoscaler, Dynatrace's workflows, the stated Chronosphere plan); each acting part is in section 4
or 5.

## 2. Consoles and cluster managers: a person clicks

| Product (owner) | What it is | Does | License, access | GitHub's free machines | Omni-Compass with it |
|---|---|---|---|---|---|
| Rancher (SUSE) | multi-cluster Kubernetes management; Rancher Prime is SUSE's paid edition on the same open code [17] | a person acts | Apache-2.0 [17] | yes | beside: a person's change through it is a native write Omni-Compass must keep |
| Portainer | container and Kubernetes management interface | a person acts | Community Edition under the zlib license [18]; Business Edition commercial, three nodes free (third-party sources) [18] | yes | beside |
| Lens (Mirantis) | desktop Kubernetes environment; its Lens Prism assistant answers questions inside the user's own permissions [19] | a person acts | Lens Desktop proprietary, with a free personal tier and paid plans (Plus at $25 a user a month on its pricing page); the OpenLens code is MIT [19] | yes (a desktop tool) | beside |
| OpenShift web console (Red Hat) | the console of OpenShift and OKD | a person acts | Apache-2.0 [20] | not tried (OKD is heavy for one runner) | beside |
| Kubernetes Dashboard | the project's web interface | a person acts | Apache-2.0; archived for lack of maintainers (one guide dates it 21 January 2026), SIG UI points to Headlamp [21] | yes (archived) | beside |
| Headlamp (Kubernetes SIG UI) | web and desktop Kubernetes interface | a person acts | Apache-2.0 [21] | yes | beside |
| k9s | terminal interface for Kubernetes | a person acts | Apache-2.0 [22] | yes | beside |
| Spectro Cloud Palette | full-stack cluster lifecycle from declarative "cluster profiles" it follows when it provisions, scales and maintains clusters [23] | a person declares; it reconciles to the declaration | commercial; its docs state a free tier [23] | not tried | beside: it holds a cluster to a declared shape; Omni-Compass moves settings inside that shape. Any reconciler that would undo the governor's writes is pointed away from the governed knobs in the preregistration |
| Cloud consoles (Azure, AWS, Google Cloud); VMware vCenter | the clouds' and the hypervisor's own consoles | a person acts | commercial | — | beside |
| SCADA and HMI (Inductive Automation's Ignition, AVEVA) | the supervisory screen over plant controllers, setpoints bound to the controllers' tags [24] | a person acts | commercial (trial software) | not tried | beside: a person's command is never a lever (`docs/REGISTER.md`, section 4) |

No console is an arm, and "instead" has no meaning for one. One test does matter: a person's write through a console during
a governed run is kept, because the governor reads native's own setting each beat and hands back on the lease. That is a
robustness test (`docs/ROBUSTNESS_PREREGISTRATION.md`), not a comparison.

## 3. Native controllers and schedulers: the muscles' own loops

These are the native arm itself. Omni-Compass is built to sit on them.

| Controller (owner) | Its loop, and the layer | License | GitHub's free machines | Omni-Compass on top | In this repository |
|---|---|---|---|---|---|
| Horizontal Pod Autoscaler (Kubernetes) | replicas from a target utilization, checked every 15 s by default [25] | Apache-2.0 [25] | yes | its target, floor and cap (muscle replicas) | every Kubernetes set |
| Vertical Pod Autoscaler (Kubernetes) | requests from observed use; its in-place update mode is beta in 1.35 [26] | Apache-2.0 [25] | yes | its bounds | register row 68; its recommender under Goldilocks (row 80) |
| In-place pod resize (Kubernetes) | requests and limits changed on a running pod; stable in Kubernetes 1.35 [26] | Apache-2.0 | yes | the path the cpu muscle writes through | every set on 1.35 |
| Cluster Autoscaler (Kubernetes) | adds nodes when pods cannot be placed, removes underused ones | Apache-2.0 [25] | yes with KWOK's machine-less nodes [78]; real nodes need a cloud | the node pool (muscle machines) | the Azure sets (`results/live/AKS_BILL.md`); row 68 |
| Karpenter; AKS node auto-provisioning; EKS Auto Mode | node provisioning for pending pods; AKS's is managed Karpenter [27]; EKS Auto Mode runs Karpenter-style autoscaling for the customer [28] | Karpenter Apache-2.0 [27]; the managed modes commercial | no (a cloud) | Omni-Compass decides when capacity is needed ahead of demand; Karpenter provisions it | row 68, next on AKS; `eks-metered.yml`, `gke-metered.yml` |
| GKE Autopilot (Google) | Google runs the whole node lifecycle [28] | commercial | no | the pods' knobs only (no node knob is given) | row 38 |
| KEDA (CNCF) | event-driven scaling, to and from zero | Apache-2.0 [29] | yes | its ScaledObject, through a plug | three-run tables (below) |
| Knative Serving autoscaler | concurrency target, scale to zero | Apache-2.0 [29] | yes | the concurrency target | row 46, queued |
| kube-scheduler; Descheduler | pod placement; eviction to rebalance | Apache-2.0 [31] | yes | Omni-Compass never places a pod | scheduler run (`results/live/GOVERNORS.md`); descheduler not registered |
| Kueue; Volcano; YuniKorn; KAI; Koordinator | batch admission, gang scheduling, queues, colocation | Apache-2.0 each [30] | yes | its own muscles beside the scheduler's | four ways, all but YuniKorn (`results/live/GOVERNORS.md`); YuniKorn not registered |
| Slurm (SchedMD) power saving | suspends nodes idle for `SuspendTime`, resumes them for work [32] | GNU GPL [32] | yes, as a container cluster | suspend timing and admission | row 48, queued |
| Linux frequency governors and RAPL | the kernel picks a clock; RAPL meters and caps package power | part of the Linux kernel | no for energy (no power registers) | the frequency ceiling (muscle clock) | row 18, kit ready (`docs/CPU_POWER_PREREGISTRATION.md`) |
| NVIDIA driver power limit; DCGM | per-card power limit (`nvidia-smi -pl`, as root) and DCGM's management interfaces [33] | DCGM Apache-2.0 [33]; the driver proprietary | no (a GPU) | the power limit and clock ceiling (muscle gpu) | register section 2, rows 13 to 17; the Lambda kit |
| NVIDIA workload power profiles; Domain Power Service | vendor bundles of power, clock and link settings from Blackwell B200 on; DPS power policies and automatic redistribution of reserved power [34] | proprietary | no | on top of the profile chosen (also listed in 4c) | not registered (row 86 is the NVIDIA Power Manager) |
| GEOPM (Intel) | job-level runtime that moves power caps toward a job's critical path inside a budget [35] | BSD-3-Clause [35] | no (power registers) | the budget it shares | not registered; EAR (row 87) is the registered HPC energy runtime |
| VMware DRS; VCF Operations (Broadcom) | DRS balances hosts inside a cluster; VCF Operations places and rightsizes VMs between clusters, by recommendation or automatically [36] | commercial | no | on top | not registered |
| Building management systems | HVAC sequences and setpoints | commercial | no (a building); modelled stand-ins BOPTEST and Sinergym [77] | setpoints (muscle cooling) | rows 9 and 10 queued; CityLearn's controller run |
| DCIM (Schneider EcoStruxure IT, Sunbird, Nlyte, Vertiv Environet) | data-centre monitoring of assets, power, cooling and space; Environet is also listed with control, by an aggregator [37] | commercial | no | beside (mostly reads) | — |
| Grid voltage control: tap changers, regulators, capacitors | local control at each device; an ADMS closes the loop over SCADA (section 4b) [38] | — | pandapower yes | the substation's setpoint, one whole tap at a time | pandapower three-run tables |
| Battery management and site energy management | charge and discharge rules | — | modelled: CityLearn | the battery's command | CityLearn three-run tables |
| Robot servos | the position servos a robot ships with | — | MuJoCo yes | the speed override inside the takt | MuJoCo three-run tables |

## 4. Automatic optimizers that decide and act: the true comparables

### 4a. Kubernetes and cloud

| Product (owner) | What it is | Does | License, access | GitHub's free machines | Omni-Compass on top | What differs in its benchmark | "Instead" meaningful |
|---|---|---|---|---|---|---|---|
| IBM Turbonomic | resource management across clouds, VMs and Kubernetes: resizes container requests and limits, moves pods to other nodes, provisions and suspends nodes, in real time or through a deployment pipeline; some pod moves are recommend-only [39] | recommends, or acts | commercial; a 30-day SaaS trial without a credit card on IBM's pricing page; a 2024 IBM community answer says that trial covered clouds, not VMware [39]; Kubernetes through the kubeturbo agent, one per cluster [39] | yes, with an account (kubeturbo on kind; the trial's Kubernetes coverage not verified) | on top; the knobs it acts on left native (`--native rightsize,cpu,machines` as the preregistration fixes) | native: automatic mode on. IBM bought Kubecost on 17 September 2024 and ties Turbonomic's actions to Kubecost or OpenCost cost [40] | yes |
| ScaleOps | rightsizes pod requests beside the HPA and KEDA without changing their configuration; a replica-optimization feature manages their minimums, maximums and triggers [43] | acts automatically | commercial; a self-hosted agent in the cluster (not a hosted service, by its own FAQ); a 30-day trial; $5 a vCPU a month on its Growth plan (its pricing page, read through a search) [43] | yes, with a trial key (install on kind not verified) | on top, `--native rightsize,cpu`; the HPA's bounds go to whichever arm the preregistration gives them | native: ScaleOps on the HPA, and on KEDA's HTTP set. Its "up to 80%" saving is its own claim [43] | yes |
| StormForge Optimize Live (CloudBolt) | machine-learning rightsizing of requests and limits, with the HPA's target utilization rewritten so the two do not fight; a 7-day learning period with manual apply, then automatic deployment by annotation; its applier holds the Kubernetes edit role [44] | acts automatically after learning | commercial; CloudBolt bought StormForge on 31 March 2025 [44]; an in-cluster agent with the vendor's service; no trial terms found | yes, with an account | on top, `--native rightsize,cpu`, the HPA target left to it | native: automatic deployment on, its learning done on the tuning load and frozen, as the Goldilocks set learns (`docs/GOLDILOCKS_PREREGISTRATION.md`) | yes |
| CAST AI | a workload autoscaler (requests, in place on Kubernetes 1.33+) with its own HPA; a node autoscaler with bin-packing, Spot and rebalancing that replaces the cluster autoscaler [42] | acts automatically | commercial; a $0 plan for monitoring and recommendations; automation in paid tiers (from $200 a month plus $5 a CPU on its pricing page, read through a search; may have changed) [42]; a user review reports a team kept only the free monitoring [42] | workload side not verified on kind; node side no (EKS, GKE or AKS) | on top of the workload side with `--native rightsize,cpu`; its node side replaces native, so the four ways put Omni-Compass on the cloud's own autoscaler beside CAST AI in its place | native: CAST AI as shipped on AKS (`aks-metered.yml`) | yes, four ways required |
| Sedai | "autonomous" optimization across Kubernetes (EKS, AKS, GKE and others), Lambda, Fargate, ECS, EC2 and EBS, in three modes: Datapilot (view only), Copilot (acts after approval), Autopilot (acts on its own) [45] | recommends, or acts | commercial; an agent in the cluster or by API; Copilot and Autopilot not yet for every resource type, by its docs [45]; no trial terms found | yes, with an account (kind not verified) | on top, the knobs it acts on left native | native: Autopilot | yes |
| Datadog Kubernetes Autoscaling | horizontal (replicas) and vertical (requests and limits, in place on 1.33+) scaling through a `DatadogPodAutoscaler`; a Preview mode only shows; up to 1,000 workloads a cluster; announced in beta on 26 June 2024 [11] | recommends, or acts | commercial; a Datadog account, Agent and Cluster Agent 7.66.1+, Remote Configuration; which plans include it is not stated [11] | yes, with an account | on top, `--native replicas,rightsize,cpu` where it acts | native: its applying mode | yes |
| PerfectScale (DoiT) | autonomous rightsizing with stability signals (out-of-memory kills, throttling) as goals; in place on 1.33+; reads the Karpenter, Cluster Autoscaler and Autopilot settings [47] | recommends, or acts | commercial; DoiT bought it on 4 February 2025; a free plan up to 200 vCPU a month on its pricing page (another listing says 300); automation in a 30-day trial [47] | yes, with an account | on top, `--native rightsize,cpu` | native: its automation on | yes |
| Densify Kubex | a mutating admission controller that sizes requests and limits at deployment, suppresses changes that would fight an HPA, and logs its actions [46] | acts automatically | commercial; a controller in each cluster, its code on GitHub [46] | yes, with an account | on top, `--native rightsize` | native: the controller on; its "up to 80%" claim is its own [46] | yes |
| Spot Ocean (Flexera) | Kubernetes infrastructure autoscaler with automatic headroom (up to 5% of capacity by default) and manual or automatic rightsizing [49] | acts automatically | commercial; Flexera completed buying Spot from NetApp on 3 March 2025; billed per vCPU-hour with minimum fees; no trial found [49] | no (a cloud) | it replaces the cluster autoscaler: four ways | native: Ocean on EKS or AKS | yes, four ways |
| Akamas | tunes container resources and the runtime inside them (heap, garbage collection) under response-time constraints; changes approved by a person, applied through CI/CD or applied by itself [48] | recommends, or acts | commercial [48] | yes, with a license | on top of the configuration it settles | Akamas runs its own experiments: native is the configuration it selects, frozen, then the paired runs | yes, on its final configuration |
| Komodor (its agent, Klaudia) | detects, investigates and remediates (restarts, rollbacks), rightsizes and moves pods between nodes, inside per-cluster policies [56] | acts, with or without a person | commercial; its agent under Komodor's own license [56] | yes, with an account | on top; its remediations are native writes | native: its policy on | partly: it overlaps on rightsizing; remediation is another job |
| Zesty Kompass | headroom reduction: hibernated nodes resumed within 30 s, minimum replicas lowered, with the Cluster Autoscaler or Karpenter [51] | acts automatically (its docs differ on whether the replica step is automatic) [51] | commercial; a base fee plus a fee per managed CPU [51] | no (AWS) | on top of the node pool it keeps | `eks-metered.yml` | yes |
| nOps Compute Copilot | on top of Karpenter: rewrites NodePools for Reserved Instance, Savings Plan and Spot use [52] | acts automatically | commercial | no (EKS) | on top for the pool's size; beside on purchasing | a bill-first set (the cloud order of 14 October) | partly (purchasing, not service) |
| CloudPilot AI | Karpenter-based node optimization with Spot interruption prediction (45 minutes ahead, its claim) [57] | acts automatically | commercial | no (EKS) | as on Karpenter | `eks-metered.yml` | yes |
| Harness CCM (AutoStopping, Cluster Orchestrator) | scales idle non-production deployments to zero on ingress traffic or a schedule; an EKS orchestrator for Spot, autoscaling and bin-packing [53] | acts automatically | commercial; a free tier with 2 clusters and 10 AutoStopping rules [53] | yes for AutoStopping | on top | narrow: idle non-production work | partly |
| Kubecost Actions (IBM) | scheduled request sizing, cluster and namespace turndown, guided sizing (alpha); needs its Cluster Controller with write access, and its docs warn some actions cannot be undone [40] | acts on a schedule | commercial; whether Actions come with its free tier was not verified | yes, with its controller | on top | native: request sizing on its schedule | yes, for request sizing |
| OpenCost (CNCF) | Kubernetes cost allocation, the cost engine under Kubecost; incubating since 31 October 2024 [41] | reads only (no automation found in its documented scope) | Apache-2.0 [41] | yes | beside: a bill meter both arms share | — | no |
| kube-green | puts Deployments and CronJobs to sleep on a schedule [58] | acts on a schedule | MIT [58] | yes | on top | native: its schedule | partly (a schedule, not the load) |
| Goldilocks (Fairwinds) | VPA recommendations shown by namespace | recommends | Apache-2.0 [55] | yes | on top | run here (below) | no (it does not act) |
| Crane (Tencent) | predictive HPA (EHPA), recommendations, QoS | acts automatically | Apache-2.0 [55] | yes | on top, through its EHPA by a plug | run here, four ways | yes |
| CruiseKube (TrueFoundry) | in-place rightsizing controller | acts automatically | Business Source License, source-available [55] | yes, for evaluation | on top; never the CPU limit it resizes | run here (below) | yes |
| VMware VCF Operations (Broadcom) | VM rightsizing and placement between clusters, by recommendation or automatically [36] | recommends, or acts | commercial | no | on top | a vSphere lab | yes |
| AWS Compute Optimizer | rightsizing recommendations for EC2, Auto Scaling groups, EBS, Lambda, ECS on Fargate and databases; Kubernetes pods are not among them, and groups running EKS work are excluded [59] | recommends; can apply on a schedule for supported resources [59] | AWS service | no | beside | — | no for Kubernetes |
| AIOps and runbook automation (PagerDuty, BigPanda) | alert correlation and incident automation; runbook actions run diagnostics and fixes [60] | acts on events, from runbooks a person writes | commercial | — | beside: an incident tool, not a resource governor | — | no |
| Intel Granulate; Opsani (both closed) | Granulate's runtime and Kubernetes optimizer, closed by Intel in late 2024 with support to the first quarter of 2025 [50]; Opsani's continuous optimization, bought by Cisco in January 2022 into AppDynamics [54] | — | — | — | — | not runnable | — |

### 4b. Facility, buildings and energy

| Product (owner) | What it is | Does | License, access | GitHub's free machines | Omni-Compass on top | What differs in its benchmark | "Instead" meaningful |
|---|---|---|---|---|---|---|---|
| Google DeepMind data-centre cooling (2018) | a cloud model reads thousands of sensors every five minutes and sends actions that the site's local control system verifies before running them; operators can step in [61] | acts automatically | Google's own, not sold | no | — | the published precedent of a governor on top of native with native keeping the last word | no (cannot be run) |
| Phaidra | autonomous control agents above an existing BMS: they read sensor trends and send instructions back to the BMS; limits, a manual override and a fall-back to the site's own sequences are described by a third-party review; a liquid-cooling agent reads rack power [62] | acts automatically | commercial service [62] | no (a facility) | on top of the BMS; the setpoints it holds are left native | modelled first (class S): Sinergym's data-centre model or BOPTEST [77] with Omni-Compass on top of the baseline; the product itself only on a real site. Savings figures differ by source and were not verified [62] | yes, on a real site |
| Siemens White Space Cooling Optimization (Vigilent's technology) | sensor-driven dynamic control of data-hall cooling, "autonomously optimizing cooling operations" in Siemens's words; Vigilent bought SynapSense from Panduit in May 2023 and states more than 1,000 facilities in 27 countries (its claim) [63] | acts automatically | commercial | no | on top of the BMS; the same setpoints | a real site | yes |
| EkkoSense (EkkoSoft Critical) | sensors and an AI "Cooling Advisor"; control and accountability stay with the operator, in the vendor's words [64] | recommends; a person acts | commercial | no | beside | — | no (it does not act) |
| BrainBox AI (Trane) | deep-learning HVAC control on top of an existing BMS; Trane completed the purchase on 3 January 2025 and pairs it with its cloud building automation as Trane Autonomous Control; up to 25% energy (its claim), more than 14,000 buildings reported [65] | acts automatically | commercial | no | on top of the BMS | BOPTEST stand-in; a real building | yes |
| Honeywell Forge Energy Optimization | cloud machine learning that re-checks building setpoints every 15 minutes, up to 96 times a day, on an existing BMS; launched February 2020; its current status was not verified [66] | acts automatically | commercial | no | on top | a real building | yes |
| Johnson Controls OpenBlue | building platform; with Nantum AI it acts on its own insights in a closed loop, and its OBI agent runs approved workflows with people in the loop [67] | acts, and recommends | commercial | no | on top | a real building | yes |
| PassiveLogic Hive | a controller that replaces the traditional control panel, running a physics-based model of the building at the edge [68] | acts automatically | commercial hardware and software | no | it replaces native: four ways only | a real building | yes, four ways |
| Stem PowerTrack Optimizer (formerly Athena) | switches between battery, on-site generation and grid, and bids in markets [69] | acts automatically | commercial | no | on top of the battery's own management | CityLearn stand-in | yes |
| ADMS volt-var optimization (utility vendors); the GridAPPS-D VVO application (PNNL, Washington State University) | central optimization of regulator and capacitor setpoints sent to the field through SCADA [38] | acts automatically | the vendors' products commercial; GridAPPS-D open source under PNNL's terms (its listing reads "exploratory license"), run in Docker [38] | GridAPPS-D possibly (not tried) | on top of the regulators, as on pandapower's tap changer | native: local regulator control; the product: the VVO application; the IEEE 8500- and 9500-node feeders; voltage violations (misses), energy delivered, tap operations (wear, power given) | yes |

### 4c. GPU and HPC power

| Product (owner) | What it is | Does | License, access | GitHub's free machines | Omni-Compass on top | What differs in its benchmark | "Instead" meaningful |
|---|---|---|---|---|---|---|---|
| NVIDIA workload power profiles and Domain Power Service (Mission Control) | profile requests arbitrated by an engine with scheduler integration; DPS power policies, resource groups and Power Reservation Steering for automatic redistribution [34] | acts automatically (DPS); a profile is chosen | proprietary; Blackwell-class systems | no | on top of the profile chosen, or the card left native (`--native gpu`) | a rented Blackwell node; cost not estimated here | yes |
| Zeus (ML.ENERGY, University of Michigan) | finds a GPU power limit online while a job runs, and searches batch sizes; its paper reports 15.3% to 75.8% less energy than the largest batch at the top power limit (the authors' measurement) [70] | acts automatically | Apache-2.0 [70] | no (a GPU): one A10 on Lambda | the same knob: Omni-Compass on top with `--native gpu` governing admission and clocks, and the four ways for Zeus instead of Omni-Compass | the Lambda kit (`docs/LAMBDA_SETUP.md`: one A10 at about $0.75 an hour) | yes |
| Emerald AI (Conductor) | software that slows, shifts or pauses AI jobs to meet grid events; a 256-GPU trial in Phoenix cut power 25% for three hours with service guarantees held (the paper's report); a 96-GPU trial in London with National Grid [71] | acts automatically | commercial | no | on top of the same cluster, sharing its power budget | a partner cluster and a grid signal | yes, on a shared cluster |
| EAR; the Kubernetes Power Manager; Climatik; PEAKS; NVIDIA Power Manager; Adaptive GPU Power Capping | pieces from the founder's list, registered here (rows 82 to 87; `docs/THE_SEAT.md`) | acts | EPL-2.0; Apache-2.0; the research code has no license file | metal or a GPU | on top | registered | yes |

### 4d. Databases and process plants

| Product (owner) | What it is | Does | License, access | GitHub's free machines | Omni-Compass on top | What differs in its benchmark | "Instead" meaningful |
|---|---|---|---|---|---|---|---|
| DBtune | tests PostgreSQL server parameters against the workload and machine, and applies the best automatically or with approval; RDS, Aurora, Azure Flexible Server, Cloud SQL, CloudNativePG; a spin-off of Stanford and Lund [72] | recommends, or acts | commercial | yes, with an account, on the PostgreSQL rig | on top of the pooler and the pool; the parameters it owns left native | `pgbench.yml` (register section 2, row 30); its "50% to 1000%" figure is its own claim [72] | yes |
| OtterTune | machine-learning tuning of PostgreSQL and MySQL settings, from Carnegie Mellon [73]; the company shut down in 2024, per a third-party profile; the research code's Business Source License turned to Apache-2.0 on 18 January 2024 [73] | acted | the research code Apache-2.0 since 2024-01-18 [73] | yes in principle (older code, not tried) | as for DBtune | — | yes |
| Imubit | closed-loop "deep learning process control" trained by offline reinforcement learning, integrated with the plant's DCS and APC [74] | acts automatically | commercial; its customer figures are its own [74] | no | on top of the plant's loops | the Tennessee Eastman model (register row 13) as the stand-in; a real plant | yes |
| Advanced process control (AspenTech DMC3; Honeywell, Emerson and Yokogawa sell the same class) | multivariable model-predictive control; supervising a plant's regulatory loops is standard APC practice, while the vendor page read here describes the controller only [75] | acts automatically | commercial | no | the industrial precedent of Omni-Compass's seat | Tennessee Eastman | yes |

## 5. Claims of the same seat, or a bigger one

| Product | The claim | What the public material read here shows | Runnable here | The benchmark that would test it |
|---|---|---|---|---|
| IBM Turbonomic | resource decisions from the application down to the infrastructure, across clouds and the data centre [39] | actions on containers, pods, nodes and VMs from one engine, manual or automatic | trial, with an account | four ways on kind, then AKS |
| Sedai | an "autonomous cloud" across Kubernetes, serverless, VMs and storage [45] | three modes; Autopilot not yet for every resource type | with an account | four ways on a cloud cluster |
| Dynatrace | AI operations toward "autonomous cloud management" [14] | problem-triggered workflows; remediation through ticketing or Ansible; no independent evaluation found | with an account | its scaling workflow as native |
| Palo Alto Networks with Chronosphere | from monitoring to autonomous remediation by AI agents [16] | announced; the closing and the product were not verified | — | when it ships, as an acting controller |
| NVIDIA Mission Control | AI-factory operations, power included [34] | power profiles, arbitration, power reservation steering; NVIDIA systems only | no | on a Blackwell system |
| Phaidra | from cooling to the facility's whole operation: electrical distribution, battery dispatch, AI workload scheduling (a research firm's report) [62] | cooling control shipped; the rest stated as direction | no | on a partner site |
| Emerald AI | AI data centres as flexible grid assets [71] | trials at 256 and 96 GPUs | no | on a partner cluster with a grid signal |
| Komodor | an autonomous "AI SRE" [56] | remediation, rightsizing and pod moves inside policies | with an account | its policy as native |
| Johnson Controls OpenBlue | autonomous buildings [67] | closed-loop optimization through Nantum AI; an agent with people in the loop | no | a real building |
| Google Borg; Meta Twine and Dynamo | private cluster managers and power management, published as papers (`docs/COMPARISON.md`) | papers and public traces | no | compared by publication only |

None of the public material read for this page describes one control law that decides across compute, accelerators,
power, cooling, buildings, grids and machines while each layer's native controller keeps running underneath. That is a
statement about public descriptions on 24 October 2026, not a proof that nothing else exists, and not a result.

## The ones that compete: the benchmarks to run

Ranked by how directly each competes: first, it decides and acts automatically; then, on the layers where Omni-Compass's
live muscles act today (replicas, requests and limits, nodes, GPU power, cooling setpoints); then, more than one muscle at
once; then, on top of native rather than in its place. Costs are list prices as read today, never quotes.

| Rank | Product | Why it ranks here | The rig | Cost | GitHub's free machines |
|---:|---|---|---|---|---|
| 1 | IBM Turbonomic | acts across pods, nodes and VMs from one engine, each action with its reason, manual or automatic | kind with kubeturbo against the SaaS trial, then AKS (`aks-metered.yml`) | $0 on the kind rig for 30 days; Azure about $12 a steady run and $22 a burst run (register row 38) | yes, with an account |
| 2 | ScaleOps | the same seat on the HPA and KEDA, vertical and horizontal | kind rig (`scripts/kind_bench.sh`; KEDA's HTTP set, `scripts/kind_addons.sh`) | $0 runner within a 30-day trial; then $5 a vCPU a month (its page) | yes, with a trial key |
| 3 | StormForge Optimize Live | on top of the HPA, writing its target and the requests | kind rig, its 7-day learning on the tuning load first | $0 runner; license by quote | yes, with an account |
| 4 | CAST AI | acts on pods and nodes; its node side replaces the autoscaler | AKS, four ways | Azure as rank 1, plus a paid tier (from $200 a month plus $5 a CPU, its page) | no for the node side |
| 5 | Sedai | Autopilot over Kubernetes and the clouds' services | AKS or EKS | quote, plus the cloud | not verified |
| 6 | Datadog Kubernetes Autoscaling | horizontal and vertical, acting, from an observability vendor | kind rig with a Datadog account | Datadog subscription | yes, with an account |
| 7 | PerfectScale (DoiT) | autonomous rightsizing | kind rig | $0 under 200 vCPU; automation on a 30-day trial | yes, with an account |
| 8 | Densify Kubex | sizing at admission | kind rig | quote | yes, with an account |
| 9 | Spot Ocean (Flexera) | node autoscaling with headroom, in place of the autoscaler | EKS or AKS, four ways | per vCPU-hour with a minimum fee, plus the cloud | no |
| 10 | Phaidra | the facility seat: supervisory over the BMS | modelled first (Sinergym's data-centre model, class S); the product only on a partner site | $0 modelled; a site by agreement | modelled, yes |
| 11 | NVIDIA Domain Power Service and power profiles | the chip maker's own power arbitration | a rented Blackwell node | not estimated | no |
| 12 | Zeus | open-source GPU power-limit optimizer, the same knob | one A10 on Lambda (the GPU kit) | about $7 to $25 (the kit's one-card runs) | no |
| 13 | Emerald AI | grid-driven GPU workload flexibility | a partner cluster | by agreement | no |
| 14 | Siemens WSCO; BrainBox AI (Trane); Honeywell Forge; Johnson Controls OpenBlue | building and data-hall setpoint control | BOPTEST and Sinergym stand-ins; the products on a real site | $0 modelled | modelled, yes |
| 15 | Komodor | remediation and rightsizing agent | kind rig | quote | yes, with an account |
| 16 | Akamas | configuration tuning | kind rig | license | yes, with a license |
| 17 | DBtune | PostgreSQL parameter tuning | `pgbench.yml` | quote | yes, with an account |
| 18 | Zesty Kompass; nOps; CloudPilot AI | node-pool cost optimizers on AWS | `eks-metered.yml` | per CPU or quote, plus EKS | no |
| 19 | Kubecost Actions; Harness AutoStopping; kube-green | scheduled sizing and sleep | kind rig | $0 (free tiers; kube-green MIT) | yes |
| 20 | GridAPPS-D VVO; Imubit and APC | grid and process supervisory optimizers | GridAPPS-D in Docker; the Tennessee Eastman model | $0 (open) or a license | possibly |

**The first five to run**, weighing directness, cost and license together:

1. **ScaleOps on the kind rig**: the closest seat at the lowest cost; a trial key, and its terms read for publication.
2. **StormForge Optimize Live on the kind rig**: the writer of the HPA's target; its learning frozen on the tuning load.
3. **IBM Turbonomic through kubeturbo on its 30-day trial**: the widest acting scope; on kind first, AKS next.
4. **CAST AI on AKS, four ways**: the case where the product replaces a native controller.
5. **Zeus on one Lambda A10**: the first acting GPU optimizer, open source, so no license stands between the run and its
   publication.

Each needs its own preregistration first (the knobs the product owns, the muscles left native, the learning window, the
gauges), a trial run that is never counted, then its A, B and C on the engine that stands.

## Already in this repository

| System | Where | State |
|---|---|---|
| Kubernetes HPA and the default scheduler | every Kubernetes set; `README.md`; `results/live/` | native in every set |
| KEDA 2.21 and its HTTP add-on 0.16 | `results/live/V11_KEDA_REQUESTS.md`, `V11_KEDA_CPU_REQUESTS.md` (register row 68) | three runs on omni-v11 |
| Goldilocks over the VPA's recommender | `results/live/V11_GOLDILOCKS.md` (row 80) | three runs on omni-v11 |
| CruiseKube | `results/live/V10_CRUISEKUBE.md` (row 81) | three runs on omni-v10; its omni-v12 runs come in the campaign (`results/live/GOVERNORS.md`) |
| Crane | `results/live/V12_CRANE_4W_*.md` (row 90) | four ways, three runs, omni-v12 |
| Kueue, Volcano, KAI, Koordinator, the bin-packing scheduler, KubeRay, Karmada, Open Cluster Management, Armada | `results/live/GOVERNORS.md` (rows 63, 88 to 96) | four ways, three runs, omni-v12; Gödel's runs not finished; KubeEdge's and Nephio's rigs not built |
| The governors as an organism of their own, modelled (class S) | `results/orchestra/ORCHESTRA.md` | modelled |
| Azure's cluster autoscaler with the HPA | `results/live/AKS_BILL.md`, `results/live/V1_AKS_*.md`; Google and Amazon in `gke-metered.yml`, `eks-metered.yml` | Azure sets in; the other two clouds behind their checks |
| Karpenter, the Cluster Autoscaler, the VPA | register row 68 | Karpenter next, on AKS; the other two after |
| Kepler as the shared meter | row 79; `docs/METER_PREREGISTRATION.md`, `docs/METAL_KIT.md` | kit built, for bare metal |
| EAR, the Kubernetes Power Manager, Climatik, PEAKS, NVIDIA Power Manager, Adaptive GPU Power Capping | rows 82 to 87; `docs/THE_SEAT.md` | registered |
| The OpenTelemetry Collector and Prometheus as native | row 73 | queued |
| Knative, Slurm, Ray and Dask, Flink, Agones, GitHub's runner controller | rows 46 to 48, 61, 74, 76 | queued |
| CityLearn's controller; pandapower's tap changer; MuJoCo's servos; the drone swarm | `results/live/V11_CITYLEARN.md`, `V11_PANDAPOWER.md`, `V11_MUJOCO.md`, `V11_SWARM.md` | three runs on omni-v11 |
| PostgreSQL behind PgBouncer, MySQL, MongoDB, Redis, Kafka | `results/live/V17_PGBENCH*.md`, `V17_SYSBENCH*.md`, `V17_YCSB*.md`, `V17_REDIS*.md`, `V17_KAFKA*.md` | three runs on omni-v17 |
| The Linux frequency governor | row 18; `docs/CPU_POWER_PREREGISTRATION.md` | kit ready for metal |
| The GPU (one A10, then eight A100, on Lambda) | register section 2, rows 13 to 17; `docs/LAMBDA_SETUP.md` | ready |
| The closest commercial products, graded from public material | `docs/LANDSCAPE.md` | read 24 October 2026 |
| Borg, Twine, Turbonomic and the native systems, compared by publication | `docs/COMPARISON.md`, `docs/THE_SEAT.md`, `docs/RELATED_WORK.md` | publications only |

Every table above is its own engine's record; the engine that stands is omni-v23 (`README.md`), and every benchmark runs
again on it. None of the commercial optimizers of section 4 has been run here.

## Sources

Read on 24 October 2026. License files were read from each project's repository on that date. Where a vendor's own page
could not be reached, the source is the search index's copy of it or a third party, and the row says so.

1. Prometheus license: https://github.com/prometheus/prometheus/blob/main/LICENSE
2. Grafana license: https://github.com/grafana/grafana/blob/main/LICENSE
3. Grafana Alloy license: https://github.com/grafana/alloy/blob/main/LICENSE
4. OpenTelemetry Collector license: https://github.com/open-telemetry/opentelemetry-collector/blob/main/LICENSE
5. VictoriaMetrics license: https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/LICENSE
6. Thanos license: https://github.com/thanos-io/thanos/blob/main/LICENSE ; Grafana Mimir license: https://github.com/grafana/mimir/blob/main/LICENSE
7. Zabbix license: https://github.com/zabbix/zabbix/blob/master/COPYING ; Netdata license: https://github.com/netdata/netdata/blob/master/LICENSE
8. Kepler license: https://github.com/sustainable-computing-io/kepler/blob/main/LICENSE
9. Elastic's AGPL option: https://www.businesswire.com/news/home/20240829537786/en ; https://alternativeto.net/news/2024/8/elastic-reverts-elasticsearch-and-kibana-to-open-source-with-new-agpl-license-option
10. Datadog pricing (the free plan): https://www.datadoghq.com/pricing/
11. Datadog Kubernetes Autoscaling: https://www.datadoghq.com/about/latest-news/press-releases/datadog-announces-kubernetes-autoscaling-to-help-teams-intelligently-optimize-resources-and-cloud-costs/ ; https://docs.datadoghq.com/containers/autoscaling/
12. New Relic's free plan (a comparison site): https://agentdeals.dev/datadog-vs-new-relic ; https://newrelic.com/info/new-relic-vs-datadog
13. Honeycomb's free tier (a pricing aggregator): https://www.modern-datatools.com/tools/honeycomb/pricing
14. Dynatrace: https://www.dynatrace.com/news/press-release/dynatrace-expands-ai-powered-observability-for-kubernetes-environments/ ; https://www.dynatrace.com/news/blog/next-level-batch-job-monitoring-and-alerting-part-2-using-ai-to-automatically-identify-issues-and-workflows-to-remediate-them/ ; https://www.dynatrace.com/news/press-release/dynatrace-opens-its-market-leading-aiops-solution-to-third-parties-for-smart-autonomous-cloud-management/
15. Cisco and Splunk: https://www.techzine.eu/news/infrastructure/117802/cisco-closes-acquisition-of-splunk/ ; https://www.splunk.com/en_us/blog/devops/cisco-and-splunk-bring-full-stack-observability-to-the-entire-enterprise
16. Palo Alto Networks and Chronosphere: https://cyberscoop.com/palo-alto-networks-to-acquire-observability-firm-chronosphere-for-3-35-billion/ ; https://securityboulevard.com/2025/11/palo-alto-networks-to-acquire-ai-era-observability-platform-chronosphere-for-3-35-billion/
17. Rancher license and Rancher Prime: https://github.com/rancher/rancher/blob/main/LICENSE ; https://documentation.suse.com/cloudnative/rancher-manager/latest/en/about-rancher/prime.html
18. Portainer: https://github.com/portainer/portainer ; https://oneuptime.com/blog/post/2026-03-20-portainer-ce-vs-business/markdown (third party)
19. Lens: https://lenshq.io/pricing/lens-k8s-ide ; https://sdtimes.com/kubernetes/mirantis-reveals-lens-prism-an-ai-copilot-for-operating-kubernetes-clusters/ ; https://github.com/lensapp/lens
20. OpenShift console: https://github.com/openshift/console
21. Kubernetes Dashboard to Headlamp: https://kubernetes.io/blog/2026/06/01/dashboard-to-headlamp/ ; https://github.com/kubernetes-retired/dashboard ; https://github.com/kubernetes-sigs/headlamp ; https://computingforgeeks.com/best-kubernetes-ui-management-tools/
22. k9s: https://github.com/derailed/k9s
23. Spectro Cloud Palette: https://docs.spectrocloud.com/tutorials/getting-started/palette/introduction-palette/ ; https://legacy.docs.spectrocloud.com/getting-started
24. SCADA and HMI: https://control.com/news/inductive-automation-releases-update-for-industrial-application-platformwith-new-hmi-and-scada-capabilities/ (as cited in `docs/LANDSCAPE.md`) ; https://www.g2.com/compare/iconics-genesis-vs-inductive-automation-ignition-vs-aveva-edge
25. The HPA: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/ ; the Cluster Autoscaler and the VPA: https://github.com/kubernetes/autoscaler
26. In-place pod resize, stable in 1.35: https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/ ; https://thenewstack.io/kubernetes-vpa-inplace-resize/
27. Karpenter: https://github.com/kubernetes-sigs/karpenter ; AKS node auto-provisioning: https://learn.microsoft.com/azure/aks/node-autoprovision
28. EKS Auto Mode and GKE Autopilot: https://thenewstack.io/a-deep-dive-into-amazon-eks-auto-part-2/ ; https://engineering.01cloud.com/2025/10/aks-automatic-vs-aws-eks-auto-mode-and-gke-autopilot-simplified-kubernetes-showdown/
29. KEDA: https://github.com/kedacore/keda ; Knative Serving: https://github.com/knative/serving
30. Kueue: https://github.com/kubernetes-sigs/kueue ; Volcano: https://github.com/volcano-sh/volcano ; YuniKorn: https://github.com/apache/yunikorn-core ; KAI: https://github.com/NVIDIA/KAI-Scheduler
31. Descheduler: https://github.com/kubernetes-sigs/descheduler
32. Slurm power saving and license: https://slurm.schedmd.com/power_save.html ; https://github.com/SchedMD/slurm/blob/master/COPYING
33. NVIDIA DCGM and the power limit: https://github.com/NVIDIA/DCGM ; https://docs.nersc.gov/jobs/power-capping/ ; https://docs.lambda.ai/hardware/servers/set-lower-gpu-power-limits/
34. NVIDIA power profiles, Mission Control and the Domain Power Service: https://developer.nvidia.com/blog/optimize-data-center-efficiency-for-ai-and-hpc-workloads-with-power-profiles/ ; https://docs.nvidia.com/mission-control/docs/systems-administration-guide/2.1.0/wpps/concepts.html ; https://docs.nvidia.com/datacenter/dps/versions/0.8/guides/concepts/
35. GEOPM: https://github.com/geopm/geopm (its BSD-3-Clause license file) ; https://sc17.supercomputing.org/SC17%20Archive/tech_poster/tech_poster_pages/post176.html
36. VMware VCF Operations: https://blogs.vmware.com/cloud-foundation/2025/11/05/vmware-cloud-foundation-workload-placement/ ; https://blogs.vmware.com/cloud-foundation/2025/08/12/vmware-cloud-foundation-helps-you-optimally-size-vms-and-keep-your-infrastructure-and-workloads-running-smoothly/
37. DCIM: https://www.datacenterknowledge.com/data-center-infrastructure-management/schneider-beefs-up-revamps-its-cloud-dcim-software ; https://www.trustradius.com/products/sunbird-dcim ; https://datacentremagazine.com/top10/top-10-data-centre-infrastructure-management-platforms ; https://us.fitgap.com/products/vertiv-environet
38. Volt-var optimization and GridAPPS-D: https://www.pnnl.gov/publications/voltvar-optimization-vvo-application-gridapps-d-platform ; https://www.pnnl.gov/copyright/gridapps-d ; https://gridappsd-training.readthedocs.io/en/latest/applications/VVO-WSU/README.html ; https://research-hub.nrel.gov/en/publications/smart-grid-enabled-cvr-an-advanced-application-for-distribution-m/
39. IBM Turbonomic: https://www.ibm.com/products/turbonomic/kubernetes ; https://www.ibm.com/docs/SSFV9Z_latest/ux-app/_Target_Configuration_Topics/Container_Opt.html ; https://www.ibm.com/products/turbonomic/pricing ; https://community.ibm.com/community/user/discussion/the-license-issue-for-turbonomic ; https://community.ibm.com/community/user/blogs/jason-shaw/2024/03/25/kubeturbo-agent
40. Kubecost: https://newsroom.ibm.com/blog-ibm-acquires-kubecost-to-broaden-hybrid-cloud-cost-management-capabilities ; https://docs.kubecost.com/using-kubecost/navigating-the-kubecost-ui/savings/savings-actions ; https://community.ibm.com/community/user/blogs/jason-shaw/2025/10/01/turbonomic-integration-with-kubecost-free-opencost
41. OpenCost: https://www.cncf.io/blog/2024/10/31/opencost-advances-to-the-cncf-incubator/ ; https://opencost.io/docs/FAQ ; https://github.com/opencost/opencost
42. CAST AI: https://cast.ai/pricing ; https://docs.cast.ai/docs/woop-in-place-resizing ; https://docs.cast.ai/docs/horizontal-pod-autoscaling ; https://cast.ai/blog/cast-ai-vs-kubecost/ ; https://www.gartner.com/reviews/product/cast-ai
43. ScaleOps: https://scaleops.com/product/automated-pod-rightsizing/ ; https://scaleops.com/product/ ; https://aws.amazon.com/marketplace/pp/prodview-t6ctoxyyxp5zs ; https://sacra.com/c/scaleops/
44. StormForge (CloudBolt): https://www.cloudbolt.io/company/news/cloudbolt-acquires-stormforge/ ; https://docs.stormforge.io/optimize-live/concepts/ ; https://docs.stormforge.io/optimize-live/recommendations/requests-and-limits ; https://www.cloudbolt.io/stormforge-by-cloudbolt/optimize-live/
45. Sedai: https://docs.sedai.io/get-started/onboarding/readme/understanding-operation-modes ; https://intellyx.com/2025/07/01/sedai-autonomous-cloud-computing-optimization/
46. Densify Kubex: https://kubex.ai/blog/kubecon-kubernetes-automation/ ; https://docs.densify.com/docs-kubex/Content/Kubex/Automation_Overview ; https://www.densify.com/lp/kubernetes-resource-optimization
47. PerfectScale: https://www.perfectscale.io/blog/press-release-doit-acquires-perfectscale ; https://perfectscale.io/pricing ; https://www.everydev.ai/tools/perfectscale
48. Akamas: https://www.dynatrace.com/news/blog/dynatrace-apps-showcase-akamas-kubernetes-optimization/ ; https://www.trustradius.com/products/akamas/details ; https://www.gartner.com/reviews/product/akamas
49. Spot Ocean (Flexera): https://www.flexera.com/about-us/press-center/flexera-completes-acquisition-of-netapps-spot-finops-portfolio ; https://docs.flexera.com/spot/ocean/features/ ; https://spot.io/news/configurable-automatic-headroom-size-for-spotinst-ocean ; https://aws.amazon.com/marketplace/pp/prodview-2f6plif6zeqya
50. Intel Granulate closed: https://www.calcalistech.com/ctechnews/article/s1ok9qagyx ; https://en.globes.co.il/en/article-intel-closes-granulate-lays-off-dozens-1001492599
51. Zesty Kompass: https://www.zesty.co/platform/headroom-reduction/ ; https://docs.zesty.co/docs/how-headroom-reduction-works
52. nOps Compute Copilot: https://aws.amazon.com/blogs/apn/automating-cloud-cost-optimization-on-aws-with-nops-compute-copilot-and-karpenter ; https://nops.io/blog/managing-commitments-with-karpenter-the-hard-way-vs-how-nops-makes-it-effortless
53. Harness CCM: https://developer.harness.io/cloud-cost-management/cost-optimization/autostopping-rules/autostopping-rules/kubernetes-autostopping-rules ; https://developer.harness.io/3k-docs/cloud-cost-management/product-behaviour/ ; https://www.harness.io/blog/cloud-autostopping-complements-kubernetes-cluster-autoscaling-cost-savings
54. Opsani and Cisco: https://www.techzine.eu/news/infrastructure/72095/cisco-acquires-opsani-for-insight-into-cloud-native-environments/ ; https://www.fenwick.com/insights/experience/fenwick-represents-cisco-in-agreement-to-acquire-opsani
55. Goldilocks: https://github.com/FairwindsOps/goldilocks ; Crane: https://github.com/gocrane/crane ; CruiseKube: https://github.com/truefoundry/cruisekube
56. Komodor: https://cloudnativenow.com/features/komodor-extends-autonomous-ai-agent-for-optimizing-kubernetes-clusters/ ; https://help.komodor.com/hc/en-us/articles/32313630528786-Self-Healing ; https://github.com/komodorio/helm-charts/blob/master/LICENSE
57. CloudPilot AI: https://aws.amazon.com/marketplace/pp/prodview-njy5lk7ivnckm ; https://dev.to/cloudpilot-ai/cloudpilot-ai-vs-karpenter-smarter-kubernetes-autoscaling-lower-cloud-costs-2b0i ; https://github.com/cloudpilot-ai/karpenter-provider-gcp
58. kube-green: https://github.com/kube-green/kube-green ; https://www.cncf.io/blog/2024/10/01/cncf-and-sustainability-how-cloud-native-projects-are-shaping-the-green-tech-movement/
59. AWS Compute Optimizer: https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html ; https://aws.amazon.com/compute-optimizer/
60. PagerDuty and BigPanda: https://www.pagerduty.com/newsroom/new-pagerduty-capabilities-enable-organizations-to-embrace-modern-approach-to-digital-operations/ ; https://www.bigpanda.io/blog/what-is-pagerduty
61. Google DeepMind's cooling control: https://deepmind.google/blog/safety-first-ai-autonomous-data-centre-cooling-and-industrial-control/ ; https://www.technologyreview.com/s/611902/google-just-gave-control-over-data-center-cooling-to-an-ai ; https://9to5google.com/2018/08/17/google-deepmind-ai-control-data-center/
62. Phaidra: https://phaidra.ai ; https://sacra.com/c/phaidra ; https://www.geekwire.com/2024/phaidra-raises-12m-for-ai-software-that-helps-data-centers-boost-energy-efficiency/
63. Siemens WSCO and Vigilent: https://www.siemens.com/en-gb/products/vigilent-white-space-cooling-optimization-wsco/ ; https://www.businesswire.com/news/home/20230503005132/en/Vigilent-Acquires-SynapSense-Business-from-Panduit-to-Enhance-Customer-Value-and-Accelerate-Growth ; https://www.datacenterdynamics.com/en/news/vigilent-improves-efficiency-at-digital-realty-data-center/
64. EkkoSense: https://www.intelligentcio.com/north-america/2023/05/24/ekkosense-continuous-ai-and-ml-optimization-with-cooling-advisor/
65. BrainBox AI and Trane: https://betakit.com/brainbox-ai-acquired-by-irish-hvac-giant-trane-to-cut-building-emissions-using-ai/ ; https://iotm2mcouncil.org/iot-library/news/smart-building-construction-news/trane-acquires-autonomous-hvac-firm-brainbox-ai/
66. Honeywell Forge Energy Optimization: https://www.automation.com/article/honeywell-announces-launch-of-honeywell-forge%C2%A0ener ; https://facilityexecutive.com/honeywell-forge-energy-optimization
67. Johnson Controls OpenBlue: https://www.unite.ai/johnson-controls-acquires-nantum-ai-to-advance-autonomous-building-energy-optimization/ ; https://www.johnsoncontrols.com/media-center/news/press-releases/2026/08/04/johnson-controls-unveils-ai-powered-openblue-platform-expansions
68. PassiveLogic: https://passivelogic.com/downloads/Hive-ProdSheet-2025_web.pdf ; https://www.buildings.com/building-systems-om/automation-controls/article/33018050/passivelogics-generative-autonomy-platform-sees-high-demand-ahead-of-launch
69. Stem: https://www.barchart.com/story/news/34624712/stem-unveils-powertrack-optimizer-flagship-enterprise-platform-powering-managed-services-strategically-rebranded-to-integrate-into-comprehensive-product-stack ; https://s27.q4cdn.com/138752898/files/doc_news/Stem-Announces-Unified-Athena-Platform-2022.pdf
70. Zeus: https://github.com/ml-energy/zeus ; https://www.usenix.org/system/files/nsdi23-you.pdf ; https://pytorch.org/blog/zeus/
71. Emerald AI: https://www.nvidia.com/en-us/case-studies/emerald-ai/ ; https://arxiv.org/html/2507.00909v1 ; https://nationalgrid.com/uk-first-trial-ai-grid-technology-successfully-demonstrates-ability-data-centres-adjust-power-needs
72. DBtune: https://www.blocksandfiles.com/data-management/2026/10/07/dbtune-autonomous-optimization-blows-postgresql-bottlenecks-away/5301616 ; https://www.postgresql.eu/events/pgconfeu2025/schedule/session/7187-dbtune-ai-driven-performance-tuning-for-all-postgresql-flavors/
73. OtterTune: https://providers.apievangelist.com/providers/ottertune/ ; https://github.com/cmu-db/ottertune/blob/master/LICENSE ; https://www.vldb.org/pvldb/vol11/p1910-zhang.pdf
74. Imubit: https://imubit.com/closed-loop-ai-optimization-for-industrial-processes/ ; https://www.hydrocarbonprocessing.com/news/2024/09/imubit-launches-closed-loop-ai-optimization-solution-powered-by-reinforcement-learning/
75. AspenTech DMC3: https://www.aspentech.com/en/resources/brochure/aspen-dmc3
76. Benchmark clauses in licenses: https://en.wikipedia.org/wiki/David_DeWitt ; https://www.dwheeler.com/essays/dewitt-clause.html ; https://cube.dev/blog/dewitt-clause-or-can-you-benchmark-a-database
77. Sinergym (MIT): https://github.com/ugr-sail/sinergym ; BOPTEST: https://github.com/ibpsa/project1-boptest
78. KWOK: https://github.com/kubernetes-sigs/kwok

Read from public material by The Omni-Compass LLC. No outside party has reviewed or approved this map.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
