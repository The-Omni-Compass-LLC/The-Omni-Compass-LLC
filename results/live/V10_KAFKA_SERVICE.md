# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39109170592 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| B | 39116292836 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| C | 39124642737 | `8b902df8d857` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 977, 973, 975 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.4 | 365.6 | 366.4 → 365.6; raw −0.2% (95%: −0.8% to +0.3%); STEADY | 365.2 → 365.1; raw ±0.0% (95%: −0.5% to +0.4%); STEADY | 365.8 → 365; raw −0.2% (95%: −1.2% to +0.8%); STEADY | STEADY, under the floor (the three runs' mean 0.15%) |
| throughput (messages a second consumed) | 429.6 | 429.6 | 429.6 → 429.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 428.2 → 428; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 428.8 → 428.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,398 | 2,447 | 2398 → 2447; raw +2.0% (95%: −2.9% to +6.9%); LOSS | 2343 → 2309; raw −1.5% (95%: −10.3% to +7.4%); GAIN | 2348 → 2363; raw +0.6% (95%: −13.0% to +14.3%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,688 | 3,753 | 3688 → 3753; raw +1.8% (95%: −9.8% to +13.3%); LOSS | 3672 → 3662; raw −0.3% (95%: −7.6% to +7.0%); STEADY | 3731 → 3783; raw +1.4% (95%: −3.0% to +5.8%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.44 | 8.43 | 8.436 → 8.426; raw −0.1% (95%: −0.8% to +0.5%); STEADY | 8.554 → 8.526; raw −0.3% (95%: −0.9% to +0.2%); STEADY | 8.581 → 8.572; raw −0.1% (95%: −2.0% to +1.8%); STEADY | STEADY, under the floor (the three runs' mean 0.19%) |
| end-to-end latency, mean (ms) | 319.8 | 324.3 | 319.8 → 324.3; raw +1.4% (95%: −5.1% to +7.9%); LOSS | 313.9 → 311.7; raw −0.7% (95%: −6.6% to +5.3%); GAIN | 315.6 → 321.4; raw +1.8% (95%: −8.5% to +12.2%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,701 | 1,708 | 1701 → 1708; raw +0.4% (95%: −6.8% to +7.6%); STEADY | 1688 → 1667; raw −1.3% (95%: −7.6% to +5.1%); GAIN | 1671 → 1683; raw +0.7% (95%: −4.9% to +6.3%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 141.3 | 143.0 | 141.3 → 143; raw +1.2% (95%: −4.9% to +7.4%); LOSS | 138.6 → 137.4; raw −0.9% (95%: −7.1% to +5.3%); GAIN | 140 → 142.1; raw +1.5% (95%: −8.6% to +11.6%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.315 | 0.313 | 0.3146 → 0.3132; raw −0.5% (95%: −3.5% to +2.6%), −0.0014 in the gauge's unit; STEADY | 0.3084 → 0.3074; raw −0.3% (95%: −3.2% to +2.6%), −0.0009 in the gauge's unit; STEADY | 0.3114 → 0.3093; raw −0.7% (95%: −2.7% to +1.3%), −0.0021 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.48%) |
| host CPU-seconds | 559.3 | 557.4 | 559.3 → 557.4; raw −0.4% (95%: −3.7% to +3.0%); STEADY | 535.7 → 535.5; raw ±0.0% (95%: −3.2% to +3.1%); STEADY | 540.9 → 537; raw −0.7% (95%: −3.0% to +1.6%); GAIN | STEADY, under the floor (the three runs' mean 0.37%) |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 3.39 | 3.391 → 3.387; raw −0.1% (95%: −4.0% to +3.7%); STEADY | 3.259 → 3.257; raw −0.1% (95%: −2.6% to +2.5%); STEADY | 3.284 → 3.268; raw −0.5% (95%: −3.7% to +2.6%); GAIN | STEADY, under the floor (the three runs' mean 0.23%) |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 980, 972, 977 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343.0 | 342.2 | 343 → 342.2; raw −0.2% (95%: −0.6% to +0.1%); STEADY | 340.4 → 337.4; raw −0.9% (95%: −1.8% to +0.1%); LOSS | 340.9 → 340.4; raw −0.1% (95%: −0.5% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.42%) |
| throughput (messages a second consumed) | 421.0 | 421.0 | 421 → 421; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 417.8 → 417.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 419.6 → 419.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,542 | 2,570 | 2542 → 2570; raw +1.1% (95%: −5.0% to +7.2%); LOSS | 2477 → 2548; raw +2.9% (95%: −3.2% to +8.9%); LOSS | 2642 → 2585; raw −2.2% (95%: −4.4% to ±0.0%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,618 | 3,615 | 3618 → 3615; raw −0.1% (95%: −12.7% to +12.5%); STEADY | 3616 → 3787; raw +4.7% (95%: −8.9% to +18.3%); LOSS | 3769 → 3692; raw −2.0% (95%: −17.4% to +13.4%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 9.65 | 9.5 | 9.647 → 9.501; raw −1.5% (95%: −16.1% to +13.1%); GAIN | 9.754 → 9.527; raw −2.3% (95%: −9.9% to +5.3%); GAIN | 9.498 → 9.373; raw −1.3% (95%: −6.2% to +3.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 384.2 | 388.1 | 384.2 → 388.1; raw +1.0% (95%: −0.8% to +2.8%); LOSS | 377.4 → 393.3; raw +4.2% (95%: −2.9% to +11.4%); LOSS | 390.6 → 390.7; raw ±0.0% (95%: −1.7% to +1.8%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,672 | 1,654 | 1672 → 1654; raw −1.1% (95%: −5.4% to +3.1%); GAIN | 1628 → 1651; raw +1.4% (95%: −1.8% to +4.7%); LOSS | 1682 → 1676; raw −0.3% (95%: −0.9% to +0.3%); STEADY | **the runs disagree** |
| consumer lag, mean messages waiting | 168.3 | 169.6 | 168.3 → 169.6; raw +0.8% (95%: −1.8% to +3.4%); LOSS | 164.2 → 169; raw +2.9% (95%: −3.7% to +9.5%); LOSS | 169.3 → 170; raw +0.4% (95%: −1.6% to +2.4%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.271 | 0.267 | 0.2708 → 0.2674; raw −1.3% (95%: −9.0% to +6.5%), −0.0034 in the gauge's unit; GAIN | 0.3109 → 0.3047; raw −2.0% (95%: −9.7% to +5.7%), −0.0062 in the gauge's unit; GAIN | 0.2943 → 0.2927; raw −0.5% (95%: −2.8% to +1.7%), −0.0016 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 194.4 | 192.0 | 194.4 → 192; raw −1.2% (95%: −9.0% to +6.5%); GAIN | 217.7 → 213.5; raw −1.9% (95%: −9.7% to +5.8%); GAIN | 205.9 → 204.8; raw −0.6% (95%: −2.6% to +1.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.14 | 3.11 | 3.138 → 3.107; raw −1.0% (95%: −8.8% to +6.8%); GAIN | 3.54 → 3.502; raw −1.1% (95%: −8.8% to +6.7%); GAIN | 3.343 → 3.329; raw −0.4% (95%: −2.5% to +1.6%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 393, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.0 | 146.8 | 147 → 146.8; raw −0.1% (95%: −0.7% to +0.5%); STEADY | 146.8 → 146.7; raw −0.1% (95%: −1.0% to +0.9%); STEADY | 147 → 147.1; raw +0.1% (95%: −0.3% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| throughput (messages a second consumed) | 172.9 | 172.9 | 172.9 → 172.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.5 → 172.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.7 → 172.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,528 | 2,515 | 2528 → 2515; raw −0.5% (95%: −8.4% to +7.4%); GAIN | 2411 → 2407; raw −0.2% (95%: −9.3% to +9.0%); STEADY | 2375 → 2382; raw +0.3% (95%: −3.8% to +4.5%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| end-to-end latency, 99th percentile (ms) | 3,813 | 3,816 | 3813 → 3816; raw +0.1% (95%: −1.4% to +1.5%); STEADY | 3730 → 3778; raw +1.3% (95%: −14.2% to +16.7%); LOSS | 3793 → 3651; raw −3.7% (95%: −15.4% to +8.0%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 11.5 | 11.5 | 11.54 → 11.53; raw −0.1% (95%: −0.7% to +0.4%); STEADY | 11.64 → 11.62; raw −0.1% (95%: −1.0% to +0.8%); STEADY | 11.3 → 11.22; raw −0.7% (95%: −2.3% to +1.0%); GAIN | STEADY, under the floor (the three runs' mean 0.30%) |
| end-to-end latency, mean (ms) | 340.2 | 340.3 | 340.2 → 340.3; raw +0.1% (95%: −5.4% to +5.5%); STEADY | 326 → 327.2; raw +0.4% (95%: −10.4% to +11.1%); STEADY | 323.1 → 316.6; raw −2.0% (95%: −8.5% to +4.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 719.0 | 718.0 | 719 → 718; raw −0.1% (95%: −7.4% to +7.1%); STEADY | 707.7 → 694; raw −1.9% (95%: −11.3% to +7.5%); GAIN | 704 → 688; raw −2.3% (95%: −3.2% to −1.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| consumer lag, mean messages waiting | 62.4 | 62.3 | 62.41 → 62.27; raw −0.2% (95%: −3.9% to +3.4%); STEADY | 59.88 → 59.71; raw −0.3% (95%: −10.1% to +9.6%); STEADY | 59.14 → 58.44; raw −1.2% (95%: −8.3% to +5.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.28 | 0.278 | 0.2798 → 0.2784; raw −0.5% (95%: −3.5% to +2.5%), −0.0014 in the gauge's unit; STEADY | 0.2835 → 0.2818; raw −0.6% (95%: −3.4% to +2.2%), −0.0017 in the gauge's unit; GAIN | 0.2758 → 0.2731; raw −1.0% (95%: −3.7% to +1.8%), −0.0027 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 493.1 | 490.7 | 493.1 → 490.7; raw −0.5% (95%: −3.5% to +2.5%); STEADY | 499.8 → 496.8; raw −0.6% (95%: −3.4% to +2.2%); GAIN | 493.7 → 489; raw −1.0% (95%: −3.7% to +1.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.44 | 7.41 | 7.444 → 7.415; raw −0.4% (95%: −3.6% to +2.8%); STEADY | 7.554 → 7.514; raw −0.5% (95%: −3.4% to +2.4%); GAIN | 7.46 → 7.383; raw −1.0% (95%: −3.6% to +1.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,917, 1,930, 1,938 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729.2 | 728.1 | 729.2 → 728.1; raw −0.2% (95%: −0.7% to +0.4%); STEADY | 726 → 723.6; raw −0.3% (95%: −0.7% to ±0.0%); STEADY | 729.3 → 726.9; raw −0.3% (95%: −0.8% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.27%) |
| throughput (messages a second consumed) | 843.3 | 843.3 | 843.3 → 843.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 848.7 → 848.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 852.6 → 852.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 1,971 | 1,943 | 1971 → 1943; raw −1.4% (95%: −8.8% to +5.9%); GAIN | 2291 → 2305; raw +0.6% (95%: −3.4% to +4.6%); LOSS | 2278 → 2310; raw +1.4% (95%: −5.8% to +8.6%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,170 | 3,235 | 3170 → 3235; raw +2.0% (95%: −7.4% to +11.5%); LOSS | 3620 → 3636; raw +0.4% (95%: −6.1% to +7.0%); STEADY | 3529 → 3664; raw +3.8% (95%: +1.5% to +6.1%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, median (ms) | 7.29 | 7.14 | 7.286 → 7.135; raw −2.1% (95%: −7.2% to +3.1%); GAIN | 8.364 → 7.834; raw −6.3% (95%: −16.7% to +4.0%); GAIN | 7.433 → 7.495; raw +0.8% (95%: −2.4% to +4.1%); LOSS | **the runs disagree** |
| end-to-end latency, mean (ms) | 250.9 | 253.4 | 250.9 → 253.4; raw +1.0% (95%: −1.7% to +3.6%); LOSS | 307.3 → 309.9; raw +0.8% (95%: −5.6% to +7.3%); LOSS | 301.2 → 311.9; raw +3.6% (95%: −5.3% to +12.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 2,893 | 2,914 | 2893 → 2914; raw +0.7% (95%: −1.1% to +2.5%); LOSS | 3238 → 3250; raw +0.4% (95%: −2.6% to +3.3%); STEADY | 3211 → 3276; raw +2.0% (95%: −3.7% to +7.8%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 215.6 | 216.9 | 215.6 → 216.9; raw +0.6% (95%: −2.9% to +4.1%); LOSS | 267 → 268; raw +0.4% (95%: −5.9% to +6.6%); STEADY | 261.9 → 272; raw +3.9% (95%: −5.0% to +12.7%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.39 | 2 → 2.386; raw +19.3% (95%: +19.2% to +19.5%); power given | 2 → 2.247; raw +12.4% (95%: −14.9% to +39.6%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 3 | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.332 | 0.334 | 0.3322 → 0.334; raw +0.6% (95%: −0.9% to +2.1%), +0.0019 in the gauge's unit; power given | 0.3345 → 0.3371; raw +0.8% (95%: −1.6% to +3.1%), +0.0026 in the gauge's unit; power given | 0.3149 → 0.3129; raw −0.6% (95%: −3.3% to +2.0%), −0.0020 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 591.8 | 595.8 | 591.8 → 595.8; raw +0.7% (95%: −1.1% to +2.4%); power given | 574.2 → 580.9; raw +1.2% (95%: −1.5% to +3.9%); power given | 560.4 → 557.5; raw −0.5% (95%: −2.7% to +1.7%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.82 | 1.803 → 1.818; raw +0.8% (95%: −0.9% to +2.6%); power given | 1.757 → 1.783; raw +1.5% (95%: −1.0% to +4.0%); power given | 1.707 → 1.704; raw −0.2% (95%: −2.3% to +1.9%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 6 | 2 → 6; raw +200.0% (95%: +200.0% to +200.0%) | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 6 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 8 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
