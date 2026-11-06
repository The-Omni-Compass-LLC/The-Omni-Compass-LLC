# The Oversight Line: the Pages a Person Would Answer, Native Against Omni-Compass on Native

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> "They don't need a 3 a.m. call and they don't need [anyone] to turn knobs when OmniCompass is ... self-gauging" (the founder, 3 November 2026)

## What GitHub's runs measure, and what they cannot

Every benchmark runs on GitHub's own machines with nobody watching, in both arms: no person is on call, no person turns a knob, so no engineer's hour and no salary is on any receipt, and none can be. What every real Kubernetes receipt does measure is the event that calls a person: an **alert minute**, a whole minute of the measured window whose 95th percentile response time, failed requests counted over, was over the response line, the minute an on-call page would be open (`tools/live_reps.py`, `babysitting`; judged, fewer is GAIN). Beside it each receipt shows the settings the governor wrote on its own, each in its audit with its reason and read back (shown, not judged: native's own autoscaler runs untouched in both arms).

## The pages, test by test (omni-v25, every real Kubernetes three-run table that carries them)

| Test | Alert minutes a repetition, native → Omni-Compass on native (mean of the three runs) | Change | Reading (the table's own, the one key) | Settings the governor wrote on its own, a repetition | Record |
|---|---|---|---|---|---|
| All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back) | 27.40 → 22.40 | down 18.2% | GAIN in all three of our runs | 52.9 | `results/live/V25_ALL_FOUR.json` |
| Armada on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 94) | 13.00 → 14.47 | up 11.3% | LOSS in all three of our runs | 126.2 | `results/live/V25_ARMADA_4W_BARE.json` |
| Armada on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Armada against Armada as shipped (register row 94) | 0.00 → 0.00 | none in either arm | STEADY, the same | 33.3 | `results/live/V25_ARMADA_4W_TOP.json` |
| Batch queue: 240 CPU jobs and cruise | 11.13 → 11.30 | up 1.5% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 9.8 | `results/live/V25_BATCH.json` |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream: Omni-Compass on top (register row 88) | 11.80 → 12.03 | up 2.0% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 69.5 | `results/live/V25_BINPACK.json` |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 88) | 9.90 → 10.47 | up 5.7% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 107.2 | `results/live/V25_BINPACK_4W_BARE.json` |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways: Omni-Compass on top of the bin-packing profile against the bin-packing profile as shipped (register row 88) | 9.13 → 9.77 | up 6.9% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 88.4 | `results/live/V25_BINPACK_4W_TOP.json` |
| The cost to match: native, native tuned harder by its operator (HPA target 40, 30, 20) and native with Omni-Compass on top; this table: Omni-Compass on top against native | 2.07 → 0.00 | down 100.0% | GAIN in all three of our runs | 18.7 | `results/live/V25_COST_TO_MATCH.json` |
| Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 90) | 0.27 → 0.10 | down 62.5% | the runs disagree | 6.6 | `results/live/V25_CRANE_4W_BARE.json` |
| Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways: Omni-Compass on top of Crane against Crane as shipped (register row 90) | 0.00 → 0.03 | — | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 6.3 | `results/live/V25_CRANE_4W_TOP.json` |
| CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations | 0.00 → 0.00 | none in either arm | STEADY, the same | 4.0 | `results/live/V25_CRUISEKUBE.json` |
| Fairness: a noisy neighbour on the same workers | 8.77 → 8.33 | down 4.9% | GAIN by the mean of our three runs, beyond the noise in 0 of 3 | 127.9 | `results/live/V25_FAIRNESS.json` |
| Faults: a machine down, a spike, a runaway pod, a blind probe | 6.73 → 5.63 | down 16.3% | GAIN by the mean of our three runs, beyond the noise in 1 of 3 | 47.6 | `results/live/V25_FAULTS.json` |
| Faults, extended: the four faults and the two that blind a governor (the API server frozen 30 s, the metrics server gone two minutes) in a 2,500 s window | 9.40 → 7.07 | down 24.8% | GAIN in all three of our runs | 64.3 | `results/live/V25_FAULTS_EXTENDED.json` |
| The Gödel scheduler under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 93) | 10.30 → 10.57 | up 2.6% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 26.6 | `results/live/V25_GODEL_4W_BARE.json` |
| The Gödel scheduler under the batch stream, the four ways: Omni-Compass on top of Gödel against Gödel as shipped (register row 93) | 10.00 → 10.27 | up 2.7% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 27.2 | `results/live/V25_GODEL_4W_TOP.json` |
| Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender | 1.47 → 0.03 | down 97.7% | GAIN in all three of our runs | 464.2 | `results/live/V25_GOLDILOCKS.json` |
| The KAI scheduler under the batch stream: Omni-Compass on top of KAI's queues (register row 91) | 10.53 → 11.17 | up 6.0% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 82.3 | `results/live/V25_KAI.json` |
| The KAI scheduler under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 91) | 10.27 → 10.90 | up 6.2% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 109.3 | `results/live/V25_KAI_4W_BARE.json` |
| The KAI scheduler under the batch stream, the four ways: Omni-Compass on top of KAI against KAI as shipped (register row 91) | 11.23 → 12.03 | up 7.1% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 74.2 | `results/live/V25_KAI_4W_TOP.json` |
| Karmada on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 95) | 12.83 → 14.90 | up 16.1% | LOSS in all three of our runs | 114.1 | `results/live/V25_KARMADA_4W_BARE.json` |
| Karmada on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Karmada against Karmada as shipped (register row 95) | 16.33 → 17.63 | up 8.0% | LOSS in all three of our runs | 73.5 | `results/live/V25_KARMADA_4W_TOP.json` |
| Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top | 0.37 → 0.00 | down 100.0% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 | 452.9 | `results/live/V25_KEDA_CPU_REQUESTS.json` |
| Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top | 5.17 → 1.77 | down 65.8% | GAIN in all three of our runs | 87.6 | `results/live/V25_KEDA_REQUESTS.json` |
| Koordinator under the batch stream: Omni-Compass on top of its colocation (register row 89) | 0.07 → 0.13 | up 100.0% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 112.5 | `results/live/V25_KOORDINATOR.json` |
| KubeRay (the Ray autoscaler) under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 92) | 9.70 → 10.03 | up 3.4% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 112.4 | `results/live/V25_KUBERAY_4W_BARE.json` |
| KubeRay (the Ray autoscaler) under the batch stream, the four ways: Omni-Compass on top of KubeRay against KubeRay as shipped (register row 92) | 23.97 → 23.90 | down 0.3% | STEADY, under the floor (the three runs' mean 0.26%) | 32.4 | `results/live/V25_KUBERAY_4W_TOP.json` |
| Kueue under the batch stream: Omni-Compass on top of Kueue's admission (register row 63) | 10.90 → 11.63 | up 6.7% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 97.5 | `results/live/V25_KUEUE.json` |
| Kueue under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 63) | 10.30 → 10.93 | up 6.1% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 107.2 | `results/live/V25_KUEUE_4W_BARE.json` |
| Kueue under the batch stream, the four ways: Omni-Compass on top of Kueue against Kueue as shipped (register row 63) | 10.30 → 10.97 | up 6.5% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 112.3 | `results/live/V25_KUEUE_4W_TOP.json` |
| Open Cluster Management on the group of two clusters under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 96) | 11.63 → 13.53 | up 16.3% | LOSS by the mean of our three runs, beyond the noise in 2 of 3 | 144.3 | `results/live/V25_OCM_4W_BARE.json` |
| Open Cluster Management on the group of two clusters under the batch stream, the four ways: Omni-Compass on top of Open Cluster Management against Open Cluster Management as shipped (register row 96) | 14.73 → 17.37 | up 17.9% | LOSS in all three of our runs | 98.9 | `results/live/V25_OCM_4W_TOP.json` |
| Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs | 10.47 → 8.43 | down 19.4% | GAIN in all three of our runs | 76.1 | `results/live/V25_ROBUST_KILL.json` |
| Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched | 100.89 → 85.67 | down 15.1% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 | 137.2 | `results/live/V25_ROBUST_LONG.json` |
| Steady load: the same fixed-rate work sent to both arms | 2.03 → 0.00 | down 100.0% | GAIN in all three of our runs | 19.3 | `results/live/V25_STEADY.json` |
| A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4) | 21.97 → 8.77 | down 60.1% | GAIN in all three of our runs | 72.6 | `results/live/V25_TRACE_GOOGLE2011.json` |
| The Kubernetes scheduler as shipped under the batch stream: Omni-Compass on top of the default scheduler alone (register row 88) | 10.07 → 10.63 | up 5.6% | LOSS by the mean of our three runs, beyond the noise in 1 of 3 | 107.4 | `results/live/V25_VANILLA.json` |
| Volcano under the batch stream: Omni-Compass on top of Volcano's queues (register row 63) | 8.70 → 9.10 | up 4.6% | the runs disagree | 106.9 | `results/live/V25_VOLCANO.json` |
| Volcano under the batch stream, the four ways: Omni-Compass on the organism alone against the organism alone (register row 63) | 9.67 → 10.10 | up 4.5% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 109.2 | `results/live/V25_VOLCANO_4W_BARE.json` |
| Volcano under the batch stream, the four ways: Omni-Compass on top of Volcano against Volcano as shipped (register row 63) | 8.33 → 8.70 | up 4.4% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 | 107.8 | `results/live/V25_VOLCANO_4W_TOP.json` |
| Wandering demand: load that steps up and down by one (1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1) | 31.03 → 25.63 | down 17.4% | GAIN in all three of our runs | 51.8 | `results/live/V25_WANDERING.json` |

