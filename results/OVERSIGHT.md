# The Oversight Line: the Pages a Person Would Answer, Native Against Omni-Compass on Native

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> "They don't need a 3 a.m. call and they don't need [anyone] to turn knobs when OmniCompass is ... self-gauging" (the founder, 3 November 2026)

## What GitHub's runs measure, and what they cannot

Every benchmark runs on GitHub's own machines with nobody watching, in both arms: no person is on call, no person turns a knob, so no engineer's hour and no salary is on any receipt, and none can be. What every real Kubernetes receipt does measure is the event that calls a person: an **alert minute**, a whole minute of the measured window whose 95th percentile response time, failed requests counted over, was over the response line, the minute an on-call page would be open (`tools/live_reps.py`, `babysitting`; judged, fewer is GAIN). Beside it each receipt shows the settings the governor wrote on its own, each in its audit with its reason and read back (shown, not judged: native's own autoscaler runs untouched in both arms).

## The pages, test by test (omni-v26, every real Kubernetes three-run table that carries them)

| Test | Alert minutes a repetition, native → Omni-Compass on native (mean of the three runs) | Change | Reading (the table's own, the one key) | Settings the governor wrote on its own, a repetition | Record |
|---|---|---|---|---|---|
| All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back) | 26.53 → 20.70 | down 22.0% | GAIN in all three of our runs | 51.8 | `results/live/V26_ALL_FOUR.json` |
| Batch queue: 240 CPU jobs and cruise | 10.53 → 10.80 | up 2.5% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 9.7 | `results/live/V26_BATCH.json` |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream: Omni-Compass on top (register row 88) | 8.93 → 9.33 | up 4.5% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 83.1 | `results/live/V26_BINPACK.json` |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 88) | 5.90 → 6.37 | up 7.9% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 162.6 | `results/live/V26_BINPACK_4W_BARE.json` |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways: Omni-Compass on top of the bin-packing profile against the bin-packing profile as shipped (register row 88) | 4.60 → 4.80 | up 4.3% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 138.0 | `results/live/V26_BINPACK_4W_TOP.json` |
| The cost to match: native, native tuned harder by its operator (HPA target 40, 30, 20) and native with Omni-Compass on top; this table: Omni-Compass on top against native | 2.23 → 0.00 | down 100.0% | GAIN in all three of our runs | 19.1 | `results/live/V26_COST_TO_MATCH.json` |
| Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 90) | 0.07 → 0.10 | up 50.0% | the runs disagree | 6.2 | `results/live/V26_CRANE_4W_BARE.json` |
| Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways: Omni-Compass on top of Crane against Crane as shipped (register row 90) | 0.17 → 0.03 | down 80.0% | GAIN by the mean of our three runs, beyond the noise in 0 of 3 | 6.9 | `results/live/V26_CRANE_4W_TOP.json` |
| CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations | 0.00 → 0.00 | none in either arm | STEADY, the same | 4.6 | `results/live/V26_CRUISEKUBE.json` |
| CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations, the recorder counting a worker held by CruiseKube's own overload mark while it serves as in service | 0.00 → 0.00 | none in either arm | STEADY, the same | 4.1 | `results/live/V26_CRUISEKUBE_RECORDER.json` |
| Fairness: a noisy neighbour on the same workers | 7.80 → 7.87 | up 0.9% | the runs disagree | 117.2 | `results/live/V26_FAIRNESS.json` |
| Faults: a machine down, a spike, a runaway pod, a blind probe | 6.33 → 5.53 | down 12.6% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 | 44.0 | `results/live/V26_FAULTS.json` |
| Faults, extended: the four faults and the two that blind a governor (the API server frozen 30 s, the metrics server gone two minutes) in a 2,500 s window | 7.67 → 6.17 | down 19.6% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 | 59.5 | `results/live/V26_FAULTS_EXTENDED.json` |
| The Gödel scheduler under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 93) | 10.10 → 10.63 | up 5.3% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 16.7 | `results/live/V26_GODEL_4W_BARE.json` |
| The Gödel scheduler under the batch stream, the four ways: Omni-Compass on top of Gödel against Gödel as shipped (register row 93) | 9.73 → 10.40 | up 6.8% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 16.8 | `results/live/V26_GODEL_4W_TOP.json` |
| Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender | 0.73 → 0.00 | down 100.0% | GAIN by the mean of our three runs, beyond the noise in 1 of 3 | 413.6 | `results/live/V26_GOLDILOCKS.json` |
| The KAI scheduler under the batch stream: Omni-Compass on top of KAI's queues (register row 91) | 7.73 → 8.50 | up 9.9% | the runs disagree | 100.8 | `results/live/V26_KAI.json` |
| The KAI scheduler under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 91) | 6.67 → 7.90 | up 18.5% | LOSS by the mean of our three runs, beyond the noise in 2 of 3 | 150.4 | `results/live/V26_KAI_4W_BARE.json` |
| The KAI scheduler under the batch stream, the four ways: Omni-Compass on top of KAI against KAI as shipped (register row 91) | 7.00 → 8.50 | up 21.4% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 97.9 | `results/live/V26_KAI_4W_TOP.json` |
| Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top | 0.27 → 0.10 | down 62.5% | the runs disagree | 421.1 | `results/live/V26_KEDA_CPU_REQUESTS.json` |
| Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top | 3.33 → 1.13 | down 66.0% | GAIN in all three of our runs | 82.6 | `results/live/V26_KEDA_REQUESTS.json` |
| Koordinator under the batch stream: Omni-Compass on top of its colocation (register row 89) | 0.10 → 0.20 | up 100.0% | the runs disagree | 108.2 | `results/live/V26_KOORDINATOR.json` |
| Koordinator under the batch stream, on the cgroup root its own tests use: Omni-Compass on top of its colocation (register row 89) | 0.07 → 0.33 | up 400.0% | the runs disagree | 106.4 | `results/live/V26_KOORDINATOR_CGROUP.json` |
| KubeRay (the Ray autoscaler) under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 92) | 7.20 → 7.63 | up 6.0% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 130.8 | `results/live/V26_KUBERAY_4W_BARE.json` |
| KubeRay (the Ray autoscaler) under the batch stream, the four ways: Omni-Compass on top of KubeRay against KubeRay as shipped (register row 92) | 23.00 → 23.17 | up 0.7% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 34.6 | `results/live/V26_KUBERAY_4W_TOP.json` |
| Kueue under the batch stream: Omni-Compass on top of Kueue's admission (register row 63) | 8.37 → 9.57 | up 14.3% | LOSS by the mean of our three runs, beyond the noise in 2 of 3 | 114.9 | `results/live/V26_KUEUE.json` |
| Kueue under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 63) | 7.87 → 8.50 | up 8.1% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 120.5 | `results/live/V26_KUEUE_4W_BARE.json` |
| Kueue under the batch stream, the four ways: Omni-Compass on top of Kueue against Kueue as shipped (register row 63) | 8.37 → 8.90 | up 6.4% | LOSS by the mean of our three runs, beyond the noise in 2 of 3 | 128.2 | `results/live/V26_KUEUE_4W_TOP.json` |
| Open Cluster Management on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 96) | 11.13 → 12.50 | up 12.3% | LOSS in all three of our runs | 112.7 | `results/live/V26_OCM_4W_BARE.json` |
| Open Cluster Management on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Open Cluster Management against Open Cluster Management as shipped (register row 96) | 13.43 → 16.23 | up 20.8% | LOSS by the mean of our three runs, beyond the noise in 2 of 3 | 73.0 | `results/live/V26_OCM_4W_TOP.json` |
| Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs | 9.47 → 7.53 | down 20.4% | GAIN in all three of our runs | 80.1 | `results/live/V26_ROBUST_KILL.json` |
| Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched | 73.00 → 56.67 | down 22.4% | GAIN by the mean of our three runs, beyond the noise in 0 of 3 | 165.2 | `results/live/V26_ROBUST_LONG.json` |
| Steady load: the same fixed-rate work sent to both arms | 2.47 → 0.00 | down 100.0% | GAIN in all three of our runs | 19.1 | `results/live/V26_STEADY.json` |
| A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4) | 19.80 → 7.37 | down 62.8% | GAIN in all three of our runs | 70.3 | `results/live/V26_TRACE_GOOGLE2011.json` |
| The Kubernetes scheduler as shipped under the batch stream: Omni-Compass on top of the default scheduler alone (register row 88) | 8.20 → 8.63 | up 5.3% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 137.8 | `results/live/V26_VANILLA.json` |
| Volcano under the batch stream: Omni-Compass on top of Volcano's queues (register row 63) | 4.63 → 5.27 | up 13.7% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 135.0 | `results/live/V26_VOLCANO.json` |
| Wandering demand: load that steps up and down by one (1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1) | 26.50 → 20.10 | down 24.2% | GAIN in all three of our runs | 50.6 | `results/live/V26_WANDERING.json` |

