# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39379918375 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| B | 39410587818 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| C | 39459233023 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 977, 979, 974 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.3 | 366.1 | 366.3 → 366.1; raw −0.1% (95%: −0.2% to +0.1%); STEADY | 366.6 → 387.8; raw +5.8% (95%: −18.8% to +30.3%); GAIN | 365.6 → 365.6; raw ±0.0% (95%: −0.4% to +0.3%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 429.7 | 429.7 | 429.7 → 429.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 430.4 → 430.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 428.5 → 428.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,460 | 2,431 | 2460 → 2431; raw −1.2% (95%: −5.2% to +2.8%); GAIN | 2450 → 1619; raw −33.9% (95%: −170.4% to +102.6%); GAIN | 2350 → 2307; raw −1.8% (95%: −3.0% to −0.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,766 | 3,781 | 3766 → 3781; raw +0.4% (95%: −8.3% to +9.0%); STEADY | 3872 → 2569; raw −33.6% (95%: −160.8% to +93.5%); GAIN | 3651 → 3707; raw +1.6% (95%: −14.4% to +17.5%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 8.49 | 8.48 | 8.489 → 8.482; raw −0.1% (95%: −1.3% to +1.2%); STEADY | 8.27 → 8.129; raw −1.7% (95%: −7.7% to +4.3%); GAIN | 8.557 → 8.535; raw −0.3% (95%: −0.7% to +0.1%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 322.9 | 322.2 | 322.9 → 322.2; raw −0.2% (95%: −2.2% to +1.7%); STEADY | 328.5 → 218.7; raw −33.4% (95%: −161.5% to +94.7%); GAIN | 316.6 → 311.4; raw −1.6% (95%: −6.5% to +3.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,707 | 1,706 | 1707 → 1706; raw ±0.0% (95%: −1.5% to +1.5%); STEADY | 1719 → 1180; raw −31.3% (95%: −160.7% to +98.0%); GAIN | 1661 → 1676; raw +0.9% (95%: −4.8% to +6.6%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 142.7 | 142.4 | 142.7 → 142.4; raw −0.2% (95%: −1.8% to +1.4%); STEADY | 145.3 → 96.71; raw −33.5% (95%: −161.9% to +95.0%); GAIN | 140 → 137.6; raw −1.7% (95%: −5.7% to +2.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.184; raw +9.2% (95%: −31.9% to +50.3%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.319 | 0.318 | 0.3194 → 0.318; raw −0.4% (95%: −2.3% to +1.5%), −0.0014 in the gauge's unit; STEADY | 0.3061 → 0.309; raw +0.9% (95%: −1.2% to +3.1%), +0.0029 in the gauge's unit; power given | 0.3088 → 0.3068; raw −0.6% (95%: −3.5% to +2.2%), −0.0020 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 558.6 | 556.9 | 558.6 → 556.9; raw −0.3% (95%: −2.2% to +1.6%); STEADY | 544.8 → 549.4; raw +0.8% (95%: −1.5% to +3.2%); power given | 536.7 → 533.2; raw −0.6% (95%: −3.5% to +2.2%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.38 | 3.388 → 3.379; raw −0.3% (95%: −2.1% to +1.6%); STEADY | 3.301 → 3.166; raw −4.1% (95%: −24.7% to +16.5%); GAIN | 3.261 → 3.24; raw −0.6% (95%: −3.7% to +2.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 981, 973, 976 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342.6 | 341.6 | 342.6 → 341.6; raw −0.3% (95%: −2.2% to +1.6%); STEADY | 340.5 → 339.1; raw −0.4% (95%: −1.5% to +0.6%); STEADY | 341.1 → 340.6; raw −0.1% (95%: −0.3% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.29%) |
| throughput (messages a second consumed) | 421.4 | 421.4 | 421.4 → 421.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 417.8 → 417.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 419.3 → 419.6; raw +0.1% (95%: −0.3% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| end-to-end latency, 95th percentile (ms) | 2,564 | 2,603 | 2564 → 2603; raw +1.5% (95%: −13.1% to +16.1%); LOSS | 2505 → 2512; raw +0.3% (95%: −7.8% to +8.4%); STEADY | 2590 → 2533; raw −2.2% (95%: −9.5% to +5.1%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,717 | 3,762 | 3717 → 3762; raw +1.2% (95%: −19.0% to +21.5%); LOSS | 3616 → 3663; raw +1.3% (95%: −4.2% to +6.8%); LOSS | 3746 → 3802; raw +1.5% (95%: −10.7% to +13.6%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 10.3 | 12.0 | 10.25 → 11.99; raw +17.0% (95%: −38.9% to +72.9%); LOSS | 9.523 → 9.471; raw −0.5% (95%: −5.2% to +4.1%); GAIN | 9.459 → 9.53; raw +0.8% (95%: −5.5% to +7.0%); LOSS | **the runs disagree** |
| end-to-end latency, mean (ms) | 394.0 | 403.9 | 394 → 403.9; raw +2.5% (95%: −14.7% to +19.7%); LOSS | 374.7 → 383.4; raw +2.3% (95%: −4.8% to +9.5%); LOSS | 388.8 → 390.7; raw +0.5% (95%: −1.4% to +2.4%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,688 | 1,741 | 1688 → 1741; raw +3.1% (95%: −11.5% to +17.7%); LOSS | 1637 → 1629; raw −0.5% (95%: −5.6% to +4.7%); STEADY | 1676 → 1690; raw +0.8% (95%: −2.5% to +4.2%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 173.0 | 176.6 | 173 → 176.6; raw +2.1% (95%: −12.6% to +16.7%); LOSS | 163.2 → 164.7; raw +0.9% (95%: −4.3% to +6.1%); LOSS | 169.1 → 168.6; raw −0.3% (95%: −3.2% to +2.5%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.267 | 0.264 | 0.2672 → 0.2645; raw −1.0% (95%: −9.5% to +7.4%), −0.0028 in the gauge's unit; GAIN | 0.2944 → 0.2946; raw +0.1% (95%: −4.7% to +4.9%), +0.0002 in the gauge's unit; STEADY | 0.3022 → 0.2998; raw −0.8% (95%: −2.5% to +0.8%), −0.0025 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 191.9 | 189.9 | 191.9 → 189.9; raw −1.0% (95%: −9.4% to +7.4%); GAIN | 206 → 206.1; raw ±0.0% (95%: −4.7% to +4.8%); STEADY | 211.5 → 209.7; raw −0.8% (95%: −2.2% to +0.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.1 | 3.08 | 3.1 → 3.077; raw −0.7% (95%: −7.8% to +6.3%); GAIN | 3.349 → 3.364; raw +0.5% (95%: −4.7% to +5.6%); STEADY | 3.432 → 3.411; raw −0.6% (95%: −2.5% to +1.2%); GAIN | STEADY, under the floor (the three runs' mean 0.30%) |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 392, 394 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.9 | 147.1 → 146.9; raw −0.1% (95%: −0.7% to +0.5%); STEADY | 146.9 → 146.8; raw ±0.0% (95%: −0.4% to +0.3%); STEADY | 147.1 → 146.9; raw −0.1% (95%: −0.2% to −0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.10%) |
| throughput (messages a second consumed) | 173.2 | 173.2 | 173.2 → 173.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.4 → 172.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.9 → 172.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,519 | 2,528 | 2519 → 2528; raw +0.3% (95%: −9.3% to +9.9%); STEADY | 2382 → 2373; raw −0.4% (95%: −2.7% to +1.9%); STEADY | 2499 → 2522; raw +0.9% (95%: −4.4% to +6.2%); LOSS | STEADY, under the floor (the three runs' mean 0.28%) |
| end-to-end latency, 99th percentile (ms) | 3,949 | 3,918 | 3949 → 3918; raw −0.8% (95%: −10.3% to +8.8%); GAIN | 3747 → 3719; raw −0.7% (95%: −13.4% to +11.9%); GAIN | 3809 → 3829; raw +0.5% (95%: −8.9% to +9.9%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 11.7 | 11.8 | 11.72 → 11.77; raw +0.4% (95%: −0.9% to +1.7%); STEADY | 11.56 → 11.55; raw −0.1% (95%: −0.7% to +0.4%); STEADY | 11.64 → 11.62; raw −0.1% (95%: −0.5% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| end-to-end latency, mean (ms) | 342.2 | 345.6 | 342.2 → 345.6; raw +1.0% (95%: −7.9% to +9.8%); LOSS | 321.3 → 320.8; raw −0.2% (95%: −3.3% to +3.0%); STEADY | 334.6 → 336.9; raw +0.7% (95%: −1.5% to +2.9%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 719.7 | 731.7 | 719.7 → 731.7; raw +1.7% (95%: −3.7% to +7.0%); LOSS | 710.3 → 693; raw −2.4% (95%: −9.6% to +4.7%); GAIN | 716.7 → 704.7; raw −1.7% (95%: −3.2% to −0.2%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 62.8 | 63.5 | 62.77 → 63.45; raw +1.1% (95%: −8.9% to +11.0%); LOSS | 59.29 → 58.44; raw −1.4% (95%: −4.9% to +2.1%); GAIN | 61.62 → 61.69; raw +0.1% (95%: −2.3% to +2.5%); STEADY | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.29 | 0.292 | 0.2897 → 0.2917; raw +0.7% (95%: −3.3% to +4.7%), +0.0020 in the gauge's unit; power given | 0.2882 → 0.2853; raw −1.0% (95%: −2.8% to +0.8%), −0.0029 in the gauge's unit; GAIN | 0.292 → 0.2907; raw −0.4% (95%: −2.6% to +1.7%), −0.0013 in the gauge's unit; STEADY | **the runs disagree** |
| host CPU-seconds | 510.3 | 514.2 | 510.3 → 514.2; raw +0.8% (95%: −3.1% to +4.6%); power given | 509.8 → 504.7; raw −1.0% (95%: −2.9% to +0.9%); GAIN | 516.3 → 514; raw −0.4% (95%: −2.6% to +1.7%); STEADY | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 7.7 | 7.77 | 7.704 → 7.773; raw +0.9% (95%: −2.9% to +4.7%); power given | 7.702 → 7.627; raw −1.0% (95%: −3.1% to +1.2%); GAIN | 7.787 → 7.762; raw −0.3% (95%: −2.5% to +1.9%); STEADY | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,941, 1,932, 1,935 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728.0 | 725.4 | 728 → 725.4; raw −0.4% (95%: −0.9% to +0.1%); STEADY | 726.6 → 720.6; raw −0.8% (95%: −3.0% to +1.4%); LOSS | 726.5 → 726.1; raw −0.1% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.42%) |
| throughput (messages a second consumed) | 853.5 | 853.5 | 853.5 → 853.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 849.8 → 849.5; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 851.3 → 851.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,364 | 2,451 | 2364 → 2451; raw +3.7% (95%: +2.4% to +5.0%); LOSS | 2260 → 2968; raw +31.4% (95%: −104.1% to +166.8%); LOSS | 2399 → 2373; raw −1.1% (95%: −4.9% to +2.8%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,749 | 3,797 | 3749 → 3797; raw +1.3% (95%: −0.1% to +2.7%); LOSS | 3631 → 4479; raw +23.4% (95%: −67.8% to +114.5%); LOSS | 3678 → 3650; raw −0.8% (95%: −6.6% to +5.0%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 8.29 | 8.09 | 8.292 → 8.086; raw −2.5% (95%: −15.6% to +10.6%); GAIN | 7.514 → 7.514; raw ±0.0% (95%: −3.4% to +3.5%); STEADY | 7.543 → 7.551; raw +0.1% (95%: −1.9% to +2.1%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 322.8 | 335.4 | 322.8 → 335.4; raw +3.9% (95%: +0.9% to +6.9%); LOSS | 299.6 → 386.1; raw +28.8% (95%: −94.0% to +151.7%); LOSS | 312.4 → 310.4; raw −0.7% (95%: −2.0% to +0.7%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,374 | 3,389 | 3374 → 3389; raw +0.4% (95%: −3.4% to +4.3%); STEADY | 3197 → 3836; raw +20.0% (95%: −63.6% to +103.6%); LOSS | 3289 → 3265; raw −0.7% (95%: −1.3% to −0.1%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 283.0 | 292.7 | 283 → 292.7; raw +3.4% (95%: +0.3% to +6.6%); LOSS | 258.7 → 332.3; raw +28.5% (95%: −91.9% to +148.8%); LOSS | 270.1 → 268.1; raw −0.7% (95%: −2.1% to +0.6%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.016; raw +0.8% (95%: −3.8% to +5.3%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.32 | 0.32 | 0.3197 → 0.3196; raw ±0.0% (95%: −2.4% to +2.4%), −0.0001 in the gauge's unit; STEADY | 0.3516 → 0.3472; raw −1.3% (95%: −4.1% to +1.6%), −0.0044 in the gauge's unit; GAIN | 0.3617 → 0.3664; raw +1.3% (95%: −1.6% to +4.2%), +0.0047 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 548.4 | 549.1 | 548.4 → 549.1; raw +0.1% (95%: −2.7% to +3.0%); STEADY | 624.5 → 617.3; raw −1.1% (95%: −3.9% to +1.6%); GAIN | 646.2 → 655.1; raw +1.4% (95%: −1.4% to +4.2%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.67 | 1.68 | 1.673 → 1.682; raw +0.5% (95%: −1.9% to +2.9%); power given | 1.909 → 1.902; raw −0.4% (95%: −3.3% to +2.6%); STEADY | 1.976 → 2.004; raw +1.4% (95%: −1.2% to +4.1%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 4 gauge-rows GAIN, 5 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 16 STEADY, 15 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
