# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 42407564542 | `b806aadd5bbb` | omni-v26 (digest 75d3c22eed4473b9, 65 files) | 4 |
| B | 42419219065 | `84462b32eacc` | omni-v26 (digest 75d3c22eed4473b9, 65 files) | 4 |
| C | 42429039058 | `25130545f054` | omni-v26 (digest 75d3c22eed4473b9, 65 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 975, 982, 965 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.4 | 428.2 | 366.4 → 428.2; raw +16.9% (95%: +16.3% to +17.5%); GAIN | 368.7 → 431.8; raw +17.1% (95%: +16.7% to +17.5%); GAIN | 363.5 → 424.2; raw +16.7% (95%: +13.8% to +19.6%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 428.7 | 428.7 | 428.7 → 428.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 431.8 → 431.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 424.4 → 424.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,305 | 9.85 | 2305 → 9.847; raw −99.6% (95%: −101.2% to −97.9%); GAIN | 2335 → 8.75; raw −99.6% (95%: −107.4% to −91.9%); GAIN | 2158 → 9.792; raw −99.5% (95%: −139.0% to −60.0%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,562 | 18.1 | 3562 → 18.13; raw −99.5% (95%: −105.6% to −93.4%); GAIN | 3689 → 10.75; raw −99.7% (95%: −104.7% to −94.7%); GAIN | 3376 → 23.92; raw −99.3% (95%: −125.8% to −72.8%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 8.3 | 7.1 | 8.302 → 7.096; raw −14.5% (95%: −23.1% to −5.9%); GAIN | 7.971 → 6.47; raw −18.8% (95%: −21.2% to −16.5%); GAIN | 8.234 → 7.2; raw −12.6% (95%: −15.4% to −9.7%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 301.2 | 8.94 | 301.2 → 8.944; raw −97.0% (95%: −100.2% to −93.8%); GAIN | 313.7 → 6.896; raw −97.8% (95%: −102.6% to −93.0%); GAIN | 284.3 → 8.083; raw −97.2% (95%: −138.6% to −55.7%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 1,645 | 127.7 | 1645 → 127.7; raw −92.2% (95%: −121.7% to −62.8%); GAIN | 1676 → 27.33; raw −98.4% (95%: −103.7% to −93.0%); GAIN | 1565 → 111.7; raw −92.9% (95%: −127.8% to −58.0%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 133.0 | 3.98 | 133 → 3.977; raw −97.0% (95%: −100.1% to −94.0%); GAIN | 140.5 → 3.043; raw −97.8% (95%: −102.8% to −92.9%); GAIN | 124.4 → 3.559; raw −97.1% (95%: −136.7% to −57.6%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.97 | 2 → 4.971; raw +148.6% (95%: +39.5% to +257.7%); power given | 2 → 5.22; raw +161.0% (95%: +138.2% to +183.8%); power given | 2 → 4.949; raw +147.5% (95%: +72.1% to +222.8%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 7 | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.308 | 0.322 | 0.3083 → 0.3217; raw +4.3% (95%: −4.0% to +12.7%), +0.0134 in the gauge's unit; power given | 0.2696 → 0.2842; raw +5.4% (95%: +2.2% to +8.6%), +0.0146 in the gauge's unit; power given | 0.2968 → 0.3107; raw +4.7% (95%: +4.3% to +5.1%), +0.0139 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds | 548.6 | 571.4 | 548.6 → 571.4; raw +4.1% (95%: −4.2% to +12.5%); power given | 480.8 → 506.2; raw +5.3% (95%: +2.3% to +8.3%); power given | 528.3 → 552.3; raw +4.6% (95%: +4.3% to +4.8%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 2.96 | 3.326 → 2.964; raw −10.9% (95%: −18.5% to −3.3%); GAIN | 2.898 → 2.604; raw −10.1% (95%: −13.3% to −7.0%); GAIN | 3.229 → 2.893; raw −10.4% (95%: −13.4% to −7.4%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 12.0 | 2 → 12; raw +500.0% (95%: +69.7% to +930.3%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 12; raw +500.0% (95%: +69.7% to +930.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 3 (2 trials, 1 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 973, 978, 978 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.7 | 417.4 | 340.7 → 417.4; raw +22.5% (95%: +20.6% to +24.5%); GAIN | 341.5 → 420.8; raw +23.2% (95%: +22.6% to +23.9%); GAIN | 341.6 → 421.4; raw +23.4% (95%: +23.2% to +23.5%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 418.3 | 419.1 | 418.3 → 419.1; raw +0.2% (95%: −0.2% to +0.6%); STEADY | 420.4 → 420.8; raw +0.1% (95%: −0.3% to +0.5%); STEADY | 420.3 → 421.5; raw +0.3% (95%: +0.3% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.18%) |
| end-to-end latency, 95th percentile (ms) | 2,516 | 11.7 | 2516 → 11.71; raw −99.5% (95%: −106.7% to −92.3%); GAIN | 2606 → 11.07; raw −99.6% (95%: −106.5% to −92.7%); GAIN | 2582 → 11.02; raw −99.6% (95%: −111.7% to −87.5%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,690 | 298.6 | 3690 → 298.6; raw −91.9% (95%: −125.8% to −58.0%); GAIN | 3850 → 32.53; raw −99.2% (95%: −114.2% to −84.1%); GAIN | 3836 → 33.51; raw −99.1% (95%: −114.8% to −83.5%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 9.16 | 8.14 | 9.164 → 8.142; raw −11.1% (95%: −14.0% to −8.3%); GAIN | 9.309 → 7.935; raw −14.8% (95%: −16.2% to −13.4%); GAIN | 9.279 → 7.941; raw −14.4% (95%: −26.9% to −1.9%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 377.7 | 16.2 | 377.7 → 16.16; raw −95.7% (95%: −103.9% to −87.5%); GAIN | 395.2 → 8.315; raw −97.9% (95%: −99.3% to −96.5%); GAIN | 391.6 → 8.426; raw −97.8% (95%: −99.8% to −95.9%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 1,651 | 291.3 | 1651 → 291.3; raw −82.4% (95%: −131.7% to −33.0%); GAIN | 1725 → 59.33; raw −96.6% (95%: −106.9% to −86.2%); GAIN | 1713 → 87.67; raw −94.9% (95%: −107.2% to −82.6%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 163.2 | 7.08 | 163.2 → 7.084; raw −95.7% (95%: −103.5% to −87.8%); GAIN | 172 → 3.551; raw −97.9% (95%: −99.5% to −96.3%); GAIN | 170.1 → 3.98; raw −97.7% (95%: −101.3% to −94.0%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.17 | 2 → 5.172; raw +158.6% (95%: +88.2% to +229.0%); power given | 2 → 6.302; raw +215.1% (95%: +154.4% to +275.8%); power given | 2 → 4.923; raw +146.1% (95%: +82.4% to +209.9%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.316 | 0.337 | 0.3155 → 0.3372; raw +6.9% (95%: +1.5% to +12.2%), +0.0217 in the gauge's unit; power given | 0.3064 → 0.3292; raw +7.4% (95%: +1.7% to +13.2%), +0.0228 in the gauge's unit; power given | 0.3046 → 0.3232; raw +6.1% (95%: +0.7% to +11.5%), +0.0186 in the gauge's unit; power given | **power given in all three of our runs** |
| host CPU-seconds | 222.3 | 236.9 | 222.3 → 236.9; raw +6.5% (95%: +0.9% to +12.2%); power given | 215.8 → 231.5; raw +7.3% (95%: +1.8% to +12.8%); power given | 214.5 → 226.8; raw +5.8% (95%: +0.2% to +11.3%); power given | **power given in all three of our runs** |
| host CPU-seconds per 1,000 messages inside the line | 3.61 | 3.15 | 3.613 → 3.147; raw −12.9% (95%: −16.7% to −9.0%); GAIN | 3.498 → 3.049; raw −12.8% (95%: −18.0% to −7.7%); GAIN | 3.476 → 2.988; raw −14.0% (95%: −19.4% to −8.6%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 14.0 | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 16; raw +700.0% (95%: +269.7% to +1130.3%) | 2 → 12; raw +500.0% (95%: +69.7% to +930.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 390, 391 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.3 | 173.0 | 147.3 → 173; raw +17.4% (95%: +17.4% to +17.5%); GAIN | 146.6 → 171.2; raw +16.8% (95%: +16.3% to +17.3%); GAIN | 147.4 → 171.5; raw +16.4% (95%: +16.2% to +16.7%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 173.1 | 173.1 | 173.1 → 173.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 171.4 → 171.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 171.7 → 171.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,500 | 12.5 | 2500 → 12.55; raw −99.5% (95%: −102.2% to −96.8%); GAIN | 2181 → 12.7; raw −99.4% (95%: −103.7% to −95.1%); GAIN | 2115 → 11.72; raw −99.4% (95%: −104.3% to −94.6%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,830 | 36.5 | 3830 → 36.48; raw −99.0% (95%: −104.7% to −93.4%); GAIN | 3445 → 17.08; raw −99.5% (95%: −104.9% to −94.1%); GAIN | 3285 → 15.36; raw −99.5% (95%: −105.9% to −93.2%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 11.6 | 11.3 | 11.55 → 11.27; raw −2.5% (95%: −2.5% to −2.4%); GAIN | 11.44 → 11.28; raw −1.4% (95%: −2.7% to −0.1%); GAIN | 10.68 → 10.64; raw −0.3% (95%: −1.2% to +0.5%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| end-to-end latency, mean (ms) | 335.2 | 11.9 | 335.2 → 11.89; raw −96.5% (95%: −96.9% to −96.0%); GAIN | 288 → 12.31; raw −95.7% (95%: −101.8% to −89.6%); GAIN | 277 → 11.53; raw −95.8% (95%: −97.5% to −94.2%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 715.0 | 45.0 | 715 → 45; raw −93.7% (95%: −107.2% to −80.2%); GAIN | 660.3 → 58; raw −91.2% (95%: −98.4% to −84.1%); GAIN | 646.3 → 62; raw −90.4% (95%: −111.6% to −69.3%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 61.2 | 2.08 | 61.18 → 2.082; raw −96.6% (95%: −99.6% to −93.6%); GAIN | 52.65 → 2.184; raw −95.9% (95%: −100.7% to −91.0%); GAIN | 51.24 → 2.086; raw −95.9% (95%: −96.8% to −95.1%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.75 | 2 → 4.75; raw +137.5% (95%: +125.5% to +149.5%); power given | 2 → 3.454; raw +72.7% (95%: +21.9% to +123.5%); power given | 2 → 4.1; raw +105.0% (95%: −40.5% to +250.4%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 5; raw +150.0% (95%: +150.0% to +150.0%); power given | 2 → 6; raw +200.0% (95%: −15.1% to +415.2%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.288 | 0.296 | 0.288 → 0.2961; raw +2.8% (95%: +1.1% to +4.6%), +0.0082 in the gauge's unit; power given | 0.2863 → 0.2925; raw +2.2% (95%: −2.0% to +6.3%), +0.0062 in the gauge's unit; power given | 0.2534 → 0.2584; raw +2.0% (95%: ±0.0% to +3.9%), +0.0050 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds | 509.3 | 523.0 | 509.3 → 523; raw +2.7% (95%: +0.9% to +4.5%); power given | 514.9 → 525.1; raw +2.0% (95%: −2.1% to +6.1%); power given | 453.8 → 462.3; raw +1.9% (95%: −0.1% to +3.8%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.67 | 6.71 | 7.674 → 6.711; raw −12.5% (95%: −14.7% to −10.4%); GAIN | 7.793 → 6.806; raw −12.7% (95%: −16.2% to −9.2%); GAIN | 6.835 → 5.981; raw −12.5% (95%: −14.0% to −11.0%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 14.0 | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%) | 2 → 10; raw +400.0% (95%: −30.3% to +830.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 4 (2 trials, 2 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,923, 1,945, 1,945 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724.7 | 845.1 | 724.7 → 845.1; raw +16.6% (95%: +16.0% to +17.2%); GAIN | 729 → 855.7; raw +17.4% (95%: +17.3% to +17.5%); GAIN | 733.1 → 855.6; raw +16.7% (95%: +16.2% to +17.2%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 846.1 | 846.1 | 846.1 → 846.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 855.7 → 855.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 855.6 → 855.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,185 | 9.25 | 2185 → 9.254; raw −99.6% (95%: −101.4% to −97.8%); GAIN | 2486 → 8.962; raw −99.6% (95%: −102.8% to −96.5%); GAIN | 2222 → 8.165; raw −99.6% (95%: −110.4% to −88.8%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,510 | 11.3 | 3510 → 11.3; raw −99.7% (95%: −108.5% to −90.8%); GAIN | 3860 → 10.25; raw −99.7% (95%: −107.0% to −92.5%); GAIN | 3423 → 9.801; raw −99.7% (95%: −105.7% to −93.7%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 7.83 | 6.08 | 7.828 → 6.081; raw −22.3% (95%: −25.9% to −18.7%); GAIN | 7.32 → 5.921; raw −19.1% (95%: −22.6% to −15.6%); GAIN | 7.659 → 5.33; raw −30.4% (95%: −43.5% to −17.3%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 289.5 | 7.9 | 289.5 → 7.9; raw −97.3% (95%: −102.0% to −92.5%); GAIN | 325.5 → 6.024; raw −98.1% (95%: −98.8% to −97.5%); GAIN | 295.8 → 5.713; raw −98.1% (95%: −105.4% to −90.8%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 3,131 | 194.0 | 3131 → 194; raw −93.8% (95%: −111.5% to −76.1%); GAIN | 3413 → 20.33; raw −99.4% (95%: −101.4% to −97.4%); GAIN | 3166 → 42; raw −98.7% (95%: −102.4% to −95.0%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 250.2 | 6.95 | 250.2 → 6.951; raw −97.2% (95%: −102.1% to −92.3%); GAIN | 282.8 → 5.254; raw −98.1% (95%: −98.7% to −97.6%); GAIN | 259.5 → 5.016; raw −98.1% (95%: −104.8% to −91.4%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.72 | 2 → 5.718; raw +185.9% (95%: +123.1% to +248.7%); power given | 2 → 5.202; raw +160.1% (95%: +149.9% to +170.3%); power given | 2 → 5.718; raw +185.9% (95%: +142.8% to +229.0%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.343 | 0.391 | 0.3425 → 0.391; raw +14.2% (95%: +11.7% to +16.6%), +0.0485 in the gauge's unit; power given | 0.3463 → 0.3789; raw +9.4% (95%: +7.7% to +11.1%), +0.0325 in the gauge's unit; power given | 0.2873 → 0.3128; raw +8.8% (95%: +7.8% to +9.9%), +0.0254 in the gauge's unit; power given | **power given in all three of our runs** |
| host CPU-seconds | 594.1 | 680.5 | 594.1 → 680.5; raw +14.6% (95%: +12.2% to +16.9%); power given | 621.1 → 674.1; raw +8.5% (95%: +6.4% to +10.7%); power given | 511.8 → 556; raw +8.6% (95%: +7.6% to +9.7%); power given | **power given in all three of our runs** |
| host CPU-seconds per 1,000 messages inside the line | 1.82 | 1.79 | 1.821 → 1.789; raw −1.8% (95%: −4.4% to +0.8%); GAIN | 1.893 → 1.75; raw −7.5% (95%: −9.7% to −5.4%); GAIN | 1.551 → 1.444; raw −6.9% (95%: −7.5% to −6.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| consumer changes written (the knob's moves) | 2 | 18.0 | 2 → 18; raw +800.0% (95%: +369.7% to +1230.3%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 24 gauge-rows GAIN, 0 LOSS, 12 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 6 STEADY, 0 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
