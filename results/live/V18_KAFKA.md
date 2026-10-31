# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40062228122 | `bbf7e12f0467` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| B | 40067527221 | `dadeec62a61a` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| C | 40130177581 | `791ad0fd93b1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 974, 983, 977 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.4 | 365.4 | 365.4 → 365.4; raw ±0.0% (95%: −0.7% to +0.7%); STEADY | 368.2 → 368.6; raw +0.1% (95%: ±0.0% to +0.2%); STEADY | 367.6 → 366.9; raw −0.2% (95%: −0.4% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (messages a second consumed) | 428.4 | 428.4 | 428.4 → 428.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 432.4 → 432.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 429.9 → 429.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,343 | 2,329 | 2343 → 2329; raw −0.6% (95%: −9.5% to +8.2%); GAIN | 2437 → 2412; raw −1.0% (95%: −3.6% to +1.5%); GAIN | 2276 → 2276; raw ±0.0% (95%: −13.8% to +13.8%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,642 | 3,704 | 3642 → 3704; raw +1.7% (95%: −9.4% to +12.8%); LOSS | 3729 → 3758; raw +0.8% (95%: −2.8% to +4.4%); LOSS | 3563 → 3688; raw +3.5% (95%: −3.9% to +10.9%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.51 | 8.52 | 8.513 → 8.52; raw +0.1% (95%: −1.3% to +1.5%); STEADY | 8.008 → 7.995; raw −0.2% (95%: −0.6% to +0.3%); STEADY | 8.059 → 8.008; raw −0.6% (95%: −3.1% to +1.8%); GAIN | STEADY, under the floor (the three runs' mean 0.24%) |
| end-to-end latency, mean (ms) | 312.6 | 312.0 | 312.6 → 312; raw −0.2% (95%: −11.3% to +10.9%); STEADY | 329.6 → 326.9; raw −0.8% (95%: −4.3% to +2.6%); GAIN | 304.5 → 308.8; raw +1.4% (95%: −5.3% to +8.1%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,664 | 1,654 | 1664 → 1654; raw −0.6% (95%: −6.8% to +5.6%); GAIN | 1735 → 1710; raw −1.4% (95%: −5.7% to +2.9%); GAIN | 1642 → 1653; raw +0.7% (95%: −5.0% to +6.4%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 138.6 | 137.9 | 138.6 → 137.9; raw −0.5% (95%: −10.1% to +9.1%); STEADY | 147.5 → 146.6; raw −0.6% (95%: −3.1% to +2.0%); GAIN | 135.9 → 137.4; raw +1.1% (95%: −5.9% to +8.1%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.245; raw +12.2% (95%: −14.8% to +39.3%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.305 | 0.306 | 0.3054 → 0.3061; raw +0.2% (95%: −0.7% to +1.1%), +0.0007 in the gauge's unit; STEADY | 0.2672 → 0.2659; raw −0.5% (95%: −1.9% to +0.9%), −0.0013 in the gauge's unit; GAIN | 0.2685 → 0.2696; raw +0.4% (95%: −3.5% to +4.3%), +0.0012 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| host CPU-seconds | 530.6 | 532.1 | 530.6 → 532.1; raw +0.3% (95%: −0.9% to +1.5%); STEADY | 477.9 → 475.8; raw −0.4% (95%: −1.6% to +0.7%); STEADY | 480 → 482.3; raw +0.5% (95%: −3.3% to +4.3%); STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.24 | 3.225 → 3.235; raw +0.3% (95%: −0.9% to +1.6%); STEADY | 2.884 → 2.868; raw −0.6% (95%: −1.6% to +0.5%); GAIN | 2.9 → 2.92; raw +0.7% (95%: −2.9% to +4.3%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 980, 972, 980 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341.7 | 341.6 | 341.7 → 341.6; raw ±0.0% (95%: −1.7% to +1.7%); STEADY | 340.8 → 340.1; raw −0.2% (95%: −0.3% to −0.1%); STEADY | 342.6 → 341.9; raw −0.2% (95%: −0.6% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.15%) |
| throughput (messages a second consumed) | 421.0 | 421.0 | 421 → 421; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 417.7 → 417.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 421.2 → 421.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,583 | 2,508 | 2583 → 2508; raw −2.9% (95%: −13.1% to +7.2%); GAIN | 2408 → 2435; raw +1.1% (95%: −18.9% to +21.2%); LOSS | 2623 → 2654; raw +1.2% (95%: −7.6% to +10.0%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,728 | 3,796 | 3728 → 3796; raw +1.8% (95%: −10.7% to +14.3%); LOSS | 3588 → 3500; raw −2.5% (95%: −11.5% to +6.6%); GAIN | 3845 → 3721; raw −3.2% (95%: −8.5% to +2.1%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 15.0 | 11.0 | 15.05 → 11.03; raw −26.7% (95%: −127.2% to +73.8%); GAIN | 8.6 → 8.602; raw ±0.0% (95%: −0.7% to +0.7%); STEADY | 8.568 → 8.523; raw −0.5% (95%: −4.4% to +3.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 397.2 | 395.1 | 397.2 → 395.1; raw −0.5% (95%: −14.5% to +13.5%); GAIN | 365.5 → 365.5; raw ±0.0% (95%: −10.3% to +10.3%); STEADY | 387.4 → 390.4; raw +0.8% (95%: ±0.0% to +1.6%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,688 | 1,707 | 1688 → 1707; raw +1.1% (95%: −4.1% to +6.4%); LOSS | 1597 → 1604; raw +0.4% (95%: −3.1% to +4.0%); STEADY | 1689 → 1700; raw +0.6% (95%: ±0.0% to +1.3%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 174.2 | 171.9 | 174.2 → 171.9; raw −1.3% (95%: −17.4% to +14.7%); GAIN | 158.2 → 157.8; raw −0.3% (95%: −10.5% to +10.0%); STEADY | 167.7 → 169.3; raw +0.9% (95%: −1.0% to +2.9%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.268 | 0.268 | 0.2684 → 0.2677; raw −0.3% (95%: −6.4% to +5.9%), −0.0007 in the gauge's unit; STEADY | 0.2846 → 0.2827; raw −0.7% (95%: −2.4% to +1.1%), −0.0019 in the gauge's unit; GAIN | 0.2836 → 0.2812; raw −0.8% (95%: −4.6% to +3.0%), −0.0024 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 192.6 | 192.2 | 192.6 → 192.2; raw −0.2% (95%: −6.2% to +5.8%); STEADY | 204.1 → 202.8; raw −0.6% (95%: −2.4% to +1.1%); GAIN | 203.4 → 201.7; raw −0.8% (95%: −4.7% to +3.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.12 | 3.12 | 3.121 → 3.115; raw −0.2% (95%: −4.9% to +4.5%); STEADY | 3.314 → 3.301; raw −0.4% (95%: −2.2% to +1.4%); STEADY | 3.285 → 3.266; raw −0.6% (95%: −4.2% to +3.1%); GAIN | STEADY, under the floor (the three runs' mean 0.39%) |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 394, 394 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.7 | 147.1 → 146.7; raw −0.3% (95%: −0.4% to −0.1%); STEADY | 147.2 → 147.2; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | 147.4 → 147; raw −0.3% (95%: −0.4% to −0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.18%) |
| throughput (messages a second consumed) | 172.8 | 172.8 | 172.8 → 172.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 173.4 → 173.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.9 → 173; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,458 | 2,499 | 2458 → 2499; raw +1.6% (95%: −3.6% to +6.8%); LOSS | 2599 → 2532; raw −2.6% (95%: −9.6% to +4.4%); GAIN | 2385 → 2441; raw +2.3% (95%: −3.9% to +8.6%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,845 | 3,859 | 3845 → 3859; raw +0.4% (95%: −4.4% to +5.1%); STEADY | 3962 → 3905; raw −1.5% (95%: −10.6% to +7.7%); GAIN | 3685 → 3766; raw +2.2% (95%: −8.9% to +13.3%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 11.5 | 11.5 | 11.54 → 11.54; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | 11.65 → 11.64; raw −0.1% (95%: −1.7% to +1.5%); STEADY | 11.14 → 11.02; raw −1.1% (95%: −6.7% to +4.5%); GAIN | STEADY, under the floor (the three runs' mean 0.39%) |
| end-to-end latency, mean (ms) | 332.1 | 338.4 | 332.1 → 338.4; raw +1.9% (95%: −3.0% to +6.8%); LOSS | 350.7 → 345.4; raw −1.5% (95%: −7.7% to +4.7%); GAIN | 319.3 → 329; raw +3.1% (95%: +0.9% to +5.2%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 703.0 | 716.7 | 703 → 716.7; raw +1.9% (95%: −3.0% to +6.9%); LOSS | 742.3 → 729.7; raw −1.7% (95%: −8.3% to +4.9%); GAIN | 679.3 → 692.7; raw +2.0% (95%: −3.9% to +7.8%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 60.8 | 62.2 | 60.76 → 62.16; raw +2.3% (95%: −2.4% to +7.0%); LOSS | 64.41 → 63.17; raw −1.9% (95%: −5.8% to +1.9%); GAIN | 58.27 → 60.12; raw +3.2% (95%: +0.6% to +5.7%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.28 | 0.278 | 0.2801 → 0.2781; raw −0.7% (95%: −3.3% to +1.8%), −0.0020 in the gauge's unit; GAIN | 0.2869 → 0.2849; raw −0.7% (95%: −4.0% to +2.7%), −0.0019 in the gauge's unit; GAIN | 0.2698 → 0.2632; raw −2.4% (95%: −14.3% to +9.5%), −0.0066 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 493.6 | 490.3 | 493.6 → 490.3; raw −0.7% (95%: −3.1% to +1.8%); GAIN | 505.3 → 502.4; raw −0.6% (95%: −4.1% to +2.9%); GAIN | 483.6 → 471.8; raw −2.4% (95%: −14.4% to +9.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.45 | 7.42 | 7.446 → 7.417; raw −0.4% (95%: −3.0% to +2.2%); STEADY | 7.627 → 7.583; raw −0.6% (95%: −4.5% to +3.3%); GAIN | 7.279 → 7.124; raw −2.1% (95%: −14.0% to +9.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,951, 1,950, 1,924 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732.9 | 731.2 | 732.9 → 731.2; raw −0.2% (95%: −0.8% to +0.4%); STEADY | 732.6 → 731.6; raw −0.1% (95%: −0.6% to +0.4%); STEADY | 725.5 → 715.6; raw −1.4% (95%: −4.4% to +1.6%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 858.0 | 858.3 | 858 → 858.3; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 857.8 → 857.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 846.1 → 846.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,293 | 2,319 | 2293 → 2319; raw +1.1% (95%: −3.0% to +5.3%); LOSS | 2301 → 2323; raw +1.0% (95%: −1.6% to +3.5%); LOSS | 2149 → 3673; raw +70.9% (95%: −87.7% to +229.6%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,691 | 3,605 | 3691 → 3605; raw −2.3% (95%: −9.7% to +5.1%); GAIN | 3621 → 3567; raw −1.5% (95%: −4.7% to +1.7%); GAIN | 3369 → 5355; raw +58.9% (95%: −68.0% to +185.8%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 15.4 | 11.2 | 15.38 → 11.19; raw −27.2% (95%: −112.3% to +57.9%); GAIN | 16.61 → 11.56; raw −30.4% (95%: −122.0% to +61.2%); GAIN | 8.372 → 8.294; raw −0.9% (95%: −7.6% to +5.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 322.1 | 323.9 | 322.1 → 323.9; raw +0.5% (95%: −3.9% to +5.0%); LOSS | 321.3 → 315.2; raw −1.9% (95%: −6.5% to +2.7%); GAIN | 287.9 → 485.4; raw +68.6% (95%: −83.5% to +220.7%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,305 | 3,332 | 3305 → 3332; raw +0.8% (95%: −4.7% to +6.3%); LOSS | 3303 → 3234; raw −2.1% (95%: −5.5% to +1.3%); GAIN | 3076 → 4491; raw +46.0% (95%: −54.2% to +146.2%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 285.7 | 284.7 | 285.7 → 284.7; raw −0.3% (95%: −5.0% to +4.3%); STEADY | 284.3 → 277.2; raw −2.5% (95%: −6.7% to +1.7%); GAIN | 250.1 → 415.6; raw +66.1% (95%: −81.2% to +213.5%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | 2 → 2.246; raw +12.3% (95%: −14.9% to +39.5%); power given | 2 → 2.247; raw +12.4% (95%: −15.0% to +39.7%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.286 | 0.283 | 0.2857 → 0.283; raw −1.0% (95%: −7.4% to +5.4%), −0.0028 in the gauge's unit; GAIN | 0.2816 → 0.2819; raw +0.1% (95%: −1.8% to +2.1%), +0.0003 in the gauge's unit; STEADY | 0.328 → 0.3233; raw −1.4% (95%: −3.8% to +1.0%), −0.0046 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 510.2 | 505.5 | 510.2 → 505.5; raw −0.9% (95%: −6.9% to +5.0%); GAIN | 503 → 503.8; raw +0.1% (95%: −1.9% to +2.2%); STEADY | 562.7 → 556.2; raw −1.1% (95%: −3.8% to +1.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 1.55 | 1.54 | 1.546 → 1.536; raw −0.7% (95%: −6.1% to +4.7%); GAIN | 1.525 → 1.53; raw +0.3% (95%: −1.3% to +1.8%); STEADY | 1.723 → 1.727; raw +0.2% (95%: −4.7% to +5.1%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| consumer changes written (the knob's moves) | 2 | 5.33 | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 6; raw +200.0% (95%: −48.4% to +448.4%) | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 10 gauge-rows GAIN, 3 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 13 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
