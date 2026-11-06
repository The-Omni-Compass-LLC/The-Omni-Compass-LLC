# The pages a person would have been sent: native against Omni-Compass on native

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The oversight line's second reading, counted from the raw files of its own 43 tables (omni-v25) by the rule written and committed before the first count (`docs/OVERSIGHT_PAGES_PREREGISTRATION.md`). A person on call is paid by the page, not by the minute: a page wakes someone, is answered, mitigated and written up. The alert minutes say how long a page would be open; this page says how many pages there would be. Class L: real software on GitHub's own machines, measured; no person is on those machines, so no hour or salary is on any receipt.

## The rule and the check

A bad minute is the oversight line's alert minute exactly: a whole minute of the measured window whose 95th percentile response time (nearest rank, a failed request counted over the line) was over the line, 500 ms in every table. A page opens after FOR bad minutes in a row while no page is open, and closes after RESET clean minutes in a row. The primary rule is FOR 1 minute, RESET 5 minutes (Alertmanager's default `resolve_timeout`); every pair of FOR 1, 2 and 5 and RESET 5 and 15 is printed below, declared with it.

Before any page was counted, the bad minutes recounted from the raw files had to give each run's printed alert minutes and their 95% interval: **129 of 129 runs** do, and only those are read.

## The pages, test by test (the primary rule)

