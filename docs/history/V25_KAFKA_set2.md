# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Lost messages: any rise in any run reads **LOSS in at least one of our runs**. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 41756685178 | `198314d551ea` | omni-v25 (digest cf56fc0a7b707452, 65 files) | 4 |
| B | 41770452498 | `db6e040b4584` | omni-v25 (digest cf56fc0a7b707452, 65 files) | 4 |
| C | 41783615016 | `0a92e09fe669` | omni-v25 (digest cf56fc0a7b707452, 65 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 979, 968, 980 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367.8 | 430.8 | 367.8 → 430.8; raw +17.1% (95%: +16.8% to +17.5%); GAIN | 365.2 → 425.9; raw +16.6% (95%: +16.3% to +16.9%); GAIN | 367.1 → 430.5; raw +17.3% (95%: +16.5% to +18.1%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 430.8 | 430.8 | 430.8 → 430.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 426 → 426; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 431 → 431; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,342 | 9.17 | 2342 → 9.175; raw −99.6% (95%: −108.0% to −91.2%); GAIN | 2169 → 10.15; raw −99.5% (95%: −101.8% to −97.3%); GAIN | 2454 → 9.982; raw −99.6% (95%: −103.3% to −95.9%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,688 | 11.2 | 3688 → 11.23; raw −99.7% (95%: −105.8% to −93.6%); GAIN | 3387 → 12.66; raw −99.6% (95%: −108.7% to −90.6%); GAIN | 3775 → 17.41; raw −99.5% (95%: −102.8% to −96.3%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 8.1 | 6.8 | 8.097 → 6.802; raw −16.0% (95%: −23.9% to −8.1%); GAIN | 8.62 → 7.339; raw −14.9% (95%: −16.4% to −13.3%); GAIN | 8.198 → 7.072; raw −13.7% (95%: −16.2% to −11.3%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 314.5 | 6.95 | 314.5 → 6.955; raw −97.8% (95%: −102.4% to −93.2%); GAIN | 282.1 → 7.862; raw −97.2% (95%: −101.0% to −93.4%); GAIN | 324.5 → 9.214; raw −97.2% (95%: −102.2% to −92.1%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 1,686 | 25.3 | 1686 → 25.33; raw −98.5% (95%: −102.6% to −94.4%); GAIN | 1583 → 67.67; raw −95.7% (95%: −98.3% to −93.2%); GAIN | 1725 → 220.3; raw −87.2% (95%: −116.7% to −57.8%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 140.4 | 3.14 | 140.4 → 3.144; raw −97.8% (95%: −102.7% to −92.8%); GAIN | 124.2 → 3.568; raw −97.1% (95%: −100.4% to −93.9%); GAIN | 143.5 → 4.19; raw −97.1% (95%: −101.5% to −92.7%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.87 | 2 → 4.869; raw +143.5% (95%: +104.9% to +182.0%); power given | 2 → 5.858; raw +192.9% (95%: +126.9% to +258.9%); power given | 2 → 4.911; raw +145.6% (95%: +70.4% to +220.7%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 7 | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.281 | 0.301 | 0.2812 → 0.3009; raw +7.0% (95%: −6.0% to +20.0%), +0.0196 in the gauge's unit; power given | 0.3225 → 0.3395; raw +5.3% (95%: +4.9% to +5.7%), +0.0170 in the gauge's unit; power given | 0.2993 → 0.3147; raw +5.2% (95%: +2.9% to +7.4%), +0.0154 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds | 501.8 | 535.4 | 501.8 → 535.4; raw +6.7% (95%: −6.2% to +19.6%); power given | 564.6 → 594.6; raw +5.3% (95%: +4.6% to +6.0%); power given | 532.2 → 559.2; raw +5.1% (95%: +2.6% to +7.5%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 3.03 | 2.76 | 3.032 → 2.761; raw −8.9% (95%: −20.5% to +2.6%); GAIN | 3.434 → 3.102; raw −9.7% (95%: −10.1% to −9.2%); GAIN | 3.221 → 2.885; raw −10.4% (95%: −12.2% to −8.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| consumer changes written (the knob's moves) | 2 | 12.0 | 2 → 12; raw +500.0% (95%: +69.7% to +930.3%) | 2 → 16; raw +700.0% (95%: +269.7% to +1130.3%) | 2 → 12; raw +500.0% (95%: +69.7% to +930.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 975, 974, 978 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339.9 | 419.5 | 339.9 → 419.5; raw +23.4% (95%: +22.9% to +23.9%); GAIN | 341.1 → 419.9; raw +23.1% (95%: +22.9% to +23.3%); GAIN | 341.5 → 420.9; raw +23.3% (95%: +22.6% to +23.9%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 418.9 | 419.7 | 418.9 → 419.7; raw +0.2% (95%: −0.2% to +0.6%); STEADY | 418.7 → 419.9; raw +0.3% (95%: +0.3% to +0.3%); STEADY | 420.5 → 420.9; raw +0.1% (95%: −0.3% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.18%) |
| end-to-end latency, 95th percentile (ms) | 2,575 | 11.2 | 2575 → 11.22; raw −99.6% (95%: −109.3% to −89.9%); GAIN | 2484 → 11.22; raw −99.5% (95%: −101.2% to −97.9%); GAIN | 2582 → 11.08; raw −99.6% (95%: −104.6% to −94.5%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,702 | 36.9 | 3702 → 36.85; raw −99.0% (95%: −101.5% to −96.5%); GAIN | 3715 → 61.18; raw −98.4% (95%: −105.1% to −91.6%); GAIN | 3971 → 44.39; raw −98.9% (95%: −107.4% to −90.3%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 9.26 | 8.05 | 9.261 → 8.05; raw −13.1% (95%: −21.1% to −5.1%); GAIN | 9.126 → 7.973; raw −12.6% (95%: −19.4% to −5.8%); GAIN | 9.355 → 7.945; raw −15.1% (95%: −22.8% to −7.3%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 388.0 | 8.89 | 388 → 8.888; raw −97.7% (95%: −105.3% to −90.1%); GAIN | 377.5 → 8.948; raw −97.6% (95%: −98.7% to −96.6%); GAIN | 395.3 → 8.614; raw −97.8% (95%: −98.4% to −97.3%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 1,685 | 54.7 | 1685 → 54.67; raw −96.8% (95%: −107.4% to −86.1%); GAIN | 1654 → 61.67; raw −96.3% (95%: −103.9% to −88.6%); GAIN | 1731 → 88.33; raw −94.9% (95%: −107.7% to −82.1%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 167.6 | 4.03 | 167.6 → 4.028; raw −97.6% (95%: −105.5% to −89.7%); GAIN | 164 → 3.842; raw −97.7% (95%: −98.4% to −96.9%); GAIN | 170.9 → 3.928; raw −97.7% (95%: −97.9% to −97.5%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.78 | 2 → 4.78; raw +139.0% (95%: +77.2% to +200.8%); power given | 2 → 5.193; raw +159.7% (95%: +75.5% to +243.8%); power given | 2 → 5.306; raw +165.3% (95%: +121.2% to +209.4%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 7 | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | 2 → 7; raw +250.0% (95%: +34.9% to +465.2%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.309 | 0.329 | 0.3087 → 0.3294; raw +6.7% (95%: +2.6% to +10.9%), +0.0207 in the gauge's unit; power given | 0.3035 → 0.3236; raw +6.6% (95%: +3.2% to +10.0%), +0.0201 in the gauge's unit; power given | 0.3053 → 0.3261; raw +6.8% (95%: +1.4% to +12.2%), +0.0208 in the gauge's unit; power given | **power given in all three of our runs** |
| host CPU-seconds | 217.3 | 231.3 | 217.3 → 231.3; raw +6.4% (95%: +2.4% to +10.4%); power given | 213.7 → 227.1; raw +6.3% (95%: +2.9% to +9.7%); power given | 215 → 229.2; raw +6.6% (95%: +1.6% to +11.7%); power given | **power given in all three of our runs** |
| host CPU-seconds per 1,000 messages inside the line | 3.54 | 3.06 | 3.54 → 3.058; raw −13.6% (95%: −17.9% to −9.3%); GAIN | 3.468 → 3.003; raw −13.4% (95%: −17.1% to −9.7%); GAIN | 3.485 → 3.018; raw −13.4% (95%: −18.8% to −8.0%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 14.0 | 2 → 14; raw +600.0% (95%: −145.3% to +1345.3%) | 2 → 14; raw +600.0% (95%: −145.3% to +1345.3%) | 2 → 16; raw +700.0% (95%: +269.7% to +1130.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 394, 390, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.1 | 173.1 | 147.1 → 173.1; raw +17.7% (95%: +17.6% to +17.7%); GAIN | 146.9 → 171.4; raw +16.6% (95%: +16.4% to +16.9%); GAIN | 146.8 → 172.5; raw +17.5% (95%: +17.1% to +17.8%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 173.2 | 173.2 | 173.2 → 173.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 171.5 → 171.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 172.8 → 172.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 2,509 | 12.5 | 2509 → 12.48; raw −99.5% (95%: −103.6% to −95.4%); GAIN | 2181 → 12.28; raw −99.4% (95%: −102.0% to −96.9%); GAIN | 2552 → 13.1; raw −99.5% (95%: −108.1% to −90.9%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 4,037 | 14.1 | 4037 → 14.1; raw −99.7% (95%: −107.1% to −92.2%); GAIN | 3420 → 15.97; raw −99.5% (95%: −108.5% to −90.5%); GAIN | 3739 → 17.3; raw −99.5% (95%: −102.1% to −97.0%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 11.6 | 11.4 | 11.59 → 11.39; raw −1.8% (95%: −3.1% to −0.4%); GAIN | 11.41 → 11.2; raw −1.9% (95%: −2.8% to −1.0%); GAIN | 11.67 → 11.52; raw −1.3% (95%: −2.9% to +0.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| end-to-end latency, mean (ms) | 341.5 | 11.2 | 341.5 → 11.22; raw −96.7% (95%: −97.7% to −95.8%); GAIN | 286.7 → 11.81; raw −95.9% (95%: −100.4% to −91.4%); GAIN | 334.6 → 13.74; raw −95.9% (95%: −101.1% to −90.7%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 723.0 | 36.7 | 723 → 36.67; raw −94.9% (95%: −97.7% to −92.2%); GAIN | 647.3 → 68; raw −89.5% (95%: −98.4% to −80.6%); GAIN | 704.7 → 118.3; raw −83.2% (95%: −95.2% to −71.2%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 62.5 | 1.98 | 62.49 → 1.982; raw −96.8% (95%: −97.2% to −96.4%); GAIN | 52.59 → 2.07; raw −96.1% (95%: −99.6% to −92.5%); GAIN | 61.36 → 2.498; raw −95.9% (95%: −101.7% to −90.2%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 6.58 | 2 → 6.577; raw +228.9% (95%: +227.9% to +229.8%); power given | 2 → 4.482; raw +124.1% (95%: −2.3% to +250.5%); power given | 2 → 3.558; raw +77.9% (95%: +51.7% to +104.1%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 6; raw +200.0% (95%: −15.1% to +415.2%); power given | 2 → 5; raw +150.0% (95%: +150.0% to +150.0%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.299 | 0.308 | 0.2994 → 0.3083; raw +3.0% (95%: −0.1% to +6.0%), +0.0089 in the gauge's unit; power given | 0.2815 → 0.2852; raw +1.3% (95%: −1.1% to +3.7%), +0.0037 in the gauge's unit; power given | 0.303 → 0.312; raw +3.0% (95%: −2.7% to +8.7%), +0.0090 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 537.9 | 552.8 | 537.9 → 552.8; raw +2.8% (95%: −0.1% to +5.7%); power given | 503.1 → 509.2; raw +1.2% (95%: −1.1% to +3.5%); power given | 543.6 → 558.1; raw +2.7% (95%: −2.7% to +8.0%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 messages inside the line | 8.11 | 7.09 | 8.114 → 7.086; raw −12.7% (95%: −15.5% to −9.8%); GAIN | 7.6 → 6.594; raw −13.2% (95%: −16.1% to −10.4%); GAIN | 8.215 → 7.18; raw −12.6% (95%: −17.1% to −8.1%); GAIN | **GAIN in all three of our runs** |
| consumer changes written (the knob's moves) | 2 | 14.0 | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 10; raw +400.0% (95%: −30.3% to +830.3%) | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (0 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); run C: acting: 2 to 3 (1 trials, 1 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,923, 1,942, 1,928 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729.1 | 844.7 | 729.1 → 844.7; raw +15.9% (95%: +15.2% to +16.5%); GAIN | 726.7 → 854.1; raw +17.5% (95%: +17.2% to +17.9%); GAIN | 725.3 → 847.3; raw +16.8% (95%: +16.6% to +17.0%); GAIN | **GAIN in all three of our runs** |
| throughput (messages a second consumed) | 845.9 | 845.9 | 845.9 → 845.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 854.2 → 854.2; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 848 → 848; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| end-to-end latency, 95th percentile (ms) | 1,976 | 8.98 | 1976 → 8.977; raw −99.5% (95%: −102.2% to −96.9%); GAIN | 2490 → 9.208; raw −99.6% (95%: −102.6% to −96.7%); GAIN | 2270 → 9.56; raw −99.6% (95%: −102.7% to −96.4%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, 99th percentile (ms) | 3,301 | 20.1 | 3301 → 20.14; raw −99.4% (95%: −107.6% to −91.1%); GAIN | 3854 → 11.05; raw −99.7% (95%: −104.8% to −94.6%); GAIN | 3593 → 11.28; raw −99.7% (95%: −100.1% to −99.3%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, median (ms) | 7.43 | 5.77 | 7.427 → 5.765; raw −22.4% (95%: −25.1% to −19.7%); GAIN | 7.823 → 6.058; raw −22.6% (95%: −26.7% to −18.4%); GAIN | 7.698 → 6.171; raw −19.8% (95%: −20.5% to −19.2%); GAIN | **GAIN in all three of our runs** |
| end-to-end latency, mean (ms) | 260.9 | 9.02 | 260.9 → 9.021; raw −96.5% (95%: −100.7% to −92.3%); GAIN | 336.3 → 6.581; raw −98.0% (95%: −101.8% to −94.3%); GAIN | 297.5 → 7.473; raw −97.5% (95%: −100.3% to −94.7%); GAIN | **GAIN in all three of our runs** |
| consumer lag, most messages waiting at once | 2,955 | 361.0 | 2955 → 361; raw −87.8% (95%: −129.6% to −46.0%); GAIN | 3426 → 62.67; raw −98.2% (95%: −102.0% to −94.4%); GAIN | 3224 → 256.3; raw −92.0% (95%: −97.6% to −86.5%); GAIN | **GAIN in all three of our runs** |
| consumer lag, mean messages waiting | 225.1 | 7.68 | 225.1 → 7.676; raw −96.6% (95%: −100.9% to −92.3%); GAIN | 292.8 → 5.753; raw −98.0% (95%: −101.3% to −94.7%); GAIN | 256.6 → 6.633; raw −97.4% (95%: −100.5% to −94.3%); GAIN | **GAIN in all three of our runs** |
| messages produced and never consumed | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.39 | 2 → 5.388; raw +169.4% (95%: +141.4% to +197.4%); power given | 2 → 5.785; raw +189.2% (95%: +122.7% to +255.8%); power given | 2 → 5.104; raw +155.2% (95%: +125.8% to +184.6%); power given | **power given in all three of our runs** |
| consumers running, most at once | 2 | 8 | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | 2 → 8; raw +300.0% (95%: +300.0% to +300.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.32 | 0.357 | 0.3204 → 0.3566; raw +11.3% (95%: +9.3% to +13.3%), +0.0362 in the gauge's unit; power given | 0.3469 → 0.3926; raw +13.2% (95%: +12.7% to +13.6%), +0.0457 in the gauge's unit; power given | 0.3707 → 0.4168; raw +12.4% (95%: +5.8% to +19.1%), +0.0461 in the gauge's unit; power given | **power given in all three of our runs** |
| host CPU-seconds | 568.2 | 631.2 | 568.2 → 631.2; raw +11.1% (95%: +9.1% to +13.0%); power given | 603.2 → 683.8; raw +13.4% (95%: +12.4% to +14.3%); power given | 660.6 → 737.2; raw +11.6% (95%: +5.1% to +18.1%); power given | **power given in all three of our runs** |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.66 | 1.731 → 1.66; raw −4.1% (95%: −6.2% to −2.1%); GAIN | 1.844 → 1.779; raw −3.5% (95%: −4.0% to −3.1%); GAIN | 2.024 → 1.933; raw −4.5% (95%: −10.2% to +1.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| consumer changes written (the knob's moves) | 2 | 16.0 | 2 → 16; raw +700.0% (95%: +269.7% to +1130.3%) | 2 → 14; raw +600.0% (95%: +600.0% to +600.0%) | 2 → 16; raw +700.0% (95%: +269.7% to +1130.3%) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 2 to 3 (1 trials, 1 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); left native (0 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (1 trials, 1 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); left native (0 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 1 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused); acting: 2 to 3 (1 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 24 gauge-rows GAIN, 0 LOSS, 12 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 6 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