**Together.** Over the 37 tests the pages a repetition add up to 349.9 alert minutes on native and 311.5 with Omni-Compass on top: **down 11.0%** (our arithmetic over the tables, each test weighed by its own minutes; the two-hour test holds 21% of native's). Fewer pages in 13 of the 37 tests, to none at all in 3, the same in 2, more in 22. Each test's word is its own table's, by the one key.

**Run by run.** The tables summed in each of our three runs (one repetition of every test, native beside Omni-Compass on native); each difference's 95% interval adds its tables' variances, each from that table's own interval and repetitions.

| Run | Alert minutes, native → Omni-Compass on native, summed | Change | Difference, 95% interval (minutes) | Settings the governor wrote on its own, an hour |
|---|---|---|---|---|
| A | 348.90 → 308.17 | down 11.7% | −40.73 (−54.77 to −26.69) | 227 |
| B | 393.97 → 349.87 | down 11.2% | −44.10 (−57.12 to −31.08) | 207 |
| C | 306.93 → 276.37 | down 10.0% | −30.57 (−40.70 to −20.43) | 226 |

**Read by the one key: GAIN in all three of our runs.** The pages fell in every run, each run's interval clear of zero. The settings the governor wrote an hour are counted over each run's measured windows (node-hours over the nodes in service), with no person touching either arm.

## Pages counted, not only minutes

A person is paid by the page, not by the minute. Counted from the same runs' raw files by the rule written before the count (a page opens on a bad minute and closes after five clean ones; `docs/OVERSIGHT_PAGES_PREREGISTRATION.md`), and only from runs whose recount gives their table's own alert minutes (111 of 111), the pages a person would have been sent went from 29.36 to 25.77 a repetition of every test together: **down 12.2%, GAIN by the mean of our three runs, beyond the noise in 2 of 3** (`results/OVERSIGHT_PAGES.md`). A page stays open about as long in both arms (minutes a page, native → Omni-Compass: 11.7 → 11.6 in run A; 13.3 → 13.3 in run B; 10.8 → 11.3 in run C): Omni-Compass sends fewer pages, not shorter ones. Every alert rule declared with it reads GAIN (4 of 6).

## The people line, through the one equation

The bill is the sum of its lines, B = Σₖ cₖ, and each line's change counts by its share of native's bill, b = Σₖ sₖ·bₖ (`docs/WORK_PER_BILL.md`). The people who watch and tune a stack are one line, k = people, with its share s(people) of the owner's bill. The receipts give that line's change only where the time spent moves with the pages; stated as the assumption it is: b(people) = the change in alert minutes. The line then moves the whole bill by s(people)·b(people), and it enters the benefit only through the bill: G = (1 + ΔW) / (1 + ΔB) − 1.

**Priced by what calls a person.** The people line itself is priced by time-driven activity-based costing (Kaplan and Anderson, *Harvard Business Review*, November 2004): P = w · Σⱼ Nⱼ · hⱼ + R, with Nⱼ the events a year of kind j (a page, a hand-made change of a setting, a capacity review), hⱼ the person-hours each takes (a page's whole cycle about six hours by Google's SRE book, chapter 11), w one person-hour fully loaded and R the fixed cost of an on-call rotation. The share of the bill saved on it is S(people) = κ · p · β · r: p the people's share of the run cost, β the share of their time that is answering pages and turning the knobs Omni-Compass governs (the SRE book holds on-call to at most 25% of an engineer's time), r the fall in what calls a person (the counted pages, or the minutes), κ the share of the freed time that becomes money (1 where a rotation or a head is released or the time goes to paid work, 0 where nothing changes). Only r is measured; p, β and κ are an owner's (`results/OVERSIGHT_PAGES.md` prints the product on a $100 million run cost for any of them).

