# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39999416157 | `9678c8ad4325` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40020500663 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40035613178 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | 1182 → 1196; raw +1.2% (95%: +1.0% to +1.5%); GAIN | 1181 → 1195; raw +1.1% (95%: +0.8% to +1.4%); GAIN | 1184 → 1194; raw +0.8% (95%: +0.3% to +1.3%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.799 | 0.7893 → 0.7986; raw +1.2% (95%: +1.1% to +1.3%), +0.0093 in the gauge's unit; GAIN | 0.7892 → 0.7979; raw +1.1% (95%: +0.8% to +1.4%), +0.0088 in the gauge's unit; GAIN | 0.7894 → 0.796; raw +0.8% (95%: +0.3% to +1.3%), +0.0066 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.22 | 5.22 | 5.219 → 5.22; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | 5.229 → 5.227; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | 5.733 → 5.731; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.28 | 5.3 | 5.28 → 5.3; raw +0.4% (95%: −2.5% to +3.2%); STEADY | 5.324 → 5.32; raw −0.1% (95%: −0.8% to +0.6%); STEADY | 5.789 → 5.793; raw +0.1% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.13%) |
| latency, mean (ms) | 1.17 | 1.12 | 1.175 → 1.125; raw −4.3% (95%: −6.6% to −2.0%); GAIN | 1.182 → 1.137; raw −3.8% (95%: −5.0% to −2.7%); GAIN | 1.341 → 1.307; raw −2.5% (95%: −4.0% to −1.1%); GAIN | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.9 | 64 → 65.86; raw +2.9% (95%: +2.5% to +3.3%); power given | 64 → 65.59; raw +2.5% (95%: +1.8% to +3.1%); power given | 64 → 65.21; raw +1.9% (95%: +0.2% to +3.6%); power given | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.5 | 61.2 → 62.52; raw +2.2% (95%: +1.8% to +2.5%); power given | 61.19 → 62.35; raw +1.9% (95%: +1.6% to +2.2%); power given | 61.19 → 62.08; raw +1.4% (95%: +0.1% to +2.7%); power given | **power given in all three of our runs** |
| keys evicted | 138,185 | 132,746 | 1.382e+05 → 1.327e+05; raw −3.9% (95%: −4.4% to −3.5%) | 1.383e+05 → 1.332e+05; raw −3.7% (95%: −4.8% to −2.5%) | 1.381e+05 → 1.345e+05; raw −2.6% (95%: −4.6% to −0.6%) | shown, not judged |
| host CPU busy (share of the run) | 0.058 | 0.0692 | 0.05797 → 0.0692; raw +19.4% (95%: −112.9% to +151.6%), +0.0112 in the gauge's unit; power given | 0.06493 → 0.06789; raw +4.6% (95%: −56.5% to +65.6%), +0.0030 in the gauge's unit; power given | 0.121 → 0.1091; raw −9.8% (95%: −28.3% to +8.6%), −0.0119 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 102.1 | 123.0 | 102.1 → 123; raw +20.6% (95%: −120.3% to +161.5%); power given | 114.2 → 120.1; raw +5.1% (95%: −59.9% to +70.1%); power given | 202.5 → 180.3; raw −11.0% (95%: −32.2% to +10.2%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.192 | 0.229 | 0.1918 → 0.2285; raw +19.1% (95%: −121.0% to +159.3%), +0.0367 in the gauge's unit; power given | 0.2149 → 0.2234; raw +4.0% (95%: −60.5% to +68.4%), +0.0085 in the gauge's unit; power given | 0.3801 → 0.3356; raw −11.7% (95%: −32.5% to +9.1%), −0.0446 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 23.0 | 0 → 23; raw +23.0000 in the gauge's unit (95%: +23.0000 to +23.0000) | 0 → 21.67; raw +21.6667 in the gauge's unit (95%: +18.7980 to +24.5353) | 0 → 19.67; raw +19.6667 in the gauge's unit (95%: +12.0769 to +27.2564) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (15 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,074 | 1075 → 1074; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | 1075 → 1076; raw +0.1% (95%: ±0.0% to +0.2%); STEADY | 1076 → 1076; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | 0.7177 → 0.7173; raw −0.1% (95%: −0.3% to +0.2%), −0.0004 in the gauge's unit; STEADY | 0.7175 → 0.7177; raw ±0.0% (95%: −0.1% to +0.1%), +0.0002 in the gauge's unit; STEADY | 0.7176 → 0.7174; raw ±0.0% (95%: −0.1% to +0.1%), −0.0002 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 5.25 | 5.22 | 5.248 → 5.224; raw −0.5% (95%: −1.6% to +0.7%); STEADY | 5.223 → 5.224; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 5.748 → 5.748; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.15%) |
| latency, 99th percentile (ms) | 5.49 | 5.34 | 5.489 → 5.343; raw −2.7% (95%: −7.3% to +2.0%); GAIN | 5.336 → 5.31; raw −0.5% (95%: −4.4% to +3.4%); STEADY | 5.8 → 5.81; raw +0.2% (95%: +0.1% to +0.3%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 1.55 | 1.55 | 1.555 → 1.547; raw −0.5% (95%: −1.2% to +0.2%); GAIN | 1.545 → 1.538; raw −0.4% (95%: −1.6% to +0.8%); STEADY | 1.739 → 1.746; raw +0.4% (95%: −0.1% to +0.9%); STEADY | STEADY, under the floor (the three runs' mean 0.17%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.6 | 64 → 62.56; raw −2.2% (95%: −2.5% to −2.0%); GAIN | 64 → 62.52; raw −2.3% (95%: −2.6% to −2.1%); GAIN | 64 → 62.5; raw −2.3% (95%: −2.9% to −1.8%); GAIN | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 56.6 | 57.16 → 56.63; raw −0.9% (95%: −1.2% to −0.6%); GAIN | 57.15 → 56.58; raw −1.0% (95%: −1.3% to −0.7%); GAIN | 57.15 → 56.58; raw −1.0% (95%: −1.8% to −0.2%); GAIN | **GAIN in all three of our runs** |
| keys evicted | 71,719 | 71,808 | 7.172e+04 → 7.181e+04; raw +0.1% (95%: −0.5% to +0.7%) | 7.173e+04 → 7.17e+04; raw ±0.0% (95%: −0.4% to +0.3%) | 7.175e+04 → 7.181e+04; raw +0.1% (95%: −0.2% to +0.3%) | shown, not judged |
| host CPU busy (share of the run) | 0.0713 | 0.0494 | 0.07129 → 0.04942; raw −30.7% (95%: −102.7% to +41.3%), −0.0219 in the gauge's unit; GAIN | 0.06686 → 0.07516; raw +12.4% (95%: −120.8% to +145.6%), +0.0083 in the gauge's unit; power given | 0.1441 → 0.1321; raw −8.4% (95%: −40.7% to +24.0%), −0.0120 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 50.3 | 34.3 | 50.33 → 34.25; raw −31.9% (95%: −108.9% to +45.0%); GAIN | 47.56 → 53.52; raw +12.5% (95%: −130.0% to +155.0%); power given | 97.65 → 88.15; raw −9.7% (95%: −47.4% to +28.0%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.26 | 0.177 | 0.26 → 0.1771; raw −31.9% (95%: −108.8% to +45.1%), −0.0829 in the gauge's unit; GAIN | 0.2459 → 0.2764; raw +12.4% (95%: −129.8% to +154.7%), +0.0305 in the gauge's unit; power given | 0.504 → 0.4552; raw −9.7% (95%: −47.4% to +28.0%), −0.0489 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 6 | 0 → 6; raw +6.0000 in the gauge's unit (95%: +6.0000 to +6.0000) | 0 → 6; raw +6.0000 in the gauge's unit (95%: +6.0000 to +6.0000) | 0 → 6; raw +6.0000 in the gauge's unit (95%: +6.0000 to +6.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,280 | 1267 → 1280; raw +1.0% (95%: −0.5% to +2.5%); GAIN | 1267 → 1288; raw +1.7% (95%: +1.5% to +1.9%); GAIN | 1267 → 1287; raw +1.6% (95%: +1.4% to +1.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.854 | 0.8451 → 0.8537; raw +1.0% (95%: −0.5% to +2.5%), +0.0086 in the gauge's unit; GAIN | 0.8449 → 0.859; raw +1.7% (95%: +1.5% to +1.9%), +0.0141 in the gauge's unit; GAIN | 0.8449 → 0.8585; raw +1.6% (95%: +1.4% to +1.8%), +0.0136 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.74 | 5.73 | 5.736 → 5.733; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 5.623 → 5.591; raw −0.6% (95%: −1.2% to ±0.0%); GAIN | 5.495 → 5.485; raw −0.2% (95%: −0.9% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.27%) |
| latency, 99th percentile (ms) | 5.8 | 5.8 | 5.798 → 5.802; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 5.732 → 5.72; raw −0.2% (95%: −0.7% to +0.2%); STEADY | 5.602 → 5.602; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 1.05 | 1 | 1.047 → 1.003; raw −4.2% (95%: −10.7% to +2.2%); GAIN | 0.9813 → 0.8981; raw −8.5% (95%: −9.5% to −7.4%), −0.0832 in the gauge's unit; GAIN | 0.9555 → 0.8838; raw −7.5% (95%: −9.0% to −6.0%), −0.0716 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.0 | 64 → 64.02; raw ±0.0% (95%: −1.8% to +1.9%); STEADY | 64 → 64.99; raw +1.5% (95%: +0.9% to +2.2%); power given | 64 → 64.7; raw +1.1% (95%: −0.3% to +2.5%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 61.1 | 61.3 → 61.14; raw −0.3% (95%: −2.1% to +1.6%); STEADY | 61.3 → 61.96; raw +1.1% (95%: +0.4% to +1.8%); power given | 61.3 → 61.69; raw +0.6% (95%: ±0.0% to +1.3%); power given | STEADY, under the floor (the three runs' mean 0.49%) |
| keys evicted | 103,288 | 97,706 | 1.033e+05 → 9.771e+04; raw −5.4% (95%: −13.7% to +2.9%) | 1.034e+05 → 9.411e+04; raw −9.0% (95%: −10.1% to −7.9%) | 1.034e+05 → 9.45e+04; raw −8.6% (95%: −9.8% to −7.5%) | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.112 | 0.1087 → 0.1119; raw +2.9% (95%: −29.5% to +35.3%), +0.0032 in the gauge's unit; power given | 0.1034 → 0.105; raw +1.5% (95%: −59.3% to +62.3%), +0.0015 in the gauge's unit; power given | 0.101 → 0.09462; raw −6.3% (95%: −40.7% to +28.1%), −0.0063 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 180.7 | 186.6 | 180.7 → 186.6; raw +3.3% (95%: −33.0% to +39.5%); power given | 181.9 → 186.3; raw +2.5% (95%: −65.7% to +70.6%); power given | 177.3 → 165.6; raw −6.6% (95%: −44.2% to +31.0%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.317 | 0.324 | 0.3168 → 0.3241; raw +2.3% (95%: −34.8% to +39.4%), +0.0073 in the gauge's unit; power given | 0.319 → 0.3214; raw +0.8% (95%: −66.8% to +68.3%), +0.0024 in the gauge's unit; power given | 0.3109 → 0.2858; raw −8.1% (95%: −45.1% to +29.0%), −0.0251 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 20.3 | 0 → 20.33; raw +20.3333 in the gauge's unit (95%: +14.5960 to +26.0707) | 0 → 21.67; raw +21.6667 in the gauge's unit (95%: +18.7980 to +24.5353) | 0 → 23; raw +23.0000 in the gauge's unit (95%: +23.0000 to +23.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (11 trials, 0 allowed, 2 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused); run B: acting: 56 to 64 (13 trials, 1 allowed, 2 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); left native (12 trials, 0 allowed, 1 refused); run C: left native (12 trials, 0 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); left native (12 trials, 0 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.5 | 935.8 | 925.5 → 935.8; raw +1.1% (95%: +0.5% to +1.8%); GAIN | 926.1 → 937; raw +1.2% (95%: +1.0% to +1.3%); GAIN | 925.8 → 937.4; raw +1.3% (95%: +1.1% to +1.4%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | 0.6173 → 0.6253; raw +1.3% (95%: +1.2% to +1.4%), +0.0080 in the gauge's unit; GAIN | 0.6176 → 0.6249; raw +1.2% (95%: +1.0% to +1.3%), +0.0073 in the gauge's unit; GAIN | 0.6173 → 0.6251; raw +1.3% (95%: +1.1% to +1.4%), +0.0078 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.69 | 5.95 | 5.692 → 5.95; raw +4.5% (95%: −15.1% to +24.2%); LOSS | 5.642 → 5.646; raw +0.1% (95%: ±0.0% to +0.1%); STEADY | 5.536 → 5.55; raw +0.3% (95%: −1.2% to +1.7%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 5.75 | 6.66 | 5.745 → 6.662; raw +16.0% (95%: −52.2% to +84.1%); LOSS | 5.707 → 5.719; raw +0.2% (95%: +0.1% to +0.4%); STEADY | 5.625 → 5.64; raw +0.3% (95%: −0.7% to +1.2%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 2.26 | 2.28 | 2.265 → 2.279; raw +0.6% (95%: −10.1% to +11.4%); LOSS | 2.215 → 2.179; raw −1.6% (95%: −1.9% to −1.3%); GAIN | 2.118 → 2.084; raw −1.6% (95%: −3.1% to −0.1%); GAIN | **the runs disagree** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | 64 → 65.41; raw +2.2% (95%: +2.1% to +2.3%); power given | 64 → 65.41; raw +2.2% (95%: +2.1% to +2.4%); power given | 64 → 65.54; raw +2.4% (95%: +2.2% to +2.7%); power given | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | 60.7 → 61.86; raw +1.9% (95%: +1.4% to +2.4%); power given | 60.7 → 61.94; raw +2.0% (95%: +2.0% to +2.1%); power given | 60.7 → 62; raw +2.1% (95%: +2.1% to +2.2%); power given | **power given in all three of our runs** |
| keys evicted | 243,204 | 236,799 | 2.432e+05 → 2.368e+05; raw −2.6% (95%: −6.3% to +1.0%) | 2.43e+05 → 2.349e+05; raw −3.3% (95%: −3.6% to −3.1%) | 2.432e+05 → 2.348e+05; raw −3.4% (95%: −3.7% to −3.2%) | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.141 | 0.1399 → 0.1406; raw +0.5% (95%: −57.0% to +58.0%), +0.0007 in the gauge's unit; STEADY | 0.1436 → 0.1402; raw −2.4% (95%: −19.4% to +14.6%), −0.0034 in the gauge's unit; GAIN | 0.1082 → 0.1002; raw −7.4% (95%: −24.9% to +10.1%), −0.0080 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 233.7 | 233.0 | 233.7 → 233; raw −0.3% (95%: −63.4% to +62.8%); STEADY | 249.8 → 242.6; raw −2.9% (95%: −22.6% to +16.9%); GAIN | 193.7 → 177.3; raw −8.5% (95%: −28.7% to +11.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.561 | 0.553 | 0.5611 → 0.5532; raw −1.4% (95%: −64.6% to +61.7%), −0.0079 in the gauge's unit; GAIN | 0.5993 → 0.5752; raw −4.0% (95%: −23.7% to +15.7%), −0.0241 in the gauge's unit; GAIN | 0.4649 → 0.4202; raw −9.6% (95%: −29.8% to +10.6%), −0.0446 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 14.0 | 0 → 14; raw +14.0000 in the gauge's unit (95%: +9.6970 to +18.3030) | 0 → 12.33; raw +12.3333 in the gauge's unit (95%: +9.4647 to +15.2020) | 0 → 13.67; raw +13.6667 in the gauge's unit (95%: +10.7980 to +16.5353) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 2 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 STEADY, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
