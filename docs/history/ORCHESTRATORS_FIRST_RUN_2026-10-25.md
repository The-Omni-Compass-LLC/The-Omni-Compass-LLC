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
| one_body | STEADY 10 | STEADY 10 | LOSS 4 · STEADY 6 | STEADY 10 | GAIN 4 · LOSS 3 · power given 1 · STEADY 2 |

## On-site (the kind rig): Omni-Compass on top of each orchestrator, against that orchestrator alone

| Organism | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| steady | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 |
| wandering | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 |
| all_four | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 |
| google_2011 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 |
| climb | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 |
| burst_1419 | LOSS 2 · STEADY 5 | LOSS 2 · STEADY 5 | LOSS 2 · STEADY 5 | LOSS 2 · STEADY 5 | LOSS 2 · STEADY 5 | LOSS 2 · STEADY 5 |
| burst_1618 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 |
| real_day | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 | LOSS 3 · STEADY 4 |
| fairness | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | LOSS 1 · STEADY 6 | STEADY 7 |
| faults | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | LOSS 2 · STEADY 5 | STEADY 7 |
| batch | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 |
| one_body | GAIN 2 · LOSS 3 · STEADY 5 | GAIN 2 · LOSS 3 · STEADY 5 | GAIN 2 · LOSS 3 · STEADY 5 | GAIN 2 · LOSS 3 · STEADY 5 | GAIN 2 · LOSS 3 · STEADY 5 | LOSS 1 · STEADY 9 |

## The cloud: each orchestrator against Kubernetes alone

The words over every gauge of the organism (how many read GAIN, LOSS, power given, STEADY).

| Organism | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|
| steady | STEADY 7 | LOSS 1 · power given 1 · STEADY 5 | GAIN 2 · LOSS 1 · STEADY 4 | LOSS 2 · power given 1 · STEADY 4 | STEADY 7 |
| wandering | STEADY 7 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 | GAIN 3 · LOSS 2 · STEADY 2 | GAIN 1 · LOSS 4 · power given 1 · STEADY 1 | STEADY 7 |
| all_four | STEADY 7 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 | GAIN 3 · LOSS 2 · STEADY 2 | GAIN 1 · LOSS 4 · power given 1 · STEADY 1 | STEADY 7 |
| google_2011 | STEADY 7 | GAIN 2 · LOSS 3 · STEADY 2 | GAIN 2 · STEADY 5 | GAIN 2 · LOSS 3 · STEADY 2 | STEADY 7 |
| climb | STEADY 7 | GAIN 1 · LOSS 2 · STEADY 4 | GAIN 3 · LOSS 2 · STEADY 2 | GAIN 1 · LOSS 4 · power given 1 · STEADY 1 | STEADY 7 |
| burst_1419 | STEADY 7 | GAIN 1 · LOSS 4 · STEADY 2 | GAIN 4 · LOSS 1 · STEADY 2 | GAIN 1 · LOSS 4 · power given 1 · STEADY 1 | GAIN 1 · LOSS 1 · power given 2 · STEADY 3 |
| burst_1618 | STEADY 7 | GAIN 1 · LOSS 2 · STEADY 4 | GAIN 3 · LOSS 2 · STEADY 2 | GAIN 1 · LOSS 4 · power given 1 · STEADY 1 | STEADY 7 |
| real_day | STEADY 7 | GAIN 2 · LOSS 3 · STEADY 2 | GAIN 2 · STEADY 5 | GAIN 2 · LOSS 3 · STEADY 2 | STEADY 7 |
| fairness | LOSS 1 · STEADY 6 | LOSS 2 · STEADY 5 | GAIN 2 · LOSS 3 · STEADY 2 | LOSS 2 · power given 1 · STEADY 4 | STEADY 7 |
| faults | STEADY 7 | LOSS 4 · power given 1 · STEADY 2 | GAIN 2 · LOSS 3 · STEADY 2 | LOSS 4 · power given 1 · STEADY 2 | STEADY 7 |
| batch | power given 1 · STEADY 5 | GAIN 4 · STEADY 2 | GAIN 1 · LOSS 3 · STEADY 2 | GAIN 3 · LOSS 2 · STEADY 1 | LOSS 2 · power given 2 · STEADY 2 |
| one_body | LOSS 4 · power given 2 · STEADY 4 | LOSS 4 · power given 2 · STEADY 4 | GAIN 2 · LOSS 5 · STEADY 3 | LOSS 5 · power given 2 · STEADY 3 | GAIN 2 · LOSS 2 · power given 2 · STEADY 4 |

## The cloud: Omni-Compass on top of each orchestrator, against that orchestrator alone

| Organism | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| steady | LOSS 1 · power given 1 · STEADY 5 | LOSS 1 · power given 1 · STEADY 5 | LOSS 1 · power given 1 · STEADY 5 | STEADY 7 | STEADY 7 | LOSS 1 · power given 1 · STEADY 5 |
| wandering | GAIN 1 · power given 1 · STEADY 5 | GAIN 1 · power given 1 · STEADY 5 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 | STEADY 7 | STEADY 7 | GAIN 1 · power given 1 · STEADY 5 |
| all_four | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 | STEADY 7 | STEADY 7 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 |
| google_2011 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| climb | GAIN 2 · STEADY 5 | GAIN 3 · STEADY 4 | GAIN 2 · LOSS 1 · power given 1 · STEADY 3 | STEADY 7 | STEADY 7 | GAIN 1 · STEADY 6 |
| burst_1419 | GAIN 2 · LOSS 1 · power given 1 · STEADY 3 | GAIN 2 · LOSS 1 · power given 1 · STEADY 3 | GAIN 2 · LOSS 2 · power given 1 · STEADY 2 | STEADY 7 | STEADY 7 | GAIN 2 · LOSS 2 · power given 1 · STEADY 2 |
| burst_1618 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 | STEADY 7 | STEADY 7 | GAIN 1 · LOSS 2 · power given 1 · STEADY 3 |
| real_day | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| fairness | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 | STEADY 7 |
| faults | LOSS 2 · power given 1 · STEADY 4 | LOSS 2 · power given 1 · STEADY 4 | LOSS 4 · power given 1 · STEADY 2 | STEADY 7 | STEADY 7 | LOSS 2 · power given 1 · STEADY 4 |
| batch | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 | STEADY 6 |
| one_body | GAIN 1 · power given 1 · STEADY 8 | GAIN 1 · power given 1 · STEADY 8 | LOSS 2 · STEADY 8 | STEADY 10 | STEADY 10 | STEADY 10 |

## Every organism, gauge by gauge