**Together.** Over the 41 tests the pages a repetition add up to 492.9 alert minutes on native and 456.4 with Omni-Compass on top: **down 7.4%** (our arithmetic over the tables, each test weighed by its own minutes; the two-hour test holds 20% of native's). Fewer pages in 15 of the 41 tests, to none at all in 3, the same in 2, more in 24. Each test's word is its own table's, by the one key.

**Run by run.** The tables summed in each of our three runs (one repetition of every test, native beside Omni-Compass on native); each difference's 95% interval adds its tables' variances, each from that table's own interval and repetitions.

| Run | Alert minutes, native → Omni-Compass on native, summed | Change | Difference, 95% interval (minutes) | Settings the governor wrote on its own, an hour |
|---|---|---|---|---|
| A | 485.03 → 451.67 | down 6.9% | −33.37 (−44.79 to −21.94) | 218 |
| B | 503.20 → 461.27 | down 8.3% | −41.93 (−49.68 to −34.19) | 218 |
| C | 490.33 → 456.27 | down 6.9% | −34.07 (−43.72 to −24.41) | 205 |

**Read by the one key: GAIN in all three of our runs.** The pages fell in every run, each run's interval clear of zero. The settings the governor wrote an hour are counted over each run's measured windows (node-hours over the nodes in service), with no person touching either arm.

## Pages counted, not only minutes

The pages a person would have been sent are counted from the raw files of omni-v21's tables (`results/OVERSIGHT_PAGES.md`, that engine's own record); these minutes are omni-v25's, and two engines are never read together, so the count of pages on omni-v25's runs comes next and is not printed here before it is made.

