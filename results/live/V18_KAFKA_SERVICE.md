# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40062235164 | `bbf7e12f0467` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| B | 40067533814 | `dadeec62a61a` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| C | 40131354530 | `791ad0fd93b1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 972, 975, 976 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.3 | 364.9 | 365.3 → 364.9; raw −0.1% (95%: −0.1% to −0.1%); STEADY | 365.5 → 365.3; raw −0.1% (95%: −0.7% to +0.6%); STEADY | 366.4 → 365.9; raw −0.1% (95%: −0.3% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.09%) |
| throughput (messages a second consumed) | 427.7 | 427.7 | 427.7 → 427.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 428.9 → 428.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 429.5 → 429.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,333 | 2,311 | 2333 → 2311; raw −0.9% (95%: −6.5% to +4.6%); GAIN | 2390 → 2431; raw +1.7% (95%: −9.4% to +12.9%); LOSS | 2394 → 2331; raw −2.6% (95%: −13.9% to +8.6%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,671 | 3,674 | 3671 → 3674; raw +0.1% (95%: −6.3% to +6.4%); STEADY | 3737 → 3708; raw −0.8% (95%: −9.5% to +7.9%); GAIN | 3770 → 3732; raw −1.0% (95%: −8.8% to +6.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.85 | 8.76 | 8.847 → 8.758; raw −1.0% (95%: −6.6% to +4.5%); GAIN | 8.614 → 8.577; raw −0.4% (95%: −2.3% to +1.4%); STEADY | 8.239 → 8.25; raw +0.1% (95%: −1.8% to +2.0%); STEADY | STEADY, under the floor (the three runs' mean 0.44%) |
| end-to-end latency, mean (ms) | 310.1 | 306.6 | 310.1 → 306.6; raw −1.2% (95%: −5.6% to +3.3%); GAIN | 318.8 → 321; raw +0.7% (95%: −4.0% to +5.5%); LOSS | 319.4 → 313.1; raw −2.0% (95%: −8.6% to +4.7%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,655 | 1,646 | 1655 → 1646; raw −0.5% (95%: −4.5% to +3.5%); GAIN | 1667 → 1686; raw +1.1% (95%: −5.1% to +7.3%); LOSS | 1708 → 1663; raw −2.6% (95%: −12.3% to +7.1%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 136.6 | 135.2 | 136.6 → 135.2; raw −1.0% (95%: −4.8% to +2.7%); GAIN | 141 → 141.8; raw +0.5% (95%: −5.1% to +6.2%); LOSS | 141 → 138; raw −2.1% (95%: −9.6% to +5.3%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | 2 → 2.119; raw +6.0% (95%: −21.2% to +33.1%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.015; raw +0.7% (95%: −3.9% to +5.4%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| consumers running, most at once | 2 | 2.33 | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.339 | 0.331 | 0.3388 → 0.331; raw −2.3% (95%: −10.8% to +6.2%), −0.0077 in the gauge's unit; GAIN | 0.3157 → 0.3107; raw −1.6% (95%: −9.1% to +6.0%), −0.0050 in the gauge's unit; GAIN | 0.3013 → 0.3043; raw +1.0% (95%: −5.5% to +7.5%), +0.0030 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 588.7 | 576.2 | 588.7 → 576.2; raw −2.1% (95%: −10.4% to +6.2%); GAIN | 548.1 → 539.3; raw −1.6% (95%: −9.9% to +6.7%); GAIN | 537.8 → 543.8; raw +1.1% (95%: −5.6% to +7.8%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.58 | 3.51 | 3.58 → 3.507; raw −2.0% (95%: −10.3% to +6.2%); GAIN | 3.331 → 3.279; raw −1.5% (95%: −10.5% to +7.4%); GAIN | 3.261 → 3.302; raw +1.3% (95%: −5.4% to +7.9%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4.67 | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 981, 978, 977 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342.7 | 340.8 | 342.7 → 340.8; raw −0.5% (95%: −2.2% to +1.2%); LOSS | 342.3 → 341.7; raw −0.2% (95%: −0.6% to +0.3%); STEADY | 341.8 → 340.7; raw −0.3% (95%: −0.5% to −0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.34%) |
| throughput (messages a second consumed) | 421.7 | 421.7 | 421.7 → 421.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 420.2 → 420.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 419.7 → 419.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,565 | 2,646 | 2565 → 2646; raw +3.2% (95%: ±0.0% to +6.4%); LOSS | 2535 → 2462; raw −2.9% (95%: −6.9% to +1.1%); GAIN | 2592 → 2571; raw −0.8% (95%: −10.8% to +9.2%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,984 | 3,787 | 3984 → 3787; raw −4.9% (95%: −25.8% to +16.0%); GAIN | 3659 → 3679; raw +0.5% (95%: −6.2% to +7.3%); LOSS | 3694 → 3729; raw +0.9% (95%: −16.5% to +18.4%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 11.9 | 10.0 | 11.95 → 10.02; raw −16.2% (95%: −54.4% to +22.0%); GAIN | 8.463 → 8.506; raw +0.5% (95%: −3.0% to +4.0%); LOSS | 8.721 → 8.642; raw −0.9% (95%: −6.2% to +4.4%); GAIN | **the runs disagree** |
| end-to-end latency, mean (ms) | 398.6 | 407.8 | 398.6 → 407.8; raw +2.3% (95%: −6.9% to +11.6%); LOSS | 373 → 376.1; raw +0.8% (95%: +0.4% to +1.2%); LOSS | 381.3 → 382.8; raw +0.4% (95%: −1.3% to +2.1%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| consumer lag, most messages waiting at once | 1,733 | 1,730 | 1733 → 1730; raw −0.2% (95%: −10.2% to +9.8%); STEADY | 1656 → 1663; raw +0.4% (95%: +0.3% to +0.6%); STEADY | 1651 → 1660; raw +0.5% (95%: −2.7% to +3.7%); LOSS | STEADY, under the floor (the three runs' mean 0.25%) |
| consumer lag, mean messages waiting | 174.9 | 178.7 | 174.9 → 178.7; raw +2.2% (95%: −6.1% to +10.4%); LOSS | 161.5 → 162.5; raw +0.6% (95%: −1.8% to +3.1%); LOSS | 164.6 → 164.3; raw −0.2% (95%: −3.4% to +3.0%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.268 | 0.27 | 0.2678 → 0.2697; raw +0.7% (95%: −5.0% to +6.5%), +0.0019 in the gauge's unit; power given | 0.2835 → 0.2819; raw −0.6% (95%: −3.5% to +2.4%), −0.0016 in the gauge's unit; GAIN | 0.3032 → 0.3009; raw −0.8% (95%: −4.4% to +2.9%), −0.0023 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 192.3 | 193.7 | 192.3 → 193.7; raw +0.8% (95%: −4.9% to +6.5%); power given | 203.6 → 202.5; raw −0.6% (95%: −3.5% to +2.3%); GAIN | 217.5 → 215.9; raw −0.7% (95%: −4.3% to +2.9%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 3.11 | 3.15 | 3.105 → 3.146; raw +1.3% (95%: −2.6% to +5.2%); power given | 3.293 → 3.28; raw −0.4% (95%: −3.8% to +3.0%); STEADY | 3.522 → 3.507; raw −0.4% (95%: −3.9% to +3.0%); STEADY | STEADY, under the floor (the three runs' mean 0.16%) |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 393, 394 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 146.6 | 147.1 → 146.6; raw −0.3% (95%: −1.1% to +0.4%); STEADY | 146.9 → 147.2; raw +0.2% (95%: +0.1% to +0.3%); STEADY | 147.1 → 155.8; raw +5.9% (95%: −19.9% to +31.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| throughput (messages a second consumed) | 172.8 | 172.8 | 172.8 → 172.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 173 → 173; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 173.3 → 173.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,458 | 2,538 | 2458 → 2538; raw +3.2% (95%: +1.4% to +5.1%); LOSS | 2493 → 2462; raw −1.2% (95%: −6.3% to +3.8%); GAIN | 2615 → 1684; raw −35.6% (95%: −179.1% to +107.9%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,843 | 3,824 | 3843 → 3824; raw −0.5% (95%: −12.9% to +11.9%); STEADY | 3896 → 3674; raw −5.7% (95%: −11.3% to −0.2%); GAIN | 4041 → 2576; raw −36.2% (95%: −160.3% to +87.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| end-to-end latency, median (ms) | 11.6 | 11.6 | 11.63 → 11.59; raw −0.3% (95%: −0.6% to +0.1%); STEADY | 11.57 → 11.56; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 11.23 → 11.16; raw −0.7% (95%: −2.0% to +0.6%); GAIN | STEADY, under the floor (the three runs' mean 0.32%) |
| end-to-end latency, mean (ms) | 332.8 | 344.2 | 332.8 → 344.2; raw +3.4% (95%: −3.5% to +10.3%); LOSS | 340.6 → 330.1; raw −3.1% (95%: −4.7% to −1.4%); GAIN | 352.6 → 229; raw −35.1% (95%: −167.8% to +97.7%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 711.3 | 720.0 | 711.3 → 720; raw +1.2% (95%: −5.4% to +7.9%); LOSS | 718 → 695.7; raw −3.1% (95%: −12.6% to +6.4%); GAIN | 720.7 → 516; raw −28.4% (95%: −142.1% to +85.3%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 61.0 | 63.1 | 61.04 → 63.13; raw +3.4% (95%: −0.8% to +7.7%); LOSS | 62.54 → 60.96; raw −2.5% (95%: −6.9% to +1.8%); GAIN | 64.8 → 42.39; raw −34.6% (95%: −165.8% to +96.7%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.186; raw +9.3% (95%: −28.6% to +47.2%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 3; raw +50.0% (95%: +50.0% to +50.0%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.285 | 0.281 | 0.2846 → 0.2812; raw −1.2% (95%: −4.6% to +2.2%), −0.0034 in the gauge's unit; GAIN | 0.2806 → 0.2806; raw ±0.0% (95%: −2.2% to +2.1%), −0.0001 in the gauge's unit; STEADY | 0.274 → 0.2728; raw −0.4% (95%: −4.1% to +3.2%), −0.0012 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 501.7 | 495.7 | 501.7 → 495.7; raw −1.2% (95%: −4.8% to +2.4%); GAIN | 494 → 494; raw ±0.0% (95%: −2.3% to +2.2%); STEADY | 490.3 → 488.2; raw −0.4% (95%: −4.1% to +3.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.57 | 7.5 | 7.568 → 7.501; raw −0.9% (95%: −3.7% to +2.0%); GAIN | 7.471 → 7.456; raw −0.2% (95%: −2.4% to +2.0%); STEADY | 7.404 → 6.999; raw −5.5% (95%: −24.4% to +13.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 6; raw +200.0% (95%: +200.0% to +200.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); acting: 2 to 3 (2 trials, 1 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,929, 1,940, 1,949 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726.0 | 724.5 | 726 → 724.5; raw −0.2% (95%: −0.5% to +0.1%); STEADY | 727.8 → 724.5; raw −0.4% (95%: −1.1% to +0.2%); STEADY | 730.5 → 728.5; raw −0.3% (95%: −0.4% to −0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.30%) |
| throughput (messages a second consumed) | 848.4 | 848.4 | 848.4 → 848.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 853.3 → 853.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 857.4 → 857.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,213 | 2,258 | 2213 → 2258; raw +2.0% (95%: −5.2% to +9.2%); LOSS | 2387 → 2607; raw +9.2% (95%: −10.6% to +29.1%); LOSS | 2498 → 2531; raw +1.3% (95%: −0.9% to +3.6%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,662 | 3,685 | 3662 → 3685; raw +0.6% (95%: −8.3% to +9.6%); LOSS | 3764 → 4062; raw +7.9% (95%: −4.7% to +20.6%); LOSS | 3822 → 3832; raw +0.3% (95%: −5.7% to +6.2%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.43 | 8.36 | 8.427 → 8.36; raw −0.8% (95%: −4.6% to +3.1%); GAIN | 7.45 → 7.513; raw +0.8% (95%: −2.0% to +3.7%); LOSS | 7.375 → 7.332; raw −0.6% (95%: −1.3% to +0.2%); GAIN | **the runs disagree** |
| end-to-end latency, mean (ms) | 304.1 | 310.1 | 304.1 → 310.1; raw +2.0% (95%: −2.5% to +6.4%); LOSS | 321.3 → 355.3; raw +10.6% (95%: −5.8% to +27.0%); LOSS | 335.4 → 341.9; raw +1.9% (95%: −4.3% to +8.1%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 3,205 | 3,222 | 3205 → 3222; raw +0.5% (95%: −5.2% to +6.3%); LOSS | 3354 → 3447; raw +2.8% (95%: −11.3% to +16.9%); LOSS | 3435 → 3440; raw +0.1% (95%: −4.9% to +5.2%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, mean messages waiting | 264.1 | 269.1 | 264.1 → 269.1; raw +1.9% (95%: −3.0% to +6.8%); LOSS | 280.1 → 307.4; raw +9.7% (95%: −5.9% to +25.4%); LOSS | 294.1 → 298.5; raw +1.5% (95%: −2.7% to +5.7%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 2.015; raw +0.7% (95%: −3.9% to +5.4%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.332 | 0.329 | 0.3325 → 0.3286; raw −1.2% (95%: −7.3% to +5.0%), −0.0038 in the gauge's unit; GAIN | 0.3157 → 0.3233; raw +2.4% (95%: −0.4% to +5.3%), +0.0076 in the gauge's unit; power given | 0.3136 → 0.3124; raw −0.4% (95%: −4.2% to +3.4%), −0.0013 in the gauge's unit; STEADY | **the runs disagree** |
| host CPU-seconds | 571.2 | 565.7 | 571.2 → 565.7; raw −1.0% (95%: −6.6% to +4.6%); GAIN | 562.1 → 576.1; raw +2.5% (95%: −0.4% to +5.4%); power given | 558.8 → 557.7; raw −0.2% (95%: −3.9% to +3.5%); STEADY | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.73 | 1.748 → 1.734; raw −0.8% (95%: −6.3% to +4.8%); GAIN | 1.716 → 1.766; raw +3.0% (95%: +0.4% to +5.6%); power given | 1.699 → 1.7; raw +0.1% (95%: −3.6% to +3.7%); STEADY | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 6 gauge-rows GAIN, 7 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 STEADY, 13 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
