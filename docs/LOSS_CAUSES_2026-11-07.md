# Koordinator's rows on omni-v25, read from their own files: 7 November 2026

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The LOSS ledger (`docs/LOSS_LEDGER.md`) listed Koordinator's two batch-stream tables on omni-v25 without a cause for most of
their rows: the web service's response time (95th and 99th percentile), its time over the response line and its alert minutes,
its pod start waits, and the queue's rows (finished, job wait, turnaround, jobs unfinished). The page
`docs/LOSS_CAUSES_2026-11-06.md` (section 2) found that the web service's target flips on these rigs a tenth as often as on the
other batch rigs, so it did not write their cause. This page reads them from the runs' own files on the branch `raw`: the
governor's audit (`audit.jsonl`), each request's response time (`latency.csv`), the cluster's capture (`capture.csv`), the
jobs (`jobs.json`) and Koordinator's batch processor at the window's end (`batch_queue_end.json`). Every number below is read
again from those files by `python3 tools/koordinator_causes.py` (a checkout whose git holds the branch `raw`).

Runs: Koordinator on the cgroup root (`results/live/V25_KOORDINATOR_CGROUP.md`) 42173258848, 42173278954 and 42185612749;
Koordinator (`results/live/V25_KOORDINATOR.md`) 41800261877, 41800269022 and 41802293120; ten repetitions each, 60 in all.
The rig: Koordinator 1.8.0 with the operator's colocation profile (`deploy/kind/koordinator-colocation.yaml`), the queue's 24
jobs best effort on Koordinator's batch resources, every kind node on one four-core runner.

## 1. What Omni-Compass wrote

Almost everything the governor wrote on these rigs is the conveyance (`omni_controller/muscles.py`): 28 to 81 raises of a web
pod's processor limit an arm (to 3,300m for a machine's one serving pod, 1,650m for two) while the shared host stood under 70%
busy, and nearly as many hand-backs, 24 to 70 an arm, each putting every raised limit back to the operator's 500m with the
reason "the shared host at its top (busy 0.79 to 0.92) beside another workload's room" (the omni-v13 rule). The web service's
target was written 0 to 7 times an arm.

## 2. The web service's rows: the conveyance's cycle

Each minute of each repetition is read in both arms at the same point of the load, and sorted by what the conveyance did in
that minute of Omni-Compass's arm:

| Rig | Minutes | What the conveyance did | Mean response time | 95th percentile | 99th percentile |
|---|---|---|---|---|---|
| On the cgroup root | 461 | held its raise (no write) | down 25.7%: faster, GAIN | down 8.4%: faster, GAIN | down 6.1%: faster, GAIN |
| On the cgroup root | 268 | handed back in the minute | down 0.1%, STEADY | up 15.9%: slower, LOSS | up 13.8%: slower, LOSS |
| On the cgroup root | 22 | raised only | down 12.4%: faster, GAIN | up 3.4%: slower, LOSS | up 2.2%: slower, LOSS |
| Koordinator | 439 | held its raise (no write) | down 28.9%: faster, GAIN | down 11.6%: faster, GAIN | down 5.0%: faster, GAIN |
| Koordinator | 271 | handed back in the minute | down 1.4%: faster, GAIN | up 11.9%: slower, LOSS | up 9.7%: slower, LOSS |
| Koordinator | 41 | raised only | down 14.3%: faster, GAIN | up 8.9%: slower, LOSS | up 4.2%: slower, LOSS |

Each change is the pooled requests of those minutes against native's in the same minutes; it is a reading of the files, not
a three-run reading. Where the conveyance held its raise, the web service answered a quarter faster than native. In the minutes
it handed back, about 36% of all minutes, the slowest requests ran 10% to 16% slower than native's, and the table's 95th and
99th percentile, its time over the line and its alert minutes come from those minutes. In run 42185612749, repetition 3, the
web service's mean was 79 to 83 ms against native's 125 to 133 ms from 180 to 300 s, while the raise held; from 660 to 900 s,
with a hand-back and a raise every minute, it was 173 to 198 ms against native's 147 to 166 ms.

**The cause.** An engine fault of the conveyance. One raise gives a serving pod 2.8 more cores on a four-core host, so the next
reading finds the host past 75% busy, and the rule hands every raised limit back to the operator's 500m at once; the host falls
under 70% and the raise comes back. The step is larger than the band (5 points), so the conveyance cycles, and each hand-back
throttles a pod serving its queue of requests to 500m until the next raise. The page of 6 November found the same cycle on the
KAI scheduler's rig (`docs/LOSS_CAUSES_2026-11-06.md`, section 1), where it lowered the web service's mean response time and
was put on the next version's list as a defect of the law; on Koordinator's rigs the target hardly flips, and the cycle is what
remains.

## 3. The queue's rows: the processor Koordinator reclaims

Koordinator gives its best-effort jobs the processor the serving pods do not use: its manager computes each node's batch
resources "from what the latency-sensitive pods leave unused" (the rig's colocation profile, `deploy/kind/koordinator-colocation.yaml`).
At the window's end the batch processor summed over the seven nodes was:

| Rig | Native, mean of 30 repetitions | Omni-Compass, mean of 30 repetitions | Change |
|---|---|---|---|
| On the cgroup root | 7,653 millicores | 6,779 millicores | down 11.4%: less batch processor |
| Koordinator | 7,032 millicores | 6,273 millicores | down 10.8%: less batch processor |

**The cause.** The same conveyance: it reads the host's unused processor as idle and gives it to the web service's pods, and on
this rig that processor is the batch processor Koordinator reclaims for the queue. The web service's faster minutes are paid for
with the queue's processor, a trade between muscles the engine's strictest rule never makes; the queue's jobs wait longer for a
place (job wait up 26.6% to 45.4% by run on the cgroup root) and take longer to finish. The control plane's reads at the 10 s
beat, suspected on these rows until now (`docs/LOSS_CAUSES_2026-11-05.md`), are not needed to explain them and stay unmeasured.

## 4. The pod start waits: the target's flips

Native's arm started 0 to 3 web pods in a run; Omni-Compass's arm started 4 to 20 (on the cgroup root 4, 17 and 6; Koordinator
19, 7 and 20), each waiting 2 to 3 s for its container and its readiness probe. In the 37 repetitions where the governor wrote
the web service's target, native started 6 web pods and Omni-Compass 67; in the 23 where it wrote none, 3 and 6. The starts are
the target's fail-up and return (30% and 50%), with the queue's best-effort pods waiting for Koordinator's batch processor: the
omni-v25 fault of `docs/LOSS_CAUSES_2026-11-06.md`, fixed in omni-v26 (`docs/OMNI_V26.md`).

## 5. What decides it

The pod start waits: the benchmark's three runs on omni-v26. The web service's rows and the queue's: the next version, through
the model gate first. The conveyance's raise sized so the shared host stays under its hand-back line, a hand-back that steps a
limit down by what the host is over rather than all the way to the operator's, and no raise of a serving pod's limit while
another workload's pods wait for a place, the test omni-v26 already makes for the target. The model gate's shared-host model is
set from these runs' own files. Then the benchmarks' three runs on that engine.

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
