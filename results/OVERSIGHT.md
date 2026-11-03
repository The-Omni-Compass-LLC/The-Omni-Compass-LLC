# The Oversight Line: the Pages a Person Would Answer, Native Against Omni-Compass on Native

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> "They don't need a 3 a.m. call and they don't need [anyone] to turn knobs when OmniCompass is ... self-gauging" (the founder, 3 November 2026)

## What GitHub's runs measure, and what they cannot

Every benchmark runs on GitHub's own machines with nobody watching, in both arms: no person is on call, no person turns a knob, so no engineer's hour and no salary is on any receipt, and none can be. What every real Kubernetes receipt does measure is the event that calls a person: an **alert minute**, a whole minute of the measured window whose 95th percentile response time, failed requests counted over, was over the response line, the minute an on-call page would be open (`tools/live_reps.py`, `babysitting`; judged, fewer is GAIN). Beside it each receipt shows the settings the governor wrote on its own, each in its audit with its reason and read back (shown, not judged: native's own autoscaler runs untouched in both arms).

## The pages, test by test (omni-v21, every real Kubernetes three-run table that carries them)

| Test | Alert minutes a repetition, native → Omni-Compass on native (mean of the three runs) | Change | Reading (the table's own, the one key) | Settings the governor wrote on its own, a repetition | Record |
|---|---|---|---|---|---|
| All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back) | 26.53 → 21.27 | down 19.8% | GAIN in all three of our runs | 34.7 | `results/live/V21_ALL_FOUR.json` |
| Batch queue: 240 CPU jobs and cruise | 9.27 → 9.27 | the same | the runs disagree | 12.7 | `results/live/V21_BATCH.json` |
| CruiseKube: Omni-Compass on top of a service rightsized by CruiseKube applying its own recommendations | 0.00 → 0.00 | none in either arm | STEADY, the same | 0.0 | `results/live/V21_CRUISEKUBE.json` |
| Fairness: a noisy neighbour on the same workers | 8.87 → 8.50 | down 4.1% | GAIN by the mean of our three runs, beyond the noise in 1 of 3 | 46.6 | `results/live/V21_FAIRNESS.json` |
| Faults: a machine down, a spike, a runaway pod, a blind probe | 6.67 → 5.33 | down 20.0% | GAIN in all three of our runs | 27.9 | `results/live/V21_FAULTS.json` |
| Goldilocks: Omni-Compass on top of a service rightsized with Goldilocks and the VPA's recommender | 0.77 → 0.00 | down 100.0% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 | 38.0 | `results/live/V21_GOLDILOCKS.json` |
| Kubernetes with KEDA on the CPU target and the live requests in flight: Omni-Compass on top | 0.20 → 0.00 | down 100.0% | GAIN by the mean of our three runs, beyond the noise in 0 of 3 | 33.3 | `results/live/V21_KEDA_CPU_REQUESTS.json` |
| Kubernetes with KEDA's HTTP add-on on the live requests in flight: Omni-Compass on top | 4.40 → 0.13 | down 97.0% | GAIN in all three of our runs | 5.2 | `results/live/V21_KEDA_REQUESTS.json` |
| Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs | 10.63 → 8.47 | down 20.4% | GAIN in all three of our runs | 47.5 | `results/live/V21_ROBUST_KILL.json` |
| Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched | 78.22 → 59.11 | down 24.4% | GAIN by the mean of our three runs, beyond the noise in 1 of 3 | 152.3 | `results/live/V21_ROBUST_LONG.json` |
| Steady load: the same fixed-rate work sent to both arms | 2.00 → 0.00 | down 100.0% | GAIN in all three of our runs | 15.9 | `results/live/V21_STEADY.json` |
| A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4) | 21.00 → 7.03 | down 66.5% | GAIN in all three of our runs | 51.4 | `results/live/V21_TRACE_GOOGLE2011.json` |
| Wandering demand: load that steps up and down by one (1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1) | 27.27 → 20.17 | down 26.0% | GAIN in all three of our runs | 37.4 | `results/live/V21_WANDERING.json` |

**Together.** Over the 13 tests the pages a repetition add up to 195.8 alert minutes on native and 139.3 with Omni-Compass on top: **down 28.9%** (our arithmetic over the tables, each test weighed by its own minutes; the two-hour test holds 40% of native's). Fewer pages in 11 of the 13 tests, to none at all in 3, the same in 2, more in 0. Each test's word is its own table's, by the one key.

## The people line, through the one equation

The bill is the sum of its lines, B = Σₖ cₖ, and each line's change counts by its share of native's bill, b = Σₖ sₖ·bₖ (`docs/WORK_PER_BILL.md`). The people who watch and tune a stack are one line, k = people, with its share s(people) of the owner's bill. The receipts give that line's change only where the time spent moves with the pages; stated as the assumption it is: b(people) = the change in alert minutes. The line then moves the whole bill by s(people)·b(people), and it enters the benefit only through the bill: G = (1 + ΔW) / (1 + ΔB) − 1.

**The example, not a result.** At the founder's example share, 7% of the bill (no receipt carries it; it plays the part the 2.9% plays in the $100 M example), the measured fall in pages moves the bill by 0.07 × (−28.9%) = **down 2.0% of the whole bill**: on the $100 M example, about $2.0 M a year of the people's time no longer spent answering pages, at native's cost. A larger share gives a larger line in proportion (10% gives down 2.9%); an owner's own share and its own count of pages replace both numbers.

## What is not claimed

- **Not a 20% (13% + 7%).** The 12.9% is the software end's second reading of the Omni index (work and speed, on GitHub's machines), not a bill; 7% is a share of a bill, not a gain. A reading and a share do not add; the people line enters G only through ΔB, as above.
- **Not the people removed.** The record counts pages, not heads or salaries. An on-call rotation is staffed whether or not it is paged; what falls is the time the pages take, the triage and the hand tuning after them.
- **Not every page gone, and never nobody.** Pages fell in most tests and to none in some, not in all. A person keeps the kill switch (one hand, instant, security only), sets the response line and chooses the profile.

## Questions and answers

**Why do the benchmarks not show the engineering cost?** Because GitHub's machines run with nobody on call in either arm: there is no engineer's hour to count. The receipts count what would have called one, the alert minutes, and the settings the governor wrote itself.

**What does self-gauging mean here?** At every beat the governor reads the system's own meters, decides, writes a setting only through the plug, reads the write back and records its reason in its audit; it acts on the reading before the line is crossed, where a person acts after the page. In the tests above it wrote its settings on its own, the number in the table, with no person touching either arm.

**Could the real number be bigger?** It can. An owner's people share may be larger than 7%, and a stack carries many services, each with its own pages, where each test here reads one. It can also be smaller: the record measures pages, and how much of a person's time moves with them is the owner's to count.

**Does Omni-Compass replace the on-call engineer?** No. It takes pages away where its reading acts before the line; the person keeps the switch, the line and the profile.

**How does an owner measure it on its own stack?** Count the alert minutes with the same rule, native and with Omni-Compass on top, over the same load (the receipts' rule: a whole minute whose 95th percentile was over the line), and the time each page took from the on-call tool; s(people) is the owner's own payroll for that work over its bill.

Engines: the tables are omni-v21's, the newest engine whose Kubernetes tables have landed; every benchmark runs again on the engine that stands, and this page is written again from the records when they land (`python3 tools/oversight.py`).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
