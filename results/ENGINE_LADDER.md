# The engine's ladder: every version a benchmark step

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

Every version of the engine, in order, read from the repository's own records (`tools/engine_ladder.py`): its fingerprint, what changed and why (`docs/CHANGE_CONTROL.md`), its model gate against the version before (our own models, evidence class S, never proof: the candidate's readings against the engine that stood, by word), and its own three-run tables on real machines (evidence class L and, on the chips, P: every judged row by its word, LOSS rows counted with the rest). A version lands only when its gate reads no LOSS against the engine that stands (the rule since 15 October); every benchmark then runs again on it, and its tables are its own record, never read across engines. The ladder sets them side by side so the tuning can be followed step by step.

| Version | Landed (UTC) | Digest | Files | Model gate against the version before (class S) | Its own three-run tables | Their judged rows |
|---|---|---|---:|---|---:|---|
| omni-v1 | before the change-control record | `ccc7fbdf8b312ed7` | 38 | none: before the gate (15 October) | 0 | none |
| omni-v2 | before the change-control record | `4fc223939c4fab03` | 40 | none: before the gate (15 October) | 0 | none |
| omni-v3 | before the change-control record | `b53d05449ee04c4b` | 40 | none: before the gate (15 October) | 2 | the runs disagree 2 |
| omni-v5 | 11 Oct 22:40 | `6093b2b88aa911b9` | 44 | none: before the gate (15 October) | 1 | GAIN 1, LOSS 1, the runs disagree 6 |
| omni-v6 | 15 Oct 06:18 | `df6147466ef18046` | 45 | none: before the gate (15 October) | 4 | GAIN 25, LOSS 3, power given 9, the runs disagree 10, STEADY 17 |
| omni-v7 | 15 Oct 15:25 | `d6d467b824c585f1` | 46 | none: before the gate (15 October) | 18 | GAIN 141, LOSS 24, power given 50, the runs disagree 138, STEADY 181 |
| omni-v8 | 17 Oct 15:39 | `f93d233136a1f902` | 46 | [V8_VS_V7.md](model_gate/V8_VS_V7.md): STEADY 28 | 0 | none |
| omni-v9 | 17 Oct 22:21 | `7379f3a79ff2c475` | 47 | [V9_VS_V8.md](model_gate/V9_VS_V8.md): STEADY 28 | 0 | none |
| omni-v10 | 18 Oct 04:23 | `4bf39b0d707784de` | 47 | [V10_VS_V9.md](model_gate/V10_VS_V9.md): STEADY 28 | 20 | GAIN 168, LOSS 38, power given 46, the runs disagree 115, STEADY 199 |
| omni-v11 | 18 Oct 16:03 | `745aa53ec8eeb67b` | 47 | [V11_VS_V10.md](model_gate/V11_VS_V10.md): STEADY 34 | 19 | GAIN 153, LOSS 33, power given 73, the runs disagree 203, STEADY 301 |
| omni-v12 | 20 Oct 00:30 | `d38b58fbe28939b8` | 47 | [V12_VS_V11.md](model_gate/V12_VS_V11.md): GAIN 1, STEADY 44 | 66 | GAIN 441, LOSS 309, power given 134, the runs disagree 313, STEADY 498 |
| omni-v13 | 20 Oct 20:31 | `0088837333c6f0fc` | 47 | [V13_VS_V12.md](model_gate/V13_VS_V12.md): GAIN 7, power given 1, STEADY 49 | 0 | none |
| omni-v14 | 21 Oct 04:47 | `7afba44615fcff8f` | 47 | [V14_VS_V13.md](model_gate/V14_VS_V13.md): STEADY 57 | 4 | GAIN 27, LOSS 17, power given 18, the runs disagree 64, STEADY 80 |
| omni-v15 | 22 Oct 02:30 | `0a53cdd7a558f803` | 55 | [V15_VS_V14.md](model_gate/V15_VS_V14.md): GAIN 3, power given 6, STEADY 77 | 0 | none |
| omni-v16 | 22 Oct 07:30 | `5c5502f12b1c0ce4` | 55 | [V16_VS_V15.md](model_gate/V16_VS_V15.md): GAIN 2, LOSS 1, power given 8, STEADY 84 | 13 | GAIN 107, LOSS 42, power given 87, the runs disagree 184, STEADY 253 |
| omni-v17 | 23 Oct 17:00 | `7c937d09e4031cc7` | 55 | [V17_VS_V16.md](model_gate/V17_VS_V16.md): GAIN 4, LOSS 2, STEADY 89 | 13 | GAIN 149, LOSS 38, power given 65, the runs disagree 182, STEADY 239 |
| omni-v18 | 24 Oct 02:51 | `1cb92edb64c4391d` | 62 | [V18_VS_V17.md](model_gate/V18_VS_V17.md): read in its page | 8 | GAIN 76, LOSS 20, power given 38, the runs disagree 117, STEADY 156 |
| omni-v19 | 24 Oct 16:54 | `36ee67284c035235` | 62 | [V19_VS_V18.md](model_gate/V19_VS_V18.md): STEADY 95 | 0 | none |
| omni-v20 | 25 Oct 13:24 | `1df07f8e36a97985` | 62 | no gate record of its own | 0 | none |
| omni-v21 | 25 Oct 17:30 | `b658f05d43c1e602` | 63 | [V21_VS_V20.md](model_gate/V21_VS_V20.md): GAIN 16, power given 8, STEADY 71 | 31 | GAIN 212, LOSS 65, power given 111, the runs disagree 216, STEADY 542 |
| omni-v22 | 30 Oct 18:30 | `0e23a0bc561b900a` | 65 | [V22_VS_V21.md](model_gate/V22_VS_V21.md): read in its page | 0 | none |
| omni-v23 | 31 Oct 20:00 | `c96ea4105d8747db` | 65 | [V23_VS_V22.md](model_gate/V23_VS_V22.md): STEADY 95 | 4 | GAIN 11, LOSS 7, power given 6, the runs disagree 9, STEADY 216 |
| omni-v24 | 2 Nov 01:30 | `66c8f2d94b3e4725` | 65 | [V24_VS_V23.md](model_gate/V24_VS_V23.md): GAIN 6, STEADY 98 | 0 | none |
| omni-v25 | 3 Nov 21:00 | `cf56fc0a7b707452` | 65 | [V25_VS_V24.md](model_gate/V25_VS_V24.md): STEADY 104 | 92 | GAIN 605, LOSS 518, power given 264, the runs disagree 247, STEADY 640 |
| omni-v26 | 7 Nov 14:31 | `75d3c22eed4473b9` | 65 | [V26_VS_V25.md](model_gate/V26_VS_V25.md): STEADY 104 | 78 | GAIN 509, LOSS 392, power given 255, the runs disagree 260, STEADY 551 |
| omni-v27 | 15 Nov 18:30 | `34548e45437a05bd` | 65 | [V27_VS_V26.md](model_gate/V27_VS_V26.md): GAIN 7, LOSS 15, power given 20, STEADY 62 | 11 | GAIN 55, LOSS 39, power given 18, the runs disagree 21, STEADY 62 |

## What each version changed, and why

