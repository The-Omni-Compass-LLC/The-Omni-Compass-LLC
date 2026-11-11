# The governors and orchestrators: native under them, Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

The founder's list of 19 October, night: every governor and orchestrator he named runs with the organism native under it, then with Omni-Compass on top of it, on the engine that stands (omni-v26); a governor whose three runs have not yet landed whole on it reads from its newest engine's table, named in the table's file and in its runs line. The organism is a six-worker real Kubernetes cluster (kind v0.31.0, Kubernetes v1.35.0) on GitHub's machines, each arm on a fresh cluster, the two arms back to back on one runner, ten paired repetitions a run, three runs (A, B and C) for a reading. Native is the governor as its project ships it; Omni-Compass sits on top with its own levers (the node pool, the service's autoscaler and processor limit, cruise and idle) and never writes the governor's objects, but where the governor owns the service's autoscaler (Crane): there its autoscaler moves reach the autoscaler through the governor's own object, by a plug, as on KEDA. Crane runs on Kubernetes 1.25.16 (its HPA is an API 1.26 removed) and Gödel on 1.24.17 (its supported range), where no pod is resized in place, so no processor limit is moved in any of their arms. Cost: $0 (GitHub's free machines). A governor's line reads only from its own three-run table; until then it says where its runs stand.

| Governor | What it governs | Register row | Where it stands | Readings (A, B and C) |
|---|---|---:|---|---|
| The Kubernetes scheduler (vanilla, and its bin-packing profile) | pod placement | 88 | as shipped: three runs in on omni-v26; bin-packing profile: three runs in on omni-v26 | as shipped: 5 GAIN, 9 LOSS, 2 power given, 5 STEADY, 1 where the runs disagree ([table](V26_VANILLA.md), omni-v26); bin-packing profile: 6 GAIN, 9 LOSS, 2 power given, 4 STEADY, 1 where the runs disagree ([table](V26_BINPACK.md), omni-v26) |
| Kueue | batch admission (a job at a time, by queue quota) | 63 | three runs in on omni-v26 | 5 GAIN, 10 LOSS, 2 power given, 4 STEADY, 1 where the runs disagree ([table](V26_KUEUE.md), omni-v26) |
| Volcano | batch scheduling (queues, gangs) | 63 | three runs in on omni-v26 | 4 GAIN, 9 LOSS, 2 power given, 5 STEADY, 2 where the runs disagree ([table](V26_VOLCANO.md), omni-v26) |
| KAI scheduler | AI workload scheduling (queues, fair share, gangs) | 91 | three runs in on omni-v26 | 4 GAIN, 7 LOSS, 2 power given, 4 STEADY, 5 where the runs disagree ([table](V26_KAI.md), omni-v26) |
| Koordinator | QoS colocation (batch work on what latency-sensitive pods leave unused) | 89 | three runs in on omni-v26 | 4 GAIN, 5 LOSS, 0 power given, 4 STEADY, 8 where the runs disagree ([table](V26_KOORDINATOR.md), omni-v26) |
| CruiseKube | rightsizing (requests and limits, in place) | 81 | three runs in on omni-v26 | 3 GAIN, 5 LOSS, 1 power given, 5 STEADY, 2 where the runs disagree ([table](V26_CRUISEKUBE.md), omni-v26) |
| Crane | predictive autoscaling and resource governance | 90 | four ways: three runs in on omni-v26 | read four ways (below) |
| KubeRay | Ray clusters (the Ray autoscaler) | 92 | four ways: three runs in on omni-v26 | read four ways (below) |
| Gödel scheduler | unified online and offline scheduling | 93 | four ways: three runs in on omni-v26 | read four ways (below) |
| Armada | multi-cluster batch | 94 | four ways: three runs in on omni-v25 | read four ways (below) |
| Karmada | multi-cluster placement | 95 | four ways: three runs in on omni-v25 | read four ways (below) |
| Open Cluster Management | multi-cluster management | 96 | four ways: three runs in on omni-v26 | read four ways (below) |
| KubeEdge | edge nodes | 97 | its rig is not yet built | not yet run |
| Nephio | network-function automation | 98 | its rig is not yet built | not yet run |

## The four ways (the founder's order of 20 October)

Each system runs four ways in every repetition, each way on a fresh cluster of the same configuration, back to back on one runner, the governor on its own core (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendments 5 and 6): the organism alone (the stream placed by Kubernetes' own scheduler, no orchestrator installed; for Crane, the service's HPA as Kubernetes ships it, `docs/CRANE_PREREGISTRATION.md`), the orchestrator as its project ships it, Omni-Compass on top of the organism alone, and Omni-Compass on top of the orchestrator. Each column is one comparison, the first against the second, paired within the repetition and read by the one key for the first; each cell reads only from its own three-run table. Omni-Compass never places a pod or admits a job: on the organism alone it sits on top of Kubernetes' own scheduler.

| System | Runs (A, B and C) | Omni-Compass on top of it, against it as shipped | it as shipped, against the organism alone | Omni-Compass on the organism alone, against the organism alone | Omni-Compass on the organism alone, against it as shipped | Omni-Compass on top of it, against the organism alone |
|---|---|---|---|---|---|---|
| The KAI scheduler | A [42442968048](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42442968048) (10 pairs), B [42444104246](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42444104246) (10 pairs), C [42445176352](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42445176352) (10 pairs); omni-v26 | 5 GAIN, 9 LOSS, 2 power given, 4 STEADY, 2 where the runs disagree ([table](V26_KAI_4W_TOP.md), omni-v26) | 1 GAIN, 10 LOSS, 2 power given, 8 STEADY, 1 where the runs disagree ([table](V26_KAI_4W_ORCH.md), omni-v26) | 6 GAIN, 8 LOSS, 2 power given, 5 STEADY, 1 where the runs disagree ([table](V26_KAI_4W_BARE.md), omni-v26) | 12 GAIN, 4 LOSS, 2 power given, 4 STEADY, 0 where the runs disagree ([table](V26_KAI_4W_VS.md), omni-v26) | 4 GAIN, 11 LOSS, 2 power given, 4 STEADY, 1 where the runs disagree ([table](V26_KAI_4W_BOTH.md), omni-v26) |
| Koordinator | A [39368366066](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/39368366066) (10 pairs), B [39368373713](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/39368373713) (10 pairs), C [39368380786](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/39368380786) (10 pairs); omni-v12; on omni-v26: [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41809048789) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41810789445) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41812570543), its three runs not yet whole | 7 GAIN, 3 LOSS, 0 power given, 4 STEADY, 8 where the runs disagree ([table](V12_KOORDINATOR_4W_TOP.md), omni-v12) | 5 GAIN, 5 LOSS, 0 power given, 8 STEADY, 4 where the runs disagree ([table](V12_KOORDINATOR_4W_ORCH.md), omni-v12) | 6 GAIN, 3 LOSS, 0 power given, 6 STEADY, 7 where the runs disagree ([table](V12_KOORDINATOR_4W_BARE.md), omni-v12) | 9 GAIN, 5 LOSS, 0 power given, 4 STEADY, 4 where the runs disagree ([table](V12_KOORDINATOR_4W_VS.md), omni-v12) | 10 GAIN, 6 LOSS, 1 power given, 4 STEADY, 1 where the runs disagree ([table](V12_KOORDINATOR_4W_BOTH.md), omni-v12) |
| Kueue | A [42442976725](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42442976725) (10 pairs), B [42445165273](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42445165273) (10 pairs), C [42445184360](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42445184360) (10 pairs); omni-v26 | 5 GAIN, 9 LOSS, 2 power given, 5 STEADY, 1 where the runs disagree ([table](V26_KUEUE_4W_TOP.md), omni-v26) | 0 GAIN, 9 LOSS, 0 power given, 9 STEADY, 4 where the runs disagree ([table](V26_KUEUE_4W_ORCH.md), omni-v26) | 5 GAIN, 9 LOSS, 2 power given, 5 STEADY, 1 where the runs disagree ([table](V26_KUEUE_4W_BARE.md), omni-v26) | 7 GAIN, 6 LOSS, 2 power given, 6 STEADY, 1 where the runs disagree ([table](V26_KUEUE_4W_VS.md), omni-v26) | 4 GAIN, 10 LOSS, 2 power given, 5 STEADY, 1 where the runs disagree ([table](V26_KUEUE_4W_BOTH.md), omni-v26) |
| Volcano | A [41809087487](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41809087487) (10 pairs), B [41812541481](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41812541481) (10 pairs), C [41814366715](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41814366715) (10 pairs); omni-v25; on omni-v26: [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41809087487) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41812541481) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41814366715), its three runs not yet whole | 4 GAIN, 8 LOSS, 2 power given, 4 STEADY, 4 where the runs disagree ([table](V25_VOLCANO_4W_TOP.md), omni-v25) | 7 GAIN, 6 LOSS, 1 power given, 8 STEADY, 0 where the runs disagree ([table](V25_VOLCANO_4W_ORCH.md), omni-v25) | 5 GAIN, 9 LOSS, 2 power given, 4 STEADY, 2 where the runs disagree ([table](V25_VOLCANO_4W_BARE.md), omni-v25) | 6 GAIN, 7 LOSS, 2 power given, 5 STEADY, 2 where the runs disagree ([table](V25_VOLCANO_4W_VS.md), omni-v25) | 7 GAIN, 9 LOSS, 2 power given, 4 STEADY, 0 where the runs disagree ([table](V25_VOLCANO_4W_BOTH.md), omni-v25) |
| The scheduler's bin-packing profile | A [42444100547](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42444100547) (10 pairs), B [42445172518](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42445172518) (10 pairs), C [42446289715](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42446289715) (10 pairs); omni-v26 | 4 GAIN, 7 LOSS, 2 power given, 5 STEADY, 4 where the runs disagree ([table](V26_BINPACK_4W_TOP.md), omni-v26) | 4 GAIN, 2 LOSS, 1 power given, 10 STEADY, 5 where the runs disagree ([table](V26_BINPACK_4W_ORCH.md), omni-v26) | 6 GAIN, 10 LOSS, 2 power given, 4 STEADY, 0 where the runs disagree ([table](V26_BINPACK_4W_BARE.md), omni-v26) | 4 GAIN, 8 LOSS, 2 power given, 6 STEADY, 2 where the runs disagree ([table](V26_BINPACK_4W_VS.md), omni-v26) | 8 GAIN, 7 LOSS, 2 power given, 4 STEADY, 1 where the runs disagree ([table](V26_BINPACK_4W_BOTH.md), omni-v26) |
| KubeRay | A [42447364135](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42447364135) (10 pairs), B [42450495106](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42450495106) (10 pairs), C [42452536842](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42452536842) (10 pairs); omni-v26 | 4 GAIN, 7 LOSS, 2 power given, 4 STEADY, 5 where the runs disagree ([table](V26_KUBERAY_4W_TOP.md), omni-v26) | 0 GAIN, 8 LOSS, 2 power given, 6 STEADY, 6 where the runs disagree ([table](V26_KUBERAY_4W_ORCH.md), omni-v26) | 5 GAIN, 9 LOSS, 2 power given, 5 STEADY, 1 where the runs disagree ([table](V26_KUBERAY_4W_BARE.md), omni-v26) | 13 GAIN, 2 LOSS, 2 power given, 3 STEADY, 2 where the runs disagree ([table](V26_KUBERAY_4W_VS.md), omni-v26) | 3 GAIN, 10 LOSS, 4 power given, 3 STEADY, 2 where the runs disagree ([table](V26_KUBERAY_4W_BOTH.md), omni-v26) |
| Crane | A [42447367322](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42447367322) (10 pairs), B [42450499095](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42450499095) (10 pairs), C [42452540225](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42452540225) (10 pairs); omni-v26 | 4 GAIN, 2 LOSS, 2 power given, 7 STEADY, 1 where the runs disagree ([table](V26_CRANE_4W_TOP.md), omni-v26) | 1 GAIN, 2 LOSS, 0 power given, 8 STEADY, 5 where the runs disagree ([table](V26_CRANE_4W_ORCH.md), omni-v26) | 5 GAIN, 1 LOSS, 2 power given, 7 STEADY, 1 where the runs disagree ([table](V26_CRANE_4W_BARE.md), omni-v26) | 7 GAIN, 1 LOSS, 2 power given, 5 STEADY, 1 where the runs disagree ([table](V26_CRANE_4W_VS.md), omni-v26) | 0 GAIN, 3 LOSS, 4 power given, 5 STEADY, 4 where the runs disagree ([table](V26_CRANE_4W_BOTH.md), omni-v26) |
| The Gödel scheduler | A [42447370557](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42447370557) (10 pairs), B [42451531911](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42451531911) (10 pairs), C [42452543740](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42452543740) (10 pairs); omni-v26 | 4 GAIN, 8 LOSS, 2 power given, 4 STEADY, 4 where the runs disagree ([table](V26_GODEL_4W_TOP.md), omni-v26) | 2 GAIN, 7 LOSS, 2 power given, 8 STEADY, 3 where the runs disagree ([table](V26_GODEL_4W_ORCH.md), omni-v26) | 4 GAIN, 10 LOSS, 2 power given, 5 STEADY, 1 where the runs disagree ([table](V26_GODEL_4W_BARE.md), omni-v26) | 5 GAIN, 6 LOSS, 2 power given, 5 STEADY, 4 where the runs disagree ([table](V26_GODEL_4W_VS.md), omni-v26) | 4 GAIN, 9 LOSS, 2 power given, 4 STEADY, 3 where the runs disagree ([table](V26_GODEL_4W_BOTH.md), omni-v26) |
| Karmada | A [41816173049](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41816173049) (10 pairs), B [41823821537](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41823821537) (10 pairs), C [41828260509](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41828260509) (10 pairs); omni-v25; on omni-v26: [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41816173049) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41823821537) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41828260509), its three runs not yet whole | 4 GAIN, 12 LOSS, 2 power given, 4 STEADY, 0 where the runs disagree ([table](V25_KARMADA_4W_TOP.md), omni-v25) | 1 GAIN, 10 LOSS, 0 power given, 8 STEADY, 3 where the runs disagree ([table](V25_KARMADA_4W_ORCH.md), omni-v25) | 4 GAIN, 11 LOSS, 2 power given, 4 STEADY, 1 where the runs disagree ([table](V25_KARMADA_4W_BARE.md), omni-v25) | 13 GAIN, 3 LOSS, 2 power given, 4 STEADY, 0 where the runs disagree ([table](V25_KARMADA_4W_VS.md), omni-v25) | 4 GAIN, 12 LOSS, 2 power given, 4 STEADY, 0 where the runs disagree ([table](V25_KARMADA_4W_BOTH.md), omni-v25) |
| Open Cluster Management | A [42447377308](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42447377308) (10 pairs), B [42452533513](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42452533513) (10 pairs), C [42453594917](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42453594917) (10 pairs); omni-v26 | 4 GAIN, 10 LOSS, 2 power given, 3 STEADY, 3 where the runs disagree ([table](V26_OCM_4W_TOP.md), omni-v26) | 0 GAIN, 12 LOSS, 0 power given, 8 STEADY, 2 where the runs disagree ([table](V26_OCM_4W_ORCH.md), omni-v26) | 5 GAIN, 10 LOSS, 2 power given, 4 STEADY, 1 where the runs disagree ([table](V26_OCM_4W_BARE.md), omni-v26) | 13 GAIN, 2 LOSS, 2 power given, 4 STEADY, 1 where the runs disagree ([table](V26_OCM_4W_VS.md), omni-v26) | 4 GAIN, 12 LOSS, 2 power given, 3 STEADY, 1 where the runs disagree ([table](V26_OCM_4W_BOTH.md), omni-v26) |
| Armada | A [41828277526](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41828277526) (10 pairs), B [41830587387](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41830587387) (10 pairs), C [41830595635](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41830595635) (10 pairs); omni-v25; on omni-v26: [A](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41828277526) [B](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41830587387) [C](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/41830595635), its three runs not yet whole | 6 GAIN, 3 LOSS, 2 power given, 10 STEADY, 0 where the runs disagree ([table](V25_ARMADA_4W_TOP.md), omni-v25) | 7 GAIN, 5 LOSS, 2 power given, 5 STEADY, 2 where the runs disagree ([table](V25_ARMADA_4W_ORCH.md), omni-v25) | 4 GAIN, 12 LOSS, 2 power given, 4 STEADY, 0 where the runs disagree ([table](V25_ARMADA_4W_BARE.md), omni-v25) | 8 GAIN, 8 LOSS, 3 power given, 2 STEADY, 0 where the runs disagree ([table](V25_ARMADA_4W_VS.md), omni-v25) | 9 GAIN, 7 LOSS, 2 power given, 3 STEADY, 0 where the runs disagree ([table](V25_ARMADA_4W_BOTH.md), omni-v25) |

