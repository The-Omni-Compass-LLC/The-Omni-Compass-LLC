# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39149249969 | `d44261ca0c5c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| B | 39157787056 | `5031411ae285` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| C | 39166374877 | `8472aaad2bf4` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 972, 976, 981 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.6 | 365.9 | 366.6 → 365.9; raw −0.2% (95%: −0.7% to +0.3%); STEADY | 366.1 → 364.6; raw −0.4% (95%: −1.1% to +0.3%); STEADY | 366.9 → 366.7; raw −0.1% (95%: −0.3% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.22%) |
| throughput (messages a second consumed) | 427.7 | 427.7 | 427.7 → 427.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 429.2 → 429; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 431.3 → 431.2; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| end-to-end latency, 95th percentile (ms) | 2,178 | 2,249 | 2178 → 2249; raw +3.3% (95%: −11.0% to +17.6%); LOSS | 2396 → 2420; raw +1.0% (95%: −7.0% to +9.0%); LOSS | 2536 → 2513; raw −0.9% (95%: −13.2% to +11.3%); GAIN | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,424 | 3,465 | 3424 → 3465; raw +1.2% (95%: −6.6% to +9.0%); LOSS | 3705 → 3803; raw +2.6% (95%: −0.5% to +5.8%); LOSS | 3966 → 3841; raw −3.1% (95%: −17.8% to +11.5%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 8.2 | 8.19 | 8.2 → 8.186; raw −0.2% (95%: −2.9% to +2.5%); STEADY | 8.517 → 8.513; raw −0.1% (95%: −1.1% to +1.0%); STEADY | 8.216 → 8.175; raw −0.5% (95%: −2.9% to +1.9%); STEADY | STEADY, under the floor (the three runs' mean 0.24%) |
| end-to-end latency, mean (ms) | 284.7 | 292.4 | 284.7 → 292.4; raw +2.7% (95%: −10.9% to +16.4%); LOSS | 319.2 → 329.3; raw +3.2% (95%: −5.9% to +12.2%); LOSS | 338.8 → 334.9; raw −1.1% (95%: −15.6% to +13.4%); GAIN | **the runs disagree** |
| consumer lag, most messages waiting at once | 1,588 | 1,588 | 1588 → 1588; raw ±0.0% (95%: −2.8% to +2.8%); STEADY | 1677 → 1695; raw +1.1% (95%: −7.3% to +9.4%); LOSS | 1761 → 1755; raw −0.4% (95%: −13.0% to +12.2%); STEADY | STEADY, under the floor (the three runs' mean 0.22%) |
| consumer lag, mean messages waiting | 125.7 | 128.7 | 125.7 → 128.7; raw +2.4% (95%: −10.4% to +15.2%); LOSS | 141.8 → 145.6; raw +2.7% (95%: −6.4% to +11.8%); LOSS | 150.5 → 147.9; raw −1.7% (95%: −15.1% to +11.6%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | 2 → 2.015; raw +0.7% (95%: −3.9% to +5.4%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| consumers running, most at once | 2 | 2.33 | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.297 | 0.296 | 0.297 → 0.2964; raw −0.2% (95%: −2.7% to +2.3%), −0.0006 in the gauge's unit; STEADY | 0.3068 → 0.3057; raw −0.4% (95%: −4.2% to +3.5%), −0.0011 in the gauge's unit; STEADY | 0.2992 → 0.2956; raw −1.2% (95%: −3.7% to +1.3%), −0.0036 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 529.7 | 529.1 | 529.7 → 529.1; raw −0.1% (95%: −2.2% to +2.0%); STEADY | 532.6 → 532.1; raw −0.1% (95%: −3.8% to +3.7%); STEADY | 533.6 → 527.6; raw −1.1% (95%: −3.5% to +1.2%); GAIN | STEADY, under the floor (the three runs' mean 0.44%) |
| host CPU-seconds per 1,000 messages inside the line | 3.21 | 3.21 | 3.209 → 3.213; raw +0.1% (95%: −1.6% to +1.9%); STEADY | 3.232 → 3.241; raw +0.3% (95%: −3.5% to +4.0%); STEADY | 3.231 → 3.195; raw −1.1% (95%: −3.6% to +1.4%); GAIN | STEADY, under the floor (the three runs' mean 0.25%) |
| consumer changes written (the knob's moves) | 2 | 4.67 | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 976, 976, 979 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.9 | 340.8 | 340.9 → 340.8; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 341.8 → 340.9; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 342.4 → 341.4; raw −0.3% (95%: −0.8% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.20%) |
| throughput (messages a second consumed) | 419.1 | 419.1 | 419.1 → 419.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 419.5 → 419.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 421 → 420.6; raw −0.1% (95%: −0.5% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| end-to-end latency, 95th percentile (ms) | 2,515 | 2,536 | 2515 → 2536; raw +0.9% (95%: −7.1% to +8.8%); LOSS | 2546 → 2501; raw −1.8% (95%: −7.3% to +3.7%); GAIN | 2581 → 2593; raw +0.5% (95%: −3.3% to +4.3%); STEADY | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,874 | 3,727 | 3874 → 3727; raw −3.8% (95%: −18.0% to +10.4%); GAIN | 3650 → 3713; raw +1.7% (95%: −8.0% to +11.4%); LOSS | 3763 → 3855; raw +2.4% (95%: −11.1% to +16.0%); LOSS | **the runs disagree** |
| end-to-end latency, median (ms) | 8.96 | 8.77 | 8.965 → 8.769; raw −2.2% (95%: −7.5% to +3.2%); GAIN | 8.756 → 8.69; raw −0.8% (95%: −1.4% to −0.1%); GAIN | 9.514 → 9.612; raw +1.0% (95%: −5.4% to +7.5%); LOSS | **the runs disagree** |
| end-to-end latency, mean (ms) | 379.0 | 382.1 | 379 → 382.1; raw +0.8% (95%: −1.2% to +2.8%); LOSS | 376.1 → 378.3; raw +0.6% (95%: −1.2% to +2.3%); LOSS | 395.9 → 398.5; raw +0.6% (95%: −0.7% to +2.0%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 1,664 | 1,661 | 1664 → 1661; raw −0.2% (95%: −4.4% to +4.1%); STEADY | 1662 → 1649; raw −0.8% (95%: −3.2% to +1.6%); GAIN | 1715 → 1720; raw +0.3% (95%: −3.5% to +4.1%); STEADY | STEADY, under the floor (the three runs' mean 0.20%) |
| consumer lag, mean messages waiting | 163.5 | 164.8 | 163.5 → 164.8; raw +0.8% (95%: −1.0% to +2.5%); LOSS | 162.7 → 162.6; raw −0.1% (95%: −3.2% to +3.1%); STEADY | 171.6 → 173.9; raw +1.3% (95%: −1.6% to +4.3%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | 2 → 1.983; raw −0.8% (95%: −0.8% to −0.8%); GAIN | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.308 | 0.304 | 0.308 → 0.3045; raw −1.1% (95%: −7.9% to +5.6%), −0.0035 in the gauge's unit; GAIN | 0.3007 → 0.2981; raw −0.9% (95%: −4.6% to +2.8%), −0.0027 in the gauge's unit; GAIN | 0.2918 → 0.2906; raw −0.4% (95%: −4.5% to +3.7%), −0.0012 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 220.9 | 218.4 | 220.9 → 218.4; raw −1.1% (95%: −7.8% to +5.6%); GAIN | 215.7 → 213.9; raw −0.9% (95%: −4.6% to +2.8%); GAIN | 204 → 203.4; raw −0.3% (95%: −4.1% to +3.6%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.59 | 3.55 | 3.587 → 3.547; raw −1.1% (95%: −7.7% to +5.5%); GAIN | 3.493 → 3.473; raw −0.6% (95%: −4.2% to +3.1%); GAIN | 3.3 → 3.298; raw −0.1% (95%: −4.3% to +4.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4 | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 392, 394, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.2 | 149.7 | 147.2 → 149.7; raw +1.8% (95%: −5.9% to +9.4%); GAIN | 146.6 → 146.9; raw +0.2% (95%: −0.5% to +0.9%); STEADY | 147.1 → 147.1; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (messages a second consumed) | 172.6 | 172.6 | 172.6 → 172.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.9 → 172.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.8 → 172.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,374 | 2,430 | 2374 → 2430; raw +2.4% (95%: −13.7% to +18.4%); LOSS | 2563 → 2518; raw −1.8% (95%: −6.9% to +3.3%); GAIN | 2391 → 2437; raw +1.9% (95%: −2.7% to +6.5%); LOSS | **the runs disagree** |
| end-to-end latency, 99th percentile (ms) | 3,663 | 3,843 | 3663 → 3843; raw +4.9% (95%: −21.6% to +31.5%); LOSS | 4001 → 3797; raw −5.1% (95%: −12.9% to +2.7%); GAIN | 3786 → 3661; raw −3.3% (95%: −9.5% to +2.9%); GAIN | **the runs disagree** |
| end-to-end latency, median (ms) | 11.5 | 11.5 | 11.54 → 11.54; raw ±0.0% (95%: −1.1% to +1.1%); STEADY | 11.53 → 11.52; raw −0.1% (95%: −1.0% to +0.9%); STEADY | 11.6 → 11.58; raw −0.2% (95%: −0.3% to −0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.10%) |
| end-to-end latency, mean (ms) | 319.1 | 308.2 | 319.1 → 308.2; raw −3.4% (95%: −16.5% to +9.6%); GAIN | 349.3 → 338.8; raw −3.0% (95%: −10.6% to +4.5%); GAIN | 326.5 → 326; raw −0.2% (95%: −1.9% to +1.6%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer lag, most messages waiting at once | 698.0 | 729.0 | 698 → 729; raw +4.4% (95%: −11.9% to +20.8%); LOSS | 731 → 713.3; raw −2.4% (95%: −7.9% to +3.0%); GAIN | 698.3 → 711.3; raw +1.9% (95%: −4.4% to +8.1%); LOSS | **the runs disagree** |
| consumer lag, mean messages waiting | 59.0 | 56.2 | 58.97 → 56.22; raw −4.7% (95%: −21.8% to +12.5%); GAIN | 64.25 → 62.46; raw −2.8% (95%: −9.5% to +3.9%); GAIN | 60.15 → 60.14; raw ±0.0% (95%: −0.4% to +0.3%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | 2 → 2.015; raw +0.7% (95%: −3.9% to +5.4%); power given | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | 2 → 1.993; raw −0.3% (95%: −0.3% to −0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| consumers running, most at once | 2 | 2.33 | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 2 → 2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.279 | 0.28 | 0.279 → 0.2796; raw +0.2% (95%: −2.1% to +2.5%), +0.0005 in the gauge's unit; STEADY | 0.2801 → 0.2779; raw −0.8% (95%: −4.0% to +2.5%), −0.0021 in the gauge's unit; GAIN | 0.2821 → 0.2803; raw −0.6% (95%: −2.8% to +1.5%), −0.0018 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.41%) |
| host CPU-seconds | 491.2 | 492.7 | 491.2 → 492.7; raw +0.3% (95%: −2.1% to +2.7%); STEADY | 493.7 → 489.9; raw −0.8% (95%: −4.0% to +2.5%); GAIN | 496.6 → 493.2; raw −0.7% (95%: −2.9% to +1.6%); GAIN | STEADY, under the floor (the three runs' mean 0.37%) |
| host CPU-seconds per 1,000 messages inside the line | 7.41 | 7.31 | 7.414 → 7.312; raw −1.4% (95%: −10.1% to +7.3%); GAIN | 7.469 → 7.398; raw −1.0% (95%: −4.0% to +2.1%); GAIN | 7.497 → 7.449; raw −0.6% (95%: −2.9% to +1.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| consumer changes written (the knob's moves) | 2 | 4.67 | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | 2 → 4; raw +100.0% (95%: +100.0% to +100.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,930, 1,935, 1,933 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725.5 | 725.0 | 725.5 → 725; raw −0.1% (95%: −1.0% to +0.9%); STEADY | 726.8 → 724.8; raw −0.3% (95%: −1.0% to +0.4%); STEADY | 725.3 → 725.3; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| throughput (messages a second consumed) | 848.7 | 848.7 | 848.7 → 848.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 851.1 → 850.8; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 850.3 → 850.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| end-to-end latency, 95th percentile (ms) | 2,250 | 2,242 | 2250 → 2242; raw −0.4% (95%: −14.1% to +13.4%); STEADY | 2311 → 2379; raw +2.9% (95%: −4.3% to +10.2%); LOSS | 2328 → 2328; raw ±0.0% (95%: −1.9% to +1.9%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,564 | 3,544 | 3564 → 3544; raw −0.6% (95%: −6.4% to +5.2%); GAIN | 3729 → 3697; raw −0.9% (95%: −7.7% to +5.9%); GAIN | 3799 → 3716; raw −2.2% (95%: −13.0% to +8.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, median (ms) | 8.38 | 7.86 | 8.385 → 7.864; raw −6.2% (95%: −15.3% to +2.9%); GAIN | 8.441 → 8.113; raw −3.9% (95%: −11.1% to +3.3%); GAIN | 8.231 → 8.039; raw −2.3% (95%: −13.5% to +8.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| end-to-end latency, mean (ms) | 304.4 | 302.8 | 304.4 → 302.8; raw −0.5% (95%: −10.7% to +9.6%); GAIN | 317.6 → 324.1; raw +2.0% (95%: −9.8% to +13.9%); LOSS | 318.3 → 316.8; raw −0.5% (95%: −1.9% to +1.0%); STEADY | **the runs disagree** |
| consumer lag, most messages waiting at once | 3,212 | 3,206 | 3212 → 3206; raw −0.2% (95%: −5.9% to +5.5%); STEADY | 3253 → 3308; raw +1.7% (95%: −6.2% to +9.6%); LOSS | 3307 → 3275; raw −1.0% (95%: −4.5% to +2.6%); GAIN | **the runs disagree** |
| consumer lag, mean messages waiting | 264.6 | 262.8 | 264.6 → 262.8; raw −0.7% (95%: −10.7% to +9.3%); GAIN | 277.6 → 280.7; raw +1.1% (95%: −10.6% to +12.8%); LOSS | 276.5 → 275.1; raw −0.5% (95%: −1.5% to +0.5%); GAIN | **the runs disagree** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | 2 → 2.246; raw +12.3% (95%: −14.9% to +39.5%); power given | 2 → 2.12; raw +6.0% (95%: −21.3% to +33.3%); power given | 2 → 2.119; raw +5.9% (95%: −21.0% to +32.9%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| consumers running, most at once | 2 | 2.67 | 2 → 2.667; raw +33.3% (95%: −38.4% to +105.0%); power given | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | 2 → 2.333; raw +16.7% (95%: −55.1% to +88.4%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.325 | 0.327 | 0.3246 → 0.3266; raw +0.6% (95%: −4.0% to +5.3%), +0.0021 in the gauge's unit; power given | 0.3253 → 0.3312; raw +1.8% (95%: −1.0% to +4.6%), +0.0060 in the gauge's unit; power given | 0.3422 → 0.3376; raw −1.3% (95%: −8.8% to +6.2%), −0.0046 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 557.0 | 561.9 | 557 → 561.9; raw +0.9% (95%: −4.6% to +6.4%); power given | 558.3 → 570.2; raw +2.1% (95%: −0.9% to +5.2%); power given | 587.7 → 580.8; raw −1.2% (95%: −9.8% to +7.4%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.72 | 1.705 → 1.722; raw +1.0% (95%: −4.6% to +6.5%); power given | 1.706 → 1.747; raw +2.4% (95%: −0.5% to +5.2%); power given | 1.8 → 1.779; raw −1.2% (95%: −9.9% to +7.6%); GAIN | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 5.33 | 2 → 5.333; raw +166.7% (95%: +23.2% to +310.1%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | 2 → 4.667; raw +133.3% (95%: −10.1% to +276.8%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 10 gauge-rows GAIN, 3 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
