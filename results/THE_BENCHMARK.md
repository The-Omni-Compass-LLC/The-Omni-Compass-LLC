# The one benchmark: every scenario on omni-v27

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

One engine. Every scenario. Every receipt. Nothing on this page asks to be believed: each line names the file it comes from, and `python3 tools/the_benchmark.py` writes the page again from those files. A receipt is the engine's own, carries to it (not one engine file its runner runs has moved), or runs again on it. A receipt on an older engine is that engine's, and is not counted here. Each one reads by the one key: GAIN, STEADY, LOSS, power given, with a 0.5% floor. The LOSS rows are printed in the same tables as the GAIN rows, because a record that hides its losses is not a record. Run it again. The numbers come out the same, or they do not. That is the whole argument.

## 1. The one engine

**omni-v27**, digest `34548e45437a05bd`, 65 files under its fingerprint (`OMNI_V27.json`), the same engine in Python and, for its 18 sealed mechanisms, in C++ held to the Python to the last bit (`results/SEAL.json`). The same governor runs on every place below; what differs per place is the wire to it.

## 2. Every scenario on real machines

Of 118 scenarios with a three-run receipt: **0 on omni-v27**, 18 carry to it, **100 run again on it**. The rows on the engine's own receipts, by what each receipt sets side by side (as the LOSS ledger reads them, `docs/LOSS_LEDGER.md`):

| Set side by side | Rows by word |
|---|---|
| Omni-Compass on native against native alone | none judged |
| Omni-Compass by itself, in place of a controller | none judged |
| Omni-Compass on top of an orchestrator, against the orchestrator alone or compounded | none judged |

### the chip (class P: the card's own meter)

9 scenarios: 0 on omni-v27, 0 carry, 9 run again.

