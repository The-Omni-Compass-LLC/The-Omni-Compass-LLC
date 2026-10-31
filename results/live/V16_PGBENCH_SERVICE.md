# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39869913163 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |
| B | 39871667274 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |
| C | 39873437772 | `a9694fbc7d2a` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,768, 16,404, 38,530 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,380 | 7,361 | 7380 → 7361; raw −0.3% (95%: −1.4% to +0.8%); STEADY | 7218 → 7165; raw −0.7% (95%: −3.7% to +2.3%); LOSS | 1.695e+04 → 1.695e+04; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.33%) |
| throughput (transactions a second) | 7,380 | 7,380 | 7380 → 7380; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 7218 → 7215; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | 1.695e+04 → 1.695e+04; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms, lag included) | 1.38 | 1.62 | 1.376 → 1.621; raw +17.8% (95%: −19.9% to +55.5%); LOSS | 1.444 → 1.34; raw −7.2% (95%: −54.3% to +39.9%); GAIN | 0.415 → 0.3377; raw −18.6% (95%: −48.9% to +11.6%), −0.0773 in the gauge's unit; GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 4.21 | 17.5 | 4.207 → 17.53; raw +316.7% (95%: −950.0% to +1583.4%); LOSS | 4.101 → 43.71; raw +965.7% (95%: −3170.9% to +5102.3%); LOSS | 4.876 → 2.13; raw −56.3% (95%: −223.4% to +110.8%); GAIN | **the runs disagree** |
| latency, median (ms) | 0.368 | 0.371 | 0.3677 → 0.3707; raw +0.8% (95%: −2.9% to +4.6%), +0.0030 in the gauge's unit; LOSS | 0.3707 → 0.3667; raw −1.1% (95%: −8.3% to +6.2%), −0.0040 in the gauge's unit; GAIN | 0.158 → 0.1537; raw −2.7% (95%: −4.6% to −0.9%), −0.0043 in the gauge's unit; GAIN | **the runs disagree** |
| latency, mean (ms) | 0.567 | 0.843 | 0.5672 → 0.8429; raw +48.6% (95%: −124.0% to +221.2%), +0.2756 in the gauge's unit; LOSS | 0.5785 → 1.449; raw +150.5% (95%: −472.9% to +774.0%), +0.8708 in the gauge's unit; LOSS | 0.3203 → 0.2729; raw −14.8% (95%: −24.8% to −4.8%), −0.0474 in the gauge's unit; GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.1 | 16.8 | 19.14 → 16.82; raw −12.1% (95%: −23.4% to −0.8%); GAIN | 19.35 → 15.48; raw −20.0% (95%: −34.4% to −5.6%); GAIN | 19.81 → 17.25; raw −13.0% (95%: −29.2% to +3.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.323 | 0.326 | 0.3231 → 0.3263; raw +1.0% (95%: −3.8% to +5.8%), +0.0032 in the gauge's unit; power given | 0.3224 → 0.3168; raw −1.7% (95%: −12.4% to +8.9%), −0.0056 in the gauge's unit; GAIN | 0.3715 → 0.3619; raw −2.6% (95%: −4.7% to −0.5%), −0.0096 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 474.6 | 480.1 | 474.6 → 480.1; raw +1.2% (95%: −4.1% to +6.4%); power given | 475.3 → 465.8; raw −2.0% (95%: −14.0% to +10.0%); GAIN | 631.3 → 615.3; raw −2.5% (95%: −4.8% to −0.2%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.145 | 0.1429 → 0.145; raw +1.4% (95%: −5.0% to +7.8%), +0.0021 in the gauge's unit; power given | 0.1464 → 0.1445; raw −1.3% (95%: −12.9% to +10.4%), −0.0019 in the gauge's unit; GAIN | 0.08277 → 0.08068; raw −2.5% (95%: −4.7% to −0.3%), −0.0021 in the gauge's unit; GAIN | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.61 | 3.4 | 2.608 → 3.402; raw +30.4% (95%: +17.8% to +43.1%) | 2.613 → 3.36; raw +28.6% (95%: +15.9% to +41.2%) | 3.067 → 3.474; raw +13.3% (95%: +9.6% to +16.9%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.1 | 20 → 17.15; raw −14.3% (95%: −44.7% to +16.2%) | 20 → 16.45; raw −17.7% (95%: −29.7% to −5.8%) | 20 → 17.7; raw −11.5% (95%: −27.6% to +4.6%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 9 to 20 (13 trials, 11 allowed, 1 refused); acting: 16 to 20 (9 trials, 4 allowed, 3 refused); run B: acting: 13 to 20 (11 trials, 7 allowed, 3 refused); acting: 15 to 20 (10 trials, 5 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 4 refused); run C: acting: 18 to 20 (7 trials, 2 allowed, 4 refused); acting: 18 to 20 (8 trials, 2 allowed, 5 refused); acting: 15 to 20 (9 trials, 5 allowed, 4 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 5,403, 3,838, 3,771 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,773 | 1,760 | 1773 → 1760; raw −0.8% (95%: −38.8% to +37.2%); LOSS | 1643 → 1644; raw ±0.0% (95%: −4.7% to +4.8%); STEADY | 1621 → 1623; raw +0.1% (95%: −3.1% to +3.4%); STEADY | STEADY, under the floor (the three runs' mean 0.21%) |
| throughput (transactions a second) | 2,341 | 2,324 | 2341 → 2324; raw −0.8% (95%: −5.3% to +3.8%); LOSS | 1688 → 1688; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | 1661 → 1657; raw −0.3% (95%: −0.6% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.34%) |
| latency, 95th percentile (ms, lag included) | 1,604 | 1,724 | 1604 → 1724; raw +7.5% (95%: −190.7% to +205.6%); LOSS | 7.64 → 7.947; raw +4.0% (95%: −88.3% to +96.3%); LOSS | 7.564 → 7.012; raw −7.3% (95%: −43.8% to +29.2%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 2,711 | 5,055 | 2711 → 5055; raw +86.5% (95%: −6.5% to +179.4%); LOSS | 202.3 → 208.7; raw +3.2% (95%: −123.2% to +129.5%); LOSS | 173.5 → 136.7; raw −21.2% (95%: −129.7% to +87.3%); GAIN | **the runs disagree** |
| latency, median (ms) | 1.19 | 1.15 | 1.189 → 1.149; raw −3.3% (95%: −40.0% to +33.3%); GAIN | 1.509 → 1.516; raw +0.5% (95%: −1.6% to +2.6%); STEADY | 1.567 → 1.567; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 233.2 | 273.3 | 233.2 → 273.3; raw +17.2% (95%: −189.9% to +224.3%); LOSS | 6.851 → 7.176; raw +4.7% (95%: −137.7% to +147.2%); LOSS | 6.095 → 5.315; raw −12.8% (95%: −94.8% to +69.2%); GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | 20 → 19.96; raw −0.2% (95%: −4.2% to +3.9%); STEADY | 20 → 19.13; raw −4.4% (95%: −9.8% to +1.1%); GAIN | 19.95 → 19; raw −4.8% (95%: −12.7% to +3.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| server connections alive, most at once | 20.0 | 22.0 | 20 → 22; raw +10.0% (95%: −2.4% to +22.4%); power given | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.376 | 0.373 | 0.3755 → 0.3725; raw −0.8% (95%: −6.0% to +4.4%), −0.0030 in the gauge's unit; GAIN | 0.3427 → 0.3444; raw +0.5% (95%: −1.6% to +2.6%), +0.0017 in the gauge's unit; power given | 0.3436 → 0.3423; raw −0.4% (95%: −1.6% to +0.9%), −0.0013 in the gauge's unit; STEADY | **the runs disagree** |
| host CPU-seconds | 649.5 | 644.5 | 649.5 → 644.5; raw −0.8% (95%: −5.0% to +3.5%); GAIN | 515.1 → 518.3; raw +0.6% (95%: −2.0% to +3.2%); power given | 518 → 515.9; raw −0.4% (95%: −1.9% to +1.1%); STEADY | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.825 | 0.821 | 0.8252 → 0.8207; raw −0.5% (95%: −40.0% to +38.9%), −0.0045 in the gauge's unit; GAIN | 0.6967 → 0.7007; raw +0.6% (95%: −6.5% to +7.6%), +0.0039 in the gauge's unit; power given | 0.71 → 0.7062; raw −0.5% (95%: −5.2% to +4.2%), −0.0038 in the gauge's unit; GAIN | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.925 | 1.6 | 0.9255 → 1.597; raw +72.6% (95%: +61.5% to +83.7%), +0.6719 in the gauge's unit | 1.016 → 1.805; raw +77.7% (95%: +72.6% to +82.8%) | 1.009 → 1.806; raw +79.0% (95%: +71.7% to +86.3%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | 20 → 19.97; raw −0.1% (95%: −3.9% to +3.6%) | 20 → 19.28; raw −3.6% (95%: −9.3% to +2.1%) | 20 → 19.26; raw −3.7% (95%: −12.4% to +5.0%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 21 (15 trials, 2 allowed, 4 refused); acting: 19 to 21 (19 trials, 2 allowed, 3 refused); acting: 19 to 22 (20 trials, 3 allowed, 3 refused); run B: acting: 19 to 21 (14 trials, 2 allowed, 5 refused); acting: 19 to 20 (12 trials, 1 allowed, 4 refused); acting: 19 to 20 (12 trials, 1 allowed, 4 refused); run C: acting: 17 to 21 (15 trials, 4 allowed, 3 refused); acting: 19 to 21 (12 trials, 2 allowed, 6 refused); left native (12 trials, 0 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,649, 1,900, 1,888 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 722.2 | 695.6 | 722.2 → 695.6; raw −3.7% (95%: −19.0% to +11.6%); LOSS | 835.7 → 835.5; raw ±0.0% (95%: −0.5% to +0.4%); STEADY | 830.4 → 830.8; raw ±0.0% (95%: −1.1% to +1.2%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 724.2 | 724.9 | 724.2 → 724.9; raw +0.1% (95%: −0.1% to +0.3%); STEADY | 835.9 → 836.2; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 831.3 → 831.1; raw ±0.0% (95%: −0.9% to +0.9%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 7.65 | 79.5 | 7.649 → 79.47; raw +939.0% (95%: −2928.5% to +4806.5%); LOSS | 4.851 → 4.953; raw +2.1% (95%: −11.8% to +16.0%); LOSS | 5.396 → 5.502; raw +2.0% (95%: −7.7% to +11.6%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 26.5 | 127.6 | 26.54 → 127.6; raw +380.9% (95%: −1117.5% to +1879.2%); LOSS | 9.994 → 12.19; raw +21.9% (95%: −4.4% to +48.2%); LOSS | 13.05 → 13.77; raw +5.5% (95%: −54.3% to +65.3%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 2.15 | 2.22 | 2.154 → 2.225; raw +3.3% (95%: −14.9% to +21.5%); LOSS | 1.877 → 1.875; raw −0.1% (95%: −2.8% to +2.6%); STEADY | 1.905 → 1.9; raw −0.2% (95%: −1.0% to +0.5%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 3.34 | 10.7 | 3.344 → 10.7; raw +220.1% (95%: −669.7% to +1109.8%); LOSS | 2.413 → 2.524; raw +4.6% (95%: −2.1% to +11.3%); LOSS | 2.619 → 2.592; raw −1.0% (95%: −23.3% to +21.2%); GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.8 | 17.7 | 19.79 → 17.67; raw −10.7% (95%: −14.6% to −6.8%); GAIN | 19.7 → 17.14; raw −13.0% (95%: −16.7% to −9.3%); GAIN | 19.73 → 17.21; raw −12.8% (95%: −16.0% to −9.6%); GAIN | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.231 | 0.241 | 0.2306 → 0.2408; raw +4.4% (95%: −16.5% to +25.4%), +0.0102 in the gauge's unit; power given | 0.2299 → 0.2305; raw +0.3% (95%: −4.1% to +4.6%), +0.0006 in the gauge's unit; STEADY | 0.232 → 0.2316; raw −0.2% (95%: −0.8% to +0.4%), −0.0004 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 365.3 | 382.2 | 365.3 → 382.2; raw +4.6% (95%: −17.0% to +26.2%); power given | 358.6 → 359.4; raw +0.2% (95%: −4.4% to +4.8%); STEADY | 362.1 → 361.4; raw −0.2% (95%: −0.9% to +0.5%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 1.12 | 1.23 | 1.124 → 1.226; raw +9.1% (95%: −22.1% to +40.3%); power given | 0.9534 → 0.9559; raw +0.3% (95%: −3.9% to +4.4%), +0.0025 in the gauge's unit; STEADY | 0.9691 → 0.9668; raw −0.2% (95%: −2.0% to +1.5%), −0.0023 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.832 | 1.66 | 0.8316 → 1.664; raw +100.1% (95%: +92.9% to +107.3%), +0.8325 in the gauge's unit | 0.7684 → 1.5; raw +95.2% (95%: +88.3% to +102.1%), +0.7316 in the gauge's unit | 0.7646 → 1.505; raw +96.8% (95%: +95.7% to +97.9%), +0.7403 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.1 | 20 → 18.07; raw −9.7% (95%: −11.9% to −7.5%) | 20 → 17.65; raw −11.7% (95%: −17.6% to −5.8%) | 20 → 17.65; raw −11.7% (95%: −15.2% to −8.3%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 17 to 20 (9 trials, 3 allowed, 4 refused); run B: acting: 16 to 20 (10 trials, 4 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 4 refused); run C: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused).

**Across 3 workloads: 4 gauge-rows GAIN, 4 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 9 STEADY, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