**The example, not a result.** At the founder's example share, 7% of the bill (no receipt carries it; it plays the part the 2.9% plays in the $100 M example), the measured fall in pages moves the bill by 0.07 × (−11.0%) = **down 0.8% of the whole bill**: on the $100 M example, about $0.8 M a year of the people's time no longer spent answering pages, at native's cost. A larger share gives a larger line in proportion (10% gives down 1.1%); an owner's own share and its own count of pages replace both numbers.

## What is not claimed

- **Not a 20% (13% + 7%).** That sum is an outside reading on the remove list (`docs/WEBSITE_CLAIMS.md`): a "13%" set beside a 7% share of a bill. The 13% is no measured share of any bill (nearest to it in the record stood omni-v21's second reading of the index, a reading of work and speed on GitHub's machines that a later engine replaced); 7% is a share of a bill, not a gain. A reading and a share do not add, whatever the reading: on omni-v26 the Omni index reads 20.0% and its second reading 96.5% (`results/OMNI_INDEX.md`), neither of them a bill; the people line enters G only through ΔB, as above.
- **Not the people removed.** The record counts pages, not heads or salaries. An on-call rotation is staffed whether or not it is paged; what falls is the time the pages take, the triage and the hand tuning after them.
- **Not every page gone, and never nobody.** Pages fell in most tests and to none in some, not in all. A person keeps the kill switch (one hand, instant, security only), sets the response line and chooses the profile.

