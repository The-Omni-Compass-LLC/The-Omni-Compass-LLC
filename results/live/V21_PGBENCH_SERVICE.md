# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40289615442 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| B | 40293188618 | `2d426169d766` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| C | 40295032874 | `c8b8e2af081f` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 37,388, 36,773, 16,496 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 16,450 | 16,452 | 1.645e+04 → 1.645e+04; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1.585e+04 → 1.617e+04; raw +2.0% (95%: −6.8% to +10.8%); GAIN | 7255 → 7253; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 16,450 | 16,452 | 1.645e+04 → 1.645e+04; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1.618e+04 → 1.617e+04; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 7255 → 7253; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 0.791 | 0.505 | 0.7913 → 0.5047; raw −36.2% (95%: −232.2% to +159.7%), −0.2867 in the gauge's unit; GAIN | 43.01 → 0.341; raw −99.2% (95%: −520.9% to +322.5%); GAIN | 1.427 → 1.267; raw −11.2% (95%: −46.3% to +23.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 5.2 | 3.77 | 5.196 → 3.769; raw −27.5% (95%: −224.2% to +169.3%); GAIN | 182.4 → 1.213; raw −99.3% (95%: −516.9% to +318.3%); GAIN | 4.468 → 3.635; raw −18.7% (95%: −62.5% to +25.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.163 | 0.162 | 0.1627 → 0.1617; raw −0.6% (95%: −3.7% to +2.4%), −0.0010 in the gauge's unit; GAIN | 0.1593 → 0.1563; raw −1.9% (95%: −12.1% to +8.3%), −0.0030 in the gauge's unit; GAIN | 0.3683 → 0.3687; raw +0.1% (95%: −0.7% to +0.9%), +0.0003 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.363 | 0.321 | 0.3635 → 0.3209; raw −11.7% (95%: −116.2% to +92.8%), −0.0425 in the gauge's unit; GAIN | 6.687 → 0.2151; raw −96.8% (95%: −505.0% to +311.4%); GAIN | 0.5846 → 0.5535; raw −5.3% (95%: −21.1% to +10.5%), −0.0311 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | 19.97 → 19.12; raw −4.3% (95%: −15.4% to +6.9%); GAIN | 19.89 → 18.11; raw −8.9% (95%: −11.3% to −6.6%); GAIN | 19.03 → 15.03; raw −21.0% (95%: −37.5% to −4.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.374 | 0.373 | 0.3744 → 0.3727; raw −0.5% (95%: −3.9% to +3.0%), −0.0017 in the gauge's unit; STEADY | 0.3617 → 0.3546; raw −1.9% (95%: −12.7% to +8.8%), −0.0070 in the gauge's unit; GAIN | 0.3208 → 0.3212; raw +0.1% (95%: −1.7% to +1.9%), +0.0004 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 648.5 | 645.6 | 648.5 → 645.6; raw −0.5% (95%: −4.2% to +3.3%); STEADY | 626.4 → 613.5; raw −2.1% (95%: −13.3% to +9.2%); GAIN | 479.8 → 480.4; raw +0.1% (95%: −2.0% to +2.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.0876 | 0.0872 | 0.08761 → 0.0872; raw −0.5% (95%: −4.3% to +3.3%), −0.0004 in the gauge's unit; STEADY | 0.08785 → 0.0843; raw −4.0% (95%: −17.7% to +9.7%), −0.0035 in the gauge's unit; GAIN | 0.147 → 0.1472; raw +0.1% (95%: −2.0% to +2.3%), +0.0002 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 10.3 | 10.9 | 10.34 → 10.92; raw +5.7% (95%: +3.2% to +8.1%) | 10.1 → 10.57; raw +4.6% (95%: −3.6% to +12.9%) | 8.534 → 9.355; raw +9.6% (95%: +2.2% to +17.1%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.3 | 20 → 19.3; raw −3.5% (95%: −13.4% to +6.4%) | 20 → 18.5; raw −7.5% (95%: −10.5% to −4.5%) | 20 → 15.91; raw −20.5% (95%: −40.3% to −0.6%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); left native (6 trials, 0 allowed, 5 refused); left native (6 trials, 0 allowed, 5 refused); run B: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused); run C: acting: 12 to 20 (11 trials, 8 allowed, 3 refused); acting: 11 to 20 (12 trials, 9 allowed, 3 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 5,934, 3,884, 7,642 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,480 | 2,507 | 2480 → 2507; raw +1.1% (95%: −1.4% to +3.6%); GAIN | 1680 → 1675; raw −0.3% (95%: −1.2% to +0.5%); STEADY | 3155 → 3155; raw ±0.0% (95%: −3.5% to +3.5%); STEADY | STEADY, under the floor (the three runs' mean 0.25%) |
| throughput (transactions a second) | 2,610 | 2,610 | 2610 → 2610; raw ±0.0% (95%: −0.7% to +0.7%); STEADY | 1710 → 1705; raw −0.3% (95%: −0.6% to ±0.0%); STEADY | 3359 → 3363; raw +0.1% (95%: −0.1% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms, lag included) | 65.3 | 15.2 | 65.34 → 15.21; raw −76.7% (95%: −325.3% to +171.8%); GAIN | 6.543 → 6.287; raw −3.9% (95%: −29.0% to +21.2%); GAIN | 91.06 → 150; raw +64.8% (95%: −161.0% to +290.5%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 589.1 | 519.3 | 589.1 → 519.3; raw −11.9% (95%: −52.3% to +28.6%); GAIN | 129.2 → 137.1; raw +6.1% (95%: −66.0% to +78.3%); LOSS | 601.6 → 666.6; raw +10.8% (95%: −32.1% to +53.7%); LOSS | **the runs disagree** |
| latency, median (ms) | 1.18 | 1.17 | 1.18 → 1.174; raw −0.5% (95%: −2.9% to +2.0%); STEADY | 1.535 → 1.528; raw −0.5% (95%: −2.9% to +1.9%); STEADY | 0.6997 → 0.6897; raw −1.4% (95%: −5.2% to +2.3%), −0.0100 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 20.5 | 16.1 | 20.51 → 16.11; raw −21.5% (95%: −87.2% to +44.2%); GAIN | 4.841 → 4.854; raw +0.3% (95%: −35.7% to +36.2%); STEADY | 21.44 → 25.13; raw +17.2% (95%: −61.1% to +95.5%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | 19.96 → 19.33; raw −3.2% (95%: −4.6% to −1.8%); GAIN | 19.92 → 19.15; raw −3.9% (95%: −5.7% to −2.0%); GAIN | 20 → 19.91; raw −0.4% (95%: −3.7% to +2.8%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 23; raw +15.0% (95%: +15.0% to +15.0%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.406 | 0.408 | 0.4062 → 0.4081; raw +0.5% (95%: +0.1% to +0.8%), +0.0018 in the gauge's unit; STEADY | 0.3467 → 0.3452; raw −0.4% (95%: −3.0% to +2.1%), −0.0015 in the gauge's unit; STEADY | 0.3545 → 0.3502; raw −1.2% (95%: −4.7% to +2.3%), −0.0043 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.40%) |
| host CPU-seconds | 704.9 | 708.1 | 704.9 → 708.1; raw +0.5% (95%: ±0.0% to +0.9%); STEADY | 522.8 → 520.5; raw −0.4% (95%: −3.3% to +2.5%); STEADY | 606.2 → 598.6; raw −1.3% (95%: −5.0% to +2.5%); GAIN | STEADY, under the floor (the three runs' mean 0.41%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.632 | 0.628 | 0.6316 → 0.6276; raw −0.6% (95%: −3.3% to +2.0%), −0.0040 in the gauge's unit; GAIN | 0.6914 → 0.6908; raw −0.1% (95%: −3.4% to +3.2%), −0.0006 in the gauge's unit; STEADY | 0.427 → 0.4216; raw −1.3% (95%: −8.5% to +5.9%), −0.0054 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.78 | 3.35 | 2.782 → 3.353; raw +20.5% (95%: +19.0% to +22.1%) | 2.5 → 3.316; raw +32.6% (95%: +32.0% to +33.3%) | 2.313 → 2.804; raw +21.2% (95%: +15.1% to +27.3%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | 20 → 19.51; raw −2.4% (95%: −3.8% to −1.1%) | 20 → 19.41; raw −3.0% (95%: −5.5% to −0.5%) | 20 → 19.97; raw −0.2% (95%: −2.8% to +2.5%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 20 (13 trials, 1 allowed, 5 refused); acting: 19 to 21 (12 trials, 2 allowed, 6 refused); acting: 19 to 20 (12 trials, 1 allowed, 5 refused); run B: acting: 19 to 21 (13 trials, 2 allowed, 3 refused); acting: 19 to 20 (12 trials, 1 allowed, 4 refused); acting: 19 to 20 (13 trials, 1 allowed, 5 refused); run C: acting: 18 to 22 (20 trials, 4 allowed, 4 refused); acting: 19 to 22 (19 trials, 3 allowed, 4 refused); acting: 19 to 22 (15 trials, 3 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,956, 1,967, 2,509 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 860.3 | 862.0 | 860.3 → 862; raw +0.2% (95%: −0.1% to +0.5%); STEADY | 864.5 → 864.3; raw ±0.0% (95%: −1.0% to +0.9%); STEADY | 1097 → 1104; raw +0.6% (95%: −1.2% to +2.5%); GAIN | STEADY, under the floor (the three runs' mean 0.27%) |
| throughput (transactions a second) | 860.5 | 862.1 | 860.5 → 862.1; raw +0.2% (95%: −0.2% to +0.5%); STEADY | 864.7 → 864.4; raw ±0.0% (95%: −1.0% to +0.9%); STEADY | 1103 → 1104; raw +0.2% (95%: −0.4% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| latency, 95th percentile (ms, lag included) | 5.26 | 4.89 | 5.256 → 4.885; raw −7.1% (95%: −18.5% to +4.4%); GAIN | 4.975 → 4.771; raw −4.1% (95%: −20.4% to +12.2%); GAIN | 3.431 → 2.996; raw −12.7% (95%: −73.7% to +48.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 13.1 | 10.8 | 13.06 → 10.8; raw −17.2% (95%: −44.1% to +9.6%); GAIN | 12.1 → 10.25; raw −15.4% (95%: −41.6% to +10.9%); GAIN | 29.44 → 6.227; raw −78.9% (95%: −417.6% to +259.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 1.88 | 1.87 | 1.878 → 1.874; raw −0.2% (95%: −1.4% to +0.9%); STEADY | 1.863 → 1.86; raw −0.2% (95%: −3.1% to +2.8%); STEADY | 1.315 → 1.318; raw +0.3% (95%: −2.0% to +2.6%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, mean (ms) | 2.51 | 2.42 | 2.509 → 2.417; raw −3.7% (95%: −9.6% to +2.3%); GAIN | 2.464 → 2.385; raw −3.2% (95%: −11.8% to +5.3%); GAIN | 2.217 → 1.703; raw −23.2% (95%: −118.7% to +72.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.5 | 16.4 | 19.46 → 16.38; raw −15.8% (95%: −24.5% to −7.1%); GAIN | 19.34 → 16.71; raw −13.6% (95%: −22.9% to −4.3%); GAIN | 19.76 → 16.72; raw −15.3% (95%: −18.9% to −11.8%); GAIN | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.239 | 0.24 | 0.2393 → 0.2397; raw +0.2% (95%: −2.4% to +2.8%), +0.0004 in the gauge's unit; STEADY | 0.2392 → 0.2388; raw −0.2% (95%: −4.2% to +3.8%), −0.0005 in the gauge's unit; STEADY | 0.2458 → 0.2472; raw +0.6% (95%: −2.2% to +3.3%), +0.0014 in the gauge's unit; power given | STEADY, under the floor (the three runs' mean 0.19%) |
| host CPU-seconds | 373.0 | 373.6 | 373 → 373.6; raw +0.2% (95%: −2.4% to +2.8%); STEADY | 372.8 → 371.9; raw −0.3% (95%: −4.2% to +3.7%); STEADY | 430.9 → 433.3; raw +0.5% (95%: −2.3% to +3.4%); power given | STEADY, under the floor (the three runs' mean 0.16%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.963 | 0.963 | 0.9635 → 0.9633; raw ±0.0% (95%: −2.5% to +2.5%), −0.0002 in the gauge's unit; STEADY | 0.9583 → 0.9561; raw −0.2% (95%: −3.5% to +3.0%), −0.0022 in the gauge's unit; STEADY | 0.8731 → 0.8723; raw −0.1% (95%: −4.6% to +4.5%), −0.0008 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.5 | 2.21 | 1.499 → 2.211; raw +47.5% (95%: +44.1% to +51.0%) | 1.51 → 2.219; raw +47.0% (95%: +45.6% to +48.4%) | 1.357 → 1.905; raw +40.4% (95%: +37.2% to +43.6%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.2 | 20 → 17.23; raw −13.9% (95%: −21.7% to −6.1%) | 20 → 17.39; raw −13.0% (95%: −14.9% to −11.2%) | 20 → 17.49; raw −12.5% (95%: −15.2% to −9.9%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 14 to 20 (10 trials, 6 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run B: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run C: acting: 15 to 21 (11 trials, 6 allowed, 3 refused); acting: 16 to 20 (9 trials, 4 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused).

**Across 3 workloads: 16 gauge-rows GAIN, 0 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 15 STEADY, 3 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
