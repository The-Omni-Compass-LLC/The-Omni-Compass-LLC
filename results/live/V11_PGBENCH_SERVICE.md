# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39182915425 | `bc2eb38f4ca8` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| B | 39184166001 | `75478eb28444` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| C | 39185403353 | `ce92ff888e73` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 26,433, 26,132, 39,585 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11,537 | 11,625 | 1.154e+04 → 1.163e+04; raw +0.8% (95%: −2.6% to +4.1%); GAIN | 1.149e+04 → 1.149e+04; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1.742e+04 → 1.732e+04; raw −0.5% (95%: −1.8% to +0.7%); LOSS | **the runs disagree** |
| throughput (transactions a second) | 11,625 | 11,625 | 1.162e+04 → 1.163e+04; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1.149e+04 → 1.149e+04; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1.742e+04 → 1.742e+04; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms, lag included) | 3.99 | 2.83 | 3.994 → 2.834; raw −29.0% (95%: −258.1% to +200.0%); GAIN | 1.264 → 1.249; raw −1.2% (95%: −34.8% to +32.5%); GAIN | 0.316 → 0.3333; raw +5.5% (95%: −37.6% to +48.6%), +0.0173 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 59.8 | 7.7 | 59.79 → 7.705; raw −87.1% (95%: −478.8% to +304.6%); GAIN | 3.102 → 3.363; raw +8.4% (95%: −63.0% to +79.8%); LOSS | 0.987 → 19.59; raw +1884.6% (95%: −4534.3% to +8303.6%), +18.6013 in the gauge's unit; LOSS | **the runs disagree** |
| latency, median (ms) | 0.255 | 0.254 | 0.255 → 0.254; raw −0.4% (95%: −3.8% to +3.0%), −0.0010 in the gauge's unit; STEADY | 0.27 → 0.2703; raw +0.1% (95%: −0.4% to +0.7%), +0.0003 in the gauge's unit; STEADY | 0.1497 → 0.151; raw +0.9% (95%: −4.9% to +6.7%), +0.0013 in the gauge's unit; LOSS | STEADY, under the floor (the three runs' mean 0.21%) |
| latency, mean (ms) | 1.89 | 0.644 | 1.893 → 0.6442; raw −66.0% (95%: −375.3% to +243.4%); GAIN | 0.4535 → 0.5225; raw +15.2% (95%: −37.3% to +67.7%), +0.0690 in the gauge's unit; LOSS | 0.2176 → 0.774; raw +255.7% (95%: −313.9% to +825.3%), +0.5564 in the gauge's unit; LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.3 | 15.8 | 19.33 → 15.8; raw −18.3% (95%: −30.4% to −6.1%); GAIN | 19.53 → 15.66; raw −19.8% (95%: −26.8% to −12.9%); GAIN | 19.37 → 15.14; raw −21.8% (95%: −30.3% to −13.3%); GAIN | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.439 | 0.437 | 0.4387 → 0.4374; raw −0.3% (95%: −3.5% to +2.9%), −0.0013 in the gauge's unit; STEADY | 0.4513 → 0.4512; raw ±0.0% (95%: −0.3% to +0.2%), −0.0002 in the gauge's unit; STEADY | 0.3584 → 0.3614; raw +0.9% (95%: −5.6% to +7.3%), +0.0031 in the gauge's unit; power given | STEADY, under the floor (the three runs' mean 0.17%) |
| host CPU-seconds | 753.3 | 751.2 | 753.3 → 751.2; raw −0.3% (95%: −4.1% to +3.5%); STEADY | 784.8 → 784.8; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 609.3 → 614.6; raw +0.9% (95%: −5.3% to +7.1%); power given | STEADY, under the floor (the three runs' mean 0.20%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.144 | 0.1451 → 0.1436; raw −1.0% (95%: −7.9% to +5.8%), −0.0015 in the gauge's unit; GAIN | 0.1517 → 0.1517; raw ±0.0% (95%: −0.1% to +0.1%), ±0.0000 in the gauge's unit; STEADY | 0.07774 → 0.07883; raw +1.4% (95%: −4.0% to +6.8%), +0.0011 in the gauge's unit; power given | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.96 | 3.63 | 2.962 → 3.63; raw +22.5% (95%: +11.9% to +33.1%) | 3.587 → 4.219; raw +17.6% (95%: +15.0% to +20.2%) | 2.921 → 3.479; raw +19.1% (95%: +14.5% to +23.8%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.4 | 20 → 16.4; raw −18.0% (95%: −23.8% to −12.2%) | 20 → 16.18; raw −19.1% (95%: −25.2% to −13.0%) | 20 → 15.61; raw −22.0% (95%: −36.6% to −7.3%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 13 to 20 (11 trials, 7 allowed, 4 refused); acting: 15 to 20 (10 trials, 5 allowed, 4 refused); acting: 14 to 20 (10 trials, 6 allowed, 4 refused); run B: acting: 12 to 21 (13 trials, 9 allowed, 3 refused); acting: 13 to 21 (12 trials, 8 allowed, 4 refused); acting: 15 to 21 (11 trials, 6 allowed, 3 refused); run C: acting: 15 to 20 (11 trials, 5 allowed, 3 refused); acting: 12 to 20 (11 trials, 8 allowed, 2 refused); acting: 14 to 20 (11 trials, 6 allowed, 3 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,847, 3,938, 3,861 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,641 | 1,637 | 1641 → 1637; raw −0.2% (95%: −6.1% to +5.6%); STEADY | 1689 → 1688; raw −0.1% (95%: −4.2% to +4.0%); STEADY | 1652 → 1652; raw +0.1% (95%: −2.1% to +2.2%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| throughput (transactions a second) | 1,692 | 1,691 | 1692 → 1691; raw −0.1% (95%: −0.7% to +0.6%); STEADY | 1733 → 1732; raw −0.1% (95%: −0.1% to ±0.0%); STEADY | 1699 → 1697; raw −0.1% (95%: −0.4% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| latency, 95th percentile (ms, lag included) | 13.9 | 18.5 | 13.9 → 18.48; raw +33.0% (95%: −427.7% to +493.7%); LOSS | 7.835 → 9.087; raw +16.0% (95%: −128.1% to +160.1%); LOSS | 8.335 → 7.773; raw −6.7% (95%: −33.9% to +20.4%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 197.9 | 216.3 | 197.9 → 216.3; raw +9.3% (95%: −109.8% to +128.5%); LOSS | 177.8 → 170.9; raw −3.9% (95%: −112.3% to +104.6%); GAIN | 211.2 → 189.4; raw −10.3% (95%: −72.9% to +52.3%); GAIN | **the runs disagree** |
| latency, median (ms) | 1.58 | 1.58 | 1.579 → 1.584; raw +0.4% (95%: −4.0% to +4.7%); STEADY | 1.546 → 1.538; raw −0.5% (95%: −2.7% to +1.8%); STEADY | 1.533 → 1.535; raw +0.1% (95%: −1.3% to +1.6%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, mean (ms) | 7.46 | 8.12 | 7.456 → 8.115; raw +8.8% (95%: −169.0% to +186.7%); LOSS | 6.262 → 6.586; raw +5.2% (95%: −120.6% to +131.0%); LOSS | 7.2 → 6.785; raw −5.8% (95%: −57.6% to +46.1%); GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | 19.99 → 19.3; raw −3.5% (95%: −6.7% to −0.2%); GAIN | 20 → 18.56; raw −7.2% (95%: −10.6% to −3.8%); GAIN | 20 → 19.21; raw −3.9% (95%: −8.0% to +0.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.349 | 0.351 | 0.3495 → 0.3508; raw +0.4% (95%: −3.9% to +4.7%), +0.0014 in the gauge's unit; STEADY | 0.3479 → 0.3469; raw −0.3% (95%: −1.3% to +0.7%), −0.0010 in the gauge's unit; STEADY | 0.3437 → 0.3443; raw +0.2% (95%: −0.1% to +0.5%), +0.0006 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.09%) |
| host CPU-seconds | 526.7 | 529.3 | 526.7 → 529.3; raw +0.5% (95%: −4.4% to +5.4%); STEADY | 521.9 → 520.3; raw −0.3% (95%: −1.3% to +0.6%); STEADY | 517 → 517.7; raw +0.1% (95%: −0.3% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.10%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.713 | 0.719 | 0.7134 → 0.7185; raw +0.7% (95%: −8.6% to +10.0%), +0.0051 in the gauge's unit; power given | 0.6867 → 0.6851; raw −0.2% (95%: −3.8% to +3.4%), −0.0016 in the gauge's unit; STEADY | 0.6956 → 0.6963; raw +0.1% (95%: −2.5% to +2.7%), +0.0007 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.19%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.82 | 1.026 → 1.819; raw +77.3% (95%: +76.5% to +78.1%) | 1.032 → 1.813; raw +75.7% (95%: +72.8% to +78.5%) | 1.019 → 1.8; raw +76.8% (95%: +72.1% to +81.4%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.4 | 20 → 19.43; raw −2.8% (95%: −6.6% to +0.9%) | 20 → 18.84; raw −5.8% (95%: −10.4% to −1.2%) | 20 → 19.49; raw −2.5% (95%: −6.2% to +1.1%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 21 (14 trials, 2 allowed, 6 refused); acting: 19 to 21 (16 trials, 2 allowed, 4 refused); acting: 19 to 20 (13 trials, 1 allowed, 5 refused); run B: acting: 17 to 21 (17 trials, 4 allowed, 4 refused); acting: 19 to 20 (12 trials, 1 allowed, 5 refused); acting: 19 to 20 (14 trials, 1 allowed, 3 refused); run C: acting: 18 to 21 (16 trials, 3 allowed, 4 refused); acting: 19 to 21 (11 trials, 2 allowed, 5 refused); left native (12 trials, 0 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,914, 1,923, 1,874 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 840.5 | 840.3 | 840.5 → 840.3; raw ±0.0% (95%: −1.0% to +0.9%); STEADY | 844.6 → 845.9; raw +0.2% (95%: −0.1% to +0.4%); STEADY | 822.7 → 824.3; raw +0.2% (95%: −0.7% to +1.1%); STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| throughput (transactions a second) | 841.9 | 841.0 | 841.9 → 841; raw −0.1% (95%: −0.6% to +0.4%); STEADY | 844.7 → 846.3; raw +0.2% (95%: ±0.0% to +0.4%); STEADY | 824.2 → 824.9; raw +0.1% (95%: −0.2% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms, lag included) | 6.02 | 5.63 | 6.024 → 5.634; raw −6.5% (95%: −94.9% to +82.0%); GAIN | 5.482 → 5.55; raw +1.2% (95%: −4.0% to +6.5%); LOSS | 5.162 → 4.962; raw −3.9% (95%: −70.4% to +62.7%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 18.4 | 15.3 | 18.41 → 15.31; raw −16.8% (95%: −219.5% to +185.9%); GAIN | 13.24 → 13.8; raw +4.2% (95%: −8.0% to +16.4%); LOSS | 17.2 → 13.99; raw −18.7% (95%: −271.5% to +234.1%); GAIN | **the runs disagree** |
| latency, median (ms) | 1.93 | 1.94 | 1.927 → 1.942; raw +0.8% (95%: −6.0% to +7.6%); LOSS | 1.907 → 1.923; raw +0.8% (95%: −1.3% to +2.9%); LOSS | 1.884 → 1.88; raw −0.2% (95%: −1.0% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.45%) |
| latency, mean (ms) | 2.78 | 2.72 | 2.782 → 2.719; raw −2.3% (95%: −50.1% to +45.5%); GAIN | 2.571 → 2.633; raw +2.4% (95%: +0.4% to +4.5%); LOSS | 2.653 → 2.539; raw −4.3% (95%: −60.1% to +51.4%); GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.4 | 17.5 | 19.42 → 17.51; raw −9.9% (95%: −14.4% to −5.3%); GAIN | 19.33 → 17.02; raw −11.9% (95%: −19.9% to −4.0%); GAIN | 19.98 → 16.87; raw −15.6% (95%: −23.4% to −7.8%); GAIN | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.3 | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.239 | 0.241 | 0.2391 → 0.2413; raw +0.9% (95%: −7.2% to +9.1%), +0.0023 in the gauge's unit; power given | 0.2384 → 0.2403; raw +0.8% (95%: −1.1% to +2.7%), +0.0019 in the gauge's unit; power given | 0.2275 → 0.2271; raw −0.2% (95%: −1.6% to +1.3%), −0.0004 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 372.8 | 376.5 | 372.8 → 376.5; raw +1.0% (95%: −7.6% to +9.5%); power given | 371.6 → 374.5; raw +0.8% (95%: −1.2% to +2.8%); power given | 355.1 → 354.3; raw −0.2% (95%: −2.1% to +1.6%); STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.986 | 0.996 | 0.9859 → 0.9957; raw +1.0% (95%: −8.5% to +10.5%), +0.0099 in the gauge's unit; power given | 0.9776 → 0.9839; raw +0.6% (95%: −1.6% to +2.9%), +0.0063 in the gauge's unit; power given | 0.9593 → 0.9553; raw −0.4% (95%: −3.1% to +2.3%), −0.0040 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.41%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.772 | 1.51 | 0.772 → 1.514; raw +96.1% (95%: +85.6% to +106.5%), +0.7415 in the gauge's unit | 0.7615 → 1.5; raw +97.0% (95%: +96.5% to +97.6%), +0.7388 in the gauge's unit | 0.7548 → 1.489; raw +97.2% (95%: +87.8% to +106.6%), +0.7339 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | 20 → 18.18; raw −9.1% (95%: −19.3% to +1.1%) | 20 → 17.66; raw −11.7% (95%: −17.2% to −6.2%) | 20 → 17.29; raw −13.5% (95%: −22.8% to −4.2%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 17 to 21 (9 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused); run B: acting: 17 to 21 (9 trials, 4 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run C: acting: 15 to 20 (10 trials, 5 allowed, 3 refused); acting: 18 to 20 (8 trials, 2 allowed, 4 refused); acting: 16 to 20 (9 trials, 4 allowed, 3 refused).

**Across 3 workloads: 3 gauge-rows GAIN, 0 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 17 STEADY, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
