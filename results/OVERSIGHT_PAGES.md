# The pages a person would have been sent: native against Omni-Compass on native

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The oversight line's second reading, counted from the raw files of its own 37 tables (omni-v26) by the rule written and committed before the first count (`docs/OVERSIGHT_PAGES_PREREGISTRATION.md`). A person on call is paid by the page, not by the minute: a page wakes someone, is answered, mitigated and written up. The alert minutes say how long a page would be open; this page says how many pages there would be. Class L: real software on GitHub's own machines, measured; no person is on those machines, so no hour or salary is on any receipt.

## The rule and the check

A bad minute is the oversight line's alert minute exactly: a whole minute of the measured window whose 95th percentile response time (nearest rank, a failed request counted over the line) was over the line, 500 ms in every table. A page opens after FOR bad minutes in a row while no page is open, and closes after RESET clean minutes in a row. The primary rule is FOR 1 minute, RESET 5 minutes (Alertmanager's default `resolve_timeout`); every pair of FOR 1, 2 and 5 and RESET 5 and 15 is printed below, declared with it.

Before any page was counted, the bad minutes recounted from the raw files had to give each run's printed alert minutes and their 95% interval: **111 of 111 runs** do, and only those are read.

## The pages, test by test (the primary rule)

| Test | Run A: pages per repetition, native → Omni-Compass | Run B | Run C | The three runs, by the one key |
|---|---|---|---|---|
| All four in one run | 1.20 → 0.90, down 25.0% (#42406258911) | 1.00 → 0.80, down 20.0% (#42415420145) | 1.00 → 0.70, down 30.0% (#42427795427) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Batch queue | 1.00 → 1.00, no change (#42407546216) | 1.00 → 1.00, no change (#42417953886) | 1.00 → 1.00, no change (#42427808988) | STEADY, the same |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream | 0.60 → 0.60, no change (#42439660401) | 0.90 → 0.90, no change (#42440706098) | 0.90 → 1.10, up 22.2% (#42440713360) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways | 0.80 → 0.60, down 25.0% (#42444100547) | 0.80 → 0.80, no change (#42445172518) | 0.50 → 0.40, down 20.0% (#42446289715) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways | 0.40 → 0.40, no change (#42444100547) | 0.90 → 0.80, down 11.1% (#42445172518) | 0.30 → 0.50, up 66.7% (#42446289715) | the runs disagree |
| The cost to match | 0.50 → 0.00, down 100.0% (#42437385663) | 0.70 → 0.00, down 100.0% (#42437389486) | 0.70 → 0.00, down 100.0% (#42437393561) | GAIN in all three of our runs |
| Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways | 0.00 → 0.10, up 0.10 pages from none (#42447367322) | 0.00 → 0.10, up 0.10 pages from none (#42450499095) | 0.20 → 0.10, down 50.0% (#42452540225) | the runs disagree |
| Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways | 0.30 → 0.10, down 66.7% (#42447367322) | 0.10 → 0.00, down 100.0% (#42450499095) | 0.10 → 0.00, down 100.0% (#42452540225) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| CruiseKube | 0.00 → 0.00, no page in either arm (#42403615734) | 0.00 → 0.00, no page in either arm (#42413970707) | 0.00 → 0.00, no page in either arm (#42425416413) | STEADY, the same |
| CruiseKube | 0.00 → 0.00, no page in either arm (#42436262163) | 0.00 → 0.00, no page in either arm (#42436265627) | 0.00 → 0.00, no page in either arm (#42437381465) | STEADY, the same |
| Fairness | 1.00 → 1.00, no change (#42406263563) | 1.00 → 1.00, no change (#42417945882) | 1.00 → 1.00, no change (#42427800113) | STEADY, the same |
| Faults | 1.00 → 1.00, no change (#42407542058) | 1.00 → 1.00, no change (#42417949915) | 1.00 → 1.00, no change (#42427804535) | STEADY, the same |
| Faults, extended | 1.60 → 1.60, no change (#42433917965) | 2.00 → 1.70, down 15.0% (#42435068170) | 2.20 → 2.00, down 9.1% (#42436258993) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| The Gödel scheduler under the batch stream, the four ways | 0.90 → 1.00, up 11.1% (#42447370557) | 1.00 → 1.00, no change (#42451531911) | 1.10 → 1.00, down 9.1% (#42452543740) | the runs disagree |
| The Gödel scheduler under the batch stream, the four ways | 0.90 → 0.80, down 11.1% (#42447370557) | 1.00 → 1.00, no change (#42451531911) | 0.90 → 1.00, up 11.1% (#42452543740) | the runs disagree |
| Goldilocks | 0.40 → 0.00, down 100.0% (#42404915439) | 0.50 → 0.00, down 100.0% (#42413975817) | 0.40 → 0.00, down 100.0% (#42425420205) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| The KAI scheduler under the batch stream | 0.80 → 0.80, no change (#42438540677) | 0.70 → 0.60, down 14.3% (#42438544638) | 0.80 → 0.80, no change (#42438548043) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| The KAI scheduler under the batch stream, the four ways | 0.50 → 0.90, up 80.0% (#42442968048) | 0.80 → 0.80, no change (#42444104246) | 0.80 → 0.80, no change (#42445176352) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| The KAI scheduler under the batch stream, the four ways | 0.50 → 0.50, no change (#42442968048) | 0.70 → 0.80, up 14.3% (#42444104246) | 0.70 → 0.70, no change (#42445176352) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Kubernetes with KEDA on the CPU target and the live requests in flight | 0.40 → 0.10, down 75.0% (#42407555127) | 0.30 → 0.00, down 100.0% (#42417962056) | 0.00 → 0.20, up 0.20 pages from none (#42427818792) | the runs disagree |
| Kubernetes with KEDA's HTTP add-on on the live requests in flight | 0.50 → 0.60, up 20.0% (#42407555127) | 0.70 → 0.30, down 57.1% (#42417962056) | 0.70 → 0.30, down 57.1% (#42427818792) | the runs disagree |
| Koordinator under the batch stream | 0.20 → 0.10, down 50.0% (#42438551739) | 0.10 → 0.00, down 100.0% (#42439648015) | 0.00 → 0.30, up 0.30 pages from none (#42439651965) | the runs disagree |
| Koordinator under the batch stream, on the cgroup root its own tests use | 0.00 → 0.50, up 0.50 pages from none (#42440716851) | 0.10 → 0.00, down 100.0% (#42441844056) | 0.00 → 0.50, up 0.50 pages from none (#42441848181) | the runs disagree |
| KubeRay (the Ray autoscaler) under the batch stream, the four ways | 0.70 → 0.70, no change (#42447364135) | 0.60 → 0.60, no change (#42450495106) | 0.60 → 0.60, no change (#42452536842) | STEADY, the same |
| KubeRay (the Ray autoscaler) under the batch stream, the four ways | 1.00 → 1.00, no change (#42447364135) | 1.00 → 1.00, no change (#42450495106) | 1.00 → 1.00, no change (#42452536842) | STEADY, the same |
| Kueue under the batch stream | 0.90 → 0.90, no change (#42412690276) | 1.10 → 1.10, no change (#42422950496) | 0.80 → 0.90, up 12.5% (#42432716761) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Kueue under the batch stream, the four ways | 1.00 → 1.00, no change (#42442976725) | 0.70 → 0.90, up 28.6% (#42445165273) | 0.50 → 0.50, no change (#42445184360) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Kueue under the batch stream, the four ways | 0.90 → 1.00, up 11.1% (#42442976725) | 0.80 → 0.70, down 12.5% (#42445165273) | 0.50 → 0.60, up 20.0% (#42445184360) | the runs disagree |
| Open Cluster Management on the group of two clusters under the batch stream, the four ways | 0.80 → 0.90, up 12.5% (#42447377308) | 0.80 → 0.90, up 12.5% (#42452533513) | 0.70 → 0.80, up 14.3% (#42453594917) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Open Cluster Management on the group of two clusters under the batch stream, the four ways | 0.90 → 1.00, up 11.1% (#42447377308) | 0.90 → 0.90, no change (#42452533513) | 0.70 → 0.80, up 14.3% (#42453594917) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Robustness: the governor killed mid-run | 1.00 → 0.90, down 10.0% (#42411433795) | 0.90 → 0.90, no change (#42421747995) | 0.90 → 0.70, down 22.2% (#42431521983) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Robustness: the two-hour run | 5.33 → 3.33, down 37.5% (#42411438422) | 3.33 → 3.33, no change (#42422946374) | 4.00 → 1.33, down 66.7% (#42432712342) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Steady load | 0.60 → 0.00, down 100.0% (#42406241542) | 0.80 → 0.00, down 100.0% (#42415400880) | 0.50 → 0.00, down 100.0% (#42426631088) | GAIN in all three of our runs |
| A public day of demand | 1.30 → 1.30, no change (#42407550879) | 1.30 → 0.90, down 30.8% (#42417958110) | 1.50 → 1.40, down 6.7% (#42427813944) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| The Kubernetes scheduler as shipped under the batch stream | 0.50 → 0.50, no change (#42439656396) | 0.80 → 0.80, no change (#42439664303) | 0.80 → 0.80, no change (#42440709856) | STEADY, the same |
| Volcano under the batch stream | 0.50 → 0.50, no change (#42412695021) | 0.30 → 0.40, up 33.3% (#42422954360) | 0.60 → 0.70, up 16.7% (#42432720979) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Wandering demand | 1.00 → 1.00, no change (#42406254590) | 1.00 → 1.20, up 20.0% (#42415415600) | 1.10 → 0.90, down 18.2% (#42426642847) | the runs disagree |
| **All the tests together** (each test's pages per repetition summed) | 29.93 → 26.63, down 11.0% | 29.63 → 26.23, down 11.5% | 28.50 → 24.43, down 14.3% | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |

Together, the three runs' means: **29.36 → 25.77 pages**, down **12.2%** with Omni-Compass on native, read **GAIN by the mean of our three runs, beyond the noise in 2 of 3**. Fewer pages, not only shorter ones: the minutes a page stays open, native → Omni-Compass, 11.7 → 11.6 in run A, 13.3 → 13.3 in run B, 10.8 → 11.3 in run C; the alert minutes over the same runs, 348.9 → 308.2, 394.0 → 349.9, 306.9 → 276.4.

## Every rule declared with it

| Rule (FOR bad minutes to open, RESET clean minutes to close) | Run A, together | Run B | Run C | The three runs |
|---|---|---|---|---|
| FOR 1, RESET 5 (the primary) | 29.93 → 26.63, down 11.0% | 29.63 → 26.23, down 11.5% | 28.50 → 24.43, down 14.3% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 1, RESET 15 | 24.43 → 22.80, down 6.7% | 25.30 → 22.80, down 9.9% | 23.87 → 22.53, down 5.6% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 2, RESET 5 | 25.83 → 22.80, down 11.7% | 25.93 → 24.23, down 6.6% | 22.50 → 19.03, down 15.4% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 2, RESET 15 | 22.23 → 20.27, down 8.8% | 22.80 → 21.60, down 5.3% | 20.30 → 18.83, down 7.2% | GAIN in all three of our runs |
| FOR 5, RESET 5 | 17.67 → 18.10, up 2.5% | 19.33 → 19.33, no change | 16.13 → 15.63, down 3.1% | the runs disagree |
| FOR 5, RESET 15 | 15.47 → 15.77, up 1.9% | 16.80 → 17.00, up 1.2% | 15.53 → 15.63, up 0.6% | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |

## How it enters the bill

The bill is the sum of its lines: C = M + P + O, with M the machines, P the people who run the stack and O the rest, held fixed. The people line is priced by time-driven activity-based costing (Kaplan and Anderson, *Harvard Business Review*, November 2004): P = w · Σⱼ Nⱼ · hⱼ + R, with Nⱼ the events a year of kind j (a page, a hand-made change of a setting, a capacity review), hⱼ the person-hours each takes (a page's whole cycle about 6 hours by Google's SRE book, chapter 11), w one person-hour fully loaded and R the fixed cost of an on-call rotation. Omni-Compass's share of the bill saved on the people line is S(people) = κ · p · β · r: p the people's share of the run cost, β the share of their time that is answering pages and turning the knobs Omni-Compass governs (the SRE book holds on-call to at most 25% of an engineer's time), r the fall in the events that call a person, κ the share of the freed time that becomes money (1 where a rotation or a head is released or the time goes to paid work, 0 where nothing changes). Only r is measured here; p, β and κ are an owner's. With the machines' line, the live page's one equation reads G = (1 + ΔW) ⁄ (1 + m · ΔM + p · ΔP) − 1, ΔP = −κ · β · r.

On a run cost of $100 million, κ = 1, r = 12.2% (the pages above, the change of the three runs' means) and, beside it, r = 11.0% (the alert minutes):

| People's share of the run cost, p | β = 25% (on-call time only) | β = 100% (every people hour) |
|---|---|---|
| 7% | $0.2 million (0.2%); by the minutes $0.2 million | $0.9 million (0.9%); by the minutes $0.8 million |
| 10% | $0.3 million (0.3%); by the minutes $0.3 million | $1.2 million (1.2%); by the minutes $1.1 million |
| 20% | $0.6 million (0.6%); by the minutes $0.5 million | $2.4 million (2.4%); by the minutes $2.2 million |

These are the arithmetic of a measured fall and an owner's own shares, not a measured saving: the people cost itself, in hours, is measured only in a paired pilot on an owner's own records, their pager history and their log of changes to the governed settings, before and with Omni-Compass on native (`docs/PILOT_PROTOCOL.md`). The machines' line is read on the chip and through the cloud (`results/TWO_BILLS.md`), and the two lines are never added as percentages of different bills: each enters the one equation with its own share.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