### steady, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 393.6 | 393.6, STEADY =0.0% | 393.6, STEADY =0.0% | 393.6, STEADY =0.0% | 393.6, STEADY =0.0% | 393.6, STEADY =0.0% |
| minutes over the line (500 ms) | 1.1 | 1.1, STEADY =0.0% | 1.1, STEADY =0.0% | 1.1, STEADY =0.0% | 1.1, STEADY =0.0% | 1.1, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.8 | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% |
| requests served | 8,996 | 8,996, STEADY =0.0% | 8,996, STEADY =0.0% | 8,996, STEADY =0.0% | 8,996, STEADY =0.0% | 8,996, STEADY =0.0% |
| machine-hours | 1.500 | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% |
| energy | 0.010 | 0.010, STEADY =0.0% | 0.010, STEADY =0.0% | 0.010, STEADY =0.0% | 0.010, STEADY =0.0% | 0.010, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −5.2% (−3.4% to −7.1%) | LOSS −5.2% (−3.4% to −7.1%) | LOSS −5.2% (−3.4% to −7.1%) | LOSS −5.2% (−3.4% to −7.1%) | LOSS −9.0% (−6.4% to −11.6%) | LOSS −5.2% (−3.4% to −7.1%) |
| minutes over the line (500 ms) | LOSS −33.3% (−22.0% to +88.6%) | LOSS −33.3% (−22.0% to +88.6%) | LOSS −33.3% (−22.0% to +88.6%) | LOSS −33.3% (−22.0% to +88.6%) | LOSS −88.9% (−16.2% to +194.0%) | LOSS −33.3% (−22.0% to +88.6%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | LOSS −9.7% (−6.4% to −13.0%) | LOSS −9.7% (−6.4% to −13.0%) | LOSS −9.7% (−6.4% to −13.0%) | LOSS −9.7% (−6.4% to −13.0%) | LOSS −20.8% (−13.1% to −28.6%) | LOSS −9.7% (−6.4% to −13.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 21.2, the Kubernetes scheduler's bin-packing profile 21.2, Volcano v1.16.0 22.6, Kueue v0.20.2 21.2, the KAI scheduler v0.18.6 15.4, Koordinator 1.8.0 19.9

### wandering, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 1,892.7 | 1,892.7, STEADY =0.0% | 1,892.7, STEADY =0.0% | 1,892.7, STEADY =0.0% | 1,892.7, STEADY =0.0% | 1,892.7, STEADY =0.0% |
| minutes over the line (500 ms) | 27.9 | 27.9, STEADY =0.0% | 27.9, STEADY =0.0% | 27.9, STEADY =0.0% | 27.9, STEADY =0.0% | 27.9, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.8 | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% |
| requests served | 64,016 | 64,016, STEADY =0.0% | 64,016, STEADY =0.0% | 64,016, STEADY =0.0% | 64,016, STEADY =0.0% | 64,016, STEADY =0.0% |
| machine-hours | 4.500 | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% |
| energy | 0.039 | 0.039, STEADY =0.0% | 0.039, STEADY =0.0% | 0.039, STEADY =0.0% | 0.039, STEADY =0.0% | 0.039, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −90.0% (−84.9% to −95.1%) | LOSS −90.0% (−84.9% to −95.1%) | LOSS −90.0% (−84.9% to −95.1%) | LOSS −90.0% (−84.9% to −95.1%) | LOSS −90.0% (−84.9% to −95.1%) | LOSS −90.0% (−84.9% to −95.1%) |
| minutes over the line (500 ms) | LOSS −30.5% (−27.3% to −33.7%) | LOSS −30.5% (−27.3% to −33.7%) | LOSS −30.5% (−27.3% to −33.7%) | LOSS −30.5% (−27.3% to −33.7%) | LOSS −33.2% (−28.4% to −37.9%) | LOSS −30.5% (−27.3% to −33.7%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 63.5, the Kubernetes scheduler's bin-packing profile 63.5, Volcano v1.16.0 64.6, Kueue v0.20.2 63.5, the KAI scheduler v0.18.6 18.0, Koordinator 1.8.0 59.8

### all_four, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 3,289.2 | 3,289.2, STEADY =0.0% | 3,289.2, STEADY =0.0% | 3,289.2, STEADY =0.0% | 3,289.2, STEADY =0.0% | 3,289.2, STEADY =0.0% |
| minutes over the line (500 ms) | 28.8 | 28.8, STEADY =0.0% | 28.8, STEADY =0.0% | 28.8, STEADY =0.0% | 28.8, STEADY =0.0% | 28.8, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.8 | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% |
| requests served | 69,192 | 69,192, STEADY =0.0% | 69,192, STEADY =0.0% | 69,192, STEADY =0.0% | 69,192, STEADY =0.0% | 69,192, STEADY =0.0% |
| machine-hours | 4.500 | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% | 4.500, STEADY =0.0% |
| energy | 0.040 | 0.040, STEADY =0.0% | 0.040, STEADY =0.0% | 0.040, STEADY =0.0% | 0.040, STEADY =0.0% | 0.040, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −89.9% (−81.6% to −98.1%) | LOSS −89.9% (−81.6% to −98.1%) | LOSS −89.9% (−81.6% to −98.1%) | LOSS −89.9% (−81.6% to −98.1%) | LOSS −89.9% (−81.6% to −98.1%) | LOSS −89.9% (−81.6% to −98.1%) |
| minutes over the line (500 ms) | LOSS −20.4% (−16.2% to −24.7%) | LOSS −20.4% (−16.2% to −24.7%) | LOSS −20.4% (−16.2% to −24.7%) | LOSS −20.4% (−16.2% to −24.7%) | LOSS −26.5% (−19.8% to −33.3%) | LOSS −20.4% (−16.2% to −24.7%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 62.0, the Kubernetes scheduler's bin-packing profile 62.0, Volcano v1.16.0 67.9, Kueue v0.20.2 62.0, the KAI scheduler v0.18.6 18.5, Koordinator 1.8.0 58.4

### google_2011, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 654.4 | 654.4, STEADY =0.0% | 654.4, STEADY =0.0% | 654.4, STEADY =0.0% | 654.4, STEADY =0.0% | 654.4, STEADY =0.0% |
| minutes over the line (500 ms) | 21.1 | 21.1, STEADY =0.0% | 21.1, STEADY =0.0% | 21.1, STEADY =0.0% | 21.1, STEADY =0.0% | 21.1, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.9 | 0.9, STEADY =0.0% | 0.9, STEADY =0.0% | 0.9, STEADY =0.0% | 0.9, STEADY =0.0% | 0.9, STEADY =0.0% |
| requests served | 50,656 | 50,656, STEADY =0.0% | 50,656, STEADY =0.0% | 50,656, STEADY =0.0% | 50,656, STEADY =0.0% | 50,656, STEADY =0.0% |
| machine-hours | 4.325 | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% |
| energy | 0.034 | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −77.0% (−74.3% to −79.6%) | LOSS −77.0% (−74.3% to −79.6%) | LOSS −77.0% (−74.3% to −79.6%) | LOSS −77.0% (−74.3% to −79.6%) | LOSS −89.9% (−88.4% to −91.3%) | LOSS −77.0% (−74.3% to −79.6%) |
| minutes over the line (500 ms) | LOSS −61.0% (−50.9% to −71.0%) | LOSS −61.0% (−50.9% to −71.0%) | LOSS −61.0% (−50.9% to −71.0%) | LOSS −61.0% (−50.9% to −71.0%) | LOSS −102.4% (−96.4% to −108.3%) | LOSS −61.0% (−50.9% to −71.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | LOSS −129.9% (−127.2% to −132.6%) | LOSS −129.9% (−127.2% to −132.6%) | LOSS −129.9% (−127.2% to −132.6%) | LOSS −129.9% (−127.2% to −132.6%) | LOSS −116.1% (−112.1% to −120.1%) | LOSS −129.9% (−127.2% to −132.6%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 69.8, the Kubernetes scheduler's bin-packing profile 69.8, Volcano v1.16.0 71.2, Kueue v0.20.2 69.8, the KAI scheduler v0.18.6 16.8, Koordinator 1.8.0 66.2

### climb, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 2,487.7 | 2,487.7, STEADY =0.0% | 2,487.7, STEADY =0.0% | 2,487.7, STEADY =0.0% | 2,487.7, STEADY =0.0% | 2,487.7, STEADY =0.0% |
| minutes over the line (500 ms) | 22.5 | 22.5, STEADY =0.0% | 22.5, STEADY =0.0% | 22.5, STEADY =0.0% | 22.5, STEADY =0.0% | 22.5, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.8 | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% |
| requests served | 48,567 | 48,567, STEADY =0.0% | 48,567, STEADY =0.0% | 48,567, STEADY =0.0% | 48,567, STEADY =0.0% | 48,567, STEADY =0.0% |
| machine-hours | 3.000 | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% |
| energy | 0.027 | 0.027, STEADY =0.0% | 0.027, STEADY =0.0% | 0.027, STEADY =0.0% | 0.027, STEADY =0.0% | 0.027, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −89.9% (−79.0% to −100.7%) | LOSS −89.9% (−79.0% to −100.7%) | LOSS −89.9% (−79.0% to −100.7%) | LOSS −89.9% (−79.0% to −100.7%) | LOSS −89.9% (−79.0% to −100.7%) | LOSS −89.9% (−79.0% to −100.7%) |
| minutes over the line (500 ms) | LOSS −11.1% (−7.7% to −14.6%) | LOSS −11.1% (−7.7% to −14.6%) | LOSS −11.1% (−7.7% to −14.6%) | LOSS −11.1% (−7.7% to −14.6%) | LOSS −11.7% (−8.9% to −14.4%) | LOSS −11.1% (−7.7% to −14.6%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 45.4, the Kubernetes scheduler's bin-packing profile 45.4, Volcano v1.16.0 46.0, Kueue v0.20.2 45.4, the KAI scheduler v0.18.6 20.1, Koordinator 1.8.0 42.4

### burst_1419, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 10,000.0 | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% |
| minutes over the line (500 ms) | 15.9 | 15.9, STEADY =0.0% | 15.9, STEADY =0.0% | 15.9, STEADY =0.0% | 15.9, STEADY =0.0% | 15.9, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 736 | 736, STEADY =0.0% | 736, STEADY =0.0% | 736, STEADY =0.0% | 736, STEADY =0.0% | 736, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.8 | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% |
| requests served | 38,406 | 38,406, STEADY =0.0% | 38,406, STEADY =0.0% | 38,406, STEADY =0.0% | 38,406, STEADY =0.0% | 38,406, STEADY =0.0% |
| machine-hours | 3.000 | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% |
| energy | 0.025 | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | LOSS −56.7% (−49.8% to −63.6%) | LOSS −56.7% (−49.8% to −63.6%) | LOSS −56.7% (−49.8% to −63.6%) | LOSS −56.7% (−49.8% to −63.6%) | LOSS −62.2% (−60.3% to −64.1%) | LOSS −56.7% (−49.8% to −63.6%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | LOSS −106.9% (−98.4% to −115.5%) | LOSS −106.9% (−98.4% to −115.5%) | LOSS −106.9% (−98.4% to −115.5%) | LOSS −106.9% (−98.4% to −115.5%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −106.9% (−98.4% to −115.5%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 48.2, the Kubernetes scheduler's bin-packing profile 48.2, Volcano v1.16.0 48.2, Kueue v0.20.2 48.2, the KAI scheduler v0.18.6 15.9, Koordinator 1.8.0 42.8

### burst_1618, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 8,330.9 | 8,330.9, STEADY =0.0% | 8,330.9, STEADY =0.0% | 8,330.9, STEADY =0.0% | 8,330.9, STEADY =0.0% | 8,330.9, STEADY =0.0% |
| minutes over the line (500 ms) | 15.8 | 15.8, STEADY =0.0% | 15.8, STEADY =0.0% | 15.8, STEADY =0.0% | 15.8, STEADY =0.0% | 15.8, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.8 | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% |
| requests served | 41,355 | 41,355, STEADY =0.0% | 41,355, STEADY =0.0% | 41,355, STEADY =0.0% | 41,355, STEADY =0.0% | 41,355, STEADY =0.0% |
| machine-hours | 3.000 | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% |
| energy | 0.025 | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% | 0.025, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −20.0% (−17.3% to −22.7%) | LOSS −20.0% (−17.3% to −22.7%) | LOSS −20.0% (−17.3% to −22.7%) | LOSS −20.0% (−17.3% to −22.7%) | LOSS −20.0% (−17.3% to −22.7%) | LOSS −20.0% (−17.3% to −22.7%) |
| minutes over the line (500 ms) | LOSS −63.5% (−63.5% to −63.5%) | LOSS −63.5% (−63.5% to −63.5%) | LOSS −63.5% (−63.5% to −63.5%) | LOSS −63.5% (−63.5% to −63.5%) | LOSS −63.5% (−63.5% to −63.5%) | LOSS −63.5% (−63.5% to −63.5%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) | LOSS −100.0% (−100.0% to −100.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 46.5, the Kubernetes scheduler's bin-packing profile 46.5, Volcano v1.16.0 49.9, Kueue v0.20.2 46.5, the KAI scheduler v0.18.6 17.5, Koordinator 1.8.0 41.5

### real_day, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 976.6 | 976.6, STEADY =0.0% | 976.6, STEADY =0.0% | 976.6, STEADY =0.0% | 976.6, STEADY =0.0% | 976.6, STEADY =0.0% |
| minutes over the line (500 ms) | 25.1 | 25.1, STEADY =0.0% | 25.1, STEADY =0.0% | 25.1, STEADY =0.0% | 25.1, STEADY =0.0% | 25.1, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.9 | 0.9, STEADY =0.0% | 0.9, STEADY =0.0% | 0.9, STEADY =0.0% | 0.9, STEADY =0.0% | 0.9, STEADY =0.0% |
| requests served | 55,734 | 55,734, STEADY =0.0% | 55,734, STEADY =0.0% | 55,734, STEADY =0.0% | 55,734, STEADY =0.0% | 55,734, STEADY =0.0% |
| machine-hours | 4.325 | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% | 4.325, STEADY =0.0% |
| energy | 0.036 | 0.036, STEADY =0.0% | 0.036, STEADY =0.0% | 0.036, STEADY =0.0% | 0.036, STEADY =0.0% | 0.036, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −88.9% (−87.0% to −90.8%) | LOSS −88.9% (−87.0% to −90.8%) | LOSS −88.9% (−87.0% to −90.8%) | LOSS −88.9% (−87.0% to −90.8%) | LOSS −90.0% (−88.4% to −91.6%) | LOSS −88.9% (−87.0% to −90.8%) |
| minutes over the line (500 ms) | LOSS −37.3% (−30.0% to −44.6%) | LOSS −37.3% (−30.0% to −44.6%) | LOSS −37.3% (−30.0% to −44.6%) | LOSS −37.3% (−30.0% to −44.6%) | LOSS −70.2% (−65.5% to −74.8%) | LOSS −37.3% (−30.0% to −44.6%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | LOSS −125.0% (−121.5% to −128.5%) | LOSS −125.0% (−121.5% to −128.5%) | LOSS −125.0% (−121.5% to −128.5%) | LOSS −125.0% (−121.5% to −128.5%) | LOSS −113.6% (−109.6% to −117.7%) | LOSS −125.0% (−121.5% to −128.5%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 68.6, the Kubernetes scheduler's bin-packing profile 68.6, Volcano v1.16.0 75.4, Kueue v0.20.2 68.6, the KAI scheduler v0.18.6 16.8, Koordinator 1.8.0 64.0

### fairness, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 1,643.9 | 1,643.9, STEADY =0.0% | 1,643.9, STEADY =0.0% | 1,643.9, STEADY =0.0% | 1,643.9, STEADY =0.0% | 1,643.9, STEADY =0.0% |
| minutes over the line (500 ms) | 13.9 | 13.9, STEADY =0.0% | 13.9, STEADY =0.0% | 13.9, STEADY =0.0% | 13.9, STEADY =0.0% | 13.9, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 1.5 | 1.5, STEADY =0.0% | 1.5, STEADY =0.0% | 1.5, STEADY =0.0% | 1.5, STEADY =0.0% | 1.5, STEADY =0.0% |
| requests served | 18,003 | 18,003, STEADY =0.0% | 18,003, STEADY =0.0% | 18,003, STEADY =0.0% | 18,003, STEADY =0.0% | 18,003, STEADY =0.0% |
| machine-hours | 1.500 | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% | 1.500, STEADY =0.0% |
| energy | 0.012 | 0.012, STEADY =0.0% | 0.012, STEADY =0.0% | 0.012, STEADY =0.0% | 0.012, STEADY =0.0% | 0.012, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −2.3% (−1.4% to −3.1%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 23.4, the Kubernetes scheduler's bin-packing profile 18.8, Volcano v1.16.0 23.1, Kueue v0.20.2 23.4, the KAI scheduler v0.18.6 4.0, Koordinator 1.8.0 19.0

### faults, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 10,000.0 | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% |
| minutes over the line (500 ms) | 6.6 | 6.6, STEADY =0.0% | 6.6, STEADY =0.0% | 6.6, STEADY =0.0% | 6.6, STEADY =0.0% | 6.6, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 32 | 32, STEADY =0.0% | 32, STEADY =0.0% | 32, STEADY =0.0% | 32, STEADY =0.0% | 32, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.8 | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% |
| requests served | 13,320 | 13,320, STEADY =0.0% | 13,320, STEADY =0.0% | 13,320, STEADY =0.0% | 13,320, STEADY =0.0% | 13,320, STEADY =0.0% |
| machine-hours | 1.467 | 1.467, STEADY =0.0% | 1.467, STEADY =0.0% | 1.467, STEADY =0.0% | 1.467, STEADY =0.0% | 1.467, STEADY =0.0% |
| energy | 0.011 | 0.011, STEADY =0.0% | 0.011, STEADY =0.0% | 0.011, STEADY =0.0% | 0.011, STEADY =0.0% | 0.011, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −3.8% (−2.1% to +9.6%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −25.0% (−20.7% to −29.3%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 15.2, the Kubernetes scheduler's bin-packing profile 15.2, Volcano v1.16.0 20.2, Kueue v0.20.2 15.2, the KAI scheduler v0.18.6 16.9, Koordinator 1.8.0 14.2

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
| the 95th percentile response time | 10,000.0 | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 10,000.0, STEADY =0.0% | 2,429.8, GAIN +75.7% |
| minutes over the line (500 ms) | 30.0 | 30.0, STEADY =0.0% | 30.0, STEADY =0.0% | 30.0, STEADY =0.0% | 30.0, STEADY =0.0% | 23.4, GAIN +22.1% |
| requests failed (unanswered in 10 s) | 8,338 | 8,338, STEADY =0.0% | 8,338, STEADY =0.0% | 8,538, LOSS −2.4% | 8,338, STEADY =0.0% | 0, GAIN +100.0% |
| pods waiting for a place (pod-minutes) | 0.9 | 0.9, STEADY =0.0% | 0.9, STEADY =0.0% | 0.9, LOSS −1.2% | 0.9, STEADY =0.0% | 201.0, LOSS −22866.7% |
| a job's turnaround | 123.4 | 123.4, STEADY =0.0% | 123.4, STEADY =0.0% | 125.7, LOSS −1.8% | 123.4, STEADY =0.0% | 315.9, LOSS −155.9% |
| the stream's makespan (first job in to last job done) | 790.6 | 790.6, STEADY =0.0% | 790.6, STEADY =0.0% | 795.0, LOSS −0.6% | 790.6, STEADY =0.0% | 1,175.6, LOSS −48.7% |
| batch pods done | 240 | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% |
| requests served | 40,211 | 40,211, STEADY =0.0% | 40,211, STEADY =0.0% | 40,010, STEADY =0.5% | 40,211, STEADY =0.0% | 48,548, GAIN +20.7% |
| machine-hours | 3.000 | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% | 3.000, STEADY =0.0% |
| energy | 0.034 | 0.034, STEADY =0.0% | 0.034, STEADY =0.0% | 0.034, STEADY =0.1% | 0.034, STEADY =0.0% | 0.036, power given +5.7% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −90.0% (−83.9% to −96.1%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | GAIN +5.4% (+3.8% to +7.0%) | GAIN +5.4% (+3.8% to +7.0%) | GAIN +5.4% (+3.8% to +7.0%) | GAIN +5.4% (+3.9% to +7.0%) | GAIN +3.1% (+2.2% to +4.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | LOSS −111.9% (−103.7% to −120.2%) | LOSS −111.9% (−103.7% to −120.2%) | LOSS −111.9% (−103.7% to −120.2%) | LOSS −109.4% (−102.2% to −116.6%) | LOSS −100.0% (−92.6% to −107.4%) | STEADY =0.4% (+0.4% to +0.4%) |
| a job's turnaround | LOSS −14.1% (−9.9% to −18.2%) | LOSS −14.1% (−9.9% to −18.2%) | LOSS −14.1% (−9.9% to −18.2%) | LOSS −14.3% (−12.2% to −16.3%) | LOSS −8.0% (−4.4% to −11.7%) | STEADY =0.0% (±0.0% to ±0.0%) |
| the stream's makespan (first job in to last job done) | LOSS −1.4% (−0.9% to −1.9%) | LOSS −1.4% (−0.9% to −1.9%) | LOSS −1.4% (−0.9% to −1.9%) | LOSS −1.3% (−1.0% to −1.7%) | LOSS −0.8% (−0.3% to −1.3%) | STEADY =0.0% (±0.0% to ±0.0%) |
| batch pods done | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | GAIN +1.1% (+0.8% to +1.5%) | GAIN +1.1% (+0.8% to +1.5%) | GAIN +1.1% (+0.8% to +1.5%) | GAIN +1.2% (+0.8% to +1.5%) | GAIN +0.6% (+0.5% to +0.8%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.2% (+0.1% to +0.2%) | STEADY =0.2% (+0.1% to +0.2%) | STEADY =0.2% (+0.1% to +0.2%) | STEADY =0.2% (+0.1% to +0.2%) | STEADY =0.1% (+0.0% to +0.1%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 56.6, the Kubernetes scheduler's bin-packing profile 56.6, Volcano v1.16.0 55.5, Kueue v0.20.2 57.9, the KAI scheduler v0.18.6 9.8, Koordinator 1.8.0 48.1

### steady, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 225.9 | 225.9, STEADY =0.0% | 239.0, LOSS −5.8% | 272.6, LOSS −20.7% | 540.8, LOSS −139.4% | 225.9, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 1.0, STEADY =0.0% | 7.1, LOSS −612.5% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.8 | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% |
| requests served | 8,992 | 8,992, STEADY =0.0% | 8,992, STEADY =0.0% | 8,992, STEADY =0.0% | 8,992, STEADY =0.0% | 8,992, STEADY =0.0% |
| machine-hours | 1.127 | 1.127, STEADY =0.0% | 1.127, STEADY =0.0% | 0.500, GAIN +55.6% | 1.127, STEADY =0.0% | 1.127, STEADY =0.0% |
| energy | 0.076 | 0.076, STEADY =0.0% | 0.078, power given +2.5% | 0.036, GAIN +52.4% | 0.086, power given +13.5% | 0.076, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −4.9% (−1.4% to −8.4%) | LOSS −13.6% (−5.3% to −21.8%) | LOSS −14.2% (−8.2% to −20.1%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −4.9% (−1.4% to −8.4%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | power given +2.7% (+1.3% to +4.1%) | power given +6.1% (+4.3% to +7.8%) | power given +3.4% (+1.2% to +5.6%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | power given +2.7% (+1.3% to +4.1%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 4.0, the Kubernetes scheduler's bin-packing profile 4.0, Volcano v1.16.0 4.0, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 7.6, Koordinator 1.8.0 4.0

### wandering, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 484.2 | 484.2, STEADY =0.0% | 492.3, LOSS −1.7% | 503.3, LOSS −4.0% | 10,000.0, LOSS −1965.3% | 484.2, STEADY =0.0% |
| minutes over the line (500 ms) | 7.0 | 7.0, STEADY =0.0% | 7.8, LOSS −10.7% | 9.4, LOSS −33.9% | 39.4, LOSS −462.5% | 7.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 377, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 1.2 | 1.2, STEADY =0.0% | 0.9, GAIN +23.2% | 0.8, GAIN +35.7% | 0.8, GAIN +35.7% | 1.2, STEADY =0.0% |
| requests served | 64,156 | 64,156, STEADY =0.0% | 64,156, STEADY =0.0% | 64,156, STEADY =0.0% | 63,779, LOSS −0.6% | 64,156, STEADY =0.0% |
| machine-hours | 2.197 | 2.197, STEADY =0.0% | 2.197, STEADY =0.0% | 1.500, GAIN +31.7% | 2.197, STEADY =0.0% | 2.197, STEADY =0.0% |
| energy | 0.175 | 0.175, STEADY =0.0% | 0.181, power given +3.3% | 0.133, GAIN +24.2% | 0.197, power given +12.5% | 0.175, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.3% (−0.8% to +0.1%) | STEADY =0.5% (−0.9% to −0.1%) | LOSS −45.9% (−26.8% to +118.6%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.3% (−0.8% to +0.1%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −56.5% (−7.5% to +120.4%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | GAIN +11.6% (+3.8% to +19.4%) | GAIN +19.6% (+16.9% to +22.4%) | GAIN +10.5% (+4.0% to +17.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | GAIN +11.6% (+3.8% to +19.4%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | power given +1.9% (+0.2% to +3.7%) | power given +3.9% (+3.9% to +3.9%) | power given +5.0% (+2.7% to +7.2%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | power given +1.9% (+0.2% to +3.7%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 8.4, the Kubernetes scheduler's bin-packing profile 7.9, Volcano v1.16.0 12.9, Kueue v0.20.2 8.9, the KAI scheduler v0.18.6 39.1, Koordinator 1.8.0 8.4

### all_four, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 387.4 | 387.4, STEADY =0.0% | 534.4, LOSS −37.9% | 555.2, LOSS −43.3% | 10,000.0, LOSS −2481.2% | 387.4, STEADY =0.0% |
| minutes over the line (500 ms) | 3.8 | 3.8, STEADY =0.0% | 11.4, LOSS −203.3% | 13.0, LOSS −246.7% | 38.9, LOSS −936.7% | 3.8, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 875, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 1.2 | 1.2, STEADY =0.0% | 0.9, GAIN +25.0% | 0.8, GAIN +35.7% | 0.8, GAIN +35.7% | 1.2, STEADY =0.0% |
| requests served | 69,069 | 69,069, STEADY =0.0% | 69,069, STEADY =0.0% | 69,069, STEADY =0.0% | 68,194, LOSS −1.3% | 69,069, STEADY =0.0% |
| machine-hours | 2.650 | 2.650, STEADY =0.0% | 2.650, STEADY =0.0% | 1.500, GAIN +43.4% | 2.650, STEADY =0.0% | 2.650, STEADY =0.0% |
| energy | 0.213 | 0.213, STEADY =0.0% | 0.229, power given +7.5% | 0.136, GAIN +36.0% | 0.249, power given +17.1% | 0.213, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −20.8% (−4.2% to −37.4%) | LOSS −43.3% (−42.4% to −44.3%) | LOSS −12.1% (−13.4% to +37.7%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −22.5% (−7.2% to −37.8%) |
| minutes over the line (500 ms) | LOSS −130.0% (−40.5% to −219.5%) | LOSS −246.7% (−236.3% to −257.0%) | LOSS −25.3% (−11.3% to +61.8%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −140.0% (−59.4% to −220.6%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | GAIN +29.5% (+24.5% to +34.5%) | GAIN +35.7% (+35.7% to +35.7%) | GAIN +9.5% (+1.0% to +18.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | GAIN +30.4% (+26.1% to +34.6%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | power given +8.8% (+3.4% to +14.2%) | power given +16.4% (+16.3% to +16.4%) | power given +3.4% (−0.6% to +7.2%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | power given +9.5% (+4.7% to +14.2%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 9.6, the Kubernetes scheduler's bin-packing profile 13.6, Volcano v1.16.0 14.5, Kueue v0.20.2 11.6, the KAI scheduler v0.18.6 39.5, Koordinator 1.8.0 10.0

### google_2011, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 360.0 | 360.0, STEADY =0.0% | 710.1, LOSS −97.3% | 360.0, STEADY =0.0% | 1,273.8, LOSS −253.9% | 360.0, STEADY =0.0% |
| minutes over the line (500 ms) | 2.4 | 2.4, STEADY =0.0% | 7.8, LOSS −226.3% | 2.4, STEADY =0.0% | 37.9, LOSS −1494.7% | 2.4, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.9 | 0.9, STEADY =0.0% | 1.1, LOSS −23.9% | 0.9, STEADY =0.0% | 1.0, LOSS −9.1% | 0.9, STEADY =0.0% |
| requests served | 50,690 | 50,690, STEADY =0.0% | 50,690, STEADY =0.0% | 50,690, STEADY =0.0% | 50,690, STEADY =0.0% | 50,690, STEADY =0.0% |
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

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 2.2, the Kubernetes scheduler's bin-packing profile 2.2, Volcano v1.16.0 6.9, Kueue v0.20.2 2.2, the KAI scheduler v0.18.6 36.4, Koordinator 1.8.0 2.2

### climb, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 533.8 | 533.8, STEADY =0.0% | 660.7, LOSS −23.8% | 544.2, LOSS −1.9% | 10,000.0, LOSS −1773.3% | 533.8, STEADY =0.0% |
| minutes over the line (500 ms) | 7.6 | 7.6, STEADY =0.0% | 9.0, LOSS −18.0% | 8.4, LOSS −9.8% | 28.6, LOSS −275.4% | 7.6, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 291, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 1.0 | 1.0, STEADY =0.0% | 0.9, GAIN +8.3% | 0.8, GAIN +25.0% | 0.8, GAIN +25.0% | 1.0, STEADY =0.0% |
| requests served | 48,619 | 48,619, STEADY =0.0% | 48,619, STEADY =0.0% | 48,619, STEADY =0.0% | 47,911, LOSS −1.5% | 48,619, STEADY =0.0% |
| machine-hours | 1.722 | 1.722, STEADY =0.0% | 1.722, STEADY =0.0% | 1.000, GAIN +41.9% | 1.722, STEADY =0.0% | 1.722, STEADY =0.0% |
| energy | 0.143 | 0.143, STEADY =0.0% | 0.143, STEADY =0.2% | 0.092, GAIN +35.2% | 0.158, power given +10.5% | 0.143, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.4% (−0.7% to −0.1%) | GAIN +0.7% (+0.4% to +0.9%) | GAIN +1.2% (−3.4% to +1.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.5% (−0.8% to −0.1%) |
| minutes over the line (500 ms) | GAIN +1.6% (−5.5% to +2.2%) | GAIN +1.6% (−5.5% to +2.2%) | LOSS −1.4% (−1.9% to +4.7%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | GAIN +5.2% (+1.6% to +8.8%) | GAIN +8.3% (+8.3% to +8.3%) | GAIN +8.0% (+5.3% to +10.6%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | GAIN +6.2% (+3.0% to +9.5%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | power given +1.2% (−1.6% to +3.9%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 8.2, the Kubernetes scheduler's bin-packing profile 8.1, Volcano v1.16.0 10.0, Kueue v0.20.2 8.2, the KAI scheduler v0.18.6 29.2, Koordinator 1.8.0 8.4

### burst_1419, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 974.5 | 974.5, STEADY =0.0% | 3,694.0, LOSS −279.1% | 960.6, GAIN +1.4% | 10,000.0, LOSS −926.1% | 707.1, GAIN +27.4% |
| minutes over the line (500 ms) | 6.6 | 6.6, STEADY =0.0% | 8.0, LOSS −20.8% | 8.8, LOSS −32.1% | 15.9, LOSS −139.6% | 6.6, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 191, LOSS −100.0% | 0, STEADY =0.0% | 3,316, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 1.0 | 1.0, STEADY =0.0% | 0.9, GAIN +10.4% | 0.8, GAIN +25.0% | 0.8, GAIN +25.0% | 3.1, LOSS −208.3% |
| requests served | 39,606 | 39,606, STEADY =0.0% | 39,290, LOSS −0.8% | 39,606, STEADY =0.0% | 35,873, LOSS −9.4% | 39,606, STEADY =0.0% |
| machine-hours | 1.747 | 1.747, STEADY =0.0% | 1.747, STEADY =0.0% | 1.000, GAIN +42.8% | 1.747, STEADY =0.0% | 1.832, power given +4.9% |
| energy | 0.137 | 0.137, STEADY =0.0% | 0.137, STEADY =0.1% | 0.086, GAIN +36.8% | 0.146, power given +6.9% | 0.145, power given +5.7% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN +1.9% (+0.9% to +2.8%) | GAIN +1.4% (+0.8% to +2.1%) | GAIN +4.4% (−120.2% to +111.5%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −18.6% (−1.7% to +39.0%) |
| minutes over the line (500 ms) | LOSS −15.1% (−9.2% to +39.4%) | LOSS −32.1% (−11.3% to −52.8%) | LOSS −37.5% (−0.4% to +75.4%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −20.8% (−4.4% to +45.9%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −2.8% (−183.4% to +189.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | GAIN +17.7% (+11.9% to +23.5%) | GAIN +25.0% (+25.0% to +25.0%) | GAIN +16.3% (+10.8% to +21.8%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | GAIN +53.7% (+15.4% to +92.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (−1.5% to +1.4%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | GAIN +1.9% (−4.7% to +1.0%) |
| energy | power given +2.6% (−0.4% to +5.6%) | power given +6.9% (+6.9% to +7.0%) | power given +7.0% (+6.5% to +7.4%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | power given +1.1% (−1.8% to +4.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 9.4, the Kubernetes scheduler's bin-packing profile 10.8, Volcano v1.16.0 13.0, Kueue v0.20.2 8.2, the KAI scheduler v0.18.6 16.9, Koordinator 1.8.0 9.8

### burst_1618, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 419.9 | 419.9, STEADY =0.0% | 570.8, LOSS −36.0% | 664.8, LOSS −58.3% | 10,000.0, LOSS −2281.6% | 419.9, STEADY =0.0% |
| minutes over the line (500 ms) | 3.8 | 3.8, STEADY =0.0% | 10.0, LOSS −166.7% | 11.2, LOSS −200.0% | 16.6, LOSS −343.3% | 3.8, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 1,533, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 1.0 | 1.0, STEADY =0.0% | 0.9, GAIN +12.5% | 0.8, GAIN +25.0% | 0.8, GAIN +25.0% | 1.0, STEADY =0.0% |
| requests served | 41,424 | 41,424, STEADY =0.0% | 41,424, STEADY =0.0% | 41,424, STEADY =0.0% | 39,892, LOSS −3.7% | 41,424, STEADY =0.0% |
| machine-hours | 1.747 | 1.747, STEADY =0.0% | 1.747, STEADY =0.0% | 1.000, GAIN +42.8% | 1.747, STEADY =0.0% | 1.747, STEADY =0.0% |
| energy | 0.140 | 0.140, STEADY =0.0% | 0.140, STEADY =0.0% | 0.088, GAIN +37.2% | 0.153, power given +9.5% | 0.140, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −26.4% (−5.6% to −47.3%) | LOSS −58.3% (−55.2% to −61.5%) | LOSS −67.3% (−28.7% to −105.9%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −15.6% (−5.2% to +36.4%) |
| minutes over the line (500 ms) | LOSS −130.0% (−56.1% to −203.9%) | LOSS −200.0% (−173.3% to −226.7%) | LOSS −33.8% (−3.8% to −63.7%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −66.7% (−14.2% to +147.5%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | GAIN +17.7% (+11.9% to +23.5%) | GAIN +25.0% (+25.0% to +25.0%) | GAIN +14.3% (+10.0% to +18.5%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | GAIN +13.5% (+7.2% to +19.9%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | power given +3.4% (−0.5% to +7.3%) | power given +9.0% (+9.0% to +9.1%) | power given +8.9% (+8.8% to +9.1%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | power given +2.3% (−1.2% to +5.8%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 9.8, the Kubernetes scheduler's bin-packing profile 12.1, Volcano v1.16.0 15.2, Kueue v0.20.2 9.1, the KAI scheduler v0.18.6 17.6, Koordinator 1.8.0 7.4

### real_day, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 412.5 | 412.5, STEADY =0.0% | 1,709.3, LOSS −314.4% | 412.5, STEADY =0.0% | 3,777.1, LOSS −815.6% | 412.5, STEADY =0.0% |
| minutes over the line (500 ms) | 5.0 | 5.0, STEADY =0.0% | 11.2, LOSS −125.0% | 5.0, STEADY =0.0% | 38.0, LOSS −660.0% | 5.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.9 | 0.9, STEADY =0.0% | 1.1, LOSS −17.2% | 0.9, STEADY =0.0% | 1.0, LOSS −9.2% | 0.9, STEADY =0.0% |
| requests served | 55,773 | 55,773, STEADY =0.0% | 55,773, STEADY =0.0% | 55,773, STEADY =0.0% | 55,773, STEADY =0.0% | 55,773, STEADY =0.0% |
| machine-hours | 2.101 | 2.101, STEADY =0.0% | 2.000, GAIN +4.8% | 1.442, GAIN +31.4% | 1.939, GAIN +7.7% | 2.101, STEADY =0.0% |
| energy | 0.181 | 0.181, STEADY =0.0% | 0.171, GAIN +5.7% | 0.124, GAIN +31.7% | 0.165, GAIN +9.0% | 0.181, STEADY =0.0% |

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

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 4.5, the Kubernetes scheduler's bin-packing profile 4.5, Volcano v1.16.0 10.0, Kueue v0.20.2 4.5, the KAI scheduler v0.18.6 36.2, Koordinator 1.8.0 4.5

### fairness, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 300.2 | 304.1, LOSS −1.3% | 412.8, LOSS −37.5% | 673.8, LOSS −124.4% | 626.4, LOSS −108.6% | 300.2, STEADY =0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY =0.0% | 2.8, LOSS −175.0% | 8.8, LOSS −775.0% | 10.6, LOSS −962.5% | 1.0, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 1.5 | 1.5, STEADY =0.0% | 1.5, STEADY =0.0% | 4.8, LOSS −222.2% | 1.5, STEADY =0.0% | 1.5, STEADY =0.0% |
| requests served | 18,000 | 18,000, STEADY =0.0% | 18,000, STEADY =0.0% | 18,000, STEADY =0.0% | 18,000, STEADY =0.0% | 18,000, STEADY =0.0% |
| machine-hours | 1.125 | 1.125, STEADY =0.0% | 1.125, STEADY =0.0% | 0.803, GAIN +28.6% | 1.125, STEADY =0.0% | 1.125, STEADY =0.0% |
| energy | 0.084 | 0.084, STEADY =0.2% | 0.084, STEADY =0.3% | 0.064, GAIN +23.6% | 0.091, power given +8.9% | 0.084, STEADY =0.0% |

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

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 3.0, the Kubernetes scheduler's bin-packing profile 3.0, Volcano v1.16.0 2.9, Kueue v0.20.2 10.0, the KAI scheduler v0.18.6 9.0, Koordinator 1.8.0 3.0

### faults, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 397.8 | 397.8, STEADY =0.0% | 2,421.6, LOSS −508.8% | 9,070.0, LOSS −2180.2% | 10,000.0, LOSS −2414.0% | 397.8, STEADY =0.0% |
| minutes over the line (500 ms) | 2.6 | 2.6, STEADY =0.0% | 4.2, LOSS −61.9% | 5.9, LOSS −123.8% | 10.0, LOSS −280.9% | 2.6, STEADY =0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 130, LOSS −100.0% | 14, LOSS −100.0% | 1,052, LOSS −100.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 0.8 | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% | 0.8, STEADY =0.0% |
| requests served | 13,313 | 13,313, STEADY =0.0% | 13,184, LOSS −1.0% | 13,299, STEADY =0.1% | 12,262, LOSS −7.9% | 13,313, STEADY =0.0% |
| machine-hours | 1.092 | 1.092, STEADY =0.0% | 1.092, STEADY =0.0% | 0.467, GAIN +57.2% | 1.092, STEADY =0.0% | 1.092, STEADY =0.0% |
| energy | 0.080 | 0.080, STEADY =0.0% | 0.085, power given +6.5% | 0.039, GAIN +50.9% | 0.092, power given +15.2% | 0.080, STEADY =0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | LOSS −55.2% (−6.4% to −104.0%) | LOSS −78.2% (−23.9% to −132.5%) | LOSS −131.1% (−21.7% to +283.9%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −55.2% (−6.4% to −104.0%) |
| minutes over the line (500 ms) | LOSS −33.3% (−6.8% to −59.9%) | LOSS −33.3% (−6.8% to −59.9%) | LOSS −44.1% (−13.9% to +102.1%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −33.3% (−6.8% to −59.9%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −204.1% (−112.5% to +520.8%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −2.0% (−5.1% to +1.1%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | power given +7.0% (+3.5% to +10.6%) | power given +9.0% (+5.5% to +12.5%) | power given +3.9% (+0.7% to +7.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | power given +7.0% (+3.5% to +10.6%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 7.9, the Kubernetes scheduler's bin-packing profile 7.9, Volcano v1.16.0 9.0, Kueue v0.20.2 6.8, the KAI scheduler v0.18.6 11.5, Koordinator 1.8.0 7.9

### batch, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | 7.3 | 7.3, STEADY =0.0% | 5.1, GAIN +30.0% | 8.0, LOSS −9.1% | 5.3, GAIN +28.0% | 32.8, LOSS −347.7% |
| a job's turnaround | 42.7 | 42.7, STEADY =0.0% | 42.1, GAIN +1.4% | 48.3, LOSS −13.2% | 46.8, LOSS −9.6% | 60.7, LOSS −42.2% |
| the stream's makespan (first job in to last job done) | 725.0 | 725.0, STEADY =0.0% | 725.6, STEADY =0.1% | 730.0, LOSS −0.7% | 731.2, LOSS −0.9% | 726.9, STEADY =0.3% |
| batch pods done | 240 | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% |
| machine-hours | 2.564 | 2.564, STEADY =0.0% | 2.222, GAIN +13.3% | 2.564, STEADY =0.0% | 2.222, GAIN +13.3% | 3.356, power given +30.9% |
| energy | 0.200 | 0.201, power given +0.8% | 0.177, GAIN +11.3% | 0.199, GAIN +0.6% | 0.193, GAIN +3.6% | 0.252, power given +26.2% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| a job's turnaround | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| the stream's makespan (first job in to last job done) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| batch pods done | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 29.0, the Kubernetes scheduler's bin-packing profile 29.0, Volcano v1.16.0 28.1, Kueue v0.20.2 27.0, the KAI scheduler v0.18.6 28.2, Koordinator 1.8.0 11.0

### one_body, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 545.0 | 554.4, LOSS −1.7% | 642.4, LOSS −17.9% | 555.2, LOSS −1.9% | 2,610.8, LOSS −379.1% | 524.6, GAIN +3.7% |
| minutes over the line (500 ms) | 8.6 | 9.2, LOSS −7.2% | 9.1, LOSS −5.8% | 10.0, LOSS −15.9% | 15.4, LOSS −78.3% | 6.4, GAIN +26.1% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% | 0, STEADY =0.0% |
| pods waiting for a place (pod-minutes) | 8.6 | 12.7, LOSS −47.3% | 11.1, LOSS −28.5% | 9.1, LOSS −5.9% | 12.9, LOSS −49.8% | 49.4, LOSS −472.6% |
| a job's turnaround | 42.6 | 44.4, LOSS −4.3% | 46.5, LOSS −9.3% | 46.9, LOSS −10.2% | 52.3, LOSS −22.9% | 67.6, LOSS −58.9% |
| the stream's makespan (first job in to last job done) | 725.0 | 725.0, STEADY =0.0% | 728.1, STEADY =0.4% | 730.0, LOSS −0.7% | 737.5, LOSS −1.7% | 725.6, STEADY =0.1% |
| batch pods done | 240 | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% | 240, STEADY =0.0% |
| requests served | 48,615 | 48,615, STEADY =0.0% | 48,615, STEADY =0.0% | 48,615, STEADY =0.0% | 48,613, STEADY =0.0% | 48,615, STEADY =0.0% |
| machine-hours | 2.747 | 3.064, power given +11.5% | 3.107, power given +13.1% | 2.389, GAIN +13.0% | 3.150, power given +14.7% | 3.522, power given +28.2% |
| energy | 0.237 | 0.266, power given +12.2% | 0.275, power given +16.3% | 0.216, GAIN +8.6% | 0.294, power given +24.2% | 0.293, power given +23.9% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY =0.1% (−0.2% to +0.0%) | STEADY =0.0% (−0.0% to ±0.0%) | STEADY =0.2% (−0.1% to +0.5%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY =0.0% (±0.0% to ±0.0%) | GAIN +1.4% (−4.5% to +1.8%) | LOSS −2.7% (−1.5% to +7.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | GAIN +0.7% (+0.3% to +1.1%) | STEADY =0.2% (−0.5% to +0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| a job's turnaround | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | LOSS −0.8% (−0.1% to −1.6%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.2% (−0.1% to +0.6%) |
| the stream's makespan (first job in to last job done) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.1% (−0.1% to +0.3%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (−0.3% to +0.3%) |
| batch pods done | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| requests served | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| machine-hours | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) |
| energy | power given +2.0% (+1.1% to +2.8%) | power given +0.7% (+0.3% to +1.0%) | STEADY =0.4% (+0.2% to +0.5%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (±0.0% to ±0.0%) | STEADY =0.0% (−0.1% to +0.1%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 20.0, the Kubernetes scheduler's bin-packing profile 19.6, Volcano v1.16.0 23.1, Kueue v0.20.2 26.2, the KAI scheduler v0.18.6 29.6, Koordinator 1.8.0 19.8

## What the model leaves out

The processor alone is modelled (memory, disks and the network are not); a request's cost, the clients' rate and the pod start times are the rig's own calibration (the model gate's); every orchestrator's rule is written from its release and documentation, never from its code, and each is listed above with the file it was read from. The Gödel scheduler, KubeRay, Crane and the multi-cluster orchestrators (Karmada, Open Cluster Management, Armada) run on GitHub's machines four ways (`results/live/GOVERNORS.md`); their rules join this model once each one's shipped default is read from its release, and nothing is written for them here before that.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
