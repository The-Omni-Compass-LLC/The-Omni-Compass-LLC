# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39108188053 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| B | 39116273889 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| C | 39123591485 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 974, 970, 982 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.7 | 364.8 | 365.7 → 364.8; raw −0.2% (95%: −0.6% to +0.1%); STEADY | 365.1 → 364.5; raw −0.2% (95%: −0.8% to +0.5%); STEADY | 368 → 367.2; raw −0.2% (95%: −0.8% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.21%) |
| throughput (messages a second consumed) | 428.5 | 428.5 | 428.5 → 428.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 426.8 → 426.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 432 → 431.8; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,346 | 2,387 | 2346 → 2387; raw +1.7% (95%: −2.5% to +6.0%); LOSS | 2214 → 2236; raw +1.0% (95%: −1.2% to +3.3%); LOSS | 2442 → 2476; raw +1.4% (95%: −6.3% to +9.1%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,617 | 3,610 | 3617 → 3610; raw −0.2% (95%: −6.2% to +5.8%); STEADY | 3479 → 3501; raw +0.6% (95%: −13.1% to +14.4%); LOSS | 3746 → 3782; raw +1.0% (95%: −12.6% to +14.5%); LOSS | STEADY, under the floor (the three runs' mean 0.47%) |
| end-to-end latency, median (ms) | 8.56 | 8.5 | 8.556 → 8.502; raw −0.6% (95%: −2.2% to +0.9%); GAIN | 8.569 → 8.558; raw −0.1% (95%: −0.5% to +0.3%); STEADY | 7.889 → 7.906; raw +0.2% (95%: −1.4% to +1.9%); STEADY | STEADY, under the floor (the three runs' mean 0.19%) |
| end-to-end latency, mean (ms) | 313.2 | 316.8 | 313.2 → 316.8; raw +1.2% (95%: −3.7% to +6.0%); LOSS | 294.2 → 298.8; raw +1.6% (95%: −8.8% to +11.9%); LOSS | 322.1 → 327; raw +1.5% (95%: −9.7% to +12.7%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,668 | 1,670 | 1668 → 1670; raw +0.1% (95%: −3.6% to +3.9%); STEADY | 1599 → 1609; raw +0.6% (95%: −2.1% to +3.3%); LOSS | 1710 → 1721; raw +0.6% (95%: −4.0% to +5.2%); LOSS | STEADY, under the floor (the three runs' mean 0.46%) |
| consumer lag, mean messages waiting | 139.0 | 140.4 | 139 → 140.4; raw +1.0% (95%: −3.2% to +5.2%); LOSS | 129.7 → 131.3; raw +1.3% (95%: −9.1% to +11.6%); LOSS | 143.3 → 144.9; raw +1.2% (95%: −10.2% to +12.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.307 | 0.306 | 0.3068 → 0.3055; raw −0.4% (95%: −3.1% to +2.2%), −0.0013 in the gauge's unit; STEADY | 0.3121 → 0.3101; raw −0.6% (95%: −4.6% to +3.3%), −0.0020 in the gauge's unit; GAIN | 0.2845 → 0.283; raw −0.6% (95%: −2.6% to +1.5%), −0.0016 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 532.1 | 531.7 | 532.1 → 531.7; raw −0.1% (95%: −3.1% to +2.9%); STEADY | 541.2 → 539.1; raw −0.4% (95%: −5.0% to +4.2%); STEADY | 510.2 → 507.2; raw −0.6% (95%: −2.9% to +1.7%); GAIN | STEADY, under the floor (the three runs' mean 0.36%) |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.24 | 3.232 → 3.237; raw +0.2% (95%: −2.5% to +2.8%); STEADY | 3.293 → 3.285; raw −0.2% (95%: −4.2% to +3.8%); STEADY | 3.079 → 3.066; raw −0.4% (95%: −2.4% to +1.5%); STEADY | STEADY, under the floor (the three runs' mean 0.16%) |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 975, 965 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341.0 | 339.3 | 341 → 339.3; raw −0.5% (95%: −0.9% to −0.1%); LOSS | 340.2 → 340.3; raw ±0.0% (95%: −0.6% to +0.7%); STEADY | 340 → 339.1; raw −0.3% (95%: −0.5% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.25%) |
| throughput (messages a second consumed) | 418.7 | 418.7 | 418.7 → 418.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 419 → 419; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 414.8 → 414.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,517 | 2,555 | 2517 → 2555; raw +1.5% (95%: −4.9% to +8.0%); LOSS | 2600 → 2459; raw −5.4% (95%: −6.7% to −4.2%); GAIN | 2232 → 2222; raw −0.4% (95%: −12.4% to +11.5%); STEADY | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,747 | 3,785 | 3747 → 3785; raw +1.0% (95%: −14.2% to +16.2%); LOSS | 3803 → 3913; raw +2.9% (95%: −10.0% to +15.7%); LOSS | 3346 → 3361; raw +0.5% (95%: −12.6% to +13.5%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 9.45 | 9.57 | 9.453 → 9.571; raw +1.2% (95%: −3.3% to +5.8%); LOSS | 9.376 → 9.439; raw +0.7% (95%: −9.4% to +10.8%); LOSS | 8.754 → 8.594; raw −1.8% (95%: −7.2% to +3.5%); GAIN | **the runs disagree** |
| end-to-end latency, mean (ms) | 382.3 | 392.0 | 382.3 → 392; raw +2.5% (95%: −5.4% to +10.5%); LOSS | 388.7 → 386.1; raw −0.7% (95%: −8.7% to +7.3%); GAIN | 335.5 → 337; raw +0.5% (95%: −0.7% to +1.6%); STEADY | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,659 | 1,670 | 1659 → 1670; raw +0.6% (95%: −2.6% to +3.8%); LOSS | 1664 → 1652; raw −0.7% (95%: −5.3% to +3.8%); GAIN | 1472 → 1476; raw +0.3% (95%: −1.4% to +2.0%); STEADY | **the runs disagree** |
| consumer lag, mean messages waiting | 166.3 | 168.8 | 166.3 → 168.8; raw +1.5% (95%: −7.2% to +10.3%); LOSS | 167.7 → 166.5; raw −0.7% (95%: −7.9% to +6.5%); GAIN | 143.8 → 143.9; raw +0.1% (95%: −2.1% to +2.3%); STEADY | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.297 | 0.294 | 0.297 → 0.2936; raw −1.1% (95%: −8.1% to +5.9%), −0.0033 in the gauge's unit; GAIN | 0.2949 → 0.2912; raw −1.3% (95%: −7.1% to +4.6%), −0.0037 in the gauge's unit; GAIN | 0.2991 → 0.2956; raw −1.2% (95%: −6.3% to +4.0%), −0.0035 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 207.9 | 205.7 | 207.9 → 205.7; raw −1.1% (95%: −8.2% to +6.1%); GAIN | 206.4 → 203.8; raw −1.3% (95%: −7.0% to +4.5%); GAIN | 214.5 → 212.1; raw −1.1% (95%: −6.3% to +4.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.37 | 3.36 | 3.374 → 3.355; raw −0.6% (95%: −7.3% to +6.2%); GAIN | 3.357 → 3.314; raw −1.3% (95%: −6.7% to +4.2%); GAIN | 3.492 → 3.463; raw −0.8% (95%: −5.9% to +4.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 392, 393, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.2 | 146.9 | 147.2 → 146.9; raw −0.3% (95%: −0.9% to +0.4%); STEADY | 147 → 146.8; raw −0.1% (95%: −0.4% to +0.2%); STEADY | 147.2 → 147; raw −0.1% (95%: −0.6% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.15%) |
| throughput (messages a second consumed) | 172.6 | 172.6 | 172.6 → 172.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.5 → 172.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.7 → 172.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,354 | 2,348 | 2354 → 2348; raw −0.3% (95%: −5.3% to +4.8%); STEADY | 2369 → 2381; raw +0.5% (95%: −4.3% to +5.3%); LOSS | 2323 → 2381; raw +2.5% (95%: −0.4% to +5.4%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,640 | 3,647 | 3640 → 3647; raw +0.2% (95%: −2.2% to +2.6%); STEADY | 3741 → 3759; raw +0.5% (95%: −6.8% to +7.8%); STEADY | 3735 → 3657; raw −2.1% (95%: −7.6% to +3.4%); GAIN | STEADY, under the floor (the three runs' mean 0.47%) |
| end-to-end latency, median (ms) | 11.3 | 11.2 | 11.25 → 11.21; raw −0.3% (95%: −0.9% to +0.2%); STEADY | 11.57 → 11.57; raw ±0.0% (95%: −0.7% to +0.6%); STEADY | 10.87 → 10.73; raw −1.3% (95%: −5.7% to +3.0%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 314.4 | 316.7 | 314.4 → 316.7; raw +0.7% (95%: −2.2% to +3.6%); LOSS | 322.8 → 325.8; raw +0.9% (95%: −2.0% to +3.8%); LOSS | 315.6 → 317.9; raw +0.7% (95%: −2.8% to +4.3%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 687.7 | 680.0 | 687.7 → 680; raw −1.1% (95%: −4.6% to +2.4%); GAIN | 693.3 → 685.7; raw −1.1% (95%: −8.1% to +5.9%); GAIN | 691.7 → 689.7; raw −0.3% (95%: −11.6% to +11.0%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 57.0 | 58.1 | 57 → 58.14; raw +2.0% (95%: −3.9% to +7.9%); LOSS | 58.9 → 59.78; raw +1.5% (95%: +0.8% to +2.2%); LOSS | 58.19 → 58.17; raw ±0.0% (95%: −3.7% to +3.7%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | 2 → 2.011; raw +0.6% (95%: −1.4% to +2.5%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| consumers running, most at once | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.275 | 0.272 | 0.2747 → 0.2723; raw −0.9% (95%: −3.8% to +2.1%), −0.0024 in the gauge's unit; GAIN | 0.2811 → 0.2791; raw −0.7% (95%: −3.8% to +2.3%), −0.0020 in the gauge's unit; GAIN | 0.2607 → 0.2561; raw −1.8% (95%: −6.9% to +3.4%), −0.0046 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 491.8 | 487.6 | 491.8 → 487.6; raw −0.9% (95%: −3.7% to +2.0%); GAIN | 495.5 → 492.2; raw −0.7% (95%: −3.9% to +2.6%); GAIN | 467.6 → 459.4; raw −1.8% (95%: −6.9% to +3.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.38 | 7.42 → 7.375; raw −0.6% (95%: −2.8% to +1.6%); GAIN | 7.48 → 7.438; raw −0.6% (95%: −4.0% to +2.9%); GAIN | 7.05 → 6.934; raw −1.6% (95%: −6.9% to +3.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 5.33 | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,951, 1,934, 1,921 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732.2 | 731.3 | 732.2 → 731.3; raw −0.1% (95%: −0.2% to −0.1%); STEADY | 728.4 → 767.7; raw +5.4% (95%: −18.1% to +28.8%); GAIN | 725.9 → 719.4; raw −0.9% (95%: −2.4% to +0.6%); LOSS | **the runs disagree** |
| throughput (messages a second consumed) | 858.2 | 858.2 | 858.2 → 858.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 850.8 → 850.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 844.9 → 844.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,431 | 2,418 | 2431 → 2418; raw −0.5% (95%: −5.6% to +4.5%); GAIN | 2198 → 1464; raw −33.4% (95%: −163.0% to +96.2%); GAIN | 2098 → 2191; raw +4.4% (95%: +0.9% to +8.0%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,721 | 3,680 | 3721 → 3680; raw −1.1% (95%: −1.9% to −0.3%); GAIN | 3624 → 2514; raw −30.6% (95%: −163.2% to +101.9%); GAIN | 3360 → 3520; raw +4.8% (95%: −4.2% to +13.7%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 8.15 | 8.56 | 8.149 → 8.562; raw +5.1% (95%: −13.1% to +23.2%); LOSS | 7.519 → 7.094; raw −5.7% (95%: −20.2% to +8.9%); GAIN | 8.525 → 8.252; raw −3.2% (95%: −14.7% to +8.3%); GAIN | **the runs disagree** |
| end-to-end latency, mean (ms) | 324.9 | 329.0 | 324.9 → 329; raw +1.2% (95%: −2.9% to +5.3%); LOSS | 297.9 → 204; raw −31.5% (95%: −160.2% to +97.1%); GAIN | 283.7 → 301.3; raw +6.2% (95%: −2.4% to +14.8%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,348 | 3,342 | 3348 → 3342; raw −0.2% (95%: −1.2% to +0.9%); STEADY | 3213 → 2253; raw −29.9% (95%: −142.6% to +82.8%); GAIN | 3057 → 3160; raw +3.4% (95%: −2.6% to +9.4%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 286.3 | 288.8 | 286.3 → 288.8; raw +0.9% (95%: −3.1% to +4.9%); LOSS | 259.3 → 177.8; raw −31.4% (95%: −159.4% to +96.5%); GAIN | 246.6 → 261.2; raw +5.9% (95%: −3.5% to +15.3%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.324; raw +16.2% (95%: −22.1% to +54.5%); power given | 2 → 2.125; raw +6.2% (95%: −21.3% to +33.8%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 3; raw +50.0% (95%: −74.2% to +174.2%); power given | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.316 | 0.306 | 0.3165 → 0.3063; raw −3.2% (95%: −12.9% to +6.5%), −0.0101 in the gauge's unit; GAIN | 0.3127 → 0.3156; raw +0.9% (95%: +0.1% to +1.8%), +0.0029 in the gauge's unit; power given | 0.322 → 0.3223; raw +0.1% (95%: −3.7% to +3.9%), +0.0003 in the gauge's unit; STEADY | **the runs disagree** |
| host CPU-seconds | 563.1 | 545.8 | 563.1 → 545.8; raw −3.1% (95%: −12.5% to +6.4%); GAIN | 556.3 → 562.7; raw +1.2% (95%: +0.2% to +2.1%); power given | 552.1 → 553.6; raw +0.3% (95%: −3.4% to +3.9%); STEADY | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.66 | 1.708 → 1.658; raw −3.0% (95%: −12.4% to +6.4%); GAIN | 1.696 → 1.636; raw −3.6% (95%: −25.1% to +18.0%); GAIN | 1.69 → 1.71; raw +1.2% (95%: −2.9% to +5.3%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 6; raw +200.0% (95%: −48.4% to +448.4%) | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 1 refused); left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 9 gauge-rows GAIN, 4 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 11 STEADY, 15 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
