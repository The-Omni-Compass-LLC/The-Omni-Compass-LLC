# The batch rigs' web rows on omni-v25, read from their own files: 6 November 2026

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The LOSS ledger (`docs/LOSS_LEDGER.md`) listed 214 rows on omni-v25 with no cause written. Most sit on the batch-scheduler rigs:
the web service's response time (mean, 95th and 99th percentile), its time over the response line, its alert minutes, its failed
requests and its pod start waits, read while a batch queue shares the cluster (`results/live/V25_<SYSTEM>_4W_<WAY>.md` and
`results/live/V25_<SYSTEM>.md`). This page reads those rows from the runs' own files on the branch `raw`: the governor's
audit (`audit.jsonl`), the cluster's capture (`capture.csv`), each request's response time (`latency.csv`), each serving
pod's record (`pod_watch.json`) and the queue's end (`batch_done.txt`). The page `docs/LOSS_CAUSES_2026-11-05.md` read the
queue's own rows; this one reads the web service's.

## 1. The KAI scheduler's four ways, Omni-Compass on the organism alone: 30 repetitions

`results/live/V25_KAI_4W_BARE.md`, runs 41809041712, 41810759693 and 41812560443, ten repetitions each.

**The window has two parts.** For the first 12 to 16 minutes the batch queue holds the cluster. The web service's response
time climbs from about 0.4 s to 3 to 5 s in both arms, and Kubernetes' own CPU autoscaler takes the starved web pods down to
one, in both arms alike. Then the queue ends. From 60 s after the later of the two arms' ends to the window's end, the web
service's mean response time with Omni-Compass on top is **41.1% to 53.8% lower than native's in all 30 repetitions** (a mean of
45.9% lower; in run 41810759693, repetition 2, 83 to 89 ms against 151 to 162 ms). A three-run table reads the whole window, so
the rows that read LOSS come from the first part.

