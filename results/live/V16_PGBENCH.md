# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39842347137 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |
| B | 39851575564 | `36cb1cc37947` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |
| C | 39860251731 | `15915c961cd2` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 38,790, 15,965, 25,605 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 17,067 | 17,063 | 1.707e+04 → 1.706e+04; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 7020 → 7023; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 1.127e+04 → 1.126e+04; raw −0.1% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (transactions a second) | 17,067 | 17,063 | 1.707e+04 → 1.706e+04; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 7020 → 7023; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 1.127e+04 → 1.126e+04; raw −0.1% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 0.446 | 0.399 | 0.4463 → 0.3993; raw −10.5% (95%: −36.8% to +15.7%), −0.0470 in the gauge's unit; GAIN | 1.035 → 1.105; raw +6.8% (95%: +1.3% to +12.4%); LOSS | 1.058 → 1.106; raw +4.5% (95%: −16.9% to +25.9%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 2.94 | 1.76 | 2.941 → 1.763; raw −40.1% (95%: −152.4% to +72.3%); GAIN | 2.221 → 2.713; raw +22.2% (95%: +0.8% to +43.5%); LOSS | 2.647 → 2.804; raw +5.9% (95%: −32.4% to +44.3%); LOSS | **the runs disagree** |
| latency, median (ms) | 0.159 | 0.16 | 0.1593 → 0.1603; raw +0.6% (95%: −2.1% to +3.3%), +0.0010 in the gauge's unit; LOSS | 0.36 → 0.3643; raw +1.2% (95%: +0.8% to +1.6%), +0.0043 in the gauge's unit; LOSS | 0.2757 → 0.2757; raw ±0.0% (95%: −5.6% to +5.6%), ±0.0000 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 0.283 | 0.239 | 0.2827 → 0.2394; raw −15.3% (95%: −68.0% to +37.4%), −0.0433 in the gauge's unit; GAIN | 0.4762 → 0.498; raw +4.6% (95%: +0.3% to +8.8%), +0.0218 in the gauge's unit; LOSS | 0.4173 → 0.4411; raw +5.7% (95%: −13.3% to +24.7%), +0.0238 in the gauge's unit; LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.8 | 17.1 | 19.79 → 17.14; raw −13.4% (95%: −27.8% to +1.0%); GAIN | 19.89 → 18.36; raw −7.7% (95%: −8.5% to −6.9%); GAIN | 19.67 → 17.27; raw −12.2% (95%: −24.3% to −0.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | 20 → 20.67; raw +3.3% (95%: −3.8% to +10.5%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.379 | 0.381 | 0.379 → 0.3806; raw +0.4% (95%: −2.0% to +2.8%), +0.0016 in the gauge's unit; STEADY | 0.3024 → 0.3089; raw +2.2% (95%: +0.9% to +3.4%), +0.0065 in the gauge's unit; power given | 0.4513 → 0.4508; raw −0.1% (95%: −3.8% to +3.6%), −0.0006 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 644.9 | 647.7 | 644.9 → 647.7; raw +0.4% (95%: −1.8% to +2.7%); STEADY | 444.6 → 455.6; raw +2.5% (95%: +0.9% to +4.0%); power given | 784.6 → 783.3; raw −0.2% (95%: −3.7% to +3.4%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.084 | 0.0843 | 0.08397 → 0.08435; raw +0.5% (95%: −1.9% to +2.8%), +0.0004 in the gauge's unit; STEADY | 0.1407 → 0.1442; raw +2.4% (95%: +0.8% to +4.0%), +0.0034 in the gauge's unit; power given | 0.1547 → 0.1546; raw −0.1% (95%: −3.6% to +3.4%), −0.0002 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.15 | 3.66 | 3.155 → 3.66; raw +16.0% (95%: +10.9% to +21.2%) | 2.517 → 3.256; raw +29.4% (95%: +22.9% to +35.8%) | 3.551 → 4.197; raw +18.2% (95%: +14.1% to +22.3%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.6 | 20 → 17.56; raw −12.2% (95%: −28.4% to +4.0%) | 20 → 19; raw −5.0% (95%: −6.0% to −4.0%) | 20 → 17.38; raw −13.1% (95%: −26.3% to +0.2%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 12 to 20 (11 trials, 8 allowed, 2 refused); acting: 16 to 20 (9 trials, 4 allowed, 3 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused); run B: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); run C: acting: 16 to 21 (10 trials, 5 allowed, 3 refused); acting: 13 to 20 (11 trials, 7 allowed, 3 refused); acting: 13 to 20 (10 trials, 7 allowed, 2 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 7,219, 3,837, 5,852 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,832 | 2,807 | 2832 → 2807; raw −0.9% (95%: −17.4% to +15.7%); LOSS | 1642 → 1636; raw −0.4% (95%: −4.9% to +4.2%); STEADY | 2484 → 2482; raw −0.1% (95%: −2.8% to +2.6%); STEADY | STEADY, under the floor (the three runs' mean 0.43%) |
| throughput (transactions a second) | 3,166 | 3,163 | 3166 → 3163; raw −0.1% (95%: −1.4% to +1.2%); STEADY | 1687 → 1688; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 2573 → 2575; raw +0.1% (95%: −0.2% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 420.9 | 408.5 | 420.9 → 408.5; raw −3.0% (95%: −293.1% to +287.2%); GAIN | 8.213 → 19.77; raw +140.8% (95%: −493.8% to +775.3%); LOSS | 8.23 → 8.047; raw −2.2% (95%: −114.6% to +110.2%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 1,467 | 953.8 | 1467 → 953.8; raw −35.0% (95%: −282.0% to +212.0%); GAIN | 205.8 → 196.1; raw −4.7% (95%: −123.9% to +114.4%); GAIN | 221.9 → 253.5; raw +14.2% (95%: −29.6% to +58.1%); LOSS | **the runs disagree** |
| latency, median (ms) | 0.756 | 0.754 | 0.7557 → 0.7543; raw −0.2% (95%: −20.1% to +19.7%), −0.0013 in the gauge's unit; STEADY | 1.546 → 1.549; raw +0.2% (95%: −3.2% to +3.7%); STEADY | 1.074 → 1.07; raw −0.4% (95%: −1.9% to +1.1%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, mean (ms) | 69.7 | 56.8 | 69.73 → 56.83; raw −18.5% (95%: −290.8% to +253.7%); GAIN | 6.864 → 7.878; raw +14.8% (95%: −126.3% to +155.8%); LOSS | 7.799 → 8.67; raw +11.2% (95%: −54.1% to +76.4%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | 20 → 19.67; raw −1.7% (95%: −5.8% to +2.4%); GAIN | 19.99 → 19.43; raw −2.8% (95%: −3.7% to −1.9%); GAIN | 20 → 19.84; raw −0.8% (95%: −2.1% to +0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.7 | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | 20 → 22; raw +10.0% (95%: +10.0% to +10.0%); power given | **power given in all three of our runs** |
| host CPU busy (share of the run) | 0.347 | 0.348 | 0.3471 → 0.3475; raw +0.1% (95%: −10.0% to +10.3%), +0.0004 in the gauge's unit; STEADY | 0.3444 → 0.3461; raw +0.5% (95%: −3.1% to +4.1%), +0.0018 in the gauge's unit; power given | 0.4327 → 0.4327; raw ±0.0% (95%: −1.0% to +1.0%), +0.0001 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.21%) |
| host CPU-seconds | 590.5 | 591.1 | 590.5 → 591.1; raw +0.1% (95%: −10.7% to +10.9%); STEADY | 519 → 522.3; raw +0.6% (95%: −3.6% to +4.9%); power given | 750.2 → 750.2; raw ±0.0% (95%: −1.1% to +1.1%); STEADY | STEADY, under the floor (the three runs' mean 0.24%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.465 | 0.469 | 0.4653 → 0.469; raw +0.8% (95%: −25.9% to +27.5%), +0.0037 in the gauge's unit; power given | 0.7024 → 0.7096; raw +1.0% (95%: −7.1% to +9.2%), +0.0072 in the gauge's unit; power given | 0.6712 → 0.6717; raw +0.1% (95%: −1.9% to +2.0%), +0.0005 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.862 | 1.4 | 0.8623 → 1.398; raw +62.1% (95%: +52.5% to +71.8%), +0.5358 in the gauge's unit | 1.014 → 1.822; raw +79.7% (95%: +71.1% to +88.3%) | 1.118 → 1.712; raw +53.2% (95%: +45.7% to +60.6%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | 20 → 19.71; raw −1.4% (95%: −5.8% to +2.9%) | 20 → 19.52; raw −2.4% (95%: −3.0% to −1.8%) | 20 → 20; raw ±0.0% (95%: −1.3% to +1.3%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 20 to 21 (20 trials, 1 allowed, 3 refused); acting: 19 to 20 (17 trials, 1 allowed, 4 refused); acting: 18 to 21 (18 trials, 3 allowed, 3 refused); run B: acting: 19 to 21 (11 trials, 2 allowed, 6 refused); acting: 18 to 21 (11 trials, 3 allowed, 7 refused); acting: 19 to 21 (12 trials, 2 allowed, 3 refused); run C: acting: 20 to 22 (12 trials, 2 allowed, 4 refused); acting: 20 to 21 (19 trials, 1 allowed, 4 refused); acting: 20 to 22 (17 trials, 2 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,179, 2,139, 1,863 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,324 | 1,237 | 1324 → 1237; raw −6.5% (95%: −23.4% to +10.3%); LOSS | 747.3 → 737.7; raw −1.3% (95%: −27.8% to +25.2%); LOSS | 818.8 → 817.8; raw −0.1% (95%: −1.3% to +1.1%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 1,394 | 1,393 | 1394 → 1393; raw −0.1% (95%: −0.1% to ±0.0%); STEADY | 938.9 → 933.1; raw −0.6% (95%: −3.0% to +1.7%); LOSS | 820.7 → 819.8; raw −0.1% (95%: −1.0% to +0.8%); STEADY | STEADY, under the floor (the three runs' mean 0.27%) |
| latency, 95th percentile (ms, lag included) | 56.5 | 299.9 | 56.55 → 299.9; raw +430.3% (95%: −716.0% to +1576.6%); LOSS | 622.3 → 1091; raw +75.3% (95%: −349.2% to +499.8%); LOSS | 6.154 → 6.142; raw −0.2% (95%: −22.6% to +22.2%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 2,750 | 922.2 | 2750 → 922.2; raw −66.5% (95%: −215.4% to +82.4%); GAIN | 1306 → 1722; raw +31.8% (95%: −175.7% to +239.4%); LOSS | 13.95 → 14.69; raw +5.3% (95%: −59.1% to +69.6%); LOSS | **the runs disagree** |
| latency, median (ms) | 0.844 | 0.854 | 0.8443 → 0.8543; raw +1.2% (95%: −7.1% to +9.4%), +0.0100 in the gauge's unit; LOSS | 1.322 → 1.298; raw −1.9% (95%: −26.0% to +22.3%); GAIN | 1.931 → 1.934; raw +0.2% (95%: −1.9% to +2.2%); STEADY | **the runs disagree** |
| latency, mean (ms) | 71.4 | 51.0 | 71.41 → 51.02; raw −28.6% (95%: −234.4% to +177.3%); GAIN | 86.16 → 120.4; raw +39.7% (95%: −197.2% to +276.6%); LOSS | 2.958 → 2.96; raw +0.1% (95%: −50.2% to +50.3%); STEADY | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.4 | 20 → 19.41; raw −2.9% (95%: −7.1% to +1.2%); GAIN | 20 → 19.73; raw −1.4% (95%: −7.9% to +5.2%); GAIN | 19.53 → 18.39; raw −5.9% (95%: −15.3% to +3.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| server connections alive, most at once | 20.0 | 21.0 | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 21; raw +5.0% (95%: +5.0% to +5.0%); power given | 20 → 20.33; raw +1.7% (95%: −5.5% to +8.8%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU busy (share of the run) | 0.212 | 0.215 | 0.2121 → 0.2147; raw +1.2% (95%: −5.1% to +7.6%), +0.0026 in the gauge's unit; power given | 0.2294 → 0.228; raw −0.6% (95%: −7.2% to +6.0%), −0.0014 in the gauge's unit; GAIN | 0.2288 → 0.2296; raw +0.4% (95%: −3.8% to +4.5%), +0.0008 in the gauge's unit; STEADY | **the runs disagree** |
| host CPU-seconds | 366.3 | 371.0 | 366.3 → 371; raw +1.3% (95%: −5.2% to +7.8%); power given | 400.7 → 397.7; raw −0.7% (95%: −7.7% to +6.3%); GAIN | 357.5 → 358.8; raw +0.4% (95%: −3.9% to +4.6%); STEADY | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.615 | 0.67 | 0.6148 → 0.6695; raw +8.9% (95%: −16.6% to +34.4%), +0.0547 in the gauge's unit; power given | 1.194 → 1.202; raw +0.7% (95%: −32.0% to +33.4%); power given | 0.9703 → 0.975; raw +0.5% (95%: −2.6% to +3.6%), +0.0046 in the gauge's unit; STEADY | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.572 | 1.05 | 0.5722 → 1.049; raw +83.2% (95%: +71.5% to +95.0%), +0.4763 in the gauge's unit | 0.6263 → 1.214; raw +93.9% (95%: +83.8% to +103.9%), +0.5879 in the gauge's unit | 0.7584 → 1.495; raw +97.1% (95%: +90.1% to +104.0%), +0.7361 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | 20 → 19.54; raw −2.3% (95%: −5.7% to +1.1%) | 20 → 19.72; raw −1.4% (95%: −7.6% to +4.8%) | 20 → 18.9; raw −5.5% (95%: −7.3% to −3.7%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 20 (15 trials, 1 allowed, 4 refused); acting: 19 to 20 (16 trials, 1 allowed, 3 refused); acting: 19 to 20 (22 trials, 1 allowed, 4 refused); run B: left native (30 trials, 0 allowed, 0 refused); left native (23 trials, 0 allowed, 3 refused); acting: 17 to 20 (21 trials, 3 allowed, 1 refused); run C: acting: 19 to 20 (8 trials, 1 allowed, 6 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (9 trials, 3 allowed, 4 refused).

**Across 3 workloads: 3 gauge-rows GAIN, 3 LOSS, 8 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 11 STEADY, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
