# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40005899721 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40022515018 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40037204297 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | 1184 → 1195; raw +1.0% (95%: +0.4% to +1.5%); GAIN | 1184 → 1193; raw +0.8% (95%: +0.3% to +1.3%); GAIN | 1184 → 1193; raw +0.8% (95%: +0.3% to +1.2%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.797 | 0.7894 → 0.797; raw +1.0% (95%: +0.4% to +1.6%), +0.0076 in the gauge's unit; GAIN | 0.7893 → 0.7957; raw +0.8% (95%: +0.3% to +1.3%), +0.0063 in the gauge's unit; GAIN | 0.7895 → 0.7957; raw +0.8% (95%: +0.3% to +1.2%), +0.0063 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.73 | 5.74 | 5.734 → 5.735; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 5.754 → 5.755; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 5.736 → 5.736; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.79 | 5.79 | 5.789 → 5.795; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 5.817 → 5.826; raw +0.1% (95%: −0.2% to +0.5%); STEADY | 5.789 → 5.796; raw +0.1% (95%: −0.1% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, mean (ms) | 1.34 | 1.3 | 1.343 → 1.305; raw −2.8% (95%: −4.9% to −0.8%); GAIN | 1.349 → 1.317; raw −2.4% (95%: −4.5% to −0.3%); GAIN | 1.34 → 1.309; raw −2.3% (95%: −4.1% to −0.6%); GAIN | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.3 | 64 → 65.33; raw +2.1% (95%: +0.3% to +3.8%); power given | 64 → 64.78; raw +1.2% (95%: ±0.0% to +2.5%); power given | 64 → 65.2; raw +1.9% (95%: +1.0% to +2.7%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 61.2 | 62.2 | 61.19 → 62.2; raw +1.6% (95%: +0.1% to +3.2%); power given | 61.19 → 61.74; raw +0.9% (95%: +0.4% to +1.4%); power given | 61.19 → 62.02; raw +1.3% (95%: +0.6% to +2.1%); power given | **power given in all three of our runs** |
| keys evicted | 138,139 | 133,815 | 1.381e+05 → 1.338e+05; raw −3.1% (95%: −5.5% to −0.8%) | 1.382e+05 → 1.353e+05; raw −2.1% (95%: −3.3% to −0.9%) | 1.381e+05 → 1.349e+05; raw −2.3% (95%: −3.2% to −1.4%) | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.129 | 0.1143 → 0.1288; raw +12.7% (95%: −16.8% to +42.1%), +0.0145 in the gauge's unit; power given | 0.1061 → 0.1272; raw +19.8% (95%: +1.0% to +38.7%), +0.0210 in the gauge's unit; power given | 0.1191 → 0.1251; raw +5.1% (95%: −15.4% to +25.6%), +0.0060 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 189.9 | 218.0 | 189.9 → 218; raw +14.8% (95%: −19.1% to +48.8%); power given | 174.1 → 213.4; raw +22.6% (95%: +3.2% to +42.0%); power given | 199.3 → 211.1; raw +5.9% (95%: −17.7% to +29.5%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.405 | 0.3563 → 0.4054; raw +13.8% (95%: −20.4% to +47.9%), +0.0490 in the gauge's unit; power given | 0.3268 → 0.3974; raw +21.6% (95%: +1.6% to +41.6%), +0.0706 in the gauge's unit; power given | 0.3741 → 0.3931; raw +5.1% (95%: −18.6% to +28.8%), +0.0190 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| ceiling changes written (the knob's moves) | 0 | 19.7 | 0 → 19.67; raw +19.6667 in the gauge's unit (95%: +12.0769 to +27.2564) | 0 → 21.67; raw +21.6667 in the gauge's unit (95%: +10.4642 to +32.8692) | 0 → 19.33; raw +19.3333 in the gauge's unit (95%: +8.1308 to +30.5358) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused); run B: acting: 56 to 72 (13 trials, 2 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 56 to 72 (13 trials, 2 allowed, 0 refused); run C: acting: 56 to 72 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | 1076 → 1075; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | 1076 → 1075; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | 1077 → 1076; raw −0.1% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.09%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | 0.7176 → 0.7172; raw −0.1% (95%: −0.2% to +0.1%), −0.0004 in the gauge's unit; STEADY | 0.7177 → 0.7172; raw −0.1% (95%: −0.2% to ±0.0%), −0.0005 in the gauge's unit; STEADY | 0.718 → 0.7174; raw −0.1% (95%: −0.2% to +0.1%), −0.0006 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 95th percentile (ms) | 5.74 | 5.74 | 5.743 → 5.739; raw −0.1% (95%: −0.3% to +0.2%); STEADY | 5.784 → 5.785; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 5.741 → 5.743; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 99th percentile (ms) | 5.8 | 5.8 | 5.796 → 5.8; raw +0.1% (95%: −0.3% to +0.4%); STEADY | 5.847 → 5.865; raw +0.3% (95%: +0.3% to +0.4%); STEADY | 5.796 → 5.805; raw +0.2% (95%: ±0.0% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.18%) |
| latency, mean (ms) | 1.74 | 1.74 | 1.736 → 1.744; raw +0.5% (95%: −0.3% to +1.3%); STEADY | 1.761 → 1.771; raw +0.6% (95%: −0.3% to +1.4%); LOSS | 1.734 → 1.743; raw +0.5% (95%: −0.1% to +1.1%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 61.9 | 64 → 61.94; raw −3.2% (95%: −6.7% to +0.3%); GAIN | 64 → 61.41; raw −4.1% (95%: −7.4% to −0.7%); GAIN | 64 → 62.92; raw −1.7% (95%: −3.5% to +0.1%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 57.2 | 56.0 | 57.16 → 56.05; raw −1.9% (95%: −6.0% to +2.1%); GAIN | 57.16 → 55.46; raw −3.0% (95%: −6.9% to +0.9%); GAIN | 57.15 → 56.6; raw −1.0% (95%: −1.6% to −0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 71,747 | 71,875 | 7.175e+04 → 7.188e+04; raw +0.2% (95%: −0.1% to +0.5%) | 7.174e+04 → 7.19e+04; raw +0.2% (95%: ±0.0% to +0.4%) | 7.163e+04 → 7.181e+04; raw +0.2% (95%: −0.2% to +0.7%) | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.135 | 0.1396 → 0.1353; raw −3.0% (95%: −38.3% to +32.3%), −0.0042 in the gauge's unit; GAIN | 0.1318 → 0.1516; raw +15.0% (95%: −1.8% to +31.9%), +0.0198 in the gauge's unit; power given | 0.1388 → 0.1415; raw +2.0% (95%: −38.2% to +42.2%), +0.0027 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 94.4 | 90.8 | 94.44 → 90.8; raw −3.8% (95%: −44.3% to +36.6%); GAIN | 86.45 → 101.6; raw +17.5% (95%: −1.9% to +36.9%); power given | 94.06 → 95.8; raw +1.9% (95%: −45.1% to +48.8%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.488 | 0.469 | 0.4875 → 0.469; raw −3.8% (95%: −44.4% to +36.8%), −0.0185 in the gauge's unit; GAIN | 0.4462 → 0.5246; raw +17.6% (95%: −1.8% to +37.0%), +0.0785 in the gauge's unit; power given | 0.4851 → 0.4946; raw +2.0% (95%: −44.9% to +48.8%), +0.0095 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 7.33 | 0 → 7.333; raw +7.3333 in the gauge's unit (95%: +1.5960 to +13.0707) | 0 → 8; raw +8.0000 in the gauge's unit (95%: +3.0313 to +12.9687) | 0 → 6; raw +6.0000 in the gauge's unit (95%: +6.0000 to +6.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | 1267 → 1288; raw +1.6% (95%: +1.3% to +2.0%); GAIN | 1264 → 1283; raw +1.5% (95%: +1.1% to +2.0%); GAIN | 1262 → 1282; raw +1.6% (95%: +0.7% to +2.4%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.859 | 0.8452 → 0.8592; raw +1.7% (95%: +1.3% to +2.0%), +0.0140 in the gauge's unit; GAIN | 0.845 → 0.8574; raw +1.5% (95%: +0.9% to +2.0%), +0.0124 in the gauge's unit; GAIN | 0.8442 → 0.8576; raw +1.6% (95%: +0.7% to +2.5%), +0.0134 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.5 | 5.48 | 5.496 → 5.484; raw −0.2% (95%: −0.6% to +0.2%); STEADY | 5.218 → 5.221; raw +0.1% (95%: −0.3% to +0.5%); STEADY | 5.231 → 5.218; raw −0.3% (95%: −0.9% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.14%) |
| latency, 99th percentile (ms) | 5.6 | 5.6 | 5.599 → 5.601; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 5.265 → 5.334; raw +1.3% (95%: −3.0% to +5.6%); LOSS | 5.288 → 5.251; raw −0.7% (95%: −2.8% to +1.4%); GAIN | **the runs disagree** |
| latency, mean (ms) | 0.956 | 0.883 | 0.9564 → 0.8834; raw −7.6% (95%: −10.1% to −5.2%), −0.0730 in the gauge's unit; GAIN | 0.8974 → 0.8333; raw −7.2% (95%: −9.2% to −5.1%), −0.0642 in the gauge's unit; GAIN | 0.9053 → 0.8307; raw −8.2% (95%: −11.0% to −5.5%), −0.0746 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | 64 → 65.42; raw +2.2% (95%: +1.4% to +3.0%); power given | 64 → 65.96; raw +3.1% (95%: +1.9% to +4.2%); power given | 64 → 66.04; raw +3.2% (95%: −2.2% to +8.6%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 61.3 | 62.4 | 61.29 → 62.4; raw +1.8% (95%: +1.7% to +1.9%); power given | 61.3 → 62.49; raw +2.0% (95%: +1.4% to +2.5%); power given | 61.29 → 62.47; raw +1.9% (95%: −1.2% to +5.1%); power given | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 103,241 | 93,999 | 1.032e+05 → 9.4e+04; raw −9.0% (95%: −10.7% to −7.2%) | 1.034e+05 → 9.503e+04; raw −8.1% (95%: −10.7% to −5.4%) | 1.039e+05 → 9.492e+04; raw −8.6% (95%: −13.8% to −3.5%) | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.103 | 0.1094 → 0.1029; raw −5.9% (95%: −76.7% to +64.9%), −0.0065 in the gauge's unit; GAIN | 0.07502 → 0.05104; raw −32.0% (95%: −111.4% to +47.5%), −0.0240 in the gauge's unit; GAIN | 0.06749 → 0.06203; raw −8.1% (95%: −50.0% to +33.8%), −0.0055 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 194.5 | 181.3 | 194.5 → 181.3; raw −6.8% (95%: −84.9% to +71.4%); GAIN | 134.5 → 88.86; raw −33.9% (95%: −118.0% to +50.1%); GAIN | 119.4 → 109.5; raw −8.3% (95%: −52.4% to +35.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.341 | 0.313 | 0.3411 → 0.3128; raw −8.3% (95%: −85.9% to +69.4%), −0.0282 in the gauge's unit; GAIN | 0.2365 → 0.1539; raw −34.9% (95%: −118.4% to +48.6%), −0.0826 in the gauge's unit; GAIN | 0.2102 → 0.1898; raw −9.7% (95%: −52.8% to +33.4%), −0.0204 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 19.7 | 0 → 19.67; raw +19.6667 in the gauge's unit (95%: +16.7980 to +22.5353) | 0 → 19; raw +19.0000 in the gauge's unit (95%: +14.6970 to +23.3030) | 0 → 21; raw +21.0000 in the gauge's unit (95%: +16.6970 to +25.3030) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 72 (12 trials, 2 allowed, 2 refused); acting: 56 to 72 (12 trials, 2 allowed, 2 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); run B: left native (14 trials, 0 allowed, 3 refused); acting: 64 to 72 (14 trials, 1 allowed, 2 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); run C: left native (12 trials, 0 allowed, 3 refused); acting: 64 to 72 (14 trials, 1 allowed, 2 refused); acting: 64 to 72 (14 trials, 1 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.2 | 937.1 | 925.2 → 937.1; raw +1.3% (95%: +1.1% to +1.4%); GAIN | 925.8 → 937.3; raw +1.2% (95%: +0.9% to +1.6%); GAIN | 925.8 → 937.5; raw +1.3% (95%: +1.0% to +1.5%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | 0.6171 → 0.6251; raw +1.3% (95%: +1.1% to +1.4%), +0.0080 in the gauge's unit; GAIN | 0.6174 → 0.6251; raw +1.2% (95%: +1.0% to +1.5%), +0.0077 in the gauge's unit; GAIN | 0.6174 → 0.6252; raw +1.3% (95%: +1.0% to +1.5%), +0.0078 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.5 | 5.5 | 5.498 → 5.5; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | 5.602 → 5.603; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | 5.528 → 5.527; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.57 | 5.58 | 5.571 → 5.575; raw +0.1% (95%: +0.1% to +0.1%); STEADY | 5.674 → 5.681; raw +0.1% (95%: ±0.0% to +0.3%); STEADY | 5.586 → 5.587; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| latency, mean (ms) | 2.14 | 2.1 | 2.136 → 2.096; raw −1.9% (95%: −2.2% to −1.6%); GAIN | 2.19 → 2.15; raw −1.8% (95%: −2.2% to −1.4%); GAIN | 2.148 → 2.106; raw −1.9% (95%: −2.2% to −1.7%); GAIN | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.6 | 64 → 65.59; raw +2.5% (95%: +0.7% to +4.3%); power given | 64 → 65.69; raw +2.6% (95%: +0.5% to +4.8%); power given | 64 → 65.59; raw +2.5% (95%: ±0.0% to +5.0%); power given | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | 60.7 → 61.86; raw +1.9% (95%: +1.1% to +2.7%); power given | 60.7 → 61.92; raw +2.0% (95%: +1.8% to +2.2%); power given | 60.7 → 61.94; raw +2.0% (95%: +1.9% to +2.2%); power given | **power given in all three of our runs** |
| keys evicted | 243,285 | 236,617 | 2.433e+05 → 2.366e+05; raw −2.7% (95%: −5.9% to +0.4%) | 2.431e+05 → 2.356e+05; raw −3.1% (95%: −4.0% to −2.2%) | 2.431e+05 → 2.355e+05; raw −3.1% (95%: −4.1% to −2.1%) | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.0997 | 0.1043 → 0.09966; raw −4.4% (95%: −27.6% to +18.7%), −0.0046 in the gauge's unit; GAIN | 0.1222 → 0.1232; raw +0.9% (95%: −24.0% to +25.8%), +0.0011 in the gauge's unit; power given | 0.1083 → 0.114; raw +5.3% (95%: −16.3% to +26.8%), +0.0057 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 181.8 | 172.9 | 181.8 → 172.9; raw −4.9% (95%: −30.5% to +20.7%); GAIN | 215.3 → 217.4; raw +1.0% (95%: −27.3% to +29.3%); power given | 188.5 → 199.9; raw +6.0% (95%: −17.4% to +29.5%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.437 | 0.41 | 0.4367 → 0.41; raw −6.1% (95%: −31.4% to +19.1%), −0.0267 in the gauge's unit; GAIN | 0.5166 → 0.5152; raw −0.3% (95%: −28.3% to +27.7%), −0.0014 in the gauge's unit; STEADY | 0.4524 → 0.4737; raw +4.7% (95%: −18.5% to +27.9%), +0.0213 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 15.0 | 0 → 15; raw +15.0000 in the gauge's unit (95%: +1.8541 to +28.1459) | 0 → 14.33; raw +14.3333 in the gauge's unit (95%: +3.9902 to +24.6765) | 0 → 15; raw +15.0000 in the gauge's unit (95%: +10.0313 to +19.9687) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 72 (11 trials, 2 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 56 to 80 (14 trials, 3 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 80 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run C: acting: 56 to 72 (11 trials, 2 allowed, 0 refused); acting: 64 to 80 (13 trials, 2 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 1 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 STEADY, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
