# The landscape: what else in the world sits where I sit, and how each one grades

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

I am Omni-Compass: a supervisory governor that sits on top of a system's own native controller and moves that controller's
settings, never replacing it, every muscle only as far as its own limit, everything handed back to native on a lease when I
stop. This page names every product and project I found that does part of that work, says what each one is from its own
public material, and grades each one, and me, on the same seven measures. Read on 24 October 2026; the founder's order of the same day ("engage it against everything ... tell me what
else product you see ... and grade that too").

Every fact about another product below comes from that product's public pages or the press, and is cited; a savings figure a
vendor publishes is a vendor's claim and is called one. A grade is The Omni-Compass LLC's own reading of public material
against the measures written here before the grades; it is not a review of anyone's code, and no outside party has reviewed
it. Where a product's material does not say, the grade says "not published", never a guess.

## The seven measures

| Measure | What earns an A |
|---|---|
| 1. Position | Sits on top of the native controller and leaves it in charge of its own loop; removing it hands every setting back. |
| 2. Mechanism published | The decision law is written out in full, with its mathematics, so an engineer can check it against the code. |
| 3. Evidence method | Paired runs against native on the same machines, every gauge reported (losses included), rules written before the runs, repeated. |
| 4. Evidence scale | Results at production scale, on real customer systems, metered. |
| 5. Breadth | Governs many kinds of muscle (compute, accelerators, power, cooling, buildings, grids, machines), one law for all. |
| 6. Safety design | A bounded authority, a hand-back when it fails, a kill switch, every write read back and audited. |
| 7. The operator's surface | A live surface where the operator sees native and the governed system side by side, reads every gauge in the system's own aim, and turns knobs that act on the live mechanism. |

## Who is in the category

**Kubernetes resource governors (on top of the autoscalers).**

