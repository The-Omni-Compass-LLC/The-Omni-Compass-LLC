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
| steady | STEADY 7 | STEADY 7 | STEADY 7 | LOSS 1 · power given 1 · STEADY 5 | STEADY 7 |
| wandering | STEADY 7 | LOSS 2 · STEADY 5 | STEADY 7 | LOSS 4 · power given 1 · STEADY 2 | STEADY 7 |
| all_four | STEADY 7 | LOSS 1 · STEADY 6 | STEADY 7 | LOSS 4 · power given 1 · STEADY 2 | STEADY 7 |
| google_2011 | STEADY 7 | LOSS 1 · STEADY 6 | STEADY 7 | LOSS 2 · STEADY 5 | STEADY 7 |
| climb | STEADY 7 | LOSS 2 · STEADY 5 | STEADY 7 | LOSS 4 · STEADY 3 | STEADY 7 |
| burst_1419 | STEADY 7 | LOSS 4 · STEADY 3 | STEADY 7 | GAIN 1 · LOSS 4 · STEADY 2 | STEADY 7 |
| burst_1618 | STEADY 7 | LOSS 1 · STEADY 6 | STEADY 7 | LOSS 4 · power given 1 · STEADY 2 | LOSS 1 · power given 2 · STEADY 4 |
| real_day | STEADY 7 | LOSS 1 · STEADY 6 | STEADY 7 | LOSS 2 · STEADY 5 | STEADY 7 |
| fairness | STEADY 7 | LOSS 1 · STEADY 6 | STEADY 7 | LOSS 1 · power given 1 · STEADY 5 | STEADY 7 |
| faults | STEADY 7 | GAIN 1 · LOSS 4 · STEADY 2 | STEADY 7 | LOSS 4 · STEADY 3 | STEADY 7 |
| batch | power given 1 · STEADY 5 | GAIN 4 · STEADY 2 | GAIN 1 · LOSS 3 · STEADY 2 | GAIN 3 · LOSS 2 · STEADY 1 | LOSS 2 · power given 2 · STEADY 2 |
| one_body | GAIN 1 · LOSS 2 · power given 2 · STEADY 5 | GAIN 1 · LOSS 3 · power given 2 · STEADY 4 | GAIN 1 · LOSS 3 · STEADY 6 | LOSS 5 · power given 2 · STEADY 3 | LOSS 4 · power given 2 · STEADY 4 |

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
| one_body | power given 1 · STEADY 9 | power given 1 · STEADY 9 | LOSS 1 · STEADY 9 | STEADY 10 | STEADY 10 | STEADY 10 |

## Every organism, gauge by gauge