| Test | Run A: pages per repetition, native → Omni-Compass | Run B | Run C | The three runs, by the one key |
|---|---|---|---|---|
| All four in one run | 1.00 → 0.80, down 20.0% (#41751114338) | 1.00 → 0.70, down 30.0% (#41768859003) | 1.00 → 1.00, no change (#41780376170) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Armada on the group of two clusters under the batch stream, the four ways | 0.90 → 0.90, no change (#41828277526) | 0.90 → 1.00, up 11.1% (#41830587387) | 0.80 → 0.90, up 12.5% (#41830595635) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Armada on the group of two clusters under the batch stream, the four ways | 0.00 → 0.00, no page in either arm (#41828277526) | 0.00 → 0.00, no page in either arm (#41830587387) | 0.00 → 0.00, no page in either arm (#41830595635) | STEADY, the same |
| Batch queue | 1.00 → 1.00, no change (#41753030885) | 1.00 → 1.00, no change (#41768876462) | 1.00 → 1.00, no change (#41781968016) | STEADY, the same |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream | 0.90 → 1.20, up 33.3% (#41802308779) | 0.80 → 0.80, no change (#41802323140) | 0.90 → 0.90, no change (#41804425696) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways | 0.60 → 0.70, up 16.7% (#41810750964) | 0.80 → 1.00, up 25.0% (#41812549051) | 1.00 → 1.00, no change (#41814375146) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways | 0.50 → 0.60, up 20.0% (#41810750964) | 0.70 → 1.00, up 42.9% (#41812549051) | 1.00 → 1.00, no change (#41814375146) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| The cost to match | 0.50 → 0.00, down 100.0% (#41798197387) | 0.70 → 0.00, down 100.0% (#41798204788) | 0.50 → 0.00, down 100.0% (#41798211646) | GAIN in all three of our runs |
| Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways | 0.20 → 0.10, down 50.0% (#41816152588) | 0.30 → 0.00, down 100.0% (#41821621221) | 0.10 → 0.20, up 100.0% (#41828241662) | the runs disagree |
| Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways | 0.00 → 0.00, no page in either arm (#41816152588) | 0.00 → 0.10, up 0.10 pages from none (#41821621221) | 0.00 → 0.00, no page in either arm (#41828241662) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| CruiseKube | 0.00 → 0.00, no page in either arm (#41747200129) | 0.00 → 0.00, no page in either arm (#41765479982) | 0.00 → 0.00, no page in either arm (#41777088814) | STEADY, the same |
| CruiseKube | 0.00 → 0.00, no page in either arm (#42173265097) | 0.00 → 0.00, no page in either arm (#42173285642) | 0.00 → 0.00, no page in either arm (#42185619972) | STEADY, the same |
| Fairness | 1.00 → 1.00, no change (#41751121984) | 1.00 → 1.00, no change (#41768864707) | 1.00 → 1.00, no change (#41780381804) | STEADY, the same |
| Faults | 1.00 → 1.00, no change (#41753024820) | 1.00 → 1.00, no change (#41768870890) | 1.00 → 1.00, no change (#41781962156) | STEADY, the same |
| Faults, extended | 1.90 → 1.80, down 5.3% (#41792496184) | 2.20 → 1.90, down 13.6% (#41794354171) | 2.20 → 1.60, down 27.3% (#41796185630) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| The Gödel scheduler under the batch stream, the four ways | 1.00 → 1.20, up 20.0% (#41816164023) | 1.00 → 0.90, down 10.0% (#41823813742) | 0.90 → 0.90, no change (#41828251636) | the runs disagree |
| The Gödel scheduler under the batch stream, the four ways | 1.20 → 1.00, down 16.7% (#41816164023) | 0.90 → 0.80, down 11.1% (#41823813742) | 0.90 → 0.90, no change (#41828251636) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Goldilocks | 0.70 → 0.10, down 85.7% (#41749168920) | 0.60 → 0.00, down 100.0% (#41765485855) | 0.50 → 0.00, down 100.0% (#41777095500) | GAIN in all three of our runs |
| The KAI scheduler under the batch stream | 0.60 → 0.60, no change (#41800238758) | 0.70 → 0.80, up 14.3% (#41800247331) | 0.90 → 0.90, no change (#41800254736) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| The KAI scheduler under the batch stream, the four ways | 0.80 → 0.80, no change (#41809041712) | 0.90 → 1.00, up 11.1% (#41810759693) | 0.80 → 0.90, up 12.5% (#41812560443) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| The KAI scheduler under the batch stream, the four ways | 0.80 → 0.80, no change (#41809041712) | 0.80 → 0.90, up 12.5% (#41810759693) | 0.80 → 0.90, up 12.5% (#41812560443) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Karmada on the group of two clusters under the batch stream, the four ways | 0.70 → 1.00, up 42.9% (#41816173049) | 0.90 → 1.00, up 11.1% (#41823821537) | 0.90 → 0.90, no change (#41828260509) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Karmada on the group of two clusters under the batch stream, the four ways | 1.00 → 1.00, no change (#41816173049) | 1.00 → 1.00, no change (#41823821537) | 0.90 → 0.90, no change (#41828260509) | STEADY, the same |
| Kubernetes with KEDA on the CPU target and the live requests in flight | 0.10 → 0.00, down 100.0% (#41753044221) | 0.50 → 0.00, down 100.0% (#41770442526) | 0.40 → 0.00, down 100.0% (#41781979744) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| Kubernetes with KEDA's HTTP add-on on the live requests in flight | 0.80 → 0.80, no change (#41753044221) | 0.90 → 0.80, down 11.1% (#41770442526) | 0.90 → 0.80, down 11.1% (#41781979744) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Koordinator under the batch stream | 0.20 → 0.20, no change (#41800261877) | 0.00 → 0.00, no page in either arm (#41800269022) | 0.00 → 0.20, up 0.20 pages from none (#41802293120) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Koordinator under the batch stream, on the cgroup root its own tests use | 0.00 → 0.00, no page in either arm (#42173258848) | 0.10 → 0.10, no change (#42173278954) | 0.20 → 0.00, down 100.0% (#42185612749) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| KubeRay (the Ray autoscaler) under the batch stream, the four ways | 1.00 → 0.90, down 10.0% (#41816118654) | 0.80 → 0.90, up 12.5% (#41821612423) | 0.90 → 0.80, down 11.1% (#41828233886) | the runs disagree |
| KubeRay (the Ray autoscaler) under the batch stream, the four ways | 1.00 → 1.00, no change (#41816118654) | 1.00 → 1.00, no change (#41821612423) | 1.00 → 1.00, no change (#41828233886) | STEADY, the same |
| Kueue under the batch stream | 1.00 → 1.10, up 10.0% (#41762066634) | 0.80 → 1.00, up 25.0% (#41775363004) | 0.90 → 0.80, down 11.1% (#41788859873) | the runs disagree |
| Kueue under the batch stream, the four ways | 0.80 → 0.90, up 12.5% (#41809077335) | 0.80 → 0.80, no change (#41810798821) | 0.90 → 0.90, no change (#41812580198) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Kueue under the batch stream, the four ways | 0.80 → 0.80, no change (#41809077335) | 0.70 → 0.70, no change (#41810798821) | 1.00 → 0.90, down 10.0% (#41812580198) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Open Cluster Management on the group of two clusters under the batch stream, the four ways | 1.00 → 1.00, no change (#41816181570) | 0.70 → 0.80, up 14.3% (#41823829193) | 0.90 → 1.00, up 11.1% (#41828268372) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Open Cluster Management on the group of two clusters under the batch stream, the four ways | 0.90 → 1.00, up 11.1% (#41816181570) | 0.90 → 1.00, up 11.1% (#41823829193) | 1.00 → 1.00, no change (#41828268372) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Robustness: the governor killed mid-run | 1.00 → 1.00, no change (#41760298127) | 1.00 → 0.80, down 20.0% (#41775351685) | 1.00 → 1.00, no change (#41788847807) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Robustness: the two-hour run | 3.33 → 3.33, no change (#41762060399) | 1.00 → 1.00, no change (#41775357254) | 3.00 → 1.67, down 44.4% (#41788854067) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Steady load | 0.60 → 0.00, down 100.0% (#41751085804) | 0.80 → 0.00, down 100.0% (#41767220817) | 0.50 → 0.00, down 100.0% (#41778758086) | GAIN in all three of our runs |
| A public day of demand | 1.40 → 0.90, down 35.7% (#41753037941) | 1.50 → 1.60, up 6.7% (#41768881626) | 1.30 → 1.50, up 15.4% (#41781973989) | the runs disagree |
| The Kubernetes scheduler as shipped under the batch stream | 0.90 → 1.00, up 11.1% (#41802300531) | 1.10 → 1.10, no change (#41802315329) | 0.70 → 0.90, up 28.6% (#41804417539) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Volcano under the batch stream | 0.50 → 0.60, up 20.0% (#41762072500) | 0.70 → 0.60, down 14.3% (#41775368304) | 0.80 → 0.90, up 12.5% (#41790635305) | the runs disagree |
| Volcano under the batch stream, the four ways | 0.90 → 0.90, no change (#41809087487) | 0.70 → 0.80, up 14.3% (#41812541481) | 0.90 → 0.90, no change (#41814366715) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Volcano under the batch stream, the four ways | 0.80 → 0.80, no change (#41809087487) | 0.40 → 0.60, up 50.0% (#41812541481) | 0.80 → 0.80, no change (#41814366715) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Wandering demand | 1.00 → 1.10, up 10.0% (#41751107237) | 1.00 → 1.00, no change (#41768852229) | 1.00 → 0.90, down 10.0% (#41780370478) | the runs disagree |
| **All the tests together** (each test's pages per repetition summed) | 34.33 → 32.93, down 4.1% | 32.60 → 30.50, down 6.4% | 35.20 → 31.87, down 9.5% | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |

Together, the three runs' means: **34.04 → 31.77 pages**, down **6.7%** with Omni-Compass on native, read **GAIN by the mean of our three runs, beyond the noise in 2 of 3**. Fewer pages, not only shorter ones: the minutes a page stays open, native → Omni-Compass, 14.1 → 13.7 in run A, 15.4 → 15.1 in run B, 13.9 → 14.3 in run C; the alert minutes over the same runs, 485.0 → 451.7, 503.3 → 461.4, 490.5 → 456.3.

## Every rule declared with it

| Rule (FOR bad minutes to open, RESET clean minutes to close) | Run A, together | Run B | Run C | The three runs |
|---|---|---|---|---|
| FOR 1, RESET 5 (the primary) | 34.33 → 32.93, down 4.1% | 32.60 → 30.50, down 6.4% | 35.20 → 31.87, down 9.5% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 1, RESET 15 | 30.40 → 28.90, down 4.9% | 30.80 → 28.70, down 6.8% | 31.10 → 30.87, down 0.8% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 2, RESET 5 | 30.73 → 29.13, down 5.2% | 29.10 → 26.50, down 8.9% | 30.27 → 28.07, down 7.3% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 2, RESET 15 | 27.90 → 26.60, down 4.7% | 27.80 → 26.40, down 5.0% | 28.80 → 27.97, down 2.9% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 5, RESET 5 | 25.53 → 25.40, down 0.5% | 23.50 → 22.50, down 4.3% | 23.67 → 23.47, down 0.8% | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| FOR 5, RESET 15 | 23.00 → 23.40, up 1.7% | 23.00 → 22.50, down 2.2% | 23.27 → 23.47, up 0.9% | the runs disagree |

## How it enters the bill

The bill is the sum of its lines: C = M + P + O, with M the machines, P the people who run the stack and O the rest, held fixed. The people line is priced by time-driven activity-based costing (Kaplan and Anderson, *Harvard Business Review*, November 2004): P = w · Σⱼ Nⱼ · hⱼ + R, with Nⱼ the events a year of kind j (a page, a hand-made change of a setting, a capacity review), hⱼ the person-hours each takes (a page's whole cycle about 6 hours by Google's SRE book, chapter 11), w one person-hour fully loaded and R the fixed cost of an on-call rotation. Omni-Compass's share of the bill saved on the people line is S(people) = κ · p · β · r: p the people's share of the run cost, β the share of their time that is answering pages and turning the knobs Omni-Compass governs (the SRE book holds on-call to at most 25% of an engineer's time), r the fall in the events that call a person, κ the share of the freed time that becomes money (1 where a rotation or a head is released or the time goes to paid work, 0 where nothing changes). Only r is measured here; p, β and κ are an owner's. With the machines' line, the live page's one equation reads G = (1 + ΔW) ⁄ (1 + m · ΔM + p · ΔP) − 1, ΔP = −κ · β · r.

On a run cost of $100 million, κ = 1, r = 6.7% (the pages above, the change of the three runs' means) and, beside it, r = 7.4% (the alert minutes):

| People's share of the run cost, p | β = 25% (on-call time only) | β = 100% (every people hour) |
|---|---|---|
| 7% | $0.1 million (0.1%); by the minutes $0.1 million | $0.5 million (0.5%); by the minutes $0.5 million |
| 10% | $0.2 million (0.2%); by the minutes $0.2 million | $0.7 million (0.7%); by the minutes $0.7 million |
| 20% | $0.3 million (0.3%); by the minutes $0.4 million | $1.3 million (1.3%); by the minutes $1.5 million |

These are the arithmetic of a measured fall and an owner's own shares, not a measured saving: the people cost itself, in hours, is measured only in a paired pilot on an owner's own records, their pager history and their log of changes to the governed settings, before and with Omni-Compass on native (`docs/PILOT_PROTOCOL.md`). The machines' line is read on the chip and through the cloud (`results/TWO_BILLS.md`), and the two lines are never added as percentages of different bills: each enters the one equation with its own share.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
