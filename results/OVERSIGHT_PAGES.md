# The pages a person would have been sent: native against Omni-Compass on native

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The oversight line's second reading, counted from the raw files of its own 13 tables (omni-v21) by the rule written and committed before the first count (`docs/OVERSIGHT_PAGES_PREREGISTRATION.md`). A person on call is paid by the page, not by the minute: a page wakes someone, is answered, mitigated and written up. The alert minutes say how long a page would be open; this page says how many pages there would be. Class L: real software on GitHub's own machines, measured; no person is on those machines, so no hour or salary is on any receipt.

## The rule and the check

A bad minute is the oversight line's alert minute exactly: a whole minute of the measured window whose 95th percentile response time (nearest rank, a failed request counted over the line) was over the line, 500 ms in every table. A page opens after FOR bad minutes in a row while no page is open, and closes after RESET clean minutes in a row. The primary rule is FOR 1 minute, RESET 5 minutes (Alertmanager's default `resolve_timeout`); every pair of FOR 1, 2 and 5 and RESET 5 and 15 is printed below, declared with it.

Before any page was counted, the bad minutes recounted from the raw files had to give each run's printed alert minutes and their 95% interval: **39 of 39 runs** do, and only those are read.

## The pages, test by test (the primary rule)

| Test | Run A: pages per repetition, native → Omni-Compass | Run B | Run C | The three runs, by the one key |
|---|---|---|---|---|
| All four in one run | 1.00 → 0.60, down 40.0% (#40227146512) | 1.00 → 0.90, down 10.0% (#40250382783) | 1.00 → 0.80, down 20.0% (#40272629580) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| Batch queue | 1.00 → 1.00, no change (#40230821800) | 1.00 → 1.00, no change (#40251625381) | 1.00 → 1.00, no change (#40274018452) | STEADY, the same |
| CruiseKube | 0.00 → 0.00, no page in either arm (#40220956277) | 0.00 → 0.00, no page in either arm (#40245486755) | 0.00 → 0.00, no page in either arm (#40267226299) | STEADY, the same |
| Fairness | 1.00 → 1.00, no change (#40227151053) | 1.00 → 1.00, no change (#40250387280) | 1.00 → 1.00, no change (#40272634568) | STEADY, the same |
| Faults | 1.00 → 1.00, no change (#40229598467) | 1.00 → 1.00, no change (#40250391552) | 1.00 → 1.00, no change (#40272639170) | STEADY, the same |
| Goldilocks | 0.60 → 0.00, down 100.0% (#40222183655) | 0.10 → 0.00, down 100.0% (#40245490699) | 0.60 → 0.00, down 100.0% (#40267231266) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| Kubernetes with KEDA on the CPU target and the live requests in flight | 0.20 → 0.00, down 100.0% (#40232040937) | 0.10 → 0.00, down 100.0% (#40254201062) | 0.30 → 0.00, down 100.0% (#40276902708) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Kubernetes with KEDA's HTTP add-on on the live requests in flight | 0.90 → 0.10, down 88.9% (#40232040937) | 0.80 → 0.20, down 75.0% (#40254201062) | 0.70 → 0.00, down 100.0% (#40276902708) | GAIN in all three of our runs |
| Robustness: the governor killed mid-run | 1.00 → 0.90, down 10.0% (#40240618830) | 1.00 → 0.90, down 10.0% (#40261931876) | 0.90 → 0.80, down 11.1% (#40286252440) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Robustness: the two-hour run | 4.33 → 3.33, down 23.1% (#40240697625) | 3.33 → 3.33, no change (#40261936964) | 5.33 → 3.67, down 31.3% (#40286258686) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Steady load | 0.50 → 0.00, down 100.0% (#40223431219) | 0.50 → 0.00, down 100.0% (#40246652453) | 0.60 → 0.00, down 100.0% (#40269968227) | GAIN in all three of our runs |
| A public day of demand | 1.50 → 1.30, down 13.3% (#40232036723) | 1.30 → 1.00, down 23.1% (#40252903510) | 1.80 → 1.50, down 16.7% (#40275448206) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Wandering demand | 1.10 → 0.80, down 27.3% (#40227141899) | 1.00 → 0.90, down 10.0% (#40250378687) | 1.00 → 0.80, down 20.0% (#40271292066) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| **All the tests together** (each test's pages per repetition summed) | 14.13 → 10.03, down 29.0% | 12.13 → 10.23, down 15.7% | 15.23 → 10.57, down 30.6% | **GAIN in all three of our runs** |

Together, the three runs' means: **13.83 → 10.28 pages**, down **25.7%** with Omni-Compass on native, read **GAIN in all three of our runs**. Fewer pages, not only shorter ones: the minutes a page stays open, native → Omni-Compass, 12.9 → 12.7 in run A, 17.6 → 15.3 in run B, 12.6 → 12.6 in run C; the alert minutes over the same runs, 182.1 → 127.6, 213.2 → 156.6, 192.2 → 133.7.

## Every rule declared with it

| Rule (FOR bad minutes to open, RESET clean minutes to close) | Run A, together | Run B | Run C | The three runs |
|---|---|---|---|---|
| FOR 1, RESET 5 (the primary) | 14.13 → 10.03, down 29.0% | 12.13 → 10.23, down 15.7% | 15.23 → 10.57, down 30.6% | GAIN in all three of our runs |
| FOR 1, RESET 15 | 10.53 → 7.70, down 26.9% | 9.50 → 7.60, down 20.0% | 10.63 → 8.13, down 23.5% | GAIN in all three of our runs |
| FOR 2, RESET 5 | 11.83 → 9.30, down 21.4% | 11.63 → 9.33, down 19.8% | 12.17 → 9.10, down 25.2% | GAIN in all three of our runs |
| FOR 2, RESET 15 | 9.10 → 6.97, down 23.4% | 9.10 → 7.00, down 23.1% | 9.00 → 6.77, down 24.8% | GAIN in all three of our runs |
| FOR 5, RESET 5 | 9.50 → 7.33, down 22.8% | 9.73 → 5.57, down 42.8% | 8.90 → 6.47, down 27.3% | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| FOR 5, RESET 15 | 6.77 → 5.67, down 16.3% | 7.20 → 5.57, down 22.7% | 6.17 → 5.47, down 11.4% | GAIN in all three of our runs |

## How it enters the bill

The bill is the sum of its lines: C = M + P + O, with M the machines, P the people who run the stack and O the rest, held fixed. The people line is priced by time-driven activity-based costing (Kaplan and Anderson, *Harvard Business Review*, November 2004): P = w · Σⱼ Nⱼ · hⱼ + R, with Nⱼ the events a year of kind j (a page, a hand-made change of a setting, a capacity review), hⱼ the person-hours each takes (a page's whole cycle about 6 hours by Google's SRE book, chapter 11), w one person-hour fully loaded and R the fixed cost of an on-call rotation. Omni-Compass's share of the bill saved on the people line is S(people) = κ · p · β · r: p the people's share of the run cost, β the share of their time that is answering pages and turning the knobs Omni-Compass governs (the SRE book holds on-call to at most 25% of an engineer's time), r the fall in the events that call a person, κ the share of the freed time that becomes money (1 where a rotation or a head is released or the time goes to paid work, 0 where nothing changes). Only r is measured here; p, β and κ are an owner's. With the machines' line, the live page's one equation reads G = (1 + ΔW) ⁄ (1 + m · ΔM + p · ΔP) − 1, ΔP = −κ · β · r.

On a run cost of $100 million, κ = 1, r = 25.7% (the pages above, the change of the three runs' means) and, beside it, r = 28.9% (the alert minutes):

| People's share of the run cost, p | β = 25% (on-call time only) | β = 100% (every people hour) |
|---|---|---|
| 7% | $0.4 million (0.4%); by the minutes $0.5 million | $1.8 million (1.8%); by the minutes $2.0 million |
| 10% | $0.6 million (0.6%); by the minutes $0.7 million | $2.6 million (2.6%); by the minutes $2.9 million |
| 20% | $1.3 million (1.3%); by the minutes $1.4 million | $5.1 million (5.1%); by the minutes $5.8 million |

These are the arithmetic of a measured fall and an owner's own shares, not a measured saving: the people cost itself, in hours, is measured only in a paired pilot on an owner's own records, their pager history and their log of changes to the governed settings, before and with Omni-Compass on native (`docs/PILOT_PROTOCOL.md`). The machines' line is read on the chip and through the cloud (`results/TWO_BILLS.md`), and the two lines are never added as percentages of different bills: each enters the one equation with its own share.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