## The people line, through the one equation

The bill is the sum of its lines, B = Σₖ cₖ, and each line's change counts by its share of native's bill, b = Σₖ sₖ·bₖ (`docs/WORK_PER_BILL.md`). The people who watch and tune a stack are one line, k = people, with its share s(people) of the owner's bill. The receipts give that line's change only where the time spent moves with the pages; stated as the assumption it is: b(people) = the change in alert minutes. The line then moves the whole bill by s(people)·b(people), and it enters the benefit only through the bill: G = (1 + ΔW) / (1 + ΔB) − 1.

**Priced by what calls a person.** The people line itself is priced by time-driven activity-based costing (Kaplan and Anderson, *Harvard Business Review*, November 2004): P = w · Σⱼ Nⱼ · hⱼ + R, with Nⱼ the events a year of kind j (a page, a hand-made change of a setting, a capacity review), hⱼ the person-hours each takes (a page's whole cycle about six hours by Google's SRE book, chapter 11), w one person-hour fully loaded and R the fixed cost of an on-call rotation. The share of the bill saved on it is S(people) = κ · p · β · r: p the people's share of the run cost, β the share of their time that is answering pages and turning the knobs Omni-Compass governs (the SRE book holds on-call to at most 25% of an engineer's time), r the fall in what calls a person (the counted pages, or the minutes), κ the share of the freed time that becomes money (1 where a rotation or a head is released or the time goes to paid work, 0 where nothing changes). Only r is measured; p, β and κ are an owner's (`results/OVERSIGHT_PAGES.md` prints the product on a $100 million run cost for any of them).

