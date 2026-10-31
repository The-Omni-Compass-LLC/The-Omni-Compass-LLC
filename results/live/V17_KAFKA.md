# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40003710547 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40020507060 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40035619419 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 972, 977, 964 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.5 | 365.4 | 365.5 → 365.4; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | 366.5 → 365.9; raw −0.2% (95%: −0.6% to +0.3%); STEADY | 367.4 → 366.2; raw −0.3% (95%: −2.2% to +1.6%); STEADY | STEADY, under the floor (the three runs' mean 0.18%) |
| throughput (messages a second consumed) | 427.5 | 427.5 | 427.5 → 427.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 429.9 → 429.7; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 424 → 424; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,255 | 2,227 | 2255 → 2227; raw −1.3% (95%: −7.1% to +4.6%); GAIN | 2357 → 2395; raw +1.6% (95%: −6.4% to +9.6%); LOSS | 1902 → 1938; raw +1.9% (95%: −13.9% to +17.6%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,573 | 3,521 | 3573 → 3521; raw −1.4% (95%: −11.1% to +8.2%); GAIN | 3679 → 3825; raw +4.0% (95%: −7.5% to +15.5%); LOSS | 3127 → 3143; raw +0.5% (95%: −12.2% to +13.3%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 8.62 | 8.58 | 8.617 → 8.575; raw −0.5% (95%: −4.2% to +3.2%); STEADY | 8.214 → 8.182; raw −0.4% (95%: −0.9% to +0.1%); STEADY | 8.177 → 8.113; raw −0.8% (95%: −6.9% to +5.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 302.1 | 298.6 | 302.1 → 298.6; raw −1.1% (95%: −8.1% to +5.8%); GAIN | 315.3 → 321.4; raw +1.9% (95%: −7.3% to +11.2%); LOSS | 245.9 → 250.7; raw +2.0% (95%: −16.6% to +20.6%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,634 | 1,604 | 1634 → 1604; raw −1.8% (95%: −6.0% to +2.3%); GAIN | 1683 → 1681; raw −0.1% (95%: −8.2% to +8.0%); STEADY | 1469 → 1467; raw −0.2% (95%: −10.9% to +10.6%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 133.8 | 132.0 | 133.8 → 132; raw −1.4% (95%: −9.8% to +7.0%); GAIN | 139.5 → 142.1; raw +1.9% (95%: −7.1% to +10.9%); LOSS | 107.8 → 109.6; raw +1.7% (95%: −14.9% to +18.2%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.383; raw +19.1% (95%: +18.9% to +19.4%); power given | **power given by the mean of our three runs, beyond the noise in 3 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.313 | 0.311 | 0.313 → 0.311; raw −0.6% (95%: −11.1% to +9.8%), −0.0020 in the gauge's unit; GAIN | 0.2979 → 0.2956; raw −0.8% (95%: −2.4% to +0.9%), −0.0022 in the gauge's unit; GAIN | 0.2984 → 0.2922; raw −2.1% (95%: −10.8% to +6.6%), −0.0062 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 543.3 | 541.1 | 543.3 → 541.1; raw −0.4% (95%: −10.7% to +9.9%); STEADY | 531.2 → 528.3; raw −0.6% (95%: −2.1% to +1.0%); GAIN | 532.6 → 521.5; raw −2.1% (95%: −10.5% to +6.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 3.29 | 3.301 → 3.289; raw −0.4% (95%: −11.2% to +10.4%); STEADY | 3.22 → 3.206; raw −0.4% (95%: −2.3% to +1.4%); STEADY | 3.22 → 3.164; raw −1.8% (95%: −12.1% to +8.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 6; raw +200.0% (95%: +200.0% to +200.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 975, 976, 973 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341.0 | 340.0 | 341 → 340; raw −0.3% (95%: −0.9% to +0.3%); STEADY | 341 → 341.1; raw ±0.0% (95%: −0.9% to +1.0%); STEADY | 340.5 → 339.3; raw −0.4% (95%: −1.6% to +0.8%); STEADY | STEADY, under the floor (the three runs' mean 0.20%) |
| throughput (messages a second consumed) | 418.9 | 418.9 | 418.9 → 418.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 419.4 → 419.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 418.1 → 418.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,511 | 2,550 | 2511 → 2550; raw +1.6% (95%: −4.3% to +7.4%); LOSS | 2547 → 2529; raw −0.7% (95%: −10.3% to +8.9%); GAIN | 2470 → 2458; raw −0.5% (95%: −5.3% to +4.3%); STEADY | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,874 | 3,687 | 3874 → 3687; raw −4.8% (95%: −13.1% to +3.5%); GAIN | 3688 → 3670; raw −0.5% (95%: −12.0% to +11.0%); STEADY | 3671 → 3655; raw −0.4% (95%: −4.7% to +3.8%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 9.37 | 9.59 | 9.374 → 9.585; raw +2.3% (95%: −2.9% to +7.4%); LOSS | 8.732 → 8.489; raw −2.8% (95%: −11.7% to +6.1%); GAIN | 9.569 → 9.579; raw +0.1% (95%: −2.4% to +2.6%); STEADY | **the runs disagree** |
| end-to-end latency, mean (ms) | 385.9 | 386.6 | 385.9 → 386.6; raw +0.2% (95%: −3.0% to +3.4%); STEADY | 381 → 378.2; raw −0.7% (95%: −1.6% to +0.1%); GAIN | 376 → 383.8; raw +2.1% (95%: −3.7% to +7.8%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,675 | 1,667 | 1675 → 1667; raw −0.5% (95%: −10.7% to +9.8%); STEADY | 1656 → 1650; raw −0.3% (95%: −3.4% to +2.8%); STEADY | 1640 → 1626; raw −0.9% (95%: −6.2% to +4.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 166.3 | 167.1 | 166.3 → 167.1; raw +0.5% (95%: −1.2% to +2.1%); STEADY | 164.7 → 163; raw −1.0% (95%: −3.9% to +1.8%); GAIN | 163.6 → 164.7; raw +0.7% (95%: −5.1% to +6.5%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.296 | 0.292 | 0.2958 → 0.292; raw −1.3% (95%: −6.4% to +3.8%), −0.0037 in the gauge's unit; GAIN | 0.2845 → 0.2818; raw −1.0% (95%: −5.3% to +3.4%), −0.0027 in the gauge's unit; GAIN | 0.2946 → 0.2919; raw −0.9% (95%: −5.5% to +3.7%), −0.0027 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 206.9 | 204.4 | 206.9 → 204.4; raw −1.2% (95%: −6.0% to +3.7%); GAIN | 204.1 → 202.1; raw −0.9% (95%: −5.2% to +3.4%); GAIN | 206.1 → 204.3; raw −0.8% (95%: −5.3% to +3.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.33 | 3.358 → 3.327; raw −0.9% (95%: −6.3% to +4.4%); GAIN | 3.313 → 3.28; raw −1.0% (95%: −5.1% to +3.2%); GAIN | 3.349 → 3.333; raw −0.5% (95%: −5.7% to +4.8%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 390, 394, 394 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146.9 | 146.3 | 146.9 → 146.3; raw −0.4% (95%: −1.1% to +0.2%); STEADY | 147.4 → 147.5; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | 147.2 → 147; raw −0.1% (95%: −0.6% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.17%) |
| throughput (messages a second consumed) | 171.6 | 171.6 | 171.6 → 171.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 173.3 → 173.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 173.1 → 173.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,135 | 2,176 | 2135 → 2176; raw +1.9% (95%: −3.1% to +6.9%); LOSS | 2465 → 2395; raw −2.9% (95%: −7.1% to +1.4%); GAIN | 2493 → 2511; raw +0.7% (95%: −8.6% to +10.0%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,429 | 3,496 | 3429 → 3496; raw +2.0% (95%: −3.8% to +7.7%); LOSS | 3803 → 3945; raw +3.7% (95%: −3.3% to +10.7%); LOSS | 3813 → 3828; raw +0.4% (95%: −5.8% to +6.6%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 10.9 | 10.8 | 10.86 → 10.78; raw −0.8% (95%: −1.5% to −0.1%); GAIN | 11.01 → 10.86; raw −1.3% (95%: −6.7% to +4.1%); GAIN | 11.58 → 11.58; raw −0.1% (95%: −0.3% to +0.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, mean (ms) | 285.0 | 296.3 | 285 → 296.3; raw +4.0% (95%: −4.0% to +11.9%); LOSS | 330.2 → 327.1; raw −0.9% (95%: −5.9% to +4.0%); GAIN | 333.7 → 336; raw +0.7% (95%: −5.5% to +6.9%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 648.7 | 659.7 | 648.7 → 659.7; raw +1.7% (95%: −7.4% to +10.8%); LOSS | 706 → 709.7; raw +0.5% (95%: −4.2% to +5.3%); LOSS | 719.3 → 712.7; raw −0.9% (95%: −8.2% to +6.4%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 52.0 | 54.0 | 51.96 → 54; raw +3.9% (95%: −1.7% to +9.5%); LOSS | 60.82 → 60.42; raw −0.7% (95%: −3.5% to +2.2%); GAIN | 61.53 → 61.16; raw −0.6% (95%: −6.2% to +5.0%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | 2 → 2.246; raw +12.3% (95%: −14.9% to +39.4%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.258 | 0.255 | 0.2583 → 0.2555; raw −1.1% (95%: −4.3% to +2.1%), −0.0028 in the gauge's unit; GAIN | 0.2646 → 0.261; raw −1.3% (95%: −7.1% to +4.4%), −0.0035 in the gauge's unit; GAIN | 0.2919 → 0.2899; raw −0.7% (95%: −4.3% to +2.9%), −0.0020 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 463.4 | 458.3 | 463.4 → 458.3; raw −1.1% (95%: −4.3% to +2.1%); GAIN | 473.8 → 467.6; raw −1.3% (95%: −7.0% to +4.4%); GAIN | 522.8 → 519.2; raw −0.7% (95%: −4.3% to +2.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7 | 6.95 | 7 → 6.953; raw −0.7% (95%: −3.4% to +2.0%); GAIN | 7.141 → 7.045; raw −1.3% (95%: −7.0% to +4.4%); GAIN | 7.889 → 7.843; raw −0.6% (95%: −3.8% to +2.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 5.33 | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,930, 1,949, 1,936 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724.9 | 724.9 | 724.9 → 724.9; raw ±0.0% (95%: −0.8% to +0.8%); STEADY | 732.4 → 732.9; raw +0.1% (95%: −0.4% to +0.5%); STEADY | 726 → 728.6; raw +0.4% (95%: −1.4% to +2.1%); STEADY | STEADY, under the floor (the three runs' mean 0.13%) |
| throughput (messages a second consumed) | 849.0 | 849.0 | 849 → 849; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 857.1 → 857.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 851.4 → 851.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,346 | 2,328 | 2346 → 2328; raw −0.8% (95%: −6.9% to +5.4%); GAIN | 2310 → 2255; raw −2.4% (95%: −9.9% to +5.1%); GAIN | 2380 → 2091; raw −12.1% (95%: −64.5% to +40.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,666 | 3,612 | 3666 → 3612; raw −1.5% (95%: −9.9% to +6.9%); GAIN | 3599 → 3524; raw −2.1% (95%: −12.3% to +8.1%); GAIN | 3764 → 3294; raw −12.5% (95%: −58.2% to +33.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.21 | 8.03 | 8.208 → 8.029; raw −2.2% (95%: −7.8% to +3.4%); GAIN | 9.521 → 10.01; raw +5.2% (95%: −83.6% to +94.0%); LOSS | 8.278 → 7.989; raw −3.5% (95%: −13.5% to +6.5%); GAIN | **the runs disagree** |
| end-to-end latency, mean (ms) | 313.7 | 308.2 | 313.7 → 308.2; raw −1.8% (95%: −10.6% to +7.1%); GAIN | 316.5 → 307; raw −3.0% (95%: −9.3% to +3.3%); GAIN | 322.7 → 287.9; raw −10.8% (95%: −54.3% to +32.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,277 | 3,225 | 3277 → 3225; raw −1.6% (95%: −6.4% to +3.3%); GAIN | 3278 → 3221; raw −1.7% (95%: −6.8% to +3.4%); GAIN | 3309 → 3060; raw −7.5% (95%: −42.3% to +27.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 272.4 | 266.6 | 272.4 → 266.6; raw −2.1% (95%: −12.5% to +8.2%); GAIN | 278.8 → 271.1; raw −2.8% (95%: −7.8% to +2.3%); GAIN | 281.1 → 250.9; raw −10.8% (95%: −53.4% to +31.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.24 | 2 → 2.245; raw +12.2% (95%: −14.8% to +39.3%); power given | 2 → 2.247; raw +12.4% (95%: −14.9% to +39.6%); power given | 2 → 2.246; raw +12.3% (95%: −14.9% to +39.4%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.343 | 0.347 | 0.3427 → 0.3475; raw +1.4% (95%: −2.0% to +4.7%), +0.0048 in the gauge's unit; power given | 0.284 → 0.2828; raw −0.4% (95%: −4.3% to +3.5%), −0.0011 in the gauge's unit; STEADY | 0.334 → 0.3344; raw +0.1% (95%: −9.0% to +9.2%), +0.0004 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.37%) |
| host CPU-seconds | 588.9 | 596.6 | 588.9 → 596.6; raw +1.3% (95%: −1.9% to +4.5%); power given | 506.9 → 504.7; raw −0.4% (95%: −4.1% to +3.2%); STEADY | 574.4 → 575.2; raw +0.1% (95%: −9.9% to +10.2%); STEADY | STEADY, under the floor (the three runs' mean 0.34%) |
| host CPU-seconds per 1,000 messages inside the line | 1.8 | 1.83 | 1.804 → 1.828; raw +1.3% (95%: −1.7% to +4.4%); power given | 1.537 → 1.53; raw −0.5% (95%: −4.1% to +3.2%); STEADY | 1.758 → 1.754; raw −0.2% (95%: −10.9% to +10.5%); STEADY | STEADY, under the floor (the three runs' mean 0.21%) |
| consumer changes written (the knob's moves) | 2 | 5.33 | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 6; raw +200.0% (95%: +200.0% to +200.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 15 gauge-rows GAIN, 1 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 STEADY, 9 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
