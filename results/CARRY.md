# Which results carry to the engine that stands (omni-v26)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Every benchmark's newest three-run table, the engine files its runner imports (followed import by import through the fingerprint), and whether any of them has moved since the table's own engine. A result **carries** when every one of those files has the same bytes on its engine and on omni-v26: the engine that stands runs exactly the code the table measured, and the benchmark need not run again for the version number alone. A result **runs again** when one moved; the files that moved are named. A carried record stays its own engine's, under its own engine's name. Written by `python3 tools/carry.py` from the fingerprints (`OMNI_V<n>.json`) and the tables; `verify.py` fails a push where it differs (the founder's order of 7 November, evening).

On omni-v26: 81 on the engine that stands, 6 carry, 30 run again.

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
| ALL_FOUR | `results/live/V26_ALL_FOUR.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| ARMADA_4W_BARE | `results/live/V25_ARMADA_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ARMADA_4W_BOTH | `results/live/V25_ARMADA_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ARMADA_4W_ORCH | `results/live/V25_ARMADA_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ARMADA_4W_TOP | `results/live/V25_ARMADA_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| ARMADA_4W_VS | `results/live/V25_ARMADA_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| BATCH | `results/live/V26_BATCH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| BIG_ORGANISM | `results/live/V3_BIG_ORGANISM.json` | omni-v3 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omni_controller/quota.py`, `omnicompass/__init__.py`, `omnicompass/adapter.py`, `omnicompass/compass_law.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/master.py`, `omnicompass/nervous_system.py`, `omnicompass/verdict.py` | **runs again** |
| BINPACK | `results/live/V26_BINPACK.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| BINPACK_4W_BARE | `results/live/V26_BINPACK_4W_BARE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| BINPACK_4W_BOTH | `results/live/V26_BINPACK_4W_BOTH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| BINPACK_4W_ORCH | `results/live/V26_BINPACK_4W_ORCH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| BINPACK_4W_TOP | `results/live/V26_BINPACK_4W_TOP.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| BINPACK_4W_VS | `results/live/V26_BINPACK_4W_VS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| CAPACITY | `results/live/V26_CAPACITY.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| CITYLEARN | `results/live/V26_CITYLEARN.md` | omni-v26 | `tools/run_citylearn.py` | 2 | none | **on the engine that stands** |
| COST_TO_MATCH | `results/live/V26_COST_TO_MATCH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| CRANE_4W_BARE | `results/live/V26_CRANE_4W_BARE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| CRANE_4W_BOTH | `results/live/V26_CRANE_4W_BOTH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| CRANE_4W_ORCH | `results/live/V26_CRANE_4W_ORCH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| CRANE_4W_TOP | `results/live/V26_CRANE_4W_TOP.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| CRANE_4W_VS | `results/live/V26_CRANE_4W_VS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| CRUISEKUBE | `results/live/V26_CRUISEKUBE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| CRUISEKUBE_RECORDER | `results/live/V26_CRUISEKUBE_RECORDER.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| FAIRNESS | `results/live/V26_FAIRNESS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| FAULTS | `results/live/V26_FAULTS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| FAULTS_EXTENDED | `results/live/V26_FAULTS_EXTENDED.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| GODEL_4W_BARE | `results/live/V26_GODEL_4W_BARE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| GODEL_4W_BOTH | `results/live/V26_GODEL_4W_BOTH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| GODEL_4W_ORCH | `results/live/V26_GODEL_4W_ORCH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| GODEL_4W_TOP | `results/live/V26_GODEL_4W_TOP.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| GODEL_4W_VS | `results/live/V26_GODEL_4W_VS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| GOLDILOCKS | `results/live/V26_GOLDILOCKS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KAFKA | `results/live/V26_KAFKA.json` | omni-v26 | `tools/run_kafka.py` | 7 | none | **on the engine that stands** |
| KAFKA_SERVICE | `results/live/V26_KAFKA_SERVICE.json` | omni-v26 | `tools/run_kafka.py` | 7 | none | **on the engine that stands** |
| KAI | `results/live/V26_KAI.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KAI_4W_BARE | `results/live/V26_KAI_4W_BARE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KAI_4W_BOTH | `results/live/V26_KAI_4W_BOTH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KAI_4W_ORCH | `results/live/V26_KAI_4W_ORCH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KAI_4W_TOP | `results/live/V26_KAI_4W_TOP.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KAI_4W_VS | `results/live/V26_KAI_4W_VS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KARMADA_4W_BARE | `results/live/V25_KARMADA_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KARMADA_4W_BOTH | `results/live/V25_KARMADA_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KARMADA_4W_ORCH | `results/live/V25_KARMADA_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KARMADA_4W_TOP | `results/live/V25_KARMADA_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KARMADA_4W_VS | `results/live/V25_KARMADA_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| KEDA_CPU_REQUESTS | `results/live/V26_KEDA_CPU_REQUESTS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KEDA_REQUESTS | `results/live/V26_KEDA_REQUESTS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KOORDINATOR | `results/live/V26_KOORDINATOR.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KOORDINATOR_4W_BARE | `results/live/V12_KOORDINATOR_4W_BARE.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_4W_BOTH | `results/live/V12_KOORDINATOR_4W_BOTH.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_4W_ORCH | `results/live/V12_KOORDINATOR_4W_ORCH.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_4W_TOP | `results/live/V12_KOORDINATOR_4W_TOP.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_4W_VS | `results/live/V12_KOORDINATOR_4W_VS.json` | omni-v12 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omnicompass/adapter.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/nervous_system.py` | **runs again** |
| KOORDINATOR_CGROUP | `results/live/V26_KOORDINATOR_CGROUP.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUBERAY_4W_BARE | `results/live/V26_KUBERAY_4W_BARE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUBERAY_4W_BOTH | `results/live/V26_KUBERAY_4W_BOTH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUBERAY_4W_ORCH | `results/live/V26_KUBERAY_4W_ORCH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUBERAY_4W_TOP | `results/live/V26_KUBERAY_4W_TOP.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUBERAY_4W_VS | `results/live/V26_KUBERAY_4W_VS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUEUE | `results/live/V26_KUEUE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUEUE_4W_BARE | `results/live/V26_KUEUE_4W_BARE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUEUE_4W_BOTH | `results/live/V26_KUEUE_4W_BOTH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUEUE_4W_ORCH | `results/live/V26_KUEUE_4W_ORCH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUEUE_4W_TOP | `results/live/V26_KUEUE_4W_TOP.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| KUEUE_4W_VS | `results/live/V26_KUEUE_4W_VS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| MUJOCO | `results/live/V26_MUJOCO.md` | omni-v26 | `tools/run_mujoco.py` | 2 | none | **on the engine that stands** |
| MUJOCO_PANDA | `results/live/V1_MUJOCO_PANDA.md` | omni-v1 | `tools/run_mujoco.py` | 2 | `omnicompass/compass_law.py`, `tools/run_mujoco.py` | **runs again** |
| OCM_4W_BARE | `results/live/V26_OCM_4W_BARE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| OCM_4W_BOTH | `results/live/V26_OCM_4W_BOTH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| OCM_4W_ORCH | `results/live/V26_OCM_4W_ORCH.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| OCM_4W_TOP | `results/live/V26_OCM_4W_TOP.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| OCM_4W_VS | `results/live/V26_OCM_4W_VS.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| OWN_COST | `results/live/V3_OWN_COST.json` | omni-v3 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omni_controller/quota.py`, `omnicompass/__init__.py`, `omnicompass/adapter.py`, `omnicompass/compass_law.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/master.py`, `omnicompass/nervous_system.py`, `omnicompass/verdict.py` | **runs again** |
| PANDAPOWER | `results/live/V26_PANDAPOWER.md` | omni-v26 | `tools/run_pandapower.py` | 2 | none | **on the engine that stands** |
| PGBENCH | `results/live/V26_PGBENCH.json` | omni-v26 | `tools/run_pgbench.py` | 6 | none | **on the engine that stands** |
| PGBENCH_SERVICE | `results/live/V26_PGBENCH_SERVICE.json` | omni-v26 | `tools/run_pgbench.py` | 6 | none | **on the engine that stands** |
| REDIS | `results/live/V26_REDIS.json` | omni-v26 | `tools/run_redis.py` | 7 | none | **on the engine that stands** |
| REDIS_SERVICE | `results/live/V26_REDIS_SERVICE.json` | omni-v26 | `tools/run_redis.py` | 7 | none | **on the engine that stands** |
| REDIS_SHIPPED | `results/live/V26_REDIS_SHIPPED.json` | omni-v26 | `tools/run_redis.py` | 7 | none | **on the engine that stands** |
| ROBUST_KILL | `results/live/V26_ROBUST_KILL.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| ROBUST_LONG | `results/live/V26_ROBUST_LONG.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| SIX_KUBE | `results/live/V3_SIX_KUBE.json` | omni-v3 | `omni_controller/controller.py` | 16 | `omni_controller/capacity.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `omni_controller/quota.py`, `omnicompass/__init__.py`, `omnicompass/adapter.py`, `omnicompass/compass_law.py`, `omnicompass/edge.py`, `omnicompass/immune.py`, `omnicompass/master.py`, `omnicompass/nervous_system.py`, `omnicompass/verdict.py` | **runs again** |
| SOLO | `results/live/V26_SOLO.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| SOLO_2 | `results/live/V26_SOLO_2.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| SOLO_2_VS_ON_NATIVE | `results/live/V26_SOLO_2_VS_ON_NATIVE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| SOLO_VS_ON_NATIVE | `results/live/V26_SOLO_VS_ON_NATIVE.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| STEADY | `results/live/V26_STEADY.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| SWARM | `results/live/V26_SWARM.md` | omni-v26 | `tools/run_swarm.py` | 2 | none | **on the engine that stands** |
| SYSBENCH | `results/live/V26_SYSBENCH.json` | omni-v26 | `tools/run_sysbench.py` | 7 | none | **on the engine that stands** |
| SYSBENCH_SERVICE | `results/live/V26_SYSBENCH_SERVICE.json` | omni-v26 | `tools/run_sysbench.py` | 7 | none | **on the engine that stands** |
| SYSBENCH_SHIPPED | `results/live/V26_SYSBENCH_SHIPPED.json` | omni-v26 | `tools/run_sysbench.py` | 7 | none | **on the engine that stands** |
| TRACE_GOOGLE2011 | `results/live/V26_TRACE_GOOGLE2011.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| VANILLA | `results/live/V26_VANILLA.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| VOLCANO | `results/live/V26_VOLCANO.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| VOLCANO_4W_BARE | `results/live/V25_VOLCANO_4W_BARE.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO_4W_BOTH | `results/live/V25_VOLCANO_4W_BOTH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO_4W_ORCH | `results/live/V25_VOLCANO_4W_ORCH.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO_4W_TOP | `results/live/V25_VOLCANO_4W_TOP.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| VOLCANO_4W_VS | `results/live/V25_VOLCANO_4W_VS.json` | omni-v25 | `omni_controller/controller.py` | 16 | `omni_controller/controller.py` | **runs again** |
| WANDERING | `results/live/V26_WANDERING.json` | omni-v26 | `omni_controller/controller.py` | 16 | none | **on the engine that stands** |
| YCSB | `results/live/V26_YCSB.json` | omni-v26 | `tools/run_ycsb.py` | 6 | none | **on the engine that stands** |
| YCSB_SERVICE | `results/live/V26_YCSB_SERVICE.json` | omni-v26 | `tools/run_ycsb.py` | 6 | none | **on the engine that stands** |
| YCSB_SHIPPED | `results/live/V26_YCSB_SHIPPED.json` | omni-v26 | `tools/run_ycsb.py` | 6 | none | **on the engine that stands** |
| THREE_ARMS_ABC | `results/orchestrator/V21_THREE_ARMS_ABC.json` | omni-v21 | `omni_orchestrator/brain.py` | 2 | none | **carries** |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
