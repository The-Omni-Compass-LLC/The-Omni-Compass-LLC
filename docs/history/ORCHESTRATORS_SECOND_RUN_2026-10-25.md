# The orchestrators on the same organisms, with the same injection

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Our own models (evidence class S), never a benchmark result. The record of `tools/orchestrators_arm.py`, preregistered in `docs/ORCHESTRATORS_PREREGISTRATION.md` before its first run; 8 repetitions on every organism, repetition k seeded from the engine's jump generator (base 20261025), the same injection in every arm of it. Omni-Compass is the shipped Kubernetes governor of omni-v19 (`omni_controller/`) at its factory flags, the rig's own.

The founder's order of 25 October: "all the orchestrators to have the same injection ran through. Those orchestrators sit on the same organism. And there lies the third arm ... And of course then OmniCompass on top of that same stack."

## The three arms

| Arm | What runs on the organism |
|---|---|
| native | Kubernetes alone: its default scheduler places every pod, the service's autoscaler (HPA), and in the cloud the Cluster Autoscaler |
| the orchestrator | the same organism and the same work, every pod sent to the orchestrator the way its project documents it, its shipped rule deciding what goes in and where |
| Omni-Compass on top | the orchestrator's arm with Omni-Compass's governor on top; it writes only what it writes on a real cluster (the service's autoscaler, a machine's idle mark, the service pods' processor limit), never an orchestrator's own objects |

## The orchestrators

| Orchestrator | Its rule in the model, from its own release |
|---|---|
| the Kubernetes scheduler as shipped (the organism alone) | default scoring: least allocated (1), topology spread (2), taint toleration (3); ties at random (Kubernetes 1.35) |
| the Kubernetes scheduler's bin-packing profile | most allocated in place of least allocated, every other plugin as shipped (deploy/kind/binpack-scheduler.yaml) |
| Volcano v1.16.0 | enqueue gate at 1.2 times the room, jobs in DRF order, PodGroups of one; leastrequested and binpack cancel, the best machines tie, one taken at random (installer/volcano-development.yaml, v1.16.0) |
| Kueue v0.20.2 | one ClusterQueue, quota the workers' processor at install, BestEffortFIFO, a job admitted whole and its quota given back as pods finish, the service's pods admitted one by one; placed by the default scheduler (v0.20.2) |
| the KAI scheduler v0.18.6 | bin-packing on the processor, a plain Job's pods one by one, its default queue (schedulingshard_types.go, v0.18.6) |
| Koordinator 1.8.0 | the batch pods best effort on batch resources (60% of the machine less the service's use), held to 65% less the service's use, at the least processor weight; load-aware filter at 65% busy (1.8.0) |

## The organisms

Each organism carries one injection, from the benchmark named; each runs in both settings.

| Organism | Benchmark it carries | Window | Clients over the window |
|---|---|---:|---|
| steady | kubernetes steady | 900 s | 1 2 3 1 2 1 |
| wandering | kubernetes wandering | 2700 s | 1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1 |
| all_four | kubernetes all four | 2700 s | 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 |
| google_2011 | kubernetes google 2011 trace | 2592 s | 2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4 |
| climb | the founder's traffic rule (1 2 3 2 3 4 ...) | 1800 s | 1 2 3 2 3 4 3 4 5 4 5 6 5 6 7 6 7 8 |
| burst_1419 | the cloud's burst 1 4 1 6 1 9 | 1800 s | 1 4 1 6 1 9 |
| burst_1618 | the cloud's burst 1 6 1 8 1 6 | 1800 s | 1 6 1 8 1 6 |
| real_day | the cloud's real day (Google 2011) on 1 to 9 | 2592 s | 2 3 3 4 3 4 4 3 2 2 2 2 2 3 2 3 4 5 4 5 6 7 6 5 |
| fairness | kubernetes fairness (two services) | 900 s | 1 2 3 1 2 1 (two services) |
| faults | kubernetes faults | 900 s | 1 2 3 1 2 1 + the fault drill |
| batch | kubernetes batch (the stream; the service deployed, its clients at zero) | 1500 s | none (the batch stream alone) |
| one_body | the batch stream beside the service | 1800 s | 1 2 3 2 3 4 3 4 5 4 5 6 5 6 7 6 7 8 + the batch stream |

| Setting | The machines |
|---|---|
| on-site | the kind rig: six workers that are containers on one runner, each reporting the runner's 4 cores; the pods share the 3 cores the governor's own leaves; no cluster autoscaler |
| cloud | machines of 2 cores of their own (1.9 allocatable), the Cluster Autoscaler at its defaults, 2 to 9 machines, 90 s to boot |

## How to read a cell

Each cell is a paired reading by the one key: the word first, then the size of the change with the word's sign (GAIN +, LOSS −, power given +, STEADY =). Time waited, missed or failed that fell is a GAIN; work that rose is a GAIN; a resource spent that fell is a cut (GAIN) and one that rose is power given, never a loss. A change under 0.5% is STEADY. Beside each count, the detailed tables give the 95% interval over the repetitions.

## On-site (the kind rig): each orchestrator against Kubernetes alone

The words over every gauge of the organism (how many read GAIN, LOSS, power given, STEADY).

| Organism | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|
| steady | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| wandering | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| all_four | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| google_2011 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| climb | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| burst_1419 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| burst_1618 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| real_day | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| fairness | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| faults | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| batch | STEADY 6 | STEADY 6 | LOSS 2 · STEADY 4 | STEADY 6 | STEADY 6 |
| one_body | STEADY 10 | STEADY 10 | LOSS 3 · STEADY 7 | STEADY 10 | GAIN 4 · LOSS 3 · power given 1 · STEADY 2 |

## On-site (the kind rig): Omni-Compass on top of each orchestrator, against that orchestrator alone

| Organism | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| steady | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 |
| wandering | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 |
| all_four | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 |
| google_2011 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 |
| climb | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 |
| burst_1419 | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 |
| burst_1618 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 |
| real_day | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 |
| fairness | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 | GAIN 1 · STEADY 6 |
| faults | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 2 · STEADY 5 | GAIN 1 · STEADY 6 | GAIN 2 · STEADY 5 |
| batch | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 |
| one_body | GAIN 3 · LOSS 2 · STEADY 5 | GAIN 3 · LOSS 2 · STEADY 5 | GAIN 3 · LOSS 2 · STEADY 5 | GAIN 3 · LOSS 2 · STEADY 5 | GAIN 3 · LOSS 2 · STEADY 5 | GAIN 2 · STEADY 8 |

## The cloud: each orchestrator against Kubernetes alone

The words over every gauge of the organism (how many read GAIN, LOSS, power given, STEADY).

| Organism | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|
| steady | STEADY 7 | STEADY 7 | GAIN 2 · STEADY 5 | LOSS 1 · power given 1 · STEADY 5 | STEADY 7 |
| wandering | STEADY 7 | LOSS 2 · power given 1 · STEADY 4 | GAIN 2 · LOSS 1 · STEADY 4 | LOSS 4 · power given 1 · STEADY 2 | STEADY 7 |
| all_four | STEADY 7 | LOSS 1 · STEADY 6 | STEADY 7 | LOSS 4 · power given 1 · STEADY 2 | STEADY 7 |
| google_2011 | STEADY 7 | GAIN 2 · LOSS 2 · STEADY 3 | GAIN 2 · STEADY 5 | GAIN 2 · LOSS 2 · STEADY 3 | STEADY 7 |
| climb | STEADY 7 | LOSS 2 · power given 1 · STEADY 4 | GAIN 2 · STEADY 5 | LOSS 4 · power given 1 · STEADY 2 | STEADY 7 |
| burst_1419 | STEADY 7 | LOSS 4 · STEADY 3 | GAIN 2 · STEADY 5 | GAIN 1 · LOSS 4 · STEADY 2 | STEADY 7 |
| burst_1618 | STEADY 7 | LOSS 1 · STEADY 6 | GAIN 2 · STEADY 5 | LOSS 4 · STEADY 3 | LOSS 1 · STEADY 6 |
| real_day | STEADY 7 | GAIN 2 · LOSS 2 · STEADY 3 | GAIN 2 · STEADY 5 | GAIN 2 · LOSS 2 · STEADY 3 | STEADY 7 |
| fairness | STEADY 7 | LOSS 1 · STEADY 6 | LOSS 2 · power given 2 · STEADY 3 | LOSS 1 · power given 1 · STEADY 5 | STEADY 7 |
| faults | STEADY 7 | LOSS 4 · STEADY 3 | GAIN 2 · STEADY 5 | LOSS 4 · power given 1 · STEADY 2 | STEADY 7 |
| batch | power given 1 · STEADY 5 | GAIN 2 · power given 1 · STEADY 3 | GAIN 2 · LOSS 3 · STEADY 1 | GAIN 2 · LOSS 2 · power given 1 · STEADY 1 | GAIN 2 · LOSS 2 · STEADY 2 |
| one_body | GAIN 1 · LOSS 3 · power given 1 · STEADY 5 | GAIN 1 · LOSS 4 · power given 1 · STEADY 4 | GAIN 2 · LOSS 5 · STEADY 3 | GAIN 1 · LOSS 5 · power given 1 · STEADY 3 | GAIN 1 · LOSS 2 · STEADY 7 |

## The cloud: Omni-Compass on top of each orchestrator, against that orchestrator alone

| Organism | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| steady | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| wandering | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| all_four | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| google_2011 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| climb | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| burst_1419 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| burst_1618 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| real_day | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| fairness | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| faults | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| batch | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 |
| one_body | power given 1 · STEADY 9 | power given 1 · STEADY 9 | LOSS 2 · power given 1 · STEADY 7 | STEADY 10 | STEADY 10 | power given 1 · STEADY 9 |

## Every organism, gauge by gauge

### steady, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 207.8 | 207.8, STEADY =0.0% | 207.8, STEADY =0.0% | 207.8, STEADY =0.0% | 207.8, STEADY =0.0% | 207.8, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 8,996 | 8,996, STEADY =0.0% | 8,996, STEADY =0.0% | 8,996, STEADY =0.0% | 8,996, STEADY =0.0% | 8,996, STEADY =0.0% |
| machine-hours | 1.500 | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% |
| energy | 0.010 | 0.010, STEADY =0.0% | 0.010, STEADY =0.0% | 0.010, STEADY =0.0% | 0.010, STEADY =0.0% | 0.010, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +50.1% (+49.1% to +51.1%) | GAIN +50.1% (+49.1% to +51.1%) | GAIN +50.1% (+49.1% to +51.1%) | GAIN +50.1% (+49.1% to +51.1%) | GAIN +7.1% (+6.0% to +8.3%) | GAIN +50.1% (+49.1% to +51.1%) |
| minutes over the line (500 ms) | GAIN +25.0% (−63.7% to +13.7%) | GAIN +25.0% (−63.7% to +13.7%) | GAIN +25.0% (−63.7% to +13.7%) | GAIN +25.0% (−63.7% to +13.7%) | GAIN +25.0% (−63.7% to +13.7%) | GAIN +25.0% (−63.7% to +13.7%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 18.0, the Kubernetes scheduler's bin-packing profile 18.0, Volcano v1.16.0 19.5, Kueue v0.20.2 18.0, the KAI scheduler v0.18.6 15.0, Koordinator 1.8.0 17.8

### wandering, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 336.9 | 336.9, STEADY =0.0% | 336.9, STEADY =0.0% | 336.9, STEADY =0.0% | 336.9, STEADY =0.0% | 336.9, STEADY =0.0% |
| minutes over the line (500 ms) | 4.0 | 4.0, STEADY =0.0% | 4.0, STEADY =0.0% | 4.0, STEADY =0.0% | 4.0, STEADY =0.0% | 4.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 64,016 | 64,016, STEADY =0.0% | 64,016, STEADY =0.0% | 64,016, STEADY =0.0% | 64,016, STEADY =0.0% | 64,016, STEADY =0.0% |
| machine-hours | 4.500 | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% |
| energy | 0.039 | 0.039, STEADY =0.0% | 0.039, STEADY =0.0% | 0.039, STEADY =0.0% | 0.039, STEADY =0.0% | 0.039, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +24.8% (+23.7% to +25.9%) | GAIN +24.8% (+23.7% to +25.9%) | GAIN +24.8% (+23.7% to +25.9%) | GAIN +24.8% (+23.7% to +25.9%) | GAIN +3.2% (+2.3% to +4.1%) | GAIN +24.8% (+23.7% to +25.9%) |
| minutes over the line (500 ms) | GAIN +6.2% (−15.9% to +3.4%) | GAIN +6.2% (−15.9% to +3.4%) | GAIN +6.2% (−15.9% to +3.4%) | GAIN +6.2% (−15.9% to +3.4%) | GAIN +3.1% (−10.5% to +4.3%) | GAIN +6.2% (−15.9% to +3.4%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 30.6, the Kubernetes scheduler's bin-packing profile 30.6, Volcano v1.16.0 34.1, Kueue v0.20.2 30.6, the KAI scheduler v0.18.6 21.0, Koordinator 1.8.0 29.0

### all_four, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 472.5 | 472.5, STEADY =0.0% | 472.5, STEADY =0.0% | 472.5, STEADY =0.0% | 472.5, STEADY =0.0% | 472.5, STEADY =0.0% |
| minutes over the line (500 ms) | 4.4 | 4.4, STEADY =0.0% | 4.4, STEADY =0.0% | 4.4, STEADY =0.0% | 4.4, STEADY =0.0% | 4.4, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 69,192 | 69,192, STEADY =0.0% | 69,192, STEADY =0.0% | 69,192, STEADY =0.0% | 69,192, STEADY =0.0% | 69,192, STEADY =0.0% |
| machine-hours | 4.500 | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% |
| energy | 0.040 | 0.040, STEADY =0.0% | 0.040, STEADY =0.0% | 0.040, STEADY =0.0% | 0.040, STEADY =0.0% | 0.040, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +14.8% (+13.6% to +16.2%) | GAIN +14.8% (+13.6% to +16.2%) | GAIN +14.8% (+13.6% to +16.2%) | GAIN +14.8% (+13.6% to +16.2%) | GAIN +2.3% (+1.9% to +2.7%) | GAIN +14.8% (+13.6% to +16.2%) |
| minutes over the line (500 ms) | GAIN +5.7% (−14.6% to +3.1%) | GAIN +5.7% (−14.6% to +3.1%) | GAIN +5.7% (−14.6% to +3.1%) | GAIN +5.7% (−14.6% to +3.1%) | GAIN +2.9% (−9.6% to +3.9%) | GAIN +5.7% (−14.6% to +3.1%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 18.4, the Kubernetes scheduler's bin-packing profile 18.4, Volcano v1.16.0 19.9, Kueue v0.20.2 18.4, the KAI scheduler v0.18.6 18.6, Koordinator 1.8.0 17.4

### google_2011, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 212.2 | 212.2, STEADY =0.0% | 212.2, STEADY =0.0% | 212.2, STEADY =0.0% | 212.2, STEADY =0.0% | 212.2, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 10 | 10, STEADY =0.0% | 10, STEADY =0.0% | 10, STEADY =0.0% | 10, STEADY =0.0% | 10, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 50,646 | 50,646, STEADY =0.0% | 50,646, STEADY =0.0% | 50,646, STEADY =0.0% | 50,646, STEADY =0.0% | 50,646, STEADY =0.0% |
| machine-hours | 4.325 | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% |
| energy | 0.034 | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +43.0% (+42.3% to +43.6%) | GAIN +43.0% (+42.3% to +43.6%) | GAIN +43.0% (+42.3% to +43.6%) | GAIN +43.0% (+42.3% to +43.6%) | GAIN +1.2% (+0.9% to +1.6%) | GAIN +43.0% (+42.3% to +43.6%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | GAIN +100.0% (+26.5% to +173.5%) | GAIN +100.0% (+26.5% to +173.5%) | GAIN +100.0% (+26.5% to +173.5%) | GAIN +100.0% (+26.5% to +173.5%) | GAIN +100.0% (+26.5% to +173.5%) | GAIN +100.0% (+26.5% to +173.5%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 34.1, the Kubernetes scheduler's bin-packing profile 34.1, Volcano v1.16.0 39.4, Kueue v0.20.2 34.1, the KAI scheduler v0.18.6 20.1, Koordinator 1.8.0 32.6

### climb, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 423.4 | 423.4, STEADY =0.0% | 423.4, STEADY =0.0% | 423.4, STEADY =0.0% | 423.4, STEADY =0.0% | 423.4, STEADY =0.0% |
| minutes over the line (500 ms) | 3.2 | 3.2, STEADY =0.0% | 3.2, STEADY =0.0% | 3.2, STEADY =0.0% | 3.2, STEADY =0.0% | 3.2, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 48,567 | 48,567, STEADY =0.0% | 48,567, STEADY =0.0% | 48,567, STEADY =0.0% | 48,567, STEADY =0.0% | 48,567, STEADY =0.0% |
| machine-hours | 3.000 | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% |
| energy | 0.027 | 0.027, STEADY =0.0% | 0.027, STEADY =0.0% | 0.027, STEADY =0.0% | 0.027, STEADY =0.0% | 0.027, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +19.4% (+17.5% to +21.4%) | GAIN +19.4% (+17.5% to +21.4%) | GAIN +19.4% (+17.5% to +21.4%) | GAIN +19.4% (+17.5% to +21.4%) | GAIN +5.9% (+4.8% to +7.1%) | GAIN +19.4% (+17.5% to +21.4%) |
| minutes over the line (500 ms) | GAIN +7.7% (−19.6% to +4.2%) | GAIN +7.7% (−19.6% to +4.2%) | GAIN +7.7% (−19.6% to +4.2%) | GAIN +7.7% (−19.6% to +4.2%) | GAIN +3.9% (−12.9% to +5.2%) | GAIN +7.7% (−19.6% to +4.2%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 15.1, the Kubernetes scheduler's bin-packing profile 15.1, Volcano v1.16.0 17.4, Kueue v0.20.2 15.1, the KAI scheduler v0.18.6 16.1, Koordinator 1.8.0 14.2

### burst_1419, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 10,000.0 | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% |
| minutes over the line (500 ms) | 6.0 | 6.0, STEADY =0.0% | 6.0, STEADY =0.0% | 6.0, STEADY =0.0% | 6.0, STEADY =0.0% | 6.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 736 | 736, STEADY =0.0% | 736, STEADY =0.0% | 736, STEADY =0.0% | 736, STEADY =0.0% | 736, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 38,406 | 38,406, STEADY =0.0% | 38,406, STEADY =0.0% | 38,406, STEADY =0.0% | 38,406, STEADY =0.0% | 38,406, STEADY =0.0% |
| machine-hours | 3.000 | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% |
| energy | 0.025 | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | GAIN +2.1% (−7.0% to +2.8%) | GAIN +2.1% (−7.0% to +2.8%) | GAIN +2.1% (−7.0% to +2.8%) | GAIN +2.1% (−7.0% to +2.8%) | GAIN +2.1% (−7.0% to +2.8%) | GAIN +2.1% (−7.0% to +2.8%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 20.4, the Kubernetes scheduler's bin-packing profile 20.4, Volcano v1.16.0 22.4, Kueue v0.20.2 20.4, the KAI scheduler v0.18.6 13.8, Koordinator 1.8.0 19.0

### burst_1618, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 1,116.6 | 1,116.6, STEADY =0.0% | 1,116.6, STEADY =0.0% | 1,116.6, STEADY =0.0% | 1,116.6, STEADY =0.0% | 1,116.6, STEADY =0.0% |
| minutes over the line (500 ms) | 7.0 | 7.0, STEADY =0.0% | 7.0, STEADY =0.0% | 7.0, STEADY =0.0% | 7.0, STEADY =0.0% | 7.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 41,355 | 41,355, STEADY =0.0% | 41,355, STEADY =0.0% | 41,355, STEADY =0.0% | 41,355, STEADY =0.0% | 41,355, STEADY =0.0% |
| machine-hours | 3.000 | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% |
| energy | 0.025 | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +19.4% (+17.1% to +21.7%) | GAIN +19.4% (+17.1% to +21.7%) | GAIN +19.4% (+17.1% to +21.7%) | GAIN +19.4% (+17.1% to +21.7%) | GAIN +14.1% (+12.1% to +16.0%) | GAIN +19.4% (+17.1% to +21.7%) |
| minutes over the line (500 ms) | GAIN +17.9% (+12.3% to +23.4%) | GAIN +17.9% (+12.3% to +23.4%) | GAIN +17.9% (+12.3% to +23.4%) | GAIN +17.9% (+12.3% to +23.4%) | GAIN +17.9% (+12.3% to +23.4%) | GAIN +17.9% (+12.3% to +23.4%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 20.4, the Kubernetes scheduler's bin-packing profile 20.4, Volcano v1.16.0 20.8, Kueue v0.20.2 20.4, the KAI scheduler v0.18.6 14.5, Koordinator 1.8.0 19.0

### real_day, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 237.5 | 237.5, STEADY =0.0% | 237.5, STEADY =0.0% | 237.5, STEADY =0.0% | 237.5, STEADY =0.0% | 237.5, STEADY =0.0% |
| minutes over the line (500 ms) | 1.1 | 1.1, STEADY =0.0% | 1.1, STEADY =0.0% | 1.1, STEADY =0.0% | 1.1, STEADY =0.0% | 1.1, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 8 | 8, STEADY =0.0% | 8, STEADY =0.0% | 8, STEADY =0.0% | 8, STEADY =0.0% | 8, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 55,726 | 55,726, STEADY =0.0% | 55,726, STEADY =0.0% | 55,726, STEADY =0.0% | 55,726, STEADY =0.0% | 55,726, STEADY =0.0% |
| machine-hours | 4.325 | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% |
| energy | 0.036 | 0.036, STEADY =0.0% | 0.036, STEADY =0.0% | 0.036, STEADY =0.0% | 0.036, STEADY =0.0% | 0.036, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +37.5% (+36.7% to +38.3%) | GAIN +37.5% (+36.7% to +38.3%) | GAIN +37.5% (+36.7% to +38.3%) | GAIN +37.5% (+36.7% to +38.3%) | GAIN +1.7% (+1.4% to +2.0%) | GAIN +37.5% (+36.7% to +38.3%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | GAIN +100.0% (+40.3% to +159.7%) | GAIN +100.0% (+40.3% to +159.7%) | GAIN +100.0% (+40.3% to +159.7%) | GAIN +100.0% (+40.3% to +159.7%) | GAIN +100.0% (+40.3% to +159.7%) | GAIN +100.0% (+40.3% to +159.7%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) | STEADY =0.0% (+0.0% to +0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) | STEADY =0.0% (±0.0% to +0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 36.8, the Kubernetes scheduler's bin-packing profile 36.8, Volcano v1.16.0 46.0, Kueue v0.20.2 36.8, the KAI scheduler v0.18.6 21.8, Koordinator 1.8.0 34.8

### fairness, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 301.6 | 301.6, STEADY =0.0% | 301.6, STEADY =0.0% | 301.6, STEADY =0.0% | 301.6, STEADY =0.0% | 301.6, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 18,003 | 18,003, STEADY =0.0% | 18,003, STEADY =0.0% | 18,003, STEADY =0.0% | 18,003, STEADY =0.0% | 18,003, STEADY =0.0% |
| machine-hours | 1.500 | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% |
| energy | 0.012 | 0.012, STEADY =0.0% | 0.012, STEADY =0.0% | 0.012, STEADY =0.0% | 0.012, STEADY =0.0% | 0.012, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +11.9% (+10.4% to +13.3%) | GAIN +11.9% (+10.4% to +13.3%) | GAIN +11.9% (+10.4% to +13.3%) | GAIN +11.9% (+10.4% to +13.3%) | GAIN +3.1% (+2.4% to +3.7%) | GAIN +11.9% (+10.4% to +13.3%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 25.0, the Kubernetes scheduler's bin-packing profile 19.6, Volcano v1.16.0 25.8, Kueue v0.20.2 25.0, the KAI scheduler v0.18.6 3.0, Koordinator 1.8.0 22.4

### faults, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 7,612.4 | 7,612.4, STEADY =0.0% | 7,612.4, STEADY =0.0% | 7,612.4, STEADY =0.0% | 7,612.4, STEADY =0.0% | 7,612.4, STEADY =0.0% |
| minutes over the line (500 ms) | 4.0 | 4.0, STEADY =0.0% | 4.0, STEADY =0.0% | 4.0, STEADY =0.0% | 4.0, STEADY =0.0% | 4.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 32 | 32, STEADY =0.0% | 32, STEADY =0.0% | 32, STEADY =0.0% | 32, STEADY =0.0% | 32, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 13,320 | 13,320, STEADY =0.0% | 13,320, STEADY =0.0% | 13,320, STEADY =0.0% | 13,320, STEADY =0.0% | 13,320, STEADY =0.0% |
| machine-hours | 1.467 | 1.467, STEADY =0.0% | 1.467, STEADY =0.0% | 1.467, STEADY =0.0% | 1.467, STEADY =0.0% | 1.467, STEADY =0.0% |
| energy | 0.011 | 0.011, STEADY =0.0% | 0.011, STEADY =0.0% | 0.011, STEADY =0.0% | 0.011, STEADY =0.0% | 0.011, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +0.8% (+0.7% to +0.9%) | GAIN +0.8% (+0.7% to +0.9%) | GAIN +0.8% (+0.7% to +0.9%) | GAIN +0.8% (+0.7% to +0.9%) | STEADY =0.0% (±0.0% to ±0.0%) | GAIN +0.8% (+0.7% to +0.9%) |
| minutes over the line (500 ms) | GAIN +6.2% (−15.9% to +3.4%) | GAIN +6.2% (−15.9% to +3.4%) | GAIN +6.2% (−15.9% to +3.4%) | GAIN +6.2% (−15.9% to +3.4%) | GAIN +6.2% (−15.9% to +3.4%) | GAIN +6.2% (−15.9% to +3.4%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 16.1, the Kubernetes scheduler's bin-packing profile 16.1, Volcano v1.16.0 21.5, Kueue v0.20.2 16.1, the KAI scheduler v0.18.6 17.8, Koordinator 1.8.0 14.9

### batch, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| a job's turnaround | 69.0 | 69.0, STEADY =0.0% | 69.0, STEADY =0.0% | 74.0, LOSS −7.2% | 69.0, STEADY =0.0% | 69.0, STEADY =0.0% |
| the stream's makespan (first job in to last job done) | 747.5 | 747.5, STEADY =0.0% | 747.5, STEADY =0.0% | 752.5, LOSS −0.7% | 747.5, STEADY =0.0% | 747.5, STEADY =0.0% |
| batch pods done | 240 | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% |
| machine-hours | 2.500 | 2.500, STEADY =0.0% | 2.500, STEADY =0.0% | 2.500, STEADY =0.0% | 2.500, STEADY =0.0% | 2.500, STEADY =0.0% |
| energy | 0.022 | 0.022, STEADY =0.0% | 0.022, STEADY =0.0% | 0.022, STEADY =0.0% | 0.022, STEADY =0.0% | 0.022, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| a job's turnaround | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| the stream's makespan (first job in to last job done) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| batch pods done | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 6.5, the Kubernetes scheduler's bin-packing profile 6.8, Volcano v1.16.0 6.6, Kueue v0.20.2 6.5, the KAI scheduler v0.18.6 3.5, Koordinator 1.8.0 6.8

### one_body, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 10,000.0 | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 412.3, GAIN +95.9% |
| minutes over the line (500 ms) | 16.2 | 16.2, STEADY =0.0% | 16.2, STEADY =0.0% | 16.2, STEADY =0.0% | 16.2, STEADY =0.0% | 3.2, GAIN +80.0% |
| requests failed (unanswered in 10 s) | 7,928 | 7,928, STEADY =0.0% | 7,928, STEADY =0.0% | 8,155, LOSS −2.9% | 7,928, STEADY =0.0% | 0, GAIN +100.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 199.8, LOSS −100.0% |
| a job's turnaround | 141.0 | 141.0, STEADY =0.0% | 141.0, STEADY =0.0% | 141.9, LOSS −0.6% | 141.0, STEADY =0.0% | 316.0, LOSS −124.0% |
| the stream's makespan (first job in to last job done) | 801.2 | 801.2, STEADY =0.0% | 801.2, STEADY =0.0% | 803.1, STEADY =0.2% | 801.2, STEADY =0.0% | 1,175.6, LOSS −46.7% |
| batch pods done | 240 | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% |
| requests served | 40,620 | 40,620, STEADY =0.0% | 40,620, STEADY =0.0% | 40,394, LOSS −0.6% | 40,620, STEADY =0.0% | 48,548, GAIN +19.5% |
| machine-hours | 3.000 | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% |
| energy | 0.034 | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% | 0.034, STEADY =0.1% | 0.034, STEADY =0.0% | 0.036, power given +5.5% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | GAIN +19.2% (+16.8% to +21.7%) |
| minutes over the line (500 ms) | GAIN +0.8% (−2.6% to +1.1%) | GAIN +0.8% (−2.6% to +1.1%) | GAIN +0.8% (−2.6% to +1.1%) | GAIN +0.8% (−2.6% to +1.1%) | GAIN +0.8% (−2.6% to +1.1%) | GAIN +3.9% (−12.9% to +5.2%) |
| requests failed (unanswered in 10 s) | GAIN +6.5% (+4.5% to +8.6%) | GAIN +6.5% (+4.5% to +8.6%) | GAIN +6.5% (+4.5% to +8.6%) | GAIN +9.2% (+8.1% to +10.3%) | GAIN +6.5% (+4.5% to +8.6%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| a job's turnaround | LOSS −9.3% (−6.6% to −11.9%) | LOSS −9.3% (−6.6% to −11.9%) | LOSS −9.3% (−6.6% to −11.9%) | LOSS −12.7% (−10.9% to −14.6%) | LOSS −9.3% (−6.6% to −12.1%) | STEADY =0.0% (±0.0% to ±0.0%) |
| the stream's makespan (first job in to last job done) | LOSS −2.0% (−1.4% to −2.7%) | LOSS −2.0% (−1.4% to −2.7%) | LOSS −2.0% (−1.4% to −2.7%) | LOSS −2.8% (−2.4% to −3.2%) | LOSS −2.0% (−1.4% to −2.7%) | STEADY =0.0% (±0.0% to ±0.0%) |
| batch pods done | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | GAIN +1.3% (+0.9% to +1.7%) | GAIN +1.3% (+0.9% to +1.7%) | GAIN +1.3% (+0.9% to +1.7%) | GAIN +1.9% (+1.6% to +2.1%) | GAIN +1.3% (+0.9% to +1.7%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.3% (+0.2% to +0.4%) | STEADY =0.3% (+0.2% to +0.4%) | STEADY =0.3% (+0.2% to +0.4%) | STEADY =0.4% (+0.3% to +0.4%) | STEADY =0.3% (+0.2% to +0.4%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 44.1, the Kubernetes scheduler's bin-packing profile 43.6, Volcano v1.16.0 44.2, Kueue v0.20.2 60.9, the KAI scheduler v0.18.6 25.1, Koordinator 1.8.0 19.2

### steady, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 202.1 | 202.1, STEADY =0.0% | 202.6, STEADY =0.2% | 202.1, STEADY =0.0% | 216.1, LOSS −6.9% | 202.1, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 8,992 | 8,992, STEADY =0.0% | 8,992, STEADY =0.0% | 8,992, STEADY =0.0% | 8,992, STEADY =0.0% | 8,992, STEADY =0.0% |
| machine-hours | 0.566 | 0.566, STEADY =0.0% | 0.566, STEADY =0.0% | 0.500, GAIN +11.6% | 0.566, STEADY =0.0% | 0.566, STEADY =0.0% |
| energy | 0.041 | 0.041, STEADY =0.0% | 0.041, STEADY =0.2% | 0.036, GAIN +11.7% | 0.044, power given +6.7% | 0.041, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.4, the Kubernetes scheduler's bin-packing profile 1.4, Volcano v1.16.0 1.4, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 1.4, Koordinator 1.8.0 1.4

### wandering, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 202.0 | 202.0, STEADY =0.0% | 222.6, LOSS −10.2% | 205.0, LOSS −1.5% | 9,532.2, LOSS −4618.2% | 202.0, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.5, LOSS −50.0% | 1.0, STEADY =0.0% | 10.9, LOSS −987.5% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 377, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 64,156 | 64,156, STEADY =0.0% | 64,156, STEADY =0.0% | 64,156, STEADY =0.0% | 63,779, LOSS −0.6% | 64,156, STEADY =0.0% |
| machine-hours | 1.831 | 1.831, STEADY =0.0% | 1.831, STEADY =0.0% | 1.500, GAIN +18.1% | 1.831, STEADY =0.0% | 1.831, STEADY =0.0% |
| energy | 0.153 | 0.153, STEADY =0.0% | 0.159, power given +3.8% | 0.133, GAIN +13.3% | 0.164, power given +7.2% | 0.153, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 1.5, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 10.4, Koordinator 1.8.0 1.0

### all_four, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 208.3 | 208.3, STEADY =0.0% | 212.0, LOSS −1.7% | 208.3, STEADY =0.0% | 10,000.0, LOSS −4700.0% | 208.3, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 14.1, LOSS −1312.5% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 875, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 69,069 | 69,069, STEADY =0.0% | 69,069, STEADY =0.0% | 69,069, STEADY =0.0% | 68,194, LOSS −1.3% | 69,069, STEADY =0.0% |
| machine-hours | 1.500 | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% |
| energy | 0.136 | 0.136, STEADY =0.0% | 0.136, STEADY =0.1% | 0.136, STEADY =0.0% | 0.138, power given +1.1% | 0.136, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 1.0, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 13.9, Koordinator 1.8.0 1.0

### google_2011, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 196.5 | 196.5, STEADY =0.0% | 218.8, LOSS −11.4% | 196.5, STEADY =0.0% | 262.0, LOSS −33.3% | 196.6, STEADY =0.1% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.2, LOSS −25.0% | 1.0, STEADY =0.0% | 2.0, LOSS −100.0% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 10 | 10, STEADY =0.0% | 10, STEADY =0.0% | 10, STEADY =0.0% | 10, STEADY =0.0% | 10, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 50,681 | 50,681, STEADY =0.0% | 50,681, STEADY =0.0% | 50,681, STEADY =0.0% | 50,681, STEADY =0.0% | 50,681, STEADY =0.0% |
| machine-hours | 2.101 | 2.101, STEADY =0.0% | 2.018, GAIN +4.0% | 1.442, GAIN +31.4% | 1.939, GAIN +7.7% | 2.101, STEADY =0.0% |
| energy | 0.176 | 0.176, STEADY =0.0% | 0.168, GAIN +4.4% | 0.120, GAIN +31.6% | 0.161, GAIN +8.5% | 0.176, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 2.0, the Kubernetes scheduler's bin-packing profile 2.0, Volcano v1.16.0 2.1, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 2.9, Koordinator 1.8.0 2.0

### climb, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 213.0 | 213.0, STEADY =0.0% | 245.9, LOSS −15.4% | 213.3, STEADY =0.1% | 5,068.5, LOSS −2279.6% | 213.0, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.2, LOSS −25.0% | 1.0, STEADY =0.0% | 9.8, LOSS −875.0% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 291, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 48,619 | 48,619, STEADY =0.0% | 48,619, STEADY =0.0% | 48,619, STEADY =0.0% | 47,911, LOSS −1.5% | 48,619, STEADY =0.0% |
| machine-hours | 1.375 | 1.375, STEADY =0.0% | 1.375, STEADY =0.0% | 1.000, GAIN +27.3% | 1.375, STEADY =0.0% | 1.375, STEADY =0.0% |
| energy | 0.125 | 0.125, STEADY =0.0% | 0.126, power given +1.4% | 0.093, GAIN +25.8% | 0.127, power given +1.7% | 0.125, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.1, the Kubernetes scheduler's bin-packing profile 1.1, Volcano v1.16.0 1.4, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 9.5, Koordinator 1.8.0 1.1

### burst_1419, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 242.2 | 242.2, STEADY =0.0% | 2,712.7, LOSS −1020.0% | 242.2, STEADY =0.0% | 10,000.0, LOSS −4028.6% | 242.2, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 2.8, LOSS −175.0% | 1.0, STEADY =0.0% | 8.5, LOSS −750.0% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 196, LOSS −100.0% | 0, STEADY =0.0% | 3,316, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 39,606 | 39,606, STEADY =0.0% | 39,287, LOSS −0.8% | 39,606, STEADY =0.0% | 35,873, LOSS −9.4% | 39,606, STEADY =0.0% |
| machine-hours | 1.331 | 1.331, STEADY =0.0% | 1.331, STEADY =0.0% | 1.000, GAIN +24.8% | 1.331, STEADY =0.0% | 1.331, STEADY =0.0% |
| energy | 0.114 | 0.114, STEADY =0.0% | 0.113, STEADY =0.2% | 0.087, GAIN +23.9% | 0.113, GAIN +0.8% | 0.114, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 2.8, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 8.4, Koordinator 1.8.0 1.0

### burst_1618, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 228.5 | 228.5, STEADY =0.0% | 254.7, LOSS −11.4% | 228.5, STEADY =0.0% | 10,000.0, LOSS −4275.5% | 228.5, STEADY =0.0% |
| minutes over the line (500 ms) | 1.9 | 1.9, STEADY =0.0% | 1.9, STEADY =0.0% | 1.9, STEADY =0.0% | 12.6, LOSS −573.3% | 1.9, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 1,533, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.1, LOSS −100.0% |
| requests served | 41,424 | 41,424, STEADY =0.0% | 41,424, STEADY =0.0% | 41,424, STEADY =0.0% | 39,892, LOSS −3.7% | 41,424, STEADY =0.0% |
| machine-hours | 1.331 | 1.331, STEADY =0.0% | 1.331, STEADY =0.0% | 1.000, GAIN +24.8% | 1.331, STEADY =0.0% | 1.331, STEADY =0.0% |
| energy | 0.117 | 0.117, STEADY =0.0% | 0.117, STEADY =0.1% | 0.088, GAIN +25.1% | 0.117, STEADY =0.3% | 0.117, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.9, the Kubernetes scheduler's bin-packing profile 1.9, Volcano v1.16.0 1.9, Kueue v0.20.2 1.9, the KAI scheduler v0.18.6 12.4, Koordinator 1.8.0 1.9

### real_day, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 199.7 | 199.7, STEADY =0.0% | 424.8, LOSS −112.7% | 199.7, STEADY =0.0% | 951.4, LOSS −376.3% | 199.8, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 2.1, LOSS −112.5% | 1.0, STEADY =0.0% | 4.2, LOSS −325.0% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 7 | 7, STEADY =0.0% | 7, STEADY =0.0% | 7, STEADY =0.0% | 7, STEADY =0.0% | 7, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 55,766 | 55,766, STEADY =0.0% | 55,766, STEADY =0.0% | 55,766, STEADY =0.0% | 55,766, STEADY =0.0% | 55,766, STEADY =0.0% |
| machine-hours | 2.101 | 2.101, STEADY =0.0% | 2.000, GAIN +4.8% | 1.442, GAIN +31.4% | 1.939, GAIN +7.7% | 2.101, STEADY =0.0% |
| energy | 0.181 | 0.181, STEADY =0.0% | 0.171, GAIN +5.7% | 0.124, GAIN +31.6% | 0.165, GAIN +9.0% | 0.181, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 2.0, the Kubernetes scheduler's bin-packing profile 2.0, Volcano v1.16.0 3.1, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 5.2, Koordinator 1.8.0 2.0

### fairness, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 223.9 | 223.9, STEADY =0.0% | 230.0, LOSS −2.7% | 226.9, LOSS −1.3% | 261.9, LOSS −17.0% | 223.9, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 2.4 | 2.4, STEADY =0.0% | 2.4, STEADY =0.0% | 3.2, LOSS −33.3% | 2.4, STEADY =0.0% | 2.4, STEADY =0.0% |
| requests served | 18,000 | 18,000, STEADY =0.0% | 18,000, STEADY =0.0% | 18,000, STEADY =0.0% | 18,000, STEADY =0.0% | 18,000, STEADY =0.0% |
| machine-hours | 0.773 | 0.773, STEADY =0.0% | 0.773, STEADY =0.0% | 0.797, power given +3.1% | 0.773, STEADY =0.0% | 0.773, STEADY =0.0% |
| energy | 0.062 | 0.062, STEADY =0.0% | 0.062, STEADY =0.3% | 0.064, power given +3.2% | 0.063, power given +2.3% | 0.062, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 7.5, the Kubernetes scheduler's bin-packing profile 7.5, Volcano v1.16.0 7.5, Kueue v0.20.2 7.0, the KAI scheduler v0.18.6 7.5, Koordinator 1.8.0 7.5

### faults, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 8,633.8 | 8,633.8, STEADY =0.0% | 9,910.2, LOSS −14.8% | 8,633.8, STEADY =0.0% | 10,000.0, LOSS −15.8% | 8,633.8, STEADY =0.0% |
| minutes over the line (500 ms) | 3.9 | 3.9, STEADY =0.0% | 4.0, LOSS −3.2% | 3.9, STEADY =0.0% | 4.0, LOSS −3.2% | 3.9, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 126 | 126, STEADY =0.0% | 885, LOSS −599.9% | 126, STEADY =0.0% | 1,135, LOSS −797.6% | 126, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% | 0.0, STEADY =0.0% |
| requests served | 13,187 | 13,187, STEADY =0.0% | 12,428, LOSS −5.8% | 13,187, STEADY =0.0% | 12,178, LOSS −7.7% | 13,187, STEADY =0.0% |
| machine-hours | 0.492 | 0.492, STEADY =0.0% | 0.492, STEADY =0.0% | 0.467, GAIN +5.1% | 0.492, STEADY =0.0% | 0.492, STEADY =0.0% |
| energy | 0.041 | 0.041, STEADY =0.0% | 0.041, STEADY =0.4% | 0.039, GAIN +4.2% | 0.041, power given +0.5% | 0.041, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 6.0, the Kubernetes scheduler's bin-packing profile 6.0, Volcano v1.16.0 6.1, Kueue v0.20.2 5.9, the KAI scheduler v0.18.6 6.1, Koordinator 1.8.0 6.0

### batch, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | 2.8 | 2.8, STEADY =0.0% | 2.6, GAIN +4.5% | 10.6, LOSS −284.5% | 2.7, GAIN +3.4% | 20.1, LOSS −630.3% |
| a job's turnaround | 39.1 | 39.1, STEADY =0.1% | 39.3, STEADY =0.4% | 50.0, LOSS −27.9% | 45.1, LOSS −15.2% | 53.0, LOSS −35.4% |
| the stream's makespan (first job in to last job done) | 725.0 | 725.0, STEADY =0.0% | 725.0, STEADY =0.0% | 730.0, LOSS −0.7% | 731.2, LOSS −0.9% | 726.9, STEADY =0.3% |
| batch pods done | 240 | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% |
| machine-hours | 3.497 | 3.497, STEADY =0.0% | 3.439, GAIN +1.7% | 2.272, GAIN +35.0% | 3.439, GAIN +1.7% | 3.406, GAIN +2.6% |
| energy | 0.258 | 0.260, power given +0.8% | 0.261, power given +1.0% | 0.174, GAIN +32.8% | 0.290, power given +12.3% | 0.256, GAIN +0.8% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| a job's turnaround | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| the stream's makespan (first job in to last job done) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| batch pods done | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 9.0, the Kubernetes scheduler's bin-packing profile 9.0, Volcano v1.16.0 9.4, Kueue v0.20.2 27.0, the KAI scheduler v0.18.6 9.8, Koordinator 1.8.0 11.0

### one_body, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 210.1 | 214.1, LOSS −1.9% | 245.0, LOSS −16.6% | 212.9, LOSS −1.3% | 426.8, LOSS −103.1% | 208.5, GAIN +0.7% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.2, LOSS −25.0% | 1.1, LOSS −12.5% | 2.6, LOSS −162.5% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 3.0 | 6.8, LOSS −129.5% | 5.1, LOSS −70.5% | 10.8, LOSS −263.2% | 8.0, LOSS −169.8% | 23.4, LOSS −687.0% |
| a job's turnaround | 39.1 | 40.9, LOSS −4.5% | 41.8, LOSS −6.9% | 49.0, LOSS −25.3% | 49.4, LOSS −26.2% | 53.0, LOSS −35.5% |
| the stream's makespan (first job in to last job done) | 725.0 | 725.0, STEADY =0.0% | 727.5, STEADY =0.3% | 730.0, LOSS −0.7% | 735.6, LOSS −1.5% | 725.0, STEADY =0.0% |
| batch pods done | 240 | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% |
| requests served | 48,615 | 48,615, STEADY =0.0% | 48,614, STEADY =0.0% | 48,615, STEADY =0.0% | 48,613, STEADY =0.0% | 48,615, STEADY =0.0% |
| machine-hours | 3.578 | 3.547, GAIN +0.9% | 3.550, GAIN +0.8% | 2.809, GAIN +21.5% | 3.557, GAIN +0.6% | 3.572, STEADY =0.2% |
| energy | 0.293 | 0.313, power given +6.9% | 0.307, power given +5.0% | 0.240, GAIN +17.9% | 0.348, power given +19.0% | 0.292, STEADY =0.4% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.1% (−0.1% to +0.0%) | STEADY =0.2% (+0.1% to +0.3%) | STEADY =0.0% (−0.0% to +0.0%) | STEADY =0.0% (−0.1% to +0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.1% (−0.2% to +0.1%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| a job's turnaround | STEADY =0.3% (−0.1% to +0.6%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −1.6% (−0.6% to −2.5%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.2% (−0.3% to +0.8%) |
| the stream's makespan (first job in to last job done) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −0.5% (−0.1% to −0.9%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.1% (−0.1% to +0.3%) |
| batch pods done | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | power given +1.5% (+1.2% to +1.8%) | power given +1.4% (+1.2% to +1.6%) | power given +0.9% (+0.6% to +1.3%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | power given +0.5% (+0.5% to +0.6%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 12.9, the Kubernetes scheduler's bin-packing profile 12.4, Volcano v1.16.0 17.0, Kueue v0.20.2 20.2, the KAI scheduler v0.18.6 15.6, Koordinator 1.8.0 14.1

## What the model leaves out

The processor alone is modelled (memory, disks and the network are not); a request's cost, the clients' rate and the pod start times are the rig's own calibration (the model gate's); every orchestrator's rule is written from its release and documentation, never from its code, and each is listed above with the file it was read from. The Gödel scheduler, KubeRay, Crane and the multi-cluster orchestrators (Karmada, Open Cluster Management, Armada) run on GitHub's machines four ways (`results/live/GOVERNORS.md`); their rules join this model once each one's shipped default is read from its release, and nothing is written for them here before that.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