## The orchestra, the eighth organism (modelled, class S)

The founder's word of 19 October, night: the governors in a catalog group, an organism of their own. Every catalog muscle that stands for a governor's knob (below, under each governor) runs in the modelled organisms as the seven do: each governor's muscles as a body of its own, then all of them together as one body, the orchestra, native and then with Omni-Compass on top at the max, on omni-v12, seeds 3000-3009. A model, not a measurement of the governor itself; every row: [`results/orchestra/ORCHESTRA.md`](../orchestra/ORCHESTRA.md).

| Body | Muscles | Own load | The climb | Work in line |
|---|---:|---|---|---|
| The Kubernetes scheduler (vanilla, and its bin-packing profile) | 12 | GAIN (fewer misses) | GAIN (fewer misses) | GAIN (fewer misses) |
| Kueue | 5 | STEADY (the same as native) | STEADY (the same as native) | STEADY (the same as native) |
| Volcano | 5 | STEADY (the same as native) | STEADY (the same as native) | STEADY (the same as native) |
| KAI scheduler | 4 | STEADY (the same as native) | STEADY (the same as native) | STEADY (the same as native) |
| Koordinator | 4 | STEADY (the same as native) | STEADY (the same as native) | STEADY (the same as native) |
| CruiseKube | 4 | GAIN (fewer misses) | GAIN (fewer misses) | GAIN (fewer misses) |
| Crane | 5 | GAIN (fewer misses) | GAIN (fewer misses) | GAIN (fewer misses) |
| KubeRay | 3 | STEADY (the same as native) | STEADY (the same as native) | STEADY (the same as native) |
| Gödel scheduler | 4 | STEADY (the same as native) | STEADY (the same as native) | STEADY (the same as native) |
| Armada | 3 | GAIN (fewer misses) | GAIN (more work + fewer misses) | GAIN (fewer misses) |
| Karmada | 4 | GAIN (more work + fewer misses) | GAIN (more work + fewer misses) | GAIN (fewer misses) |
| Open Cluster Management | 3 | GAIN (more work + fewer misses) | GAIN (more work + fewer misses) | GAIN (more work + fewer misses) |
| KubeEdge | 4 | GAIN (fewer misses) | GAIN (more work + fewer misses) | GAIN (fewer misses) |
| Nephio | 4 | GAIN (fewer misses) | GAIN (more work + fewer misses) | GAIN (fewer misses) |
| **The orchestra, every governor's muscle once** | 55 | **GAIN (more work + fewer misses)** | **GAIN (more work + fewer misses)** | **GAIN (more work + fewer misses)** |

