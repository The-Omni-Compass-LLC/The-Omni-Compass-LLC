# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39381449955 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| B | 39412421481 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| C | 39461515383 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | 1184 → 1197; raw +1.1% (95%: +0.8% to +1.4%); GAIN | 1184 → 1190; raw +0.5% (95%: +0.2% to +0.9%); GAIN | 1184 → 1194; raw +0.8% (95%: +0.2% to +1.5%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.79 | 0.798 | 0.7896 → 0.798; raw +1.1% (95%: +0.7% to +1.4%), +0.0084 in the gauge's unit; GAIN | 0.7895 → 0.794; raw +0.6% (95%: +0.2% to +0.9%), +0.0044 in the gauge's unit; GAIN | 0.7892 → 0.7959; raw +0.8% (95%: +0.2% to +1.5%), +0.0067 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.65 | 5.66 | 5.647 → 5.659; raw +0.2% (95%: −0.5% to +0.9%); STEADY | 5.74 → 5.747; raw +0.1% (95%: −0.1% to +0.3%); STEADY | 5.752 → 5.742; raw −0.2% (95%: −0.9% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 99th percentile (ms) | 5.71 | 5.73 | 5.715 → 5.728; raw +0.2% (95%: −0.1% to +0.6%); STEADY | 5.798 → 5.811; raw +0.2% (95%: ±0.0% to +0.4%); STEADY | 5.808 → 5.804; raw −0.1% (95%: −1.0% to +0.9%); STEADY | STEADY, under the floor (the three runs' mean 0.13%) |
| latency, mean (ms) | 1.29 | 1.25 | 1.289 → 1.252; raw −2.9% (95%: −5.3% to −0.4%); GAIN | 1.345 → 1.328; raw −1.3% (95%: −2.3% to −0.2%); GAIN | 1.35 → 1.313; raw −2.7% (95%: −5.9% to +0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 66.0 | 64 → 65.98; raw +3.1% (95%: +1.1% to +5.1%); power given | 64 → 64.66; raw +1.0% (95%: +0.1% to +2.0%); power given | 64 → 65.46; raw +2.3% (95%: −0.5% to +5.1%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 61.2 | 62.5 | 61.2 → 62.54; raw +2.2% (95%: +0.7% to +3.6%); power given | 61.2 → 61.66; raw +0.8% (95%: ±0.0% to +1.5%); power given | 61.19 → 62.26; raw +1.7% (95%: −0.1% to +3.5%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 137,977 | 133,161 | 1.38e+05 → 1.332e+05; raw −3.5% (95%: −4.8% to −2.2%) | 1.38e+05 → 1.364e+05; raw −1.2% (95%: −3.2% to +0.9%) | 1.383e+05 → 1.346e+05; raw −2.7% (95%: −5.1% to −0.3%) | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.122 | 0.1222 → 0.1223; raw +0.1% (95%: −38.6% to +38.7%), +0.0001 in the gauge's unit; STEADY | 0.1173 → 0.1372; raw +16.9% (95%: −1.0% to +34.9%), +0.0198 in the gauge's unit; power given | 0.1282 → 0.1214; raw −5.4% (95%: −9.8% to −0.9%), −0.0069 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 213.0 | 212.1 | 213 → 212.1; raw −0.4% (95%: −43.4% to +42.6%); STEADY | 194.7 → 232.5; raw +19.4% (95%: −0.7% to +39.5%); power given | 214.6 → 202.3; raw −5.7% (95%: −11.1% to −0.3%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.4 | 0.394 | 0.3997 → 0.3938; raw −1.5% (95%: −44.1% to +41.2%), −0.0059 in the gauge's unit; GAIN | 0.3654 → 0.4339; raw +18.7% (95%: −1.1% to +38.5%), +0.0685 in the gauge's unit; power given | 0.4028 → 0.3766; raw −6.5% (95%: −11.5% to −1.5%), −0.0262 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.0 | 0 → 21; raw +21.0000 in the gauge's unit (95%: +16.0313 to +25.9687) | 0 → 18.33; raw +18.3333 in the gauge's unit (95%: +11.1617 to +25.5050) | 0 → 18.33; raw +18.3333 in the gauge's unit (95%: +12.5960 to +24.0707) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); run B: acting: 56 to 72 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused); acting: 56 to 72 (13 trials, 2 allowed, 0 refused); run C: acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 1 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | 1076 → 1076; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 1075 → 1075; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 1075 → 1074; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.718 | 0.7177 → 0.7175; raw ±0.0% (95%: −0.1% to +0.1%), −0.0001 in the gauge's unit; STEADY | 0.7177 → 0.7174; raw ±0.0% (95%: −0.2% to +0.1%), −0.0002 in the gauge's unit; STEADY | 0.7177 → 0.7175; raw ±0.0% (95%: −0.1% to +0.1%), −0.0001 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 5.76 | 5.76 | 5.759 → 5.758; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | 5.701 → 5.699; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 5.215 → 5.219; raw +0.1% (95%: ±0.0% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.82 | 5.83 | 5.817 → 5.83; raw +0.2% (95%: +0.1% to +0.4%); STEADY | 5.754 → 5.755; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | 5.261 → 5.348; raw +1.7% (95%: −0.6% to +3.9%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 1.75 | 1.75 | 1.749 → 1.754; raw +0.3% (95%: −0.4% to +1.0%); STEADY | 1.728 → 1.724; raw −0.2% (95%: −1.4% to +0.9%); STEADY | 1.539 → 1.55; raw +0.8% (95%: −0.7% to +2.2%); LOSS | STEADY, under the floor (the three runs' mean 0.29%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 61.4 | 64 → 61.44; raw −4.0% (95%: −7.9% to −0.1%); GAIN | 64 → 61.93; raw −3.2% (95%: −6.0% to −0.5%); GAIN | 64 → 62.4; raw −2.5% (95%: −2.8% to −2.2%); GAIN | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 55.5 | 57.15 → 55.46; raw −3.0% (95%: −7.3% to +1.4%); GAIN | 57.15 → 56.02; raw −2.0% (95%: −5.1% to +1.2%); GAIN | 57.15 → 56.48; raw −1.2% (95%: −1.6% to −0.7%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 71,738 | 71,792 | 7.174e+04 → 7.179e+04; raw +0.1% (95%: −0.3% to +0.4%) | 7.173e+04 → 7.181e+04; raw +0.1% (95%: −0.3% to +0.5%) | 7.169e+04 → 7.174e+04; raw +0.1% (95%: −0.1% to +0.3%) | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.142 | 0.1447 → 0.1421; raw −1.8% (95%: −74.2% to +70.6%), −0.0026 in the gauge's unit; GAIN | 0.1447 → 0.1529; raw +5.7% (95%: +2.6% to +8.7%), +0.0082 in the gauge's unit; power given | 0.07126 → 0.07009; raw −1.6% (95%: −90.1% to +86.8%), −0.0012 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 98.1 | 95.7 | 98.13 → 95.67; raw −2.5% (95%: −88.0% to +83.0%); GAIN | 99.52 → 106.2; raw +6.8% (95%: +4.0% to +9.5%); power given | 50.81 → 49.8; raw −2.0% (95%: −96.7% to +92.7%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.507 | 0.494 | 0.5066 → 0.4939; raw −2.5% (95%: −87.9% to +82.9%), −0.0127 in the gauge's unit; GAIN | 0.5141 → 0.5489; raw +6.8% (95%: +3.9% to +9.6%), +0.0348 in the gauge's unit; power given | 0.2626 → 0.2576; raw −1.9% (95%: −96.9% to +93.0%), −0.0051 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 8 | 0 → 8; raw +8.0000 in the gauge's unit (95%: +3.0313 to +12.9687) | 0 → 7.333; raw +7.3333 in the gauge's unit (95%: +1.5960 to +13.0707) | 0 → 6; raw +6.0000 in the gauge's unit (95%: +6.0000 to +6.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,287 | 1266 → 1287; raw +1.6% (95%: +1.4% to +1.9%); GAIN | 1267 → 1279; raw +1.0% (95%: +0.8% to +1.2%); GAIN | 1267 → 1280; raw +1.0% (95%: +0.4% to +1.6%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.846 | 0.859 | 0.8456 → 0.8594; raw +1.6% (95%: +1.4% to +1.9%), +0.0138 in the gauge's unit; GAIN | 0.845 → 0.8535; raw +1.0% (95%: +0.8% to +1.2%), +0.0085 in the gauge's unit; GAIN | 0.845 → 0.8535; raw +1.0% (95%: +0.4% to +1.6%), +0.0085 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.23 | 5.23 | 5.23 → 5.227; raw −0.1% (95%: −0.3% to +0.2%); STEADY | 5.675 → 5.67; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | 5.741 → 5.737; raw −0.1% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 99th percentile (ms) | 5.27 | 5.27 | 5.272 → 5.269; raw −0.1% (95%: −0.7% to +0.5%); STEADY | 5.736 → 5.738; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 5.803 → 5.809; raw +0.1% (95%: ±0.0% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, mean (ms) | 0.891 | 0.817 | 0.8912 → 0.8166; raw −8.4% (95%: −10.0% to −6.7%), −0.0746 in the gauge's unit; GAIN | 1.023 → 0.979; raw −4.3% (95%: −5.1% to −3.5%); GAIN | 1.049 → 1.006; raw −4.1% (95%: −6.6% to −1.5%); GAIN | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.6 | 64 → 65.56; raw +2.4% (95%: +0.1% to +4.8%); power given | 64 → 63.83; raw −0.3% (95%: −3.2% to +2.6%); STEADY | 64 → 63.93; raw −0.1% (95%: −4.6% to +4.4%); STEADY | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 62.5 | 61.3 → 62.47; raw +1.9% (95%: +1.1% to +2.7%); power given | 61.3 → 60.6; raw −1.1% (95%: −3.1% to +0.8%); GAIN | 61.3 → 60.74; raw −0.9% (95%: −5.1% to +3.3%); GAIN | **the runs disagree** |
| keys evicted | 102,969 | 93,778 | 1.03e+05 → 9.378e+04; raw −8.9% (95%: −10.0% to −7.8%) | 1.034e+05 → 9.799e+04; raw −5.2% (95%: −6.3% to −4.1%) | 1.033e+05 → 9.797e+04; raw −5.2% (95%: −8.5% to −1.9%) | shown, not judged |
| host CPU busy (share of the run) | 0.0668 | 0.0733 | 0.06684 → 0.0733; raw +9.7% (95%: −13.7% to +33.1%), +0.0065 in the gauge's unit; power given | 0.1241 → 0.1329; raw +7.0% (95%: −7.1% to +21.2%), +0.0087 in the gauge's unit; power given | 0.114 → 0.1196; raw +4.9% (95%: −7.7% to +17.4%), +0.0055 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 117.8 | 130.2 | 117.8 → 130.2; raw +10.6% (95%: −14.3% to +35.4%); power given | 213.5 → 231.7; raw +8.5% (95%: −8.2% to +25.3%); power given | 190.3 → 200.9; raw +5.6% (95%: −8.7% to +19.9%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.207 | 0.225 | 0.2067 → 0.2249; raw +8.8% (95%: −15.6% to +33.1%), +0.0181 in the gauge's unit; power given | 0.3744 → 0.4025; raw +7.5% (95%: −8.9% to +23.9%), +0.0281 in the gauge's unit; power given | 0.3337 → 0.3488; raw +4.5% (95%: −9.2% to +18.2%), +0.0151 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 20.7 | 0 → 20.67; raw +20.6667 in the gauge's unit (95%: +16.8718 to +24.4616) | 0 → 24.33; raw +24.3333 in the gauge's unit (95%: +12.5928 to +36.0739) | 0 → 24.67; raw +24.6667 in the gauge's unit (95%: +16.6806 to +32.6527) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (12 trials, 0 allowed, 3 refused); left native (14 trials, 0 allowed, 3 refused); acting: 64 to 72 (14 trials, 1 allowed, 1 refused); run B: acting: 56 to 72 (14 trials, 2 allowed, 1 refused); acting: 56 to 72 (11 trials, 2 allowed, 3 refused); acting: 56 to 72 (15 trials, 2 allowed, 0 refused); run C: acting: 56 to 72 (11 trials, 2 allowed, 3 refused); acting: 48 to 72 (14 trials, 3 allowed, 2 refused); acting: 56 to 72 (12 trials, 2 allowed, 2 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.6 | 936.7 | 925.6 → 936.7; raw +1.2% (95%: +1.0% to +1.4%); GAIN | 925.2 → 937; raw +1.3% (95%: +1.2% to +1.3%); GAIN | 925.5 → 938; raw +1.3% (95%: +1.2% to +1.5%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | 0.6173 → 0.6251; raw +1.3% (95%: +1.0% to +1.6%), +0.0079 in the gauge's unit; GAIN | 0.6172 → 0.625; raw +1.3% (95%: +1.2% to +1.3%), +0.0078 in the gauge's unit; GAIN | 0.6172 → 0.6255; raw +1.3% (95%: +1.2% to +1.5%), +0.0083 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | 5.689 → 5.687; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | 5.503 → 5.505; raw ±0.0% (95%: −0.4% to +0.5%); STEADY | 5.68 → 5.678; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.74 | 5.81 | 5.742 → 5.809; raw +1.2% (95%: −3.6% to +6.0%); LOSS | 5.572 → 5.576; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 5.732 → 5.736; raw +0.1% (95%: −0.1% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.45%) |
| latency, mean (ms) | 2.26 | 2.23 | 2.263 → 2.226; raw −1.6% (95%: −2.6% to −0.7%); GAIN | 2.14 → 2.099; raw −1.9% (95%: −2.5% to −1.3%); GAIN | 2.258 → 2.214; raw −2.0% (95%: −2.3% to −1.6%); GAIN | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | 64 → 65.38; raw +2.2% (95%: +2.0% to +2.3%); power given | 64 → 65.38; raw +2.2% (95%: +1.8% to +2.5%); power given | 64 → 65.41; raw +2.2% (95%: +1.9% to +2.5%); power given | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | 60.7 → 61.87; raw +1.9% (95%: +1.4% to +2.4%); power given | 60.7 → 61.96; raw +2.1% (95%: +2.0% to +2.2%); power given | 60.7 → 61.8; raw +1.8% (95%: +1.3% to +2.3%); power given | **power given in all three of our runs** |
| keys evicted | 243,186 | 236,889 | 2.432e+05 → 2.369e+05; raw −2.6% (95%: −5.9% to +0.7%) | 2.432e+05 → 2.348e+05; raw −3.5% (95%: −3.6% to −3.3%) | 2.432e+05 → 2.387e+05; raw −1.8% (95%: −5.4% to +1.7%) | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.131 | 0.1447 → 0.1311; raw −9.4% (95%: −21.8% to +3.1%), −0.0136 in the gauge's unit; GAIN | 0.108 → 0.1098; raw +1.6% (95%: −37.2% to +40.4%), +0.0018 in the gauge's unit; power given | 0.133 → 0.1319; raw −0.8% (95%: −16.5% to +14.8%), −0.0011 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 242.9 | 217.2 | 242.9 → 217.2; raw −10.6% (95%: −25.3% to +4.2%); GAIN | 188.6 → 192.4; raw +2.0% (95%: −40.8% to +44.8%); power given | 221.4 → 219.5; raw −0.9% (95%: −19.2% to +17.5%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.583 | 0.515 | 0.5831 → 0.5153; raw −11.6% (95%: −26.1% to +2.8%), −0.0678 in the gauge's unit; GAIN | 0.453 → 0.4561; raw +0.7% (95%: −41.7% to +43.0%), +0.0031 in the gauge's unit; power given | 0.5315 → 0.5199; raw −2.2% (95%: −20.6% to +16.2%), −0.0117 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 13.7 | 0 → 13.67; raw +13.6667 in the gauge's unit (95%: +6.0769 to +21.2564) | 0 → 13.67; raw +13.6667 in the gauge's unit (95%: +6.0769 to +21.2564) | 0 → 15.33; raw +15.3333 in the gauge's unit (95%: +10.1618 to +20.5049) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 80 (12 trials, 3 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused); run C: acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 56 to 80 (13 trials, 3 allowed, 0 refused).

**Across 3 untouched workloads: 8 gauge-rows GAIN, 1 LOSS, 6 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
