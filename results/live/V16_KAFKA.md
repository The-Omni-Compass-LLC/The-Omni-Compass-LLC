# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39821402572 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| B | 39840024618 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| C | 39860244280 | `15915c961cd2` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 977, 954, 984 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.2 | 365.5 | 366.2 → 365.5; raw −0.2% (95%: −0.7% to +0.3%); STEADY | 367.7 → 369.4; raw +0.5% (95%: −0.8% to +1.7%); STEADY | 368.5 → 368.3; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| throughput (messages a second consumed) | 429.4 | 429.4 | 429.4 → 429.4; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 419.8 → 419.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 432.9 → 432.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,418 | 2,453 | 2418 → 2453; raw +1.5% (95%: −2.3% to +5.2%); LOSS | 1670 → 1641; raw −1.7% (95%: −9.4% to +5.9%); GAIN | 2491 → 2461; raw −1.2% (95%: −6.4% to +4.0%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,764 | 3,844 | 3764 → 3844; raw +2.1% (95%: −6.0% to +10.3%); LOSS | 2878 → 2707; raw −5.9% (95%: −16.8% to +4.9%); GAIN | 3869 → 3811; raw −1.5% (95%: −5.7% to +2.7%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 8.49 | 8.53 | 8.494 → 8.532; raw +0.4% (95%: −1.5% to +2.4%); STEADY | 8.243 → 8.095; raw −1.8% (95%: −4.3% to +0.8%); GAIN | 8.043 → 8.001; raw −0.5% (95%: −2.0% to +0.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 320.1 | 325.5 | 320.1 → 325.5; raw +1.7% (95%: −2.0% to +5.4%); LOSS | 215.4 → 204.3; raw −5.2% (95%: −19.0% to +8.6%); GAIN | 337.5 → 333.7; raw −1.1% (95%: −4.4% to +2.1%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,698 | 1,710 | 1698 → 1710; raw +0.7% (95%: −4.6% to +6.0%); LOSS | 1328 → 1289; raw −3.0% (95%: −16.0% to +10.1%); GAIN | 1737 → 1722; raw −0.9% (95%: −4.9% to +3.2%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 141.3 | 143.4 | 141.3 → 143.4; raw +1.5% (95%: −1.3% to +4.3%); LOSS | 94.35 → 88.89; raw −5.8% (95%: −17.5% to +6.0%); GAIN | 151.6 → 149.5; raw −1.4% (95%: −3.7% to +1.0%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.417; raw +20.8% (95%: +18.8% to +22.8%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | **power given by the mean of our three runs, beyond the noise in 3 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.326 | 0.331 | 0.3261 → 0.3306; raw +1.4% (95%: −3.3% to +6.1%), +0.0045 in the gauge's unit; power given | 0.2957 → 0.2923; raw −1.1% (95%: −5.8% to +3.6%), −0.0033 in the gauge's unit; GAIN | 0.2729 → 0.2716; raw −0.5% (95%: −4.8% to +3.8%), −0.0013 in the gauge's unit; STEADY | **the runs disagree** |
| host CPU-seconds | 581.9 | 590.4 | 581.9 → 590.4; raw +1.5% (95%: −3.3% to +6.2%); power given | 526.2 → 521; raw −1.0% (95%: −5.6% to +3.7%); GAIN | 487.5 → 485.7; raw −0.4% (95%: −4.4% to +3.6%); STEADY | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.53 | 3.59 | 3.527 → 3.586; raw +1.7% (95%: −3.4% to +6.7%); power given | 3.179 → 3.133; raw −1.4% (95%: −4.8% to +1.9%); GAIN | 2.939 → 2.93; raw −0.3% (95%: −4.5% to +3.8%); STEADY | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (4 trials, 1 allowed, 1 refused); acting: 2 to 3 (4 trials, 1 allowed, 1 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 979, 974, 983 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342.0 | 341.9 | 342 → 341.9; raw ±0.0% (95%: −2.1% to +2.1%); STEADY | 341 → 340.1; raw −0.2% (95%: −0.4% to −0.1%); STEADY | 342.8 → 342.5; raw −0.1% (95%: −0.3% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| throughput (messages a second consumed) | 420.9 | 420.9 | 420.9 → 420.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 418.3 → 418.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 422.5 → 422.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,484 | 2,506 | 2484 → 2506; raw +0.9% (95%: −13.8% to +15.5%); LOSS | 2505 → 2522; raw +0.7% (95%: −8.8% to +10.2%); LOSS | 2633 → 2507; raw −4.8% (95%: −17.7% to +8.1%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,838 | 3,843 | 3838 → 3843; raw +0.1% (95%: −1.4% to +1.7%); STEADY | 3646 → 3642; raw −0.1% (95%: −11.7% to +11.4%); STEADY | 3859 → 3934; raw +1.9% (95%: −9.1% to +13.0%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 9.16 | 9.18 | 9.161 → 9.175; raw +0.2% (95%: −21.7% to +22.0%); STEADY | 9.537 → 9.396; raw −1.5% (95%: −6.1% to +3.1%); GAIN | 22.3 → 13.24; raw −40.6% (95%: −111.5% to +30.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 385.0 | 387.6 | 385 → 387.6; raw +0.7% (95%: −14.2% to +15.5%); LOSS | 376.6 → 380; raw +0.9% (95%: +0.4% to +1.4%); LOSS | 406.6 → 405.4; raw −0.3% (95%: −2.1% to +1.5%); STEADY | STEADY, under the floor (the three runs' mean 0.42%) |
| consumer lag, most messages waiting at once | 1,644 | 1,681 | 1644 → 1681; raw +2.2% (95%: −6.7% to +11.1%); LOSS | 1627 → 1647; raw +1.2% (95%: −3.2% to +5.6%); LOSS | 1725 → 1734; raw +0.5% (95%: −6.5% to +7.5%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 167.8 | 168.9 | 167.8 → 168.9; raw +0.7% (95%: −12.6% to +14.0%); LOSS | 163 → 164.9; raw +1.2% (95%: −0.7% to +3.2%); LOSS | 179.1 → 177.7; raw −0.8% (95%: −2.8% to +1.2%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.265 | 0.263 | 0.2649 → 0.2634; raw −0.6% (95%: −6.9% to +5.8%), −0.0015 in the gauge's unit; GAIN | 0.2938 → 0.2901; raw −1.3% (95%: −7.2% to +4.7%), −0.0037 in the gauge's unit; GAIN | 0.2588 → 0.2576; raw −0.5% (95%: −2.7% to +1.7%), −0.0012 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 189.9 | 189.0 | 189.9 → 189; raw −0.5% (95%: −6.8% to +5.9%); STEADY | 205.5 → 203; raw −1.2% (95%: −7.3% to +4.9%); GAIN | 186 → 185.2; raw −0.5% (95%: −2.6% to +1.7%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.07 | 3.06 | 3.075 → 3.06; raw −0.5% (95%: −8.9% to +7.9%); STEADY | 3.336 → 3.303; raw −1.0% (95%: −7.1% to +5.1%); GAIN | 3.004 → 2.993; raw −0.4% (95%: −2.8% to +2.0%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 392, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.3 | 146.8 | 147.3 → 146.8; raw −0.3% (95%: −0.5% to −0.1%); STEADY | 146.6 → 146.6; raw ±0.0% (95%: −0.8% to +0.8%); STEADY | 147.1 → 146.7; raw −0.3% (95%: −0.8% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.20%) |
| throughput (messages a second consumed) | 172.9 | 172.9 | 172.9 → 172.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.2 → 172.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.7 → 172.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,393 | 2,470 | 2393 → 2470; raw +3.2% (95%: −2.5% to +8.9%); LOSS | 2399 → 2383; raw −0.6% (95%: −14.8% to +13.5%); GAIN | 2459 → 2493; raw +1.4% (95%: −10.9% to +13.6%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,784 | 3,821 | 3784 → 3821; raw +1.0% (95%: −1.3% to +3.2%); LOSS | 3697 → 3652; raw −1.2% (95%: −14.6% to +12.2%); GAIN | 3792 → 3844; raw +1.4% (95%: −3.8% to +6.6%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 11.6 | 11.5 | 11.57 → 11.54; raw −0.2% (95%: −0.4% to −0.1%); STEADY | 11.77 → 11.71; raw −0.5% (95%: −2.6% to +1.6%); GAIN | 11.54 → 11.56; raw +0.2% (95%: −1.2% to +1.6%); STEADY | STEADY, under the floor (the three runs' mean 0.18%) |
| end-to-end latency, mean (ms) | 325.0 | 334.4 | 325 → 334.4; raw +2.9% (95%: −3.1% to +8.9%); LOSS | 321.9 → 322.9; raw +0.3% (95%: −12.1% to +12.8%); STEADY | 327.7 → 337.4; raw +3.0% (95%: −6.2% to +12.1%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 693.3 | 709.3 | 693.3 → 709.3; raw +2.3% (95%: −13.1% to +17.8%); LOSS | 690.3 → 698.3; raw +1.2% (95%: −5.4% to +7.7%); LOSS | 684 → 699.7; raw +2.3% (95%: −2.0% to +6.6%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 59.8 | 61.3 | 59.78 → 61.32; raw +2.6% (95%: −6.5% to +11.6%); LOSS | 58.8 → 59.57; raw +1.3% (95%: −8.9% to +11.5%); LOSS | 59.83 → 62.01; raw +3.6% (95%: −2.1% to +9.3%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.288 | 0.287 | 0.288 → 0.2865; raw −0.5% (95%: −2.8% to +1.8%), −0.0015 in the gauge's unit; GAIN | 0.2909 → 0.286; raw −1.7% (95%: −8.0% to +4.6%), −0.0049 in the gauge's unit; GAIN | 0.2788 → 0.2795; raw +0.2% (95%: −6.3% to +6.7%), +0.0006 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 508.8 | 506.3 | 508.8 → 506.3; raw −0.5% (95%: −2.8% to +1.8%); STEADY | 513.2 → 504.6; raw −1.7% (95%: −8.1% to +4.7%); GAIN | 491.3 → 493.1; raw +0.4% (95%: −6.2% to +6.9%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.68 | 7.66 | 7.675 → 7.66; raw −0.2% (95%: −2.3% to +1.9%); STEADY | 7.766 → 7.637; raw −1.7% (95%: −8.8% to +5.5%); GAIN | 7.41 → 7.457; raw +0.6% (95%: −6.4% to +7.7%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,938, 1,966, 1,938 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727.3 | 725.3 | 727.3 → 725.3; raw −0.3% (95%: −0.8% to +0.3%); STEADY | 734.1 → 734.4; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | 726 → 725.9; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| throughput (messages a second consumed) | 852.2 | 852.2 | 852.2 → 852.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 864.2 → 864.5; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 852.3 → 852.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,375 | 2,399 | 2375 → 2399; raw +1.0% (95%: +0.4% to +1.6%); LOSS | 2583 → 2538; raw −1.8% (95%: −8.0% to +4.5%); GAIN | 2393 → 2432; raw +1.7% (95%: −5.1% to +8.4%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,650 | 3,749 | 3650 → 3749; raw +2.7% (95%: −4.3% to +9.7%); LOSS | 3946 → 3961; raw +0.4% (95%: −2.7% to +3.5%); STEADY | 3862 → 3623; raw −6.2% (95%: −16.8% to +4.4%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 8.37 | 8.23 | 8.373 → 8.228; raw −1.7% (95%: −11.7% to +8.3%); GAIN | 8.893 → 8.68; raw −2.4% (95%: −3.0% to −1.7%); GAIN | 8.211 → 8.116; raw −1.2% (95%: −6.6% to +4.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, mean (ms) | 320.2 | 326.2 | 320.2 → 326.2; raw +1.9% (95%: −5.6% to +9.3%); LOSS | 355.1 → 350.4; raw −1.3% (95%: −5.7% to +3.0%); GAIN | 330.7 → 327.1; raw −1.1% (95%: −5.8% to +3.6%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,288 | 3,353 | 3288 → 3353; raw +2.0% (95%: −0.2% to +4.2%); LOSS | 3523 → 3481; raw −1.2% (95%: −2.5% to ±0.0%); GAIN | 3367 → 3326; raw −1.2% (95%: −4.3% to +1.9%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 279.0 | 285.0 | 279 → 285; raw +2.1% (95%: −5.1% to +9.4%); LOSS | 315.2 → 309.7; raw −1.7% (95%: −5.1% to +1.6%); GAIN | 288.2 → 285; raw −1.1% (95%: −5.0% to +2.8%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | 2 → 2.12; raw +6.0% (95%: −21.3% to +33.3%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.119; raw +5.9% (95%: −21.0% to +32.9%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2.33 | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.324 | 0.322 | 0.3236 → 0.322; raw −0.5% (95%: −2.6% to +1.6%), −0.0017 in the gauge's unit; GAIN | 0.2913 → 0.288; raw −1.1% (95%: −2.9% to +0.6%), −0.0033 in the gauge's unit; GAIN | 0.3309 → 0.3318; raw +0.3% (95%: −1.1% to +1.6%), +0.0009 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.46%) |
| host CPU-seconds | 555.9 | 552.9 | 555.9 → 552.9; raw −0.5% (95%: −2.8% to +1.7%); GAIN | 519.7 → 514.7; raw −1.0% (95%: −2.4% to +0.5%); GAIN | 569.4 → 571.2; raw +0.3% (95%: −1.4% to +2.0%); STEADY | STEADY, under the floor (the three runs' mean 0.39%) |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.69 | 1.698 → 1.693; raw −0.3% (95%: −2.0% to +1.4%); STEADY | 1.572 → 1.557; raw −1.0% (95%: −2.6% to +0.7%); GAIN | 1.742 → 1.748; raw +0.3% (95%: −0.9% to +1.6%); STEADY | STEADY, under the floor (the three runs' mean 0.30%) |
| consumer changes written (the knob's moves) | 2 | 4.67 | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 8 gauge-rows GAIN, 5 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 17 STEADY, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
