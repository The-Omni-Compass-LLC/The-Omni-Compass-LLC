# Preregistration: the real Kubernetes cluster under a public demand trace (written before the runs, 2026-10-08)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Why this test

Every Kubernetes test so far (`docs/K8S_COMPASS_PREREGISTRATION.md`: steady, wandering, all four, faults, batch,
fairness) drives the real cluster with a load schedule of our own: steps we wrote, one change at a time. A referee may
ask whether the shape of our own schedules suits the governor. This test keeps everything else of the wandering test and
replaces only the shape of the demand with one somebody else measured and published: a day of a real cluster's job
submissions, turned into a load schedule by a rule written here before any run. Register row 17, proof-program row 4.

## What is someone else's

- **The cluster and its native controller:** Kubernetes with its Horizontal Pod Autoscaler at the operator's target
  (50%), exactly as in the six tests; kind, six workers, fresh per arm; the floor of two machines, every machine usable.
- **The demand trace:** the **Google cluster-usage traces 2011** (`clusterdata-2011-2`, published by Google, public bucket
  `clusterdata-2011-2` on Google Cloud Storage), table `job_events`: the number of jobs **submitted** (event type 0) in each
  hour of the trace's first day. The trace starts at 600 s; events stamped 0 are jobs that existed before it and are not
  counted. 18 parts of the table (`part-00000` to `part-00017`) cover the day; each is named with its SHA-256 in the
  receipt. It is a batch cluster's job arrivals, not a web service's requests; what we take from it is the **shape** of a
  day's demand, measured by someone else, nothing more.
