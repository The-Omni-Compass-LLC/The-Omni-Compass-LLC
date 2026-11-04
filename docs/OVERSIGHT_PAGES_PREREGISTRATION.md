# Preregistration: the pages a person would have been sent, native against Omni-Compass on native

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written and committed on 4 November 2026, before a single page was counted, on the founder's words of the same day ("find a
way to measure what the babysitting tax would be ... a referee level ... way to calculate this fee within a $100 million
budget or any budget"). Nothing below changes after the first count; a change would be a new, dated amendment, and the first
count would stand beside it.

## The question

The oversight line (`results/OVERSIGHT.md`) reads the alert minutes: the whole minutes in which a person on call would have a
page open. A person is paid by the page, not by the minute: a page wakes someone, is answered, mitigated and written up, and
Google's SRE book (Beyer, Jones, Petoff and Murphy, *Site Reliability Engineering*, O'Reilly 2016, chapter 11) puts that whole
cycle at about six hours of an engineer's time. Fewer minutes could come from the same number of pages, each shorter. So the
question asked here is the one the labor follows: **how many pages would a person have been sent in each arm?**

## The records

The thirteen Kubernetes three-run tables of omni-v21 that carry the alert minutes (`results/live/V21_*.json`, the same tables
the oversight line pools), thirty-nine runs on GitHub's own machines, each repetition's two arms kept whole on the branch
`raw` with their SHA-256 sums: every arm's `latency.csv` (each sampled request's response time, and whether it failed) and its
measured window (`window_start.txt`, `window_end.txt`). Nothing is run again; nothing is added.

## The rule

- **A bad minute** is the oversight line's alert minute exactly, as `tools/live_reps.py` counts it: a whole minute of the
  measured window whose 95th percentile response time (nearest rank, a failed request counted over the line) was over the line.
  The line is 500 ms in all thirteen tables (no workflow behind them sets another). A minute with no sample is not bad.
- **A page** opens on the first bad minute when no page is open, after `FOR` bad minutes in a row (the alert's pending time),
  stays open through every bad minute and every gap of fewer than `RESET` clean minutes, and closes after `RESET` clean minutes
  in a row or at the end of the window. Each opening is one page.
- **The primary rule:** `FOR` = 1 minute (a page on the first bad minute, no pending time) and `RESET` = 5 minutes (the
  default `resolve_timeout` of Prometheus's Alertmanager). **Declared with it, as sensitivity, every pair** of `FOR` 1, 2 and
  5 minutes and `RESET` 5 and 15 minutes; every pair is printed, the primary first, and none is chosen after the count.

## The check before any page is counted

For every run, the bad minutes recounted from the raw files must give, arm by arm, the mean alert minutes the table itself
prints for that run (to its printed precision). A run whose recount differs is named and left out of the pages, never fitted;
the count of runs that pass is printed.

## The reading

- Each test, run by run: the pages per repetition in each arm, paired by repetition; the change, the mean difference in
  percent of native with its 95% interval on the exact Student t (`omnicompass/student_t.py`); the three runs read by the one
  key (`tools/readings.py`, `three_run_reading`), the gauge's aim lower (a page is time a person is taken: a fall is GAIN).
- All the tests together, run by run: the pages per repetition of each test summed (each test once, as the oversight line sums
  its minutes), the variances added, the three runs read by the one key.
- Every number beside its word, the word first, the run's number beside each run (#run).

## What it does not measure, and how it enters the bill

It measures the events that call a person, under one load and one line, in our own runs (class L). It does not measure a
person's hours, a salary or an owner's own pager: no person is on GitHub's machines. The bill takes it as one line, priced by
time-driven activity-based costing (Kaplan and Anderson, "Time-Driven Activity-Based Costing", *Harvard Business Review*,
November 2004):

C = M + P + O, &nbsp; P = w · Σⱼ Nⱼ · hⱼ + R

with C the run cost of the stack, M its machines, P the people who run it, O the rest held fixed; Nⱼ the events a year of kind
j (a page, a hand-made change of a setting, a capacity review), hⱼ the person-hours each takes, w one person-hour fully
loaded, R the fixed cost of an on-call rotation. Omni-Compass's share of the bill saved on the people line is

S(people) = κ · p · β · r

with p = P ⁄ C the people's share of the run cost (an owner's own number), β the share of their time that is answering pages
and turning the knobs Omni-Compass governs (the SRE book holds on-call to at most 25% of an engineer's time), r the fall in
the events that call a person (this count's pages; the oversight line's minutes beside it), and κ the share of the freed time
that becomes money (1 where a rotation or a head is released or the time goes to paid work, 0 where nothing changes). The
measured term is r alone; p, β and κ are an owner's, and every page that prints the product says so. The whole bill's work
for the money, the live page's one equation with the people line added:

G = (1 + ΔW) ⁄ (1 + m · ΔM + p · ΔP) − 1, &nbsp; ΔP = −κ · β · r

with m = M ⁄ C. The people cost itself, in hours, is measured only in a paired pilot on an owner's own records (their pager
history and their log of changes to the governed settings, before and with Omni-Compass on native;
`docs/PILOT_PROTOCOL.md`).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
