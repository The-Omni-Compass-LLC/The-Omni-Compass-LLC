# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39149254727 | `d44261ca0c5c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| B | 39157791268 | `5031411ae285` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| C | 39166378754 | `8472aaad2bf4` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,564, 16,586, 16,503 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,284 | 7,289 | 7284 → 7289; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 7299 → 7284; raw −0.2% (95%: −0.6% to +0.2%); STEADY | 7261 → 7259; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| throughput (transactions a second) | 7,284 | 7,289 | 7284 → 7289; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 7301 → 7292; raw −0.1% (95%: −0.5% to +0.3%); STEADY | 7261 → 7259; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms, lag included) | 1.51 | 1.46 | 1.512 → 1.463; raw −3.3% (95%: −36.7% to +30.2%); GAIN | 1.515 → 2.626; raw +73.3% (95%: −208.6% to +355.2%); LOSS | 1.184 → 1.144; raw −3.4% (95%: −22.5% to +15.7%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 4.63 | 4.21 | 4.629 → 4.214; raw −9.0% (95%: −59.0% to +41.0%); GAIN | 6.381 → 11.44; raw +79.2% (95%: −217.7% to +376.1%); LOSS | 3.512 → 3.136; raw −10.7% (95%: −62.6% to +41.2%); GAIN | **the runs disagree** |
| latency, median (ms) | 0.373 | 0.373 | 0.3727 → 0.3727; raw ±0.0% (95%: −1.2% to +1.2%), ±0.0000 in the gauge's unit; STEADY | 0.373 → 0.3777; raw +1.3% (95%: −4.2% to +6.7%), +0.0047 in the gauge's unit; LOSS | 0.3613 → 0.3613; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.42%) |
| latency, mean (ms) | 0.597 | 0.577 | 0.5974 → 0.5775; raw −3.3% (95%: −24.2% to +17.5%), −0.0199 in the gauge's unit; GAIN | 0.6615 → 0.8571; raw +29.6% (95%: −75.9% to +135.0%), +0.1956 in the gauge's unit; LOSS | 0.5244 → 0.5108; raw −2.6% (95%: −17.3% to +12.1%), −0.0136 in the gauge's unit; GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.5 | 18.4 | 19.53 → 18.37; raw −5.9% (95%: −13.6% to +1.7%); GAIN | 19.88 → 18.84; raw −5.3% (95%: −7.6% to −2.9%); GAIN | 19.47 → 18.09; raw −7.1% (95%: −10.3% to −3.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.327 | 0.328 | 0.327 → 0.3278; raw +0.2% (95%: −1.4% to +1.8%), +0.0007 in the gauge's unit; STEADY | 0.3272 → 0.331; raw +1.2% (95%: −6.3% to +8.6%), +0.0038 in the gauge's unit; power given | 0.3121 → 0.3125; raw +0.1% (95%: −0.5% to +0.8%), +0.0004 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 482.2 | 483.4 | 482.2 → 483.4; raw +0.3% (95%: −1.4% to +2.0%); STEADY | 482.3 → 489.5; raw +1.5% (95%: −6.7% to +9.7%); power given | 458.4 → 458.9; raw +0.1% (95%: −0.9% to +1.1%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.147 | 0.1471 → 0.1474; raw +0.2% (95%: −1.3% to +1.7%), +0.0003 in the gauge's unit; STEADY | 0.1468 → 0.1493; raw +1.7% (95%: −6.8% to +10.1%), +0.0025 in the gauge's unit; power given | 0.1403 → 0.1405; raw +0.1% (95%: −0.9% to +1.2%), +0.0002 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.61 | 3.36 | 2.61 → 3.358; raw +28.7% (95%: +22.5% to +34.9%) | 2.614 → 3.418; raw +30.8% (95%: +22.1% to +39.4%) | 2.582 → 3.271; raw +26.7% (95%: +19.5% to +33.9%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | 20 → 18.95; raw −5.3% (95%: −5.6% to −5.0%) | 20 → 19.04; raw −4.8% (95%: −5.5% to −4.1%) | 20 → 18.92; raw −5.4% (95%: −6.1% to −4.7%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run B: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 18 to 20 (8 trials, 2 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused); run C: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,791, 3,729, 3,823 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,625 | 1,624 | 1625 → 1624; raw −0.1% (95%: −3.6% to +3.4%); STEADY | 1599 → 1607; raw +0.5% (95%: −2.4% to +3.4%); STEADY | 1641 → 1647; raw +0.4% (95%: −1.6% to +2.4%); STEADY | STEADY, under the floor (the three runs' mean 0.26%) |
| throughput (transactions a second) | 1,667 | 1,668 | 1667 → 1668; raw ±0.0% (95%: −0.6% to +0.6%); STEADY | 1641 → 1641; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 1682 → 1681; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms, lag included) | 7.29 | 10.5 | 7.295 → 10.49; raw +43.8% (95%: −185.5% to +273.2%); LOSS | 6.434 → 5.992; raw −6.9% (95%: −61.6% to +47.8%); GAIN | 6.658 → 6.287; raw −5.6% (95%: −25.3% to +14.2%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 180.6 | 173.4 | 180.6 → 173.4; raw −4.0% (95%: −112.8% to +104.8%); GAIN | 179.7 → 147.4; raw −18.0% (95%: −112.9% to +76.9%); GAIN | 180 → 157.3; raw −12.6% (95%: −73.3% to +48.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 1.53 | 1.53 | 1.528 → 1.528; raw ±0.0% (95%: −1.7% to +1.7%); STEADY | 1.499 → 1.499; raw ±0.0% (95%: −0.8% to +0.9%); STEADY | 1.509 → 1.504; raw −0.3% (95%: −1.2% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, mean (ms) | 6.36 | 6.63 | 6.36 → 6.625; raw +4.2% (95%: −102.5% to +110.8%); LOSS | 6.266 → 5.201; raw −17.0% (95%: −113.3% to +79.3%); GAIN | 5.983 → 5.394; raw −9.8% (95%: −65.5% to +45.8%); GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | 20 → 19.26; raw −3.7% (95%: −6.2% to −1.1%); GAIN | 20 → 19.61; raw −2.0% (95%: −4.5% to +0.6%); GAIN | 20 → 19.52; raw −2.4% (95%: −5.9% to +1.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.7 | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | 20 → 22; raw +10.0% (95%: +10.0% to +10.0%); power given | 20 → 22; raw +10.0% (95%: +10.0% to +10.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.341 | 0.342 | 0.3413 → 0.3416; raw +0.1% (95%: −2.0% to +2.1%), +0.0002 in the gauge's unit; STEADY | 0.3267 → 0.3273; raw +0.2% (95%: −0.3% to +0.7%), +0.0006 in the gauge's unit; STEADY | 0.3336 → 0.3329; raw −0.2% (95%: −0.6% to +0.2%), −0.0008 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| host CPU-seconds | 513.6 | 514.2 | 513.6 → 514.2; raw +0.1% (95%: −2.3% to +2.5%); STEADY | 490.8 → 491.6; raw +0.2% (95%: −0.4% to +0.8%); STEADY | 500.7 → 499.3; raw −0.3% (95%: −0.6% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.702 | 0.704 | 0.7024 → 0.7038; raw +0.2% (95%: −5.0% to +5.4%), +0.0014 in the gauge's unit; STEADY | 0.682 → 0.6798; raw −0.3% (95%: −3.6% to +2.9%), −0.0023 in the gauge's unit; STEADY | 0.678 → 0.6736; raw −0.6% (95%: −2.9% to +1.7%), −0.0044 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.26%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.81 | 1.022 → 1.813; raw +77.4% (95%: +75.3% to +79.6%) | 1.011 → 1.77; raw +75.1% (95%: +71.6% to +78.5%) | 1.012 → 1.787; raw +76.5% (95%: +68.7% to +84.3%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | 20 → 19.5; raw −2.5% (95%: −6.1% to +1.1%) | 20 → 19.81; raw −1.0% (95%: −3.4% to +1.5%) | 20 → 19.67; raw −1.7% (95%: −5.4% to +2.1%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 18 to 22 (12 trials, 4 allowed, 5 refused); acting: 20 to 21 (10 trials, 1 allowed, 4 refused); acting: 19 to 20 (10 trials, 1 allowed, 7 refused); run B: acting: 19 to 21 (11 trials, 2 allowed, 5 refused); acting: 20 to 21 (11 trials, 1 allowed, 4 refused); acting: 19 to 21 (12 trials, 2 allowed, 3 refused); run C: acting: 20 to 22 (11 trials, 2 allowed, 4 refused); acting: 19 to 21 (14 trials, 2 allowed, 5 refused); acting: 19 to 21 (12 trials, 2 allowed, 3 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,951, 1,910, 2,333 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,732 | 1,736 | 1732 → 1736; raw +0.2% (95%: −1.1% to +1.6%); STEADY | 840.9 → 839.2; raw −0.2% (95%: −0.3% to −0.1%); STEADY | 1026 → 1025; raw −0.1% (95%: −1.2% to +1.0%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (transactions a second) | 1,739 | 1,740 | 1739 → 1740; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 840.9 → 839.3; raw −0.2% (95%: −0.3% to −0.1%); STEADY | 1028 → 1028; raw ±0.0% (95%: −0.8% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms, lag included) | 2.62 | 2.25 | 2.618 → 2.245; raw −14.3% (95%: −108.1% to +79.6%); GAIN | 4.576 → 4.607; raw +0.7% (95%: −15.6% to +16.9%); LOSS | 3.059 → 3.092; raw +1.1% (95%: −11.9% to +14.0%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 24.9 | 19.7 | 24.85 → 19.75; raw −20.5% (95%: −247.8% to +206.8%); GAIN | 9.318 → 9.762; raw +4.8% (95%: −45.6% to +55.1%); LOSS | 7.773 → 7.068; raw −9.1% (95%: −98.7% to +80.5%); GAIN | **the runs disagree** |
| latency, median (ms) | 0.792 | 0.791 | 0.7917 → 0.791; raw −0.1% (95%: −2.1% to +1.9%), −0.0007 in the gauge's unit; STEADY | 1.861 → 1.859; raw −0.1% (95%: −1.6% to +1.3%); STEADY | 1.391 → 1.393; raw +0.1% (95%: −2.1% to +2.4%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, mean (ms) | 1.61 | 1.45 | 1.609 → 1.454; raw −9.6% (95%: −109.1% to +89.9%); GAIN | 2.338 → 2.351; raw +0.6% (95%: −9.0% to +10.1%); LOSS | 1.834 → 1.971; raw +7.4% (95%: −13.6% to +28.5%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.0 | 19.99 → 19.01; raw −4.9% (95%: −5.4% to −4.4%); GAIN | 19.67 → 18.15; raw −7.7% (95%: −9.1% to −6.3%); GAIN | 19.89 → 17.46; raw −12.2% (95%: −30.5% to +6.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.0 | 20 → 21; raw +5.0% (95%: −7.4% to +17.4%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.244 | 0.244 | 0.2439 → 0.244; raw ±0.0% (95%: −2.6% to +2.7%), +0.0001 in the gauge's unit; STEADY | 0.2331 → 0.2319; raw −0.5% (95%: −3.3% to +2.2%), −0.0012 in the gauge's unit; GAIN | 0.2449 → 0.2445; raw −0.2% (95%: −2.3% to +2.0%), −0.0005 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.23%) |
| host CPU-seconds | 419.3 | 419.2 | 419.3 → 419.2; raw ±0.0% (95%: −2.8% to +2.7%); STEADY | 363.8 → 361.8; raw −0.5% (95%: −3.6% to +2.5%); GAIN | 428.6 → 427.9; raw −0.2% (95%: −2.2% to +1.9%); STEADY | STEADY, under the floor (the three runs' mean 0.25%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.538 | 0.537 | 0.5378 → 0.5366; raw −0.2% (95%: −4.3% to +3.8%), −0.0013 in the gauge's unit; STEADY | 0.9614 → 0.9581; raw −0.4% (95%: −3.5% to +2.8%), −0.0034 in the gauge's unit; STEADY | 0.9282 → 0.9272; raw −0.1% (95%: −3.1% to +2.8%), −0.0010 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.23%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.561 | 0.958 | 0.5615 → 0.9582; raw +70.7% (95%: +58.1% to +83.2%), +0.3967 in the gauge's unit | 0.7619 → 1.481; raw +94.4% (95%: +89.8% to +99.0%), +0.7190 in the gauge's unit | 0.6455 → 1.195; raw +85.2% (95%: +78.4% to +91.9%), +0.5497 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.1 | 20 → 19.13; raw −4.3% (95%: −5.2% to −3.4%) | 20 → 18.87; raw −5.7% (95%: −7.2% to −4.1%) | 20 → 17.96; raw −10.2% (95%: −30.4% to +10.0%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 21 (8 trials, 2 allowed, 4 refused); acting: 17 to 20 (10 trials, 3 allowed, 3 refused); acting: 17 to 21 (10 trials, 4 allowed, 4 refused); run B: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); run C: acting: 17 to 20 (10 trials, 3 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 12 to 20 (12 trials, 8 allowed, 2 refused).

**Across 3 workloads: 4 gauge-rows GAIN, 0 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 19 STEADY, 8 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
