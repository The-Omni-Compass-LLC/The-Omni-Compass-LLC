# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40135948429 | `19db275eb391` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |
| B | 40137076834 | `19db275eb391` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |
| C | 40138213124 | `96ebf29137fe` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,879, 16,623, 16,353 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,422 | 7,355 | 7422 → 7355; raw −0.9% (95%: −4.7% to +2.9%); LOSS | 7315 → 7292; raw −0.3% (95%: −0.8% to +0.2%); STEADY | 7190 → 7176; raw −0.2% (95%: −1.0% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.47%) |
| throughput (transactions a second) | 7,422 | 7,424 | 7422 → 7424; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | 7315 → 7310; raw −0.1% (95%: −0.3% to +0.1%); STEADY | 7190 → 7197; raw +0.1% (95%: −0.1% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms, lag included) | 1.85 | 2.45 | 1.854 → 2.449; raw +32.1% (95%: −68.1% to +132.3%); LOSS | 1.603 → 2.104; raw +31.3% (95%: −142.9% to +205.5%); LOSS | 2.015 → 1.371; raw −31.9% (95%: −127.8% to +63.9%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 5.4 | 52.3 | 5.4 → 52.32; raw +868.9% (95%: −2847.1% to +4585.0%); LOSS | 4.876 → 9.786; raw +100.7% (95%: −295.6% to +497.1%); LOSS | 5.282 → 11.71; raw +121.6% (95%: −418.0% to +661.2%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.378 | 0.376 | 0.378 → 0.3763; raw −0.4% (95%: −2.7% to +1.9%), −0.0017 in the gauge's unit; STEADY | 0.3737 → 0.3763; raw +0.7% (95%: −2.4% to +3.9%), +0.0027 in the gauge's unit; LOSS | 0.381 → 0.3733; raw −2.0% (95%: −8.0% to +4.0%), −0.0077 in the gauge's unit; GAIN | **the runs disagree** |
| latency, mean (ms) | 0.646 | 1.88 | 0.6459 → 1.877; raw +190.6% (95%: −610.3% to +991.5%), +1.2308 in the gauge's unit; LOSS | 0.6118 → 0.9252; raw +51.2% (95%: −84.2% to +186.7%), +0.3134 in the gauge's unit; LOSS | 0.6512 → 0.8428; raw +29.4% (95%: −69.0% to +127.8%), +0.1916 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.2 | 15.6 | 19.25 → 15.64; raw −18.8% (95%: −36.8% to −0.8%); GAIN | 19.46 → 16.85; raw −13.4% (95%: −28.0% to +1.1%); GAIN | 19.53 → 14.67; raw −24.9% (95%: −35.0% to −14.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.339 | 0.337 | 0.3389 → 0.3373; raw −0.5% (95%: −3.9% to +3.0%), −0.0016 in the gauge's unit; STEADY | 0.3295 → 0.3323; raw +0.9% (95%: −3.0% to +4.7%), +0.0028 in the gauge's unit; power given | 0.3357 → 0.3263; raw −2.8% (95%: −11.2% to +5.5%), −0.0095 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 501.4 | 498.7 | 501.4 → 498.7; raw −0.5% (95%: −4.4% to +3.3%); GAIN | 486 → 491.4; raw +1.1% (95%: −3.4% to +5.6%); power given | 498.9 → 482.8; raw −3.2% (95%: −12.8% to +6.3%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.151 | 0.1501 → 0.1507; raw +0.4% (95%: −2.0% to +2.8%), +0.0006 in the gauge's unit; STEADY | 0.1477 → 0.1497; raw +1.4% (95%: −3.2% to +6.0%), +0.0021 in the gauge's unit; power given | 0.1542 → 0.1495; raw −3.0% (95%: −12.5% to +6.4%), −0.0047 in the gauge's unit; GAIN | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.69 | 3.43 | 2.694 → 3.428; raw +27.3% (95%: +18.4% to +36.1%) | 2.585 → 3.416; raw +32.2% (95%: +27.6% to +36.7%) | 2.706 → 3.516; raw +29.9% (95%: +26.9% to +32.9%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.2 | 20 → 16.23; raw −18.8% (95%: −30.8% to −6.9%) | 20 → 17.3; raw −13.5% (95%: −22.1% to −4.9%) | 20 → 15.57; raw −22.1% (95%: −37.9% to −6.3%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 14 to 20 (10 trials, 6 allowed, 3 refused); acting: 15 to 20 (9 trials, 5 allowed, 4 refused); acting: 11 to 20 (12 trials, 9 allowed, 2 refused); run B: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 4 refused); run C: acting: 11 to 20 (12 trials, 9 allowed, 3 refused); acting: 16 to 20 (9 trials, 4 allowed, 5 refused); acting: 11 to 20 (12 trials, 9 allowed, 2 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 5,535, 6,705, 3,913 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,376 | 2,367 | 2376 → 2367; raw −0.4% (95%: −1.8% to +1.0%); STEADY | 2813 → 2830; raw +0.6% (95%: −1.4% to +2.6%); GAIN | 1671 → 1669; raw −0.1% (95%: −3.6% to +3.4%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (transactions a second) | 2,434 | 2,433 | 2434 → 2433; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2954 → 2950; raw −0.1% (95%: −0.7% to +0.5%); STEADY | 1721 → 1721; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 4.19 | 4.16 | 4.191 → 4.159; raw −0.8% (95%: −46.5% to +44.9%); GAIN | 34.48 → 9.502; raw −72.4% (95%: −277.8% to +133.0%); GAIN | 7.925 → 8.958; raw +13.0% (95%: −103.3% to +129.4%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 185.7 | 207.0 | 185.7 → 207; raw +11.4% (95%: −30.7% to +53.6%); LOSS | 525.9 → 477.9; raw −9.1% (95%: −13.1% to −5.1%); GAIN | 198.7 → 224.9; raw +13.2% (95%: −49.9% to +76.2%); LOSS | **the runs disagree** |
| latency, median (ms) | 1.06 | 1.04 | 1.062 → 1.038; raw −2.2% (95%: −7.6% to +3.2%); GAIN | 0.722 → 0.706; raw −2.2% (95%: −14.2% to +9.8%), −0.0160 in the gauge's unit; GAIN | 1.516 → 1.519; raw +0.2% (95%: −1.0% to +1.4%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 5.47 | 6.18 | 5.47 → 6.178; raw +12.9% (95%: −41.2% to +67.1%); LOSS | 16.67 → 14.45; raw −13.3% (95%: −37.3% to +10.6%); GAIN | 7.005 → 7.759; raw +10.8% (95%: −83.4% to +104.9%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | 19.99 → 19.06; raw −4.7% (95%: −5.4% to −4.0%); GAIN | 20 → 19.6; raw −2.0% (95%: −6.8% to +2.9%); GAIN | 19.98 → 18.83; raw −5.8% (95%: −9.5% to −2.0%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.0 | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.416 | 0.411 | 0.4162 → 0.4109; raw −1.3% (95%: −4.7% to +2.2%), −0.0052 in the gauge's unit; GAIN | 0.3314 → 0.3247; raw −2.0% (95%: −12.3% to +8.2%), −0.0067 in the gauge's unit; GAIN | 0.3422 → 0.3434; raw +0.3% (95%: ±0.0% to +0.7%), +0.0012 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 721.6 | 712.3 | 721.6 → 712.3; raw −1.3% (95%: −4.7% to +2.2%); GAIN | 564.8 → 553.3; raw −2.0% (95%: −12.2% to +8.2%); GAIN | 513.3 → 515; raw +0.3% (95%: −0.1% to +0.8%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.675 | 0.669 | 0.6747 → 0.6687; raw −0.9% (95%: −3.5% to +1.7%), −0.0061 in the gauge's unit; GAIN | 0.4463 → 0.4345; raw −2.6% (95%: −13.9% to +8.6%), −0.0117 in the gauge's unit; GAIN | 0.6827 → 0.6858; raw +0.5% (95%: −3.1% to +4.0%), +0.0031 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.08 | 1.66 | 1.075 → 1.663; raw +54.6% (95%: +50.7% to +58.5%) | 0.8534 → 1.367; raw +60.1% (95%: +58.9% to +61.4%), +0.5132 in the gauge's unit | 1.005 → 1.779; raw +77.0% (95%: +73.8% to +80.2%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | 20 → 19.24; raw −3.8% (95%: −4.1% to −3.5%) | 20 → 19.67; raw −1.6% (95%: −6.7% to +3.4%) | 20 → 19.07; raw −4.6% (95%: −7.5% to −1.8%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 21 (16 trials, 2 allowed, 5 refused); acting: 19 to 20 (14 trials, 1 allowed, 5 refused); acting: 19 to 20 (17 trials, 1 allowed, 4 refused); run B: acting: 19 to 21 (18 trials, 2 allowed, 4 refused); acting: 19 to 20 (15 trials, 1 allowed, 5 refused); acting: 19 to 21 (15 trials, 2 allowed, 4 refused); run C: acting: 18 to 21 (16 trials, 3 allowed, 4 refused); acting: 17 to 20 (13 trials, 3 allowed, 4 refused); acting: 19 to 20 (12 trials, 1 allowed, 5 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,440, 1,832, 1,192 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,505 | 1,507 | 1505 → 1507; raw +0.2% (95%: −1.7% to +2.0%); STEADY | 632.4 → 599.1; raw −5.3% (95%: −9.0% to −1.6%); LOSS | 336.4 → 362.6; raw +7.8% (95%: −25.5% to +41.0%); GAIN | **the runs disagree** |
| throughput (transactions a second) | 1,513 | 1,512 | 1513 → 1512; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | 803.3 → 792; raw −1.4% (95%: −5.1% to +2.3%); LOSS | 521.8 → 523.7; raw +0.4% (95%: −0.9% to +1.6%); STEADY | STEADY, under the floor (the three runs' mean 0.35%) |
| latency, 95th percentile (ms, lag included) | 2.43 | 2.14 | 2.427 → 2.135; raw −12.0% (95%: −81.2% to +57.2%); GAIN | 780.2 → 2673; raw +242.6% (95%: −293.6% to +778.7%); LOSS | 728 → 1018; raw +39.8% (95%: −233.2% to +312.8%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 25.0 | 20.4 | 25.03 → 20.37; raw −18.6% (95%: −343.2% to +306.0%); GAIN | 3487 → 3259; raw −6.5% (95%: −66.6% to +53.6%); GAIN | 1441 → 2074; raw +44.0% (95%: −262.5% to +350.4%); LOSS | **the runs disagree** |
| latency, median (ms) | 0.862 | 0.847 | 0.8623 → 0.8467; raw −1.8% (95%: −10.2% to +6.5%), −0.0157 in the gauge's unit; GAIN | 1.289 → 1.351; raw +4.8% (95%: −6.2% to +15.9%); LOSS | 5.7 → 6.452; raw +13.2% (95%: −230.0% to +256.3%); LOSS | **the runs disagree** |
| latency, mean (ms) | 1.75 | 1.65 | 1.753 → 1.653; raw −5.7% (95%: −147.1% to +135.7%); GAIN | 174.3 → 309.3; raw +77.5% (95%: −75.3% to +230.3%); LOSS | 135.5 → 150.8; raw +11.2% (95%: −185.2% to +207.7%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.8 | 17.5 | 19.82 → 17.52; raw −11.6% (95%: −18.6% to −4.7%); GAIN | 20 → 19.97; raw −0.2% (95%: −1.1% to +0.8%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.0 | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.234 | 0.23 | 0.2337 → 0.2305; raw −1.4% (95%: −9.2% to +6.4%), −0.0032 in the gauge's unit; GAIN | 0.1985 → 0.1963; raw −1.1% (95%: −5.3% to +3.1%), −0.0022 in the gauge's unit; GAIN | 0.1326 → 0.131; raw −1.2% (95%: −6.9% to +4.5%), −0.0016 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 402.3 | 396.8 | 402.3 → 396.8; raw −1.4% (95%: −9.1% to +6.4%); GAIN | 348.2 → 344.8; raw −1.0% (95%: −5.5% to +3.5%); GAIN | 234.7 → 231.8; raw −1.2% (95%: −7.2% to +4.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.594 | 0.585 | 0.5942 → 0.5852; raw −1.5% (95%: −10.8% to +7.7%), −0.0090 in the gauge's unit; GAIN | 1.232 → 1.288; raw +4.5% (95%: +1.1% to +8.0%); power given | 1.552 → 1.438; raw −7.4% (95%: −39.4% to +24.7%); GAIN | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.6 | 1.13 | 0.6001 → 1.126; raw +87.6% (95%: +75.5% to +99.8%), +0.5259 in the gauge's unit | 0.5928 → 1.151; raw +94.2% (95%: +89.9% to +98.5%), +0.5584 in the gauge's unit | 0.5225 → 1.049; raw +100.7% (95%: +97.2% to +104.3%), +0.5262 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | 20 → 17.8; raw −11.0% (95%: −18.1% to −3.8%) | 20 → 19.96; raw −0.2% (95%: −0.8% to +0.3%) | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 21 (9 trials, 3 allowed, 4 refused); acting: 15 to 20 (12 trials, 5 allowed, 4 refused); acting: 15 to 21 (11 trials, 6 allowed, 2 refused); run B: left native (22 trials, 0 allowed, 0 refused); left native (23 trials, 0 allowed, 0 refused); left native (25 trials, 0 allowed, 2 refused); run C: left native (19 trials, 0 allowed, 0 refused); left native (23 trials, 0 allowed, 0 refused); left native (30 trials, 0 allowed, 0 refused).

**Across 3 workloads: 9 gauge-rows GAIN, 2 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 9 STEADY, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
