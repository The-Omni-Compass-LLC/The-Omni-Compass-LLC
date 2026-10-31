# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40043218026 | `f22776e60a87` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |
| B | 40044599601 | `0d532c7a2dbd` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |
| C | 40045930230 | `e4a97f22dce1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,287, 16,340, 39,049 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,161 | 7,166 | 7161 → 7166; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 7187 → 7136; raw −0.7% (95%: −2.6% to +1.2%); LOSS | 1.718e+04 → 1.717e+04; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.22%) |
| throughput (transactions a second) | 7,161 | 7,166 | 7161 → 7166; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 7189 → 7188; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1.718e+04 → 1.718e+04; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 1.26 | 1.29 | 1.26 → 1.29; raw +2.3% (95%: −2.9% to +7.5%); LOSS | 1.365 → 1.737; raw +27.3% (95%: −25.1% to +79.7%); LOSS | 1.023 → 0.7463; raw −27.0% (95%: −112.0% to +57.9%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 3.79 | 4.01 | 3.788 → 4.009; raw +5.8% (95%: −12.6% to +24.2%); LOSS | 5.774 → 34.75; raw +501.8% (95%: −1164.7% to +2168.4%); LOSS | 14.2 → 8.36; raw −41.1% (95%: −128.4% to +46.2%); GAIN | **the runs disagree** |
| latency, median (ms) | 0.368 | 0.368 | 0.3677 → 0.3677; raw ±0.0% (95%: −0.7% to +0.7%), ±0.0000 in the gauge's unit; STEADY | 0.372 → 0.3767; raw +1.3% (95%: +0.2% to +2.3%), +0.0047 in the gauge's unit; LOSS | 0.159 → 0.1593; raw +0.2% (95%: −3.7% to +4.1%), +0.0003 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.49%) |
| latency, mean (ms) | 0.547 | 0.582 | 0.5471 → 0.5816; raw +6.3% (95%: −4.8% to +17.4%), +0.0344 in the gauge's unit; LOSS | 0.6511 → 1.335; raw +105.1% (95%: −147.4% to +357.6%), +0.6842 in the gauge's unit; LOSS | 0.5945 → 0.4579; raw −23.0% (95%: −72.8% to +26.9%), −0.1365 in the gauge's unit; GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.2 | 15.0 | 19.23 → 15.02; raw −21.9% (95%: −34.5% to −9.3%); GAIN | 19.43 → 15.12; raw −22.2% (95%: −38.1% to −6.2%); GAIN | 19.84 → 18.03; raw −9.1% (95%: −18.7% to +0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.316 | 0.317 | 0.3164 → 0.317; raw +0.2% (95%: −0.5% to +0.9%), +0.0006 in the gauge's unit; STEADY | 0.324 → 0.3302; raw +1.9% (95%: +0.7% to +3.2%), +0.0062 in the gauge's unit; power given | 0.3811 → 0.3819; raw +0.2% (95%: −4.2% to +4.7%), +0.0009 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 466.0 | 467.1 | 466 → 467.1; raw +0.2% (95%: −0.8% to +1.2%); STEADY | 478.4 → 489.2; raw +2.3% (95%: +0.7% to +3.8%); power given | 650 → 651; raw +0.1% (95%: −4.4% to +4.7%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.145 | 0.1446 → 0.1448; raw +0.2% (95%: −1.0% to +1.3%), +0.0002 in the gauge's unit; STEADY | 0.1479 → 0.1524; raw +3.0% (95%: +0.5% to +5.4%), +0.0044 in the gauge's unit; power given | 0.0841 → 0.08423; raw +0.2% (95%: −4.5% to +4.9%), +0.0001 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.56 | 3.34 | 2.559 → 3.341; raw +30.6% (95%: +22.1% to +39.0%) | 2.583 → 3.42; raw +32.4% (95%: +27.5% to +37.3%) | 3.16 → 3.681; raw +16.5% (95%: +14.0% to +18.9%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 15.7 | 20 → 15.75; raw −21.3% (95%: −28.4% to −14.2%) | 20 → 16.01; raw −20.0% (95%: −38.2% to −1.7%) | 20 → 18.22; raw −8.9% (95%: −20.0% to +2.2%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 12 to 20 (12 trials, 8 allowed, 3 refused); acting: 13 to 20 (11 trials, 7 allowed, 4 refused); acting: 12 to 20 (11 trials, 8 allowed, 3 refused); run B: acting: 13 to 20 (10 trials, 7 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 10 to 20 (13 trials, 10 allowed, 2 refused); run C: acting: 16 to 20 (9 trials, 4 allowed, 3 refused); acting: 17 to 20 (9 trials, 3 allowed, 3 refused); acting: 19 to 20 (6 trials, 1 allowed, 5 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,849, 5,315, 4,536 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,645 | 1,639 | 1645 → 1639; raw −0.4% (95%: −4.1% to +3.3%); STEADY | 1571 → 1635; raw +4.1% (95%: −21.7% to +29.9%); GAIN | 1388 → 1123; raw −19.1% (95%: −92.9% to +54.8%); LOSS | **the runs disagree** |
| throughput (transactions a second) | 1,695 | 1,690 | 1695 → 1690; raw −0.3% (95%: −0.8% to +0.2%); STEADY | 2282 → 2326; raw +1.9% (95%: −6.0% to +9.9%); GAIN | 1980 → 1940; raw −2.0% (95%: −5.9% to +1.9%); LOSS | **the runs disagree** |
| latency, 95th percentile (ms, lag included) | 7.68 | 9.43 | 7.68 → 9.435; raw +22.8% (95%: −101.6% to +147.3%); LOSS | 1848 → 966.9; raw −47.7% (95%: −122.7% to +27.3%); GAIN | 1057 → 3623; raw +242.6% (95%: −43.4% to +528.5%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 206.8 | 202.8 | 206.8 → 202.8; raw −1.9% (95%: −75.3% to +71.4%); GAIN | 4834 → 2625; raw −45.7% (95%: −232.9% to +141.5%); GAIN | 1661 → 5117; raw +208.0% (95%: −89.4% to +505.5%); LOSS | **the runs disagree** |
| latency, median (ms) | 1.52 | 1.52 | 1.518 → 1.522; raw +0.3% (95%: −0.7% to +1.2%); STEADY | 1.397 → 1.917; raw +37.2% (95%: −177.8% to +252.3%); LOSS | 1.634 → 30.65; raw +1776.0% (95%: −2882.0% to +6434.0%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 7.16 | 7.3 | 7.164 → 7.303; raw +1.9% (95%: −87.8% to +91.6%); LOSS | 318 → 184.2; raw −42.1% (95%: −118.6% to +34.5%); GAIN | 179.7 → 524.4; raw +191.7% (95%: −119.7% to +503.2%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 18.6 | 19.99 → 18.6; raw −6.9% (95%: −9.5% to −4.4%); GAIN | 20 → 20.9; raw +4.5% (95%: −4.5% to +13.5%); power given | 20 → 20.3; raw +1.5% (95%: −2.4% to +5.5%); power given | **the runs disagree** |
| server connections alive, most at once | 20.0 | 21.0 | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 22.67; raw +13.3% (95%: −12.5% to +39.2%); power given | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.342 | 0.342 | 0.3417 → 0.3422; raw +0.1% (95%: −1.7% to +2.0%), +0.0005 in the gauge's unit; STEADY | 0.3631 → 0.3712; raw +2.2% (95%: −4.0% to +8.4%), +0.0081 in the gauge's unit; power given | 0.3171 → 0.3073; raw −3.1% (95%: −10.2% to +4.1%), −0.0098 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 513.7 | 514.3 | 513.7 → 514.3; raw +0.1% (95%: −1.7% to +1.9%); STEADY | 630.2 → 644.5; raw +2.3% (95%: −4.9% to +9.4%); power given | 553.4 → 538.1; raw −2.8% (95%: −8.8% to +3.3%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.694 | 0.697 | 0.6939 → 0.6973; raw +0.5% (95%: −1.5% to +2.5%), +0.0035 in the gauge's unit; power given | 0.8931 → 0.8807; raw −1.4% (95%: −33.8% to +31.0%), −0.0124 in the gauge's unit; GAIN | 0.8954 → 1.095; raw +22.2% (95%: −63.9% to +108.4%), +0.1991 in the gauge's unit; power given | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.81 | 1.014 → 1.808; raw +78.3% (95%: +75.1% to +81.5%) | 0.896 → 1.556; raw +73.6% (95%: +66.4% to +80.9%), +0.6598 in the gauge's unit | 0.8412 → 1.431; raw +70.1% (95%: +54.3% to +85.8%), +0.5894 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | 20 → 18.9; raw −5.5% (95%: −9.1% to −1.9%) | 20 → 20.82; raw +4.1% (95%: −4.3% to +12.5%) | 20 → 20.26; raw +1.3% (95%: −2.3% to +4.9%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 17 to 20 (14 trials, 3 allowed, 5 refused); acting: 18 to 21 (13 trials, 3 allowed, 4 refused); acting: 19 to 20 (14 trials, 1 allowed, 3 refused); run B: acting: 19 to 21 (18 trials, 2 allowed, 3 refused); acting: 20 to 24 (21 trials, 4 allowed, 1 refused); left native (19 trials, 0 allowed, 2 refused); run C: left native (25 trials, 0 allowed, 0 refused); left native (24 trials, 0 allowed, 0 refused); acting: 20 to 21 (20 trials, 1 allowed, 2 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 2,293, 1,912, 1,531 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,007 | 1,007 | 1007 → 1007; raw ±0.0% (95%: −1.8% to +1.7%); STEADY | 839.7 → 839.9; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 554.8 → 536.1; raw −3.4% (95%: −13.1% to +6.4%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 1,010 | 1,008 | 1010 → 1008; raw −0.2% (95%: −0.5% to ±0.0%); STEADY | 840.5 → 840.2; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | 672.3 → 672.2; raw ±0.0% (95%: −0.7% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.09%) |
| latency, 95th percentile (ms, lag included) | 2.96 | 2.84 | 2.959 → 2.838; raw −4.1% (95%: −27.8% to +19.5%); GAIN | 5.651 → 5.466; raw −3.3% (95%: −19.4% to +12.9%); GAIN | 332.7 → 359.1; raw +8.0% (95%: −32.4% to +48.3%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 18.7 | 5.52 | 18.73 → 5.523; raw −70.5% (95%: −394.9% to +253.9%); GAIN | 14.11 → 13.5; raw −4.3% (95%: −79.8% to +71.1%); GAIN | 1254 → 867.5; raw −30.8% (95%: −87.7% to +26.0%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 1.35 | 1.34 | 1.355 → 1.341; raw −1.0% (95%: −4.7% to +2.6%); GAIN | 1.916 → 1.91; raw −0.3% (95%: −0.9% to +0.2%); STEADY | 1.212 → 1.24; raw +2.3% (95%: −8.0% to +12.6%); LOSS | **the runs disagree** |
| latency, mean (ms) | 1.99 | 1.74 | 1.992 → 1.742; raw −12.6% (95%: −103.9% to +78.8%); GAIN | 2.666 → 2.584; raw −3.1% (95%: −16.4% to +10.2%); GAIN | 62.79 → 60.18; raw −4.1% (95%: −21.7% to +13.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.7 | 17.4 | 19.74 → 17.37; raw −12.0% (95%: −25.1% to +1.0%); GAIN | 19.81 → 16.74; raw −15.5% (95%: −18.5% to −12.5%); GAIN | 20 → 19.92; raw −0.4% (95%: −1.0% to +0.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.239 | 0.237 | 0.2393 → 0.237; raw −0.9% (95%: −5.2% to +3.3%), −0.0022 in the gauge's unit; GAIN | 0.2369 → 0.2367; raw −0.1% (95%: −1.5% to +1.4%), −0.0002 in the gauge's unit; STEADY | 0.1617 → 0.1626; raw +0.6% (95%: −1.2% to +2.4%), +0.0010 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 419.2 | 415.4 | 419.2 → 415.4; raw −0.9% (95%: −5.0% to +3.2%); GAIN | 369.7 → 369.4; raw −0.1% (95%: −1.7% to +1.5%); STEADY | 284.3 → 286.1; raw +0.6% (95%: −1.2% to +2.4%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.925 | 0.917 | 0.9249 → 0.917; raw −0.9% (95%: −3.3% to +1.6%), −0.0079 in the gauge's unit; GAIN | 0.9783 → 0.9773; raw −0.1% (95%: −1.8% to +1.6%), −0.0009 in the gauge's unit; STEADY | 1.141 → 1.193; raw +4.5% (95%: −8.4% to +17.4%); power given | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.629 | 1.17 | 0.6293 → 1.169; raw +85.8% (95%: +83.2% to +88.4%), +0.5398 in the gauge's unit | 0.763 → 1.507; raw +97.4% (95%: +90.9% to +104.0%), +0.7435 in the gauge's unit | 0.5573 → 1.098; raw +97.0% (95%: +95.1% to +98.9%), +0.5407 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | 20 → 17.82; raw −10.9% (95%: −26.3% to +4.6%) | 20 → 17.34; raw −13.3% (95%: −15.5% to −11.1%) | 20 → 19.94; raw −0.3% (95%: −0.9% to +0.3%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 16 to 20 (10 trials, 4 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run B: acting: 15 to 20 (9 trials, 5 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); run C: left native (25 trials, 0 allowed, 1 refused); left native (21 trials, 0 allowed, 1 refused); left native (28 trials, 0 allowed, 1 refused).

**Across 3 workloads: 4 gauge-rows GAIN, 2 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 8 STEADY, 17 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