## The orchestrators on the same organisms, with the same injection (modelled, class S): the third arm

The founder's order of 25 October: every orchestrator on the same organisms with the same injection, and Omni-Compass on top of each. 12 injections in two settings (the kind rig and the cloud), 8 repetitions, every arm of a repetition meeting the same random numbers; each orchestrator's rule written from its own release; Omni-Compass the shipped governor of omni-v19. A model, never a measurement of the orchestrator itself; every organism and gauge: [`results/orchestrators/ORCHESTRATORS.md`](../orchestrators/ORCHESTRATORS.md).

| Orchestrator | Setting | Against Kubernetes alone | Omni-Compass on top of it, against it |
|---|---|---|---|
| the Kubernetes scheduler as shipped (the organism alone) | on-site | it is native | 21 GAIN, 2 LOSS, 0 power given, 63 STEADY |
| the Kubernetes scheduler as shipped (the organism alone) | cloud | it is native | 0 GAIN, 0 LOSS, 1 power given, 85 STEADY |
| the Kubernetes scheduler's bin-packing profile | on-site | 0 GAIN, 0 LOSS, 0 power given, 86 STEADY | 21 GAIN, 2 LOSS, 0 power given, 63 STEADY |
| the Kubernetes scheduler's bin-packing profile | cloud | 1 GAIN, 2 LOSS, 3 power given, 80 STEADY | 0 GAIN, 0 LOSS, 1 power given, 85 STEADY |
| Volcano v1.16.0 | on-site | 0 GAIN, 0 LOSS, 0 power given, 86 STEADY | 21 GAIN, 2 LOSS, 0 power given, 63 STEADY |
| Volcano v1.16.0 | cloud | 6 GAIN, 20 LOSS, 2 power given, 58 STEADY | 0 GAIN, 1 LOSS, 0 power given, 85 STEADY |
| Kueue v0.20.2 | on-site | 0 GAIN, 5 LOSS, 0 power given, 81 STEADY | 21 GAIN, 2 LOSS, 0 power given, 63 STEADY |
| Kueue v0.20.2 | cloud | 2 GAIN, 6 LOSS, 0 power given, 78 STEADY | 0 GAIN, 0 LOSS, 0 power given, 86 STEADY |
| the KAI scheduler v0.18.6 | on-site | 0 GAIN, 0 LOSS, 0 power given, 86 STEADY | 20 GAIN, 2 LOSS, 0 power given, 64 STEADY |
| the KAI scheduler v0.18.6 | cloud | 4 GAIN, 37 LOSS, 7 power given, 38 STEADY | 0 GAIN, 0 LOSS, 0 power given, 86 STEADY |
| Koordinator 1.8.0 | on-site | 4 GAIN, 3 LOSS, 1 power given, 78 STEADY | 20 GAIN, 0 LOSS, 0 power given, 66 STEADY |
| Koordinator 1.8.0 | cloud | 0 GAIN, 7 LOSS, 6 power given, 73 STEADY | 0 GAIN, 0 LOSS, 0 power given, 86 STEADY |

