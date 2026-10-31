# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39108191914 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 3 |
| B | 39116277778 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 3 |
| C | 39123595298 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 46,379, 42,016, 16,770 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 20,082 | 20,341 | 2.008e+04 → 2.034e+04; raw +1.3% (95%: −4.7% to +7.2%); GAIN | 1.843e+04 → 1.846e+04; raw +0.2% (95%: −0.6% to +0.9%); STEADY | 7377 → 7377; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.49%) |
| throughput (transactions a second) | 20,408 | 20,406 | 2.041e+04 → 2.041e+04; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | 1.848e+04 → 1.848e+04; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 7377 → 7377; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms, lag included) | 10.6 | 2.62 | 10.57 → 2.619; raw −75.2% (95%: −409.3% to +258.9%); GAIN | 6.463 → 4.814; raw −25.5% (95%: −145.1% to +94.0%); GAIN | 1.55 → 1.387; raw −10.5% (95%: −27.6% to +6.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 90.8 | 22.5 | 90.79 → 22.48; raw −75.2% (95%: −413.4% to +262.9%); GAIN | 25.4 → 18.62; raw −26.7% (95%: −127.0% to +73.6%); GAIN | 4.631 → 4.093; raw −11.6% (95%: −33.1% to +9.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.199 | 0.197 | 0.1987 → 0.1973; raw −0.7% (95%: −4.5% to +3.1%), −0.0013 in the gauge's unit; GAIN | 0.205 → 0.2053; raw +0.2% (95%: −4.9% to +5.2%), +0.0003 in the gauge's unit; STEADY | 0.372 → 0.3697; raw −0.6% (95%: −2.7% to +1.4%), −0.0023 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.38%) |
| latency, mean (ms) | 3.08 | 0.983 | 3.078 → 0.9826; raw −68.1% (95%: −376.9% to +240.7%); GAIN | 1.326 → 1.039; raw −21.6% (95%: −103.5% to +60.3%); GAIN | 0.6078 → 0.5672; raw −6.7% (95%: −19.4% to +6.1%), −0.0406 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.6 | 16.1 | 19.61 → 16.07; raw −18.0% (95%: −32.4% to −3.7%); GAIN | 19.69 → 17.74; raw −9.9% (95%: −17.3% to −2.6%); GAIN | 19.51 → 18.31; raw −6.1% (95%: −14.8% to +2.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.0 | 20 → 21; raw +5.0% (95%: −7.4% to +17.4%); power given | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.461 | 0.461 | 0.4606 → 0.4613; raw +0.2% (95%: −2.1% to +2.4%), +0.0007 in the gauge's unit; STEADY | 0.4624 → 0.4633; raw +0.2% (95%: −2.0% to +2.4%), +0.0009 in the gauge's unit; STEADY | 0.3286 → 0.326; raw −0.8% (95%: −3.9% to +2.3%), −0.0025 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.14%) |
| host CPU-seconds | 796.6 | 799.0 | 796.6 → 799; raw +0.3% (95%: −2.1% to +2.7%); STEADY | 800.6 → 802.1; raw +0.2% (95%: −2.1% to +2.5%); STEADY | 484 → 479.5; raw −0.9% (95%: −4.6% to +2.7%); GAIN | STEADY, under the floor (the three runs' mean 0.15%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.0882 | 0.0873 | 0.08817 → 0.08729; raw −1.0% (95%: −6.2% to +4.2%), −0.0009 in the gauge's unit; GAIN | 0.09653 → 0.09654; raw ±0.0% (95%: −2.7% to +2.7%), ±0.0000 in the gauge's unit; STEADY | 0.1458 → 0.1444; raw −0.9% (95%: −4.5% to +2.6%), −0.0014 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.74 | 4.15 | 3.741 → 4.152; raw +11.0% (95%: +5.9% to +16.0%) | 4.314 → 4.903; raw +13.6% (95%: +9.9% to +17.4%) | 2.664 → 3.348; raw +25.7% (95%: +18.4% to +32.9%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.5 | 20 → 16.48; raw −17.6% (95%: −32.2% to −3.0%) | 20 → 18.17; raw −9.2% (95%: −15.9% to −2.5%) | 20 → 18.88; raw −5.6% (95%: −6.5% to −4.7%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 14 to 22 (12 trials, 8 allowed, 2 refused); acting: 10 to 20 (13 trials, 10 allowed, 1 refused); acting: 11 to 21 (12 trials, 10 allowed, 1 refused); run B: acting: 15 to 20 (9 trials, 5 allowed, 4 refused); acting: 16 to 21 (10 trials, 5 allowed, 3 refused); acting: 17 to 21 (8 trials, 4 allowed, 4 refused); run C: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 7,615, 7,277, 3,812 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3,149 | 3,150 | 3149 → 3150; raw ±0.0% (95%: −4.2% to +4.3%); STEADY | 3006 → 3049; raw +1.4% (95%: −6.5% to +9.3%); GAIN | 1635 → 1641; raw +0.4% (95%: −2.4% to +3.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 3,350 | 3,350 | 3350 → 3350; raw ±0.0% (95%: −0.4% to +0.3%); STEADY | 3197 → 3197; raw ±0.0% (95%: −0.8% to +0.8%); STEADY | 1677 → 1678; raw ±0.0% (95%: −0.4% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms, lag included) | 92.9 | 114.3 | 92.9 → 114.3; raw +23.0% (95%: −138.4% to +184.3%); LOSS | 120.3 → 46.2; raw −61.6% (95%: −401.3% to +278.1%); GAIN | 8.885 → 8.575; raw −3.5% (95%: −38.2% to +31.2%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 596.7 | 577.1 | 596.7 → 577.1; raw −3.3% (95%: −13.9% to +7.4%); GAIN | 574.4 → 533; raw −7.2% (95%: −93.3% to +78.9%); GAIN | 173.9 → 170.3; raw −2.1% (95%: −76.5% to +72.3%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.692 | 0.701 | 0.692 → 0.7013; raw +1.3% (95%: −7.0% to +9.7%), +0.0093 in the gauge's unit; LOSS | 1.068 → 1.05; raw −1.7% (95%: −7.1% to +3.8%); GAIN | 1.516 → 1.523; raw +0.5% (95%: −0.5% to +1.5%); STEADY | **the runs disagree** |
| latency, mean (ms) | 21.8 | 21.8 | 21.77 → 21.76; raw −0.1% (95%: −45.5% to +45.4%); STEADY | 22.18 → 17.63; raw −20.5% (95%: −169.5% to +128.5%); GAIN | 6.284 → 5.892; raw −6.2% (95%: −79.7% to +67.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | 20 → 19.99; raw −0.1% (95%: −6.5% to +6.4%); STEADY | 20 → 19.62; raw −1.9% (95%: −6.4% to +2.6%); GAIN | 20 → 19.22; raw −3.9% (95%: −6.2% to −1.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 22.0 | 20 → 22; raw +10.0% (95%: −2.4% to +22.4%); power given | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.35 | 0.355 | 0.3505 → 0.3552; raw +1.3% (95%: −5.3% to +8.0%), +0.0047 in the gauge's unit; power given | 0.408 → 0.4061; raw −0.5% (95%: −6.5% to +5.5%), −0.0019 in the gauge's unit; STEADY | 0.3342 → 0.3365; raw +0.7% (95%: −0.8% to +2.2%), +0.0023 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 596.4 | 604.7 | 596.4 → 604.7; raw +1.4% (95%: −4.9% to +7.7%); power given | 704.8 → 701.1; raw −0.5% (95%: −6.4% to +5.4%); GAIN | 502.6 → 506.2; raw +0.7% (95%: −0.8% to +2.2%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.421 | 0.427 | 0.421 → 0.4266; raw +1.3% (95%: −6.8% to +9.5%), +0.0056 in the gauge's unit; power given | 0.5211 → 0.511; raw −1.9% (95%: −6.6% to +2.7%), −0.0101 in the gauge's unit; GAIN | 0.6833 → 0.6853; raw +0.3% (95%: −1.1% to +1.7%), +0.0020 in the gauge's unit; STEADY | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.873 | 1.41 | 0.8726 → 1.414; raw +62.0% (95%: +51.6% to +72.4%), +0.5411 in the gauge's unit | 1.026 → 1.506; raw +46.8% (95%: +42.3% to +51.2%) | 1.014 → 1.808; raw +78.4% (95%: +73.8% to +83.0%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | 20 → 20.04; raw +0.2% (95%: −6.0% to +6.4%) | 20 → 19.69; raw −1.5% (95%: −6.2% to +3.1%) | 20 → 19.34; raw −3.3% (95%: −5.1% to −1.5%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 21 (14 trials, 2 allowed, 4 refused); acting: 19 to 20 (16 trials, 1 allowed, 4 refused); acting: 20 to 22 (14 trials, 2 allowed, 5 refused); run B: acting: 18 to 21 (18 trials, 3 allowed, 3 refused); acting: 20 to 21 (19 trials, 1 allowed, 2 refused); acting: 19 to 20 (12 trials, 1 allowed, 5 refused); run C: acting: 19 to 22 (12 trials, 3 allowed, 5 refused); acting: 18 to 20 (10 trials, 2 allowed, 6 refused); acting: 19 to 20 (11 trials, 1 allowed, 6 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,912, 1,898, 1,858 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 826.6 | 835.0 | 826.6 → 835; raw +1.0% (95%: −5.2% to +7.3%); GAIN | 833.2 → 831.7; raw −0.2% (95%: −1.7% to +1.3%); STEADY | 817.3 → 818.4; raw +0.1% (95%: −0.2% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.32%) |
| throughput (transactions a second) | 839.6 | 839.0 | 839.6 → 839; raw −0.1% (95%: −0.7% to +0.5%); STEADY | 833.7 → 833.6; raw ±0.0% (95%: −0.7% to +0.7%); STEADY | 817.5 → 818.9; raw +0.2% (95%: −0.2% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms, lag included) | 6.84 | 5.42 | 6.842 → 5.416; raw −20.8% (95%: −106.6% to +64.9%); GAIN | 5.14 → 5.736; raw +11.6% (95%: −21.5% to +44.7%); LOSS | 4.84 → 5.294; raw +9.4% (95%: −13.1% to +31.8%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 125.1 | 45.9 | 125.1 → 45.94; raw −63.3% (95%: −467.1% to +340.6%); GAIN | 13.26 → 17.72; raw +33.6% (95%: −88.3% to +155.6%); LOSS | 10.92 → 12.79; raw +17.1% (95%: −40.0% to +74.3%); LOSS | **the runs disagree** |
| latency, median (ms) | 1.89 | 1.87 | 1.892 → 1.873; raw −1.0% (95%: −1.5% to −0.4%); GAIN | 1.885 → 1.907; raw +1.1% (95%: −1.8% to +4.1%); LOSS | 1.875 → 1.884; raw +0.5% (95%: −2.0% to +3.0%); STEADY | **the runs disagree** |
| latency, mean (ms) | 5.99 | 3.23 | 5.995 → 3.235; raw −46.0% (95%: −277.5% to +185.4%); GAIN | 2.558 → 3.441; raw +34.5% (95%: −107.9% to +177.0%); LOSS | 2.425 → 2.552; raw +5.2% (95%: −7.3% to +17.8%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.5 | 18.2 | 19.51 → 18.19; raw −6.7% (95%: −10.2% to −3.3%); GAIN | 19.89 → 17.86; raw −10.2% (95%: −13.5% to −6.9%); GAIN | 19.78 → 18.65; raw −5.7% (95%: −7.8% to −3.6%); GAIN | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.232 | 0.23 | 0.2324 → 0.2299; raw −1.1% (95%: −2.1% to −0.1%), −0.0025 in the gauge's unit; GAIN | 0.2318 → 0.2349; raw +1.3% (95%: −1.3% to +4.0%), +0.0031 in the gauge's unit; power given | 0.2252 → 0.2268; raw +0.7% (95%: −1.3% to +2.7%), +0.0016 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 362.7 | 358.5 | 362.7 → 358.5; raw −1.2% (95%: −2.4% to +0.1%); GAIN | 361.8 → 366.7; raw +1.4% (95%: −1.6% to +4.3%); power given | 351.8 → 354.3; raw +0.7% (95%: −1.1% to +2.6%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.975 | 0.954 | 0.9754 → 0.954; raw −2.2% (95%: −9.7% to +5.3%), −0.0214 in the gauge's unit; GAIN | 0.9648 → 0.9799; raw +1.6% (95%: −2.8% to +5.9%), +0.0151 in the gauge's unit; power given | 0.9565 → 0.9621; raw +0.6% (95%: −1.4% to +2.6%), +0.0056 in the gauge's unit; power given | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.759 | 1.48 | 0.759 → 1.477; raw +94.6% (95%: +88.9% to +100.3%), +0.7177 in the gauge's unit | 0.7627 → 1.502; raw +97.0% (95%: +90.2% to +103.7%), +0.7396 in the gauge's unit | 0.7726 → 1.516; raw +96.2% (95%: +83.1% to +109.3%), +0.7435 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | 20 → 18.88; raw −5.6% (95%: −6.5% to −4.7%) | 20 → 18.37; raw −8.2% (95%: −16.7% to +0.4%) | 20 → 19.07; raw −4.6% (95%: −6.5% to −2.8%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 17 to 20 (9 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run B: acting: 14 to 20 (10 trials, 6 allowed, 2 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 14 to 20 (11 trials, 6 allowed, 2 refused); run C: acting: 17 to 20 (9 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused).

**Across 3 workloads: 10 gauge-rows GAIN, 0 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 12 STEADY, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