- **omni-v27** (15 Nov 18:30): place before asking, the forward look, the stand-ins and the conveyance owed (the founder's orders of 14 and 15 November): no pod asked for that no machine in service can take, the pods Omni-Compass asked for that wait withdrawn to native's count at once; the scale-up looks three beats ahead at the rate held at every one of the last three beats, never nearer than a machine's measured delivery, where omni-v19's memory held the largest rise ever seen; through a cloud, stand-ins of the lowest priority ask the cloud's own autoscaler for the machines ahead; the conveyance gives what is owed. The model gate against omni-v26 (`results/model_gate/V27_VS_V26.md`, eight seeds, twelve models, class S, never proof): against native the cloud and on-site models read GAIN or STEADY on every service gauge but one, the minutes the autoscaler wanted more pods than its cap allowed in the cloud at 60 s (up 0.8%, about two seconds an hour, inside the seeds' noise), with the machines power given; against omni-v26 the pods waiting read GAIN (down 28.4% in the cloud at its factory 60 s, beyond the seeds' noise; down 76.2% at 15 s), and the 95th percentile and the alert minutes read LOSS (in the cloud at 60 s up 5.0% and 9.7%, inside the seeds' noise; at 15 s up 8.5% and 67.5%; on site at 10 s up 1.4% and 2.5 minutes a day): omni-v26's speed came from the two things the founder ordered out, the pods it asked for waiting for a machine and the largest rise ever seen held as a reserve; the conveyance, card and verdict models read omni-v26's numbers to the digit, its rows against native among them (LOSS: the conveyance models' pod start wait up 9.0%, the batch model's requests served down 2.1% and alert minutes up 9.8%, the card's 95th percentile up 2.4%), on the next version's list
- **omni-v26** (7 Nov 14:31): another workload's waiting pods hold native's target: when a service's target stood below native's and pods waited, the decision returned native's target without starting the immune hand-back's hold, so a batch queue's normal waiting flipped the web service's target every one or two decisions and the flips kept extra web pods in room the queue was owed; the decision now starts the hold when the waiting pods include a workload's no autoscaler governs (`docs/OMNI_V26.md`; the model gate identical on all 104 readings, no LOSS)
- **omni-v25** (3 Nov 21:00): the Kafka wire's producer started before the governor's thread: from omni-v22 the forked producer inherited a lock that thread held and never sent a message, so every Kafka run on GitHub stopped at the job's 150-minute limit; a producer that overruns its schedule now stops its workload with the reason; the governor's decisions byte for byte omni-v24's (`docs/OMNI_V25.md`)
- **omni-v24** (2 Nov 01:30): the factory beat for its place: with no beat set, the Kubernetes governor reads the cluster's nodes at its start and decides every 10 s on site and every 60 s through a cloud (a reading that fails keeps 60 s, a beat set by hand always wins), the pick of a rule frozen before any reading (docs/PACE_PREREGISTRATION.md, amendments 4 to 6); the model gate against omni-v23: no LOSS; eleven of twelve models identical; on site the minutes over the line down 60.7% and the 95th percentile down 8.2% (GAIN)
- **omni-v23** (31 Oct 20:00): Omni direct keeps every muscle Omni-Compass cannot be: a workload's own scale write the cluster refuses three times in a row hands the knob back to native's own pod autoscaler, made from the operator's target and range (the founder's order of 31 October; `docs/OMNI_V23.md`)
- **omni-v22** (30 Oct 18:30): the five data stores' wires at the max, through each store's own account of a miss; the governor's hand-back tried five times against a transient failure of the cluster's API (`docs/OMNI_V22.md`)
- **omni-v21** (25 Oct 17:30): the immune system knows itself, knob by knob: a knob redlining past its line that Omni-Compass cannot bring back goes to native when native's twin reads it lower (`docs/OMNI_V21.md`)
- **omni-v20** (25 Oct 13:24): the five data stores' wires fixed at their causes (sysbench's own statements, Kafka's hand-back within a poll round, YCSB's cache growing back while it misses) (`docs/OMNI_V20.md`)
- **omni-v19** (24 Oct 16:54): the pod muscle of its own (`--own-replicas`) for a workload no autoscaler governs; the models' arm by itself (`docs/OMNI_V19.md`)
- **omni-v18** (24 Oct 02:51): Omni direct taken into the engine: the seven rule files of Omni-Compass's own orchestrator fingerprinted, the three arms shown together (`docs/OMNI_V18.md`)
- **omni-v17** (23 Oct 17:00): the Kubernetes governor's heartbeat a dial, the main engine every 60 s (the parser's default; omni-v16's was 15 s), any beat from 5 to 120 s, every beat shown beside native (`results/model_gate/V17_LADDER.md`, the live engine page's 1j); the monitors scale with the beat (`omni_heartbeat_seconds`, the alert at three beats, the panel's `/v1/beat`); the cruise wait never under two readings (at 90 and 120 s it had rounded to one, found by the dial's own ladder before it landed); the founder's order of 22 October, afternoon
- **omni-v16** (22 Oct 07:30): the Kubernetes governor: every clock in seconds (the brain's minute and its C++ twin, the compass's damping and smoothing, the edge, the additions past the floor, a command's minute to land, the host's busy share, the heat law, one batch job a minute, the conveyance every 15 s, the loop's own schedule), so the decision period is a clean setting; the heartbeat, the full decision, every 15 s by default (the founder's word, "15 sec all over"), the fast checks every 5 s; at 60 s exactly omni-v15's decisions; the pace read by its own runs (`docs/PACE_PREREGISTRATION.md`)
- **omni-v15** (22 Oct 02:30): the brain: the power cap's request trims only while the response line has been clean for the governor's own clear time (the omni-v11 long run's 126 switches in 350 decisions); every wire that holds a governor's rules in the fingerprint (eight taken in, their bytes as they stood)
- **omni-v14** (21 Oct 04:47): Kubernetes: a knob that leaves any one muscle native; the operator's own commands run without a shell
- **omni-v13** (20 Oct 20:31): Kubernetes: the CPU limits the conveyance gave go back to the operator's on a shared host at its top beside another workload's room; every other pod counted by its own limit
- **omni-v12** (20 Oct 00:30): Kubernetes: a raise the cluster's admission refused is held, not written again at every check; the swarm's proximity reflex at once (its wire outside the digest, declared with the version)
- **omni-v11** (18 Oct 16:03): Kubernetes: a reading with no machine in service is held, never read as an overload
- **omni-v10** (18 Oct 04:23): CityLearn: the battery glide that cuts the bill most with no LOSS
- **omni-v9** (17 Oct 22:21): CityLearn: the battery wire reads the coming hour; the exact Student t
- **omni-v8** (17 Oct 15:39): CityLearn: a battery whose building has outages stays native (its charge is the building's reserve)
- **omni-v7** (15 Oct 15:25): conveyance bounded by the namespace's CPU quota; every rule in seconds
- **omni-v6** (15 Oct 06:18): shared-host capacity: on kind the host's processor counted once
- **omni-v5** (11 Oct 22:40): the max as the default brain on the 1,107-muscle catalog; re-declared while in development

## Each version's own tables

### omni-v27

| Table | Judged rows |
|---|---|
| [V27_ALL_FOUR.md](live/V27_ALL_FOUR.md) | GAIN 6, LOSS 2, power given 2, the runs disagree 1, STEADY 6 |
| [V27_BATCH.md](live/V27_BATCH.md) | GAIN 8, LOSS 5, power given 1, the runs disagree 1, STEADY 3 |
| [V27_FAIRNESS.md](live/V27_FAIRNESS.md) | GAIN 1, LOSS 7, power given 2, the runs disagree 4, STEADY 6 |
| [V27_FAULTS.md](live/V27_FAULTS.md) | GAIN 6, power given 2, the runs disagree 2, STEADY 6 |
| [V27_KUEUE.md](live/V27_KUEUE.md) | GAIN 6, LOSS 9, power given 2, STEADY 5 |
| [V27_SOLO.md](live/V27_SOLO.md) | GAIN 5, LOSS 3, power given 2, STEADY 6 |
| [V27_SOLO_VS_ON_NATIVE.md](live/V27_SOLO_VS_ON_NATIVE.md) | LOSS 5, power given 2, the runs disagree 3, STEADY 6 |
| [V27_STEADY.md](live/V27_STEADY.md) | GAIN 7, power given 1, the runs disagree 1, STEADY 7 |
| [V27_TRACE_GOOGLE2011.md](live/V27_TRACE_GOOGLE2011.md) | GAIN 6, LOSS 1, power given 2, the runs disagree 1, STEADY 6 |
| [V27_VOLCANO.md](live/V27_VOLCANO.md) | GAIN 5, LOSS 5, the runs disagree 7, STEADY 5 |
| [V27_WANDERING.md](live/V27_WANDERING.md) | GAIN 5, LOSS 2, power given 2, the runs disagree 1, STEADY 6 |

### omni-v26

| Table | Judged rows |
|---|---|
| [V26_AKS_FULL_BURST.md](live/V26_AKS_FULL_BURST.md) | GAIN 2, LOSS 7, power given 8, the runs disagree 1 |
| [V26_AKS_WORK_METER.md](live/V26_AKS_WORK_METER.md) | GAIN 8, LOSS 4, power given 8 |
| [V26_ALL_FOUR.md](live/V26_ALL_FOUR.md) | GAIN 5, LOSS 2, power given 2, the runs disagree 2, STEADY 6 |
| [V26_BATCH.md](live/V26_BATCH.md) | GAIN 6, LOSS 4, power given 2, the runs disagree 2, STEADY 4 |
| [V26_BINPACK.md](live/V26_BINPACK.md) | GAIN 6, LOSS 9, power given 2, the runs disagree 1, STEADY 4 |
| [V26_BINPACK_4W_BARE.md](live/V26_BINPACK_4W_BARE.md) | GAIN 6, LOSS 10, power given 2, STEADY 4 |
| [V26_BINPACK_4W_BOTH.md](live/V26_BINPACK_4W_BOTH.md) | GAIN 8, LOSS 7, power given 2, the runs disagree 1, STEADY 4 |
| [V26_BINPACK_4W_ORCH.md](live/V26_BINPACK_4W_ORCH.md) | GAIN 4, LOSS 2, power given 1, the runs disagree 5, STEADY 10 |
| [V26_BINPACK_4W_TOP.md](live/V26_BINPACK_4W_TOP.md) | GAIN 4, LOSS 7, power given 2, the runs disagree 4, STEADY 5 |
| [V26_BINPACK_4W_VS.md](live/V26_BINPACK_4W_VS.md) | GAIN 4, LOSS 8, power given 2, the runs disagree 2, STEADY 6 |
| [V26_CAPACITY.md](live/V26_CAPACITY.md) | GAIN 2, LOSS 3, the runs disagree 3 |
| [V26_COST_TO_MATCH.md](live/V26_COST_TO_MATCH.md) | GAIN 7, power given 1, the runs disagree 1, STEADY 7 |
| [V26_CRANE_4W_BARE.md](live/V26_CRANE_4W_BARE.md) | GAIN 5, LOSS 1, power given 2, the runs disagree 1, STEADY 7 |
| [V26_CRANE_4W_BOTH.md](live/V26_CRANE_4W_BOTH.md) | LOSS 3, power given 4, the runs disagree 4, STEADY 5 |
| [V26_CRANE_4W_ORCH.md](live/V26_CRANE_4W_ORCH.md) | GAIN 1, LOSS 2, the runs disagree 5, STEADY 8 |
| [V26_CRANE_4W_TOP.md](live/V26_CRANE_4W_TOP.md) | GAIN 4, LOSS 2, power given 2, the runs disagree 1, STEADY 7 |
| [V26_CRANE_4W_VS.md](live/V26_CRANE_4W_VS.md) | GAIN 7, LOSS 1, power given 2, the runs disagree 1, STEADY 5 |
| [V26_CRUISEKUBE.md](live/V26_CRUISEKUBE.md) | GAIN 3, LOSS 5, power given 1, the runs disagree 2, STEADY 5 |
| [V26_CRUISEKUBE_RECORDER.md](live/V26_CRUISEKUBE_RECORDER.md) | GAIN 3, LOSS 4, power given 2, the runs disagree 1, STEADY 6 |
| [V26_FAIRNESS.md](live/V26_FAIRNESS.md) | GAIN 1, LOSS 4, power given 2, the runs disagree 6, STEADY 7 |
| [V26_FAULTS.md](live/V26_FAULTS.md) | GAIN 5, LOSS 1, power given 2, the runs disagree 2, STEADY 6 |
| [V26_FAULTS_EXTENDED.md](live/V26_FAULTS_EXTENDED.md) | GAIN 6, LOSS 2, power given 1, the runs disagree 1, STEADY 6 |
| [V26_GODEL_4W_BARE.md](live/V26_GODEL_4W_BARE.md) | GAIN 4, LOSS 10, power given 2, the runs disagree 1, STEADY 5 |
| [V26_GODEL_4W_BOTH.md](live/V26_GODEL_4W_BOTH.md) | GAIN 4, LOSS 9, power given 2, the runs disagree 3, STEADY 4 |
| [V26_GODEL_4W_ORCH.md](live/V26_GODEL_4W_ORCH.md) | GAIN 2, LOSS 7, power given 2, the runs disagree 3, STEADY 8 |
| [V26_GODEL_4W_TOP.md](live/V26_GODEL_4W_TOP.md) | GAIN 4, LOSS 8, power given 2, the runs disagree 4, STEADY 4 |
| [V26_GODEL_4W_VS.md](live/V26_GODEL_4W_VS.md) | GAIN 5, LOSS 6, power given 2, the runs disagree 4, STEADY 5 |
| [V26_GOLDILOCKS.md](live/V26_GOLDILOCKS.md) | GAIN 5, LOSS 2, power given 4, STEADY 5 |
| [V26_KAFKA.md](live/V26_KAFKA.md) | GAIN 32, power given 16, STEADY 8 |
| [V26_KAFKA_SERVICE.md](live/V26_KAFKA_SERVICE.md) | GAIN 31, power given 16, the runs disagree 1, STEADY 8 |
| [V26_KAI.md](live/V26_KAI.md) | GAIN 4, LOSS 7, power given 2, the runs disagree 5, STEADY 4 |
| [V26_KAI_4W_BARE.md](live/V26_KAI_4W_BARE.md) | GAIN 6, LOSS 8, power given 2, the runs disagree 1, STEADY 5 |
| [V26_KAI_4W_BOTH.md](live/V26_KAI_4W_BOTH.md) | GAIN 4, LOSS 11, power given 2, the runs disagree 1, STEADY 4 |
| [V26_KAI_4W_ORCH.md](live/V26_KAI_4W_ORCH.md) | GAIN 1, LOSS 10, power given 2, the runs disagree 1, STEADY 8 |
| [V26_KAI_4W_TOP.md](live/V26_KAI_4W_TOP.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 2, STEADY 4 |
| [V26_KAI_4W_VS.md](live/V26_KAI_4W_VS.md) | GAIN 12, LOSS 4, power given 2, STEADY 4 |
| [V26_KEDA_CPU_REQUESTS.md](live/V26_KEDA_CPU_REQUESTS.md) | GAIN 4, LOSS 1, power given 4, the runs disagree 2, STEADY 5 |
| [V26_KEDA_REQUESTS.md](live/V26_KEDA_REQUESTS.md) | GAIN 6, power given 2, the runs disagree 3, STEADY 5 |
| [V26_KOORDINATOR.md](live/V26_KOORDINATOR.md) | GAIN 4, LOSS 5, the runs disagree 8, STEADY 4 |
| [V26_KOORDINATOR_CGROUP.md](live/V26_KOORDINATOR_CGROUP.md) | GAIN 2, LOSS 9, power given 2, the runs disagree 2, STEADY 6 |
| [V26_KUBERAY_4W_BARE.md](live/V26_KUBERAY_4W_BARE.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 1, STEADY 5 |
| [V26_KUBERAY_4W_BOTH.md](live/V26_KUBERAY_4W_BOTH.md) | GAIN 3, LOSS 10, power given 4, the runs disagree 2, STEADY 3 |
| [V26_KUBERAY_4W_ORCH.md](live/V26_KUBERAY_4W_ORCH.md) | LOSS 8, power given 2, the runs disagree 6, STEADY 6 |
| [V26_KUBERAY_4W_TOP.md](live/V26_KUBERAY_4W_TOP.md) | GAIN 4, LOSS 7, power given 2, the runs disagree 5, STEADY 4 |
| [V26_KUBERAY_4W_VS.md](live/V26_KUBERAY_4W_VS.md) | GAIN 13, LOSS 2, power given 2, the runs disagree 2, STEADY 3 |
| [V26_KUEUE.md](live/V26_KUEUE.md) | GAIN 5, LOSS 10, power given 2, the runs disagree 1, STEADY 4 |
| [V26_KUEUE_4W_BARE.md](live/V26_KUEUE_4W_BARE.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 1, STEADY 5 |
| [V26_KUEUE_4W_BOTH.md](live/V26_KUEUE_4W_BOTH.md) | GAIN 4, LOSS 10, power given 2, the runs disagree 1, STEADY 5 |
| [V26_KUEUE_4W_ORCH.md](live/V26_KUEUE_4W_ORCH.md) | LOSS 9, the runs disagree 4, STEADY 9 |
| [V26_KUEUE_4W_TOP.md](live/V26_KUEUE_4W_TOP.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 1, STEADY 5 |
| [V26_KUEUE_4W_VS.md](live/V26_KUEUE_4W_VS.md) | GAIN 7, LOSS 6, power given 2, the runs disagree 1, STEADY 6 |
| [V26_OCM_4W_BARE.md](live/V26_OCM_4W_BARE.md) | GAIN 5, LOSS 10, power given 2, the runs disagree 1, STEADY 4 |
| [V26_OCM_4W_BOTH.md](live/V26_OCM_4W_BOTH.md) | GAIN 4, LOSS 12, power given 2, the runs disagree 1, STEADY 3 |
| [V26_OCM_4W_ORCH.md](live/V26_OCM_4W_ORCH.md) | LOSS 12, the runs disagree 2, STEADY 8 |
| [V26_OCM_4W_TOP.md](live/V26_OCM_4W_TOP.md) | GAIN 4, LOSS 10, power given 2, the runs disagree 3, STEADY 3 |
| [V26_OCM_4W_VS.md](live/V26_OCM_4W_VS.md) | GAIN 13, LOSS 2, power given 2, the runs disagree 1, STEADY 4 |
| [V26_PGBENCH.md](live/V26_PGBENCH.md) | GAIN 9, LOSS 2, power given 7, the runs disagree 5, STEADY 13 |
| [V26_PGBENCH_SERVICE.md](live/V26_PGBENCH_SERVICE.md) | LOSS 3, power given 7, the runs disagree 6, STEADY 20 |
| [V26_REDIS.md](live/V26_REDIS.md) | GAIN 31, power given 8, the runs disagree 4, STEADY 9 |
| [V26_REDIS_SERVICE.md](live/V26_REDIS_SERVICE.md) | GAIN 34, power given 8, STEADY 10 |
| [V26_REDIS_SHIPPED.md](live/V26_REDIS_SHIPPED.md) | GAIN 7, power given 1, the runs disagree 12, STEADY 32 |
| [V26_ROBUST_KILL.md](live/V26_ROBUST_KILL.md) | GAIN 5, LOSS 2, power given 2, the runs disagree 3, STEADY 6 |
| [V26_ROBUST_LONG.md](live/V26_ROBUST_LONG.md) | GAIN 6, LOSS 2, power given 2, STEADY 6 |
| [V26_SOLO.md](live/V26_SOLO.md) | GAIN 5, LOSS 3, power given 2, STEADY 6 |
| [V26_SOLO_2.md](live/V26_SOLO_2.md) | GAIN 5, LOSS 3, power given 2, STEADY 6 |
| [V26_SOLO_2_VS_ON_NATIVE.md](live/V26_SOLO_2_VS_ON_NATIVE.md) | GAIN 1, LOSS 6, power given 2, the runs disagree 1, STEADY 6 |
| [V26_SOLO_VS_ON_NATIVE.md](live/V26_SOLO_VS_ON_NATIVE.md) | GAIN 2, LOSS 6, power given 2, STEADY 6 |
| [V26_STEADY.md](live/V26_STEADY.md) | GAIN 8, power given 1, STEADY 7 |
| [V26_SYSBENCH.md](live/V26_SYSBENCH.md) | GAIN 24, power given 10, the runs disagree 12, STEADY 14 |
| [V26_SYSBENCH_SERVICE.md](live/V26_SYSBENCH_SERVICE.md) | GAIN 13, power given 8, the runs disagree 23, STEADY 16 |
| [V26_SYSBENCH_SHIPPED.md](live/V26_SYSBENCH_SHIPPED.md) | GAIN 17, LOSS 4, power given 10, the runs disagree 11, STEADY 18 |
| [V26_TRACE_GOOGLE2011.md](live/V26_TRACE_GOOGLE2011.md) | GAIN 6, LOSS 1, power given 2, the runs disagree 1, STEADY 6 |
| [V26_VANILLA.md](live/V26_VANILLA.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 1, STEADY 5 |
| [V26_VOLCANO.md](live/V26_VOLCANO.md) | GAIN 4, LOSS 9, power given 2, the runs disagree 2, STEADY 5 |
| [V26_WANDERING.md](live/V26_WANDERING.md) | GAIN 4, LOSS 2, power given 2, the runs disagree 2, STEADY 6 |
| [V26_YCSB.md](live/V26_YCSB.md) | GAIN 9, LOSS 4, power given 18, the runs disagree 10, STEADY 19 |
| [V26_YCSB_SERVICE.md](live/V26_YCSB_SERVICE.md) | GAIN 4, LOSS 1, power given 8, the runs disagree 27, STEADY 20 |
| [V26_YCSB_SHIPPED.md](live/V26_YCSB_SHIPPED.md) | GAIN 1, LOSS 6, power given 3, the runs disagree 20, STEADY 30 |

### omni-v25

| Table | Judged rows |
|---|---|
| [V25_AKS_FULL_BURST.md](live/V25_AKS_FULL_BURST.md) | GAIN 1, LOSS 6, power given 8, the runs disagree 3 |
| [V25_ALL_FOUR.md](live/V25_ALL_FOUR.md) | GAIN 6, LOSS 2, power given 2, the runs disagree 1, STEADY 6 |
| [V25_ARMADA_4W_BARE.md](live/V25_ARMADA_4W_BARE.md) | GAIN 4, LOSS 12, power given 2, STEADY 4 |
| [V25_ARMADA_4W_BOTH.md](live/V25_ARMADA_4W_BOTH.md) | GAIN 9, LOSS 7, power given 2, STEADY 3 |
| [V25_ARMADA_4W_ORCH.md](live/V25_ARMADA_4W_ORCH.md) | GAIN 7, LOSS 5, power given 2, the runs disagree 2, STEADY 5 |
| [V25_ARMADA_4W_TOP.md](live/V25_ARMADA_4W_TOP.md) | GAIN 6, LOSS 3, power given 2, STEADY 10 |
| [V25_ARMADA_4W_VS.md](live/V25_ARMADA_4W_VS.md) | GAIN 8, LOSS 8, power given 3, STEADY 2 |
| [V25_BATCH.md](live/V25_BATCH.md) | GAIN 9, LOSS 4, the runs disagree 2, STEADY 3 |
| [V25_BINPACK.md](live/V25_BINPACK.md) | GAIN 6, LOSS 10, power given 2, STEADY 4 |
| [V25_BINPACK_4W_BARE.md](live/V25_BINPACK_4W_BARE.md) | GAIN 4, LOSS 9, power given 2, the runs disagree 3, STEADY 4 |
| [V25_BINPACK_4W_BOTH.md](live/V25_BINPACK_4W_BOTH.md) | GAIN 6, LOSS 8, power given 2, the runs disagree 1, STEADY 5 |
| [V25_BINPACK_4W_ORCH.md](live/V25_BINPACK_4W_ORCH.md) | GAIN 3, LOSS 5, power given 1, the runs disagree 3, STEADY 10 |
| [V25_BINPACK_4W_TOP.md](live/V25_BINPACK_4W_TOP.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 1, STEADY 5 |
| [V25_BINPACK_4W_VS.md](live/V25_BINPACK_4W_VS.md) | GAIN 4, LOSS 10, power given 2, the runs disagree 2, STEADY 4 |
| [V25_CAPACITY.md](live/V25_CAPACITY.md) | GAIN 1, LOSS 3, the runs disagree 4 |
| [V25_COST_TO_MATCH.md](live/V25_COST_TO_MATCH.md) | GAIN 8, the runs disagree 1, STEADY 7 |
| [V25_CRANE_4W_BARE.md](live/V25_CRANE_4W_BARE.md) | LOSS 1, power given 2, the runs disagree 5, STEADY 8 |
| [V25_CRANE_4W_BOTH.md](live/V25_CRANE_4W_BOTH.md) | GAIN 3, LOSS 2, power given 4, the runs disagree 1, STEADY 6 |
| [V25_CRANE_4W_ORCH.md](live/V25_CRANE_4W_ORCH.md) | GAIN 1, LOSS 1, power given 2, the runs disagree 6, STEADY 6 |
| [V25_CRANE_4W_TOP.md](live/V25_CRANE_4W_TOP.md) | LOSS 3, power given 2, the runs disagree 4, STEADY 7 |
| [V25_CRANE_4W_VS.md](live/V25_CRANE_4W_VS.md) | GAIN 4, LOSS 2, power given 2, the runs disagree 3, STEADY 5 |
| [V25_CRUISEKUBE.md](live/V25_CRUISEKUBE.md) | GAIN 1, LOSS 3, power given 1, the runs disagree 4, STEADY 7 |
| [V25_CRUISEKUBE_RECORDER.md](live/V25_CRUISEKUBE_RECORDER.md) | GAIN 2, LOSS 4, the runs disagree 3, STEADY 7 |
| [V25_FAIRNESS.md](live/V25_FAIRNESS.md) | GAIN 3, LOSS 5, power given 2, the runs disagree 4, STEADY 6 |
| [V25_FAULTS.md](live/V25_FAULTS.md) | GAIN 6, LOSS 1, power given 2, the runs disagree 1, STEADY 6 |
| [V25_FAULTS_EXTENDED.md](live/V25_FAULTS_EXTENDED.md) | GAIN 6, LOSS 2, power given 2, STEADY 6 |
| [V25_GODEL_4W_BARE.md](live/V25_GODEL_4W_BARE.md) | GAIN 4, LOSS 9, power given 2, the runs disagree 3, STEADY 4 |
| [V25_GODEL_4W_BOTH.md](live/V25_GODEL_4W_BOTH.md) | GAIN 7, LOSS 7, power given 2, the runs disagree 2, STEADY 4 |
| [V25_GODEL_4W_ORCH.md](live/V25_GODEL_4W_ORCH.md) | GAIN 6, LOSS 5, the runs disagree 3, STEADY 8 |
| [V25_GODEL_4W_TOP.md](live/V25_GODEL_4W_TOP.md) | GAIN 4, LOSS 9, power given 2, the runs disagree 3, STEADY 4 |
| [V25_GODEL_4W_VS.md](live/V25_GODEL_4W_VS.md) | GAIN 5, LOSS 6, power given 2, the runs disagree 4, STEADY 5 |
| [V25_GOLDILOCKS.md](live/V25_GOLDILOCKS.md) | GAIN 5, LOSS 2, power given 4, STEADY 5 |
| [V25_KAFKA.md](live/V25_KAFKA.md) | GAIN 32, power given 16, STEADY 8 |
| [V25_KAFKA_SERVICE.md](live/V25_KAFKA_SERVICE.md) | GAIN 32, power given 16, STEADY 8 |
| [V25_KAI.md](live/V25_KAI.md) | GAIN 5, LOSS 8, power given 2, the runs disagree 3, STEADY 4 |
| [V25_KAI_4W_BARE.md](live/V25_KAI_4W_BARE.md) | GAIN 4, LOSS 10, power given 2, the runs disagree 1, STEADY 5 |
| [V25_KAI_4W_BOTH.md](live/V25_KAI_4W_BOTH.md) | GAIN 4, LOSS 11, power given 2, the runs disagree 1, STEADY 4 |
| [V25_KAI_4W_ORCH.md](live/V25_KAI_4W_ORCH.md) | LOSS 11, power given 1, the runs disagree 2, STEADY 8 |
| [V25_KAI_4W_TOP.md](live/V25_KAI_4W_TOP.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 2, STEADY 4 |
| [V25_KAI_4W_VS.md](live/V25_KAI_4W_VS.md) | GAIN 13, LOSS 3, power given 2, STEADY 4 |
| [V25_KARMADA_4W_BARE.md](live/V25_KARMADA_4W_BARE.md) | GAIN 4, LOSS 11, power given 2, the runs disagree 1, STEADY 4 |
| [V25_KARMADA_4W_BOTH.md](live/V25_KARMADA_4W_BOTH.md) | GAIN 4, LOSS 12, power given 2, STEADY 4 |
| [V25_KARMADA_4W_ORCH.md](live/V25_KARMADA_4W_ORCH.md) | GAIN 1, LOSS 10, the runs disagree 3, STEADY 8 |
| [V25_KARMADA_4W_TOP.md](live/V25_KARMADA_4W_TOP.md) | GAIN 4, LOSS 12, power given 2, STEADY 4 |
| [V25_KARMADA_4W_VS.md](live/V25_KARMADA_4W_VS.md) | GAIN 13, LOSS 3, power given 2, STEADY 4 |
| [V25_KEDA_CPU_REQUESTS.md](live/V25_KEDA_CPU_REQUESTS.md) | GAIN 5, LOSS 1, power given 4, the runs disagree 1, STEADY 5 |
| [V25_KEDA_REQUESTS.md](live/V25_KEDA_REQUESTS.md) | GAIN 7, LOSS 1, power given 2, the runs disagree 1, STEADY 5 |
| [V25_KOORDINATOR.md](live/V25_KOORDINATOR.md) | GAIN 1, LOSS 11, power given 2, STEADY 7 |
| [V25_KOORDINATOR_CGROUP.md](live/V25_KOORDINATOR_CGROUP.md) | GAIN 3, LOSS 10, power given 2, STEADY 7 |
| [V25_KUBERAY_4W_BARE.md](live/V25_KUBERAY_4W_BARE.md) | GAIN 5, LOSS 7, power given 2, the runs disagree 3, STEADY 5 |
| [V25_KUBERAY_4W_BOTH.md](live/V25_KUBERAY_4W_BOTH.md) | GAIN 3, LOSS 10, power given 4, the runs disagree 2, STEADY 3 |
| [V25_KUBERAY_4W_ORCH.md](live/V25_KUBERAY_4W_ORCH.md) | LOSS 10, power given 4, the runs disagree 2, STEADY 6 |
| [V25_KUBERAY_4W_TOP.md](live/V25_KUBERAY_4W_TOP.md) | GAIN 6, LOSS 2, power given 2, the runs disagree 7, STEADY 5 |
| [V25_KUBERAY_4W_VS.md](live/V25_KUBERAY_4W_VS.md) | GAIN 13, LOSS 4, power given 2, STEADY 3 |
| [V25_KUEUE.md](live/V25_KUEUE.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 2, STEADY 4 |
| [V25_KUEUE_4W_BARE.md](live/V25_KUEUE_4W_BARE.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 2, STEADY 4 |
| [V25_KUEUE_4W_BOTH.md](live/V25_KUEUE_4W_BOTH.md) | GAIN 4, LOSS 11, power given 2, the runs disagree 1, STEADY 4 |
| [V25_KUEUE_4W_ORCH.md](live/V25_KUEUE_4W_ORCH.md) | GAIN 1, LOSS 8, the runs disagree 3, STEADY 10 |
| [V25_KUEUE_4W_TOP.md](live/V25_KUEUE_4W_TOP.md) | GAIN 4, LOSS 11, power given 2, the runs disagree 1, STEADY 4 |
| [V25_KUEUE_4W_VS.md](live/V25_KUEUE_4W_VS.md) | GAIN 8, LOSS 8, power given 2, STEADY 4 |
| [V25_OCM_4W_BARE.md](live/V25_OCM_4W_BARE.md) | GAIN 4, LOSS 10, power given 2, the runs disagree 2, STEADY 4 |
| [V25_OCM_4W_BOTH.md](live/V25_OCM_4W_BOTH.md) | GAIN 4, LOSS 12, power given 2, STEADY 4 |
| [V25_OCM_4W_ORCH.md](live/V25_OCM_4W_ORCH.md) | LOSS 10, the runs disagree 4, STEADY 8 |
| [V25_OCM_4W_TOP.md](live/V25_OCM_4W_TOP.md) | GAIN 4, LOSS 10, power given 2, the runs disagree 2, STEADY 4 |
| [V25_OCM_4W_VS.md](live/V25_OCM_4W_VS.md) | GAIN 14, LOSS 2, power given 2, STEADY 4 |
| [V25_PGBENCH.md](live/V25_PGBENCH.md) | GAIN 4, LOSS 1, power given 7, the runs disagree 8, STEADY 16 |
| [V25_PGBENCH_SERVICE.md](live/V25_PGBENCH_SERVICE.md) | GAIN 9, LOSS 1, power given 4, the runs disagree 12, STEADY 10 |
| [V25_REDIS.md](live/V25_REDIS.md) | GAIN 31, power given 10, STEADY 11 |
| [V25_REDIS_SERVICE.md](live/V25_REDIS_SERVICE.md) | GAIN 33, power given 8, STEADY 11 |
| [V25_REDIS_SHIPPED.md](live/V25_REDIS_SHIPPED.md) | GAIN 6, LOSS 1, the runs disagree 9, STEADY 36 |
| [V25_ROBUST_KILL.md](live/V25_ROBUST_KILL.md) | GAIN 5, LOSS 4, power given 2, the runs disagree 1, STEADY 6 |
| [V25_ROBUST_LONG.md](live/V25_ROBUST_LONG.md) | GAIN 5, LOSS 2, power given 2, the runs disagree 1, STEADY 6 |
| [V25_SOLO.md](live/V25_SOLO.md) | GAIN 5, LOSS 3, power given 2, STEADY 6 |
| [V25_SOLO_2.md](live/V25_SOLO_2.md) | GAIN 5, LOSS 3, power given 2, STEADY 6 |
| [V25_SOLO_2_VS_ON_NATIVE.md](live/V25_SOLO_2_VS_ON_NATIVE.md) | LOSS 6, power given 2, the runs disagree 1, STEADY 7 |
| [V25_SOLO_VS_ON_NATIVE.md](live/V25_SOLO_VS_ON_NATIVE.md) | GAIN 1, LOSS 6, power given 2, the runs disagree 1, STEADY 6 |
| [V25_STEADY.md](live/V25_STEADY.md) | GAIN 7, power given 1, the runs disagree 1, STEADY 7 |
| [V25_SYSBENCH.md](live/V25_SYSBENCH.md) | GAIN 21, power given 9, the runs disagree 9, STEADY 21 |
| [V25_SYSBENCH_SERVICE.md](live/V25_SYSBENCH_SERVICE.md) | GAIN 17, power given 8, the runs disagree 13, STEADY 22 |
| [V25_SYSBENCH_SHIPPED.md](live/V25_SYSBENCH_SHIPPED.md) | GAIN 18, LOSS 2, power given 10, the runs disagree 14, STEADY 16 |
| [V25_TRACE_GOOGLE2011.md](live/V25_TRACE_GOOGLE2011.md) | GAIN 6, LOSS 2, power given 2, STEADY 6 |
| [V25_VANILLA.md](live/V25_VANILLA.md) | GAIN 6, LOSS 9, power given 2, STEADY 5 |
| [V25_VOLCANO.md](live/V25_VOLCANO.md) | GAIN 4, LOSS 9, power given 2, the runs disagree 2, STEADY 5 |
| [V25_VOLCANO_4W_BARE.md](live/V25_VOLCANO_4W_BARE.md) | GAIN 5, LOSS 9, power given 2, the runs disagree 2, STEADY 4 |
| [V25_VOLCANO_4W_BOTH.md](live/V25_VOLCANO_4W_BOTH.md) | GAIN 7, LOSS 9, power given 2, STEADY 4 |
| [V25_VOLCANO_4W_ORCH.md](live/V25_VOLCANO_4W_ORCH.md) | GAIN 7, LOSS 6, power given 1, STEADY 8 |
| [V25_VOLCANO_4W_TOP.md](live/V25_VOLCANO_4W_TOP.md) | GAIN 4, LOSS 8, power given 2, the runs disagree 4, STEADY 4 |
| [V25_VOLCANO_4W_VS.md](live/V25_VOLCANO_4W_VS.md) | GAIN 6, LOSS 7, power given 2, the runs disagree 2, STEADY 5 |
| [V25_WANDERING.md](live/V25_WANDERING.md) | GAIN 4, LOSS 2, power given 2, the runs disagree 2, STEADY 6 |
| [V25_YCSB.md](live/V25_YCSB.md) | GAIN 14, LOSS 2, power given 10, the runs disagree 15, STEADY 19 |
| [V25_YCSB_SERVICE.md](live/V25_YCSB_SERVICE.md) | GAIN 10, LOSS 4, power given 8, the runs disagree 19, STEADY 19 |
| [V25_YCSB_SHIPPED.md](live/V25_YCSB_SHIPPED.md) | GAIN 4, LOSS 3, power given 4, the runs disagree 16, STEADY 33 |

### omni-v23

| Table | Judged rows |
|---|---|
| [V23_A10_CAP_ABC.md](gpu/V23_A10_CAP_ABC.md) | GAIN 3, the runs disagree 3, STEADY 7 |
| [V23_A10_CAP_FULL_ABC.md](gpu/V23_A10_CAP_FULL_ABC.md) | GAIN 7, the runs disagree 5, STEADY 1 |
| [V23_A10_FAST_ABC.md](gpu/V23_A10_FAST_ABC.md) | the runs disagree 1, STEADY 12 |
| [V23_A10_STACKS_FULL_ABC.md](gpu/V23_A10_STACKS_FULL_ABC.md) | GAIN 1, LOSS 7, power given 6, STEADY 196 |

### omni-v21

| Table | Judged rows |
|---|---|
| [V21_A100_CAP_ABC.md](gpu/V21_A100_CAP_ABC.md) | GAIN 2, LOSS 2, the runs disagree 1, STEADY 8 |
| [V21_A100_CAP_FULL_ABC.md](gpu/V21_A100_CAP_FULL_ABC.md) | GAIN 1, LOSS 2, STEADY 10 |
| [V21_A100_SAVE_ABC.md](gpu/V21_A100_SAVE_ABC.md) | GAIN 6, the runs disagree 1, STEADY 6 |
| [V21_STACKS_A10_ABC.md](gpu/V21_STACKS_A10_ABC.md) | GAIN 1, LOSS 3, power given 2, the runs disagree 1, STEADY 175 |
| [V21_ALL_FOUR.md](live/V21_ALL_FOUR.md) | GAIN 6, LOSS 1, power given 1, the runs disagree 3, STEADY 6 |
| [V21_BATCH.md](live/V21_BATCH.md) | GAIN 7, LOSS 3, power given 2, the runs disagree 1, STEADY 5 |
| [V21_CAPACITY.md](live/V21_CAPACITY.md) | LOSS 1, the runs disagree 6, STEADY 1 |
| [V21_CRUISEKUBE.md](live/V21_CRUISEKUBE.md) | GAIN 1, LOSS 3, the runs disagree 5, STEADY 7 |
| [V21_FAIRNESS.md](live/V21_FAIRNESS.md) | GAIN 6, LOSS 2, power given 1, the runs disagree 5, STEADY 6 |
| [V21_FAULTS.md](live/V21_FAULTS.md) | GAIN 8, power given 2, the runs disagree 2, STEADY 4 |
| [V21_GOLDILOCKS.md](live/V21_GOLDILOCKS.md) | GAIN 5, LOSS 2, power given 4, STEADY 5 |
| [V21_KAFKA.md](live/V21_KAFKA.md) | GAIN 7, LOSS 9, power given 5, the runs disagree 16, STEADY 19 |
| [V21_KAFKA_SERVICE.md](live/V21_KAFKA_SERVICE.md) | GAIN 5, LOSS 10, power given 5, the runs disagree 15, STEADY 21 |
| [V21_KEDA_CPU_REQUESTS.md](live/V21_KEDA_CPU_REQUESTS.md) | GAIN 5, LOSS 1, power given 4, the runs disagree 2, STEADY 4 |
| [V21_KEDA_REQUESTS.md](live/V21_KEDA_REQUESTS.md) | GAIN 9, power given 2, STEADY 5 |
| [V21_PGBENCH.md](live/V21_PGBENCH.md) | GAIN 6, power given 5, the runs disagree 7, STEADY 18 |
| [V21_PGBENCH_SERVICE.md](live/V21_PGBENCH_SERVICE.md) | GAIN 16, power given 2, the runs disagree 3, STEADY 15 |
| [V21_REDIS.md](live/V21_REDIS.md) | GAIN 14, LOSS 1, power given 10, the runs disagree 7, STEADY 20 |
| [V21_REDIS_SERVICE.md](live/V21_REDIS_SERVICE.md) | GAIN 16, LOSS 1, power given 6, the runs disagree 11, STEADY 18 |
| [V21_REDIS_SHIPPED.md](live/V21_REDIS_SHIPPED.md) | GAIN 5, LOSS 1, power given 1, the runs disagree 10, STEADY 35 |
| [V21_ROBUST_KILL.md](live/V21_ROBUST_KILL.md) | GAIN 7, LOSS 1, power given 1, the runs disagree 3, STEADY 6 |
| [V21_ROBUST_LONG.md](live/V21_ROBUST_LONG.md) | GAIN 5, LOSS 2, power given 2, the runs disagree 1, STEADY 6 |
| [V21_STEADY.md](live/V21_STEADY.md) | GAIN 9, STEADY 7 |
| [V21_SYSBENCH.md](live/V21_SYSBENCH.md) | GAIN 17, power given 7, the runs disagree 14, STEADY 22 |
| [V21_SYSBENCH_SERVICE.md](live/V21_SYSBENCH_SERVICE.md) | GAIN 19, LOSS 1, power given 5, the runs disagree 17, STEADY 18 |
| [V21_SYSBENCH_SHIPPED.md](live/V21_SYSBENCH_SHIPPED.md) | GAIN 1, LOSS 3, power given 13, the runs disagree 21, STEADY 22 |
| [V21_TRACE_GOOGLE2011.md](live/V21_TRACE_GOOGLE2011.md) | GAIN 6, LOSS 1, power given 2, the runs disagree 1, STEADY 6 |
| [V21_WANDERING.md](live/V21_WANDERING.md) | GAIN 7, power given 1, the runs disagree 2, STEADY 6 |
| [V21_YCSB.md](live/V21_YCSB.md) | GAIN 7, LOSS 4, power given 12, the runs disagree 17, STEADY 20 |
| [V21_YCSB_SERVICE.md](live/V21_YCSB_SERVICE.md) | GAIN 4, LOSS 2, power given 9, the runs disagree 32, STEADY 13 |
| [V21_YCSB_SHIPPED.md](live/V21_YCSB_SHIPPED.md) | GAIN 4, LOSS 9, power given 7, the runs disagree 12, STEADY 28 |

### omni-v18

| Table | Judged rows |
|---|---|
| [V18_KAFKA.md](live/V18_KAFKA.md) | GAIN 11, LOSS 4, power given 4, the runs disagree 17, STEADY 20 |
| [V18_KAFKA_SERVICE.md](live/V18_KAFKA_SERVICE.md) | GAIN 7, LOSS 7, power given 5, the runs disagree 20, STEADY 17 |
| [V18_PGBENCH_SERVICE.md](live/V18_PGBENCH_SERVICE.md) | GAIN 9, LOSS 2, power given 2, the runs disagree 14, STEADY 9 |
| [V18_REDIS.md](live/V18_REDIS.md) | GAIN 11, power given 8, the runs disagree 9, STEADY 20 |
| [V18_REDIS_SERVICE.md](live/V18_REDIS_SERVICE.md) | GAIN 14, power given 5, the runs disagree 9, STEADY 20 |
| [V18_REDIS_SHIPPED.md](live/V18_REDIS_SHIPPED.md) | power given 9, the runs disagree 4, STEADY 35 |
| [V18_SYSBENCH_SERVICE.md](live/V18_SYSBENCH_SERVICE.md) | GAIN 13, LOSS 1, power given 2, the runs disagree 25, STEADY 19 |
| [V18_YCSB_SERVICE.md](live/V18_YCSB_SERVICE.md) | GAIN 11, LOSS 6, power given 3, the runs disagree 19, STEADY 16 |

### omni-v17

| Table | Judged rows |
|---|---|
| [V17_KAFKA.md](live/V17_KAFKA.md) | GAIN 20, LOSS 1, power given 6, the runs disagree 13, STEADY 16 |
| [V17_KAFKA_SERVICE.md](live/V17_KAFKA_SERVICE.md) | GAIN 11, LOSS 3, power given 10, the runs disagree 16, STEADY 16 |
| [V17_PGBENCH.md](live/V17_PGBENCH.md) | GAIN 6, LOSS 2, power given 10, the runs disagree 7, STEADY 11 |
| [V17_PGBENCH_SERVICE.md](live/V17_PGBENCH_SERVICE.md) | GAIN 4, LOSS 2, power given 5, the runs disagree 17, STEADY 8 |
| [V17_REDIS.md](live/V17_REDIS.md) | GAIN 14, LOSS 2, power given 5, the runs disagree 10, STEADY 17 |
| [V17_REDIS_SERVICE.md](live/V17_REDIS_SERVICE.md) | GAIN 14, LOSS 1, power given 9, the runs disagree 7, STEADY 17 |
| [V17_REDIS_SHIPPED.md](live/V17_REDIS_SHIPPED.md) | GAIN 1, power given 3, the runs disagree 10, STEADY 34 |
| [V17_SYSBENCH.md](live/V17_SYSBENCH.md) | GAIN 16, LOSS 2, power given 1, the runs disagree 19, STEADY 22 |
| [V17_SYSBENCH_SERVICE.md](live/V17_SYSBENCH_SERVICE.md) | GAIN 18, power given 2, the runs disagree 21, STEADY 19 |
| [V17_SYSBENCH_SHIPPED.md](live/V17_SYSBENCH_SHIPPED.md) | GAIN 19, LOSS 1, power given 10, the runs disagree 11, STEADY 19 |
| [V17_YCSB.md](live/V17_YCSB.md) | GAIN 13, LOSS 7, power given 3, the runs disagree 14, STEADY 18 |
| [V17_YCSB_SERVICE.md](live/V17_YCSB_SERVICE.md) | GAIN 10, LOSS 7, the runs disagree 20, STEADY 18 |
| [V17_YCSB_SHIPPED.md](live/V17_YCSB_SHIPPED.md) | GAIN 3, LOSS 10, power given 1, the runs disagree 17, STEADY 24 |

### omni-v16

| Table | Judged rows |
|---|---|
| [V16_KAFKA.md](live/V16_KAFKA.md) | GAIN 9, LOSS 5, power given 4, the runs disagree 18, STEADY 20 |
| [V16_KAFKA_SERVICE.md](live/V16_KAFKA_SERVICE.md) | GAIN 6, LOSS 2, power given 9, the runs disagree 22, STEADY 17 |
| [V16_PGBENCH.md](live/V16_PGBENCH.md) | GAIN 3, LOSS 3, power given 8, the runs disagree 11, STEADY 11 |
| [V16_PGBENCH_SERVICE.md](live/V16_PGBENCH_SERVICE.md) | GAIN 4, LOSS 4, power given 5, the runs disagree 14, STEADY 9 |
| [V16_REDIS.md](live/V16_REDIS.md) | GAIN 15, power given 11, the runs disagree 4, STEADY 18 |
| [V16_REDIS_SERVICE.md](live/V16_REDIS_SERVICE.md) | GAIN 15, LOSS 1, power given 9, the runs disagree 6, STEADY 17 |
| [V16_REDIS_SHIPPED.md](live/V16_REDIS_SHIPPED.md) | LOSS 1, the runs disagree 12, STEADY 35 |
| [V16_SYSBENCH.md](live/V16_SYSBENCH.md) | GAIN 13, LOSS 3, power given 6, the runs disagree 19, STEADY 19 |
| [V16_SYSBENCH_SERVICE.md](live/V16_SYSBENCH_SERVICE.md) | GAIN 13, power given 8, the runs disagree 21, STEADY 18 |
| [V16_SYSBENCH_SHIPPED.md](live/V16_SYSBENCH_SHIPPED.md) | GAIN 12, LOSS 1, power given 13, the runs disagree 13, STEADY 21 |
| [V16_YCSB.md](live/V16_YCSB.md) | GAIN 9, LOSS 10, power given 5, the runs disagree 14, STEADY 17 |
| [V16_YCSB_SERVICE.md](live/V16_YCSB_SERVICE.md) | GAIN 8, LOSS 4, power given 9, the runs disagree 10, STEADY 24 |
| [V16_YCSB_SHIPPED.md](live/V16_YCSB_SHIPPED.md) | LOSS 8, the runs disagree 20, STEADY 27 |

### omni-v14

| Table | Judged rows |
|---|---|
| [V14_PGBENCH_SERVICE.md](live/V14_PGBENCH_SERVICE.md) | GAIN 4, LOSS 2, power given 2, the runs disagree 14, STEADY 14 |
| [V14_SYSBENCH_SERVICE.md](live/V14_SYSBENCH_SERVICE.md) | GAIN 11, LOSS 2, power given 7, the runs disagree 22, STEADY 18 |
| [V14_YCSB_SERVICE.md](live/V14_YCSB_SERVICE.md) | GAIN 11, LOSS 6, power given 3, the runs disagree 14, STEADY 21 |
| [V14_YCSB_SHIPPED.md](live/V14_YCSB_SHIPPED.md) | GAIN 1, LOSS 7, power given 6, the runs disagree 14, STEADY 27 |

### omni-v12

| Table | Judged rows |
|---|---|
| [V12_ARMADA_4W_BARE.md](live/V12_ARMADA_4W_BARE.md) | GAIN 5, LOSS 8, power given 2, the runs disagree 3, STEADY 4 |
| [V12_ARMADA_4W_BOTH.md](live/V12_ARMADA_4W_BOTH.md) | GAIN 10, LOSS 7, power given 2, STEADY 2 |
| [V12_ARMADA_4W_ORCH.md](live/V12_ARMADA_4W_ORCH.md) | GAIN 8, LOSS 5, power given 1, the runs disagree 3, STEADY 4 |
| [V12_ARMADA_4W_TOP.md](live/V12_ARMADA_4W_TOP.md) | GAIN 6, LOSS 1, power given 2, the runs disagree 2, STEADY 10 |
| [V12_ARMADA_4W_VS.md](live/V12_ARMADA_4W_VS.md) | GAIN 8, LOSS 6, power given 2, the runs disagree 3, STEADY 2 |
| [V12_BINPACK.md](live/V12_BINPACK.md) | GAIN 6, LOSS 7, power given 1, the runs disagree 2, STEADY 6 |
| [V12_BINPACK_4W_BARE.md](live/V12_BINPACK_4W_BARE.md) | GAIN 6, LOSS 4, power given 1, the runs disagree 5, STEADY 6 |
| [V12_BINPACK_4W_BOTH.md](live/V12_BINPACK_4W_BOTH.md) | GAIN 6, LOSS 3, power given 2, the runs disagree 5, STEADY 6 |
| [V12_BINPACK_4W_ORCH.md](live/V12_BINPACK_4W_ORCH.md) | GAIN 3, LOSS 1, power given 1, the runs disagree 7, STEADY 10 |
| [V12_BINPACK_4W_TOP.md](live/V12_BINPACK_4W_TOP.md) | GAIN 6, LOSS 3, power given 2, the runs disagree 5, STEADY 6 |
| [V12_BINPACK_4W_VS.md](live/V12_BINPACK_4W_VS.md) | GAIN 8, LOSS 4, the runs disagree 5, STEADY 5 |
| [V12_CRANE_4W_BARE.md](live/V12_CRANE_4W_BARE.md) | GAIN 4, LOSS 1, power given 2, the runs disagree 2, STEADY 7 |
| [V12_CRANE_4W_BOTH.md](live/V12_CRANE_4W_BOTH.md) | LOSS 2, power given 4, the runs disagree 5, STEADY 5 |
| [V12_CRANE_4W_ORCH.md](live/V12_CRANE_4W_ORCH.md) | GAIN 2, LOSS 1, power given 1, the runs disagree 5, STEADY 7 |
| [V12_CRANE_4W_TOP.md](live/V12_CRANE_4W_TOP.md) | GAIN 1, LOSS 2, power given 2, the runs disagree 4, STEADY 7 |
| [V12_CRANE_4W_VS.md](live/V12_CRANE_4W_VS.md) | GAIN 4, LOSS 2, power given 2, the runs disagree 1, STEADY 7 |
| [V12_KAFKA.md](live/V12_KAFKA.md) | GAIN 10, LOSS 5, power given 4, the runs disagree 19, STEADY 18 |
| [V12_KAFKA_SERVICE.md](live/V12_KAFKA_SERVICE.md) | GAIN 14, LOSS 5, power given 5, the runs disagree 14, STEADY 18 |
| [V12_KAI.md](live/V12_KAI.md) | GAIN 5, LOSS 5, the runs disagree 6, STEADY 6 |
| [V12_KAI_4W_BARE.md](live/V12_KAI_4W_BARE.md) | GAIN 7, LOSS 3, the runs disagree 7, STEADY 5 |
| [V12_KAI_4W_BOTH.md](live/V12_KAI_4W_BOTH.md) | GAIN 5, LOSS 10, power given 2, STEADY 5 |
| [V12_KAI_4W_ORCH.md](live/V12_KAI_4W_ORCH.md) | GAIN 1, LOSS 8, power given 1, the runs disagree 3, STEADY 9 |
| [V12_KAI_4W_TOP.md](live/V12_KAI_4W_TOP.md) | GAIN 6, LOSS 6, power given 2, the runs disagree 3, STEADY 5 |
| [V12_KAI_4W_VS.md](live/V12_KAI_4W_VS.md) | GAIN 14, LOSS 1, the runs disagree 2, STEADY 5 |
| [V12_KARMADA_4W_BARE.md](live/V12_KARMADA_4W_BARE.md) | GAIN 4, LOSS 9, power given 2, the runs disagree 3, STEADY 4 |
| [V12_KARMADA_4W_BOTH.md](live/V12_KARMADA_4W_BOTH.md) | GAIN 4, LOSS 12, power given 2, STEADY 4 |
| [V12_KARMADA_4W_ORCH.md](live/V12_KARMADA_4W_ORCH.md) | LOSS 12, power given 2, STEADY 8 |
| [V12_KARMADA_4W_TOP.md](live/V12_KARMADA_4W_TOP.md) | GAIN 4, LOSS 9, power given 2, the runs disagree 3, STEADY 4 |
| [V12_KARMADA_4W_VS.md](live/V12_KARMADA_4W_VS.md) | GAIN 14, LOSS 2, power given 2, STEADY 4 |
| [V12_KOORDINATOR.md](live/V12_KOORDINATOR.md) | GAIN 7, LOSS 2, power given 2, the runs disagree 4, STEADY 7 |
| [V12_KOORDINATOR_4W_BARE.md](live/V12_KOORDINATOR_4W_BARE.md) | GAIN 6, LOSS 3, the runs disagree 7, STEADY 6 |
| [V12_KOORDINATOR_4W_BOTH.md](live/V12_KOORDINATOR_4W_BOTH.md) | GAIN 10, LOSS 6, power given 1, the runs disagree 1, STEADY 4 |
| [V12_KOORDINATOR_4W_ORCH.md](live/V12_KOORDINATOR_4W_ORCH.md) | GAIN 5, LOSS 5, the runs disagree 4, STEADY 8 |
| [V12_KOORDINATOR_4W_TOP.md](live/V12_KOORDINATOR_4W_TOP.md) | GAIN 7, LOSS 3, the runs disagree 8, STEADY 4 |
| [V12_KOORDINATOR_4W_VS.md](live/V12_KOORDINATOR_4W_VS.md) | GAIN 9, LOSS 5, the runs disagree 4, STEADY 4 |
| [V12_KUBERAY_4W_BARE.md](live/V12_KUBERAY_4W_BARE.md) | GAIN 6, LOSS 8, power given 2, the runs disagree 1, STEADY 5 |
| [V12_KUBERAY_4W_BOTH.md](live/V12_KUBERAY_4W_BOTH.md) | GAIN 3, LOSS 10, power given 4, the runs disagree 2, STEADY 3 |
| [V12_KUBERAY_4W_ORCH.md](live/V12_KUBERAY_4W_ORCH.md) | LOSS 10, power given 4, the runs disagree 2, STEADY 6 |
| [V12_KUBERAY_4W_TOP.md](live/V12_KUBERAY_4W_TOP.md) | GAIN 8, LOSS 2, the runs disagree 6, STEADY 6 |
| [V12_KUBERAY_4W_VS.md](live/V12_KUBERAY_4W_VS.md) | GAIN 13, power given 1, the runs disagree 5, STEADY 3 |
| [V12_KUEUE_4W_BARE.md](live/V12_KUEUE_4W_BARE.md) | GAIN 8, LOSS 4, power given 1, the runs disagree 3, STEADY 6 |
| [V12_KUEUE_4W_BOTH.md](live/V12_KUEUE_4W_BOTH.md) | GAIN 6, LOSS 10, power given 2, STEADY 4 |
| [V12_KUEUE_4W_ORCH.md](live/V12_KUEUE_4W_ORCH.md) | LOSS 11, power given 2, STEADY 9 |
| [V12_KUEUE_4W_TOP.md](live/V12_KUEUE_4W_TOP.md) | GAIN 6, LOSS 4, power given 1, the runs disagree 6, STEADY 5 |
| [V12_KUEUE_4W_VS.md](live/V12_KUEUE_4W_VS.md) | GAIN 17, STEADY 5 |
| [V12_OCM_4W_BARE.md](live/V12_OCM_4W_BARE.md) | GAIN 7, LOSS 7, power given 2, the runs disagree 2, STEADY 4 |
| [V12_OCM_4W_BOTH.md](live/V12_OCM_4W_BOTH.md) | GAIN 4, LOSS 12, power given 2, STEADY 4 |
| [V12_OCM_4W_ORCH.md](live/V12_OCM_4W_ORCH.md) | GAIN 4, LOSS 9, the runs disagree 1, STEADY 8 |
| [V12_OCM_4W_TOP.md](live/V12_OCM_4W_TOP.md) | GAIN 4, LOSS 10, power given 2, the runs disagree 2, STEADY 4 |
| [V12_OCM_4W_VS.md](live/V12_OCM_4W_VS.md) | GAIN 14, LOSS 2, power given 2, STEADY 4 |
| [V12_PGBENCH.md](live/V12_PGBENCH.md) | GAIN 2, power given 4, the runs disagree 18, STEADY 12 |
| [V12_PGBENCH_SERVICE.md](live/V12_PGBENCH_SERVICE.md) | GAIN 3, LOSS 6, power given 6, the runs disagree 10, STEADY 11 |
| [V12_REDIS.md](live/V12_REDIS.md) | GAIN 18, power given 5, the runs disagree 6, STEADY 19 |
| [V12_REDIS_SERVICE.md](live/V12_REDIS_SERVICE.md) | GAIN 11, LOSS 1, power given 8, the runs disagree 10, STEADY 18 |
| [V12_REDIS_SHIPPED.md](live/V12_REDIS_SHIPPED.md) | GAIN 4, the runs disagree 11, STEADY 33 |
| [V12_SYSBENCH.md](live/V12_SYSBENCH.md) | GAIN 18, LOSS 4, power given 8, the runs disagree 11, STEADY 19 |
| [V12_SYSBENCH_SERVICE.md](live/V12_SYSBENCH_SERVICE.md) | GAIN 9, LOSS 1, power given 7, the runs disagree 24, STEADY 19 |
| [V12_SYSBENCH_SHIPPED.md](live/V12_SYSBENCH_SHIPPED.md) | GAIN 10, LOSS 1, power given 13, the runs disagree 18, STEADY 18 |
| [V12_VANILLA.md](live/V12_VANILLA.md) | GAIN 5, LOSS 4, power given 1, the runs disagree 5, STEADY 7 |
| [V12_VOLCANO_4W_BARE.md](live/V12_VOLCANO_4W_BARE.md) | GAIN 9, LOSS 4, power given 1, the runs disagree 2, STEADY 6 |
| [V12_VOLCANO_4W_BOTH.md](live/V12_VOLCANO_4W_BOTH.md) | GAIN 9, LOSS 6, power given 1, the runs disagree 1, STEADY 5 |
| [V12_VOLCANO_4W_ORCH.md](live/V12_VOLCANO_4W_ORCH.md) | GAIN 8, LOSS 4, the runs disagree 1, STEADY 9 |
| [V12_VOLCANO_4W_TOP.md](live/V12_VOLCANO_4W_TOP.md) | GAIN 6, LOSS 4, power given 1, the runs disagree 5, STEADY 6 |
| [V12_VOLCANO_4W_VS.md](live/V12_VOLCANO_4W_VS.md) | GAIN 8, LOSS 5, the runs disagree 4, STEADY 5 |
| [V12_YCSB_SERVICE.md](live/V12_YCSB_SERVICE.md) | GAIN 3, LOSS 1, the runs disagree 11, STEADY 7 |
| [V12_YCSB_SHIPPED.md](live/V12_YCSB_SHIPPED.md) | GAIN 3, LOSS 1, the runs disagree 1, STEADY 6 |

### omni-v11

| Table | Judged rows |
|---|---|
| [V11_CAPACITY.md](live/V11_CAPACITY.md) | GAIN 1, LOSS 4, the runs disagree 2, STEADY 1 |
| [V11_GOLDILOCKS.md](live/V11_GOLDILOCKS.md) | GAIN 8, power given 3, STEADY 5 |
| [V11_KAFKA.md](live/V11_KAFKA.md) | GAIN 11, LOSS 3, power given 4, the runs disagree 16, STEADY 22 |
| [V11_KAFKA_SERVICE.md](live/V11_KAFKA_SERVICE.md) | GAIN 8, LOSS 5, power given 5, the runs disagree 13, STEADY 25 |
| [V11_KEDA_CPU_REQUESTS.md](live/V11_KEDA_CPU_REQUESTS.md) | GAIN 6, power given 3, the runs disagree 3, STEADY 4 |
| [V11_KEDA_REQUESTS.md](live/V11_KEDA_REQUESTS.md) | GAIN 8, LOSS 1, power given 2, the runs disagree 1, STEADY 4 |
| [V11_PGBENCH.md](live/V11_PGBENCH.md) | GAIN 4, power given 5, the runs disagree 8, STEADY 19 |
| [V11_PGBENCH_SERVICE.md](live/V11_PGBENCH_SERVICE.md) | GAIN 3, power given 5, the runs disagree 11, STEADY 17 |
| [V11_REDIS.md](live/V11_REDIS.md) | GAIN 11, power given 6, the runs disagree 12, STEADY 19 |
| [V11_REDIS_SERVICE.md](live/V11_REDIS_SERVICE.md) | GAIN 11, power given 5, the runs disagree 13, STEADY 19 |
| [V11_REDIS_SHIPPED.md](live/V11_REDIS_SHIPPED.md) | LOSS 2, the runs disagree 14, STEADY 32 |
| [V11_ROBUST_KILL.md](live/V11_ROBUST_KILL.md) | GAIN 5, power given 1, the runs disagree 6, STEADY 6 |
| [V11_ROBUST_LONG.md](live/V11_ROBUST_LONG.md) | GAIN 6, LOSS 1, power given 2, the runs disagree 1, STEADY 6 |
| [V11_SYSBENCH.md](live/V11_SYSBENCH.md) | GAIN 16, LOSS 1, power given 1, the runs disagree 23, STEADY 19 |
| [V11_SYSBENCH_SERVICE.md](live/V11_SYSBENCH_SERVICE.md) | GAIN 16, power given 2, the runs disagree 23, STEADY 19 |
| [V11_SYSBENCH_SHIPPED.md](live/V11_SYSBENCH_SHIPPED.md) | GAIN 3, LOSS 6, power given 17, the runs disagree 12, STEADY 22 |
| [V11_YCSB.md](live/V11_YCSB.md) | GAIN 18, LOSS 1, power given 3, the runs disagree 15, STEADY 18 |
| [V11_YCSB_SERVICE.md](live/V11_YCSB_SERVICE.md) | GAIN 16, LOSS 4, power given 6, the runs disagree 11, STEADY 18 |
| [V11_YCSB_SHIPPED.md](live/V11_YCSB_SHIPPED.md) | GAIN 2, LOSS 5, power given 3, the runs disagree 19, STEADY 26 |

### omni-v10

| Table | Judged rows |
|---|---|
| [V10_ALL_FOUR.md](live/V10_ALL_FOUR.md) | GAIN 8, power given 2, the runs disagree 1, STEADY 6 |
| [V10_BATCH.md](live/V10_BATCH.md) | GAIN 8, LOSS 3, power given 2, the runs disagree 1, STEADY 4 |
| [V10_CAPACITY.md](live/V10_CAPACITY.md) | GAIN 3, LOSS 2, the runs disagree 2, STEADY 1 |
| [V10_CRUISEKUBE.md](live/V10_CRUISEKUBE.md) | GAIN 2, LOSS 3, power given 1, the runs disagree 3, STEADY 7 |
| [V10_FAIRNESS.md](live/V10_FAIRNESS.md) | GAIN 6, power given 1, the runs disagree 7, STEADY 6 |
| [V10_FAULTS.md](live/V10_FAULTS.md) | GAIN 6, power given 1, the runs disagree 3, STEADY 6 |
| [V10_GOLDILOCKS.md](live/V10_GOLDILOCKS.md) | GAIN 8, power given 3, STEADY 5 |
| [V10_KAFKA.md](live/V10_KAFKA.md) | GAIN 10, LOSS 7, power given 3, the runs disagree 15, STEADY 21 |
| [V10_KAFKA_SERVICE.md](live/V10_KAFKA_SERVICE.md) | GAIN 11, LOSS 7, power given 3, the runs disagree 12, STEADY 23 |
| [V10_KEDA_CPU_REQUESTS.md](live/V10_KEDA_CPU_REQUESTS.md) | GAIN 6, power given 3, the runs disagree 2, STEADY 5 |
| [V10_KEDA_REQUESTS.md](live/V10_KEDA_REQUESTS.md) | GAIN 7, LOSS 2, power given 2, the runs disagree 1, STEADY 4 |
| [V10_PGBENCH.md](live/V10_PGBENCH.md) | GAIN 10, power given 3, the runs disagree 11, STEADY 12 |
| [V10_REDIS.md](live/V10_REDIS.md) | GAIN 15, power given 5, the runs disagree 8, STEADY 20 |
| [V10_REDIS_SERVICE.md](live/V10_REDIS_SERVICE.md) | GAIN 12, LOSS 2, power given 4, the runs disagree 13, STEADY 17 |
| [V10_ROBUST_LONG.md](live/V10_ROBUST_LONG.md) | GAIN 7, LOSS 1, power given 2, STEADY 6 |
| [V10_STEADY.md](live/V10_STEADY.md) | GAIN 8, the runs disagree 1, STEADY 7 |
| [V10_SYSBENCH.md](live/V10_SYSBENCH.md) | GAIN 16, LOSS 6, power given 5, the runs disagree 17, STEADY 16 |
| [V10_TRACE_GOOGLE2011.md](live/V10_TRACE_GOOGLE2011.md) | GAIN 7, LOSS 1, power given 2, STEADY 6 |
| [V10_WANDERING.md](live/V10_WANDERING.md) | GAIN 6, LOSS 1, power given 1, the runs disagree 2, STEADY 6 |
| [V10_YCSB.md](live/V10_YCSB.md) | GAIN 12, LOSS 3, power given 3, the runs disagree 16, STEADY 21 |

### omni-v7

| Table | Judged rows |
|---|---|
| [V7_ALL_FOUR.md](live/V7_ALL_FOUR.md) | GAIN 8, power given 1, the runs disagree 2, STEADY 6 |
| [V7_BATCH.md](live/V7_BATCH.md) | GAIN 7, LOSS 1, power given 1, the runs disagree 5, STEADY 4 |
| [V7_CAPACITY.md](live/V7_CAPACITY.md) | LOSS 5, the runs disagree 3 |
| [V7_CRUISEKUBE.md](live/V7_CRUISEKUBE.md) | LOSS 2, power given 1, the runs disagree 4, STEADY 9 |
| [V7_FAIRNESS.md](live/V7_FAIRNESS.md) | GAIN 3, LOSS 3, the runs disagree 8, STEADY 6 |
| [V7_FAULTS.md](live/V7_FAULTS.md) | GAIN 8, power given 2, the runs disagree 1, STEADY 5 |
| [V7_GOLDILOCKS.md](live/V7_GOLDILOCKS.md) | GAIN 7, power given 3, the runs disagree 1, STEADY 5 |
| [V7_KAFKA.md](live/V7_KAFKA.md) | GAIN 9, power given 2, the runs disagree 23, STEADY 22 |
| [V7_KAFKA_SERVICE.md](live/V7_KAFKA_SERVICE.md) | GAIN 14, power given 6, the runs disagree 19, STEADY 17 |
| [V7_KEDA_CPU_REQUESTS.md](live/V7_KEDA_CPU_REQUESTS.md) | GAIN 6, power given 3, the runs disagree 3, STEADY 4 |
| [V7_KEDA_REQUESTS.md](live/V7_KEDA_REQUESTS.md) | GAIN 8, LOSS 1, power given 2, STEADY 5 |
| [V7_PGBENCH.md](live/V7_PGBENCH.md) | GAIN 6, LOSS 1, power given 5, the runs disagree 13, STEADY 11 |
| [V7_REDIS.md](live/V7_REDIS.md) | GAIN 11, power given 11, the runs disagree 7, STEADY 19 |
| [V7_REDIS_SERVICE.md](live/V7_REDIS_SERVICE.md) | GAIN 15, power given 6, the runs disagree 8, STEADY 19 |
| [V7_ROBUST_LONG.md](live/V7_ROBUST_LONG.md) | GAIN 7, LOSS 1, power given 2, STEADY 6 |
| [V7_SYSBENCH.md](live/V7_SYSBENCH.md) | GAIN 11, LOSS 2, power given 3, the runs disagree 25, STEADY 19 |
| [V7_TRACE_GOOGLE2011.md](live/V7_TRACE_GOOGLE2011.md) | GAIN 7, LOSS 1, power given 2, STEADY 6 |
| [V7_YCSB.md](live/V7_YCSB.md) | GAIN 14, LOSS 7, the runs disagree 16, STEADY 18 |

### omni-v6

| Table | Judged rows |
|---|---|
| [V6_CRUISEKUBE.md](live/V6_CRUISEKUBE.md) | GAIN 3, the runs disagree 9, STEADY 4 |
| [V6_GOLDILOCKS.md](live/V6_GOLDILOCKS.md) | GAIN 8, power given 3, STEADY 5 |
| [V6_KEDA_CPU_REQUESTS.md](live/V6_KEDA_CPU_REQUESTS.md) | GAIN 6, LOSS 2, power given 4, STEADY 4 |
| [V6_KEDA_REQUESTS.md](live/V6_KEDA_REQUESTS.md) | GAIN 8, LOSS 1, power given 2, the runs disagree 1, STEADY 4 |

### omni-v5

| Table | Judged rows |
|---|---|
| [V5_CAPACITY.md](live/V5_CAPACITY.md) | GAIN 1, LOSS 1, the runs disagree 6 |

### omni-v3

| Table | Judged rows |
|---|---|
| [V3_PGBENCH.md](live/V3_PGBENCH.md) | the runs disagree 1 |
| [V3_YCSB.md](live/V3_YCSB.md) | the runs disagree 1 |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
