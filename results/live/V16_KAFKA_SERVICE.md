# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39823828673 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| B | 39844651167 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| C | 39864227589 | `681ff70efadd` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 973, 972, 975 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.1 | 365.4 | 365.1 → 365.4; raw +0.1% (95%: −0.3% to +0.4%); STEADY | 365.9 → 364.8; raw −0.3% (95%: −0.8% to +0.3%); STEADY | 366.2 → 365.6; raw −0.2% (95%: −0.3% to −0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.13%) |
| throughput (messages a second consumed) | 427.9 | 427.9 | 427.9 → 427.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 427.3 → 427.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 428.9 → 428.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,357 | 2,237 | 2357 → 2237; raw −5.1% (95%: −9.4% to −0.8%); GAIN | 2229 → 2263; raw +1.5% (95%: +0.9% to +2.1%); LOSS | 2336 → 2364; raw +1.2% (95%: −0.6% to +3.0%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,506 | 3,594 | 3506 → 3594; raw +2.5% (95%: −5.5% to +10.6%); LOSS | 3514 → 3614; raw +2.9% (95%: +0.7% to +5.0%); LOSS | 3702 → 3753; raw +1.4% (95%: −1.4% to +4.1%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, median (ms) | 8.56 | 8.51 | 8.555 → 8.505; raw −0.6% (95%: −1.9% to +0.7%); GAIN | 8.589 → 8.564; raw −0.3% (95%: −1.1% to +0.5%); STEADY | 8.566 → 8.592; raw +0.3% (95%: −1.5% to +2.1%); STEADY | STEADY, under the floor (the three runs' mean 0.19%) |
| end-to-end latency, mean (ms) | 308.5 | 301.2 | 308.5 → 301.2; raw −2.4% (95%: −7.3% to +2.6%); GAIN | 296.6 → 302.9; raw +2.1% (95%: −2.8% to +7.1%); LOSS | 313.9 → 318.5; raw +1.5% (95%: −0.5% to +3.4%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,637 | 1,615 | 1637 → 1615; raw −1.3% (95%: −6.3% to +3.7%); GAIN | 1615 → 1621; raw +0.4% (95%: −2.8% to +3.5%); STEADY | 1653 → 1674; raw +1.3% (95%: −2.1% to +4.6%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 136.8 | 132.7 | 136.8 → 132.7; raw −3.0% (95%: −7.1% to +1.1%); GAIN | 131 → 133.4; raw +1.8% (95%: −3.0% to +6.6%); LOSS | 138.7 → 140.8; raw +1.6% (95%: −1.8% to +4.9%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.24 | 2 → 2.245; raw +12.2% (95%: −14.8% to +39.3%); power given | 2 → 2.119; raw +6.0% (95%: −21.2% to +33.1%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.305 | 0.305 | 0.3051 → 0.305; raw ±0.0% (95%: −3.9% to +3.8%), −0.0002 in the gauge's unit; STEADY | 0.3096 → 0.3157; raw +2.0% (95%: +0.2% to +3.7%), +0.0061 in the gauge's unit; power given | 0.3116 → 0.3135; raw +0.6% (95%: −1.0% to +2.2%), +0.0019 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 529.6 | 530.3 | 529.6 → 530.3; raw +0.1% (95%: −4.2% to +4.4%); STEADY | 536.8 → 549.5; raw +2.4% (95%: +0.4% to +4.4%); power given | 541.3 → 544.5; raw +0.6% (95%: −1.3% to +2.4%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.22 | 3.222 → 3.223; raw ±0.0% (95%: −4.4% to +4.5%); STEADY | 3.259 → 3.346; raw +2.7% (95%: +0.2% to +5.1%); power given | 3.283 → 3.308; raw +0.8% (95%: −1.1% to +2.7%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumer changes written (the knob's moves) | 2 | 5.33 | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 977, 974 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.7 | 340.1 | 340.7 → 340.1; raw −0.2% (95%: −0.8% to +0.5%); STEADY | 341.3 → 340.7; raw −0.2% (95%: −0.5% to +0.1%); STEADY | 341.4 → 341; raw −0.1% (95%: −0.7% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.16%) |
| throughput (messages a second consumed) | 418.4 | 418.4 | 418.4 → 418.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 419.6 → 419.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 418.7 → 418.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,565 | 2,502 | 2565 → 2502; raw −2.5% (95%: −13.4% to +8.4%); GAIN | 2593 → 2483; raw −4.2% (95%: −12.3% to +3.8%); GAIN | 2433 → 2507; raw +3.0% (95%: −9.2% to +15.3%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,763 | 3,696 | 3763 → 3696; raw −1.8% (95%: −7.7% to +4.1%); GAIN | 3650 → 3968; raw +8.7% (95%: +2.6% to +14.8%); LOSS | 3615 → 3511; raw −2.9% (95%: −20.0% to +14.2%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 9.05 | 8.88 | 9.053 → 8.876; raw −2.0% (95%: −9.3% to +5.4%); GAIN | 9.357 → 9.387; raw +0.3% (95%: −3.1% to +3.7%); STEADY | 8.497 → 8.615; raw +1.4% (95%: −2.3% to +5.1%); LOSS | **the runs disagree** |
| end-to-end latency, mean (ms) | 376.4 | 380.1 | 376.4 → 380.1; raw +1.0% (95%: −1.9% to +3.8%); LOSS | 386.6 → 388.9; raw +0.6% (95%: −0.9% to +2.1%); LOSS | 365.3 → 368.2; raw +0.8% (95%: −0.1% to +1.7%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,658 | 1,639 | 1658 → 1639; raw −1.1% (95%: −4.6% to +2.4%); GAIN | 1664 → 1683; raw +1.1% (95%: −1.7% to +4.0%); LOSS | 1605 → 1592; raw −0.8% (95%: −3.5% to +1.9%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 162.7 | 162.7 | 162.7 → 162.7; raw ±0.0% (95%: −2.9% to +2.9%); STEADY | 167.9 → 168.6; raw +0.4% (95%: −1.3% to +2.2%); STEADY | 158.4 → 158.7; raw +0.2% (95%: −0.6% to +1.0%); STEADY | STEADY, under the floor (the three runs' mean 0.21%) |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.308 | 0.309 | 0.3083 → 0.3085; raw +0.1% (95%: −7.3% to +7.4%), +0.0003 in the gauge's unit; STEADY | 0.2947 → 0.291; raw −1.2% (95%: −5.9% to +3.4%), −0.0036 in the gauge's unit; GAIN | 0.2863 → 0.2841; raw −0.7% (95%: −4.7% to +3.2%), −0.0021 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 221.1 | 221.3 | 221.1 → 221.3; raw +0.1% (95%: −7.2% to +7.3%); STEADY | 206.1 → 203.7; raw −1.2% (95%: −5.7% to +3.3%); GAIN | 205.7 → 204.2; raw −0.7% (95%: −4.7% to +3.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.59 | 3.6 | 3.592 → 3.6; raw +0.2% (95%: −7.0% to +7.4%); STEADY | 3.342 → 3.309; raw −1.0% (95%: −5.2% to +3.3%); GAIN | 3.335 → 3.314; raw −0.6% (95%: −4.9% to +3.7%); GAIN | STEADY, under the floor (the three runs' mean 0.45%) |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 391, 393, 391 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.3 | 144.6 | 147.3 → 144.6; raw −1.9% (95%: −4.9% to +1.1%); LOSS | 147.1 → 155.5; raw +5.7% (95%: −18.9% to +30.3%); GAIN | 147.3 → 147; raw −0.2% (95%: −0.6% to +0.2%); STEADY | **the runs disagree** |
| throughput (messages a second consumed) | 171.8 | 171.8 | 171.8 → 171.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.7 → 172.7; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 171.8 → 171.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,095 | 2,232 | 2095 → 2232; raw +6.6% (95%: +1.2% to +11.9%); LOSS | 2423 → 1575; raw −35.0% (95%: −169.3% to +99.3%); GAIN | 2108 → 2157; raw +2.3% (95%: −5.0% to +9.6%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,445 | 3,633 | 3445 → 3633; raw +5.5% (95%: −11.9% to +22.8%); LOSS | 3823 → 2625; raw −31.3% (95%: −173.9% to +111.2%); GAIN | 3470 → 3485; raw +0.4% (95%: −5.1% to +6.0%); STEADY | **the runs disagree** |
| end-to-end latency, median (ms) | 10.7 | 10.7 | 10.68 → 10.66; raw −0.2% (95%: −0.9% to +0.4%); STEADY | 11.33 → 11.27; raw −0.5% (95%: −4.4% to +3.4%); GAIN | 10.93 → 10.95; raw +0.2% (95%: −1.1% to +1.5%); STEADY | STEADY, under the floor (the three runs' mean 0.20%) |
| end-to-end latency, mean (ms) | 280.1 | 313.8 | 280.1 → 313.8; raw +12.0% (95%: −1.2% to +25.3%); LOSS | 326.6 → 221.1; raw −32.3% (95%: −166.1% to +101.5%); GAIN | 282.6 → 291.3; raw +3.1% (95%: −5.1% to +11.2%); LOSS | **the runs disagree** |
| consumer lag, most messages waiting at once | 653.0 | 642.7 | 653 → 642.7; raw −1.6% (95%: −10.7% to +7.5%); GAIN | 714 → 492.7; raw −31.0% (95%: −158.1% to +96.1%); GAIN | 656.7 → 663.3; raw +1.0% (95%: −9.6% to +11.7%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 51.2 | 57.6 | 51.17 → 57.65; raw +12.7% (95%: −3.5% to +28.8%); LOSS | 59.86 → 40.56; raw −32.2% (95%: −167.0% to +102.6%); GAIN | 51.91 → 53.58; raw +3.2% (95%: −4.7% to +11.2%); LOSS | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2 | 2 → 1.999; raw −0.1% (95%: −0.6% to +0.5%); STEADY | 2 → 2.187; raw +9.3% (95%: −32.2% to +50.9%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.253 | 0.252 | 0.2535 → 0.2519; raw −0.6% (95%: −3.0% to +1.7%), −0.0016 in the gauge's unit; GAIN | 0.2774 → 0.2781; raw +0.2% (95%: −2.5% to +3.0%), +0.0007 in the gauge's unit; STEADY | 0.2619 → 0.2615; raw −0.2% (95%: −3.6% to +3.3%), −0.0004 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.19%) |
| host CPU-seconds | 454.2 | 451.3 | 454.2 → 451.3; raw −0.6% (95%: −3.0% to +1.7%); GAIN | 497 → 498.3; raw +0.3% (95%: −2.4% to +2.9%); STEADY | 470.7 → 470; raw −0.2% (95%: −3.6% to +3.3%); STEADY | STEADY, under the floor (the three runs' mean 0.18%) |
| host CPU-seconds per 1,000 messages inside the line | 6.85 | 6.94 | 6.849 → 6.936; raw +1.3% (95%: −1.7% to +4.2%); power given | 7.498 → 7.147; raw −4.7% (95%: −27.3% to +18.0%); GAIN | 7.092 → 7.094; raw ±0.0% (95%: −3.7% to +3.8%); STEADY | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 5.33 | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,932, 1,949, 1,931 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726.4 | 725.2 | 726.4 → 725.2; raw −0.2% (95%: −0.4% to +0.1%); STEADY | 727.9 → 770.9; raw +5.9% (95%: −19.1% to +31.0%); GAIN | 725.4 → 725.4; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 849.8 | 849.8 | 849.8 → 849.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 857.2 → 857.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 849.3 → 849.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,298 | 2,297 | 2298 → 2297; raw ±0.0% (95%: −10.2% to +10.2%); STEADY | 2659 → 1713; raw −35.6% (95%: −167.0% to +95.9%); GAIN | 2345 → 2292; raw −2.2% (95%: −10.7% to +6.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,658 | 3,775 | 3658 → 3775; raw +3.2% (95%: −7.8% to +14.1%); LOSS | 4170 → 2533; raw −39.2% (95%: −156.9% to +78.4%); GAIN | 3642 → 3636; raw −0.2% (95%: −10.0% to +9.7%); STEADY | **the runs disagree** |
| end-to-end latency, median (ms) | 7.86 | 7.78 | 7.863 → 7.78; raw −1.1% (95%: −4.2% to +2.1%); GAIN | 7.447 → 7.017; raw −5.8% (95%: −23.6% to +12.1%); GAIN | 7.472 → 7.464; raw −0.1% (95%: −2.9% to +2.7%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 305.7 | 310.3 | 305.7 → 310.3; raw +1.5% (95%: −2.6% to +5.6%); LOSS | 360.1 → 232.4; raw −35.5% (95%: −161.4% to +90.5%); GAIN | 305 → 302; raw −1.0% (95%: −8.6% to +6.7%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,222 | 3,287 | 3222 → 3287; raw +2.0% (95%: −0.4% to +4.5%); LOSS | 3599 → 2408; raw −33.1% (95%: −145.1% to +78.9%); GAIN | 3248 → 3211; raw −1.1% (95%: −5.4% to +3.1%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 264.4 | 268.5 | 264.4 → 268.5; raw +1.5% (95%: −2.2% to +5.3%); LOSS | 315.3 → 204.2; raw −35.2% (95%: −160.4% to +89.9%); GAIN | 262.9 → 260.3; raw −1.0% (95%: −8.4% to +6.5%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.195; raw +9.8% (95%: −33.7% to +53.2%); power given | 2 → 2.12; raw +6.0% (95%: −21.3% to +33.3%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.346 | 0.342 | 0.3463 → 0.3421; raw −1.2% (95%: −3.4% to +0.9%), −0.0042 in the gauge's unit; GAIN | 0.3131 → 0.3156; raw +0.8% (95%: −3.7% to +5.3%), +0.0024 in the gauge's unit; power given | 0.354 → 0.356; raw +0.6% (95%: −6.0% to +7.2%), +0.0020 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 601.2 | 595.4 | 601.2 → 595.4; raw −1.0% (95%: −3.3% to +1.3%); GAIN | 558 → 561.9; raw +0.7% (95%: −3.3% to +4.7%); power given | 629.4 → 633.5; raw +0.6% (95%: −6.2% to +7.5%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.82 | 1.838 → 1.824; raw −0.8% (95%: −3.2% to +1.6%); GAIN | 1.703 → 1.627; raw −4.4% (95%: −24.0% to +15.1%); GAIN | 1.927 → 1.94; raw +0.7% (95%: −6.6% to +7.9%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 6 gauge-rows GAIN, 1 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 STEADY, 18 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