## Questions and answers

**Why do the benchmarks not show the engineering cost?** Because GitHub's machines run with nobody on call in either arm: there is no engineer's hour to count. The receipts count what would have called one, the alert minutes, and the settings the governor wrote itself.

**What does self-gauging mean here?** At every beat the governor reads the system's own meters, decides, writes a setting only through the plug, reads the write back and records its reason in its audit; it acts on the reading before the line is crossed, where a person acts after the page. In the tests above it wrote its settings on its own, the number in the table, with no person touching either arm.

**Could the real number be bigger?** It can. An owner's people share may be larger than 7%, and a stack carries many services, each with its own pages, where each test here reads one. It can also be smaller: the record measures pages, and how much of a person's time moves with them is the owner's to count.

**What holds the stack's health when nobody is watching?** The mechanism, not a person's reaction time: the governor reads every gauge every beat, which no person can, and moves before the line is crossed, inside each muscle's own limit. The alert minutes are the record of how long health was lost, and they are what fell.

**Does Omni-Compass replace the on-call engineer?** No. It takes pages away where its reading acts before the line; the person keeps the switch, the line and the profile.

**How does an owner measure it on its own stack?** Count the alert minutes with the same rule, native and with Omni-Compass on top, over the same load (the receipts' rule: a whole minute whose 95th percentile was over the line), and the time each page took from the on-call tool; s(people) is the owner's own payroll for that work over its bill.

Engines: the tables are omni-v26's, the newest engine whose Kubernetes tables have landed; every benchmark runs again on the engine that stands, and this page is written again from the records when they land (`python3 tools/oversight.py`).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