## The Kubernetes scheduler (vanilla, and its bin-packing profile)

- **Native**: the default scheduler of Kubernetes 1.35 as shipped, which places every pod of every Kubernetes set; and the same release's scheduler with the operator's bin-packing profile (NodeResourcesFit, MostAllocated).
- **Its test on real Kubernetes (class L)**: the batch stream placed by the scheduler alone, in each setting (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 3); register row 88.
- **In the catalog (modelled, class S)**: family 4, Kubernetes Placement & Scheduling (21 muscles, in the spine and every realm): `node_selector`, `node_affinity`, `pod_anti_affinity`, `topology_spread`, `taint_toleration`, `priority_class`, `preemption_policy`, `scheduler_backoff`, `scheduler_scoring_strategy`, `scheduler_plugin_weights`, `scheduling_gates`, `deschedule`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (fewer misses); work in line: GAIN (fewer misses).
- **Runs (as shipped)**: A [42439656396](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42439656396) (10 pairs), B [42439664303](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42439664303) (10 pairs), C [42440709856](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42440709856) (10 pairs); engine omni-v26 (digest 75d3c22eed4473b9, 65 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| queue: job turnaround, submitted to done, mean (s) | LOSS in all three of our runs |
| queue: jobs unfinished at the window's end | STEADY, the same |
| batch: queue finished (s) | LOSS by the mean of our three runs, beyond the noise in 2 of 3 |
| batch: worker machines in service after the queue finished, mean | GAIN in all three of our runs |
| worker nodes in service, mean | GAIN in all three of our runs |
| node-hours | GAIN in all three of our runs |
| energy, parked workers still on at idle power (Wh) | STEADY, under the floor (the three runs' mean 0.05%) |
| energy (Wh) | GAIN in all three of our runs |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| response time (ms), 95th percentile | LOSS in all three of our runs |
| failed requests (%) | STEADY, the same |

Every row of the run: [`results/live/V26_VANILLA.md`](V26_VANILLA.md).

- **Runs (bin-packing profile)**: A [42439660401](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42439660401) (10 pairs), B [42440706098](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42440706098) (10 pairs), C [42440713360](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42440713360) (10 pairs); engine omni-v26 (digest 75d3c22eed4473b9, 65 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| queue: job turnaround, submitted to done, mean (s) | LOSS in all three of our runs |
| queue: jobs unfinished at the window's end | STEADY, the same |
| batch: queue finished (s) | LOSS in all three of our runs |
| batch: worker machines in service after the queue finished, mean | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| worker nodes in service, mean | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| node-hours | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| energy, parked workers still on at idle power (Wh) | STEADY, under the floor (the three runs' mean 0.06%) |
| energy (Wh) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| response time (ms), 95th percentile | LOSS by the mean of our three runs, beyond the noise in 2 of 3 |
| failed requests (%) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |

Every row of the run: [`results/live/V26_BINPACK.md`](V26_BINPACK.md).


## Kueue

- **Native**: Kueue v0.20.2 with the operator's single ClusterQueue sized to the workers.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`; register row 63.
- **In the catalog (modelled, class S)**: family 1, Work Admission & Demand Shaping (19 muscles, in its realm and the whole tower): `job_admission`, `batch_admission`, `queue_concurrency`, `queue_backpressure`, `tenant_admission`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: STEADY (the same as native); the climb: STEADY (the same as native); work in line: STEADY (the same as native).
- **Runs**: A [42412690276](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42412690276) (10 pairs), B [42422950496](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42422950496) (10 pairs), C [42432716761](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42432716761) (10 pairs); engine omni-v26 (digest 75d3c22eed4473b9, 65 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | LOSS by the mean of our three runs, beyond the noise in 1 of 3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| queue: job turnaround, submitted to done, mean (s) | LOSS in all three of our runs |
| queue: jobs unfinished at the window's end | STEADY, the same |
| batch: queue finished (s) | LOSS by the mean of our three runs, beyond the noise in 2 of 3 |
| batch: worker machines in service after the queue finished, mean | GAIN in all three of our runs |
| worker nodes in service, mean | GAIN in all three of our runs |
| node-hours | GAIN in all three of our runs |
| energy, parked workers still on at idle power (Wh) | STEADY, under the floor (the three runs' mean 0.06%) |
| energy (Wh) | GAIN in all three of our runs |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| response time (ms), 95th percentile | LOSS by the mean of our three runs, beyond the noise in 1 of 3 |
| failed requests (%) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |

Every row of the run: [`results/live/V26_KUEUE.md`](V26_KUEUE.md).


## Volcano

- **Native**: Volcano v1.16.0 with its default queue as shipped.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`; register row 63.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `gang_schedule`, `queue_fairness`, `task_priority`, `task_preemption`, `binpack_pressure`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: STEADY (the same as native); the climb: STEADY (the same as native); work in line: STEADY (the same as native).
- **Runs**: A [42412695021](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42412695021) (10 pairs), B [42422954360](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42422954360) (10 pairs), C [42432720979](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42432720979) (10 pairs); engine omni-v26 (digest 75d3c22eed4473b9, 65 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | the runs disagree |
| queue: job turnaround, submitted to done, mean (s) | LOSS by the mean of our three runs, beyond the noise in 2 of 3 |
| queue: jobs unfinished at the window's end | STEADY, the same |
| batch: queue finished (s) | LOSS by the mean of our three runs, beyond the noise in 2 of 3 |
| batch: worker machines in service after the queue finished, mean | GAIN in all three of our runs |
| worker nodes in service, mean | GAIN in all three of our runs |
| node-hours | GAIN in all three of our runs |
| energy, parked workers still on at idle power (Wh) | STEADY, under the floor (the three runs' mean 0.02%) |
| energy (Wh) | GAIN in all three of our runs |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | the runs disagree |
| response time (ms), 95th percentile | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |

Every row of the run: [`results/live/V26_VOLCANO.md`](V26_VOLCANO.md).


## KAI scheduler

- **Native**: the KAI scheduler v0.18.6 with its chart's default queues.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 1; register row 91.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `gang_schedule`, `queue_fairness`, `cluster_quota`, `task_preemption`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: STEADY (the same as native); the climb: STEADY (the same as native); work in line: STEADY (the same as native).
- **Runs**: A [42438540677](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42438540677) (10 pairs), B [42438544638](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42438544638) (10 pairs), C [42438548043](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42438548043) (10 pairs); engine omni-v26 (digest 75d3c22eed4473b9, 65 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | the runs disagree |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | the runs disagree |
| queue: job turnaround, submitted to done, mean (s) | LOSS by the mean of our three runs, beyond the noise in 1 of 3 |
| queue: jobs unfinished at the window's end | STEADY, the same |
| batch: queue finished (s) | LOSS by the mean of our three runs, beyond the noise in 1 of 3 |
| batch: worker machines in service after the queue finished, mean | GAIN in all three of our runs |
| worker nodes in service, mean | GAIN in all three of our runs |
| node-hours | GAIN in all three of our runs |
| energy, parked workers still on at idle power (Wh) | STEADY, under the floor (the three runs' mean 0.07%) |
| energy (Wh) | GAIN in all three of our runs |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | the runs disagree |
| response time (ms), 95th percentile | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |

Every row of the run: [`results/live/V26_KAI.md`](V26_KAI.md).


## Koordinator

- **Native**: Koordinator 1.8.0, colocation on as shipped, the operator's colocation profile.
- **Its test on real Kubernetes (class L)**: `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 2; register row 89.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `oversubscription`, `resource_reclaim`, `binpack_pressure`, `spread_pressure`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: STEADY (the same as native); the climb: STEADY (the same as native); work in line: STEADY (the same as native).
- **Runs**: A [42438551739](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42438551739) (10 pairs), B [42439648015](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42439648015) (10 pairs), C [42439651965](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42439651965) (10 pairs); engine omni-v26 (digest 75d3c22eed4473b9, 65 files).

| Gauge | Reading |
|---|---|
| queue: job wait, submitted to its first pod running, mean (s) | LOSS by the mean of our three runs, beyond the noise in 2 of 3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | LOSS by the mean of our three runs, beyond the noise in 2 of 3 |
| queue: job turnaround, submitted to done, mean (s) | the runs disagree |
| queue: jobs unfinished at the window's end | the runs disagree |
| batch: queue finished (s) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| worker nodes in service, mean | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| node-hours | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| energy, parked workers still on at idle power (Wh) | STEADY, under the floor (the three runs' mean 0.19%) |
| energy (Wh) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | GAIN in all three of our runs |
| response time (ms), 95th percentile | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| failed requests (%) | STEADY, the same |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | the runs disagree |

Every row of the run: [`results/live/V26_KOORDINATOR.md`](V26_KOORDINATOR.md).


## CruiseKube

- **Native**: CruiseKube applying its own recommendations as shipped.
- **Its test on real Kubernetes (class L)**: `docs/CRUISEKUBE_PREREGISTRATION.md`; register row 81.
- **In the catalog (modelled, class S)**: family 3, Container Resources (25 muscles, in the spine and every realm): `cruisekube_request_rightsizing`, `in_place_resize`, `cpu_request`, `memory_request`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (fewer misses); work in line: GAIN (fewer misses).
- **Runs**: A [42403615734](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42403615734) (10 pairs), B [42413970707](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42413970707) (10 pairs), C [42425416413](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/42425416413) (10 pairs); engine omni-v26 (digest 75d3c22eed4473b9, 65 files).

| Gauge | Reading |
|---|---|
| worker nodes in service, mean | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| node-hours | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| energy, parked workers still on at idle power (Wh) | STEADY, under the floor (the three runs' mean 0.11%) |
| energy (Wh) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| energy per core-hour (Wh) | shown, not judged |
| response time (ms), mean | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| response time (ms), 95th percentile | LOSS by the mean of our three runs, beyond the noise in 2 of 3 |
| failed requests (%) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | STEADY, the same |

Every row of the run: [`results/live/V26_CRUISEKUBE.md`](V26_CRUISEKUBE.md).


## Crane

- **Native**: Crane 0.11.0 and the Prometheus it reads, as its installation guide installs them, the service's autoscaler handed to its Effective HPA in auto mode (its own example for this service), on Kubernetes 1.25.16 (Crane builds its HPA as autoscaling/v2beta2, which 1.26 removed).
- **Its test on real Kubernetes (class L)**: the served app under the closed load of the add-on sets, four ways (`docs/CRANE_PREREGISTRATION.md`); register row 90.
- **In the catalog (modelled, class S)**: family 2, Kubernetes Workload Scaling (32 muscles, in the spine and every realm): `hpa_cpu_target`, `hpa_custom_target`, `hpa_scaling_rate_policies`, `hpa_min_replicas`, `hpa_max_replicas`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## KubeRay

- **Native**: KubeRay 1.7.1 and one Ray cluster (Ray 2.52.0) from KubeRay's own autoscaling sample, the Ray autoscaler as shipped.
- **Its test on real Kubernetes (class L)**: the batch stream as Ray jobs (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 7); register row 92.
- **In the catalog (modelled, class S)**: family 12, AI Training (18 muscles, in its realm and the whole tower): `training_workers`, `elastic_worker_count`, `training_gang_size`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: STEADY (the same as native); the climb: STEADY (the same as native); work in line: STEADY (the same as native).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Gödel scheduler

- **Native**: the Gödel scheduler built from its pinned source and deployed by its own manifests, its placement as shipped, on Kubernetes 1.24.17 (it supports 1.21.4 to 1.24.6).
- **Its test on real Kubernetes (class L)**: the batch stream placed by Gödel, four ways (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 8); register row 93.
- **In the catalog (modelled, class S)**: family 14, Distributed Cluster Managers (15 muscles, in its realm and the whole tower): `gang_schedule`, `task_admission`, `binpack_pressure`, `resource_reservation`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: STEADY (the same as native); the climb: STEADY (the same as native); work in line: STEADY (the same as native).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Armada

- **Native**: Armada v0.22.14 as its own local stack runs it (its server, scheduler, ingesters, Pulsar, Redis and PostgreSQL as containers on the runner, one executor per member cluster), one queue, each batch of the stream a job set of its pods.
- **Its test on real Kubernetes (class L)**: the batch stream sent to a group of two clusters through Armada's queue, four ways (`docs/GROUP_PREREGISTRATION.md`, amendment 2); register row 94.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `multi_cluster_dispatch`, `federation_quota`, `global_admission`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Karmada

- **Native**: Karmada v1.19.0 on a cluster of its own, two member clusters joined, its placement of the stream as shipped with the operator's one propagation policy.
- **Its test on real Kubernetes (class L)**: the batch stream sent to a group of two clusters, four ways (`docs/GROUP_PREREGISTRATION.md`); register row 95.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `multi_cluster_dispatch`, `region_dispatch`, `global_failover`, `cross_cluster_replication`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (more work + fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Open Cluster Management

- **Native**: OCM's hub (bundle 1.4.0, clusteradm v1.4.0) on a cluster of its own, two member clusters registered and accepted, a Placement per job with its default prioritizers and the job as a ManifestWork where it decided.
- **Its test on real Kubernetes (class L)**: the batch stream sent to a group of two clusters placed by OCM, four ways (`docs/GROUP_PREREGISTRATION.md`, amendment 1); register row 96.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `multi_cluster_dispatch`, `workload_migrate_region`, `federation_quota`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (more work + fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (more work + fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## KubeEdge

- **Native**: its edge sync and offline autonomy.
- **Its test on real Kubernetes (class L)**: not yet written; register row 97.
- **In the catalog (modelled, class S)**: family 39, Cross-Cluster, Multi-Region & Edge (18 muscles, in its realm and the whole tower): `edge_dispatch`, `edge_offload`, `edge_sync_interval`, `edge_site_node_pool`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

## Nephio

- **Native**: its intent-driven deployment and scaling.
- **Its test on real Kubernetes (class L)**: not yet written (a candidate: its sandbox asks more than a free runner gives); register row 98.
- **In the catalog (modelled, class S)**: family 66, Telecom RAN & Edge Radio (12 muscles, in its realm and the whole tower): `ran_slice_resource_budget`, `ran_du_cu_placement`, `ran_cell_sleep`, `ran_carrier_enable`.
- **Its muscles as a body in the orchestra (modelled, class S)**: own load: GAIN (fewer misses); the climb: GAIN (more work + fewer misses); work in line: GAIN (fewer misses).
- **Readings**: none yet; nothing is written here before its three runs are in.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
