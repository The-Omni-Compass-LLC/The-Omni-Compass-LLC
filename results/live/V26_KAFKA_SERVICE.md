# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 42408820342 | `e81cb06c22b0` | omni-v26 (digest 75d3c22eed4473b9, 65 files) | 4 |
| B | 42419242767 | `84462b32eacc` | omni-v26 (digest 75d3c22eed4473b9, 65 files) | 4 |
| C | 42430252207 | `25130545f054` | omni-v26 (digest 75d3c22eed4473b9, 65 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 982, 963, 979 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367.6 | 431.9 | 367.6 → 431.9; raw +17.5% (95%: +17.2% to +17.8%); GAIN | 363.9 → 423.7; raw +16.4% (95%: +8.9% to +24.0%); GAIN | 368.1 → 430.7; raw +17.0% (95%: +16.8% to +17.2%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 432.0 | 432.0 | 432 → 432; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 423.7 → 423.7; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 430.8 → 430.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,477 | 9.13 | 2477 → 9.131; raw −99.6% (95%: −103.8% to −95.5%); GAIN | 2413 → 9.034; raw −99.6% (95%: −213.8% to +14.5%); GAIN | 2324 → 8.954; raw −99.6% (95%: −105.1% to −94.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| end-to-end latency, 99th percentile (ms) | 3,895 | 11.8 | 3895 → 11.83; raw −99.7% (95%: −106.3% to −93.1%); GAIN | 3822 → 13.43; raw −99.6% (95%: −192.6% to −6.7%); GAIN | 3584 → 13.15; raw −99.6% (95%: −107.0% to −92.3%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 8.06 | 6.67 | 8.061 → 6.673; raw −17.2% (95%: −19.1% to −15.3%); GAIN | 8.075 → 6.634; raw −17.8% (95%: −22.0% to −13.7%); GAIN | 8.083 → 6.563; raw −18.8% (95%: −20.2% to −17.4%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 334.1 | 7.14 | 334.1 → 7.137; raw −97.9% (95%: −101.4% to −94.3%); GAIN | 325.7 → 7.011; raw −97.8% (95%: −225.8% to +30.1%); GAIN | 308.9 → 7.193; raw −97.7% (95%: −99.1% to −96.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| consumer lag, most messages waiting at once | 1,737 | 35.7 | 1737 → 35.67; raw −97.9% (95%: −100.8% to −95.1%); GAIN | 1699 → 27.67; raw −98.4% (95%: −175.4% to −21.4%); GAIN | 1658 → 84; raw −94.9% (95%: −108.0% to −81.9%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 149.1 | 3.1 | 149.1 → 3.099; raw −97.9% (95%: −100.1% to −95.7%); GAIN | 141.9 → 3.061; raw −97.8% (95%: −221.7% to +26.1%); GAIN | 137.1 → 3.268; raw −97.6% (95%: −99.1% to −96.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.27 | 2 → 5.266; raw +163.3% (95%: +139.7% to +186.9%); power given | 2 → 5.889; raw +194.5% (95%: +153.6% to +235.3%); power given | 2 → 5.417; raw +170.8% (95%: +124.4% to +217.3%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.278 | 0.299 | 0.2779 → 0.2989; raw +7.6% (95%: +5.4% to +9.7%), +0.0210 in the gauge's unit; power given | 0.2818 → 0.296; raw +5.0% (95%: −2.5% to +12.6%), +0.0142 in the gauge's unit; power given | 0.2849 → 0.2942; raw +3.2% (95%: −1.6% to +8.1%), +0.0093 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 495.5 | 532.2 | 495.5 → 532.2; raw +7.4% (95%: +5.0% to +9.8%); power given | 502.5 → 526.9; raw +4.9% (95%: −2.4% to +12.1%); power given | 508.1 → 523.7; raw +3.1% (95%: −1.8% to +7.9%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 2.99 | 2.74 | 2.995 → 2.738; raw −8.6% (95%: −10.1% to −7.1%); GAIN | 3.069 → 2.763; raw −10.0% (95%: −18.1% to −1.9%); GAIN | 3.066 → 2.702; raw −11.9% (95%: −16.8% to −7.0%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 14.0 | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 18; raw +800.0% (95%: +369.7% to +1230.3%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (0 trials, 0 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 978, 974, 976 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341.8 | 421.2 | 341.8 → 421.2; raw +23.2% (95%: +22.9% to +23.6%); GAIN | 341.7 → 419.9; raw +22.9% (95%: +22.7% to +23.1%); GAIN | 341 → 420; raw +23.2% (95%: +21.9% to +24.4%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 420.3 | 421.4 | 420.3 → 421.4; raw +0.3% (95%: +0.3% to +0.3%); STEADY | 418.7 → 419.9; raw +0.3% (95%: +0.3% to +0.3%); STEADY | 419.3 → 420.1; raw +0.2% (95%: −0.2% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.25%) |
| end-to-end latency, 95th percentile (ms) | 2,668 | 11.1 | 2668 → 11.13; raw −99.6% (95%: −114.0% to −85.2%); GAIN | 2490 → 10.56; raw −99.6% (95%: −104.0% to −95.2%); GAIN | 2547 → 10.84; raw −99.6% (95%: −108.3% to −90.8%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,847 | 52.7 | 3847 → 52.74; raw −98.6% (95%: −107.3% to −90.0%); GAIN | 3496 → 24.68; raw −99.3% (95%: −107.2% to −91.4%); GAIN | 3832 → 65.21; raw −98.3% (95%: −109.1% to −87.5%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 8.72 | 7.89 | 8.716 → 7.894; raw −9.4% (95%: −16.2% to −2.7%); GAIN | 8.445 → 7.57; raw −10.4% (95%: −12.1% to −8.6%); GAIN | 8.858 → 7.662; raw −13.5% (95%: −18.7% to −8.4%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 393.8 | 9.21 | 393.8 → 9.212; raw −97.7% (95%: −109.3% to −86.1%); GAIN | 365.4 → 7.696; raw −97.9% (95%: −97.9% to −97.9%); GAIN | 384.9 → 8.724; raw −97.7% (95%: −103.8% to −91.7%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 1,736 | 82.7 | 1736 → 82.67; raw −95.2% (95%: −108.8% to −81.7%); GAIN | 1608 → 14.33; raw −99.1% (95%: −100.6% to −97.6%); GAIN | 1711 → 119.3; raw −93.0% (95%: −115.8% to −70.2%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 170.6 | 4.2 | 170.6 → 4.202; raw −97.5% (95%: −108.7% to −86.4%); GAIN | 157.9 → 3.149; raw −98.0% (95%: −98.9% to −97.1%); GAIN | 166.5 → 4.18; raw −97.5% (95%: −103.0% to −92.0%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.42 | 2 → 5.419; raw +170.9% (95%: +121.6% to +220.3%); power given | 2 → 5.044; raw +152.2% (95%: +72.3% to +232.1%); power given | 2 → 4.919; raw +146.0% (95%: +115.6% to +176.3%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.311 | 0.325 | 0.3106 → 0.3253; raw +4.8% (95%: +0.5% to +9.1%), +0.0148 in the gauge's unit; power given | 0.2858 → 0.3015; raw +5.5% (95%: +3.3% to +7.6%), +0.0157 in the gauge's unit; power given | 0.2891 → 0.3072; raw +6.2% (95%: +0.4% to +12.1%), +0.0180 in the gauge's unit; power given | **power given in all three of our runs** |
| host CPU-seconds | 221.8 | 230.8 | 221.8 → 230.8; raw +4.0% (95%: −0.1% to +8.2%); power given | 204.3 → 214.6; raw +5.0% (95%: +2.8% to +7.3%); power given | 206.6 → 218.7; raw +5.9% (95%: +0.5% to +11.3%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.59 | 3.04 | 3.593 → 3.042; raw −15.3% (95%: −19.0% to −11.6%); GAIN | 3.311 → 2.838; raw −14.3% (95%: −16.6% to −12.0%); GAIN | 3.355 → 2.889; raw −13.9% (95%: −17.9% to −9.9%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 14.0 | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 12; raw +500.0% (95%: +69.7% to +930.3%) | 2 → 16; raw +700.0% (95%: +269.7% to +1130.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 391, 394, 394 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146.9 | 171.5 | 146.9 → 171.5; raw +16.8% (95%: +15.9% to +17.6%); GAIN | 147.1 → 172.9; raw +17.6% (95%: +16.9% to +18.2%); GAIN | 147.4 → 172.8; raw +17.2% (95%: +16.6% to +17.8%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 172.0 | 172.0 | 172 → 172; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 173.2 → 173.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 173.1 → 173.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,261 | 12.1 | 2261 → 12.05; raw −99.5% (95%: −108.0% to −91.0%); GAIN | 2569 → 12.65; raw −99.5% (95%: −104.2% to −94.8%); GAIN | 2440 → 11.89; raw −99.5% (95%: −105.6% to −93.4%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,453 | 16.8 | 3453 → 16.8; raw −99.5% (95%: −100.6% to −98.4%); GAIN | 3893 → 43.19; raw −98.9% (95%: −103.0% to −94.8%); GAIN | 3711 → 15.81; raw −99.6% (95%: −106.0% to −93.2%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 11.2 | 11.0 | 11.21 → 11.04; raw −1.5% (95%: −1.9% to −1.1%); GAIN | 11.55 → 11.27; raw −2.4% (95%: −2.6% to −2.3%); GAIN | 10.81 → 10.67; raw −1.3% (95%: −5.4% to +2.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| end-to-end latency, mean (ms) | 299.3 | 15.0 | 299.3 → 15.02; raw −95.0% (95%: −102.2% to −87.8%); GAIN | 345.3 → 13.38; raw −96.1% (95%: −102.3% to −89.9%); GAIN | 322.9 → 12.56; raw −96.1% (95%: −104.0% to −88.2%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 670.3 | 161.3 | 670.3 → 161.3; raw −75.9% (95%: −93.3% to −58.6%); GAIN | 715 → 99; raw −86.2% (95%: −103.4% to −68.9%); GAIN | 699.3 → 82.67; raw −88.2% (95%: −100.6% to −75.8%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 54.9 | 2.71 | 54.88 → 2.715; raw −95.1% (95%: −101.3% to −88.8%); GAIN | 62.6 → 2.455; raw −96.1% (95%: −101.7% to −90.4%); GAIN | 59 → 2.213; raw −96.2% (95%: −103.4% to −89.1%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.55 | 2 → 3.549; raw +77.5% (95%: +50.4% to +104.6%); power given | 2 → 4.265; raw +113.2% (95%: +85.5% to +140.9%); power given | 2 → 4.111; raw +105.6% (95%: −18.0% to +229.1%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 5 | 2 → 5; raw +150.0% (95%: +150.0% to +150.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 6; raw +200.0% (95%: −15.1% to +415.2%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.28 | 0.284 | 0.28 → 0.2838; raw +1.3% (95%: −1.0% to +3.7%), +0.0038 in the gauge's unit; power given | 0.2872 → 0.2941; raw +2.4% (95%: −0.4% to +5.3%), +0.0069 in the gauge's unit; power given | 0.2616 → 0.2679; raw +2.4% (95%: −2.6% to +7.4%), +0.0063 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 504.9 | 510.9 | 504.9 → 510.9; raw +1.2% (95%: −1.1% to +3.5%); power given | 507.8 → 519.4; raw +2.3% (95%: −0.5% to +5.1%); power given | 468.3 → 479; raw +2.3% (95%: −2.7% to +7.3%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 7.63 | 6.61 | 7.627 → 6.61; raw −13.3% (95%: −15.0% to −11.6%); GAIN | 7.662 → 6.665; raw −13.0% (95%: −15.9% to −10.1%); GAIN | 7.049 → 6.151; raw −12.7% (95%: −18.6% to −6.8%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 10; raw +400.0% (95%: −30.3% to +830.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,940, 1,941, 1,938 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727.1 | 852.9 | 727.1 → 852.9; raw +17.3% (95%: +16.9% to +17.7%); GAIN | 726.3 → 853.3; raw +17.5% (95%: +17.3% to +17.7%); GAIN | 725.2 → 851.2; raw +17.4% (95%: +16.6% to +18.1%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 853.2 | 853.2 | 853.2 → 853.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 853.6 → 853.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 852.6 → 852.6; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,403 | 8.74 | 2403 → 8.738; raw −99.6% (95%: −109.3% to −90.0%); GAIN | 2478 → 9.242; raw −99.6% (95%: −102.1% to −97.1%); GAIN | 2569 → 9.921; raw −99.6% (95%: −101.8% to −97.4%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,796 | 12.3 | 3796 → 12.29; raw −99.7% (95%: −111.5% to −87.8%); GAIN | 3932 → 13.02; raw −99.7% (95%: −101.7% to −97.6%); GAIN | 3876 → 13.87; raw −99.6% (95%: −101.3% to −98.0%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 7.37 | 5.74 | 7.371 → 5.736; raw −22.2% (95%: −25.0% to −19.4%); GAIN | 7.875 → 6.087; raw −22.7% (95%: −30.5% to −15.0%); GAIN | 8.142 → 6.424; raw −21.1% (95%: −26.2% to −16.0%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 321.9 | 6.64 | 321.9 → 6.637; raw −97.9% (95%: −110.0% to −85.8%); GAIN | 337.2 → 6.935; raw −97.9% (95%: −99.8% to −96.1%); GAIN | 338.7 → 9.363; raw −97.2% (95%: −100.9% to −93.5%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 3,351 | 92.0 | 3351 → 92; raw −97.3% (95%: −112.6% to −81.9%); GAIN | 3442 → 121.7; raw −96.5% (95%: −105.2% to −87.7%); GAIN | 3425 → 413; raw −87.9% (95%: −135.4% to −40.5%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 279.2 | 5.75 | 279.2 → 5.746; raw −97.9% (95%: −110.3% to −85.6%); GAIN | 293 → 6.169; raw −97.9% (95%: −99.2% to −96.5%); GAIN | 292.7 → 8.247; raw −97.2% (95%: −101.1% to −93.3%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.51 | 2 → 5.506; raw +175.3% (95%: +137.9% to +212.6%); power given | 2 → 5.43; raw +171.5% (95%: +148.8% to +194.2%); power given | 2 → 5.523; raw +176.2% (95%: +108.4% to +243.9%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.318 | 0.35 | 0.3183 → 0.3503; raw +10.0% (95%: +7.9% to +12.2%), +0.0320 in the gauge's unit; power given | 0.3453 → 0.3922; raw +13.6% (95%: +8.0% to +19.1%), +0.0468 in the gauge's unit; power given | 0.3772 → 0.4477; raw +18.7% (95%: +15.7% to +21.7%), +0.0705 in the gauge's unit; power given | **power given in all three of our runs** |
| host CPU-seconds | 564.7 | 620.9 | 564.7 → 620.9; raw +10.0% (95%: +7.8% to +12.2%); power given | 600.2 → 682.3; raw +13.7% (95%: +8.1% to +19.3%); power given | 655.3 → 780; raw +19.0% (95%: +15.9% to +22.1%); power given | **power given in all three of our runs** |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.62 | 1.725 → 1.617; raw −6.3% (95%: −8.2% to −4.3%); GAIN | 1.836 → 1.776; raw −3.2% (95%: −8.7% to +2.3%); GAIN | 2.007 → 2.036; raw +1.4% (95%: −1.8% to +4.6%); power given | **the runs disagree** |
| consumer changes written (the knob's moves) | 2 | 16.0 | 2 → 16; raw +700.0% (95%: +269.7% to +1130.3%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 23 gauge-rows GAIN, 0 LOSS, 12 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 6 STEADY, 1 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