**In the first part, the governor's target flips.** In repetition 2 of run 41810759693 the governor wrote the web service's
autoscaler target 13 times in the first 270 s: 30%, 50%, 30%, 50%, every one or two decisions (10 to 20 s). The decision behind
it is the same every time: the response line is far behind it (the compass law's position at its wall, 1.0). Two rules then
choose between the cover's floor (30%, more pods: the fail-up) and native's own target (50%):

- the fail-up is taken only while **no pod in the cluster waits** (`omni_controller/controller.py`, the decision's `load`);
- otherwise the rule reads the wait as "pods waiting for a machine that is gone" and returns native's target.

The count of waiting pods is the whole cluster's (`snapshot`, `pending`), by design: a pod of any workload waiting means the
room is spoken for, and Omni-Compass's extra pods may not hold it. On these rigs the batch queue's own pods wait for a place as
its normal queueing, on and off, so the decision turns between the two rules with the queue. The rule meant to stop exactly that
is the immune hand-back (`_pods_wait_handback`, omni-v19: "a pod waits, the HPA target back to native's 50% for 600 s"). Its
hold keeps native's target for ten minutes. But only the fast check starts it, and only while the target still stands below
native's. The decision has already put the target back at native's by then, so the hold almost never starts, and the next
decision that finds no pod waiting fails up again. In that repetition the hold caught on only at 274.5 s, when a fast check
happened to find the floor with pods waiting. At 273 s the capture shows 5 pods waiting, and the pod watch shows all 7 of the
web service's pods scheduled and Ready since 22 s at the latest: the waiting pods were the queue's. Across the 30 repetitions the
governor wrote 304 target changes that turned back on the one before, and the hold caught on 21 times.

**What the flips cost.** Kubernetes' autoscaler answers a lower target at once and holds a higher one for its five-minute window,
so the flipping keeps the extra pods: 7 web pods against native's 5 for the first five minutes in that repetition. They take
processor and room from the queue the engine's own rule says it never trades with. In the 15 repetitions where the queue ran
long (857 to 939 s in native's arm) the conveyance wrote at most 8 hand-backs, so the target's flips were nearly all the
governor did, and **the queue finished 0.1% to 6.8% later** (a mean of 2.25%). The web service's minutes at 1 to 5 s last as
long as the queue, so its 95th percentile, its time over the line and its alert minutes rise with it.

**The conveyance's own cycle is real, and not the cause.** In the 15 repetitions where the queue ran short (722 to 768 s in
native's arm), the host stood under 70% busy at times, and the conveyance raised the web pods' limits (to 2,700m to 3,700m) and
handed them back when the host reached 75% busy, 10 to 123 times an arm, 1,100 times in all. One raise gives a pod 2.2 to 3.2 more
cores on a four-core machine, so a single step jumps the band's 5-point cushion (`omni_controller/muscles.py`, the omni-v13
hand-back). But the more it cycled, the lower the web service's mean response time against native (a correlation of -0.60 over
the 30 repetitions), and in those repetitions the queue was 0.62% later on average. Its cost is the writes, about 250 an arm.
It goes on the next version's list as a defect of the law (a step larger than the band), not as the cause of these rows.

## 2. The same rules on the other rigs

One run of ten repetitions on each rig, the governor's audit read for the same two records. "Flips" are target changes that
turn back on the one before.

| Rig | Way | Flips | Hand-backs on a waiting pod | 95th percentile, median change | Queue, median change |
|---|---|---|---|---|---|
| Volcano | on the organism alone | 66 | 11 | up 5.4%, LOSS | up 0.3% |
| Kueue | on the organism alone | 84 | 8 | up 15.0%, LOSS | up 1.5% |
| Gödel | on the organism alone | 67 | 8 | up 13.2%, LOSS | up 0.8% |
| The bin-packing profile | on the organism alone | 86 | 8 | up 15.9%, LOSS | up 0.3% |
| Armada | on the organism alone | 212 | 23 | up 32.3%, LOSS | up 5.2% |
| Karmada | on the organism alone | 148 | 25 | up 37.7%, LOSS | up 3.9% |
| Open Cluster Management | on the organism alone | 166 | 17 | up 21.7%, LOSS | up 5.5% |
| KubeRay | on the organism alone | 98 | 10 | up 10.3%, LOSS | up 0.6% |
| The KAI scheduler | on top of it | 66 | 9 | up 6.2%, LOSS | |
| Volcano | on top of it | 65 | 8 | up 25.3%, LOSS | |
| Kueue | on top of it | 64 | 8 | up 18.0%, LOSS | |
| Gödel | on top of it | 75 | 7 | up 3.4%, LOSS | |
| The bin-packing profile | on top of it | 73 | 8 | down 0.4%, EVEN | |
| Armada | on top of it | 2 | 0 | down 44.7%, GAIN | |
| Karmada | on top of it | 132 | 19 | up 29.4%, LOSS | |
| Open Cluster Management | on top of it | 202 | 20 | up 35.4%, LOSS | |
| KubeRay | on top of it | 2 | 2 | down 2.0%, GAIN | |

Runs: Volcano 41809087487, Kueue 41809077335, Gödel 41816164023, the bin-packing profile 41810750964, Armada 41828277526,
Karmada 41816173049, Open Cluster Management 41816181570, KubeRay 41816118654, the KAI scheduler 41809041712. Each change is the
median over the run's ten repetitions, read from `latency.csv` and `batch_done.txt`. It is a reading of one run, not a three-run
reading.

The two rigs where the target hardly flipped are the two where the queue waits outside the cluster's pods: Armada on top holds its
jobs in its own queue, and KubeRay hands work to its own head. There no pod waits, the fail-up holds, the immune hand-back never
fires, and Omni-Compass's 95th percentile reads lower than native's. Where the flips run highest (Karmada and Open Cluster
Management, a group of two clusters), the rise is largest.

The batch stream through each scheduler, Omni-Compass on top against the scheduler alone, one run of ten repetitions each:

| Scheduler | Run | Flips | Hand-backs on a waiting pod | 95th percentile, median change |
|---|---|---|---|---|
| The KAI scheduler | 41800238758 | 77 | 7 | up 2.0%, LOSS |
| Volcano | 41762072500 | 32 | 8 | up 4.8%, LOSS |
| Kueue | 41762066634 | 78 | 12 | up 4.5%, LOSS |
| The bin-packing profile | 41802308779 | 101 | 8 | up 3.5%, LOSS |
| The default scheduler | 41802300531 | 73 | 11 | up 8.0%, LOSS |
| Koordinator | 41800261877 | 10 | 3 | up 4.9%, LOSS |
| Koordinator, on the cgroup root | 42173258848 | 12 | 3 | up 7.8%, LOSS |
| The plain batch stream | 41753030885 | 0 | 0 | up 0.6%, EVEN |

Koordinator's two rigs flip a tenth as often and still rise, so this page does not write their cause: on them the rows stay
without one until they are read. They were read on 7 November (`docs/LOSS_CAUSES_2026-11-07.md`): the conveyance's cycle, and
the processor Koordinator reclaims for its batch jobs given to the web service. The plain batch stream never flips; its queue's row is the governor's own processor
(`docs/LOSS_CAUSES_2026-11-05.md`, section 1).

## 3. The cause, and what decides it

**The cause.** An engine fault of omni-v25, and of every engine since omni-v19's hand-back. When a pod waits while a service's
target stands at the fail-up's floor, the decision returns native's target but does not start the hand-back's hold
(`omni_controller/controller.py`, the branch "past the wall, but not from load", and the same branch of the pod muscle of
Omni-Compass's own). The hold is started only by the fast check, which skips a target already at native's. So the fail-up is
taken again at the next decision with no pod waiting, and the target flips with the queue's waiting. Kubernetes' autoscaler takes
a lower target at once and a higher one only after its five-minute window, so the flips keep the extra pods: they hold room the
queue's waiting pods were owed, a trade between muscles the engine's strictest rule never makes. The shared test machine (every
kind node on one four-core runner) makes the trade visible at once. On a real cluster the same rule would flip the target wherever
a batch system leaves its pods waiting.

**What it is not.** It is not the conveyance (its cycle lowers the web's mean response time where it runs). It is not the
immune system's comparison with native's twin, which read "native not stronger: stays" at every decision of the repetition read.
And it is not the count of every waiting pod, which is the rule's protection of the neighbour, not its fault.

**What decides it.** omni-v26 (`docs/OMNI_V26.md`), landed on 7 November through the model gate. The decision that returns native's target because pods wait starts the same hold as the hand-back (ten minutes, doubled for each hold in a row, halved after a quiet one) when the waiting pods include those of a workload no autoscaler governs, so the fail-up is not taken again while the room is spoken for; another governed service keeps its own rule, and a DaemonSet's pod never starts the hold. Its model gate against omni-v25 (`results/model_gate/V26_VS_V25.md`) read all twelve models identical, 104 readings, no LOSS. The batch queue's replay (`results/model_gate/V26_BATCH_FLIP.md`, `tools/batch_flip_model.py`, class S, open loop) put these runs' own timelines through both governors: the target's flips down 88.6% and the time below native's target while the queue's pods waited down 78.2%. The benchmarks' three runs on omni-v26 decide the rows. The conveyance's step, sized to the band, stays on the next version's list.

The rows that carry this cause in the ledger (`tools/loss_ledger.py`, keyed with omni-v25) are the web service's response time,
time over the response line and alert minutes on the tables read above where the target flipped: on the organism alone, the KAI
scheduler's, Volcano's, Kueue's, Gödel's, the bin-packing profile's, Armada's, Karmada's, Open Cluster Management's and KubeRay's;
on top of the orchestrator, the KAI scheduler's, Volcano's, Kueue's, Gödel's, the bin-packing profile's, Karmada's and Open
Cluster Management's; and the
batch stream through the KAI scheduler, Volcano, Kueue, the bin-packing profile and the default scheduler. Their size is each
table's own; their pod start waits carry the cause of section 4. Their failed requests were not read here and stay without a cause until they are.

## 4. The pod start waits on the same rigs

The same tables read the web service's pod start wait LOSS: on most of them native's arm started no web pod inside the window in
most repetitions, so its total reads zero and Omni-Compass's arm reads a few seconds ("0 to 2.4 s"). The starts are the flips' extra
pods. Each start waits 2 to 3 s for its container and its readiness probe, a wait native never paid because it never started the pod.
Counted from each repetition's capture (`capture.csv`, every rise in the web service's replicas), one run of ten repetitions each:

| Rig | Way | Web pods started, native | Web pods started, Omni-Compass |
|---|---|---|---|
| The KAI scheduler | on the organism alone (three runs) | 1, 1, 2 | 13, 21, 20 |
| Volcano | on the organism alone | 2 | 16 |
| Kueue | on the organism alone | 1 | 13 |
| Gödel | on the organism alone | 3 | 14 |
| The bin-packing profile | on the organism alone | 1 | 17 |
| Armada | on the organism alone | 6 | 23 |
| Karmada | on the organism alone | 4 | 31 |
| Open Cluster Management | on the organism alone | 3 | 27 |
| KubeRay | on the organism alone | 0 | 13 |
| The KAI scheduler | on top of it | 2 | 7 |
| Volcano | on top of it | 0 | 9 |
| Kueue | on top of it | 0 | 11 |
| Gödel | on top of it | 3 | 11 |
| The bin-packing profile | on top of it | 2 | 17 |
| Karmada | on top of it | 1 | 34 |
| Open Cluster Management | on top of it | 0 | 41 |
| Volcano | the batch stream | 0 | 10 |
| Kueue | the batch stream | 1 | 9 |
| The bin-packing profile | the batch stream | 6 | 19 |
| The default scheduler | the batch stream | 3 | 11 |

The batch stream through the KAI scheduler started the same 3 web pods in both arms in the run read, so its pod start rows do not
take this cause. On Armada on the organism alone (run 41828277526, repetitions 1 to 3) the pod watch shows each of Omni-Compass's
starts Ready 2 to 3 s after it was made, none of them waiting for a place.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
