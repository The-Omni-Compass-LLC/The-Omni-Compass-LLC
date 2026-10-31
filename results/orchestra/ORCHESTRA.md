# The orchestra, the eighth organism: the governors' muscles, native and with Omni-Compass on top (modelled)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

The founder's word of 19 October, night: the governors and orchestrators in a catalog group, an organism of their own, benchmarked native and then with Omni-Compass on top of them. Every catalog muscle that stands for a knob of a governor or orchestrator he named (the mapping on the governors page, `tools/governors_page.py`) runs in the modelled organisms as the seven do (`tools/run_realms_v5.py`): each governor's muscles as a body of its own, and all of them together as one body, the orchestra (55 muscles). Native is each muscle's own native controller in the catalog, the governor's rule as modelled; omni is Omni-Compass on top at the max, on omni-v12 (digest d38b58fbe28939b85919c04b876e7c72edd1f77515dde92b75dfd897e4ebe12d), commit `49bf9644184d`, seeds 3000-3009 (10 paired seeds per body and load).

These are models (evidence class S): a model's energy is not a meter's, and a plant written by the people who wrote the law is not an independent test. The governors' live results, each on a real Kubernetes cluster with the governor as shipped and Omni-Compass on top (class L), stand on the governors page (`results/live/GOVERNORS.md`).

## The organism's own load

Work: the mean over the body's plants of each plant's work against native's. Misses: the plants' decisions over their own line, native → omni. Power given: the body's energy against native's. Wear: shown, never judged. 95% intervals over seeds.

