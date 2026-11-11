# The seat: one governor over the muscles

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This page states where Omni-Compass sits among the systems that already run computers, power and machines, what each
of those systems is, who owns what, and what is still to be shown. Every statement about another system is read from
that system's own publication or repository, on the date given; every statement about Omni-Compass is read from this
repository's code and results. Where a statement is wrong or out of date, it is corrected from the maker's own
publication.

## 1. The claim, in one sentence

Omni-Compass is a **supervisory governor**: one control law that reads every muscle in a body at once and writes each
muscle's own knob, inside the envelope its native controller already allows, under the limits the muscles share, while
every native controller keeps running underneath, unchanged. It is never standalone and never a replacement for the
native controller: a benchmark has two arms only, native, and Omni-Compass on top of native (`CLAUDE.md`, "What Omni
is").

What makes it one governor and not a collection of tools is stated formally in `docs/FORMAL_V5.md` (Definition 2 and
Proposition 1): the knob it writes on one muscle depends on what every other muscle is doing, through the lines they
share (a battery site's grid connection, a room's cooling). A collection of separate tools cannot have that property,
however many run at once: each decides on its own reading and writes only its own knob.

## 2. Muscles and governors

A **muscle** is a controller of one kind of knob on one kind of system: how many machines, how many replicas, a power
limit, a frequency, a temperature setpoint, a cache size. A **governor** decides, for the whole body at once, what each
muscle may do. The systems in common use are muscles, or optimizers over a few kinds of muscle; Omni-Compass sits on top
of them and calls them.

### 2.1 The five systems named most often

| System | Maker | Source | What it controls (its maker's description) | Kind | Omni-Compass with it |
|---|---|---|---|---|---|
| IBM Turbonomic | IBM | closed, commercial | resource actions across layers: sizing, placement and scaling of workloads and hosts | an optimizer over several kinds of muscle, not one control law | on top of the muscles it drives, or compared on the customer's own system in paired runs; it cannot be run here |
| Karpenter | AWS; its core is a Kubernetes SIG Autoscaling project (`kubernetes-sigs/karpenter`) | open source (Apache-2.0) | provisions and removes nodes for pending pods | node-provisioning muscle | on top: Omni-Compass decides when nodes are needed ahead of demand; Karpenter provisions them (register row 68, on a cloud) |
| NVIDIA's GPU power-management software (power profiles and the dynamic power tools above the driver) | NVIDIA | closed (user-space software on top of the driver; the Linux kernel and its NVIDIA modules are a separate layer) | power limits and power profiles on NVIDIA GPUs | power-limit muscle | on top: Omni-Compass writes the card's clock ceiling and power limit through the driver's own tool (`nvidia-smi -lgc`, `-pl`; `omni_controller/gpu_compass.py`), inside the envelope the card allows; the receipt is the chip-level energy run (section 5) |
| Energy Aware Runtime (EAR) | Barcelona Supercomputing Center | open source (EPL-2.0, `github.com/eas4dc/EAR`) | CPU frequency selection per application and node, energy accounting, and a global energy manager for supercomputers | energy muscle with its own optimizer at node and job level | on top, on bare metal with access to the CPU's power registers (register row 87) |
| Cluster Autoscaler, with commercial layers such as ScaleOps and Cast AI | the Kubernetes project; the vendors | Cluster Autoscaler open source (Apache-2.0); the commercial layers closed | adds nodes when pods cannot be placed, removes them when unneeded; the commercial layers sell optimization on top | node muscle, and optimizers above it | on top of the Cluster Autoscaler (register row 68); the commercial layers are compared on a customer's system, as Turbonomic |

Run all five at once and there are still five systems, each reading its own gauges through its own interface and
writing its own knobs. Nothing among them makes one decision for the whole body under the limits the muscles share.
That is the seat Omni-Compass is written for.

### 2.2 Open-source pieces that can be benchmarked with Omni-Compass on top

Read from each repository on 12 October 2026 (its README, its license file and its last commit). The license is the
file in the repository, not a description of it.

| Project | Repository | What it is, in its own words | License found | Last commit | Kind | Where it can run | Register |
|---|---|---|---|---|---|---|---|
| Kepler | `sustainable-computing-io/kepler` | "a Prometheus exporter that measures energy consumption metrics at the container, pod, and node level in Kubernetes clusters" | Apache-2.0 | 2026-10-12 | a meter, not a controller | a machine with the processor's power registers (RAPL), through the meter kit (`docs/METAL_KIT.md`); on GitHub's virtual machines Kepler 0.10 and later run only a stand-in development meter | row 79 |
| Goldilocks | `FairwindsOps/goldilocks` | "a utility that can help you identify a starting point for resource requests and limits" (built on the Vertical Pod Autoscaler's recommender) | Apache-2.0 | 2026-09-18 | a recommendation tool over a muscle (VPA) | GitHub's machines (kind) | row 80 |
| CruiseKube | `truefoundry/cruisekube` | "an intelligent Kubernetes resource optimization controller that automatically monitors, analyzes, and applies resource recommendations" | **Business Source License** (source-available, not open source) | 2026-08-06 | a rightsizing muscle | GitHub's machines (kind), for evaluation under its license | row 81 |
| Climatik | `Climatik-Project/Climatik-Project` | a power-capping operator for Kubernetes (its README is the operator template, unfinished) | Apache-2.0 | 2024-09-10 | power-capping muscle, early stage | a machine with power control (GPU) | row 82 |
| Kubernetes Power Manager (AMD EPYC) | `AMDEPYC/kubernetes-power-manager` (a fork of Intel's `intel/kubernetes-power-manager`) | "a Kubernetes Operator ... to dynamically request adjustment of worker node power management settings applied to cores allocated to the Pods" | Apache-2.0 | 2025-11-07 | CPU power muscle | bare metal with the processor's power controls | row 83 |
| PEAKS | `sustainable-computing-io/peaks` | "Power Efficiency Aware Kubernetes Scheduler" (its README is meeting notes; the design is in its docs) | Apache-2.0 | 2024-10-23 | a scheduler, early stage | GitHub's machines (kind) once it runs | row 84 |
| Adaptive GPU Power Capping | `tanish111/Adaptive-GPU-Power-Capping` | the code for the paper "Adaptive GPU Power Capping: Balancing Energy Efficiency, Thermal Control and Performance" (HPDC '25): a learned model choosing GPU power caps | **no license file** (no right to reuse the code without the authors' permission) | 2025-04-29 | a research power-capping method | a rented GPU; compared from the paper's own method unless the authors grant use | row 85 |
| NVIDIA Power Manager | `NVIDIA/nvidia-power-manager` | "Nvidia power management app." | Apache-2.0 | 2026-07-13 | platform power muscle (NVIDIA server platforms) | NVIDIA server hardware | row 86 |
| Energy Aware Runtime | `eas4dc/EAR` | "an energy management framework for super computers" | EPL-2.0 | 2026-09-28 | energy muscle and optimizer (HPC) | bare metal with the CPU's power registers, under a batch scheduler | row 87 |

Already benchmarked or registered: the Kubernetes HPA (every Kubernetes set), KEDA and its HTTP add-on (done, three
runs), Karpenter, the Cluster Autoscaler and the Vertical Pod Autoscaler (register row 68).

None of these projects is described by its makers as one law deciding for the whole body. That is a statement about
their public descriptions on the date above, not a proof that nothing else exists anywhere.

## 3. How a benchmark with each of them is built

The same way as every benchmark here: the project, installed as its makers ship it, is the native; Omni-Compass on top
of it is the other arm; both arms see the same work; the rules are written before the counted runs, frozen on one
tuning case and run three times (A, B, C); every row is reported, losses included (`docs/HOW_TO_READ_THE_RESULTS.md`).
A meter (Kepler) is not an arm: it reads both arms the same way, so its numbers sit beside the arms' own gauges.

Order (one or two at a time): Goldilocks with the Vertical Pod Autoscaler, and Kepler as the shared meter, on GitHub's
machines first; CruiseKube next under its license's evaluation terms; the GPU and platform power pieces in the Lambda
kit; EAR and the processor power managers on bare metal when a machine with power registers is rented.

Built so far: **Goldilocks** (register row 80; `scripts/kind_addons_goldilocks.sh`, workflow `kind-goldilocks`,
`docs/GOLDILOCKS_PREREGISTRATION.md`), run three times on the card version (`results/live/V5_GOLDILOCKS.md`): the
service faster in all three of our runs, machines the same, 1.9% to 2.6% more energy on the declared model, every row
shown. **CruiseKube** (register row 81; `scripts/kind_addons_cruisekube.sh`, workflow `kind-cruisekube`,
`docs/CRUISEKUBE_PREREGISTRATION.md`), beside KEDA's HTTP add-on, since CruiseKube leaves alone a service whose
autoscaler scales on CPU: a trial run proves the wiring and records its chart's SHA-256 for the pin, then three
counted runs.

**As muscles in the organisms** (the founder's order of 12 October: "expand my organisms"): each of the nine is also a
muscle of the catalog (`realms/catalog_v5.csv`, ids 2172 to 2181), modelled on the plant its knob turns and placed in the
spine family that knob belongs to, so each is in all four realms, the four stacked and the whole tower: Kepler's energy
reading driving a pool's target, Climatik's inference power cap, EAR's CPU frequency policy and global energy budget,
CruiseKube's and Goldilocks's request rightsizing, the Kubernetes Power Manager's core profiles, PEAKS's power-aware
placement, the learned GPU power cap and NVIDIA's platform power budget. A model of a knob is not the project itself
(class S); the project's own benchmark is the live test of it.

## 4. Who owns Omni-Compass, and on what terms it is seen

- **The copyright in Omni-Compass belongs to Dubra Software Inc. / The Omni-Compass LLC.** Contributions are accepted only on the terms of
  `.github/CONTRIBUTING.md`, which assign their rights to Dubra Software Inc. / The Omni-Compass LLC.
- **The source is visible under the Omni-Compass Evaluation License (`LICENSE`): evaluation and Simulation use only.**
  It is not an open-source license. Any commercial use, commercialization, monetization, production use,
  redistribution or hosted service requires a signed, paid Omni-Compass Enterprise License. Seeing the source grants
  no right beyond the Evaluation License.
- **Two licenses from one owner.** The owner of a copyright may grant it under more than one license at once (an
  evaluation license to everyone, a paid enterprise license to a customer), may set the terms of each new version, and
  may assign the copyright. Copies already received keep the terms they were received under.
- **All patents, copyrights and trademarks covering the Omni-Compass engine, its mathematics and its software have been
  filed in the United States by Dubra Software Inc. / The Omni-Compass LLC.**
- This section states how the repository is licensed; the license texts (`LICENSE`, `NOTICE`, `DISCLOSURES.md`) govern.

## 5. What is shown, and what is still to be shown

What is shown, and by which kind of evidence, is set out receipt by receipt in `docs/THE_RECEIPTS.md`. In one line:
on real software (class L), Omni-Compass on top of native has given faster service and more work inside the response
line on the same machines, and memory back on databases at the same service, with no row LOSS in all three runs on the
real stacks; on our own models (class S) no muscle alone is behind native.

**The decisive receipt still to be produced is a physical one (class P): the chip's own energy meter on a real GPU,
native against Omni-Compass on top, on the same clock and with the same membership as the Kubernetes runs.** Every
earlier card result ran on a controller since replaced and is obsolete. The run is the founder's, on rented cards, at
one exact commit, after the CPU side is done (`docs/GPU_RUN_GUIDE.md`, `docs/GPU_PREREGISTRATION.md`). Until it lands,
no energy saving on real machines is claimed. The seat is claimed by design and by the receipts on this page; it is held
when the receipts cover it.

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
