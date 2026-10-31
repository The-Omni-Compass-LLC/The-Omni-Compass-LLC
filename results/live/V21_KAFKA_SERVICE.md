# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40236926576 | `23c7e8eb27be` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| B | 40259312876 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| C | 40283010023 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 969, 970, 970 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.8 | 363.1 | 365.8 → 363.1; raw −0.7% (95%: −2.8% to +1.3%); LOSS | 365 → 365.3; raw +0.1% (95%: −0.3% to +0.4%); STEADY | 364.9 → 365.3; raw +0.1% (95%: −0.4% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.19%) |
| throughput (messages a second consumed) | 426.1 | 426.1 | 426.1 → 426.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 426.8 → 426.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 426.7 → 426.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,092 | 2,185 | 2092 → 2185; raw +4.4% (95%: −6.4% to +15.2%); LOSS | 2197 → 2181; raw −0.7% (95%: −1.8% to +0.4%); GAIN | 2255 → 2166; raw −3.9% (95%: −8.7% to +0.9%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,428 | 3,392 | 3428 → 3392; raw −1.1% (95%: −5.2% to +3.1%); GAIN | 3595 → 3519; raw −2.1% (95%: −5.5% to +1.3%); GAIN | 3509 → 3519; raw +0.3% (95%: −17.3% to +18.0%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.58 | 8.55 | 8.579 → 8.548; raw −0.4% (95%: −0.9% to +0.2%); STEADY | 8.569 → 8.559; raw −0.1% (95%: −1.3% to +1.1%); STEADY | 8.613 → 8.612; raw ±0.0% (95%: −2.0% to +2.0%); STEADY | STEADY, under the floor (the three runs' mean 0.16%) |
| end-to-end latency, mean (ms) | 281.1 | 292.6 | 281.1 → 292.6; raw +4.1% (95%: −8.8% to +17.0%); LOSS | 295.2 → 293; raw −0.7% (95%: −3.2% to +1.7%); GAIN | 297.4 → 292.1; raw −1.8% (95%: −10.1% to +6.5%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,568 | 1,564 | 1568 → 1564; raw −0.3% (95%: −6.9% to +6.3%); STEADY | 1613 → 1590; raw −1.4% (95%: −4.4% to +1.5%); GAIN | 1606 → 1588; raw −1.1% (95%: −3.8% to +1.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 124.3 | 129.3 | 124.3 → 129.3; raw +4.0% (95%: −8.7% to +16.8%); LOSS | 130 → 129.3; raw −0.5% (95%: −3.0% to +2.0%); STEADY | 131 → 128.4; raw −2.0% (95%: −10.6% to +6.6%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.07 | 2 → 2.067; raw +3.4% (95%: −4.5% to +11.2%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 3 | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.305 | 0.303 | 0.3048 → 0.3034; raw −0.5% (95%: −4.5% to +3.6%), −0.0014 in the gauge's unit; STEADY | 0.3076 → 0.306; raw −0.5% (95%: −4.4% to +3.3%), −0.0017 in the gauge's unit; GAIN | 0.3111 → 0.3109; raw −0.1% (95%: −3.2% to +3.0%), −0.0002 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.36%) |
| host CPU-seconds | 529.5 | 527.5 | 529.5 → 527.5; raw −0.4% (95%: −5.0% to +4.2%); STEADY | 534 → 531.6; raw −0.4% (95%: −4.4% to +3.5%); STEADY | 540.1 → 539.4; raw −0.1% (95%: −3.3% to +3.1%); STEADY | STEADY, under the floor (the three runs' mean 0.32%) |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 3.23 | 3.215 → 3.227; raw +0.4% (95%: −4.6% to +5.4%); STEADY | 3.25 → 3.233; raw −0.5% (95%: −4.8% to +3.7%); GAIN | 3.287 → 3.28; raw −0.2% (95%: −3.9% to +3.5%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| consumer changes written (the knob's moves) | 2 | 4.67 | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 974, 985 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342.4 | 341.2 | 342.4 → 341.2; raw −0.4% (95%: −1.4% to +0.7%); STEADY | 340.6 → 340.8; raw +0.1% (95%: −0.1% to +0.3%); STEADY | 344.2 → 342.5; raw −0.5% (95%: −1.6% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.25%) |
| throughput (messages a second consumed) | 418.5 | 418.5 | 418.5 → 418.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 418.7 → 418.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 423.3 → 423.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,401 | 2,383 | 2401 → 2383; raw −0.7% (95%: −6.3% to +4.8%); GAIN | 2527 → 2583; raw +2.2% (95%: −7.4% to +11.9%); LOSS | 2603 → 2744; raw +5.4% (95%: −2.3% to +13.1%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,432 | 3,678 | 3432 → 3678; raw +7.1% (95%: −1.5% to +15.8%); LOSS | 3828 → 3642; raw −4.9% (95%: −12.7% to +3.0%); GAIN | 3892 → 3821; raw −1.8% (95%: −8.5% to +4.9%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 9.86 | 12.0 | 9.862 → 11.98; raw +21.5% (95%: −30.5% to +73.5%); LOSS | 9.826 → 9.581; raw −2.5% (95%: −14.8% to +9.8%); GAIN | 18.77 → 11.56; raw −38.4% (95%: −165.4% to +88.5%); GAIN | **the runs disagree** |
| end-to-end latency, mean (ms) | 362.2 | 371.4 | 362.2 → 371.4; raw +2.5% (95%: −4.5% to +9.6%); LOSS | 385.8 → 384.7; raw −0.3% (95%: −3.4% to +2.8%); STEADY | 405.4 → 418.6; raw +3.3% (95%: −3.3% to +9.8%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,565 | 1,574 | 1565 → 1574; raw +0.5% (95%: −6.5% to +7.5%); LOSS | 1656 → 1678; raw +1.3% (95%: −4.8% to +7.4%); LOSS | 1737 → 1788; raw +2.9% (95%: +1.9% to +3.9%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| consumer lag, mean messages waiting | 158.0 | 162.6 | 158 → 162.6; raw +2.9% (95%: −4.1% to +9.9%); LOSS | 167.4 → 167; raw −0.2% (95%: −5.9% to +5.4%); STEADY | 180.1 → 184.5; raw +2.4% (95%: −4.4% to +9.3%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.266 | 0.26 | 0.266 → 0.2599; raw −2.3% (95%: −7.9% to +3.3%), −0.0061 in the gauge's unit; GAIN | 0.3071 → 0.3045; raw −0.8% (95%: −7.0% to +5.3%), −0.0026 in the gauge's unit; GAIN | 0.2603 → 0.266; raw +2.2% (95%: −10.0% to +14.4%), +0.0057 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 191.0 | 186.7 | 191 → 186.7; raw −2.3% (95%: −7.8% to +3.3%); GAIN | 215.1 → 213.2; raw −0.9% (95%: −7.2% to +5.4%); GAIN | 187 → 191; raw +2.2% (95%: −9.9% to +14.2%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.09 | 3.03 | 3.087 → 3.028; raw −1.9% (95%: −6.7% to +2.9%); GAIN | 3.496 → 3.462; raw −1.0% (95%: −7.2% to +5.3%); GAIN | 3.007 → 3.086; raw +2.6% (95%: −8.3% to +13.6%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 391, 394, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.3 | 147.1 | 147.3 → 147.1; raw −0.2% (95%: −0.8% to +0.5%); STEADY | 147.1 → 146.7; raw −0.2% (95%: −1.0% to +0.6%); STEADY | 147.1 → 146.7; raw −0.2% (95%: −0.9% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.21%) |
| throughput (messages a second consumed) | 172.1 | 172.1 | 172.1 → 172.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 173.2 → 173.2; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 172.8 → 172.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,205 | 2,168 | 2205 → 2168; raw −1.6% (95%: −5.3% to +2.0%); GAIN | 2562 → 2590; raw +1.1% (95%: −9.7% to +11.9%); LOSS | 2448 → 2508; raw +2.5% (95%: −6.7% to +11.7%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,404 | 3,415 | 3404 → 3415; raw +0.3% (95%: −6.3% to +6.9%); STEADY | 3924 → 3988; raw +1.6% (95%: −3.3% to +6.6%); LOSS | 3797 → 3779; raw −0.5% (95%: −3.6% to +2.7%); STEADY | STEADY, under the floor (the three runs' mean 0.50%) |
| end-to-end latency, median (ms) | 11.0 | 10.9 | 10.95 → 10.92; raw −0.3% (95%: −1.5% to +0.9%); STEADY | 11.55 → 11.54; raw −0.1% (95%: −0.5% to +0.3%); STEADY | 11.48 → 11.49; raw +0.1% (95%: −0.4% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.10%) |
| end-to-end latency, mean (ms) | 289.1 | 287.8 | 289.1 → 287.8; raw −0.4% (95%: −2.4% to +1.5%); STEADY | 347.2 → 354; raw +1.9% (95%: −9.9% to +13.8%); LOSS | 328.8 → 337.7; raw +2.7% (95%: −4.3% to +9.8%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 646.3 | 654.0 | 646.3 → 654; raw +1.2% (95%: −14.0% to +16.4%); LOSS | 731.7 → 741.3; raw +1.3% (95%: −4.3% to +6.9%); LOSS | 695.7 → 706; raw +1.5% (95%: −7.4% to +10.4%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 52.7 | 52.4 | 52.71 → 52.45; raw −0.5% (95%: −8.2% to +7.2%); STEADY | 63.84 → 65.04; raw +1.9% (95%: −10.3% to +14.0%); LOSS | 60.45 → 61.5; raw +1.7% (95%: −2.4% to +5.9%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.02 | 2 → 2.021; raw +1.1% (95%: −3.5% to +5.7%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.36%) |
| consumers running, most at once | 2 | 2.33 | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.262 | 0.261 | 0.262 → 0.2607; raw −0.5% (95%: −2.5% to +1.6%), −0.0012 in the gauge's unit; STEADY | 0.2803 → 0.2778; raw −0.9% (95%: −5.0% to +3.2%), −0.0025 in the gauge's unit; GAIN | 0.2849 → 0.2843; raw −0.2% (95%: −3.0% to +2.6%), −0.0006 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 470.2 | 468.0 | 470.2 → 468; raw −0.5% (95%: −2.4% to +1.5%); STEADY | 493.7 → 489.3; raw −0.9% (95%: −4.9% to +3.1%); GAIN | 510.9 → 509.8; raw −0.2% (95%: −2.9% to +2.5%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.09 | 7.07 | 7.089 → 7.068; raw −0.3% (95%: −2.5% to +1.9%); STEADY | 7.45 → 7.399; raw −0.7% (95%: −5.5% to +4.1%); GAIN | 7.709 → 7.709; raw ±0.0% (95%: −2.0% to +2.0%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumer changes written (the knob's moves) | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −110.1% to +176.8%) | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,927, 1,927, 1,915 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724.8 | 715.5 | 724.8 → 715.5; raw −1.3% (95%: −3.1% to +0.5%); LOSS | 725.4 → 720.8; raw −0.6% (95%: −2.8% to +1.5%); LOSS | 723.4 → 720.3; raw −0.4% (95%: −2.2% to +1.3%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 847.7 | 845.8 | 847.7 → 845.8; raw −0.2% (95%: −1.2% to +0.7%); STEADY | 847.6 → 847.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 842 → 842.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| end-to-end latency, 95th percentile (ms) | 2,272 | 2,293 | 2272 → 2293; raw +0.9% (95%: −6.0% to +7.9%); LOSS | 2181 → 2238; raw +2.6% (95%: −0.7% to +5.9%); LOSS | 2100 → 2098; raw −0.1% (95%: −2.6% to +2.4%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,523 | 3,679 | 3523 → 3679; raw +4.4% (95%: −8.4% to +17.2%); LOSS | 3548 → 3593; raw +1.2% (95%: −1.0% to +3.5%); LOSS | 3386 → 3338; raw −1.4% (95%: −14.1% to +11.3%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 8.45 | 8.14 | 8.449 → 8.136; raw −3.7% (95%: −12.3% to +4.8%); GAIN | 8.364 → 8.03; raw −4.0% (95%: −12.5% to +4.5%); GAIN | 8.244 → 8.196; raw −0.6% (95%: −5.7% to +4.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 304.5 | 320.9 | 304.5 → 320.9; raw +5.4% (95%: −9.7% to +20.5%); LOSS | 298.5 → 310.1; raw +3.9% (95%: −3.9% to +11.7%); LOSS | 274.6 → 279.5; raw +1.8% (95%: −7.6% to +11.2%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,199 | 3,226 | 3199 → 3226; raw +0.8% (95%: −1.3% to +2.9%); LOSS | 3177 → 3186; raw +0.3% (95%: −7.3% to +7.9%); STEADY | 3045 → 3019; raw −0.9% (95%: −1.8% to +0.1%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 266.5 | 277.3 | 266.5 → 277.3; raw +4.0% (95%: −11.0% to +19.1%); LOSS | 259.2 → 268.7; raw +3.7% (95%: −4.4% to +11.7%); LOSS | 235.9 → 239.9; raw +1.7% (95%: −7.3% to +10.7%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.27 | 2 → 2.27; raw +13.5% (95%: −15.4% to +42.4%); power given | 2 → 2.159; raw +8.0% (95%: −12.3% to +28.2%); power given | 2 → 2.098; raw +4.9% (95%: −15.4% to +25.2%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 3.67 | 2 → 3.667; raw +83.3% (95%: +11.6% to +155.1%); power given | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | 2 → 3; raw +50.0% (95%: −74.2% to +174.2%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.329 | 0.331 | 0.3295 → 0.3314; raw +0.6% (95%: −5.3% to +6.4%), +0.0019 in the gauge's unit; power given | 0.3337 → 0.3322; raw −0.5% (95%: −4.8% to +3.9%), −0.0015 in the gauge's unit; STEADY | 0.3782 → 0.3724; raw −1.5% (95%: −3.7% to +0.7%), −0.0058 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 565.6 | 570.2 | 565.6 → 570.2; raw +0.8% (95%: −5.8% to +7.4%); power given | 573.7 → 570.8; raw −0.5% (95%: −4.7% to +3.7%); GAIN | 651.9 → 640.7; raw −1.7% (95%: −3.2% to −0.3%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.77 | 1.733 → 1.766; raw +1.9% (95%: −3.8% to +7.6%); power given | 1.757 → 1.759; raw +0.1% (95%: −1.9% to +2.2%); STEADY | 2.002 → 1.976; raw −1.3% (95%: −3.8% to +1.2%); GAIN | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 11.3 | 2 → 11.33; raw +466.7% (95%: −331.9% to +1265.3%) | 2 → 8; raw +300.0% (95%: −560.6% to +1160.6%) | 2 → 5.333; raw +166.7% (95%: −350.5% to +683.8%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (3 trials, 1 allowed, 1 refused); acting: 2 to 3 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (2 trials, 1 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 3 gauge-rows GAIN, 10 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
