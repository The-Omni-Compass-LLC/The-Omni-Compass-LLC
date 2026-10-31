# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39625603596 | `e32bbb605501` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 3 |
| B | 39628245625 | `990711a99dc4` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 3 |
| C | 39630669154 | `67b7cd6bf1e8` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 15,805, 16,528, 33,899 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6,950 | 6,949 | 6950 → 6949; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 7272 → 7269; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | 1.491e+04 → 1.492e+04; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (transactions a second) | 6,950 | 6,949 | 6950 → 6949; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 7272 → 7269; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | 1.491e+04 → 1.492e+04; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 0.852 | 0.894 | 0.8523 → 0.8943; raw +4.9% (95%: −10.9% to +20.8%), +0.0420 in the gauge's unit; LOSS | 1.289 → 1.168; raw −9.4% (95%: −16.3% to −2.4%); GAIN | 0.2607 → 0.296; raw +13.6% (95%: −7.4% to +34.5%), +0.0353 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 1.63 | 1.92 | 1.629 → 1.921; raw +17.9% (95%: −44.7% to +80.6%); LOSS | 3.388 → 3.659; raw +8.0% (95%: −21.0% to +37.0%); LOSS | 0.6063 → 0.9377; raw +54.6% (95%: −25.4% to +134.7%), +0.3313 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.339 | 0.341 | 0.3387 → 0.341; raw +0.7% (95%: −1.2% to +2.5%), +0.0023 in the gauge's unit; LOSS | 0.3687 → 0.3633; raw −1.4% (95%: −2.5% to −0.4%), −0.0053 in the gauge's unit; GAIN | 0.146 → 0.149; raw +2.1% (95%: −3.1% to +7.2%), +0.0030 in the gauge's unit; LOSS | **the runs disagree** |
| latency, mean (ms) | 0.425 | 0.449 | 0.4254 → 0.4493; raw +5.6% (95%: −4.5% to +15.7%), +0.0239 in the gauge's unit; LOSS | 0.5352 → 0.5778; raw +8.0% (95%: −7.9% to +23.9%), +0.0426 in the gauge's unit; LOSS | 0.1686 → 0.1973; raw +17.0% (95%: −5.3% to +39.4%), +0.0287 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.8 | 16.8 | 19.76 → 16.77; raw −15.1% (95%: −29.2% to −1.1%); GAIN | 19.42 → 17.53; raw −9.7% (95%: −23.7% to +4.2%); GAIN | 19.92 → 17.5; raw −12.1% (95%: −37.6% to +13.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.378 | 0.379 | 0.3777 → 0.3792; raw +0.4% (95%: −0.8% to +1.6%), +0.0015 in the gauge's unit; STEADY | 0.3217 → 0.3147; raw −2.2% (95%: −3.8% to −0.6%), −0.0070 in the gauge's unit; GAIN | 0.316 → 0.326; raw +3.1% (95%: −3.8% to +10.0%), +0.0099 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 633.4 | 635.8 | 633.4 → 635.8; raw +0.4% (95%: −0.8% to +1.5%); STEADY | 473.7 → 461.9; raw −2.5% (95%: −4.2% to −0.8%); GAIN | 536.4 → 553.9; raw +3.2% (95%: −3.6% to +10.1%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.203 | 0.203 | 0.2025 → 0.2033; raw +0.4% (95%: −0.5% to +1.2%), +0.0008 in the gauge's unit; STEADY | 0.1448 → 0.1412; raw −2.4% (95%: −4.4% to −0.5%), −0.0035 in the gauge's unit; GAIN | 0.07994 → 0.08252; raw +3.2% (95%: −3.5% to +9.9%), +0.0026 in the gauge's unit; power given | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.48 | 3.22 | 2.483 → 3.216; raw +29.5% (95%: +26.6% to +32.5%) | 2.619 → 3.309; raw +26.4% (95%: +24.4% to +28.3%) | 2.684 → 3.308; raw +23.2% (95%: +14.8% to +31.6%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | 20 → 17.71; raw −11.5% (95%: −31.8% to +8.8%) | 20 → 18.01; raw −10.0% (95%: −23.9% to +4.0%) | 20 → 17.76; raw −11.2% (95%: −35.4% to +13.0%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 12 to 20 (12 trials, 8 allowed, 3 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run B: acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run C: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 13 to 20 (10 trials, 7 allowed, 3 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,704, 4,590, 3,809 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,590 | 1,589 | 1590 → 1589; raw −0.1% (95%: −2.4% to +2.2%); STEADY | 1972 → 1980; raw +0.4% (95%: −1.8% to +2.6%); STEADY | 1631 → 1631; raw ±0.0% (95%: −4.3% to +4.2%); STEADY | STEADY, under the floor (the three runs' mean 0.10%) |
| throughput (transactions a second) | 1,631 | 1,629 | 1631 → 1629; raw −0.1% (95%: −0.3% to +0.1%); STEADY | 2019 → 2020; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 1675 → 1674; raw −0.1% (95%: −0.8% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms, lag included) | 7.11 | 6.5 | 7.105 → 6.499; raw −8.5% (95%: −57.1% to +40.0%); GAIN | 6.665 → 6.143; raw −7.8% (95%: −34.5% to +18.9%); GAIN | 7.478 → 7.67; raw +2.6% (95%: −102.9% to +108.0%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 180.9 | 181.9 | 180.9 → 181.9; raw +0.5% (95%: −54.1% to +55.2%); LOSS | 164.4 → 152; raw −7.6% (95%: −71.6% to +56.5%); GAIN | 197.6 → 187.7; raw −5.0% (95%: −111.4% to +101.3%); GAIN | **the runs disagree** |
| latency, median (ms) | 1.52 | 1.53 | 1.522 → 1.533; raw +0.7% (95%: +0.4% to +1.0%); LOSS | 1.269 → 1.267; raw −0.2% (95%: −2.9% to +2.5%); STEADY | 1.527 → 1.528; raw +0.1% (95%: −1.5% to +1.8%); STEADY | STEADY, under the floor (the three runs' mean 0.22%) |
| latency, mean (ms) | 6.22 | 6.18 | 6.22 → 6.184; raw −0.6% (95%: −67.0% to +65.9%); GAIN | 5.571 → 4.969; raw −10.8% (95%: −73.1% to +51.5%); GAIN | 6.779 → 6.753; raw −0.4% (95%: −123.0% to +122.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.9 | 19.0 | 19.91 → 18.99; raw −4.6% (95%: −8.7% to −0.5%); GAIN | 19.95 → 19.22; raw −3.7% (95%: −7.4% to +0.1%); GAIN | 19.99 → 18.92; raw −5.4% (95%: −7.1% to −3.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.7 | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.33 | 0.333 | 0.3301 → 0.3332; raw +0.9% (95%: +0.2% to +1.7%), +0.0031 in the gauge's unit; power given | 0.4294 → 0.4294; raw ±0.0% (95%: −2.1% to +2.0%), ±0.0000 in the gauge's unit; STEADY | 0.3405 → 0.3403; raw −0.1% (95%: −1.2% to +1.1%), −0.0002 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.30%) |
| host CPU-seconds | 496.7 | 501.4 | 496.7 → 501.4; raw +0.9% (95%: +0.2% to +1.7%); power given | 734.9 → 734.8; raw ±0.0% (95%: −2.1% to +2.1%); STEADY | 512.7 → 512.1; raw −0.1% (95%: −1.5% to +1.3%); STEADY | STEADY, under the floor (the three runs' mean 0.27%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.694 | 0.701 | 0.6941 → 0.7011; raw +1.0% (95%: −0.7% to +2.7%), +0.0071 in the gauge's unit; power given | 0.8282 → 0.8245; raw −0.4% (95%: −1.5% to +0.6%), −0.0037 in the gauge's unit; STEADY | 0.6984 → 0.698; raw −0.1% (95%: −5.7% to +5.5%), −0.0005 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.17%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.84 | 1.031 → 1.838; raw +78.3% (95%: +73.2% to +83.4%) | 1.169 → 1.981; raw +69.4% (95%: +68.6% to +70.2%) | 1.009 → 1.81; raw +79.3% (95%: +74.4% to +84.3%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | 20 → 19.23; raw −3.9% (95%: −6.5% to −1.2%) | 20 → 19.46; raw −2.7% (95%: −6.5% to +1.1%) | 20 → 19.15; raw −4.3% (95%: −5.7% to −2.8%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 22 (17 trials, 4 allowed, 2 refused); acting: 19 to 21 (13 trials, 2 allowed, 3 refused); acting: 19 to 20 (14 trials, 1 allowed, 4 refused); run B: acting: 18 to 21 (16 trials, 3 allowed, 3 refused); acting: 19 to 21 (13 trials, 2 allowed, 3 refused); left native (13 trials, 0 allowed, 4 refused); run C: acting: 18 to 21 (16 trials, 3 allowed, 3 refused); acting: 18 to 20 (13 trials, 2 allowed, 4 refused); acting: 18 to 20 (15 trials, 2 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,912, 1,906, 3,284 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 840.8 | 839.7 | 840.8 → 839.7; raw −0.1% (95%: −0.7% to +0.4%); STEADY | 839.4 → 838.3; raw −0.1% (95%: −0.8% to +0.5%); STEADY | 1436 → 1441; raw +0.4% (95%: −0.1% to +1.0%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| throughput (transactions a second) | 841.6 | 841.1 | 841.6 → 841.1; raw −0.1% (95%: −0.3% to +0.1%); STEADY | 839.8 → 839; raw −0.1% (95%: −0.5% to +0.3%); STEADY | 1444 → 1445; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms, lag included) | 5.94 | 6.19 | 5.943 → 6.188; raw +4.1% (95%: −38.9% to +47.1%); LOSS | 5.29 → 5.936; raw +12.2% (95%: +9.5% to +14.9%); LOSS | 3.564 → 2.836; raw −20.4% (95%: −54.8% to +13.9%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 23.7 | 24.8 | 23.74 → 24.77; raw +4.4% (95%: −47.0% to +55.7%); LOSS | 12.12 → 15.34; raw +26.6% (95%: −15.9% to +69.0%); LOSS | 34.58 → 14.81; raw −57.2% (95%: −141.1% to +26.7%); GAIN | **the runs disagree** |
| latency, median (ms) | 1.89 | 1.9 | 1.893 → 1.898; raw +0.3% (95%: −0.7% to +1.3%); STEADY | 1.887 → 1.906; raw +1.0% (95%: −0.1% to +2.1%); LOSS | 1.211 → 1.196; raw −1.2% (95%: −2.8% to +0.3%); GAIN | **the runs disagree** |
| latency, mean (ms) | 2.85 | 2.96 | 2.846 → 2.959; raw +4.0% (95%: −21.6% to +29.6%); LOSS | 2.525 → 2.692; raw +6.6% (95%: −4.9% to +18.2%); LOSS | 2.33 → 1.788; raw −23.3% (95%: −56.6% to +10.1%); GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.9 | 16.9 | 19.89 → 16.93; raw −14.9% (95%: −26.9% to −2.8%); GAIN | 19.82 → 17.69; raw −10.7% (95%: −24.8% to +3.3%); GAIN | 19.93 → 18.89; raw −5.2% (95%: −11.2% to +0.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 20.3 | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | 20 → 22; raw +10.0% (95%: −2.4% to +22.4%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.233 | 0.235 | 0.2331 → 0.2346; raw +0.7% (95%: −1.8% to +3.1%), +0.0015 in the gauge's unit; power given | 0.2324 → 0.2358; raw +1.5% (95%: +0.3% to +2.6%), +0.0034 in the gauge's unit; power given | 0.2645 → 0.2605; raw −1.5% (95%: −3.7% to +0.6%), −0.0040 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 363.5 | 366.1 | 363.5 → 366.1; raw +0.7% (95%: −1.8% to +3.2%); power given | 362.2 → 367.7; raw +1.5% (95%: +0.4% to +2.7%); power given | 469.9 → 462.9; raw −1.5% (95%: −3.5% to +0.5%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.961 | 0.969 | 0.9609 → 0.9688; raw +0.8% (95%: −1.8% to +3.4%), +0.0079 in the gauge's unit; power given | 0.9587 → 0.9746; raw +1.7% (95%: +0.9% to +2.4%), +0.0159 in the gauge's unit; power given | 0.7274 → 0.7136; raw −1.9% (95%: −3.7% to −0.1%), −0.0138 in the gauge's unit; GAIN | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.771 | 1.56 | 0.7707 → 1.558; raw +102.2% (95%: +96.4% to +108.0%), +0.7875 in the gauge's unit | 0.7647 → 1.502; raw +96.5% (95%: +89.2% to +103.8%), +0.7377 in the gauge's unit | 0.5592 → 0.9944; raw +77.8% (95%: +68.6% to +87.1%), +0.4352 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.4 | 20 → 17.44; raw −12.8% (95%: −26.4% to +0.9%) | 20 → 18.27; raw −8.6% (95%: −23.7% to +6.4%) | 20 → 19.14; raw −4.3% (95%: −9.7% to +1.0%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 13 to 21 (12 trials, 8 allowed, 2 refused); acting: 18 to 20 (8 trials, 2 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); run B: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 19 to 21 (8 trials, 2 allowed, 5 refused); run C: acting: 18 to 22 (12 trials, 4 allowed, 3 refused); acting: 19 to 20 (10 trials, 1 allowed, 5 refused); acting: 17 to 22 (11 trials, 5 allowed, 5 refused).

**Across 3 workloads: 4 gauge-rows GAIN, 2 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
