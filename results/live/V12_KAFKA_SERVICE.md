# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39381455200 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| B | 39412428649 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| C | 39461523366 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 976, 974, 978 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.5 | 365.4 | 366.5 → 365.4; raw −0.3% (95%: −0.8% to +0.2%); STEADY | 365.7 → 365; raw −0.2% (95%: −1.0% to +0.6%); STEADY | 367.4 → 366.7; raw −0.2% (95%: −0.8% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.22%) |
| throughput (messages a second consumed) | 428.9 | 428.6 | 428.9 → 428.6; raw −0.1% (95%: −0.2% to +0.1%); STEADY | 428.6 → 428.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 430.1 → 430.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| end-to-end latency, 95th percentile (ms) | 2,296 | 2,310 | 2296 → 2310; raw +0.6% (95%: −0.5% to +1.7%); LOSS | 2343 → 2321; raw −0.9% (95%: −12.4% to +10.5%); GAIN | 2300 → 2311; raw +0.5% (95%: −5.9% to +6.9%); STEADY | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,565 | 3,580 | 3565 → 3580; raw +0.4% (95%: −4.2% to +5.0%); STEADY | 3719 → 3777; raw +1.6% (95%: −5.0% to +8.1%); LOSS | 3621 → 3667; raw +1.3% (95%: −12.9% to +15.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.26 | 8.18 | 8.256 → 8.184; raw −0.9% (95%: −3.3% to +1.6%); GAIN | 8.549 → 8.531; raw −0.2% (95%: −0.5% to +0.1%); STEADY | 8.152 → 8.146; raw −0.1% (95%: −1.4% to +1.3%); STEADY | STEADY, under the floor (the three runs' mean 0.38%) |
| end-to-end latency, mean (ms) | 301.6 | 306.4 | 301.6 → 306.4; raw +1.6% (95%: −6.2% to +9.4%); LOSS | 314.9 → 317.9; raw +1.0% (95%: −8.0% to +9.9%); LOSS | 311.1 → 314.9; raw +1.2% (95%: −7.7% to +10.1%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,626 | 1,643 | 1626 → 1643; raw +1.0% (95%: −2.3% to +4.3%); LOSS | 1677 → 1670; raw −0.4% (95%: −4.1% to +3.3%); STEADY | 1644 → 1674; raw +1.8% (95%: −7.3% to +11.0%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 133.2 | 135.0 | 133.2 → 135; raw +1.3% (95%: −5.9% to +8.5%); LOSS | 139.2 → 140.7; raw +1.1% (95%: −7.4% to +9.5%); LOSS | 139.3 → 139.9; raw +0.4% (95%: −6.4% to +7.3%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | 2 → 2.119; raw +6.0% (95%: −21.2% to +33.1%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2.33 | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.307 | 0.305 | 0.3067 → 0.3051; raw −0.5% (95%: −3.5% to +2.5%), −0.0016 in the gauge's unit; GAIN | 0.3072 → 0.3056; raw −0.5% (95%: −3.5% to +2.5%), −0.0016 in the gauge's unit; GAIN | 0.2798 → 0.2813; raw +0.5% (95%: −5.4% to +6.5%), +0.0015 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 548.5 | 546.7 | 548.5 → 546.7; raw −0.3% (95%: −3.3% to +2.6%); STEADY | 533.6 → 531.1; raw −0.5% (95%: −3.8% to +2.8%); STEADY | 498.7 → 502.1; raw +0.7% (95%: −5.5% to +6.8%); power given | STEADY, under the floor (the three runs' mean 0.04%) |
| host CPU-seconds per 1,000 messages inside the line | 3.32 | 3.32 | 3.323 → 3.32; raw −0.1% (95%: −3.1% to +2.9%); STEADY | 3.241 → 3.232; raw −0.3% (95%: −4.4% to +3.8%); STEADY | 3.016 → 3.041; raw +0.9% (95%: −5.4% to +7.1%); power given | STEADY, under the floor (the three runs' mean 0.16%) |
| consumer changes written (the knob's moves) | 2 | 4.67 | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 976, 964, 969 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341.5 | 340.4 | 341.5 → 340.4; raw −0.3% (95%: −0.6% to −0.1%); STEADY | 338.3 → 338.7; raw +0.1% (95%: −0.8% to +1.0%); STEADY | 340.1 → 337; raw −0.9% (95%: −3.7% to +1.9%); LOSS | STEADY, under the floor (the three runs' mean 0.38%) |
| throughput (messages a second consumed) | 419.2 | 419.2 | 419.2 → 419.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 414.4 → 414.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 416.6 → 416.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,570 | 2,568 | 2570 → 2568; raw −0.1% (95%: −8.5% to +8.3%); STEADY | 2310 → 2332; raw +1.0% (95%: −12.1% to +14.1%); LOSS | 2406 → 2577; raw +7.1% (95%: −1.5% to +15.7%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,694 | 3,744 | 3694 → 3744; raw +1.4% (95%: −5.8% to +8.5%); LOSS | 3508 → 3317; raw −5.5% (95%: −30.4% to +19.5%); GAIN | 3762 → 3788; raw +0.7% (95%: −5.5% to +6.8%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 9.28 | 9.24 | 9.285 → 9.237; raw −0.5% (95%: −5.6% to +4.6%); GAIN | 8.601 → 8.557; raw −0.5% (95%: −4.5% to +3.5%); GAIN | 8.753 → 8.634; raw −1.4% (95%: −6.4% to +3.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 381.4 | 383.6 | 381.4 → 383.6; raw +0.6% (95%: −0.6% to +1.7%); LOSS | 348.6 → 345; raw −1.0% (95%: −12.2% to +10.1%); GAIN | 372.1 → 394.2; raw +5.9% (95%: −2.2% to +14.1%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,651 | 1,663 | 1651 → 1663; raw +0.8% (95%: −2.1% to +3.6%); LOSS | 1537 → 1502; raw −2.3% (95%: −9.9% to +5.3%); GAIN | 1686 → 1665; raw −1.3% (95%: −13.1% to +10.5%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 165.3 | 165.7 | 165.3 → 165.7; raw +0.2% (95%: −2.3% to +2.7%); STEADY | 148.7 → 147.3; raw −0.9% (95%: −10.5% to +8.7%); GAIN | 161.5 → 169.1; raw +4.6% (95%: −5.6% to +14.9%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 2.009; raw +0.5% (95%: −5.1% to +6.0%); STEADY | 2 → 2.103; raw +5.1% (95%: −7.9% to +18.2%); power given | **the runs disagree** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.29 | 0.289 | 0.2904 → 0.2888; raw −0.6% (95%: −6.5% to +5.3%), −0.0017 in the gauge's unit; GAIN | 0.2869 → 0.2831; raw −1.3% (95%: −9.8% to +7.1%), −0.0038 in the gauge's unit; GAIN | 0.2839 → 0.2828; raw −0.4% (95%: −4.7% to +4.0%), −0.0011 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 203.0 | 201.9 | 203 → 201.9; raw −0.6% (95%: −6.6% to +5.5%); GAIN | 205.7 → 203.1; raw −1.2% (95%: −9.6% to +7.1%); GAIN | 203.1 → 202.4; raw −0.4% (95%: −4.7% to +3.9%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.28 | 3.291 → 3.283; raw −0.3% (95%: −6.1% to +5.6%); STEADY | 3.365 → 3.319; raw −1.3% (95%: −8.8% to +6.1%); GAIN | 3.305 → 3.324; raw +0.6% (95%: −0.9% to +2.0%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 6; raw +200.0% (95%: −48.4% to +448.4%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 392, 393, 392 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.2 | 146.9 | 147.2 → 146.9; raw −0.2% (95%: −0.5% to +0.1%); STEADY | 147 → 147.1; raw +0.1% (95%: −0.6% to +0.7%); STEADY | 147.2 → 147; raw −0.1% (95%: −0.4% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.09%) |
| throughput (messages a second consumed) | 172.6 | 172.6 | 172.6 → 172.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.9 → 172.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.5 → 172.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,387 | 2,424 | 2387 → 2424; raw +1.6% (95%: −3.8% to +6.9%); LOSS | 2492 → 2417; raw −3.0% (95%: −5.3% to −0.7%); GAIN | 2321 → 2347; raw +1.1% (95%: −4.0% to +6.3%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,721 | 3,730 | 3721 → 3730; raw +0.2% (95%: −8.2% to +8.7%); STEADY | 3844 → 3749; raw −2.5% (95%: −13.2% to +8.2%); GAIN | 3672 → 3582; raw −2.5% (95%: −7.9% to +3.0%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 11.8 | 11.7 | 11.77 → 11.7; raw −0.6% (95%: −2.4% to +1.2%); GAIN | 11.51 → 11.51; raw ±0.0% (95%: −0.9% to +0.9%); STEADY | 11.59 → 11.51; raw −0.6% (95%: −0.8% to −0.4%); GAIN | STEADY, under the floor (the three runs' mean 0.41%) |
| end-to-end latency, mean (ms) | 321.4 | 325.9 | 321.4 → 325.9; raw +1.4% (95%: −2.8% to +5.6%); LOSS | 334.3 → 329.5; raw −1.5% (95%: −7.9% to +4.9%); GAIN | 311.3 → 312.9; raw +0.5% (95%: −0.8% to +1.8%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 704.0 | 699.3 | 704 → 699.3; raw −0.7% (95%: −8.3% to +6.9%); GAIN | 708.3 → 705; raw −0.5% (95%: −12.9% to +12.0%); STEADY | 666 → 680.3; raw +2.2% (95%: −3.9% to +8.2%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 59.3 | 59.8 | 59.29 → 59.77; raw +0.8% (95%: −2.7% to +4.3%); LOSS | 61.46 → 61.25; raw −0.3% (95%: −4.4% to +3.7%); STEADY | 57.25 → 57.44; raw +0.3% (95%: −0.8% to +1.4%); STEADY | STEADY, under the floor (the three runs' mean 0.26%) |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.292 | 0.287 | 0.292 → 0.2867; raw −1.8% (95%: −7.6% to +4.0%), −0.0053 in the gauge's unit; GAIN | 0.2788 → 0.2766; raw −0.8% (95%: −4.1% to +2.4%), −0.0023 in the gauge's unit; GAIN | 0.2896 → 0.2851; raw −1.5% (95%: −3.5% to +0.4%), −0.0045 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 514.6 | 505.3 | 514.6 → 505.3; raw −1.8% (95%: −7.6% to +4.0%); GAIN | 491.3 → 487.6; raw −0.8% (95%: −4.2% to +2.7%); GAIN | 518.2 → 510.4; raw −1.5% (95%: −3.4% to +0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.77 | 7.64 | 7.768 → 7.642; raw −1.6% (95%: −7.8% to +4.5%); GAIN | 7.418 → 7.357; raw −0.8% (95%: −4.9% to +3.2%); GAIN | 7.82 → 7.713; raw −1.4% (95%: −3.1% to +0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,924, 1,964, 1,932 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725.2 | 764.0 | 725.2 → 764; raw +5.3% (95%: −20.7% to +31.4%); GAIN | 733.7 → 732.6; raw −0.1% (95%: −0.5% to +0.2%); STEADY | 725.4 → 725.1; raw ±0.0% (95%: −0.4% to +0.3%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 846.3 | 846.3 | 846.3 → 846.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 864.1 → 863.8; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 849.5 → 849.8; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,151 | 1,595 | 2151 → 1595; raw −25.9% (95%: −202.1% to +150.3%); GAIN | 2628 → 2569; raw −2.3% (95%: −9.1% to +4.6%); GAIN | 2330 → 2318; raw −0.5% (95%: −1.7% to +0.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,444 | 2,501 | 3444 → 2501; raw −27.4% (95%: −188.8% to +134.1%); GAIN | 3941 → 3974; raw +0.8% (95%: −7.7% to +9.4%); LOSS | 3691 → 3571; raw −3.2% (95%: −8.8% to +2.3%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 7.51 | 7.16 | 7.514 → 7.162; raw −4.7% (95%: −21.0% to +11.6%); GAIN | 7.855 → 7.804; raw −0.7% (95%: −11.4% to +10.1%); GAIN | 7.93 → 7.734; raw −2.5% (95%: −7.5% to +2.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 288.6 | 211.1 | 288.6 → 211.1; raw −26.9% (95%: −200.3% to +146.6%); GAIN | 352.9 → 352.2; raw −0.2% (95%: −4.9% to +4.5%); STEADY | 311.9 → 309.4; raw −0.8% (95%: −5.4% to +3.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,083 | 2,328 | 3083 → 2328; raw −24.5% (95%: −171.8% to +122.8%); GAIN | 3537 → 3545; raw +0.2% (95%: −6.9% to +7.4%); STEADY | 3256 → 3220; raw −1.1% (95%: −3.9% to +1.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 250.4 | 180.9 | 250.4 → 180.9; raw −27.8% (95%: −198.3% to +142.8%); GAIN | 311.2 → 310.4; raw −0.3% (95%: −5.3% to +4.7%); STEADY | 270.4 → 268.3; raw −0.8% (95%: −4.8% to +3.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.43 | 2 → 2.432; raw +21.6% (95%: +7.6% to +35.6%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.119; raw +6.0% (95%: −21.2% to +33.1%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 3 | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.32 | 0.333 | 0.3201 → 0.3332; raw +4.1% (95%: −2.6% to +10.8%), +0.0131 in the gauge's unit; power given | 0.29 → 0.2867; raw −1.1% (95%: −3.1% to +0.9%), −0.0032 in the gauge's unit; GAIN | 0.3459 → 0.3458; raw ±0.0% (95%: −5.6% to +5.5%), −0.0001 in the gauge's unit; STEADY | **the runs disagree** |
| host CPU-seconds | 570.9 | 592.9 | 570.9 → 592.9; raw +3.9% (95%: −2.6% to +10.3%); power given | 516.4 → 511.6; raw −0.9% (95%: −2.9% to +1.1%); GAIN | 600.9 → 601.2; raw +0.1% (95%: −6.1% to +6.3%); STEADY | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.73 | 1.749 → 1.734; raw −0.9% (95%: −25.7% to +24.0%); GAIN | 1.564 → 1.551; raw −0.8% (95%: −2.7% to +1.1%); GAIN | 1.839 → 1.842; raw +0.1% (95%: −6.1% to +6.4%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 6 | 2 → 6; raw +200.0% (95%: +200.0% to +200.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 14 gauge-rows GAIN, 1 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 12 STEADY, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
