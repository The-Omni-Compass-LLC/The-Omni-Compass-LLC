# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39473169216 | `ac0eeaef8ecc` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| B | 39477818906 | `fb90309cad0d` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| C | 39491674383 | `de8da62736d4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 15,231, 46,624, 44,401 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6,700 | 6,703 | 6700 → 6703; raw +0.1% (95%: −0.1% to +0.2%); STEADY | 1.991e+04 → 1.982e+04; raw −0.5% (95%: −4.7% to +3.8%); STEADY | 1.953e+04 → 1.946e+04; raw −0.4% (95%: −1.1% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.27%) |
| throughput (transactions a second) | 6,700 | 6,703 | 6700 → 6703; raw +0.1% (95%: −0.1% to +0.2%); STEADY | 2.051e+04 → 2.051e+04; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1.954e+04 → 1.953e+04; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 0.819 | 0.817 | 0.8193 → 0.817; raw −0.3% (95%: −7.3% to +6.7%), −0.0023 in the gauge's unit; STEADY | 17.74 → 33; raw +86.0% (95%: −260.9% to +433.0%); LOSS | 1.638 → 1.538; raw −6.1% (95%: −104.2% to +92.0%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 1.49 | 1.54 | 1.495 → 1.545; raw +3.3% (95%: −19.9% to +26.6%); LOSS | 127.2 → 129.3; raw +1.6% (95%: −105.2% to +108.4%); LOSS | 13.39 → 25.61; raw +91.3% (95%: −201.3% to +383.8%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.339 | 0.338 | 0.339 → 0.3383; raw −0.2% (95%: −3.7% to +3.3%), −0.0007 in the gauge's unit; STEADY | 0.1987 → 0.2; raw +0.7% (95%: −1.2% to +2.6%), +0.0013 in the gauge's unit; LOSS | 0.1967 → 0.197; raw +0.2% (95%: −4.3% to +4.6%), +0.0003 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.21%) |
| latency, mean (ms) | 0.422 | 0.43 | 0.4218 → 0.4296; raw +1.8% (95%: −12.6% to +16.3%), +0.0078 in the gauge's unit; LOSS | 4.202 → 5.285; raw +25.8% (95%: −101.2% to +152.7%); LOSS | 0.6541 → 0.8893; raw +36.0% (95%: −74.0% to +145.9%), +0.2352 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.2 | 16.7 | 19.18 → 16.72; raw −12.9% (95%: −23.0% to −2.7%); GAIN | 19.85 → 16.42; raw −17.3% (95%: −29.6% to −4.9%); GAIN | 19.72 → 17; raw −13.8% (95%: −20.4% to −7.2%); GAIN | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 19.0 | 20 → 19; raw −5.0% (95%: −26.5% to +16.5%); GAIN | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **the runs disagree** |
| host CPU busy (share of the run) | 0.37 | 0.369 | 0.3696 → 0.3693; raw −0.1% (95%: −2.8% to +2.7%), −0.0003 in the gauge's unit; STEADY | 0.4747 → 0.4762; raw +0.3% (95%: −0.7% to +1.3%), +0.0015 in the gauge's unit; STEADY | 0.4592 → 0.4592; raw ±0.0% (95%: −0.9% to +0.9%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| host CPU-seconds | 619.8 | 619.1 | 619.8 → 619.1; raw −0.1% (95%: −2.7% to +2.5%); STEADY | 833.2 → 835.9; raw +0.3% (95%: −0.7% to +1.4%); STEADY | 806.1 → 806; raw ±0.0% (95%: −0.7% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.206 | 0.205 | 0.2056 → 0.2053; raw −0.2% (95%: −2.9% to +2.6%), −0.0003 in the gauge's unit; STEADY | 0.09301 → 0.0938; raw +0.9% (95%: −2.9% to +4.6%), +0.0008 in the gauge's unit; power given | 0.09171 → 0.09204; raw +0.4% (95%: +0.1% to +0.6%), +0.0003 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.35%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.45 | 3.16 | 2.449 → 3.159; raw +29.0% (95%: +24.7% to +33.4%) | 4.099 → 4.541; raw +10.8% (95%: +8.1% to +13.5%) | 3.873 → 4.258; raw +9.9% (95%: +3.8% to +16.1%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.3 | 20 → 17.27; raw −13.6% (95%: −36.0% to +8.7%) | 20 → 16.79; raw −16.0% (95%: −29.4% to −2.7%) | 20 → 17.31; raw −13.5% (95%: −22.8% to −4.1%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 14 to 20 (10 trials, 6 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run B: acting: 13 to 20 (13 trials, 7 allowed, 3 refused); acting: 16 to 21 (9 trials, 5 allowed, 4 refused); acting: 15 to 21 (10 trials, 6 allowed, 3 refused); run C: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 4,069, 5,952, 5,663 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,742 | 1,749 | 1742 → 1749; raw +0.4% (95%: −2.2% to +3.0%); STEADY | 2471 → 2421; raw −2.0% (95%: −14.1% to +10.0%); LOSS | 2416 → 2411; raw −0.2% (95%: −3.5% to +3.1%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 1,789 | 1,790 | 1789 → 1790; raw +0.1% (95%: −0.4% to +0.5%); STEADY | 2615 → 2609; raw −0.2% (95%: −0.7% to +0.3%); STEADY | 2490 → 2490; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms, lag included) | 8.53 | 8.35 | 8.528 → 8.348; raw −2.1% (95%: −45.0% to +40.8%); GAIN | 69.31 → 184.9; raw +166.8% (95%: −822.2% to +1155.8%); LOSS | 5.547 → 5.913; raw +6.6% (95%: −88.3% to +101.5%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 172.5 | 173.3 | 172.5 → 173.3; raw +0.5% (95%: −96.7% to +97.6%); STEADY | 476 → 1309; raw +175.1% (95%: −650.5% to +1000.6%); LOSS | 212.2 → 235.3; raw +10.9% (95%: −70.0% to +91.8%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 1.48 | 1.49 | 1.48 → 1.486; raw +0.4% (95%: −1.8% to +2.7%); STEADY | 0.7133 → 0.7457; raw +4.5% (95%: −7.5% to +16.5%), +0.0323 in the gauge's unit; LOSS | 1.091 → 1.086; raw −0.5% (95%: −6.2% to +5.2%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 6.27 | 6.13 | 6.27 → 6.134; raw −2.2% (95%: −94.7% to +90.3%); GAIN | 16.28 → 43.92; raw +169.7% (95%: −664.9% to +1004.3%); LOSS | 6.784 → 7.678; raw +13.2% (95%: −97.1% to +123.5%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 18.8 | 20 → 18.83; raw −5.8% (95%: −8.3% to −3.4%); GAIN | 19.97 → 19.81; raw −0.8% (95%: −10.6% to +9.0%); GAIN | 20 → 19.42; raw −2.9% (95%: −8.4% to +2.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 22.33; raw +11.7% (95%: −7.3% to +30.6%); power given | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.43 | 0.432 | 0.4302 → 0.4321; raw +0.4% (95%: −0.9% to +1.8%), +0.0019 in the gauge's unit; STEADY | 0.2962 → 0.3071; raw +3.7% (95%: −3.9% to +11.3%), +0.0109 in the gauge's unit; power given | 0.4285 → 0.4276; raw −0.2% (95%: −3.9% to +3.5%), −0.0009 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 734.6 | 738.1 | 734.6 → 738.1; raw +0.5% (95%: −0.9% to +1.8%); STEADY | 506.5 → 525.4; raw +3.7% (95%: −4.0% to +11.4%); power given | 742.7 → 740.7; raw −0.3% (95%: −4.0% to +3.5%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.937 | 0.938 | 0.9373 → 0.9381; raw +0.1% (95%: −3.8% to +4.0%), +0.0008 in the gauge's unit; STEADY | 0.4555 → 0.4828; raw +6.0% (95%: −12.8% to +24.8%), +0.0273 in the gauge's unit; power given | 0.6832 → 0.6827; raw −0.1% (95%: −4.2% to +4.1%), −0.0005 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.05 | 1.86 | 1.05 → 1.858; raw +76.9% (95%: +74.7% to +79.1%) | 0.7942 → 1.394; raw +75.6% (95%: +69.0% to +82.1%), +0.6001 in the gauge's unit | 1.089 → 1.703; raw +56.3% (95%: +49.8% to +62.8%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | 20 → 19.03; raw −4.8% (95%: −7.8% to −1.9%) | 20 → 19.88; raw −0.6% (95%: −9.3% to +8.0%) | 20 → 19.59; raw −2.0% (95%: −7.4% to +3.3%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 20 (15 trials, 2 allowed, 4 refused); acting: 19 to 21 (11 trials, 2 allowed, 5 refused); acting: 19 to 20 (15 trials, 1 allowed, 4 refused); run B: acting: 19 to 21 (18 trials, 2 allowed, 3 refused); acting: 19 to 23 (20 trials, 4 allowed, 3 refused); acting: 19 to 21 (16 trials, 2 allowed, 4 refused); run C: acting: 20 to 21 (17 trials, 1 allowed, 5 refused); acting: 19 to 20 (14 trials, 1 allowed, 4 refused); acting: 19 to 21 (14 trials, 2 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,606, 2,206, 2,291 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,535 | 1,501 | 1535 → 1501; raw −2.2% (95%: −21.9% to +17.6%); LOSS | 960 → 946.4; raw −1.4% (95%: −5.5% to +2.7%); LOSS | 1005 → 1006; raw +0.1% (95%: −1.8% to +2.1%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 1,587 | 1,568 | 1587 → 1568; raw −1.2% (95%: −6.3% to +3.9%); LOSS | 970.8 → 970.8; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 1009 → 1008; raw −0.1% (95%: −0.9% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.43%) |
| latency, 95th percentile (ms, lag included) | 117.1 | 76.2 | 117.1 → 76.24; raw −34.9% (95%: −637.7% to +568.0%); GAIN | 1.752 → 19.07; raw +988.5% (95%: −3327.8% to +5304.7%); LOSS | 2.586 → 2.507; raw −3.0% (95%: −22.0% to +16.0%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 1,334 | 688.7 | 1334 → 688.7; raw −48.4% (95%: −544.6% to +447.8%); GAIN | 70.65 → 788.7; raw +1016.4% (95%: −3143.7% to +5176.6%); LOSS | 19.38 → 4.373; raw −77.4% (95%: −422.4% to +267.6%); GAIN | **the runs disagree** |
| latency, median (ms) | 0.774 | 0.788 | 0.774 → 0.7883; raw +1.9% (95%: −3.1% to +6.8%), +0.0143 in the gauge's unit; LOSS | 0.7967 → 0.7827; raw −1.8% (95%: −6.7% to +3.1%), −0.0140 in the gauge's unit; GAIN | 1.28 → 1.278; raw −0.1% (95%: −1.5% to +1.3%); STEADY | **the runs disagree** |
| latency, mean (ms) | 44.1 | 24.3 | 44.08 → 24.25; raw −45.0% (95%: −548.1% to +458.1%); GAIN | 2.886 → 19.97; raw +592.0% (95%: −1812.4% to +2996.3%); LOSS | 1.859 → 1.604; raw −13.7% (95%: −113.5% to +86.1%); GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.0 | 19.95 → 18.97; raw −4.9% (95%: −6.8% to −3.0%); GAIN | 19.92 → 18.18; raw −8.7% (95%: −18.5% to +1.1%); GAIN | 19.44 → 16.38; raw −15.8% (95%: −27.9% to −3.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.7 | 20 → 21.67; raw +8.3% (95%: −6.0% to +22.7%); power given | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.226 | 0.228 | 0.2262 → 0.2281; raw +0.9% (95%: +0.2% to +1.6%), +0.0019 in the gauge's unit; power given | 0.1457 → 0.1429; raw −2.0% (95%: −10.4% to +6.4%), −0.0029 in the gauge's unit; GAIN | 0.2239 → 0.2235; raw −0.2% (95%: −2.4% to +2.1%), −0.0004 in the gauge's unit; STEADY | **the runs disagree** |
| host CPU-seconds | 390.2 | 393.5 | 390.2 → 393.5; raw +0.9% (95%: +0.4% to +1.3%); power given | 254.4 → 249.6; raw −1.9% (95%: −10.2% to +6.5%); GAIN | 392.9 → 392.2; raw −0.2% (95%: −2.5% to +2.2%); STEADY | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.565 | 0.584 | 0.5654 → 0.5837; raw +3.3% (95%: −17.9% to +24.4%), +0.0184 in the gauge's unit; power given | 0.5888 → 0.5863; raw −0.4% (95%: −11.6% to +10.8%), −0.0025 in the gauge's unit; STEADY | 0.8686 → 0.866; raw −0.3% (95%: −4.2% to +3.6%), −0.0027 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.6 | 1.11 | 0.5997 → 1.11; raw +85.1% (95%: +82.5% to +87.7%), +0.5104 in the gauge's unit | 0.5084 → 0.9685; raw +90.5% (95%: +69.6% to +111.4%), +0.4601 in the gauge's unit | 0.6246 → 1.145; raw +83.3% (95%: +79.7% to +86.9%), +0.5203 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | 20 → 19.15; raw −4.2% (95%: −6.7% to −1.8%) | 20 → 18.64; raw −6.8% (95%: −16.0% to +2.4%) | 20 → 17.05; raw −14.8% (95%: −21.2% to −8.4%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 20 (18 trials, 1 allowed, 4 refused); acting: 17 to 22 (15 trials, 5 allowed, 4 refused); acting: 19 to 20 (9 trials, 1 allowed, 5 refused); run B: acting: 16 to 21 (14 trials, 5 allowed, 3 refused); acting: 18 to 21 (13 trials, 3 allowed, 3 refused); acting: 19 to 20 (11 trials, 1 allowed, 4 refused); run C: acting: 15 to 20 (11 trials, 5 allowed, 4 refused); acting: 16 to 21 (9 trials, 5 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused).

**Across 3 workloads: 3 gauge-rows GAIN, 6 LOSS, 6 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 11 STEADY, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
