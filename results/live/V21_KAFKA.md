# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40256717947 | `a9f3cc761821` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| B | 40279909158 | `796063486f34` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| C | 40400868003 | `5e222aa21371` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 973, 979, 979 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.7 | 365.1 | 365.7 → 365.1; raw −0.2% (95%: −1.9% to +1.5%); STEADY | 367 → 367.5; raw +0.1% (95%: −0.7% to +0.9%); STEADY | 371.1 → 366.1; raw −1.4% (95%: −6.1% to +3.4%); LOSS | STEADY, under the floor (the three runs' mean 0.46%) |
| throughput (messages a second consumed) | 427.4 | 427.6 | 427.4 → 427.6; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 430.8 → 430.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 430.5 → 430.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,208 | 2,265 | 2208 → 2265; raw +2.6% (95%: −7.3% to +12.5%); LOSS | 2363 → 2389; raw +1.1% (95%: −13.1% to +15.4%); LOSS | 1612 → 1704; raw +5.7% (95%: −15.0% to +26.4%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,496 | 3,506 | 3496 → 3506; raw +0.3% (95%: −2.8% to +3.4%); STEADY | 3748 → 3666; raw −2.2% (95%: −3.8% to −0.7%); GAIN | 2450 → 2674; raw +9.1% (95%: −16.2% to +34.5%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 8.42 | 8.39 | 8.424 → 8.389; raw −0.4% (95%: −0.5% to −0.4%); STEADY | 8.175 → 8.192; raw +0.2% (95%: −1.9% to +2.3%); STEADY | 8.135 → 8.15; raw +0.2% (95%: −2.6% to +3.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, mean (ms) | 293.3 | 295.8 | 293.3 → 295.8; raw +0.9% (95%: −9.4% to +11.1%); LOSS | 322 → 321.6; raw −0.1% (95%: −8.2% to +8.0%); STEADY | 219.1 → 243.9; raw +11.3% (95%: −28.9% to +51.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,603 | 1,604 | 1603 → 1604; raw +0.1% (95%: −5.7% to +5.8%); STEADY | 1700 → 1718; raw +1.1% (95%: −3.6% to +5.8%); LOSS | 1130 → 1192; raw +5.5% (95%: −11.5% to +22.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 128.9 | 130.2 | 128.9 → 130.2; raw +1.0% (95%: −9.2% to +11.2%); LOSS | 143.6 → 143.4; raw −0.1% (95%: −8.4% to +8.2%); STEADY | 98.81 → 110; raw +11.3% (95%: −28.3% to +50.9%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.02 | 2 → 2.022; raw +1.1% (95%: −3.7% to +5.9%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.002; raw +0.1% (95%: −0.4% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.41%) |
| consumers running, most at once | 2 | 2.33 | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.317 | 0.313 | 0.3167 → 0.3134; raw −1.0% (95%: −2.5% to +0.4%), −0.0033 in the gauge's unit; GAIN | 0.2848 → 0.282; raw −1.0% (95%: −10.9% to +8.9%), −0.0028 in the gauge's unit; GAIN | 0.2821 → 0.286; raw +1.4% (95%: −3.9% to +6.7%), +0.0039 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 565.1 | 559.6 | 565.1 → 559.6; raw −1.0% (95%: −2.3% to +0.3%); GAIN | 508.7 → 503.6; raw −1.0% (95%: −10.5% to +8.5%); GAIN | 335.8 → 340.6; raw +1.4% (95%: −3.7% to +6.6%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.4 | 3.43 → 3.404; raw −0.8% (95%: −2.8% to +1.2%); GAIN | 3.079 → 3.043; raw −1.2% (95%: −11.2% to +8.9%); GAIN | 3.014 → 3.1; raw +2.9% (95%: −7.1% to +12.8%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −110.1% to +176.8%) | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | 2 → 2.667; raw +33.3% (95%: −110.1% to +176.8%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 977, 980, 975 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339.2 | 341.6 | 339.2 → 341.6; raw +0.7% (95%: +0.5% to +0.9%); GAIN | 341.7 → 341.7; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 346.7 → 347.2; raw +0.1% (95%: −0.3% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.29%) |
| throughput (messages a second consumed) | 419.6 | 419.6 | 419.6 → 419.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 421 → 421; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 418.1 → 418.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,626 | 2,531 | 2626 → 2531; raw −3.6% (95%: −12.6% to +5.3%); GAIN | 2608 → 2659; raw +2.0% (95%: −3.5% to +7.4%); LOSS | 1706 → 1711; raw +0.3% (95%: −3.9% to +4.4%); STEADY | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,966 | 3,898 | 3966 → 3898; raw −1.7% (95%: −9.4% to +6.0%); GAIN | 3906 → 3790; raw −3.0% (95%: −7.6% to +1.7%); GAIN | 2500 → 2497; raw −0.1% (95%: −8.2% to +7.9%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 9.83 | 9.4 | 9.825 → 9.401; raw −4.3% (95%: −19.4% to +10.8%); GAIN | 8.753 → 8.633; raw −1.4% (95%: −6.8% to +4.0%); GAIN | 9.83 → 9.83; raw ±0.0% (95%: −8.2% to +8.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 407.2 | 386.4 | 407.2 → 386.4; raw −5.1% (95%: −7.2% to −3.0%); GAIN | 398 → 397.7; raw −0.1% (95%: −2.2% to +2.0%); STEADY | 266.1 → 265.4; raw −0.3% (95%: −0.8% to +0.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| consumer lag, most messages waiting at once | 1,720 | 1,684 | 1720 → 1684; raw −2.1% (95%: −6.3% to +2.1%); GAIN | 1731 → 1724; raw −0.4% (95%: −2.6% to +1.9%); STEADY | 1128 → 1144; raw +1.4% (95%: −2.8% to +5.6%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 178.0 | 167.3 | 178 → 167.3; raw −6.0% (95%: −10.6% to −1.3%); GAIN | 173.1 → 172.5; raw −0.4% (95%: −4.8% to +4.0%); STEADY | 117.1 → 116.3; raw −0.7% (95%: −1.7% to +0.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.293 | 0.289 | 0.2927 → 0.2893; raw −1.2% (95%: −6.9% to +4.5%), −0.0034 in the gauge's unit; GAIN | 0.289 → 0.2825; raw −2.2% (95%: −6.5% to +2.0%), −0.0065 in the gauge's unit; GAIN | 0.3012 → 0.2942; raw −2.3% (95%: −15.9% to +11.3%), −0.0071 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 204.9 | 202.3 | 204.9 → 202.3; raw −1.3% (95%: −6.9% to +4.4%); GAIN | 207.2 → 202.6; raw −2.2% (95%: −6.5% to +2.0%); GAIN | 140.8 → 137.5; raw −2.3% (95%: −16.1% to +11.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.28 | 3.344 → 3.279; raw −2.0% (95%: −7.6% to +3.6%); GAIN | 3.356 → 3.282; raw −2.2% (95%: −6.4% to +2.0%); GAIN | 3.366 → 3.282; raw −2.5% (95%: −16.4% to +11.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 391, 391 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.0 | 147.1 | 147 → 147.1; raw ±0.0% (95%: −0.6% to +0.7%); STEADY | 147.2 → 146.7; raw −0.3% (95%: −1.0% to +0.3%); STEADY | 148.2 → 147.3; raw −0.6% (95%: −3.5% to +2.3%); LOSS | STEADY, under the floor (the three runs' mean 0.31%) |
| throughput (messages a second consumed) | 173.1 | 173.1 | 173.1 → 173.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 171.8 → 171.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 171.9 → 171.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,516 | 2,529 | 2516 → 2529; raw +0.5% (95%: −5.2% to +6.3%); LOSS | 2148 → 2190; raw +1.9% (95%: −5.9% to +9.8%); LOSS | 1567 → 1543; raw −1.6% (95%: −13.1% to +10.0%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,850 | 3,789 | 3850 → 3789; raw −1.6% (95%: −5.6% to +2.4%); GAIN | 3398 → 3476; raw +2.3% (95%: −3.5% to +8.1%); LOSS | 2435 → 2433; raw −0.1% (95%: −22.6% to +22.4%); STEADY | **the runs disagree** |
| end-to-end latency, median (ms) | 11.6 | 11.6 | 11.64 → 11.63; raw −0.2% (95%: −0.8% to +0.5%); STEADY | 11.38 → 11.32; raw −0.5% (95%: −3.3% to +2.3%); GAIN | 11.63 → 11.67; raw +0.4% (95%: −0.2% to +0.9%); STEADY | STEADY, under the floor (the three runs' mean 0.10%) |
| end-to-end latency, mean (ms) | 341.0 | 339.6 | 341 → 339.6; raw −0.4% (95%: −8.4% to +7.6%); STEADY | 284.4 → 293.1; raw +3.0% (95%: −6.0% to +12.0%); LOSS | 214.2 → 220.5; raw +2.9% (95%: −20.8% to +26.7%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 717.7 | 718.7 | 717.7 → 718.7; raw +0.1% (95%: −1.7% to +2.0%); STEADY | 657.3 → 653.3; raw −0.6% (95%: −12.8% to +11.5%); GAIN | 462.7 → 468.7; raw +1.3% (95%: −21.2% to +23.8%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 62.6 | 62.5 | 62.6 → 62.55; raw −0.1% (95%: −6.1% to +5.9%); STEADY | 52.12 → 53.75; raw +3.1% (95%: −5.2% to +11.5%); LOSS | 39.89 → 41.44; raw +3.9% (95%: −23.7% to +31.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.064; raw +3.2% (95%: +3.0% to +3.3%); power given | 2 → 2.233; raw +11.6% (95%: −12.4% to +35.6%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.285 | 0.284 | 0.2851 → 0.2837; raw −0.5% (95%: −2.7% to +1.7%), −0.0015 in the gauge's unit; GAIN | 0.2787 → 0.2749; raw −1.4% (95%: −6.6% to +3.9%), −0.0038 in the gauge's unit; GAIN | 0.2825 → 0.2845; raw +0.7% (95%: −4.0% to +5.4%), +0.0020 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 502.2 | 499.5 | 502.2 → 499.5; raw −0.5% (95%: −2.7% to +1.7%); GAIN | 499 → 492.2; raw −1.4% (95%: −6.5% to +3.8%); GAIN | 331.8 → 334.2; raw +0.7% (95%: −4.0% to +5.4%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 7.59 | 7.54 | 7.587 → 7.545; raw −0.6% (95%: −3.1% to +2.0%); GAIN | 7.531 → 7.455; raw −1.0% (95%: −6.8% to +4.8%); GAIN | 7.458 → 7.559; raw +1.4% (95%: −0.6% to +3.3%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 8; raw +300.0% (95%: −130.3% to +730.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,934, 1,951, 1,925 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726.1 | 724.7 | 726.1 → 724.7; raw −0.2% (95%: −0.8% to +0.5%); STEADY | 732.2 → 730; raw −0.3% (95%: −1.7% to +1.1%); STEADY | 732.6 → 726.6; raw −0.8% (95%: −2.1% to +0.5%); LOSS | STEADY, under the floor (the three runs' mean 0.44%) |
| throughput (messages a second consumed) | 850.5 | 850.5 | 850.5 → 850.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 858.2 → 858.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 846.6 → 846.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,369 | 2,362 | 2369 → 2362; raw −0.3% (95%: −4.5% to +3.9%); STEADY | 2375 → 2359; raw −0.7% (95%: −13.4% to +12.0%); GAIN | 1515 → 1716; raw +13.2% (95%: −27.0% to +53.5%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,736 | 3,759 | 3736 → 3759; raw +0.6% (95%: −4.3% to +5.5%); LOSS | 3649 → 3679; raw +0.8% (95%: −3.8% to +5.4%); LOSS | 2394 → 2611; raw +9.1% (95%: −14.1% to +32.2%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.34 | 8.34 | 8.339 → 8.336; raw ±0.0% (95%: −3.8% to +3.7%); STEADY | 10.27 → 10.39; raw +1.2% (95%: −108.0% to +110.3%); LOSS | 8.223 → 7.917; raw −3.7% (95%: −10.1% to +2.6%); GAIN | **the runs disagree** |
| end-to-end latency, mean (ms) | 318.8 | 323.5 | 318.8 → 323.5; raw +1.5% (95%: −3.7% to +6.6%); LOSS | 326.7 → 326.9; raw +0.1% (95%: −10.7% to +10.8%); STEADY | 210.7 → 235.5; raw +11.8% (95%: −13.9% to +37.4%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,274 | 3,293 | 3274 → 3293; raw +0.6% (95%: −0.2% to +1.4%); LOSS | 3348 → 3316; raw −1.0% (95%: −10.3% to +8.4%); GAIN | 2195 → 2276; raw +3.7% (95%: −17.4% to +24.9%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 277.4 | 281.1 | 277.4 → 281.1; raw +1.3% (95%: −4.4% to +7.1%); LOSS | 287.4 → 287.7; raw +0.1% (95%: −10.3% to +10.5%); STEADY | 184.6 → 205.4; raw +11.2% (95%: −13.1% to +35.6%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.338; raw +16.9% (95%: −24.5% to +58.3%); power given | 2 → 2.289; raw +14.5% (95%: −5.8% to +34.7%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 3.333; raw +66.7% (95%: −123.1% to +256.4%); power given | 2 → 3.667; raw +83.3% (95%: +11.6% to +155.1%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.332 | 0.33 | 0.3316 → 0.3302; raw −0.4% (95%: −1.5% to +0.7%), −0.0014 in the gauge's unit; STEADY | 0.2884 → 0.2856; raw −1.0% (95%: −7.7% to +5.8%), −0.0028 in the gauge's unit; GAIN | 0.3311 → 0.3311; raw ±0.0% (95%: −3.3% to +3.3%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.46%) |
| host CPU-seconds | 569.8 | 567.2 | 569.8 → 567.2; raw −0.5% (95%: −0.9% to −0.1%); STEADY | 515 → 509.7; raw −1.0% (95%: −7.5% to +5.4%); GAIN | 379.5 → 379.6; raw ±0.0% (95%: −2.9% to +2.9%); STEADY | STEADY, under the floor (the three runs' mean 0.48%) |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.74 | 1.743 → 1.738; raw −0.3% (95%: −1.1% to +0.5%); STEADY | 1.562 → 1.551; raw −0.7% (95%: −8.5% to +7.0%); GAIN | 1.726 → 1.741; raw +0.9% (95%: −2.7% to +4.4%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | 2 → 10.67; raw +433.3% (95%: −507.2% to +1373.9%) | 2 → 9.333; raw +366.7% (95%: −12.8% to +746.2%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: acting: 2 to 4 (4 trials, 2 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 1 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 7 gauge-rows GAIN, 5 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
