# The pages a person would have been sent: native against Omni-Compass on native

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The oversight line's second reading, counted from the raw files of its own 9 tables (omni-v27) by the rule written and committed before the first count (`docs/OVERSIGHT_PAGES_PREREGISTRATION.md`). A person on call is paid by the page, not by the minute: a page wakes someone, is answered, mitigated and written up. The alert minutes say how long a page would be open; this page says how many pages there would be. Class L: real software on GitHub's own machines, measured; no person is on those machines, so no hour or salary is on any receipt.

## The rule and the check

A bad minute is the oversight line's alert minute exactly: a whole minute of the measured window whose 95th percentile response time (nearest rank, a failed request counted over the line) was over the line, 500 ms in every table. A page opens after FOR bad minutes in a row while no page is open, and closes after RESET clean minutes in a row. The primary rule is FOR 1 minute, RESET 5 minutes (Alertmanager's default `resolve_timeout`); every pair of FOR 1, 2 and 5 and RESET 5 and 15 is printed below, declared with it.

Before any page was counted, the bad minutes recounted from the raw files had to give each run's printed alert minutes and their 95% interval: **27 of 27 runs** do, and only those are read.

## The pages, test by test (the primary rule)

| Test | Run A: pages per repetition, native → Omni-Compass | Run B | Run C | The three runs, by the one key |
|---|---|---|---|---|
| All four in one run | 1.10 → 0.70, down 36.4% (#44664572156) | 1.00 → 0.80, down 20.0% (#44680366764) | 1.00 → 0.90, down 10.0% (#44695279547) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| Batch queue | 1.00 → 1.00, no change (#44666372071) | 1.00 → 1.00, no change (#44680386621) | 1.00 → 1.00, no change (#44695299456) | STEADY, the same |
| Fairness | 1.00 → 1.00, no change (#44664578678) | 1.00 → 1.00, no change (#44680373422) | 1.00 → 1.00, no change (#44695285715) | STEADY, the same |
| Faults | 1.00 → 1.00, no change (#44666366302) | 1.00 → 1.00, no change (#44680380054) | 1.00 → 1.00, no change (#44695292827) | STEADY, the same |
| Kueue under the batch stream | 0.60 → 0.70, up 16.7% (#44673401745) | 0.90 → 0.90, no change (#44685881054) | 0.80 → 1.00, up 25.0% (#44697253488) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| Steady load | 0.30 → 0.00, down 100.0% (#44664547563) | 0.80 → 0.00, down 100.0% (#44678596546) | 0.60 → 0.00, down 100.0% (#44693353493) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| A public day of demand | 1.60 → 1.20, down 25.0% (#44666378039) | 2.00 → 1.20, down 40.0% (#44680393256) | 1.70 → 1.40, down 17.6% (#44695306073) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| Volcano under the batch stream | 0.40 → 0.30, down 25.0% (#44673408351) | 0.60 → 0.50, down 16.7% (#44687723958) | 0.40 → 0.50, up 25.0% (#44697261681) | the runs disagree |
| Wandering demand | 1.20 → 1.00, down 16.7% (#44664565856) | 0.90 → 0.80, down 11.1% (#44680359486) | 1.10 → 1.00, down 9.1% (#44695273057) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| **All the tests together** (each test's pages per repetition summed) | 8.20 → 6.90, down 15.9% | 9.20 → 7.20, down 21.7% | 8.60 → 7.80, down 9.3% | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |

Together, the three runs' means: **8.67 → 7.30 pages**, down **15.8%** with Omni-Compass on native, read **GAIN by the mean of our three runs, beyond the noise in 2 of 3**. Fewer pages, not only shorter ones: the minutes a page stays open, native → Omni-Compass, 12.9 → 11.3 in run A, 11.7 → 11.5 in run B, 14.6 → 12.8 in run C; the alert minutes over the same runs, 105.8 → 77.9, 107.2 → 82.9, 125.8 → 99.9.

## Every rule declared with it

| Rule (FOR bad minutes to open, RESET clean minutes to close) | Run A, together | Run B | Run C | The three runs |
|---|---|---|---|---|
| FOR 1, RESET 5 (the primary) | 8.20 → 6.90, down 15.9% | 9.20 → 7.20, down 21.7% | 8.60 → 7.80, down 9.3% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 1, RESET 15 | 7.60 → 6.70, down 11.8% | 8.20 → 7.10, down 13.4% | 8.10 → 7.60, down 6.2% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 2, RESET 5 | 7.70 → 6.50, down 15.6% | 8.10 → 6.80, down 16.0% | 7.90 → 7.20, down 8.9% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 2, RESET 15 | 7.40 → 6.30, down 14.9% | 7.50 → 6.70, down 10.7% | 7.70 → 7.10, down 7.8% | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| FOR 5, RESET 5 | 5.30 → 4.30, down 18.9% | 4.80 → 4.00, down 16.7% | 5.80 → 5.10, down 12.1% | GAIN in all three of our runs |
| FOR 5, RESET 15 | 5.10 → 4.30, down 15.7% | 4.40 → 4.00, down 9.1% | 5.60 → 5.10, down 8.9% | GAIN in all three of our runs |

## How it enters the bill

The bill is the sum of its lines: C = M + P + O, with M the machines, P the people who run the stack and O the rest, held fixed. The people line is priced by time-driven activity-based costing (Kaplan and Anderson, *Harvard Business Review*, November 2004): P = w · Σⱼ Nⱼ · hⱼ + R, with Nⱼ the events a year of kind j (a page, a hand-made change of a setting, a capacity review), hⱼ the person-hours each takes (a page's whole cycle about 6 hours by Google's SRE book, chapter 11), w one person-hour fully loaded and R the fixed cost of an on-call rotation. Omni-Compass's share of the bill saved on the people line is S(people) = κ · p · β · r: p the people's share of the run cost, β the share of their time that is answering pages and turning the knobs Omni-Compass governs (the SRE book holds on-call to at most 25% of an engineer's time), r the fall in the events that call a person, κ the share of the freed time that becomes money (1 where a rotation or a head is released or the time goes to paid work, 0 where nothing changes). Only r is measured here; p, β and κ are an owner's. With the machines' line, the live page's one equation reads G = (1 + ΔW) ⁄ (1 + m · ΔM + p · ΔP) − 1, ΔP = −κ · β · r.

On a run cost of $100 million, κ = 1, r = 15.8% (the pages above, the change of the three runs' means) and, beside it, r = 23.1% (the alert minutes):

| People's share of the run cost, p | β = 25% (on-call time only) | β = 100% (every people hour) |
|---|---|---|
| 7% | $0.3 million (0.3%); by the minutes $0.4 million | $1.1 million (1.1%); by the minutes $1.6 million |
| 10% | $0.4 million (0.4%); by the minutes $0.6 million | $1.6 million (1.6%); by the minutes $2.3 million |
| 20% | $0.8 million (0.8%); by the minutes $1.2 million | $3.2 million (3.2%); by the minutes $4.6 million |

These are the arithmetic of a measured fall and an owner's own shares, not a measured saving: the people cost itself, in hours, is measured only in a paired pilot on an owner's own records, their pager history and their log of changes to the governed settings, before and with Omni-Compass on native (`docs/PILOT_PROTOCOL.md`). The machines' line is read on the chip and through the cloud (`results/TWO_BILLS.md`), and the two lines are never added as percentages of different bills: each enters the one equation with its own share.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
