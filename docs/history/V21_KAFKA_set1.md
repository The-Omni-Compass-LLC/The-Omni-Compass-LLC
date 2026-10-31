# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40235701004 | `5ce458c7e7d2` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| B | 40256717947 | `a9f3cc761821` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| C | 40279909158 | `796063486f34` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 976, 973, 979 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.3 | 366.0 | -0.1% (-0.2 to +0.0) | -0.2% (-1.9 to +1.5) | +0.1% (-0.7 to +0.9) | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (messages a second consumed) | 429.2 | 429.2 | -0.0% (-0.0 to +0.0) | +0.0% (-0.1 to +0.2) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,371 | 2,394 | +1.0% (-4.1 to +6.0) | +2.6% (-7.3 to +12.5) | +1.1% (-13.1 to +15.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,653 | 3,705 | +1.4% (-4.8 to +7.7) | +0.3% (-2.8 to +3.4) | -2.2% (-3.8 to -0.7) | **the runs disagree** |
| end-to-end latency, median (ms) | 8.55 | 8.54 | -0.2% (-1.5 to +1.0) | -0.4% (-0.5 to -0.4) | +0.2% (-1.9 to +2.3) | STEADY, under the floor (the three runs' mean 0.14%) |
| end-to-end latency, mean (ms) | 316.7 | 319.4 | +0.8% (-0.8 to +2.5) | +0.9% (-9.4 to +11.1) | -0.1% (-8.2 to +8.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,667 | 1,687 | +1.2% (-3.1 to +5.5) | +0.1% (-5.7 to +5.8) | +1.1% (-3.6 to +5.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 140.9 | 141.2 | +0.2% (-1.3 to +1.7) | +1.0% (-9.2 to +11.2) | -0.1% (-8.4 to +8.2) | STEADY, under the floor (the three runs' mean 0.35%) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% (+0.0 to +0.0) | +1.1% (-3.7 to +5.9) | +0.0% (+0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.37%) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.307 | 0.305 | -0.7% (-3.1 to +1.6) | -1.0% (-2.5 to +0.4) | -1.0% (-10.9 to +8.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 532.6 | 528.6 | -0.7% (-3.5 to +2.0) | -1.0% (-2.3 to +0.3) | -1.0% (-10.5 to +8.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.21 | -0.7% (-3.4 to +2.1) | -0.8% (-2.8 to +1.2) | -1.2% (-11.2 to +8.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% (+0.0 to +0.0) | +33.3% (-110.1 to +176.8) | +0.0% (+0.0 to +0.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 971, 977, 980 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.3 | 340.3 | -0.0% (-0.3 to +0.3) | +0.7% (+0.5 to +0.9) | +0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.24%) |
| throughput (messages a second consumed) | 417.1 | 417.1 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,355 | 2,397 | +1.8% (-3.2 to +6.8) | -3.6% (-12.6 to +5.3) | +2.0% (-3.5 to +7.4) | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,605 | 3,453 | -4.2% (-6.7 to -1.7) | -1.7% (-9.4 to +6.0) | -3.0% (-7.6 to +1.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, median (ms) | 8.66 | 8.7 | +0.5% (-1.8 to +2.8) | -4.3% (-19.4 to +10.8) | -1.4% (-6.8 to +4.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 357.3 | 359.0 | +0.5% (-0.1 to +1.0) | -5.1% (-7.2 to -3.0) | -0.1% (-2.2 to +2.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| consumer lag, most messages waiting at once | 1,560 | 1,581 | +1.3% (-0.3 to +3.0) | -2.1% (-6.3 to +2.1) | -0.4% (-2.6 to +1.9) | **the runs disagree** |
| consumer lag, mean messages waiting | 153.8 | 154.3 | +0.3% (-0.1 to +0.7) | -6.0% (-10.6 to -1.3) | -0.4% (-4.8 to +4.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -0.9% (-6.8 to +5.0) | -1.2% (-6.9 to +4.5) | -2.2% (-6.5 to +2.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 214.3 | 212.2 | -1.0% (-6.8 to +4.9) | -1.3% (-6.9 to +4.4) | -2.2% (-6.5 to +2.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 3.45 | -1.0% (-6.7 to +4.8) | -2.0% (-7.6 to +3.6) | -2.2% (-6.4 to +2.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 393, 391 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146.9 | 147.0 | +0.0% (-0.5 to +0.5) | +0.0% (-0.6 to +0.7) | -0.3% (-1.0 to +0.3) | STEADY, under the floor (the three runs' mean 0.09%) |
| throughput (messages a second consumed) | 172.9 | 172.9 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,486 | 2,498 | +0.5% (-10.9 to +11.9) | +0.5% (-5.2 to +6.3) | +1.9% (-5.9 to +9.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,869 | 3,892 | +0.6% (-11.3 to +12.5) | -1.6% (-5.6 to +2.4) | +2.3% (-3.5 to +8.1) | **the runs disagree** |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.2% (-0.5 to +0.1) | -0.2% (-0.8 to +0.5) | -0.5% (-3.3 to +2.3) | STEADY, under the floor (the three runs' mean 0.29%) |
| end-to-end latency, mean (ms) | 339.9 | 339.3 | -0.2% (-5.7 to +5.3) | -0.4% (-8.4 to +7.6) | +3.0% (-6.0 to +12.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 717.7 | 705.0 | -1.8% (-9.2 to +5.6) | +0.1% (-1.7 to +2.0) | -0.6% (-12.8 to +11.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 62.5 | 62.1 | -0.6% (-5.4 to +4.2) | -0.1% (-6.1 to +5.9) | +3.1% (-5.2 to +11.5) | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +3.2% (+3.0 to +3.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +50.0% (+50.0 to +50.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.279 | 0.277 | -0.7% (-3.2 to +1.9) | -0.5% (-2.7 to +1.7) | -1.4% (-6.6 to +3.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 491.4 | 488.1 | -0.7% (-3.2 to +1.8) | -0.5% (-2.7 to +1.7) | -1.4% (-6.5 to +3.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.37 | -0.7% (-3.7 to +2.3) | -0.6% (-3.1 to +2.0) | -1.0% (-6.8 to +4.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,935, 1,934, 1,951 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726.8 | 724.9 | -0.3% (-1.3 to +0.8) | -0.2% (-0.8 to +0.5) | -0.3% (-1.7 to +1.1) | STEADY, under the floor (the three runs' mean 0.25%) |
| throughput (messages a second consumed) | 851.0 | 851.0 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,315 | 2,321 | +0.2% (-8.4 to +8.9) | -0.3% (-4.5 to +3.9) | -0.7% (-13.4 to +12.0) | STEADY, under the floor (the three runs' mean 0.25%) |
| end-to-end latency, 99th percentile (ms) | 3,756 | 3,758 | +0.0% (-16.8 to +16.9) | +0.6% (-4.3 to +5.5) | +0.8% (-3.8 to +5.4) | STEADY, under the floor (the three runs' mean 0.50%) |
| end-to-end latency, median (ms) | 7.78 | 7.66 | -1.6% (-3.2 to +0.0) | -0.0% (-3.8 to +3.7) | +1.2% (-108.0 to +110.3) | **the runs disagree** |
| end-to-end latency, mean (ms) | 310.5 | 314.1 | +1.2% (-2.2 to +4.5) | +1.5% (-3.7 to +6.6) | +0.1% (-10.7 to +10.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,289 | 3,279 | -0.3% (-1.4 to +0.8) | +0.6% (-0.2 to +1.4) | -1.0% (-10.3 to +8.4) | **the runs disagree** |
| consumer lag, mean messages waiting | 269.1 | 271.5 | +0.9% (-1.9 to +3.7) | +1.3% (-4.4 to +7.1) | +0.1% (-10.3 to +10.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.8% (-19.0 to +30.5) | +0.0% (+0.0 to +0.0) | +16.9% (-24.5 to +58.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | +66.7% (-123.1 to +256.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.352 | 0.344 | -2.2% (-7.1 to +2.6) | -0.4% (-1.5 to +0.7) | -1.0% (-7.7 to +5.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 624.1 | 610.8 | -2.1% (-7.4 to +3.2) | -0.5% (-0.9 to -0.1) | -1.0% (-7.5 to +5.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 1.91 | 1.87 | -1.9% (-8.2 to +4.4) | -0.3% (-1.1 to +0.5) | -0.7% (-8.5 to +7.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% (-660.6 to +1060.6) | +0.0% (+0.0 to +0.0) | +433.3% (-507.2 to +1373.9) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: acting: 2 to 4 (4 trials, 2 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 14 gauge-rows GAIN, 4 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 6 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