- **The rule that turns counts into load** (the organism runs' rule, `docs/K8S_COMPASS_PREREGISTRATION.md`, "the real
  cluster as one more muscle"): the 24 hourly counts are placed on the load generator's range by min and max,
  `r_raw(k) = 1 + round(7 (c_k - min c) / (max c - min c))`, 1 to 8 generators (the wandering test's range), rounding half
  up. Then the founder's rule for real traffic (the amendment to the wandering test, 2026-10-04): the schedule moves **one
  step a bin toward the trace's level, never skipping**, starting at the first bin's own level. Each bin is one step of
  **108 s** (the wandering test's step): 24 steps, **2,592 measured seconds**, a day in 43 minutes.

## The schedule, derived and committed before the runs

`tools/trace_schedule.py --out results/traces/google2011` (18 October 2011-trace parts, re-derivable by anyone; the tool and
its rule are tested without the network in `tests/test_trace_schedule.py`, run by `verify.py`). The receipt is
`results/traces/google2011/schedule.json`; the line the workflow takes is `results/traces/google2011/LOAD_STEPS.txt`:

| Hour | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| jobs submitted | 635 | 745 | 742 | 816 | 784 | 1232 | 898 | 764 | 529 | 643 | 683 | 617 | 681 | 795 | 598 | 853 | 882 | 917 | 834 | 1043 | 1039 | 1397 | 884 | 741 |
| level (min-max, 1 to 8) | 2 | 3 | 3 | 3 | 3 | 7 | 4 | 3 | 1 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 4 | 4 | 3 | 5 | 5 | 8 | 4 | 3 |
| **load generators (one step a bin)** | **2** | **3** | **3** | **3** | **3** | **4** | **4** | **3** | **2** | **2** | **2** | **2** | **2** | **3** | **2** | **3** | **4** | **4** | **3** | **4** | **5** | **6** | **5** | **4** |

`load_steps` = `2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4`. Said plainly: the one-step rule reaches the trace's two
sharp hours late (hour 5's level 7 becomes a step to 4, hour 21's level 8 a step to 6), so the replayed day is the trace's
shape with its two spikes blunted to the rate real traffic is allowed to move in this harness; the raw levels stand beside
the steps in the receipt. Nothing in this table was changed after the runs were dispatched.

## Arms, runs and gauges (the wandering test's, unchanged)

- **Workflow** `benchmark-reps`: ten paired repetitions, arms `native compass` in rotated order, a fresh six-worker kind
  cluster per arm, open-loop load (`loadgen=open`, the same work in every arm), `duration_s` 2592, `load_steps` as above,
  the HPA's replica cap as the operator set it (no `replica_ceiling`), floor two, every machine usable. Three separate
  dispatches on one commit are runs A, B and C.
- **Gauges**, native + Omni against native, paired with the 95% interval and read in words: time over the 500 ms line,
  failed requests, p95 and p99 response time, worker machines in service, energy (the declared model; on kind it is not a
  meter), CPU with Omni's own, pods started. No capacity is read (the load does not only rise).
- **Readings**: the three-run rule (`tools/confirm_abc.py`): GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given) when all three runs move
  the same way with every interval clear of zero; no difference beyond the noise when a run's interval includes zero (with
  the count of such runs); the runs disagree when clear runs point different ways. Every row shown, losses included.
- **Table**: written beside the six tests' tables in `results/live/`, named for the trace (V3_TRACE_GOOGLE2011). The test enters the Omni index's Kubernetes category beside the six
  (`tools/omni_index.py`, SOURCES), with the same measures as the wandering test, when its table lands.
- **No tuning case.** Nothing is fitted: the law, the gates, the HPA target, the floor, the line, the probe and the step
  length are the wandering test's; the only new thing is the shape of the demand, and it is someone else's.
- **Engine**: Omni v3, checked on every run by `tools/omni_version.py --commit`.
- **Cost**: free (GitHub's runners); about 1 h 40 min a run, the ten repetitions in parallel.

## Dispatched (2026-10-08 18:43 UTC, on commit `13ee69e8`, Omni v3)

Three dispatches of `benchmark-reps` with the inputs above (`duration_s` 2592, `arms` native compass, `loadgen` open,
`load_steps` 2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4, no replica ceiling): **A 37826513664, B 37826518868,
C 37826522419**, ten paired repetitions each, in parallel. Nothing above this line changed after the dispatch; the
derivation receipt in `results/traces/google2011/schedule.json` is the one committed in that commit.

## Result (runs A, B and C of 2026-10-08, `results/live/V3_TRACE_GOOGLE2011.md`)

All thirty paired repetitions ran and none was marked invalid; the schedule read back from every arm's own log is the one
above, identical in both arms. Native + Omni against native, three runs, the three-run rule:

| Gauge | A | B | C | Reading |
|---|---|---|---|---|
| response time, 95th percentile | −65% | −68% | −71% | **GAIN in all three of our runs** |
| response time, 99th percentile | −49% | −61% | −61% | **GAIN in all three of our runs** |
| response time, mean | −51% | −53% | −55% | **GAIN in all three of our runs** |
| time over the 500 ms line | −81% | −82% | −84% | **GAIN in all three of our runs** |
| failed requests | −13% | −8% | −17% | **GAIN in all three of our runs** |
| worker machines in service, mean | −9.5% | −5.9% | −6.1% | **GAIN in all three of our runs** |
| HPA replicas, mean | −6.3% | −4.8% | −6.2% | **GAIN in all three of our runs** |
| energy, 25 W standby model | −6.7% | −4.3% | −4.6% | **GAIN in all three of our runs** |
| energy, idle-power model | −0.2% | −0.4% | −0.5% | no difference beyond the noise in 1 of 3 runs |
| pods started | +23% | +27% | +35% | no difference beyond the noise in 1 of 3 runs |
| pod start wait | inside the noise | inside the noise | inside the noise | no difference beyond the noise |
| pods with no machine to take them | 0 in both arms | 0 | 0 | same |

**9 gauge-rows GAIN in all three of our runs, 0 power given in all three of our runs, 0 where the runs disagree.** Shown and not judged: CPU used with
Omni's own −3.7% to −4.5% (Omni's own CPU about 0.0095 of a core), host CPU busy −3% to −4%, utilisation +0.4% to +3.8%.
Read against the wandering test (our own schedule: p95 −57% to −63%, machines inside the noise): under a day somebody else
measured the governor read the same way on service and read GAIN on machines (−6% to −10%, the same in all three of our runs, where the wandering
test's machines row was inside the noise), because the trace's long quiet stretch (hours 8 to 14 at two generators) is
where machines are given back and the wandering schedule has no such stretch. The one row that leans the other way, more
pods started (+23% to +35% as point estimates, one run's interval across zero), is the price of following demand up and
down; it is in the table and is not an index column. The test enters the Omni index's Kubernetes category as its seventh
test: the category moves from +25.5% to **+28.8%** and the headline from +23.5% to **+24.1%**. The "our own schedules"
threat (`docs/OMNI_COMPASS_MANUAL.md`, section 16.7) is answered for one public day-shape; the Azure Functions trace, a
request-driven shape, follows by the same rule.

## What a referee should ask, and the answers given before the result

- *Is a batch cluster's job arrival a fair stand-in for a web service's demand?* It is a real day's demand shape measured
  by someone else, which is what this test is for; it is not the same service, and the result is read as "under a
  published day-shape", not as "under Google's load". The Azure Functions invocation trace, a request-driven shape, is
  the next trace in row 17 and follows the same rule.
- *Does blunting the spikes favour the governor?* It blunts them for both arms equally, and the one-step rule is the
  rule every real-traffic test here has run under since 4 October; a schedule with the raw levels would be a different,
  also legitimate, test, and the receipt holds the raw levels so a reader can run it.
- *Why a day in 43 minutes?* Because the wandering test's step is 108 s and its runs fit a GitHub job; the compression
  is the same for both arms, and the step length is the one every reading in this harness has been taken at.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
