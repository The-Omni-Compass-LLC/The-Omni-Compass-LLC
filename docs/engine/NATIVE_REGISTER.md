# The native register: native's real settings, knob by knob

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's order of 17 October: native's numbers must be real measurements. The realms harness sets native from
"round engineering figures for the class of machine, not measurements of any product" (`realms/presets.py`, its own
first lines). This register puts, for every kind of knob the harness drives, native's setting in the harness beside
native's real setting, each with its source, and says what the difference means for the max. A row with no real source
reads **not yet measured**; no number is filled in by hand.

Sources are of three kinds: **R**, measured in this repository's own receipts on real systems (class L); **D**, the
system's own published default; **M**, to be read on the machine itself when it runs (the command is named).

## What the max's "native at its limit" rule assumes, against the real thing

`realms/compass_arm_v5.py` `native_at_limit` leaves a muscle native when its knob is a power limit or an admission gate,
or the capacity of a motion axis or a process loop: the harness's native already sits at the top of the knob's range.
Twenty-four of the live benchmark engine page's sixty muscles meet that rule.

| Knob | Native in the harness | Native in the real thing | Source | The rule against the real thing |
|---|---|---|---|---|
| GPU power limit | 1.0 (the top of its range) | Data-centre GPUs ship with the default limit at the rated board power: H100 SXM rated 700 W, the PCIe card 350 W; the driver's own default, minimum and maximum limits are read by `nvidia-smi -q -d POWER` | D (rated power); M (the Lambda run's snapshot records default, min and max limits, `docs/GPU_PREREGISTRATION.md`) | Holds where the default equals the maximum, as on data-centre cards: there is nothing above native to give, and the GPU benefit is the same work for less energy under a lower cap (the GPU preregistration's own design). To be confirmed by the Lambda snapshot |
| CPU frequency ceiling | 1.0 (full clock) | Linux sets each CPU's frequency ceiling to the hardware maximum unless an operator lowers it; the live values are in `/sys/devices/system/cpu/cpu*/cpufreq/` | D (kernel cpufreq); M (`docs/CPU_POWER_PREREGISTRATION.md`, the machine on the metal) | Holds by default. Room above native exists only where an operator capped the clock |
| Admission gate | open (nothing paced or turned away) | Kubernetes admits every request a service is sent unless the operator sets a limit; no default rate limit on a workload | D | Holds: an open gate has nothing above it. Pacing is a give-back, never a gain |
| Motion axis capacity | 1.0, the everyday profile, except presets with a peak (`s_peak` 1.15 to 1.25) | **not yet measured**: a robot's programmed speed, a vehicle's everyday acceleration and a ship's service speed are set by each operator below the drive's peak | none yet | The harness already gives the max a peak on the presets that have one; the others are an assumption until a real machine's setting is read |
| Process loop capacity | 1.0, the actuator's full range | **not yet measured** | none yet | An assumption |

## The settings the harness takes from a real default

| Knob | Native in the harness | Native in the real thing | Source | Match |
|---|---|---|---|---|
| HPA tolerance | 10% (`realms/plants.py` hpa) | 10% | D: Kubernetes HPA, "within a configurable tolerance, 0.1 by default" | yes |
| HPA scale-down window | 20 decisions of 15 s = 300 s (`stab_steps`) | 300 s | D: Kubernetes HPA v2 API, `scaleDown.stabilizationWindowSeconds` unset | yes |
| Cluster Autoscaler, time before an unneeded machine is removed | 40 decisions of 15 s = 10 min (`ca_unneeded_steps`) | 10 min | D: cluster-autoscaler `scale-down-unneeded-time` | yes |
| HPA target utilisation | 70% (every compute pool, `_CP target`) | Kubernetes has no default: the operator sets it. This repository's real runs: php-apache at **50%**, 1 to 10 replicas, 200m request, 500m limit | R: `docs/OMNI_V7.md`, `deploy/kind/`, `results/live/raw/addons-run-38725705826` | **no**: the harness's native packs pods tighter than the real runs' native did |
| Data-hall setpoint | 24 °C, limit 27 °C | ASHRAE TC 9.9 (5th edition, 2021) recommends an inlet of 18 to 27 °C for classes A1 to A4; the setpoint inside it is the operator's | D (the envelope) | the limit matches the recommended top; the setpoint is the operator's own choice |
| Battery reserve | 0.2 (microgrid, facility), 0.6 (UPS, held for an outage) | **not yet measured** | none yet | an assumption |
| Cloud machines | a pool of 2 to 80 | Azure, the real bill: the cloud's own autoscaler ran the light load on about 1.86 of 4 `Standard_D2s_v4` workers | R: `results/live/AKS_BILL.md` | the harness's pools are larger than the real Azure fleet; a machine to give back appears only under a heavier load |

## What the register says

1. **For power limits, CPU clocks and admission gates, the rule is right on real defaults.** Native already runs them at
   the top. The max cannot give more there; Omni-Compass's benefit on those knobs is the same work for less energy (a
   lower cap where the work does not feel it), which is the GPU and CPU preregistrations' own design, and the size of it
   is what the Lambda run and the machine on the metal will measure.
2. **One harness setting is off against the real runs: the HPA target.** The harness's native runs every pool at 70%;
   the repository's real Kubernetes native ran at 50%. A native with more spare capacity changes what the max can add
   and what it can hand back. Setting it from the receipts is a change to `realms/presets.py`, which sits inside the
   omni-v10 fingerprint: the next engine version, the model gate first, every realms result run again.
3. **Axes, loops and batteries are not yet measured.** Their rows stay assumptions, marked so, until a real machine's
   setting is read.
4. **The cloud bill needs a heavier load.** Azure's own autoscaler ran the real light load on fewer than two workers;
   a machine can be given back only where native runs several.

Sources: [Kubernetes, Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale),
[Kubernetes v1.31, HorizontalPodAutoscaler v2 API](https://v1-31.docs.kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2),
[OVHcloud, configuring the cluster autoscaler (the upstream defaults)](https://docs.ovhcloud.com/en/guides/public-cloud/containers-orchestration/managed-kubernetes/configure-cluster-autoscaler),
[Tom's Hardware, H100 SXM5 at 700 W](https://www.tomshardware.com/news/nvidia-hopper-h100-sxm5-pictured),
[RunPod, H100 power (SXM 700 W, PCIe 350 W)](https://runpod.io/ai-faq/what-is-the-power-consumption-of-the-nvidia-h100-gpu),
[Upsite, ASHRAE recommended envelope 18 to 27 °C](https://www.upsite.com/blog/what-is-the-difference-between-ashraes-recommended-and-allowable-data-center-environmental-limits-part-4/),
[Linux power management, cpufreq attributes](https://power-management-5e98d6.pages.code.europa.eu/episodes/PowerManagement-1-ImplementationAndRuntime/).
Each **M** row is read on the machine when its run starts; until then its number is the published default.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
