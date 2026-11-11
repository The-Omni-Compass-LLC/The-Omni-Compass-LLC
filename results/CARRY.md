# Which results carry to the engine that stands (omni-v26)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Every benchmark's newest three-run table, the engine files its runner imports (followed import by import through the fingerprint), and whether any of them has moved since the table's own engine. A result **carries** when every one of those files has the same bytes on its engine and on omni-v26: the engine that stands runs exactly the code the table measured, and the benchmark need not run again for the version number alone. A result **runs again** when one moved; the files that moved are named. A carried record stays its own engine's, under its own engine's name. Written by `python3 tools/carry.py` from the fingerprints (`OMNI_V<n>.json`) and the tables; `verify.py` fails a push where it differs (the founder's order of 7 November, evening).

On omni-v26: 2 on the engine that stands, 22 carry, 93 run again.

| Benchmark | Its newest table | Its engine | The runner | Engine files it runs | Moved since its engine | On omni-v26 |
|---|---|---|---|---:|---|---|
| A100_8CARD_STACKS_ABC | `results/gpu/V23_A100_8CARD_STACKS_ABC.json` | omni-v23 | `omni_controller/gpu_compass.py` | 14 | none | **carries** |
| A100_CAP_ABC | `results/gpu/V21_A100_CAP_ABC.json` | omni-v21 | `omni_controller/gpu_compass.py` | 14 | `omni_controller/muscles.py` | **runs again** |
| A100_CAP_FULL_ABC | `results/gpu/V21_A100_CAP_FULL_ABC.json` | omni-v21 | `omni_controller/gpu_compass.py` | 14 | `omni_controller/muscles.py` | **runs again** |
| A100_SAVE_ABC | `results/gpu/V21_A100_SAVE_ABC.json` | omni-v21 | `omni_controller/gpu_compass.py` | 14 | `omni_controller/muscles.py` | **runs again** |
| A10_CAP_ABC | `results/gpu/V23_A10_CAP_ABC.json` | omni-v23 | `omni_controller/gpu_compass.py` | 14 | none | **carries** |
| A10_CAP_FULL_ABC | `results/gpu/V23_A10_CAP_FULL_ABC.json` | omni-v23 | `omni_controller/gpu_compass.py` | 14 | none | **carries** |
| A10_FAST_ABC | `results/gpu/V23_A10_FAST_ABC.json` | omni-v23 | `omni_controller/gpu_compass.py` | 14 | none | **carries** |
| A10_STACKS_FULL_ABC | `results/gpu/V23_A10_STACKS_FULL_ABC.json` | omni-v23 | `omni_controller/gpu_compass.py` | 14 | none | **carries** |
| STACKS_A10_ABC | `results/gpu/V21_STACKS_A10_ABC.json` | omni-v21 | `omni_controller/gpu_compass.py` | 14 | `omni_controller/muscles.py` | **runs again** |
| AKS_BURST | `results/live/V1_AKS_BURST.json` | omni-v1 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omni_controller/quota.py`, `omnicompass/__init__.py`, `omnicompass/adapter.py`, `omnicompass/compass_law.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/master.py`, `omnicompass/nervous_system.py`, `omnicompass/verdict.py` | **runs again** |
| AKS_FULL_BURST | `results/live/V26_AKS_FULL_BURST.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| AKS_STEADY | `results/live/V1_AKS_STEADY.json` | omni-v1 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omni_controller/quota.py`, `omnicompass/__init__.py`, `omnicompass/adapter.py`, `omnicompass/compass_law.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/master.py`, `omnicompass/nervous_system.py`, `omnicompass/verdict.py` | **runs again** |
| ALL_FOUR | `results/live/V25_ALL_FOUR.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ARMADA_4W_BARE | `results/live/V25_ARMADA_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ARMADA_4W_BOTH | `results/live/V25_ARMADA_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ARMADA_4W_ORCH | `results/live/V25_ARMADA_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ARMADA_4W_TOP | `results/live/V25_ARMADA_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ARMADA_4W_VS | `results/live/V25_ARMADA_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| BATCH | `results/live/V25_BATCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| BIG_ORGANISM | `results/live/V3_BIG_ORGANISM.json` | omni-v3 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omni_controller/quota.py`, `omnicompass/__init__.py`, `omnicompass/adapter.py`, `omnicompass/compass_law.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/master.py`, `omnicompass/nervous_system.py`, `omnicompass/verdict.py` | **runs again** |
| BINPACK | `results/live/V25_BINPACK.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| BINPACK_4W_BARE | `results/live/V25_BINPACK_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| BINPACK_4W_BOTH | `results/live/V25_BINPACK_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| BINPACK_4W_ORCH | `results/live/V25_BINPACK_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| BINPACK_4W_TOP | `results/live/V25_BINPACK_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| BINPACK_4W_VS | `results/live/V25_BINPACK_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| CAPACITY | `results/live/V25_CAPACITY.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| CITYLEARN | `results/live/V25_CITYLEARN.md` | omni-v25 | `tools/run_citylearn.py` | 2 | none | **carries** |
| COST_TO_MATCH | `results/live/V25_COST_TO_MATCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| CRANE_4W_BARE | `results/live/V25_CRANE_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| CRANE_4W_BOTH | `results/live/V25_CRANE_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| CRANE_4W_ORCH | `results/live/V25_CRANE_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| CRANE_4W_TOP | `results/live/V25_CRANE_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| CRANE_4W_VS | `results/live/V25_CRANE_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| CRUISEKUBE | `results/live/V25_CRUISEKUBE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| CRUISEKUBE_RECORDER | `results/live/V25_CRUISEKUBE_RECORDER.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| FAIRNESS | `results/live/V25_FAIRNESS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| FAULTS | `results/live/V25_FAULTS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| FAULTS_EXTENDED | `results/live/V25_FAULTS_EXTENDED.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| GODEL_4W_BARE | `results/live/V25_GODEL_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| GODEL_4W_BOTH | `results/live/V25_GODEL_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| GODEL_4W_ORCH | `results/live/V25_GODEL_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| GODEL_4W_TOP | `results/live/V25_GODEL_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| GODEL_4W_VS | `results/live/V25_GODEL_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| GOLDILOCKS | `results/live/V25_GOLDILOCKS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KAFKA | `results/live/V26_KAFKA.json` | omni-v26 | `tools/run_kafka.py` | 7 | none | **on the engine that stands** |
| KAFKA_SERVICE | `results/live/V25_KAFKA_SERVICE.json` | omni-v25 | `tools/run_kafka.py` | 7 | none | **carries** |
| KAI | `results/live/V25_KAI.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KAI_4W_BARE | `results/live/V25_KAI_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KAI_4W_BOTH | `results/live/V25_KAI_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KAI_4W_ORCH | `results/live/V25_KAI_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KAI_4W_TOP | `results/live/V25_KAI_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KAI_4W_VS | `results/live/V25_KAI_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KARMADA_4W_BARE | `results/live/V25_KARMADA_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KARMADA_4W_BOTH | `results/live/V25_KARMADA_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KARMADA_4W_ORCH | `results/live/V25_KARMADA_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KARMADA_4W_TOP | `results/live/V25_KARMADA_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KARMADA_4W_VS | `results/live/V25_KARMADA_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KEDA_CPU_REQUESTS | `results/live/V25_KEDA_CPU_REQUESTS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KEDA_REQUESTS | `results/live/V25_KEDA_REQUESTS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KOORDINATOR | `results/live/V25_KOORDINATOR.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KOORDINATOR_4W_BARE | `results/live/V12_KOORDINATOR_4W_BARE.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_4W_BOTH | `results/live/V12_KOORDINATOR_4W_BOTH.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_4W_ORCH | `results/live/V12_KOORDINATOR_4W_ORCH.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_4W_TOP | `results/live/V12_KOORDINATOR_4W_TOP.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_4W_VS | `results/live/V12_KOORDINATOR_4W_VS.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_CGROUP | `results/live/V25_KOORDINATOR_CGROUP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUBERAY_4W_BARE | `results/live/V25_KUBERAY_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUBERAY_4W_BOTH | `results/live/V25_KUBERAY_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUBERAY_4W_ORCH | `results/live/V25_KUBERAY_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUBERAY_4W_TOP | `results/live/V25_KUBERAY_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUBERAY_4W_VS | `results/live/V25_KUBERAY_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUEUE | `results/live/V25_KUEUE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUEUE_4W_BARE | `results/live/V25_KUEUE_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUEUE_4W_BOTH | `results/live/V25_KUEUE_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUEUE_4W_ORCH | `results/live/V25_KUEUE_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUEUE_4W_TOP | `results/live/V25_KUEUE_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KUEUE_4W_VS | `results/live/V25_KUEUE_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| MUJOCO | `results/live/V25_MUJOCO.md` | omni-v25 | `tools/run_mujoco.py` | 2 | none | **carries** |
| MUJOCO_PANDA | `results/live/V1_MUJOCO_PANDA.md` | omni-v1 | `tools/run_mujoco.py` | 2 | `omnicompass/compass_law.py`, `tools/run_mujoco.py` | **runs again** |
| OCM_4W_BARE | `results/live/V25_OCM_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| OCM_4W_BOTH | `results/live/V25_OCM_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| OCM_4W_ORCH | `results/live/V25_OCM_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| OCM_4W_TOP | `results/live/V25_OCM_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| OCM_4W_VS | `results/live/V25_OCM_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| OWN_COST | `results/live/V3_OWN_COST.json` | omni-v3 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omni_controller/quota.py`, `omnicompass/__init__.py`, `omnicompass/adapter.py`, `omnicompass/compass_law.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/master.py`, `omnicompass/nervous_system.py`, `omnicompass/verdict.py` | **runs again** |
| PANDAPOWER | `results/live/V25_PANDAPOWER.md` | omni-v25 | `tools/run_pandapower.py` | 2 | none | **carries** |
| PGBENCH | `results/live/V25_PGBENCH.json` | omni-v25 | `tools/run_pgbench.py` | 6 | none | **carries** |
| PGBENCH_SERVICE | `results/live/V25_PGBENCH_SERVICE.json` | omni-v25 | `tools/run_pgbench.py` | 6 | none | **carries** |
| REDIS | `results/live/V25_REDIS.json` | omni-v25 | `tools/run_redis.py` | 7 | none | **carries** |
| REDIS_SERVICE | `results/live/V25_REDIS_SERVICE.json` | omni-v25 | `tools/run_redis.py` | 7 | none | **carries** |
| REDIS_SHIPPED | `results/live/V25_REDIS_SHIPPED.json` | omni-v25 | `tools/run_redis.py` | 7 | none | **carries** |
| ROBUST_KILL | `results/live/V25_ROBUST_KILL.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ROBUST_LONG | `results/live/V25_ROBUST_LONG.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| SIX_KUBE | `results/live/V3_SIX_KUBE.json` | omni-v3 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omni_controller/quota.py`, `omnicompass/__init__.py`, `omnicompass/adapter.py`, `omnicompass/compass_law.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/master.py`, `omnicompass/nervous_system.py`, `omnicompass/verdict.py` | **runs again** |
| SOLO | `results/live/V25_SOLO.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| SOLO_2 | `results/live/V25_SOLO_2.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| SOLO_2_VS_ON_NATIVE | `results/live/V25_SOLO_2_VS_ON_NATIVE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| SOLO_VS_ON_NATIVE | `results/live/V25_SOLO_VS_ON_NATIVE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| STEADY | `results/live/V25_STEADY.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| SWARM | `results/live/V25_SWARM.md` | omni-v25 | `tools/run_swarm.py` | 2 | none | **carries** |
| SYSBENCH | `results/live/V25_SYSBENCH.json` | omni-v25 | `tools/run_sysbench.py` | 7 | none | **carries** |
| SYSBENCH_SERVICE | `results/live/V25_SYSBENCH_SERVICE.json` | omni-v25 | `tools/run_sysbench.py` | 7 | none | **carries** |
| SYSBENCH_SHIPPED | `results/live/V25_SYSBENCH_SHIPPED.json` | omni-v25 | `tools/run_sysbench.py` | 7 | none | **carries** |
| TRACE_GOOGLE2011 | `results/live/V25_TRACE_GOOGLE2011.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VANILLA | `results/live/V25_VANILLA.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO | `results/live/V25_VOLCANO.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO_4W_BARE | `results/live/V25_VOLCANO_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO_4W_BOTH | `results/live/V25_VOLCANO_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO_4W_ORCH | `results/live/V25_VOLCANO_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO_4W_TOP | `results/live/V25_VOLCANO_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO_4W_VS | `results/live/V25_VOLCANO_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| WANDERING | `results/live/V25_WANDERING.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| YCSB | `results/live/V25_YCSB.json` | omni-v25 | `tools/run_ycsb.py` | 6 | none | **carries** |
| YCSB_SERVICE | `results/live/V25_YCSB_SERVICE.json` | omni-v25 | `tools/run_ycsb.py` | 6 | none | **carries** |
| YCSB_SHIPPED | `results/live/V25_YCSB_SHIPPED.json` | omni-v25 | `tools/run_ycsb.py` | 6 | none | **carries** |
| THREE_ARMS_ABC | `results/orchestrator/V21_THREE_ARMS_ABC.json` | omni-v21 | `omni_orchestrator/brain.py` | 2 | none | **carries** |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