| Scenario | Its newest receipt | Its engine | On omni-v27 | Its rows by word (on the engine's own receipt) |
|---|---|---|---|---|
| A100_8CARD_STACKS_ABC | [V23_A100_8CARD_STACKS_ABC.json](gpu/V23_A100_8CARD_STACKS_ABC.json) | omni-v23 | **runs again** | — |
| A100_CAP_ABC | [V21_A100_CAP_ABC.json](gpu/V21_A100_CAP_ABC.json) | omni-v21 | **runs again** | — |
| A100_CAP_FULL_ABC | [V21_A100_CAP_FULL_ABC.json](gpu/V21_A100_CAP_FULL_ABC.json) | omni-v21 | **runs again** | — |
| A100_SAVE_ABC | [V21_A100_SAVE_ABC.json](gpu/V21_A100_SAVE_ABC.json) | omni-v21 | **runs again** | — |
| A10_CAP_ABC | [V23_A10_CAP_ABC.json](gpu/V23_A10_CAP_ABC.json) | omni-v23 | **runs again** | — |
| A10_CAP_FULL_ABC | [V23_A10_CAP_FULL_ABC.json](gpu/V23_A10_CAP_FULL_ABC.json) | omni-v23 | **runs again** | — |
| A10_FAST_ABC | [V23_A10_FAST_ABC.json](gpu/V23_A10_FAST_ABC.json) | omni-v23 | **runs again** | — |
| A10_STACKS_FULL_ABC | [V23_A10_STACKS_FULL_ABC.json](gpu/V23_A10_STACKS_FULL_ABC.json) | omni-v23 | **runs again** | — |
| STACKS_A10_ABC | [V21_STACKS_A10_ABC.json](gpu/V21_STACKS_A10_ABC.json) | omni-v21 | **runs again** | — |

### through the cloud (class L: the cloud's own bill)

4 scenarios: 0 on omni-v27, 0 carry, 4 run again.

| Scenario | Its newest receipt | Its engine | On omni-v27 | Its rows by word (on the engine's own receipt) |
|---|---|---|---|---|
| AKS_BURST | [V1_AKS_BURST.json](live/V1_AKS_BURST.json) | omni-v1 | **runs again** | — |
| AKS_FULL_BURST | [V26_AKS_FULL_BURST.json](live/V26_AKS_FULL_BURST.json) | omni-v26 | **runs again** | — |
| AKS_STEADY | [V1_AKS_STEADY.json](live/V1_AKS_STEADY.json) | omni-v1 | **runs again** | — |
| AKS_WORK_METER | [V26_AKS_WORK_METER.json](live/V26_AKS_WORK_METER.json) | omni-v26 | **runs again** | — |

### Kubernetes (class L)

20 scenarios: 0 on omni-v27, 0 carry, 20 run again.

| Scenario | Its newest receipt | Its engine | On omni-v27 | Its rows by word (on the engine's own receipt) |
|---|---|---|---|---|
| ALL_FOUR | [V26_ALL_FOUR.json](live/V26_ALL_FOUR.json) | omni-v26 | **runs again** | — |
| BATCH | [V26_BATCH.json](live/V26_BATCH.json) | omni-v26 | **runs again** | — |
| BIG_ORGANISM | [V3_BIG_ORGANISM.json](live/V3_BIG_ORGANISM.json) | omni-v3 | **runs again** | — |
| CAPACITY | [V26_CAPACITY.json](live/V26_CAPACITY.json) | omni-v26 | **runs again** | — |
| COST_TO_MATCH | [V26_COST_TO_MATCH.json](live/V26_COST_TO_MATCH.json) | omni-v26 | **runs again** | — |
| FAIRNESS | [V26_FAIRNESS.json](live/V26_FAIRNESS.json) | omni-v26 | **runs again** | — |
| FAULTS | [V26_FAULTS.json](live/V26_FAULTS.json) | omni-v26 | **runs again** | — |
| FAULTS_EXTENDED | [V26_FAULTS_EXTENDED.json](live/V26_FAULTS_EXTENDED.json) | omni-v26 | **runs again** | — |
| OWN_COST | [V3_OWN_COST.json](live/V3_OWN_COST.json) | omni-v3 | **runs again** | — |
| ROBUST_KILL | [V26_ROBUST_KILL.json](live/V26_ROBUST_KILL.json) | omni-v26 | **runs again** | — |
| ROBUST_LONG | [V26_ROBUST_LONG.json](live/V26_ROBUST_LONG.json) | omni-v26 | **runs again** | — |
| SIX_KUBE | [V3_SIX_KUBE.json](live/V3_SIX_KUBE.json) | omni-v3 | **runs again** | — |
| SOLO | [V26_SOLO.json](live/V26_SOLO.json) | omni-v26 | **runs again** | — |
| SOLO_2 | [V26_SOLO_2.json](live/V26_SOLO_2.json) | omni-v26 | **runs again** | — |
| SOLO_2_VS_ON_NATIVE | [V26_SOLO_2_VS_ON_NATIVE.json](live/V26_SOLO_2_VS_ON_NATIVE.json) | omni-v26 | **runs again** | — |
| SOLO_VS_ON_NATIVE | [V26_SOLO_VS_ON_NATIVE.json](live/V26_SOLO_VS_ON_NATIVE.json) | omni-v26 | **runs again** | — |
| STEADY | [V26_STEADY.json](live/V26_STEADY.json) | omni-v26 | **runs again** | — |
| TRACE_GOOGLE2011 | [V26_TRACE_GOOGLE2011.json](live/V26_TRACE_GOOGLE2011.json) | omni-v26 | **runs again** | — |
| VANILLA | [V26_VANILLA.json](live/V26_VANILLA.json) | omni-v26 | **runs again** | — |
| WANDERING | [V26_WANDERING.json](live/V26_WANDERING.json) | omni-v26 | **runs again** | — |

### the governors and orchestrators on Kubernetes (class L)

66 scenarios: 0 on omni-v27, 0 carry, 66 run again.

| Scenario | Its newest receipt | Its engine | On omni-v27 | Its rows by word (on the engine's own receipt) |
|---|---|---|---|---|
| ARMADA_4W_BARE | [V25_ARMADA_4W_BARE.json](live/V25_ARMADA_4W_BARE.json) | omni-v25 | **runs again** | — |
| ARMADA_4W_BOTH | [V25_ARMADA_4W_BOTH.json](live/V25_ARMADA_4W_BOTH.json) | omni-v25 | **runs again** | — |
| ARMADA_4W_ORCH | [V25_ARMADA_4W_ORCH.json](live/V25_ARMADA_4W_ORCH.json) | omni-v25 | **runs again** | — |
| ARMADA_4W_TOP | [V25_ARMADA_4W_TOP.json](live/V25_ARMADA_4W_TOP.json) | omni-v25 | **runs again** | — |
| ARMADA_4W_VS | [V25_ARMADA_4W_VS.json](live/V25_ARMADA_4W_VS.json) | omni-v25 | **runs again** | — |
| BINPACK | [V26_BINPACK.json](live/V26_BINPACK.json) | omni-v26 | **runs again** | — |
| BINPACK_4W_BARE | [V26_BINPACK_4W_BARE.json](live/V26_BINPACK_4W_BARE.json) | omni-v26 | **runs again** | — |
| BINPACK_4W_BOTH | [V26_BINPACK_4W_BOTH.json](live/V26_BINPACK_4W_BOTH.json) | omni-v26 | **runs again** | — |
| BINPACK_4W_ORCH | [V26_BINPACK_4W_ORCH.json](live/V26_BINPACK_4W_ORCH.json) | omni-v26 | **runs again** | — |
| BINPACK_4W_TOP | [V26_BINPACK_4W_TOP.json](live/V26_BINPACK_4W_TOP.json) | omni-v26 | **runs again** | — |
| BINPACK_4W_VS | [V26_BINPACK_4W_VS.json](live/V26_BINPACK_4W_VS.json) | omni-v26 | **runs again** | — |
| CRANE_4W_BARE | [V26_CRANE_4W_BARE.json](live/V26_CRANE_4W_BARE.json) | omni-v26 | **runs again** | — |
| CRANE_4W_BOTH | [V26_CRANE_4W_BOTH.json](live/V26_CRANE_4W_BOTH.json) | omni-v26 | **runs again** | — |
| CRANE_4W_ORCH | [V26_CRANE_4W_ORCH.json](live/V26_CRANE_4W_ORCH.json) | omni-v26 | **runs again** | — |
| CRANE_4W_TOP | [V26_CRANE_4W_TOP.json](live/V26_CRANE_4W_TOP.json) | omni-v26 | **runs again** | — |
| CRANE_4W_VS | [V26_CRANE_4W_VS.json](live/V26_CRANE_4W_VS.json) | omni-v26 | **runs again** | — |
| CRUISEKUBE | [V26_CRUISEKUBE.json](live/V26_CRUISEKUBE.json) | omni-v26 | **runs again** | — |
| CRUISEKUBE_RECORDER | [V26_CRUISEKUBE_RECORDER.json](live/V26_CRUISEKUBE_RECORDER.json) | omni-v26 | **runs again** | — |
| GODEL_4W_BARE | [V26_GODEL_4W_BARE.json](live/V26_GODEL_4W_BARE.json) | omni-v26 | **runs again** | — |
| GODEL_4W_BOTH | [V26_GODEL_4W_BOTH.json](live/V26_GODEL_4W_BOTH.json) | omni-v26 | **runs again** | — |
| GODEL_4W_ORCH | [V26_GODEL_4W_ORCH.json](live/V26_GODEL_4W_ORCH.json) | omni-v26 | **runs again** | — |
| GODEL_4W_TOP | [V26_GODEL_4W_TOP.json](live/V26_GODEL_4W_TOP.json) | omni-v26 | **runs again** | — |
| GODEL_4W_VS | [V26_GODEL_4W_VS.json](live/V26_GODEL_4W_VS.json) | omni-v26 | **runs again** | — |
| GOLDILOCKS | [V26_GOLDILOCKS.json](live/V26_GOLDILOCKS.json) | omni-v26 | **runs again** | — |
| KAI | [V26_KAI.json](live/V26_KAI.json) | omni-v26 | **runs again** | — |
| KAI_4W_BARE | [V26_KAI_4W_BARE.json](live/V26_KAI_4W_BARE.json) | omni-v26 | **runs again** | — |
| KAI_4W_BOTH | [V26_KAI_4W_BOTH.json](live/V26_KAI_4W_BOTH.json) | omni-v26 | **runs again** | — |
| KAI_4W_ORCH | [V26_KAI_4W_ORCH.json](live/V26_KAI_4W_ORCH.json) | omni-v26 | **runs again** | — |
| KAI_4W_TOP | [V26_KAI_4W_TOP.json](live/V26_KAI_4W_TOP.json) | omni-v26 | **runs again** | — |
| KAI_4W_VS | [V26_KAI_4W_VS.json](live/V26_KAI_4W_VS.json) | omni-v26 | **runs again** | — |
| KARMADA_4W_BARE | [V25_KARMADA_4W_BARE.json](live/V25_KARMADA_4W_BARE.json) | omni-v25 | **runs again** | — |
| KARMADA_4W_BOTH | [V25_KARMADA_4W_BOTH.json](live/V25_KARMADA_4W_BOTH.json) | omni-v25 | **runs again** | — |
| KARMADA_4W_ORCH | [V25_KARMADA_4W_ORCH.json](live/V25_KARMADA_4W_ORCH.json) | omni-v25 | **runs again** | — |
| KARMADA_4W_TOP | [V25_KARMADA_4W_TOP.json](live/V25_KARMADA_4W_TOP.json) | omni-v25 | **runs again** | — |
| KARMADA_4W_VS | [V25_KARMADA_4W_VS.json](live/V25_KARMADA_4W_VS.json) | omni-v25 | **runs again** | — |
| KEDA_CPU_REQUESTS | [V26_KEDA_CPU_REQUESTS.json](live/V26_KEDA_CPU_REQUESTS.json) | omni-v26 | **runs again** | — |
| KEDA_REQUESTS | [V26_KEDA_REQUESTS.json](live/V26_KEDA_REQUESTS.json) | omni-v26 | **runs again** | — |
| KOORDINATOR | [V26_KOORDINATOR.json](live/V26_KOORDINATOR.json) | omni-v26 | **runs again** | — |
| KOORDINATOR_4W_BARE | [V12_KOORDINATOR_4W_BARE.json](live/V12_KOORDINATOR_4W_BARE.json) | omni-v12 | **runs again** | — |
| KOORDINATOR_4W_BOTH | [V12_KOORDINATOR_4W_BOTH.json](live/V12_KOORDINATOR_4W_BOTH.json) | omni-v12 | **runs again** | — |
| KOORDINATOR_4W_ORCH | [V12_KOORDINATOR_4W_ORCH.json](live/V12_KOORDINATOR_4W_ORCH.json) | omni-v12 | **runs again** | — |
| KOORDINATOR_4W_TOP | [V12_KOORDINATOR_4W_TOP.json](live/V12_KOORDINATOR_4W_TOP.json) | omni-v12 | **runs again** | — |
| KOORDINATOR_4W_VS | [V12_KOORDINATOR_4W_VS.json](live/V12_KOORDINATOR_4W_VS.json) | omni-v12 | **runs again** | — |
| KOORDINATOR_CGROUP | [V26_KOORDINATOR_CGROUP.json](live/V26_KOORDINATOR_CGROUP.json) | omni-v26 | **runs again** | — |
| KUBERAY_4W_BARE | [V26_KUBERAY_4W_BARE.json](live/V26_KUBERAY_4W_BARE.json) | omni-v26 | **runs again** | — |
| KUBERAY_4W_BOTH | [V26_KUBERAY_4W_BOTH.json](live/V26_KUBERAY_4W_BOTH.json) | omni-v26 | **runs again** | — |
| KUBERAY_4W_ORCH | [V26_KUBERAY_4W_ORCH.json](live/V26_KUBERAY_4W_ORCH.json) | omni-v26 | **runs again** | — |
| KUBERAY_4W_TOP | [V26_KUBERAY_4W_TOP.json](live/V26_KUBERAY_4W_TOP.json) | omni-v26 | **runs again** | — |
| KUBERAY_4W_VS | [V26_KUBERAY_4W_VS.json](live/V26_KUBERAY_4W_VS.json) | omni-v26 | **runs again** | — |
| KUEUE | [V26_KUEUE.json](live/V26_KUEUE.json) | omni-v26 | **runs again** | — |
| KUEUE_4W_BARE | [V26_KUEUE_4W_BARE.json](live/V26_KUEUE_4W_BARE.json) | omni-v26 | **runs again** | — |
| KUEUE_4W_BOTH | [V26_KUEUE_4W_BOTH.json](live/V26_KUEUE_4W_BOTH.json) | omni-v26 | **runs again** | — |
| KUEUE_4W_ORCH | [V26_KUEUE_4W_ORCH.json](live/V26_KUEUE_4W_ORCH.json) | omni-v26 | **runs again** | — |
| KUEUE_4W_TOP | [V26_KUEUE_4W_TOP.json](live/V26_KUEUE_4W_TOP.json) | omni-v26 | **runs again** | — |
| KUEUE_4W_VS | [V26_KUEUE_4W_VS.json](live/V26_KUEUE_4W_VS.json) | omni-v26 | **runs again** | — |
| OCM_4W_BARE | [V26_OCM_4W_BARE.json](live/V26_OCM_4W_BARE.json) | omni-v26 | **runs again** | — |
| OCM_4W_BOTH | [V26_OCM_4W_BOTH.json](live/V26_OCM_4W_BOTH.json) | omni-v26 | **runs again** | — |
| OCM_4W_ORCH | [V26_OCM_4W_ORCH.json](live/V26_OCM_4W_ORCH.json) | omni-v26 | **runs again** | — |
| OCM_4W_TOP | [V26_OCM_4W_TOP.json](live/V26_OCM_4W_TOP.json) | omni-v26 | **runs again** | — |
| OCM_4W_VS | [V26_OCM_4W_VS.json](live/V26_OCM_4W_VS.json) | omni-v26 | **runs again** | — |
| VOLCANO | [V26_VOLCANO.json](live/V26_VOLCANO.json) | omni-v26 | **runs again** | — |
| VOLCANO_4W_BARE | [V25_VOLCANO_4W_BARE.json](live/V25_VOLCANO_4W_BARE.json) | omni-v25 | **runs again** | — |
| VOLCANO_4W_BOTH | [V25_VOLCANO_4W_BOTH.json](live/V25_VOLCANO_4W_BOTH.json) | omni-v25 | **runs again** | — |
| VOLCANO_4W_ORCH | [V25_VOLCANO_4W_ORCH.json](live/V25_VOLCANO_4W_ORCH.json) | omni-v25 | **runs again** | — |
| VOLCANO_4W_TOP | [V25_VOLCANO_4W_TOP.json](live/V25_VOLCANO_4W_TOP.json) | omni-v25 | **runs again** | — |
| VOLCANO_4W_VS | [V25_VOLCANO_4W_VS.json](live/V25_VOLCANO_4W_VS.json) | omni-v25 | **runs again** | — |

### Omni-Compass's own orchestrator (class L)

1 scenarios: 0 on omni-v27, 1 carry, 0 run again.

| Scenario | Its newest receipt | Its engine | On omni-v27 | Its rows by word (on the engine's own receipt) |
|---|---|---|---|---|
| THREE_ARMS_ABC | [V21_THREE_ARMS_ABC.json](orchestrator/V21_THREE_ARMS_ABC.json) | omni-v21 | **carries** | — |

### the data stores (class L)

13 scenarios: 0 on omni-v27, 13 carry, 0 run again.

| Scenario | Its newest receipt | Its engine | On omni-v27 | Its rows by word (on the engine's own receipt) |
|---|---|---|---|---|
| KAFKA | [V26_KAFKA.json](live/V26_KAFKA.json) | omni-v26 | **carries** | — |
| KAFKA_SERVICE | [V26_KAFKA_SERVICE.json](live/V26_KAFKA_SERVICE.json) | omni-v26 | **carries** | — |
| PGBENCH | [V26_PGBENCH.json](live/V26_PGBENCH.json) | omni-v26 | **carries** | — |
| PGBENCH_SERVICE | [V26_PGBENCH_SERVICE.json](live/V26_PGBENCH_SERVICE.json) | omni-v26 | **carries** | — |
| REDIS | [V26_REDIS.json](live/V26_REDIS.json) | omni-v26 | **carries** | — |
| REDIS_SERVICE | [V26_REDIS_SERVICE.json](live/V26_REDIS_SERVICE.json) | omni-v26 | **carries** | — |
| REDIS_SHIPPED | [V26_REDIS_SHIPPED.json](live/V26_REDIS_SHIPPED.json) | omni-v26 | **carries** | — |
| SYSBENCH | [V26_SYSBENCH.json](live/V26_SYSBENCH.json) | omni-v26 | **carries** | — |
| SYSBENCH_SERVICE | [V26_SYSBENCH_SERVICE.json](live/V26_SYSBENCH_SERVICE.json) | omni-v26 | **carries** | — |
| SYSBENCH_SHIPPED | [V26_SYSBENCH_SHIPPED.json](live/V26_SYSBENCH_SHIPPED.json) | omni-v26 | **carries** | — |
| YCSB | [V26_YCSB.json](live/V26_YCSB.json) | omni-v26 | **carries** | — |
| YCSB_SERVICE | [V26_YCSB_SERVICE.json](live/V26_YCSB_SERVICE.json) | omni-v26 | **carries** | — |
| YCSB_SHIPPED | [V26_YCSB_SHIPPED.json](live/V26_YCSB_SHIPPED.json) | omni-v26 | **carries** | — |

### the grid, the batteries and the robots (class L)

5 scenarios: 0 on omni-v27, 4 carry, 1 run again.

| Scenario | Its newest receipt | Its engine | On omni-v27 | Its rows by word (on the engine's own receipt) |
|---|---|---|---|---|
| CITYLEARN | [V26_CITYLEARN.md](live/V26_CITYLEARN.md) | omni-v26 | **carries** | — |
| MUJOCO | [V26_MUJOCO.md](live/V26_MUJOCO.md) | omni-v26 | **carries** | — |
| MUJOCO_PANDA | [V1_MUJOCO_PANDA.md](live/V1_MUJOCO_PANDA.md) | omni-v1 | **runs again** | — |
| PANDAPOWER | [V26_PANDAPOWER.md](live/V26_PANDAPOWER.md) | omni-v26 | **carries** | — |
| SWARM | [V26_SWARM.md](live/V26_SWARM.md) | omni-v26 | **carries** | — |

## 3. Wired, waiting for the founder's word

Every paid scenario is built and wired as the free ones are (the same governor, the same harness, the same reading); none starts until its switch is on (the founder's order of 15 November: no chip and no cloud until the mechanism is right).

| Cloud | Its queue | Switch | Its sets |
|---|---|---|---|
| alibaba | `scripts/alibaba_queue.txt` | **off** | steady; burst 1 4 1 6 1 9; burst 1 6 1 8 1 6; the real day on 1 to 9 |
| amazon | `scripts/amazon_queue.txt` | **off** | steady; burst 1 4 1 6 1 9; burst 1 6 1 8 1 6; the real day on 1 to 9 |
| azure | `scripts/azure_queue.txt` | **off** | work meter tuning case; work meter tuning case 2; work meter |
| digitalocean | `scripts/digitalocean_queue.txt` | **off** | steady; burst 1 4 1 6 1 9; burst 1 6 1 8 1 6; the real day on 1 to 9 |
| google | `scripts/google_queue.txt` | **off** | steady; burst 1 4 1 6 1 9; burst 1 6 1 8 1 6; the real day on 1 to 9 |
| ibm | `scripts/ibm_queue.txt` | **off** | steady; burst 1 4 1 6 1 9; burst 1 6 1 8 1 6; the real day on 1 to 9 |
| linode | `scripts/linode_queue.txt` | **off** | steady; burst 1 4 1 6 1 9; burst 1 6 1 8 1 6; the real day on 1 to 9 |
| oracle | `scripts/oracle_queue.txt` | **off** | steady; burst 1 4 1 6 1 9; burst 1 6 1 8 1 6; the real day on 1 to 9 |

| Chip workflow | What it runs | Wired |
|---|---|---|
| `aws-gpu.yml` | Amazon, one card (g5.xlarge): probe, then one card at 1, 10 and 100 copies | yes, started only by hand |
| `lambda-gpu.yml` | Lambda: the A10 and A100 cards, the organisms on the chip | yes, started only by hand |
| `gpu-bench.yml` | the card benchmark on a machine the founder attaches | yes, started only by hand |

## 4. Our own models (class S, never proof)

Modelled beside the real runs, never counted as a receipt of a real machine: every organism three ways with the jump generator and the Monte Carlo, each version's model gate.

| Record | What it holds |
|---|---|
| `results/realms_v5` | the 1,107 muscles and the seven organisms, native, Omni-Compass on native and by itself |
| `results/orchestra` | the orchestra: every governor's and orchestrator's muscles |
| `results/orchestrator` | Omni-Compass's own orchestrator, the three arms |
| `results/RUNS_LEDGER.md` | the Python's runs and the core's Monte Carlo from the jump generator, with the C++ twin |
| `results/model_gate` | the model gate: each version against the one before |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
