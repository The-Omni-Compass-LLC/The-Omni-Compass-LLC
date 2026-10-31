# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40005908588 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40022521256 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40037209884 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 973, 973, 972 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.0 | 365.3 | 366 → 365.3; raw −0.2% (95%: −1.1% to +0.7%); STEADY | 366 → 365.3; raw −0.2% (95%: −0.3% to ±0.0%); STEADY | 365.2 → 364.9; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.16%) |
| throughput (messages a second consumed) | 427.9 | 427.8 | 427.9 → 427.8; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 427.8 → 427.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 427.5 → 427.7; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,239 | 2,235 | 2239 → 2235; raw −0.1% (95%: −10.0% to +9.7%); STEADY | 2300 → 2267; raw −1.4% (95%: −6.2% to +3.4%); GAIN | 2282 → 2294; raw +0.5% (95%: −2.3% to +3.4%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,580 | 3,627 | 3580 → 3627; raw +1.3% (95%: −9.1% to +11.7%); LOSS | 3469 → 3620; raw +4.3% (95%: −10.9% to +19.6%); LOSS | 3628 → 3637; raw +0.2% (95%: −9.9% to +10.3%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.34 | 8.27 | 8.336 → 8.27; raw −0.8% (95%: −1.5% to ±0.0%); GAIN | 8.414 → 8.536; raw +1.5% (95%: −0.8% to +3.7%); LOSS | 8.587 → 8.64; raw +0.6% (95%: −2.2% to +3.5%); LOSS | **the runs disagree** |
| end-to-end latency, mean (ms) | 295.1 | 298.5 | 295.1 → 298.5; raw +1.1% (95%: −9.5% to +11.8%); LOSS | 296.2 → 301.3; raw +1.7% (95%: −0.1% to +3.5%); LOSS | 304.2 → 306.8; raw +0.8% (95%: −0.1% to +1.8%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,608 | 1,614 | 1608 → 1614; raw +0.4% (95%: −5.3% to +6.0%); STEADY | 1629 → 1628; raw −0.1% (95%: −2.4% to +2.3%); STEADY | 1644 → 1632; raw −0.7% (95%: −3.3% to +1.9%); GAIN | STEADY, under the floor (the three runs' mean 0.15%) |
| consumer lag, mean messages waiting | 129.9 | 131.4 | 129.9 → 131.4; raw +1.2% (95%: −8.7% to +11.0%); LOSS | 130.3 → 132.5; raw +1.7% (95%: +0.2% to +3.1%); LOSS | 134.1 → 135.6; raw +1.1% (95%: −0.7% to +2.9%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | 2 → 2.119; raw +6.0% (95%: −21.2% to +33.1%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2.33 | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.31 | 0.308 | 0.3098 → 0.3083; raw −0.5% (95%: −1.2% to +0.2%), −0.0015 in the gauge's unit; STEADY | 0.3172 → 0.3276; raw +3.3% (95%: −2.8% to +9.3%), +0.0104 in the gauge's unit; power given | 0.3114 → 0.3136; raw +0.7% (95%: −0.6% to +2.0%), +0.0022 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 553.1 | 551.4 | 553.1 → 551.4; raw −0.3% (95%: −1.0% to +0.4%); STEADY | 564.6 → 583; raw +3.3% (95%: −2.7% to +9.2%); power given | 541 → 544.2; raw +0.6% (95%: −0.7% to +1.9%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.35 | 3.357 → 3.352; raw −0.1% (95%: −1.4% to +1.1%); STEADY | 3.427 → 3.546; raw +3.5% (95%: −2.5% to +9.5%); power given | 3.29 → 3.313; raw +0.7% (95%: −0.7% to +2.2%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4.67 | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 968, 948, 983 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 338.6 | 363.8 | 338.6 → 363.8; raw +7.4% (95%: −22.2% to +37.1%); GAIN | 336.1 → 336.1; raw ±0.0% (95%: −3.2% to +3.1%); STEADY | 343.1 → 342; raw −0.3% (95%: −0.9% to +0.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 416.1 | 416.1 | 416.1 → 416.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 407.2 → 407.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 422.3 → 422.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,508 | 1,592 | 2508 → 1592; raw −36.5% (95%: −153.5% to +80.4%); GAIN | 2043 → 2661; raw +30.3% (95%: −90.8% to +151.4%); LOSS | 2550 → 2550; raw ±0.0% (95%: −5.3% to +5.4%); STEADY | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,822 | 2,548 | 3822 → 2548; raw −33.3% (95%: −128.9% to +62.2%); GAIN | 2890 → 3716; raw +28.6% (95%: −60.1% to +117.3%); LOSS | 3909 → 3947; raw +1.0% (95%: −9.1% to +11.1%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 8.66 | 8.46 | 8.665 → 8.462; raw −2.3% (95%: −11.5% to +6.9%); GAIN | 8.796 → 8.704; raw −1.0% (95%: −6.5% to +4.4%); GAIN | 19.94 → 18.21; raw −8.7% (95%: −153.5% to +136.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 381.1 | 244.4 | 381.1 → 244.4; raw −35.9% (95%: −142.3% to +70.6%); GAIN | 304.4 → 375.5; raw +23.3% (95%: −54.4% to +101.1%); LOSS | 403.9 → 408.2; raw +1.1% (95%: −1.3% to +3.4%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,622 | 1,179 | 1622 → 1179; raw −27.3% (95%: −108.3% to +53.7%); GAIN | 1274 → 1568; raw +23.0% (95%: −61.8% to +107.9%); LOSS | 1722 → 1716; raw −0.3% (95%: −3.4% to +2.8%); STEADY | **the runs disagree** |
| consumer lag, mean messages waiting | 163.5 | 105.2 | 163.5 → 105.2; raw −35.6% (95%: −140.9% to +69.7%); GAIN | 128.2 → 157.5; raw +22.9% (95%: −53.5% to +99.2%); LOSS | 176.4 → 179.2; raw +1.6% (95%: −2.3% to +5.5%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | 2 → 2.245; raw +12.3% (95%: −44.1% to +68.6%); power given | 2 → 1.985; raw −0.7% (95%: −1.1% to −0.3%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **the runs disagree** |
| consumers running, most at once | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −110.1% to +176.8%); power given | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.293 | 0.293 | 0.2929 → 0.2933; raw +0.1% (95%: −1.2% to +1.5%), +0.0004 in the gauge's unit; STEADY | 0.285 → 0.2907; raw +2.0% (95%: −5.0% to +9.0%), +0.0057 in the gauge's unit; power given | 0.2595 → 0.2591; raw −0.2% (95%: −3.6% to +3.2%), −0.0004 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 210.0 | 210.3 | 210 → 210.3; raw +0.2% (95%: −1.3% to +1.6%); STEADY | 204.2 → 208.4; raw +2.0% (95%: −4.8% to +8.9%); power given | 186.5 → 186.2; raw −0.2% (95%: −3.5% to +3.2%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.23 | 3.432 → 3.226; raw −6.0% (95%: −31.3% to +19.3%); GAIN | 3.363 → 3.431; raw +2.0% (95%: −4.0% to +8.0%); power given | 3.008 → 3.013; raw +0.2% (95%: −3.0% to +3.3%); STEADY | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 5.33 | 2 → 5.333; raw +166.7% (95%: −120.2% to +453.5%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 393, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.8 | 147.1 → 146.8; raw −0.2% (95%: −0.8% to +0.4%); STEADY | 147 → 147; raw ±0.0% (95%: −0.6% to +0.7%); STEADY | 146.7 → 146.9; raw +0.1% (95%: −0.1% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (messages a second consumed) | 173.2 | 173.2 | 173.2 → 173.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.9 → 172.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.5 → 172.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,546 | 2,550 | 2546 → 2550; raw +0.1% (95%: −2.9% to +3.2%); STEADY | 2495 → 2449; raw −1.9% (95%: −12.9% to +9.2%); GAIN | 2448 → 2354; raw −3.9% (95%: −11.5% to +3.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,841 | 3,955 | 3841 → 3955; raw +3.0% (95%: −7.3% to +13.3%); LOSS | 3752 → 3775; raw +0.6% (95%: −11.0% to +12.2%); LOSS | 3816 → 3737; raw −2.1% (95%: −8.2% to +4.1%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 11.7 | 11.6 | 11.68 → 11.65; raw −0.3% (95%: −1.0% to +0.4%); STEADY | 11.62 → 11.6; raw −0.2% (95%: −0.8% to +0.4%); STEADY | 11.61 → 11.61; raw ±0.0% (95%: −1.1% to +1.1%); STEADY | STEADY, under the floor (the three runs' mean 0.17%) |
| end-to-end latency, mean (ms) | 341.2 | 348.3 | 341.2 → 348.3; raw +2.1% (95%: −6.1% to +10.3%); LOSS | 335.2 → 330.7; raw −1.3% (95%: −10.7% to +8.0%); GAIN | 334.2 → 322.3; raw −3.6% (95%: −6.4% to −0.7%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 711.3 | 732.0 | 711.3 → 732; raw +2.9% (95%: −1.5% to +7.3%); LOSS | 706 → 712.3; raw +0.9% (95%: −7.2% to +9.0%); LOSS | 705.7 → 690.3; raw −2.2% (95%: −6.8% to +2.4%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 62.5 | 63.5 | 62.46 → 63.46; raw +1.6% (95%: −5.5% to +8.8%); LOSS | 61.44 → 60.59; raw −1.4% (95%: −11.9% to +9.2%); GAIN | 61.4 → 59.15; raw −3.7% (95%: −5.9% to −1.5%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.289 | 0.284 | 0.2889 → 0.2843; raw −1.6% (95%: −4.7% to +1.4%), −0.0047 in the gauge's unit; GAIN | 0.2834 → 0.2807; raw −0.9% (95%: −4.4% to +2.5%), −0.0026 in the gauge's unit; GAIN | 0.2827 → 0.2815; raw −0.4% (95%: −4.6% to +3.8%), −0.0011 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 509.1 | 500.9 | 509.1 → 500.9; raw −1.6% (95%: −4.7% to +1.4%); GAIN | 499 → 494.1; raw −1.0% (95%: −4.5% to +2.5%); GAIN | 498.5 → 496.2; raw −0.5% (95%: −4.8% to +3.9%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.69 | 7.58 | 7.686 → 7.579; raw −1.4% (95%: −4.9% to +2.1%); GAIN | 7.541 → 7.465; raw −1.0% (95%: −4.9% to +2.9%); GAIN | 7.54 → 7.496; raw −0.6% (95%: −4.9% to +3.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,927, 1,907, 1,963 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724.2 | 724.4 | 724.2 → 724.4; raw ±0.0% (95%: −0.7% to +0.8%); STEADY | 731.3 → 731.7; raw ±0.0% (95%: −0.9% to +1.0%); STEADY | 732.9 → 731.7; raw −0.2% (95%: −0.8% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| throughput (messages a second consumed) | 847.7 | 847.8 | 847.7 → 847.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 838.9 → 838.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 863.6 → 863.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,269 | 2,236 | 2269 → 2236; raw −1.4% (95%: −9.3% to +6.4%); GAIN | 1802 → 1801; raw −0.1% (95%: −4.0% to +3.8%); STEADY | 2641 → 2644; raw +0.1% (95%: −10.5% to +10.7%); STEADY | STEADY, under the floor (the three runs' mean 0.48%) |
| end-to-end latency, 99th percentile (ms) | 3,636 | 3,542 | 3636 → 3542; raw −2.6% (95%: −4.9% to −0.2%); GAIN | 3025 → 2971; raw −1.8% (95%: −9.2% to +5.7%); GAIN | 4061 → 4011; raw −1.2% (95%: −7.3% to +4.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, median (ms) | 8.13 | 8.11 | 8.135 → 8.106; raw −0.4% (95%: −10.8% to +10.1%); STEADY | 7.291 → 7.195; raw −1.3% (95%: −2.5% to −0.2%); GAIN | 8.91 → 8.236; raw −7.6% (95%: −11.4% to −3.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| end-to-end latency, mean (ms) | 306.2 | 301.7 | 306.2 → 301.7; raw −1.5% (95%: −8.4% to +5.5%); GAIN | 230.8 → 228.1; raw −1.2% (95%: −10.3% to +8.0%); GAIN | 362.1 → 362.6; raw +0.1% (95%: −10.9% to +11.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,259 | 3,170 | 3259 → 3170; raw −2.8% (95%: −7.6% to +2.1%); GAIN | 2770 → 2733; raw −1.3% (95%: −5.3% to +2.6%); GAIN | 3609 → 3582; raw −0.8% (95%: −5.6% to +4.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 265.7 | 261.4 | 265.7 → 261.4; raw −1.6% (95%: −9.1% to +5.8%); GAIN | 197.4 → 194.6; raw −1.5% (95%: −9.8% to +6.9%); GAIN | 320.8 → 319.9; raw −0.3% (95%: −10.7% to +10.1%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | 2 → 2.249; raw +12.4% (95%: −15.0% to +39.9%); power given | 2 → 2.26; raw +13.0% (95%: −15.7% to +41.6%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.347 | 0.337 | 0.3465 → 0.3372; raw −2.7% (95%: −9.9% to +4.5%), −0.0093 in the gauge's unit; GAIN | 0.3347 → 0.3336; raw −0.3% (95%: −5.9% to +5.3%), −0.0010 in the gauge's unit; STEADY | 0.2987 → 0.321; raw +7.5% (95%: −5.7% to +20.6%), +0.0223 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 595.6 | 580.1 | 595.6 → 580.1; raw −2.6% (95%: −10.6% to +5.4%); GAIN | 595.9 → 594.9; raw −0.2% (95%: −5.7% to +5.4%); STEADY | 532.6 → 571.5; raw +7.3% (95%: −5.6% to +20.2%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.83 | 1.78 | 1.827 → 1.779; raw −2.6% (95%: −11.4% to +6.1%); GAIN | 1.81 → 1.806; raw −0.2% (95%: −6.7% to +6.2%); STEADY | 1.614 → 1.735; raw +7.5% (95%: −5.7% to +20.6%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 5.33 | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 0 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 12 STEADY, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
