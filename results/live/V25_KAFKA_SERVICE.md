# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 41758475899 | `e29ad045b2ac` | omni-v25 (digest cf56fc0a7b707452, 65 files) | 4 |
| B | 41772114283 | `db6e040b4584` | omni-v25 (digest cf56fc0a7b707452, 65 files) | 4 |
| C | 41785350365 | `0a92e09fe669` | omni-v25 (digest cf56fc0a7b707452, 65 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 976, 967, 977 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.9 | 429.2 | 365.9 → 429.2; raw +17.3% (95%: +16.9% to +17.7%); GAIN | 366.6 → 425.2; raw +16.0% (95%: +15.3% to +16.6%); GAIN | 366.3 → 429.4; raw +17.2% (95%: +16.8% to +17.6%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 429.5 | 429.5 | 429.5 → 429.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 425.5 → 425.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 429.6 → 429.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,450 | 10.5 | 2450 → 10.5; raw −99.6% (95%: −103.3% to −95.8%); GAIN | 1991 → 9.918; raw −99.5% (95%: −104.5% to −94.5%); GAIN | 2420 → 10.31; raw −99.6% (95%: −101.8% to −97.4%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,773 | 16.6 | 3773 → 16.58; raw −99.6% (95%: −105.4% to −93.7%); GAIN | 3255 → 23.25; raw −99.3% (95%: −102.4% to −96.2%); GAIN | 3754 → 13.12; raw −99.7% (95%: −102.4% to −96.9%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 8.52 | 7.44 | 8.518 → 7.441; raw −12.6% (95%: −14.9% to −10.4%); GAIN | 8.193 → 7.194; raw −12.2% (95%: −14.3% to −10.1%); GAIN | 8.491 → 7.387; raw −13.0% (95%: −15.3% to −10.7%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 325.4 | 8.83 | 325.4 → 8.833; raw −97.3% (95%: −99.0% to −95.6%); GAIN | 260.6 → 8.609; raw −96.7% (95%: −103.8% to −89.6%); GAIN | 322.8 → 8.379; raw −97.4% (95%: −99.7% to −95.1%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 1,714 | 119.7 | 1714 → 119.7; raw −93.0% (95%: −117.5% to −68.5%); GAIN | 1489 → 134; raw −91.0% (95%: −95.7% to −86.3%); GAIN | 1694 → 104.7; raw −93.8% (95%: −116.3% to −71.3%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 143.5 | 3.87 | 143.5 → 3.866; raw −97.3% (95%: −98.8% to −95.8%); GAIN | 114.5 → 4.093; raw −96.4% (95%: −102.8% to −90.1%); GAIN | 142.7 → 3.747; raw −97.4% (95%: −99.5% to −95.3%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.36 | 2 → 5.357; raw +167.8% (95%: +122.1% to +213.6%); power given | 2 → 4.856; raw +142.8% (95%: +109.4% to +176.2%); power given | 2 → 5.796; raw +189.8% (95%: +85.7% to +293.9%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.326 | 0.347 | 0.326 → 0.3469; raw +6.4% (95%: +3.0% to +9.8%), +0.0209 in the gauge's unit; power given | 0.2944 → 0.3051; raw +3.6% (95%: +1.5% to +5.8%), +0.0107 in the gauge's unit; power given | 0.3183 → 0.3384; raw +6.3% (95%: +4.9% to +7.7%), +0.0201 in the gauge's unit; power given | **power given in all three of our runs** |
| host CPU-seconds | 571.0 | 607.5 | 571 → 607.5; raw +6.4% (95%: +3.1% to +9.7%); power given | 524.2 → 542.2; raw +3.4% (95%: +1.0% to +5.9%); power given | 557 → 592.6; raw +6.4% (95%: +4.9% to +7.9%); power given | **power given in all three of our runs** |
| host CPU-seconds per 1,000 messages inside the line | 3.47 | 3.14 | 3.467 → 3.144; raw −9.3% (95%: −12.2% to −6.4%); GAIN | 3.176 → 2.833; raw −10.8% (95%: −13.9% to −7.7%); GAIN | 3.378 → 3.066; raw −9.2% (95%: −11.0% to −7.5%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 14.0 | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 976, 975, 980 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.6 | 419.2 | 340.6 → 419.2; raw +23.1% (95%: +21.9% to +24.2%); GAIN | 341.2 → 418.1; raw +22.6% (95%: +19.8% to +25.3%); GAIN | 341.9 → 418.9; raw +22.5% (95%: +21.0% to +24.0%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 419.7 | 419.7 | 419.7 → 419.7; raw ±0.0% (95%: −0.7% to +0.7%); STEADY | 419.2 → 420; raw +0.2% (95%: −0.2% to +0.6%); STEADY | 421 → 422.1; raw +0.3% (95%: +0.3% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.15%) |
| end-to-end latency, 95th percentile (ms) | 2,641 | 11.4 | 2641 → 11.43; raw −99.6% (95%: −106.8% to −92.3%); GAIN | 2602 → 11.58; raw −99.6% (95%: −100.8% to −98.3%); GAIN | 2654 → 11.35; raw −99.6% (95%: −106.6% to −92.5%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,707 | 76.7 | 3707 → 76.73; raw −97.9% (95%: −100.6% to −95.3%); GAIN | 3795 → 352.3; raw −90.7% (95%: −118.0% to −63.4%); GAIN | 3911 → 494.1; raw −87.4% (95%: −115.9% to −58.8%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 9.27 | 8.15 | 9.266 → 8.152; raw −12.0% (95%: −16.5% to −7.5%); GAIN | 9.211 → 8.105; raw −12.0% (95%: −20.7% to −3.4%); GAIN | 9.488 → 8.062; raw −15.0% (95%: −23.5% to −6.6%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 393.2 | 10.6 | 393.2 → 10.6; raw −97.3% (95%: −104.8% to −89.8%); GAIN | 385 → 16.92; raw −95.6% (95%: −103.8% to −87.4%); GAIN | 399.2 → 21.93; raw −94.5% (95%: −100.0% to −89.0%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 1,700 | 180.0 | 1700 → 180; raw −89.4% (95%: −107.5% to −71.3%); GAIN | 1684 → 328; raw −80.5% (95%: −128.5% to −32.6%); GAIN | 1717 → 459.7; raw −73.2% (95%: −123.2% to −23.3%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 169.2 | 4.82 | 169.2 → 4.822; raw −97.1% (95%: −104.6% to −89.7%); GAIN | 166 → 7.432; raw −95.5% (95%: −104.4% to −86.6%); GAIN | 172.8 → 9.36; raw −94.6% (95%: −99.5% to −89.7%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.26 | 2 → 5.264; raw +163.2% (95%: +108.5% to +217.9%); power given | 2 → 5.027; raw +151.3% (95%: +107.5% to +195.2%); power given | 2 → 5.275; raw +163.8% (95%: +72.4% to +255.2%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.324 | 0.341 | 0.3245 → 0.3414; raw +5.2% (95%: +1.5% to +9.0%), +0.0169 in the gauge's unit; power given | 0.3133 → 0.3335; raw +6.4% (95%: +1.3% to +11.6%), +0.0202 in the gauge's unit; power given | 0.3079 → 0.3324; raw +8.0% (95%: −1.7% to +17.6%), +0.0245 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds | 233.3 | 243.6 | 233.3 → 243.6; raw +4.4% (95%: +1.2% to +7.7%); power given | 220.7 → 234.2; raw +6.1% (95%: +0.6% to +11.7%); power given | 216.8 → 233.2; raw +7.5% (95%: −2.0% to +17.0%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.79 | 3.22 | 3.795 → 3.221; raw −15.1% (95%: −18.9% to −11.3%); GAIN | 3.581 → 3.108; raw −13.2% (95%: −19.4% to −7.0%); GAIN | 3.511 → 3.09; raw −12.0% (95%: −20.9% to −3.1%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 16.0 | 2 → 16; raw +700.0% (95%: +269.7% to +1130.3%) | 2 → 16; raw +700.0% (95%: +269.7% to +1130.3%) | 2 → 14; raw +600.0% (95%: −145.3% to +1345.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (1 trials, 1 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 393, 394, 392 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 172.7 | 147.1 → 172.7; raw +17.4% (95%: +17.1% to +17.6%); GAIN | 147.4 → 173; raw +17.4% (95%: +17.2% to +17.6%); GAIN | 147 → 171.8; raw +16.8% (95%: +16.2% to +17.4%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 172.8 | 172.8 | 172.8 → 172.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 173.4 → 173.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.3 → 172.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,450 | 14.2 | 2450 → 14.2; raw −99.4% (95%: −101.0% to −97.9%); GAIN | 2537 → 12.56; raw −99.5% (95%: −102.7% to −96.3%); GAIN | 2348 → 12.83; raw −99.5% (95%: −105.3% to −93.6%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,741 | 21.3 | 3741 → 21.34; raw −99.4% (95%: −105.4% to −93.4%); GAIN | 3933 → 28.35; raw −99.3% (95%: −102.7% to −95.9%); GAIN | 3574 → 69.38; raw −98.1% (95%: −101.9% to −94.2%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 11.7 | 11.5 | 11.73 → 11.5; raw −2.0% (95%: −3.3% to −0.6%); GAIN | 11.57 → 11.3; raw −2.3% (95%: −3.0% to −1.7%); GAIN | 11.25 → 11.11; raw −1.3% (95%: −2.1% to −0.4%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 327.7 | 12.4 | 327.7 → 12.45; raw −96.2% (95%: −99.4% to −93.0%); GAIN | 341.5 → 14.62; raw −95.7% (95%: −96.4% to −95.1%); GAIN | 308.9 → 16.09; raw −94.8% (95%: −100.0% to −89.6%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 720.7 | 59.0 | 720.7 → 59; raw −91.8% (95%: −117.4% to −66.2%); GAIN | 725.7 → 139; raw −80.8% (95%: −99.4% to −62.3%); GAIN | 667.7 → 174; raw −73.9% (95%: −90.9% to −57.0%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 60.6 | 2.22 | 60.56 → 2.218; raw −96.3% (95%: −99.4% to −93.3%); GAIN | 62.72 → 2.731; raw −95.6% (95%: −96.4% to −94.9%); GAIN | 56.62 → 3.089; raw −94.5% (95%: −101.1% to −88.0%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.58 | 2 → 3.583; raw +79.2% (95%: +31.2% to +127.1%); power given | 2 → 5.018; raw +150.9% (95%: −11.9% to +313.7%); power given | 2 → 3.773; raw +88.6% (95%: +47.3% to +129.9%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 5 | 2 → 5; raw +150.0% (95%: +150.0% to +150.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.298 | 0.305 | 0.2982 → 0.3048; raw +2.2% (95%: −0.9% to +5.3%), +0.0066 in the gauge's unit; power given | 0.2889 → 0.2965; raw +2.6% (95%: −1.2% to +6.5%), +0.0076 in the gauge's unit; power given | 0.2758 → 0.2818; raw +2.2% (95%: +0.8% to +3.5%), +0.0060 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 527.0 | 538.2 | 527 → 538.2; raw +2.1% (95%: −0.9% to +5.1%); power given | 510.2 → 523; raw +2.5% (95%: −1.2% to +6.2%); power given | 493.1 → 503.4; raw +2.1% (95%: +0.8% to +3.4%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.96 | 6.92 | 7.957 → 6.924; raw −13.0% (95%: −16.4% to −9.6%); GAIN | 7.692 → 6.717; raw −12.7% (95%: −16.3% to −9.1%); GAIN | 7.443 → 6.504; raw −12.6% (95%: −13.6% to −11.6%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 12; raw +500.0% (95%: +69.7% to +930.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 1 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,941, 1,933, 1,938 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728.2 | 853.9 | 728.2 → 853.9; raw +17.3% (95%: +16.8% to +17.7%); GAIN | 723.3 → 850; raw +17.5% (95%: +17.4% to +17.6%); GAIN | 726.7 → 852.5; raw +17.3% (95%: +17.1% to +17.5%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 853.9 | 853.9 | 853.9 → 853.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 850.2 → 850.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 852.7 → 852.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,433 | 9.42 | 2433 → 9.415; raw −99.6% (95%: −105.5% to −93.7%); GAIN | 2552 → 10.94; raw −99.6% (95%: −103.6% to −95.5%); GAIN | 2413 → 9.279; raw −99.6% (95%: −105.2% to −94.1%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,853 | 10.9 | 3853 → 10.93; raw −99.7% (95%: −102.4% to −97.0%); GAIN | 3971 → 14.29; raw −99.6% (95%: −103.0% to −96.3%); GAIN | 3846 → 11.13; raw −99.7% (95%: −104.4% to −95.0%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 7.47 | 6.15 | 7.472 → 6.15; raw −17.7% (95%: −25.9% to −9.5%); GAIN | 8.521 → 7.013; raw −17.7% (95%: −25.0% to −10.4%); GAIN | 7.828 → 6.161; raw −21.3% (95%: −22.2% to −20.4%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 320.9 | 6.28 | 320.9 → 6.279; raw −98.0% (95%: −101.9% to −94.2%); GAIN | 338.6 → 7.563; raw −97.8% (95%: −103.2% to −92.3%); GAIN | 324.8 → 6.746; raw −97.9% (95%: −99.8% to −96.0%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 3,373 | 48.3 | 3373 → 48.33; raw −98.6% (95%: −100.9% to −96.2%); GAIN | 3433 → 82.33; raw −97.6% (95%: −100.7% to −94.5%); GAIN | 3350 → 87.67; raw −97.4% (95%: −99.3% to −95.4%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 278.1 | 5.62 | 278.1 → 5.619; raw −98.0% (95%: −101.6% to −94.4%); GAIN | 291.6 → 6.687; raw −97.7% (95%: −103.1% to −92.3%); GAIN | 282.6 → 5.821; raw −97.9% (95%: −99.3% to −96.6%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.12 | 2 → 5.12; raw +156.0% (95%: +155.2% to +156.8%); power given | 2 → 5.033; raw +151.7% (95%: +136.2% to +167.1%); power given | 2 → 5.519; raw +175.9% (95%: +136.5% to +215.4%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.355 | 0.398 | 0.3549 → 0.3978; raw +12.1% (95%: +7.6% to +16.5%), +0.0429 in the gauge's unit; power given | 0.4302 → 0.48; raw +11.6% (95%: +4.2% to +19.0%), +0.0499 in the gauge's unit; power given | 0.3419 → 0.3885; raw +13.6% (95%: +11.5% to +15.7%), +0.0466 in the gauge's unit; power given | **power given in all three of our runs** |
| host CPU-seconds | 635.6 | 705.7 | 635.6 → 705.7; raw +11.0% (95%: +6.4% to +15.6%); power given | 750.7 → 835.5; raw +11.3% (95%: +2.8% to +19.8%); power given | 593.9 → 676.8; raw +14.0% (95%: +11.9% to +16.0%); power given | **power given in all three of our runs** |
| host CPU-seconds per 1,000 messages inside the line | 1.94 | 1.84 | 1.939 → 1.836; raw −5.3% (95%: −10.4% to −0.3%); GAIN | 2.306 → 2.184; raw −5.3% (95%: −13.0% to +2.4%); GAIN | 1.815 → 1.764; raw −2.9% (95%: −5.2% to −0.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| consumer changes written (the knob's moves) | 2 | 14.0 | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 1 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 24 gauge-rows GAIN, 0 LOSS, 12 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 6 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