| Body | Muscles | Reading | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Valid |
|---|---:|---|---:|---|---:|---:|---:|---|
| The Kubernetes scheduler (vanilla, and its bin-packing profile) | 12 | **GAIN (fewer misses)** | +0.00% (-0.00 to +0.00) | 1.80% → 0.95% (−47.0%) | -0.84 (-1.10 to -0.59) | +17.26% (+15.12 to +19.39) | +40.77% | yes |
| Kueue | 5 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 1.75% → 1.75% (−0.0%) | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% | yes |
| Volcano | 5 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +9.06% (+7.72 to +10.40) | +25.43% | yes |
| KAI scheduler | 4 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +5.63% (+2.99 to +8.27) | +19.05% | yes |
| Koordinator | 4 | **STEADY (the same as native)** | -0.00% (-0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +22.55% (+19.23 to +25.86) | +50.09% | yes |
| CruiseKube | 4 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 1.30% → 0.25% (−80.8%) | -1.05 (-1.79 to -0.32) | +23.45% (+19.28 to +27.63) | +50.56% | yes |
| Crane | 5 | **GAIN (fewer misses)** | +0.01% (-0.02 to +0.04) | 1.72% → 0.41% (−76.2%) | -1.31 (-1.67 to -0.95) | +28.26% (+24.26 to +32.27) | +61.29% | yes |
| KubeRay | 3 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +12.50% (+10.82 to +14.17) | +39.54% | yes |
| Gödel scheduler | 4 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +19.22% (+16.81 to +21.62) | +44.73% | yes |
| Armada | 3 | **GAIN (fewer misses)** | +0.11% (-0.02 to +0.23) | 5.43% → 3.42% (−37.1%) | -2.01 (-2.89 to -1.14) | +21.65% (+16.06 to +27.25) | +55.52% | yes |
| Karmada | 4 | **GAIN (more work + fewer misses)** | +0.30% (+0.04 to +0.56) | 4.97% → 0.62% (−87.4%) | -4.34 (-5.26 to -3.43) | +79.81% (+64.97 to +94.66) | +154.79% | yes |
| Open Cluster Management | 3 | **GAIN (more work + fewer misses)** | +0.20% (+0.04 to +0.35) | 6.00% → 2.81% (−53.2%) | -3.19 (-4.35 to -2.04) | +56.28% (+42.63 to +69.92) | +106.62% | yes |
| KubeEdge | 4 | **GAIN (fewer misses)** | +0.08% (-0.06 to +0.23) | 3.39% → 0.55% (−83.7%) | -2.83 (-3.82 to -1.85) | +63.37% (+52.92 to +73.82) | +118.55% | yes |
| Nephio | 4 | **GAIN (fewer misses)** | +0.01% (-0.00 to +0.03) | 2.16% → 1.53% (−29.0%) | -0.63 (-0.89 to -0.36) | +7.11% (+5.03 to +9.19) | +12.94% | yes |
| **The orchestra, every governor's muscle once** | 55 | **GAIN (more work + fewer misses)** | +0.04% (+0.02 to +0.05) | 1.82% → 0.81% (−55.5%) | -1.01 (-1.12 to -0.90) | +25.39% (+23.29 to +27.48) | +49.88% | yes |

## The climb (1 2 3 2 3 4 ..., level 4 = own load, 8 = twice it)

Work: the mean over the body's plants of each plant's work against native's. Misses: the plants' decisions over their own line, native → omni. Power given: the body's energy against native's. Wear: shown, never judged. 95% intervals over seeds.

| Body | Muscles | Reading | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Valid |
|---|---:|---|---:|---|---:|---:|---:|---|
| The Kubernetes scheduler (vanilla, and its bin-packing profile) | 12 | **GAIN (fewer misses)** | +0.02% (-0.01 to +0.05) | 3.05% → 1.43% (−53.2%) | -1.62 (-2.02 to -1.23) | +36.02% (+31.52 to +40.53) | +79.99% | yes |
| Kueue | 5 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 2.67% → 2.67% (−0.0%) | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% | yes |
| Volcano | 5 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +18.87% (+14.93 to +22.80) | +53.19% | yes |
| KAI scheduler | 4 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +13.16% (+7.23 to +19.08) | +44.18% | yes |
| Koordinator | 4 | **STEADY (the same as native)** | +0.00% (-0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +50.53% (+46.65 to +54.42) | +107.00% | yes |
| CruiseKube | 4 | **GAIN (fewer misses)** | +0.02% (-0.03 to +0.07) | 3.14% → 0.20% (−93.7%) | -2.94 (-3.72 to -2.16) | +53.96% (+47.41 to +60.52) | +112.55% | yes |
| Crane | 5 | **GAIN (fewer misses)** | +0.06% (-0.03 to +0.15) | 3.40% → 0.47% (−86.3%) | -2.93 (-3.40 to -2.47) | +60.76% (+52.39 to +69.12) | +127.37% | yes |
| KubeRay | 3 | **STEADY (the same as native)** | -0.00% (-0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +36.72% (+32.22 to +41.22) | +107.73% | yes |
| Gödel scheduler | 4 | **STEADY (the same as native)** | +0.00% (-0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +39.64% (+32.01 to +47.28) | +90.70% | yes |
| Armada | 3 | **GAIN (more work + fewer misses)** | +0.45% (+0.02 to +0.88) | 7.47% → 5.24% (−29.9%) | -2.24 (-2.95 to -1.52) | +54.44% (+41.27 to +67.61) | +129.09% | yes |
| Karmada | 4 | **GAIN (more work + fewer misses)** | +0.97% (+0.47 to +1.47) | 7.32% → 0.02% (−99.7%) | -7.30 (-8.90 to -5.70) | +178.95% (+159.44 to +198.45) | +324.14% | yes |
| Open Cluster Management | 3 | **GAIN (more work + fewer misses)** | +0.89% (+0.36 to +1.42) | 7.92% → 3.15% (−60.2%) | -4.76 (-5.96 to -3.57) | +114.99% (+96.46 to +133.53) | +213.67% | yes |
| KubeEdge | 4 | **GAIN (more work + fewer misses)** | +0.39% (+0.23 to +0.56) | 5.93% → 0.04% (−99.3%) | -5.89 (-7.37 to -4.40) | +129.62% (+115.17 to +144.07) | +224.24% | yes |
| Nephio | 4 | **GAIN (more work + fewer misses)** | +0.05% (+0.01 to +0.08) | 5.10% → 3.34% (−34.5%) | -1.76 (-2.48 to -1.04) | +9.96% (+5.63 to +14.30) | +19.48% | yes |
| **The orchestra, every governor's muscle once** | 55 | **GAIN (more work + fewer misses)** | +0.14% (+0.09 to +0.19) | 3.20% → 1.14% (−64.3%) | -2.06 (-2.21 to -1.90) | +54.54% (+49.43 to +59.64) | +101.76% | yes |

## Work waiting in line (a 25% share of the run's own work waiting when it starts)

Work: the mean over the body's plants of each plant's work against native's. Misses: the plants' decisions over their own line, native → omni. Power given: the body's energy against native's. Wear: shown, never judged. 95% intervals over seeds.

| Body | Muscles | Reading | Work | Misses, native → omni | Misses (pp) | Power given | Wear | Valid |
|---|---:|---|---:|---|---:|---:|---:|---|
| The Kubernetes scheduler (vanilla, and its bin-packing profile) | 12 | **GAIN (fewer misses)** | +0.00% (-0.00 to +0.00) | 1.29% → 0.68% (−47.2%) | -0.61 (-0.82 to -0.39) | +25.12% (+23.83 to +26.40) | +54.14% | yes |
| Kueue | 5 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 1.18% → 1.18% (−0.0%) | +0.00 (+0.00 to +0.00) | +0.00% (+0.00 to +0.00) | +0.00% | yes |
| Volcano | 5 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +12.40% (+11.32 to +13.48) | +32.90% | yes |
| KAI scheduler | 4 | **STEADY (the same as native)** | +0.00% (+0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +6.64% (+4.61 to +8.67) | +21.99% | yes |
| Koordinator | 4 | **STEADY (the same as native)** | +0.00% (-0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +36.06% (+33.69 to +38.43) | +75.09% | yes |
| CruiseKube | 4 | **GAIN (fewer misses)** | -0.00% (-0.00 to +0.00) | 1.00% → 0.25% (−75.0%) | -0.75 (-1.20 to -0.30) | +33.34% (+29.84 to +36.85) | +67.20% | yes |
| Crane | 5 | **GAIN (fewer misses)** | +0.00% (+0.00 to +0.00) | 1.09% → 0.23% (−79.4%) | -0.87 (-1.15 to -0.58) | +33.71% (+31.37 to +36.05) | +68.49% | yes |
| KubeRay | 3 | **STEADY (the same as native)** | -0.00% (-0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +24.01% (+22.92 to +25.10) | +70.14% | yes |
| Gödel scheduler | 4 | **STEADY (the same as native)** | -0.00% (-0.00 to +0.00) | 0.00% → 0.00% (−0.0%) | +0.00 (+0.00 to +0.00) | +27.47% (+25.68 to +29.27) | +60.88% | yes |
| Armada | 3 | **GAIN (fewer misses)** | +0.04% (-0.02 to +0.11) | 4.50% → 3.06% (−32.1%) | -1.44 (-2.13 to -0.76) | +41.53% (+33.64 to +49.42) | +120.48% | yes |
| Karmada | 4 | **GAIN (fewer misses)** | +0.17% (-0.01 to +0.35) | 4.05% → 0.50% (−87.7%) | -3.55 (-4.59 to -2.52) | +164.02% (+156.14 to +171.90) | +361.60% | yes |
| Open Cluster Management | 3 | **GAIN (more work + fewer misses)** | +0.09% (+0.02 to +0.17) | 5.00% → 2.42% (−51.7%) | -2.58 (-3.55 to -1.61) | +113.46% (+103.51 to +123.41) | +247.09% | yes |
| KubeEdge | 4 | **GAIN (fewer misses)** | +0.04% (-0.04 to +0.13) | 3.01% → 0.51% (−83.0%) | -2.50 (-3.51 to -1.49) | +132.26% (+117.87 to +146.64) | +278.62% | yes |
| Nephio | 4 | **GAIN (fewer misses)** | +0.00% (-0.00 to +0.01) | 1.60% → 1.16% (−27.9%) | -0.45 (-0.70 to -0.19) | +5.28% (+3.57 to +7.00) | +10.06% | yes |
| **The orchestra, every governor's muscle once** | 55 | **GAIN (more work + fewer misses)** | +0.02% (+0.01 to +0.03) | 1.43% → 0.62% (−56.2%) | -0.80 (-0.91 to -0.69) | +42.40% (+40.72 to +44.09) | +89.45% | yes |

## Inside every body: each plant that did less work than native or missed its line more often

| Load | Body | Plants | Plants with less work or more misses | The plants (work change, extra decisions over the line, all seeds) |
|---|---|---:|---:|---|
| normal | The Kubernetes scheduler (vanilla, and its bin-packing profile) | 12 | 0 | none |
| normal | Kueue | 5 | 0 | none |
| normal | Volcano | 5 | 0 | none |
| normal | KAI scheduler | 4 | 0 | none |
| normal | Koordinator | 4 | 0 | none |
| normal | CruiseKube | 4 | 0 | none |
| normal | Crane | 5 | 0 | none |
| normal | KubeRay | 3 | 0 | none |
| normal | Gödel scheduler | 4 | 0 | none |
| normal | Armada | 3 | 0 | none |
| normal | Karmada | 4 | 0 | none |
| normal | Open Cluster Management | 3 | 0 | none |
| normal | KubeEdge | 4 | 0 | none |
| normal | Nephio | 4 | 0 | none |
| normal | **The orchestra, every governor's muscle once** | 55 | 0 | none |
| climb | The Kubernetes scheduler (vanilla, and its bin-packing profile) | 12 | 0 | none |
| climb | Kueue | 5 | 0 | none |
| climb | Volcano | 5 | 0 | none |
| climb | KAI scheduler | 4 | 0 | none |
| climb | Koordinator | 4 | 0 | none |
| climb | CruiseKube | 4 | 0 | none |
| climb | Crane | 5 | 0 | none |
| climb | KubeRay | 3 | 0 | none |
| climb | Gödel scheduler | 4 | 0 | none |
| climb | Armada | 3 | 0 | none |
| climb | Karmada | 4 | 0 | none |
| climb | Open Cluster Management | 3 | 0 | none |
| climb | KubeEdge | 4 | 0 | none |
| climb | Nephio | 4 | 0 | none |
| climb | **The orchestra, every governor's muscle once** | 55 | 0 | none |
| line | The Kubernetes scheduler (vanilla, and its bin-packing profile) | 12 | 0 | none |
| line | Kueue | 5 | 0 | none |
| line | Volcano | 5 | 0 | none |
| line | KAI scheduler | 4 | 0 | none |
| line | Koordinator | 4 | 0 | none |
| line | CruiseKube | 4 | 0 | none |
| line | Crane | 5 | 0 | none |
| line | KubeRay | 3 | 0 | none |
| line | Gödel scheduler | 4 | 0 | none |
| line | Armada | 3 | 0 | none |
| line | Karmada | 4 | 0 | none |
| line | Open Cluster Management | 3 | 0 | none |
| line | KubeEdge | 4 | 0 | none |
| line | Nephio | 4 | 0 | none |
| line | **The orchestra, every governor's muscle once** | 55 | 0 | none |

## The muscles

| Body | Muscles (catalog family) |
|---|---|
| The Kubernetes scheduler (vanilla, and its bin-packing profile) | `node_selector` (4), `node_affinity` (4), `pod_anti_affinity` (4), `topology_spread` (4), `taint_toleration` (4), `priority_class` (4), `preemption_policy` (4), `scheduler_backoff` (4), `scheduler_scoring_strategy` (4), `scheduler_plugin_weights` (4), `scheduling_gates` (4), `deschedule` (4) |
| Kueue | `job_admission` (1), `batch_admission` (1), `queue_concurrency` (1), `queue_backpressure` (1), `tenant_admission` (1) |
| Volcano | `gang_schedule` (14), `queue_fairness` (14), `task_priority` (14), `task_preemption` (14), `binpack_pressure` (14) |
| KAI scheduler | `gang_schedule` (14), `queue_fairness` (14), `cluster_quota` (14), `task_preemption` (14) |
| Koordinator | `oversubscription` (14), `resource_reclaim` (14), `binpack_pressure` (14), `spread_pressure` (14) |
| CruiseKube | `cruisekube_request_rightsizing` (3), `in_place_resize` (3), `cpu_request` (3), `memory_request` (3) |
| Crane | `hpa_cpu_target` (2), `hpa_custom_target` (2), `hpa_scaling_rate_policies` (2), `hpa_min_replicas` (2), `hpa_max_replicas` (2) |
| KubeRay | `training_workers` (12), `elastic_worker_count` (12), `training_gang_size` (12) |
| Gödel scheduler | `gang_schedule` (14), `task_admission` (14), `binpack_pressure` (14), `resource_reservation` (14) |
| Armada | `multi_cluster_dispatch` (39), `federation_quota` (39), `global_admission` (39) |
| Karmada | `multi_cluster_dispatch` (39), `region_dispatch` (39), `global_failover` (39), `cross_cluster_replication` (39) |
| Open Cluster Management | `multi_cluster_dispatch` (39), `workload_migrate_region` (39), `federation_quota` (39) |
| KubeEdge | `edge_dispatch` (39), `edge_offload` (39), `edge_sync_interval` (39), `edge_site_node_pool` (39) |
| Nephio | `ran_slice_resource_budget` (66), `ran_du_cu_placement` (66), `ran_cell_sleep` (66), `ran_carrier_enable` (66) |
| **The orchestra, every governor's muscle once** | `node_selector` (4), `node_affinity` (4), `pod_anti_affinity` (4), `topology_spread` (4), `taint_toleration` (4), `priority_class` (4), `preemption_policy` (4), `scheduler_backoff` (4), `scheduler_scoring_strategy` (4), `scheduler_plugin_weights` (4), `scheduling_gates` (4), `deschedule` (4), `job_admission` (1), `batch_admission` (1), `queue_concurrency` (1), `queue_backpressure` (1), `tenant_admission` (1), `gang_schedule` (14), `queue_fairness` (14), `task_priority` (14), `task_preemption` (14), `binpack_pressure` (14), `cluster_quota` (14), `oversubscription` (14), `resource_reclaim` (14), `spread_pressure` (14), `cruisekube_request_rightsizing` (3), `in_place_resize` (3), `cpu_request` (3), `memory_request` (3), `hpa_cpu_target` (2), `hpa_custom_target` (2), `hpa_scaling_rate_policies` (2), `hpa_min_replicas` (2), `hpa_max_replicas` (2), `training_workers` (12), `elastic_worker_count` (12), `training_gang_size` (12), `task_admission` (14), `resource_reservation` (14), `multi_cluster_dispatch` (39), `federation_quota` (39), `global_admission` (39), `region_dispatch` (39), `global_failover` (39), `cross_cluster_replication` (39), `workload_migrate_region` (39), `edge_dispatch` (39), `edge_offload` (39), `edge_sync_interval` (39), `edge_site_node_pool` (39), `ran_slice_resource_budget` (66), `ran_du_cu_placement` (66), `ran_cell_sleep` (66), `ran_carrier_enable` (66) |

Raw per-seed contrasts: `ORCHESTRA.json`. Fingerprints: `RUN.json`, `SHA256SUMS.txt`.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