### steady, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 207.8 | 207.8, STEADY 0.0% | 207.8, STEADY 0.0% | 207.8, STEADY 0.0% | 207.8, STEADY 0.0% | 207.8, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 8,996 | 8,996, STEADY 0.0% | 8,996, STEADY 0.0% | 8,996, STEADY 0.0% | 8,996, STEADY 0.0% | 8,996, STEADY 0.0% |
| machine-hours | 1.500 | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% |
| energy | 0.010 | 0.010, STEADY 0.0% | 0.010, STEADY 0.0% | 0.010, STEADY 0.0% | 0.010, STEADY 0.0% | 0.010, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN 50.1% (raw −51.1% to −49.1%) | GAIN 50.1% (raw −51.1% to −49.1%) | GAIN 50.1% (raw −51.1% to −49.1%) | GAIN 50.1% (raw −51.1% to −49.1%) | GAIN 7.1% (raw −8.3% to −6.0%) | GAIN 50.1% (raw −51.1% to −49.1%) |
| minutes over the line (500 ms) | GAIN 25.0% (raw −63.7% to +13.7%) | GAIN 25.0% (raw −63.7% to +13.7%) | GAIN 25.0% (raw −63.7% to +13.7%) | GAIN 25.0% (raw −63.7% to +13.7%) | GAIN 25.0% (raw −63.7% to +13.7%) | GAIN 25.0% (raw −63.7% to +13.7%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 18.0, the Kubernetes scheduler's bin-packing profile 18.0, Volcano v1.16.0 19.5, Kueue v0.20.2 18.0, the KAI scheduler v0.18.6 15.0, Koordinator 1.8.0 17.8

### wandering, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 336.9 | 336.9, STEADY 0.0% | 336.9, STEADY 0.0% | 336.9, STEADY 0.0% | 336.9, STEADY 0.0% | 336.9, STEADY 0.0% |
| minutes over the line (500 ms) | 4.0 | 4.0, STEADY 0.0% | 4.0, STEADY 0.0% | 4.0, STEADY 0.0% | 4.0, STEADY 0.0% | 4.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 64,016 | 64,016, STEADY 0.0% | 64,016, STEADY 0.0% | 64,016, STEADY 0.0% | 64,016, STEADY 0.0% | 64,016, STEADY 0.0% |
| machine-hours | 4.500 | 4.500, STEADY 0.0% | 4.500, STEADY 0.0% | 4.500, STEADY 0.0% | 4.500, STEADY 0.0% | 4.500, STEADY 0.0% |
| energy | 0.039 | 0.039, STEADY 0.0% | 0.039, STEADY 0.0% | 0.039, STEADY 0.0% | 0.039, STEADY 0.0% | 0.039, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN 24.8% (raw −25.9% to −23.7%) | GAIN 24.8% (raw −25.9% to −23.7%) | GAIN 24.8% (raw −25.9% to −23.7%) | GAIN 24.8% (raw −25.9% to −23.7%) | GAIN 3.2% (raw −4.1% to −2.3%) | GAIN 24.8% (raw −25.9% to −23.7%) |
| minutes over the line (500 ms) | GAIN 6.2% (raw −15.9% to +3.4%) | GAIN 6.2% (raw −15.9% to +3.4%) | GAIN 6.2% (raw −15.9% to +3.4%) | GAIN 6.2% (raw −15.9% to +3.4%) | GAIN 3.1% (raw −10.5% to +4.3%) | GAIN 6.2% (raw −15.9% to +3.4%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 30.6, the Kubernetes scheduler's bin-packing profile 30.6, Volcano v1.16.0 34.1, Kueue v0.20.2 30.6, the KAI scheduler v0.18.6 21.0, Koordinator 1.8.0 29.0

### all_four, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 472.5 | 472.5, STEADY 0.0% | 472.5, STEADY 0.0% | 472.5, STEADY 0.0% | 472.5, STEADY 0.0% | 472.5, STEADY 0.0% |
| minutes over the line (500 ms) | 4.4 | 4.4, STEADY 0.0% | 4.4, STEADY 0.0% | 4.4, STEADY 0.0% | 4.4, STEADY 0.0% | 4.4, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 69,192 | 69,192, STEADY 0.0% | 69,192, STEADY 0.0% | 69,192, STEADY 0.0% | 69,192, STEADY 0.0% | 69,192, STEADY 0.0% |
| machine-hours | 4.500 | 4.500, STEADY 0.0% | 4.500, STEADY 0.0% | 4.500, STEADY 0.0% | 4.500, STEADY 0.0% | 4.500, STEADY 0.0% |
| energy | 0.040 | 0.040, STEADY 0.0% | 0.040, STEADY 0.0% | 0.040, STEADY 0.0% | 0.040, STEADY 0.0% | 0.040, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN 14.8% (raw −16.2% to −13.6%) | GAIN 14.8% (raw −16.2% to −13.6%) | GAIN 14.8% (raw −16.2% to −13.6%) | GAIN 14.8% (raw −16.2% to −13.6%) | GAIN 2.3% (raw −2.7% to −1.9%) | GAIN 14.8% (raw −16.2% to −13.6%) |
| minutes over the line (500 ms) | GAIN 5.7% (raw −14.6% to +3.1%) | GAIN 5.7% (raw −14.6% to +3.1%) | GAIN 5.7% (raw −14.6% to +3.1%) | GAIN 5.7% (raw −14.6% to +3.1%) | GAIN 2.9% (raw −9.6% to +3.9%) | GAIN 5.7% (raw −14.6% to +3.1%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 18.4, the Kubernetes scheduler's bin-packing profile 18.4, Volcano v1.16.0 19.9, Kueue v0.20.2 18.4, the KAI scheduler v0.18.6 18.6, Koordinator 1.8.0 17.4

### google_2011, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 212.2 | 212.2, STEADY 0.0% | 212.2, STEADY 0.0% | 212.2, STEADY 0.0% | 212.2, STEADY 0.0% | 212.2, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 10 | 10, STEADY 0.0% | 10, STEADY 0.0% | 10, STEADY 0.0% | 10, STEADY 0.0% | 10, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 50,646 | 50,646, STEADY 0.0% | 50,646, STEADY 0.0% | 50,646, STEADY 0.0% | 50,646, STEADY 0.0% | 50,646, STEADY 0.0% |
| machine-hours | 4.325 | 4.325, STEADY 0.0% | 4.325, STEADY 0.0% | 4.325, STEADY 0.0% | 4.325, STEADY 0.0% | 4.325, STEADY 0.0% |
| energy | 0.034 | 0.034, STEADY 0.0% | 0.034, STEADY 0.0% | 0.034, STEADY 0.0% | 0.034, STEADY 0.0% | 0.034, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN 43.0% (raw −43.6% to −42.3%) | GAIN 43.0% (raw −43.6% to −42.3%) | GAIN 43.0% (raw −43.6% to −42.3%) | GAIN 43.0% (raw −43.6% to −42.3%) | GAIN 1.2% (raw −1.6% to −0.9%) | GAIN 43.0% (raw −43.6% to −42.3%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | GAIN 100.0% (raw −173.5% to −26.5%) | GAIN 100.0% (raw −173.5% to −26.5%) | GAIN 100.0% (raw −173.5% to −26.5%) | GAIN 100.0% (raw −173.5% to −26.5%) | GAIN 100.0% (raw −173.5% to −26.5%) | GAIN 100.0% (raw −173.5% to −26.5%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 34.1, the Kubernetes scheduler's bin-packing profile 34.1, Volcano v1.16.0 39.4, Kueue v0.20.2 34.1, the KAI scheduler v0.18.6 20.1, Koordinator 1.8.0 32.6

### climb, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 423.4 | 423.4, STEADY 0.0% | 423.4, STEADY 0.0% | 423.4, STEADY 0.0% | 423.4, STEADY 0.0% | 423.4, STEADY 0.0% |
| minutes over the line (500 ms) | 3.2 | 3.2, STEADY 0.0% | 3.2, STEADY 0.0% | 3.2, STEADY 0.0% | 3.2, STEADY 0.0% | 3.2, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 48,567 | 48,567, STEADY 0.0% | 48,567, STEADY 0.0% | 48,567, STEADY 0.0% | 48,567, STEADY 0.0% | 48,567, STEADY 0.0% |
| machine-hours | 3.000 | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% |
| energy | 0.027 | 0.027, STEADY 0.0% | 0.027, STEADY 0.0% | 0.027, STEADY 0.0% | 0.027, STEADY 0.0% | 0.027, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN 19.4% (raw −21.4% to −17.5%) | GAIN 19.4% (raw −21.4% to −17.5%) | GAIN 19.4% (raw −21.4% to −17.5%) | GAIN 19.4% (raw −21.4% to −17.5%) | GAIN 5.9% (raw −7.1% to −4.8%) | GAIN 19.4% (raw −21.4% to −17.5%) |
| minutes over the line (500 ms) | GAIN 7.7% (raw −19.6% to +4.2%) | GAIN 7.7% (raw −19.6% to +4.2%) | GAIN 7.7% (raw −19.6% to +4.2%) | GAIN 7.7% (raw −19.6% to +4.2%) | GAIN 3.9% (raw −12.9% to +5.2%) | GAIN 7.7% (raw −19.6% to +4.2%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 15.1, the Kubernetes scheduler's bin-packing profile 15.1, Volcano v1.16.0 17.4, Kueue v0.20.2 15.1, the KAI scheduler v0.18.6 16.1, Koordinator 1.8.0 14.2

### burst_1419, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 10,000.0 | 10,000.0, STEADY 0.0% | 10,000.0, STEADY 0.0% | 10,000.0, STEADY 0.0% | 10,000.0, STEADY 0.0% | 10,000.0, STEADY 0.0% |
| minutes over the line (500 ms) | 6.0 | 6.0, STEADY 0.0% | 6.0, STEADY 0.0% | 6.0, STEADY 0.0% | 6.0, STEADY 0.0% | 6.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 736 | 736, STEADY 0.0% | 736, STEADY 0.0% | 736, STEADY 0.0% | 736, STEADY 0.0% | 736, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 38,406 | 38,406, STEADY 0.0% | 38,406, STEADY 0.0% | 38,406, STEADY 0.0% | 38,406, STEADY 0.0% | 38,406, STEADY 0.0% |
| machine-hours | 3.000 | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% |
| energy | 0.025 | 0.025, STEADY 0.0% | 0.025, STEADY 0.0% | 0.025, STEADY 0.0% | 0.025, STEADY 0.0% | 0.025, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | GAIN 2.1% (raw −7.0% to +2.8%) | GAIN 2.1% (raw −7.0% to +2.8%) | GAIN 2.1% (raw −7.0% to +2.8%) | GAIN 2.1% (raw −7.0% to +2.8%) | GAIN 2.1% (raw −7.0% to +2.8%) | GAIN 2.1% (raw −7.0% to +2.8%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 20.4, the Kubernetes scheduler's bin-packing profile 20.4, Volcano v1.16.0 22.4, Kueue v0.20.2 20.4, the KAI scheduler v0.18.6 13.8, Koordinator 1.8.0 19.0

### burst_1618, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 1,116.6 | 1,116.6, STEADY 0.0% | 1,116.6, STEADY 0.0% | 1,116.6, STEADY 0.0% | 1,116.6, STEADY 0.0% | 1,116.6, STEADY 0.0% |
| minutes over the line (500 ms) | 7.0 | 7.0, STEADY 0.0% | 7.0, STEADY 0.0% | 7.0, STEADY 0.0% | 7.0, STEADY 0.0% | 7.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 41,355 | 41,355, STEADY 0.0% | 41,355, STEADY 0.0% | 41,355, STEADY 0.0% | 41,355, STEADY 0.0% | 41,355, STEADY 0.0% |
| machine-hours | 3.000 | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% |
| energy | 0.025 | 0.025, STEADY 0.0% | 0.025, STEADY 0.0% | 0.025, STEADY 0.0% | 0.025, STEADY 0.0% | 0.025, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN 19.4% (raw −21.7% to −17.1%) | GAIN 19.4% (raw −21.7% to −17.1%) | GAIN 19.4% (raw −21.7% to −17.1%) | GAIN 19.4% (raw −21.7% to −17.1%) | GAIN 14.1% (raw −16.0% to −12.1%) | GAIN 19.4% (raw −21.7% to −17.1%) |
| minutes over the line (500 ms) | GAIN 17.9% (raw −23.4% to −12.3%) | GAIN 17.9% (raw −23.4% to −12.3%) | GAIN 17.9% (raw −23.4% to −12.3%) | GAIN 17.9% (raw −23.4% to −12.3%) | GAIN 17.9% (raw −23.4% to −12.3%) | GAIN 17.9% (raw −23.4% to −12.3%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 20.4, the Kubernetes scheduler's bin-packing profile 20.4, Volcano v1.16.0 20.8, Kueue v0.20.2 20.4, the KAI scheduler v0.18.6 14.5, Koordinator 1.8.0 19.0

### real_day, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 237.5 | 237.5, STEADY 0.0% | 237.5, STEADY 0.0% | 237.5, STEADY 0.0% | 237.5, STEADY 0.0% | 237.5, STEADY 0.0% |
| minutes over the line (500 ms) | 1.1 | 1.1, STEADY 0.0% | 1.1, STEADY 0.0% | 1.1, STEADY 0.0% | 1.1, STEADY 0.0% | 1.1, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 8 | 8, STEADY 0.0% | 8, STEADY 0.0% | 8, STEADY 0.0% | 8, STEADY 0.0% | 8, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 55,726 | 55,726, STEADY 0.0% | 55,726, STEADY 0.0% | 55,726, STEADY 0.0% | 55,726, STEADY 0.0% | 55,726, STEADY 0.0% |
| machine-hours | 4.325 | 4.325, STEADY 0.0% | 4.325, STEADY 0.0% | 4.325, STEADY 0.0% | 4.325, STEADY 0.0% | 4.325, STEADY 0.0% |
| energy | 0.036 | 0.036, STEADY 0.0% | 0.036, STEADY 0.0% | 0.036, STEADY 0.0% | 0.036, STEADY 0.0% | 0.036, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN 37.5% (raw −38.3% to −36.7%) | GAIN 37.5% (raw −38.3% to −36.7%) | GAIN 37.5% (raw −38.3% to −36.7%) | GAIN 37.5% (raw −38.3% to −36.7%) | GAIN 1.7% (raw −2.0% to −1.4%) | GAIN 37.5% (raw −38.3% to −36.7%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | GAIN 100.0% (raw −159.7% to −40.3%) | GAIN 100.0% (raw −159.7% to −40.3%) | GAIN 100.0% (raw −159.7% to −40.3%) | GAIN 100.0% (raw −159.7% to −40.3%) | GAIN 100.0% (raw −159.7% to −40.3%) | GAIN 100.0% (raw −159.7% to −40.3%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) | STEADY 0.0% (raw +0.0% to +0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) | STEADY 0.0% (raw ±0.0% to +0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 36.8, the Kubernetes scheduler's bin-packing profile 36.8, Volcano v1.16.0 46.0, Kueue v0.20.2 36.8, the KAI scheduler v0.18.6 21.8, Koordinator 1.8.0 34.8

### fairness, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 301.6 | 301.6, STEADY 0.0% | 301.6, STEADY 0.0% | 301.6, STEADY 0.0% | 301.6, STEADY 0.0% | 301.6, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 18,003 | 18,003, STEADY 0.0% | 18,003, STEADY 0.0% | 18,003, STEADY 0.0% | 18,003, STEADY 0.0% | 18,003, STEADY 0.0% |
| machine-hours | 1.500 | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% |
| energy | 0.012 | 0.012, STEADY 0.0% | 0.012, STEADY 0.0% | 0.012, STEADY 0.0% | 0.012, STEADY 0.0% | 0.012, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN 11.9% (raw −13.3% to −10.4%) | GAIN 11.9% (raw −13.3% to −10.4%) | GAIN 11.9% (raw −13.3% to −10.4%) | GAIN 11.9% (raw −13.3% to −10.4%) | GAIN 3.1% (raw −3.7% to −2.4%) | GAIN 11.9% (raw −13.3% to −10.4%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 25.0, the Kubernetes scheduler's bin-packing profile 19.6, Volcano v1.16.0 25.8, Kueue v0.20.2 25.0, the KAI scheduler v0.18.6 3.0, Koordinator 1.8.0 22.4

### faults, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 7,612.4 | 7,612.4, STEADY 0.0% | 7,612.4, STEADY 0.0% | 7,612.4, STEADY 0.0% | 7,612.4, STEADY 0.0% | 7,612.4, STEADY 0.0% |
| minutes over the line (500 ms) | 4.0 | 4.0, STEADY 0.0% | 4.0, STEADY 0.0% | 4.0, STEADY 0.0% | 4.0, STEADY 0.0% | 4.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 32 | 32, STEADY 0.0% | 32, STEADY 0.0% | 32, STEADY 0.0% | 32, STEADY 0.0% | 32, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 13,320 | 13,320, STEADY 0.0% | 13,320, STEADY 0.0% | 13,320, STEADY 0.0% | 13,320, STEADY 0.0% | 13,320, STEADY 0.0% |
| machine-hours | 1.467 | 1.467, STEADY 0.0% | 1.467, STEADY 0.0% | 1.467, STEADY 0.0% | 1.467, STEADY 0.0% | 1.467, STEADY 0.0% |
| energy | 0.011 | 0.011, STEADY 0.0% | 0.011, STEADY 0.0% | 0.011, STEADY 0.0% | 0.011, STEADY 0.0% | 0.011, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | GAIN 0.8% (raw −0.9% to −0.7%) | GAIN 0.8% (raw −0.9% to −0.7%) | GAIN 0.8% (raw −0.9% to −0.7%) | GAIN 0.8% (raw −0.9% to −0.7%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | GAIN 0.8% (raw −0.9% to −0.7%) |
| minutes over the line (500 ms) | GAIN 6.2% (raw −15.9% to +3.4%) | GAIN 6.2% (raw −15.9% to +3.4%) | GAIN 6.2% (raw −15.9% to +3.4%) | GAIN 6.2% (raw −15.9% to +3.4%) | GAIN 6.2% (raw −15.9% to +3.4%) | GAIN 6.2% (raw −15.9% to +3.4%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 16.1, the Kubernetes scheduler's bin-packing profile 16.1, Volcano v1.16.0 21.5, Kueue v0.20.2 16.1, the KAI scheduler v0.18.6 17.8, Koordinator 1.8.0 14.9

### batch, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| a job's turnaround | 69.0 | 69.0, STEADY 0.0% | 69.0, STEADY 0.0% | 74.0, LOSS 7.2% | 69.0, STEADY 0.0% | 69.0, STEADY 0.0% |
| the stream's makespan (first job in to last job done) | 747.5 | 747.5, STEADY 0.0% | 747.5, STEADY 0.0% | 752.5, LOSS 0.7% | 747.5, STEADY 0.0% | 747.5, STEADY 0.0% |
| batch pods done | 240 | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% |
| machine-hours | 2.500 | 2.500, STEADY 0.0% | 2.500, STEADY 0.0% | 2.500, STEADY 0.0% | 2.500, STEADY 0.0% | 2.500, STEADY 0.0% |
| energy | 0.022 | 0.022, STEADY 0.0% | 0.022, STEADY 0.0% | 0.022, STEADY 0.0% | 0.022, STEADY 0.0% | 0.022, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| a job's turnaround | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| the stream's makespan (first job in to last job done) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| batch pods done | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 6.5, the Kubernetes scheduler's bin-packing profile 6.8, Volcano v1.16.0 6.6, Kueue v0.20.2 6.5, the KAI scheduler v0.18.6 3.5, Koordinator 1.8.0 6.8

### one_body, on-site

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 10,000.0 | 10,000.0, STEADY 0.0% | 10,000.0, STEADY 0.0% | 10,000.0, STEADY 0.0% | 10,000.0, STEADY 0.0% | 412.3, GAIN 95.9% |
| minutes over the line (500 ms) | 16.2 | 16.2, STEADY 0.0% | 16.2, STEADY 0.0% | 16.2, STEADY 0.0% | 16.2, STEADY 0.0% | 3.2, GAIN 80.0% |
| requests failed (unanswered in 10 s) | 7,928 | 7,928, STEADY 0.0% | 7,928, STEADY 0.0% | 8,155, LOSS 2.9% | 7,928, STEADY 0.0% | 0, GAIN 100.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 199.8, LOSS 100.0% |
| a job's turnaround | 141.0 | 141.0, STEADY 0.0% | 141.0, STEADY 0.0% | 141.9, LOSS 0.6% | 141.0, STEADY 0.0% | 316.0, LOSS 124.0% |
| the stream's makespan (first job in to last job done) | 801.2 | 801.2, STEADY 0.0% | 801.2, STEADY 0.0% | 803.1, STEADY 0.2% | 801.2, STEADY 0.0% | 1,175.6, LOSS 46.7% |
| batch pods done | 240 | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% |
| requests served | 40,620 | 40,620, STEADY 0.0% | 40,620, STEADY 0.0% | 40,394, LOSS 0.6% | 40,620, STEADY 0.0% | 48,548, GAIN 19.5% |
| machine-hours | 3.000 | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% | 3.000, STEADY 0.0% |
| energy | 0.034 | 0.034, STEADY 0.0% | 0.034, STEADY 0.0% | 0.034, STEADY 0.1% | 0.034, STEADY 0.0% | 0.036, power given 5.5% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | GAIN 19.2% (raw −21.7% to −16.8%) |
| minutes over the line (500 ms) | GAIN 0.8% (raw −2.6% to +1.1%) | GAIN 0.8% (raw −2.6% to +1.1%) | GAIN 0.8% (raw −2.6% to +1.1%) | GAIN 0.8% (raw −2.6% to +1.1%) | GAIN 0.8% (raw −2.6% to +1.1%) | GAIN 3.9% (raw −12.9% to +5.2%) |
| requests failed (unanswered in 10 s) | GAIN 6.5% (raw −8.6% to −4.5%) | GAIN 6.5% (raw −8.6% to −4.5%) | GAIN 6.5% (raw −8.6% to −4.5%) | GAIN 9.2% (raw −10.3% to −8.1%) | GAIN 6.5% (raw −8.6% to −4.5%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| a job's turnaround | LOSS 9.3% (raw +6.6% to +11.9%) | LOSS 9.3% (raw +6.6% to +11.9%) | LOSS 9.3% (raw +6.6% to +11.9%) | LOSS 12.7% (raw +10.9% to +14.6%) | LOSS 9.3% (raw +6.6% to +12.1%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| the stream's makespan (first job in to last job done) | LOSS 2.0% (raw +1.4% to +2.7%) | LOSS 2.0% (raw +1.4% to +2.7%) | LOSS 2.0% (raw +1.4% to +2.7%) | LOSS 2.8% (raw +2.4% to +3.2%) | LOSS 2.0% (raw +1.4% to +2.7%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| batch pods done | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | GAIN 1.3% (raw +0.9% to +1.7%) | GAIN 1.3% (raw +0.9% to +1.7%) | GAIN 1.3% (raw +0.9% to +1.7%) | GAIN 1.9% (raw +1.6% to +2.1%) | GAIN 1.3% (raw +0.9% to +1.7%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.3% (raw +0.2% to +0.4%) | STEADY 0.3% (raw +0.2% to +0.4%) | STEADY 0.3% (raw +0.2% to +0.4%) | STEADY 0.4% (raw +0.3% to +0.4%) | STEADY 0.3% (raw +0.2% to +0.4%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 44.1, the Kubernetes scheduler's bin-packing profile 43.6, Volcano v1.16.0 44.2, Kueue v0.20.2 60.9, the KAI scheduler v0.18.6 25.1, Koordinator 1.8.0 19.2

### steady, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 202.1 | 202.1, STEADY 0.0% | 202.6, STEADY 0.2% | 202.1, STEADY 0.0% | 216.1, LOSS 6.9% | 202.1, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 8,992 | 8,992, STEADY 0.0% | 8,992, STEADY 0.0% | 8,992, STEADY 0.0% | 8,992, STEADY 0.0% | 8,992, STEADY 0.0% |
| machine-hours | 0.500 | 0.500, STEADY 0.0% | 0.500, STEADY 0.0% | 0.500, STEADY 0.0% | 0.500, STEADY 0.0% | 0.500, STEADY 0.0% |
| energy | 0.036 | 0.036, STEADY 0.0% | 0.036, STEADY 0.2% | 0.036, STEADY 0.0% | 0.039, power given 7.0% | 0.036, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 1.0, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 1.0, Koordinator 1.8.0 1.0

### wandering, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 205.0 | 205.0, STEADY 0.0% | 223.4, LOSS 9.0% | 205.0, STEADY 0.0% | 9,532.2, LOSS 4549.9% | 205.0, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.5, LOSS 50.0% | 1.0, STEADY 0.0% | 10.9, LOSS 987.5% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 377, LOSS 100.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 64,156 | 64,156, STEADY 0.0% | 64,156, STEADY 0.0% | 64,156, STEADY 0.0% | 63,779, LOSS 0.6% | 64,156, STEADY 0.0% |
| machine-hours | 1.500 | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% |
| energy | 0.133 | 0.133, STEADY 0.0% | 0.133, STEADY 0.0% | 0.133, STEADY 0.0% | 0.134, power given 1.0% | 0.133, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 1.5, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 10.4, Koordinator 1.8.0 1.0

### all_four, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 208.3 | 208.3, STEADY 0.0% | 212.0, LOSS 1.7% | 208.3, STEADY 0.0% | 10,000.0, LOSS 4700.0% | 208.3, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 14.1, LOSS 1312.5% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 875, LOSS 100.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 69,069 | 69,069, STEADY 0.0% | 69,069, STEADY 0.0% | 69,069, STEADY 0.0% | 68,194, LOSS 1.3% | 69,069, STEADY 0.0% |
| machine-hours | 1.500 | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% | 1.500, STEADY 0.0% |
| energy | 0.136 | 0.136, STEADY 0.0% | 0.136, STEADY 0.1% | 0.136, STEADY 0.0% | 0.138, power given 1.1% | 0.136, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 1.0, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 13.9, Koordinator 1.8.0 1.0

### google_2011, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 196.5 | 196.5, STEADY 0.0% | 198.9, LOSS 1.2% | 196.5, STEADY 0.0% | 261.9, LOSS 33.3% | 196.6, STEADY 0.1% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 2.0, LOSS 100.0% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 10 | 10, STEADY 0.0% | 10, STEADY 0.0% | 10, STEADY 0.0% | 10, STEADY 0.0% | 10, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 50,681 | 50,681, STEADY 0.0% | 50,681, STEADY 0.0% | 50,681, STEADY 0.0% | 50,681, STEADY 0.0% | 50,681, STEADY 0.0% |
| machine-hours | 1.442 | 1.442, STEADY 0.0% | 1.442, STEADY 0.0% | 1.442, STEADY 0.0% | 1.442, STEADY 0.0% | 1.442, STEADY 0.0% |
| energy | 0.120 | 0.120, STEADY 0.0% | 0.120, STEADY 0.0% | 0.120, STEADY 0.0% | 0.121, STEADY 0.1% | 0.120, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 1.0, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 1.9, Koordinator 1.8.0 1.0

### climb, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 213.3 | 213.3, STEADY 0.0% | 245.9, LOSS 15.3% | 213.3, STEADY 0.0% | 5,068.5, LOSS 2276.6% | 213.3, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.2, LOSS 25.0% | 1.0, STEADY 0.0% | 9.8, LOSS 875.0% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 291, LOSS 100.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 48,619 | 48,619, STEADY 0.0% | 48,619, STEADY 0.0% | 48,619, STEADY 0.0% | 47,911, LOSS 1.5% | 48,619, STEADY 0.0% |
| machine-hours | 1.000 | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% |
| energy | 0.093 | 0.093, STEADY 0.0% | 0.093, STEADY 0.0% | 0.093, STEADY 0.0% | 0.093, STEADY 0.4% | 0.093, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 1.2, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 9.4, Koordinator 1.8.0 1.0

### burst_1419, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 242.2 | 242.2, STEADY 0.0% | 2,712.7, LOSS 1020.0% | 242.2, STEADY 0.0% | 10,000.0, LOSS 4028.6% | 242.2, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 2.8, LOSS 175.0% | 1.0, STEADY 0.0% | 8.5, LOSS 750.0% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 196, LOSS 100.0% | 0, STEADY 0.0% | 3,316, LOSS 100.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 39,606 | 39,606, STEADY 0.0% | 39,287, LOSS 0.8% | 39,606, STEADY 0.0% | 35,873, LOSS 9.4% | 39,606, STEADY 0.0% |
| machine-hours | 1.000 | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% |
| energy | 0.087 | 0.087, STEADY 0.0% | 0.086, STEADY 0.2% | 0.087, STEADY 0.0% | 0.086, GAIN 0.9% | 0.087, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 2.8, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 8.4, Koordinator 1.8.0 1.0

### burst_1618, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 228.5 | 228.5, STEADY 0.0% | 254.7, LOSS 11.4% | 228.5, STEADY 0.0% | 10,000.0, LOSS 4275.5% | 228.5, STEADY 0.0% |
| minutes over the line (500 ms) | 1.9 | 1.9, STEADY 0.0% | 1.9, STEADY 0.0% | 1.9, STEADY 0.0% | 12.6, LOSS 573.3% | 1.9, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 1,533, LOSS 100.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.1, LOSS 100.0% |
| requests served | 41,424 | 41,424, STEADY 0.0% | 41,424, STEADY 0.0% | 41,424, STEADY 0.0% | 39,892, LOSS 3.7% | 41,424, STEADY 0.0% |
| machine-hours | 1.000 | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% | 1.000, STEADY 0.0% | 1.248, power given 24.8% |
| energy | 0.088 | 0.088, STEADY 0.0% | 0.088, STEADY 0.1% | 0.088, STEADY 0.0% | 0.088, power given 0.9% | 0.110, power given 25.1% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.9, the Kubernetes scheduler's bin-packing profile 1.9, Volcano v1.16.0 1.9, Kueue v0.20.2 1.9, the KAI scheduler v0.18.6 12.4, Koordinator 1.8.0 1.9

### real_day, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 199.7 | 199.7, STEADY 0.0% | 207.7, LOSS 4.0% | 199.7, STEADY 0.0% | 951.4, LOSS 376.3% | 199.8, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 4.2, LOSS 325.0% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 7 | 7, STEADY 0.0% | 7, STEADY 0.0% | 7, STEADY 0.0% | 7, STEADY 0.0% | 7, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 55,766 | 55,766, STEADY 0.0% | 55,766, STEADY 0.0% | 55,766, STEADY 0.0% | 55,766, STEADY 0.0% | 55,766, STEADY 0.0% |
| machine-hours | 1.442 | 1.442, STEADY 0.0% | 1.442, STEADY 0.0% | 1.442, STEADY 0.0% | 1.442, STEADY 0.0% | 1.442, STEADY 0.0% |
| energy | 0.124 | 0.124, STEADY 0.0% | 0.124, STEADY 0.0% | 0.124, STEADY 0.0% | 0.124, STEADY 0.1% | 0.124, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 1.0, the Kubernetes scheduler's bin-packing profile 1.0, Volcano v1.16.0 1.0, Kueue v0.20.2 1.0, the KAI scheduler v0.18.6 4.2, Koordinator 1.8.0 1.0

### fairness, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 227.5 | 227.5, STEADY 0.0% | 231.7, LOSS 1.9% | 227.5, STEADY 0.0% | 263.1, LOSS 15.7% | 227.5, STEADY 0.0% |
| minutes over the line (500 ms) | 1.0 | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% | 1.0, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 3.3 | 3.3, STEADY 0.0% | 3.3, STEADY 0.0% | 3.3, STEADY 0.0% | 3.3, STEADY 0.0% | 3.3, STEADY 0.0% |
| requests served | 18,000 | 18,000, STEADY 0.0% | 18,000, STEADY 0.0% | 18,000, STEADY 0.0% | 18,000, STEADY 0.0% | 18,000, STEADY 0.0% |
| machine-hours | 0.797 | 0.797, STEADY 0.0% | 0.797, STEADY 0.0% | 0.797, STEADY 0.0% | 0.797, STEADY 0.0% | 0.797, STEADY 0.0% |
| energy | 0.064 | 0.064, STEADY 0.0% | 0.064, STEADY 0.3% | 0.064, STEADY 0.0% | 0.065, power given 2.2% | 0.064, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 7.0, the Kubernetes scheduler's bin-packing profile 7.0, Volcano v1.16.0 7.0, Kueue v0.20.2 7.0, the KAI scheduler v0.18.6 7.0, Koordinator 1.8.0 7.0

### faults, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 8,633.8 | 8,633.8, STEADY 0.0% | 9,910.2, LOSS 14.8% | 8,633.8, STEADY 0.0% | 10,000.0, LOSS 15.8% | 8,633.8, STEADY 0.0% |
| minutes over the line (500 ms) | 3.9 | 3.9, STEADY 0.0% | 4.0, LOSS 3.2% | 3.9, STEADY 0.0% | 4.0, LOSS 3.2% | 3.9, STEADY 0.0% |
| requests failed (unanswered in 10 s) | 126 | 126, STEADY 0.0% | 885, LOSS 599.9% | 126, STEADY 0.0% | 1,135, LOSS 797.6% | 126, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 0.0 | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% | 0.0, STEADY 0.0% |
| requests served | 13,187 | 13,187, STEADY 0.0% | 12,428, LOSS 5.8% | 13,187, STEADY 0.0% | 12,178, LOSS 7.7% | 13,187, STEADY 0.0% |
| machine-hours | 0.467 | 0.467, STEADY 0.0% | 0.467, STEADY 0.0% | 0.467, STEADY 0.0% | 0.467, STEADY 0.0% | 0.467, STEADY 0.0% |
| energy | 0.039 | 0.039, STEADY 0.0% | 0.039, GAIN 0.6% | 0.039, STEADY 0.0% | 0.039, STEADY 0.5% | 0.039, STEADY 0.0% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 5.9, the Kubernetes scheduler's bin-packing profile 5.9, Volcano v1.16.0 6.0, Kueue v0.20.2 5.9, the KAI scheduler v0.18.6 6.0, Koordinator 1.8.0 5.9

### batch, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | 7.3 | 7.3, STEADY 0.0% | 5.1, GAIN 30.0% | 8.0, LOSS 9.1% | 5.3, GAIN 28.0% | 32.8, LOSS 347.7% |
| a job's turnaround | 42.7 | 42.7, STEADY 0.0% | 42.1, GAIN 1.4% | 48.3, LOSS 13.2% | 46.8, LOSS 9.6% | 60.7, LOSS 42.2% |
| the stream's makespan (first job in to last job done) | 725.0 | 725.0, STEADY 0.0% | 725.6, STEADY 0.1% | 730.0, LOSS 0.7% | 731.2, LOSS 0.9% | 726.9, STEADY 0.3% |
| batch pods done | 240 | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% |
| machine-hours | 2.564 | 2.564, STEADY 0.0% | 2.222, GAIN 13.3% | 2.564, STEADY 0.0% | 2.222, GAIN 13.3% | 3.356, power given 30.9% |
| energy | 0.200 | 0.201, power given 0.8% | 0.177, GAIN 11.3% | 0.199, GAIN 0.6% | 0.193, GAIN 3.6% | 0.252, power given 26.2% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| a job's turnaround | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| the stream's makespan (first job in to last job done) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| batch pods done | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 29.0, the Kubernetes scheduler's bin-packing profile 29.0, Volcano v1.16.0 28.1, Kueue v0.20.2 27.0, the KAI scheduler v0.18.6 28.2, Koordinator 1.8.0 11.0

### one_body, cloud

Each orchestrator against Kubernetes alone (its mean, then its reading):

| Gauge | native (mean) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---:|---|---|---|---|---|
| the 95th percentile response time | 215.0 | 214.4, STEADY 0.3% | 222.0, LOSS 3.3% | 214.9, STEADY 0.1% | 426.1, LOSS 98.2% | 233.1, LOSS 8.4% |
| minutes over the line (500 ms) | 1.4 | 1.0, GAIN 27.3% | 1.1, GAIN 18.2% | 1.1, GAIN 18.2% | 2.6, LOSS 90.9% | 1.9, LOSS 36.4% |
| requests failed (unanswered in 10 s) | 0 | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% | 0, STEADY 0.0% |
| pods waiting for a place (pod-minutes) | 7.8 | 15.3, LOSS 96.9% | 11.9, LOSS 53.3% | 9.9, LOSS 27.2% | 16.3, LOSS 110.2% | 47.8, LOSS 515.6% |
| a job's turnaround | 42.2 | 45.7, LOSS 8.2% | 46.8, LOSS 10.8% | 48.4, LOSS 14.6% | 53.6, LOSS 27.0% | 67.0, LOSS 58.6% |
| the stream's makespan (first job in to last job done) | 725.0 | 725.0, STEADY 0.0% | 728.1, STEADY 0.4% | 730.0, LOSS 0.7% | 735.6, LOSS 1.5% | 725.6, STEADY 0.1% |
| batch pods done | 240 | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% | 240, STEADY 0.0% |
| requests served | 48,615 | 48,615, STEADY 0.0% | 48,615, STEADY 0.0% | 48,615, STEADY 0.0% | 48,613, STEADY 0.0% | 48,615, STEADY 0.0% |
| machine-hours | 2.602 | 3.383, power given 30.0% | 3.027, power given 16.3% | 2.602, STEADY 0.0% | 3.572, power given 37.3% | 3.522, power given 35.3% |
| energy | 0.232 | 0.302, power given 30.1% | 0.271, power given 16.8% | 0.232, STEADY 0.1% | 0.347, power given 49.7% | 0.295, power given 27.2% |

Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):

| Gauge | the Kubernetes scheduler as shipped (the organism alone) | the Kubernetes scheduler's bin-packing profile | Volcano v1.16.0 | Kueue v0.20.2 | the KAI scheduler v0.18.6 | Koordinator 1.8.0 |
|---|---|---|---|---|---|---|
| the 95th percentile response time | STEADY 0.1% (raw +0.0% to +0.2%) | STEADY 0.1% (raw −0.0% to +0.2%) | STEADY 0.0% (raw −0.0% to +0.1%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| minutes over the line (500 ms) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests failed (unanswered in 10 s) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| pods waiting for a place (pod-minutes) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| a job's turnaround | STEADY 0.2% (raw −0.0% to +0.4%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | LOSS 0.7% (raw −0.3% to +1.7%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.1% (raw −0.1% to +0.3%) |
| the stream's makespan (first job in to last job done) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.1% (raw −0.3% to +0.1%) |
| batch pods done | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| requests served | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| machine-hours | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) |
| energy | power given 1.8% (raw +1.4% to +2.2%) | power given 1.0% (raw +0.8% to +1.3%) | STEADY 0.4% (raw +0.1% to +0.7%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw ±0.0% to ±0.0%) | STEADY 0.0% (raw −0.1% to +0.1%) |

Omni-Compass's writes a run (mean): the Kubernetes scheduler as shipped (the organism alone) 12.9, the Kubernetes scheduler's bin-packing profile 12.8, Volcano v1.16.0 17.8, Kueue v0.20.2 20.1, the KAI scheduler v0.18.6 16.6, Koordinator 1.8.0 15.2

## What the model leaves out

The processor alone is modelled (memory, disks and the network are not); a request's cost, the clients' rate and the pod start times are the rig's own calibration (the model gate's); every orchestrator's rule is written from its release and documentation, never from its code, and each is listed above with the file it was read from. The Gödel scheduler, KubeRay, Crane and the multi-cluster orchestrators (Karmada, Open Cluster Management, Armada) run on GitHub's machines four ways (`results/live/GOVERNORS.md`); their rules join this model once each one's shipped default is read from its release, and nothing is written for them here before that.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
