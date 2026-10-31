# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39150481307 | `c1c1b59711b1` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| B | 39159000835 | `3cb376bb3284` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| C | 39167574190 | `e2d5958834f5` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 974, 984, 976 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.3 | 364.9 | 365.3 → 364.9; raw −0.1% (95%: −0.6% to +0.4%); STEADY | 368 → 367.6; raw −0.1% (95%: −0.5% to +0.3%); STEADY | 365.7 → 365.6; raw ±0.0% (95%: −0.4% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.09%) |
| throughput (messages a second consumed) | 428.6 | 428.6 | 428.6 → 428.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 432.7 → 432.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 429.1 → 429.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,395 | 2,372 | 2395 → 2372; raw −1.0% (95%: −16.6% to +14.7%); GAIN | 2499 → 2530; raw +1.2% (95%: −3.2% to +5.6%); LOSS | 2394 → 2385; raw −0.4% (95%: −6.6% to +5.8%); STEADY | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,675 | 3,776 | 3675 → 3776; raw +2.8% (95%: −2.2% to +7.7%); LOSS | 3887 → 3839; raw −1.2% (95%: −6.6% to +4.1%); GAIN | 3850 → 3761; raw −2.3% (95%: −11.1% to +6.5%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 8.55 | 8.54 | 8.554 → 8.539; raw −0.2% (95%: −1.9% to +1.5%); STEADY | 8.041 → 8.058; raw +0.2% (95%: −3.5% to +3.9%); STEADY | 8.524 → 8.491; raw −0.4% (95%: −0.9% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| end-to-end latency, mean (ms) | 317.7 | 320.5 | 317.7 → 320.5; raw +0.9% (95%: −6.6% to +8.4%); LOSS | 340.6 → 343.1; raw +0.7% (95%: −2.2% to +3.6%); LOSS | 324.3 → 319.6; raw −1.5% (95%: −9.1% to +6.1%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,685 | 1,681 | 1685 → 1681; raw −0.3% (95%: −5.8% to +5.2%); STEADY | 1763 → 1748; raw −0.8% (95%: −3.7% to +2.1%); GAIN | 1679 → 1684; raw +0.3% (95%: −7.0% to +7.6%); STEADY | STEADY, under the floor (the three runs' mean 0.27%) |
| consumer lag, mean messages waiting | 140.6 | 141.6 | 140.6 → 141.6; raw +0.7% (95%: −5.9% to +7.3%); LOSS | 152.3 → 153.2; raw +0.6% (95%: −3.6% to +4.8%); LOSS | 143.5 → 141.6; raw −1.3% (95%: −8.8% to +6.1%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.308 | 0.309 | 0.3079 → 0.3088; raw +0.3% (95%: −2.3% to +2.8%), +0.0009 in the gauge's unit; STEADY | 0.2753 → 0.2763; raw +0.4% (95%: −6.1% to +6.8%), +0.0010 in the gauge's unit; STEADY | 0.3079 → 0.308; raw ±0.0% (95%: −3.2% to +3.3%), +0.0001 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.22%) |
| host CPU-seconds | 534.4 | 537.7 | 534.4 → 537.7; raw +0.6% (95%: −2.1% to +3.3%); power given | 491.7 → 494.1; raw +0.5% (95%: −5.8% to +6.8%); STEADY | 534.4 → 536.2; raw +0.3% (95%: −3.0% to +3.7%); STEADY | STEADY, under the floor (the three runs' mean 0.48%) |
| host CPU-seconds per 1,000 messages inside the line | 3.25 | 3.27 | 3.25 → 3.273; raw +0.7% (95%: −1.5% to +2.9%); power given | 2.968 → 2.986; raw +0.6% (95%: −5.4% to +6.6%); power given | 3.246 → 3.258; raw +0.4% (95%: −3.2% to +3.9%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 973, 973 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.1 | 340.3 | 340.1 → 340.3; raw +0.1% (95%: −0.9% to +1.1%); STEADY | 340.3 → 339.7; raw −0.2% (95%: −0.4% to ±0.0%); STEADY | 339.8 → 339.8; raw ±0.0% (95%: −1.4% to +1.4%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| throughput (messages a second consumed) | 418.6 | 418.6 | 418.6 → 418.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 418.1 → 418.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 418.2 → 418.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,520 | 2,482 | 2520 → 2482; raw −1.5% (95%: −8.2% to +5.2%); GAIN | 2513 → 2535; raw +0.9% (95%: −3.0% to +4.7%); LOSS | 2468 → 2493; raw +1.0% (95%: −8.6% to +10.6%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,877 | 3,663 | 3877 → 3663; raw −5.5% (95%: −17.7% to +6.6%); GAIN | 3588 → 3715; raw +3.5% (95%: −3.8% to +10.9%); LOSS | 3852 → 3598; raw −6.6% (95%: −18.0% to +4.8%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 9.83 | 9.28 | 9.834 → 9.275; raw −5.7% (95%: −17.4% to +6.0%); GAIN | 9.569 → 9.036; raw −5.6% (95%: −14.5% to +3.3%); GAIN | 9.613 → 9.413; raw −2.1% (95%: −7.3% to +3.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 388.7 | 383.2 | 388.7 → 383.2; raw −1.4% (95%: −10.8% to +7.9%); GAIN | 376.8 → 377.5; raw +0.2% (95%: −1.9% to +2.3%); STEADY | 384.2 → 378.5; raw −1.5% (95%: −8.5% to +5.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,661 | 1,664 | 1661 → 1664; raw +0.2% (95%: −5.7% to +6.0%); STEADY | 1642 → 1652; raw +0.6% (95%: −0.5% to +1.8%); LOSS | 1654 → 1625; raw −1.7% (95%: −7.2% to +3.7%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 168.4 | 164.9 | 168.4 → 164.9; raw −2.1% (95%: −13.5% to +9.3%); GAIN | 162.7 → 162.5; raw −0.1% (95%: −4.0% to +3.8%); STEADY | 166.4 → 163.1; raw −2.0% (95%: −11.1% to +7.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.984; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | 0.2989 → 0.2958; raw −1.0% (95%: −6.8% to +4.7%), −0.0031 in the gauge's unit; GAIN | 0.3259 → 0.3113; raw −4.5% (95%: −18.4% to +9.5%), −0.0145 in the gauge's unit; GAIN | 0.298 → 0.2922; raw −1.9% (95%: −5.4% to +1.6%), −0.0057 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 209.2 | 207.1 | 209.2 → 207.1; raw −1.0% (95%: −6.8% to +4.8%); GAIN | 233.1 → 222.8; raw −4.4% (95%: −18.5% to +9.6%); GAIN | 208.6 → 204.5; raw −2.0% (95%: −5.5% to +1.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.4 | 3.37 | 3.405 → 3.368; raw −1.1% (95%: −6.0% to +3.8%); GAIN | 3.791 → 3.629; raw −4.3% (95%: −18.1% to +9.6%); GAIN | 3.397 → 3.331; raw −2.0% (95%: −4.3% to +0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 393, 377 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.8 | 147.1 → 146.8; raw −0.2% (95%: −0.6% to +0.2%); STEADY | 146.9 → 146.8; raw −0.1% (95%: −0.7% to +0.6%); STEADY | 149.5 → 147.1; raw −1.6% (95%: −8.7% to +5.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 172.8 | 172.8 | 172.8 → 172.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.7 → 172.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 165.8 → 165.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,403 | 2,450 | 2403 → 2450; raw +1.9% (95%: −10.6% to +14.5%); LOSS | 2455 → 2479; raw +1.0% (95%: −8.2% to +10.2%); LOSS | 1208 → 1905; raw +57.7% (95%: −186.1% to +301.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,767 | 3,826 | 3767 → 3826; raw +1.6% (95%: −6.8% to +9.9%); LOSS | 3856 → 3813; raw −1.1% (95%: −11.6% to +9.4%); GAIN | 2155 → 3126; raw +45.1% (95%: −139.9% to +230.0%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 11.5 | 11.5 | 11.47 → 11.47; raw ±0.0% (95%: −0.6% to +0.6%); STEADY | 11.67 → 11.69; raw +0.2% (95%: −0.4% to +0.8%); STEADY | 11.09 → 11.06; raw −0.3% (95%: −1.4% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| end-to-end latency, mean (ms) | 324.8 | 331.4 | 324.8 → 331.4; raw +2.0% (95%: −1.3% to +5.4%); LOSS | 332.6 → 334.2; raw +0.5% (95%: −8.4% to +9.3%); STEADY | 149.8 → 232.1; raw +54.9% (95%: −173.5% to +283.3%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 693.3 | 691.3 | 693.3 → 691.3; raw −0.3% (95%: −7.3% to +6.7%); STEADY | 705.7 → 703.3; raw −0.3% (95%: −10.2% to +9.5%); STEADY | 441.7 → 596.7; raw +35.1% (95%: −103.3% to +173.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 59.6 | 60.6 | 59.58 → 60.6; raw +1.7% (95%: −4.9% to +8.3%); LOSS | 60.92 → 61.18; raw +0.4% (95%: −7.6% to +8.4%); STEADY | 27.37 → 41.19; raw +50.5% (95%: −160.2% to +261.2%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.19; raw +9.5% (95%: −16.5% to +35.5%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.283 | 0.284 | 0.2834 → 0.2836; raw +0.1% (95%: −3.0% to +3.1%), +0.0002 in the gauge's unit; STEADY | 0.287 → 0.2875; raw +0.2% (95%: −1.5% to +1.9%), +0.0005 in the gauge's unit; STEADY | 0.2661 → 0.2633; raw −1.1% (95%: −1.5% to −0.6%), −0.0029 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.28%) |
| host CPU-seconds | 508.4 | 508.7 | 508.4 → 508.7; raw ±0.0% (95%: −3.0% to +3.1%); STEADY | 506.3 → 507.4; raw +0.2% (95%: −1.5% to +1.9%); STEADY | 477 → 471.9; raw −1.1% (95%: −1.6% to −0.6%); GAIN | STEADY, under the floor (the three runs' mean 0.27%) |
| host CPU-seconds per 1,000 messages inside the line | 7.67 | 7.69 | 7.668 → 7.686; raw +0.2% (95%: −2.5% to +3.0%); STEADY | 7.646 → 7.668; raw +0.3% (95%: −0.7% to +1.3%); STEADY | 7.079 → 7.12; raw +0.6% (95%: −7.3% to +8.4%); power given | STEADY, under the floor (the three runs' mean 0.37%) |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 7.333; raw +266.7% (95%: +123.2% to +410.1%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,933, 1,940, 1,953 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726.5 | 724.5 | 726.5 → 724.5; raw −0.3% (95%: −0.5% to −0.1%); STEADY | 725.9 → 726.5; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 732.7 → 732.7; raw ±0.0% (95%: −1.1% to +1.1%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| throughput (messages a second consumed) | 850.3 | 850.3 | 850.3 → 850.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 853.2 → 853.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 858.6 → 858.9; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,329 | 2,315 | 2329 → 2315; raw −0.6% (95%: −13.4% to +12.2%); GAIN | 2500 → 2413; raw −3.5% (95%: −10.7% to +3.8%); GAIN | 2351 → 2299; raw −2.2% (95%: −14.1% to +9.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,574 | 3,725 | 3574 → 3725; raw +4.2% (95%: +2.0% to +6.5%); LOSS | 3869 → 3808; raw −1.6% (95%: −11.8% to +8.6%); GAIN | 3734 → 3630; raw −2.8% (95%: −12.6% to +7.0%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 8.38 | 7.94 | 8.376 → 7.937; raw −5.2% (95%: −11.1% to +0.6%); GAIN | 8.34 → 8.298; raw −0.5% (95%: −7.6% to +6.6%); GAIN | 9.326 → 10.4; raw +11.5% (95%: −80.3% to +103.2%); LOSS | **the runs disagree** |
| end-to-end latency, mean (ms) | 312.6 | 315.7 | 312.6 → 315.7; raw +1.0% (95%: −3.7% to +5.6%); LOSS | 337.4 → 329.6; raw −2.3% (95%: −8.4% to +3.7%); GAIN | 324.5 → 319.4; raw −1.6% (95%: −11.8% to +8.7%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,227 | 3,270 | 3227 → 3270; raw +1.3% (95%: −2.6% to +5.2%); LOSS | 3399 → 3319; raw −2.4% (95%: −5.8% to +1.0%); GAIN | 3341 → 3282; raw −1.8% (95%: −11.6% to +8.1%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 271.9 | 274.4 | 271.9 → 274.4; raw +0.9% (95%: −4.0% to +5.8%); LOSS | 294.7 → 287.3; raw −2.5% (95%: −8.6% to +3.6%); GAIN | 285.7 → 280.9; raw −1.7% (95%: −11.5% to +8.1%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.119; raw +6.0% (95%: −21.2% to +33.1%); power given | 2 → 2.119; raw +6.0% (95%: −21.2% to +33.1%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.326 | 0.325 | 0.3255 → 0.325; raw −0.2% (95%: −3.0% to +2.6%), −0.0005 in the gauge's unit; STEADY | 0.3264 → 0.3246; raw −0.5% (95%: −2.8% to +1.7%), −0.0017 in the gauge's unit; GAIN | 0.2807 → 0.2789; raw −0.6% (95%: −3.5% to +2.3%), −0.0018 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.45%) |
| host CPU-seconds | 559.1 | 559.2 | 559.1 → 559.2; raw ±0.0% (95%: −3.3% to +3.4%); STEADY | 560 → 556.9; raw −0.6% (95%: −3.3% to +2.1%); GAIN | 501.9 → 498.5; raw −0.7% (95%: −3.7% to +2.3%); GAIN | STEADY, under the floor (the three runs' mean 0.40%) |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.71 | 1.709 → 1.715; raw +0.3% (95%: −3.1% to +3.8%); STEADY | 1.714 → 1.703; raw −0.6% (95%: −3.5% to +2.2%); GAIN | 1.521 → 1.511; raw −0.6% (95%: −4.4% to +3.2%); GAIN | STEADY, under the floor (the three runs' mean 0.32%) |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 8 gauge-rows GAIN, 5 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 16 STEADY, 9 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
