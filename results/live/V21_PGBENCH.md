# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40258014810 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| B | 40281459100 | `fa6da97bbaa6` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |
| C | 40400963499 | `5e222aa21371` | omni-v21 (digest b658f05d43c1e602, 63 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,493, 16,085, 16,753 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,256 | 7,259 | 7256 → 7259; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | 7073 → 7080; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 7371 → 7368; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (transactions a second) | 7,256 | 7,259 | 7256 → 7259; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | 7073 → 7080; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 7371 → 7368; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 1.41 | 1.44 | 1.412 → 1.442; raw +2.1% (95%: −23.5% to +27.7%); LOSS | 1.166 → 1.226; raw +5.1% (95%: −9.5% to +19.7%); LOSS | 1.731 → 1.503; raw −13.2% (95%: −72.7% to +46.4%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 4.05 | 3.94 | 4.05 → 3.935; raw −2.8% (95%: −49.4% to +43.7%); GAIN | 3.217 → 3.392; raw +5.4% (95%: −53.7% to +64.5%); LOSS | 5.085 → 4.479; raw −11.9% (95%: −59.1% to +35.2%); GAIN | **the runs disagree** |
| latency, median (ms) | 0.371 | 0.372 | 0.371 → 0.372; raw +0.3% (95%: −1.5% to +2.0%), +0.0010 in the gauge's unit; STEADY | 0.366 → 0.369; raw +0.8% (95%: −0.4% to +2.0%), +0.0030 in the gauge's unit; LOSS | 0.3707 → 0.371; raw +0.1% (95%: −0.3% to +0.5%), +0.0003 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.39%) |
| latency, mean (ms) | 0.565 | 0.57 | 0.5654 → 0.5698; raw +0.8% (95%: −14.9% to +16.5%), +0.0044 in the gauge's unit; LOSS | 0.5184 → 0.5339; raw +3.0% (95%: −10.7% to +16.7%), +0.0154 in the gauge's unit; LOSS | 0.6224 → 0.5927; raw −4.8% (95%: −21.7% to +12.2%), −0.0297 in the gauge's unit; GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.8 | 18.4 | 19.82 → 18.38; raw −7.2% (95%: −12.5% to −2.0%); GAIN | 19.89 → 18.46; raw −7.2% (95%: −9.4% to −5.0%); GAIN | 19.48 → 18.32; raw −6.0% (95%: −11.0% to −1.0%); GAIN | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.325 | 0.326 | 0.3247 → 0.3264; raw +0.5% (95%: −2.3% to +3.4%), +0.0017 in the gauge's unit; power given | 0.3121 → 0.3162; raw +1.3% (95%: −0.8% to +3.4%), +0.0041 in the gauge's unit; power given | 0.3246 → 0.3258; raw +0.4% (95%: −0.7% to +1.4%), +0.0012 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 486.9 | 489.6 | 486.9 → 489.6; raw +0.6% (95%: −2.7% to +3.8%); power given | 467.4 → 474.1; raw +1.4% (95%: −0.9% to +3.8%); power given | 323.4 → 324.8; raw +0.4% (95%: −0.9% to +1.7%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.15 | 0.1491 → 0.1499; raw +0.5% (95%: −3.1% to +4.1%), +0.0008 in the gauge's unit; power given | 0.1469 → 0.1488; raw +1.3% (95%: −1.2% to +3.9%), +0.0020 in the gauge's unit; power given | 0.1462 → 0.1469; raw +0.5% (95%: −0.7% to +1.6%), +0.0007 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.37 | 9.13 | 8.368 → 9.133; raw +9.2% (95%: +1.1% to +17.2%) | 8.202 → 9.021; raw +10.0% (95%: +6.5% to +13.5%) | 5.571 → 6.093; raw +9.4% (95%: +5.7% to +13.0%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | 20 → 18.87; raw −5.7% (95%: −9.9% to −1.4%) | 20 → 18.97; raw −5.2% (95%: −6.1% to −4.2%) | 20 → 18.86; raw −5.7% (95%: −6.0% to −5.3%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 3 refused); run B: acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run C: acting: 16 to 20 (6 trials, 4 allowed, 2 refused); acting: 16 to 20 (7 trials, 4 allowed, 2 refused); acting: 16 to 20 (7 trials, 4 allowed, 2 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,839, 3,911, 3,754 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,658 | 1,657 | 1658 → 1657; raw ±0.0% (95%: −0.8% to +0.7%); STEADY | 1687 → 1683; raw −0.2% (95%: −1.5% to +1.1%); STEADY | 1611 → 1608; raw −0.2% (95%: −0.9% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.14%) |
| throughput (transactions a second) | 1,690 | 1,689 | 1690 → 1689; raw ±0.0% (95%: −0.5% to +0.4%); STEADY | 1720 → 1721; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 1651 → 1650; raw −0.1% (95%: −0.5% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 6.05 | 5.93 | 6.052 → 5.932; raw −2.0% (95%: −11.3% to +7.3%); GAIN | 7.438 → 7.067; raw −5.0% (95%: −25.0% to +15.1%); GAIN | 7.008 → 7.282; raw +3.9% (95%: −5.5% to +13.3%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 146.0 | 148.4 | 146 → 148.4; raw +1.6% (95%: −61.6% to +64.8%); LOSS | 141.7 → 159; raw +12.2% (95%: −91.8% to +116.3%); LOSS | 182.9 → 180.2; raw −1.5% (95%: −18.7% to +15.7%); GAIN | **the runs disagree** |
| latency, median (ms) | 1.48 | 1.48 | 1.476 → 1.476; raw ±0.0% (95%: −0.8% to +0.8%); STEADY | 1.512 → 1.511; raw −0.1% (95%: −3.3% to +3.1%); STEADY | 1.579 → 1.581; raw +0.1% (95%: −2.1% to +2.3%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, mean (ms) | 5.02 | 4.91 | 5.017 → 4.905; raw −2.2% (95%: −41.4% to +37.0%); GAIN | 5.355 → 5.553; raw +3.7% (95%: −39.3% to +46.7%); LOSS | 6.226 → 6.213; raw −0.2% (95%: −23.4% to +23.0%); STEADY | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | 19.96 → 19.32; raw −3.2% (95%: −6.4% to ±0.0%); GAIN | 19.96 → 19.69; raw −1.3% (95%: −4.7% to +2.0%); GAIN | 19.97 → 19.73; raw −1.2% (95%: −2.0% to −0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.333 | 0.334 | 0.3333 → 0.334; raw +0.2% (95%: +0.1% to +0.3%), +0.0008 in the gauge's unit; STEADY | 0.3446 → 0.3444; raw ±0.0% (95%: −3.3% to +3.2%), −0.0002 in the gauge's unit; STEADY | 0.3439 → 0.3434; raw −0.2% (95%: −0.6% to +0.3%), −0.0005 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| host CPU-seconds | 501.1 | 502.2 | 501.1 → 502.2; raw +0.2% (95%: −0.1% to +0.5%); STEADY | 519.3 → 518.8; raw −0.1% (95%: −3.7% to +3.5%); STEADY | 347.2 → 346.4; raw −0.2% (95%: −0.7% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.672 | 0.673 | 0.6717 → 0.6733; raw +0.2% (95%: −0.7% to +1.2%), +0.0016 in the gauge's unit; STEADY | 0.6842 → 0.6851; raw +0.1% (95%: −4.3% to +4.6%), +0.0008 in the gauge's unit; STEADY | 0.7183 → 0.718; raw ±0.0% (95%: −1.2% to +1.1%), −0.0003 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.4 | 3.15 | 2.403 → 3.145; raw +30.9% (95%: +24.9% to +36.8%) | 2.449 → 3.23; raw +31.9% (95%: +28.2% to +35.6%) | 1.563 → 2.099; raw +34.3% (95%: +32.9% to +35.8%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.6 | 20 → 19.6; raw −2.0% (95%: −3.5% to −0.5%) | 20 → 19.84; raw −0.8% (95%: −4.4% to +2.8%) | 20 → 19.95; raw −0.3% (95%: −0.6% to +0.1%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (12 trials, 0 allowed, 4 refused); acting: 19 to 20 (12 trials, 1 allowed, 7 refused); acting: 18 to 21 (12 trials, 3 allowed, 6 refused); run B: acting: 19 to 20 (11 trials, 1 allowed, 7 refused); acting: 19 to 21 (12 trials, 2 allowed, 4 refused); acting: 20 to 22 (13 trials, 2 allowed, 4 refused); run C: acting: 19 to 21 (9 trials, 2 allowed, 3 refused); acting: 20 to 21 (7 trials, 1 allowed, 4 refused); acting: 20 to 21 (6 trials, 1 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,219, 1,916, 1,821 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,317 | 1,325 | 1317 → 1325; raw +0.6% (95%: −22.9% to +24.0%); GAIN | 842 → 843.3; raw +0.1% (95%: −0.3% to +0.6%); STEADY | 802.5 → 802.3; raw ±0.0% (95%: −0.5% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.23%) |
| throughput (transactions a second) | 1,415 | 1,404 | 1415 → 1404; raw −0.8% (95%: −3.8% to +2.3%); LOSS | 842.1 → 843.3; raw +0.1% (95%: −0.3% to +0.6%); STEADY | 802.5 → 802.3; raw ±0.0% (95%: −0.5% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.22%) |
| latency, 95th percentile (ms, lag included) | 242.4 | 86.6 | 242.4 → 86.58; raw −64.3% (95%: −455.5% to +327.0%); GAIN | 4.139 → 4.14; raw ±0.0% (95%: −7.0% to +7.1%); STEADY | 4.369 → 4.27; raw −2.3% (95%: −18.2% to +13.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 1,180 | 407.7 | 1180 → 407.7; raw −65.5% (95%: −404.4% to +273.4%); GAIN | 7.958 → 7.955; raw ±0.0% (95%: −13.9% to +13.8%); STEADY | 8.292 → 8.361; raw +0.8% (95%: −26.7% to +28.4%); LOSS | **the runs disagree** |
| latency, median (ms) | 0.847 | 0.845 | 0.8473 → 0.8453; raw −0.2% (95%: −10.8% to +10.3%), −0.0020 in the gauge's unit; STEADY | 1.806 → 1.806; raw ±0.0% (95%: −1.1% to +1.1%); STEADY | 1.881 → 1.868; raw −0.7% (95%: −3.8% to +2.4%); GAIN | STEADY, under the floor (the three runs' mean 0.30%) |
| latency, mean (ms) | 50.3 | 28.5 | 50.3 → 28.55; raw −43.3% (95%: −452.6% to +366.0%); GAIN | 2.209 → 2.206; raw −0.2% (95%: −2.5% to +2.1%); STEADY | 2.307 → 2.291; raw −0.7% (95%: −8.4% to +7.0%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.9 | 19.6 | 19.93 → 19.61; raw −1.7% (95%: −3.9% to +0.6%); GAIN | 19.73 → 18.25; raw −7.5% (95%: −9.7% to −5.3%); GAIN | 19.42 → 18.42; raw −5.1% (95%: −15.0% to +4.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.216 | 0.213 | 0.2157 → 0.2132; raw −1.2% (95%: −10.0% to +7.7%), −0.0026 in the gauge's unit; GAIN | 0.2225 → 0.2234; raw +0.4% (95%: −2.2% to +3.1%), +0.0009 in the gauge's unit; STEADY | 0.22 → 0.2188; raw −0.6% (95%: −4.7% to +3.6%), −0.0012 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.45%) |
| host CPU-seconds | 373.2 | 368.9 | 373.2 → 368.9; raw −1.1% (95%: −10.1% to +7.8%); GAIN | 346.9 → 348.3; raw +0.4% (95%: −2.4% to +3.3%); STEADY | 230 → 228.6; raw −0.6% (95%: −4.9% to +3.7%); GAIN | STEADY, under the floor (the three runs' mean 0.44%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.63 | 0.62 | 0.6305 → 0.6203; raw −1.6% (95%: −32.0% to +28.8%), −0.0102 in the gauge's unit; GAIN | 0.9154 → 0.9179; raw +0.3% (95%: −2.2% to +2.7%), +0.0024 in the gauge's unit; STEADY | 0.9552 → 0.9497; raw −0.6% (95%: −5.2% to +4.1%), −0.0056 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.18 | 1.63 | 1.181 → 1.63; raw +38.1% (95%: +26.1% to +50.0%) | 1.458 → 2.116; raw +45.2% (95%: +44.7% to +45.7%) | 0.9355 → 1.401; raw +49.8% (95%: +46.0% to +53.5%), +0.4655 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | 20 → 19.74; raw −1.3% (95%: −2.2% to −0.4%) | 20 → 18.9; raw −5.5% (95%: −6.8% to −4.2%) | 20 → 18.93; raw −5.4% (95%: −5.7% to −5.1%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 18 to 20 (19 trials, 2 allowed, 2 refused); acting: 19 to 21 (18 trials, 2 allowed, 2 refused); acting: 17 to 21 (14 trials, 4 allowed, 4 refused); run B: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run C: acting: 18 to 20 (6 trials, 2 allowed, 3 refused); acting: 17 to 20 (6 trials, 3 allowed, 2 refused); acting: 17 to 20 (6 trials, 3 allowed, 2 refused).

**Across 3 workloads: 6 gauge-rows GAIN, 0 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 18 STEADY, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