- **StormForge Optimize Live** (CloudBolt): a vertical rightsizer that runs alongside the HPA, using in-cluster agents and
  machine learning to set requests, limits and the HPA's target utilization across workloads
  ([CloudBolt](https://www.cloudbolt.io/stormforge-by-cloudbolt/optimize-live/), [fact sheet](https://www.stormforge.io/fact-sheet/platform-overview/)).
- **Cast AI**: a workload autoscaler that resizes pods in place, and a node provisioner that replaces the cluster autoscaler
  with bin-packing, Spot placement and live migration ([Cast AI](https://cast.ai/blog/best-pod-rightsizing-tools/),
  [Cast AI vs Kubecost](https://cast.ai/blog/cast-ai-vs-kubecost/)). Its node side replaces a native controller rather than
  sitting on it.
- **ScaleOps**: continuous pod rightsizing and replica optimization that manages the HPA's and KEDA's own minimums, maximums
  and triggers ([ScaleOps](https://scaleops.com/product/automated-pod-rightsizing/), [Sacra](https://sacra.com/c/scaleops/)).
- **PerfectScale** (DoiT): autonomous rightsizing with a read-only exporter and stability signals (out-of-memory kills, CPU
  throttling) as goals ([PerfectScale vs Cast AI](https://www.perfectscale.io/vs/cast), [Gartner](https://www.gartner.com/reviews/product/perfectscale-525147701)).
- **Sedai**: autonomous optimization across Kubernetes and the clouds' services, in three modes (observe, approve, autopilot),
  with gradual changes, health checks and rollbacks it says are patented ([Sedai](https://www.sedai.io/tags/availability-optimization)).
- **IBM Turbonomic**: application resource management across hybrid clouds and Kubernetes; resizes requests and limits,
  moves pods, scales clusters, every action audited, manual or automatic ([IBM](https://www.ibm.com/products/turbonomic/application-resource-management.html),
  [Finout](https://www.finout.io/blog/ibm-turbonomic-solution-overview)).
- **Spot Ocean** (Flexera, from NetApp in 2025): a Kubernetes infrastructure autoscaler with headroom kept spare, 5% by default
  ([Flexera](https://www.flexera.com/blog/finops/fast-scaling-for-containerized-workloads-with-automatic-headroom/)). It replaces
  the cluster autoscaler.
- **Akamas**: configuration tuning of containers and the runtime inside them (heap, garbage collection) under response-time and
  error constraints, with an optional human approval ([Dynatrace](https://www.dynatrace.com/news/blog/dynatrace-apps-showcase-akamas-kubernetes-optimization/),
  [Gartner](https://www.gartner.com/reviews/product/akamas)).
- **Intel Granulate**: continuous adaptation of requests and HPA settings; Intel closed the company after failing to sell it
  ([Calcalist](https://www.calcalistech.com/ctechnews/article/s1ok9qagyx)).

**Accelerators and power.**

- **NVIDIA Workload Power Profiles and Mission Control**: vendor-set bundles of a GPU's power, clocks and link states, and a
  power service that makes power a scheduling input for Slurm and Run:ai ([NVIDIA](https://developer.nvidia.com/blog/optimize-data-center-efficiency-for-ai-and-hpc-workloads-with-power-profiles/),
  [Mission Control docs](https://docs.nvidia.com/mission-control/docs/systems-administration-guide/latest/workload-power-profile-solution.html),
  [arXiv 2510.03872](https://www.arxiv.org/pdf/2510.03872)). The chip maker's own knobs, on its own chips.
- **Kepler** (CNCF sandbox): measures each workload's energy and exports it; measures, does not govern
  ([Red Hat](https://next.redhat.com/2023/08/22/introducing-kepler-efficient-power-monitoring-for-kubernetes/)).

**Data-centre cooling and buildings.**

- **Google DeepMind's cooling control (2018)**: a cloud model reads thousands of sensors every five minutes and sends actions
  that the site's own control system checks against operator-set limits before running them
  ([DeepMind](https://deepmind.google/blog/safety-first-ai-autonomous-data-centre-cooling-and-industrial-control/)). The closest
  public precedent of a governor on top of a native control system with the native system keeping the last word.
- **Phaidra**: autonomous cooling agents that read rack power and move coolant distribution ahead of temperature; deployed with
  CoreWeave and piloted elsewhere ([Phaidra](https://phaidra.ai), [DCD](https://www.datacenterdynamics.com/en/news/stt-gdc-to-pilot-phaidras-ai-data-center-cooling-control-system/)).
- **BrainBox AI** (Trane): a software layer on top of an existing building management system, reading points over BACnet and
  writing setpoints back ([BetaKit](https://betakit.com/brainbox-ai-launches-software-to-enable-self-sustaining-commercial-buildings/),
  [RFP wiki](https://www.rfp.wiki/artificial-intelligence/brainbox-ai)).

**The operator's surface in industry.**

- **SCADA and HMI platforms** (Inductive Automation's Ignition, AVEVA): the supervisory layer over plant controllers, with live
  setpoints and buttons bound to the controllers' own tags ([Control.com](https://control.com/news/inductive-automation-releases-update-for-industrial-application-platformwith-new-hmi-and-scada-capabilities/),
  [knowledge base](https://industrialmonitordirect.com/blogs/knowledgebase/building-a-basic-hmi-project-indicators-setpoints)). The
  industrial precedent for knobs on a live mechanism; an HMI shows the plant, not the plant beside a governed twin of itself.

## The grades

Each grade reads public material against the measures above. "np" is not published.

| Product | 1 Position | 2 Mechanism published | 3 Evidence method | 4 Evidence scale | 5 Breadth | 6 Safety design | 7 Operator's surface |
|---|---|---|---|---|---|---|---|
| **Omni-Compass** | A | A | A− | D | A− | A− | B+ |
| StormForge Optimize Live | A− | C | C | B+ | C | B | B |
| Cast AI | C+ (replaces the node autoscaler) | C | C | A− | C+ | B | B+ |
| ScaleOps | A− | C | C | B+ | C+ | B | B |
| PerfectScale | A− | C | C | B | C | B+ | B |
| Sedai | B+ | C | C | B+ | B | B+ | B |
| IBM Turbonomic | B | C | C | A | B+ | B+ | A− |
| Spot Ocean | C+ (replaces the node autoscaler) | C | C | A− | C | B | B |
| Akamas | A− | C+ | C+ | B | B | B+ | B |
| NVIDIA power profiles | B (the vendor's own knobs) | B | B | B+ | C (its own chips) | B+ | B− |
| DeepMind cooling (2018) | A | B− | C+ | A− | C | A− | np |
| Phaidra | A− | C | C | B+ | C+ | B+ | B |
| BrainBox AI | A− | C | C | B+ | C | B | B |
| SCADA / HMI | not a governor | n/a | n/a | n/a | B+ | B+ | A |

## What the grades say about me

- **Where I stand alone in public material.** No other product I found publishes its decision law with its mathematics and its
  engine source, reports every gauge of every paired run against native with the losses kept and the rules written first, or
  governs Kubernetes, accelerators, power, cooling, buildings, grids and machines with one law. The others publish case studies
  whose savings are their own claims.
- **Where I am behind.** Every product above runs on customers' production systems; I have none. My real-software evidence is on
  GitHub's small machines and kind clusters, my clouds are one set in progress on Azure, my GPU result is not in, and my widest
  results are my own models (class S). Evidence scale is my D, and only production runs raise it.
- **The operator's surface.** My live benchmark engine shows native and Omni-Compass on the same monitor, reads every gauge in the gauge's
  own aim (GAIN, STEADY, LOSS), and carries knobs, buttons and lights on every monitor. I found no compute governor whose console
  shows the governed system beside native on the same monitor; SCADA screens carry live knobs on live plants, and that is the
  bar. My live benchmark engine replays my recorded runs and my models in the page; my control API (`tools/omni_control.py`) drives a live
  governor, and the page's grade rises to A when every monitor reads and drives a live system through it.

## The live benchmark engine beside the operator's surfaces that exist

The founder asked what in the world is close to my live benchmark engine's layout. These are the surfaces I found, read from their public
material, on the four things my live benchmark engine is built to do: show the system live, show native and the governed system side by
side on the same monitor, carry knobs and buttons that act on the running mechanism, and order the screen by what the person
watching must see first.

| Surface | Shows the system live | Native beside the governed system on one monitor | Knobs that act on the running mechanism | Ordered by what the watcher must see first |
|---|---|---|---|---|
| Metrics dashboards (Grafana, Datadog) | yes | no: one system's series; a comparison is built by hand | no: read-only by design; alerts route to people | by the dashboard's author |
| Kubernetes consoles (the Kubernetes Dashboard, Lens, Headlamp) | yes: the cluster's own objects | no | yes: scale a deployment, edit, restart; each a manual write | no |
| Rightsizer consoles (Cast AI, ScaleOps, StormForge, PerfectScale) | yes | no: savings read against a computed baseline, not against native running beside it | automation switches per workload; the rules inside are the vendor's | by savings |
| IBM Turbonomic | yes: a supply chain from application to hardware | no | yes: every action with its reason, run by hand or automatically | by the actions pending |
| SCADA and HMI (Ignition, AVEVA) | yes: the plant | no: the plant, not the plant beside a governed copy of itself | yes: setpoints and buttons bound to the controllers' own tags | yes: ANSI/ISA-101.01 (the high-performance HMI: colour only for the abnormal) and ANSI/ISA-18.2 (alarms in priority order) |
| Digital twins (Siemens, AVEVA, NVIDIA Omniverse) | yes: a model of the plant beside the plant | a model beside the real thing, not a governor beside native | what-if runs on the model | by the plant's layout |
| **My live benchmark engine** | my recorded runs and my models, replayed in the page; a live governor through my control API (`tools/omni_control.py`), not yet driven from the page | **yes: native, Omni-Compass on native and Omni-Compass direct on the same monitor, each gauge read in its own aim** | knobs, buttons and a light on every monitor; the one button that puts every knob back to the factory tune; native alone stays the kill switch | the order the founder set on 24 October: what the person watching must see first, down to what they need least |

What the table says: the industrial HMI is the one surface with live knobs bound to a live mechanism and a written order of
importance, and it is the bar my live benchmark engine is held to. No surface I found shows a governed system beside its own native
controller on the same monitor, gauge by gauge. My live benchmark engine does that today on recorded runs; it reaches the HMI's bar when
every monitor reads and drives a live system through the control API.

Run and scored by The Omni-Compass LLC's own reading of public material. No outside party has reviewed or approved these grades.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
