# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40003718316 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 3 |
| B | 40022493643 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 3 |
| C | 40037187971 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 3 |

> **Warning:** A, B and C are not all on the same engine.

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,523, 16,911, 16,367 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,269 | 7,267 | 7269 → 7267; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 7442 → 7443; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 7197 → 7197; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (transactions a second) | 7,269 | 7,267 | 7269 → 7267; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 7442 → 7443; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 7197 → 7197; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms, lag included) | 1.5 | 1.36 | 1.5 → 1.357; raw −9.6% (95%: −66.3% to +47.1%); GAIN | 1.581 → 1.482; raw −6.3% (95%: −45.0% to +32.5%); GAIN | 1.516 → 1.338; raw −11.7% (95%: −40.2% to +16.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 4.69 | 3.96 | 4.686 → 3.965; raw −15.4% (95%: −103.5% to +72.7%); GAIN | 4.967 → 4.845; raw −2.5% (95%: −34.8% to +29.9%); GAIN | 4.477 → 3.911; raw −12.6% (95%: −55.8% to +30.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.372 | 0.372 | 0.3717 → 0.3723; raw +0.2% (95%: −1.5% to +1.9%), +0.0007 in the gauge's unit; STEADY | 0.3673 → 0.3693; raw +0.5% (95%: −1.2% to +2.3%), +0.0020 in the gauge's unit; LOSS | 0.3743 → 0.3747; raw +0.1% (95%: −0.7% to +0.9%), +0.0003 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.27%) |
| latency, mean (ms) | 0.589 | 0.563 | 0.5891 → 0.5633; raw −4.4% (95%: −37.2% to +28.5%), −0.0258 in the gauge's unit; GAIN | 0.6092 → 0.604; raw −0.8% (95%: −14.4% to +12.7%), −0.0052 in the gauge's unit; GAIN | 0.5923 → 0.5637; raw −4.8% (95%: −19.7% to +10.0%), −0.0285 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.9 | 18.4 | 19.87 → 18.44; raw −7.2% (95%: −9.1% to −5.3%); GAIN | 19.46 → 18.18; raw −6.6% (95%: −11.3% to −1.9%); GAIN | 19.73 → 18.29; raw −7.3% (95%: −7.8% to −6.8%); GAIN | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.325 | 0.327 | 0.3249 → 0.3269; raw +0.6% (95%: −2.9% to +4.2%), +0.0020 in the gauge's unit; power given | 0.3241 → 0.3272; raw +0.9% (95%: −1.5% to +3.4%), +0.0031 in the gauge's unit; power given | 0.327 → 0.3277; raw +0.2% (95%: −1.3% to +1.6%), +0.0006 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 479.1 | 482.4 | 479.1 → 482.4; raw +0.7% (95%: −3.5% to +4.9%); power given | 475.7 → 480.9; raw +1.1% (95%: −1.6% to +3.8%); power given | 483.3 → 484.2; raw +0.2% (95%: −1.6% to +1.9%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.146 | 0.148 | 0.1465 → 0.1475; raw +0.7% (95%: −3.4% to +4.8%), +0.0010 in the gauge's unit; power given | 0.1421 → 0.1436; raw +1.1% (95%: −1.8% to +4.0%), +0.0016 in the gauge's unit; power given | 0.1492 → 0.1495; raw +0.2% (95%: −1.6% to +2.0%), +0.0003 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.59 | 3.37 | 2.588 → 3.367; raw +30.1% (95%: +27.7% to +32.6%) | 2.657 → 3.364; raw +26.6% (95%: +25.5% to +27.8%) | 2.643 → 3.408; raw +29.0% (95%: +26.9% to +31.0%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | 20 → 18.95; raw −5.3% (95%: −5.7% to −4.9%) | 20 → 18.9; raw −5.5% (95%: −6.2% to −4.9%) | 20 → 18.95; raw −5.2% (95%: −5.8% to −4.7%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run B: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run C: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,860, 3,802, 3,894 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,647 | 1,654 | 1647 → 1654; raw +0.4% (95%: −4.0% to +4.9%); STEADY | 1626 → 1632; raw +0.4% (95%: −2.8% to +3.5%); STEADY | 1673 → 1670; raw −0.1% (95%: −1.3% to +1.1%); STEADY | STEADY, under the floor (the three runs' mean 0.23%) |
| throughput (transactions a second) | 1,696 | 1,699 | 1696 → 1699; raw +0.1% (95%: −0.6% to +0.9%); STEADY | 1674 → 1672; raw −0.1% (95%: −0.2% to +0.1%); STEADY | 1714 → 1711; raw −0.2% (95%: −1.0% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 9.82 | 8.51 | 9.818 → 8.505; raw −13.4% (95%: −84.1% to +57.4%); GAIN | 8.078 → 8.315; raw +2.9% (95%: −58.5% to +64.3%); LOSS | 6.992 → 7.131; raw +2.0% (95%: −5.2% to +9.2%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 210.5 | 189.1 | 210.5 → 189.1; raw −10.2% (95%: −126.9% to +106.6%); GAIN | 206.5 → 183.4; raw −11.2% (95%: −84.1% to +61.7%); GAIN | 178.4 → 182.1; raw +2.1% (95%: −57.0% to +61.2%); LOSS | **the runs disagree** |
| latency, median (ms) | 1.57 | 1.58 | 1.57 → 1.576; raw +0.4% (95%: −0.5% to +1.3%); STEADY | 1.534 → 1.571; raw +2.4% (95%: +0.5% to +4.3%); LOSS | 1.479 → 1.479; raw ±0.0% (95%: −2.7% to +2.8%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 7.49 | 6.84 | 7.494 → 6.841; raw −8.7% (95%: −116.5% to +99.1%); GAIN | 7.158 → 6.474; raw −9.5% (95%: −94.6% to +75.5%); GAIN | 6.049 → 6.127; raw +1.3% (95%: −56.4% to +59.0%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | 20 → 19.35; raw −3.2% (95%: −9.9% to +3.4%); GAIN | 20 → 19.24; raw −3.8% (95%: −9.4% to +1.8%); GAIN | 20 → 19.67; raw −1.6% (95%: −5.1% to +1.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 22; raw +10.0% (95%: +10.0% to +10.0%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.353 | 0.355 | 0.3526 → 0.3546; raw +0.6% (95%: −0.2% to +1.3%), +0.0020 in the gauge's unit; power given | 0.3424 → 0.3527; raw +3.0% (95%: +0.9% to +5.1%), +0.0103 in the gauge's unit; power given | 0.3425 → 0.3429; raw +0.1% (95%: −2.2% to +2.5%), +0.0005 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 531.8 | 534.5 | 531.8 → 534.5; raw +0.5% (95%: −0.3% to +1.3%); power given | 516.1 → 533.2; raw +3.3% (95%: +0.8% to +5.8%); power given | 513.5 → 514.6; raw +0.2% (95%: −2.4% to +2.8%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.718 | 0.718 | 0.7178 → 0.7182; raw +0.1% (95%: −4.2% to +4.3%), +0.0004 in the gauge's unit; STEADY | 0.7053 → 0.7259; raw +2.9% (95%: +0.1% to +5.7%), +0.0206 in the gauge's unit; power given | 0.6822 → 0.6847; raw +0.4% (95%: −1.6% to +2.4%), +0.0025 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.84 | 1.03 → 1.837; raw +78.4% (95%: +68.9% to +87.9%) | 1.017 → 1.842; raw +81.1% (95%: +74.6% to +87.6%) | 1.031 → 1.78; raw +72.7% (95%: +69.9% to +75.5%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | 20 → 19.5; raw −2.5% (95%: −8.8% to +3.7%) | 20 → 19.46; raw −2.7% (95%: −7.5% to +2.1%) | 20 → 19.85; raw −0.7% (95%: −4.2% to +2.7%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 20 to 21 (12 trials, 1 allowed, 6 refused); acting: 19 to 21 (10 trials, 2 allowed, 5 refused); acting: 18 to 20 (11 trials, 2 allowed, 6 refused); run B: acting: 19 to 21 (13 trials, 2 allowed, 5 refused); acting: 19 to 20 (10 trials, 1 allowed, 6 refused); acting: 18 to 20 (12 trials, 2 allowed, 6 refused); run C: acting: 20 to 21 (12 trials, 1 allowed, 5 refused); acting: 19 to 21 (11 trials, 2 allowed, 3 refused); acting: 20 to 21 (10 trials, 1 allowed, 5 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,876, 2,882, 3,301 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 825.5 | 824.5 | 825.5 → 824.5; raw −0.1% (95%: −0.6% to +0.4%); STEADY | 1267 → 1267; raw ±0.0% (95%: −0.6% to +0.7%); STEADY | 1427 → 1449; raw +1.5% (95%: −4.4% to +7.4%); GAIN | STEADY, under the floor (the three runs' mean 0.48%) |
| throughput (transactions a second) | 825.5 | 824.5 | 825.5 → 824.5; raw −0.1% (95%: −0.6% to +0.3%); STEADY | 1267 → 1268; raw +0.1% (95%: −0.4% to +0.6%); STEADY | 1451 → 1451; raw ±0.0% (95%: −0.5% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms, lag included) | 4.66 | 4.74 | 4.665 → 4.74; raw +1.6% (95%: −11.6% to +14.8%); LOSS | 3.314 → 3.515; raw +6.1% (95%: −9.9% to +22.1%); LOSS | 6.731 → 1.747; raw −74.0% (95%: −388.8% to +240.7%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 9.59 | 9.81 | 9.592 → 9.813; raw +2.3% (95%: −26.6% to +31.2%); LOSS | 7.369 → 9.581; raw +30.0% (95%: −53.8% to +113.8%); LOSS | 105.9 → 5.39; raw −94.9% (95%: −467.4% to +277.6%); GAIN | **the runs disagree** |
| latency, median (ms) | 1.92 | 1.92 | 1.916 → 1.924; raw +0.5% (95%: −1.4% to +2.3%); STEADY | 1.283 → 1.293; raw +0.8% (95%: +0.4% to +1.2%); LOSS | 0.825 → 0.834; raw +1.1% (95%: +0.3% to +1.9%), +0.0090 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, mean (ms) | 2.4 | 2.42 | 2.396 → 2.421; raw +1.0% (95%: −6.7% to +8.7%); LOSS | 1.653 → 1.794; raw +8.5% (95%: −12.0% to +29.1%); LOSS | 4.308 → 1.159; raw −73.1% (95%: −363.7% to +217.6%); GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.7 | 18.4 | 19.73 → 18.39; raw −6.8% (95%: −10.9% to −2.7%); GAIN | 19.53 → 17.47; raw −10.6% (95%: −20.2% to −0.9%); GAIN | 19.89 → 18.36; raw −7.7% (95%: −11.6% to −3.8%); GAIN | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.233 | 0.235 | 0.2333 → 0.2352; raw +0.8% (95%: −2.1% to +3.7%), +0.0019 in the gauge's unit; power given | 0.3071 → 0.3096; raw +0.8% (95%: +0.4% to +1.2%), +0.0025 in the gauge's unit; power given | 0.2159 → 0.218; raw +1.0% (95%: ±0.0% to +2.0%), +0.0022 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds | 364.4 | 367.7 | 364.4 → 367.7; raw +0.9% (95%: −2.2% to +3.9%); power given | 535.5 → 539.8; raw +0.8% (95%: +0.4% to +1.2%); power given | 372.7 → 376.1; raw +0.9% (95%: ±0.0% to +1.8%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.981 | 0.991 | 0.9811 → 0.9909; raw +1.0% (95%: −2.3% to +4.3%), +0.0099 in the gauge's unit; power given | 0.9392 → 0.9465; raw +0.8% (95%: −0.1% to +1.7%), +0.0073 in the gauge's unit; power given | 0.5807 → 0.5767; raw −0.7% (95%: −5.9% to +4.6%), −0.0039 in the gauge's unit; GAIN | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.757 | 1.48 | 0.7574 → 1.476; raw +94.9% (95%: +88.3% to +101.5%), +0.7187 in the gauge's unit | 0.7344 → 1.286; raw +75.1% (95%: +70.5% to +79.7%), +0.5517 in the gauge's unit | 0.5767 → 1.099; raw +90.6% (95%: +81.3% to +99.9%), +0.5225 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | 20 → 18.94; raw −5.3% (95%: −5.4% to −5.2%) | 20 → 17.89; raw −10.5% (95%: −27.7% to +6.6%) | 20 → 18.56; raw −7.2% (95%: −13.0% to −1.3%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run B: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 12 to 20 (11 trials, 8 allowed, 2 refused); acting: 16 to 21 (11 trials, 5 allowed, 5 refused); run C: acting: 19 to 20 (6 trials, 1 allowed, 5 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused); acting: 15 to 20 (10 trials, 5 allowed, 3 refused).

**Across 3 workloads: 6 gauge-rows GAIN, 2 LOSS, 10 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 11 STEADY, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