**The example, not a result.** At the founder's example share, 7% of the bill (no receipt carries it; it plays the part the 2.9% plays in the $100 M example), the measured fall in pages moves the bill by 0.07 × (−7.4%) = **down 0.5% of the whole bill**: on the $100 M example, about $0.5 M a year of the people's time no longer spent answering pages, at native's cost. A larger share gives a larger line in proportion (10% gives down 0.7%); an owner's own share and its own count of pages replace both numbers.

## What is not claimed

- **Not a 20% (13% + 7%).** That sum is an outside reading on the remove list (`docs/WEBSITE_CLAIMS.md`): a "13%" set beside a 7% share of a bill. The 13% is no measured share of any bill (nearest to it in the record stood omni-v21's second reading of the index, a reading of work and speed on GitHub's machines that a later engine replaced); 7% is a share of a bill, not a gain. A reading and a share do not add, whatever the reading: on omni-v25 the Omni index reads 20.4% and its second reading 94.0% (`results/OMNI_INDEX.md`), neither of them a bill; the people line enters G only through ΔB, as above.
- **Not the people removed.** The record counts pages, not heads or salaries. An on-call rotation is staffed whether or not it is paged; what falls is the time the pages take, the triage and the hand tuning after them.
- **Not every page gone, and never nobody.** Pages fell in most tests and to none in some, not in all. A person keeps the kill switch (one hand, instant, security only), sets the response line and chooses the profile.

## Questions and answers

**Why do the benchmarks not show the engineering cost?** Because GitHub's machines run with nobody on call in either arm: there is no engineer's hour to count. The receipts count what would have called one, the alert minutes, and the settings the governor wrote itself.

**What does self-gauging mean here?** At every beat the governor reads the system's own meters, decides, writes a setting only through the plug, reads the write back and records its reason in its audit; it acts on the reading before the line is crossed, where a person acts after the page. In the tests above it wrote its settings on its own, the number in the table, with no person touching either arm.

**Could the real number be bigger?** It can. An owner's people share may be larger than 7%, and a stack carries many services, each with its own pages, where each test here reads one. It can also be smaller: the record measures pages, and how much of a person's time moves with them is the owner's to count.

**What holds the stack's health when nobody is watching?** The mechanism, not a person's reaction time: the governor reads every gauge every beat, which no person can, and moves before the line is crossed, inside each muscle's own limit. The alert minutes are the record of how long health was lost, and they are what fell.

**Does Omni-Compass replace the on-call engineer?** No. It takes pages away where its reading acts before the line; the person keeps the switch, the line and the profile.

**How does an owner measure it on its own stack?** Count the alert minutes with the same rule, native and with Omni-Compass on top, over the same load (the receipts' rule: a whole minute whose 95th percentile was over the line), and the time each page took from the on-call tool; s(people) is the owner's own payroll for that work over its bill.

Engines: the tables are omni-v25's, the newest engine whose Kubernetes tables have landed; every benchmark runs again on the engine that stands, and this page is written again from the records when they land (`python3 tools/oversight.py`).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
