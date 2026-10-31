# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39109167603 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| B | 39116289213 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| C | 39124638850 | `8b902df8d857` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,195 | 1182 → 1195; raw +1.1% (95%: +0.5% to +1.6%); GAIN | 1184 → 1197; raw +1.1% (95%: +0.8% to +1.3%); GAIN | 1182 → 1195; raw +1.1% (95%: +0.9% to +1.3%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.798 | 0.7893 → 0.7976; raw +1.1% (95%: +0.5% to +1.6%), +0.0083 in the gauge's unit; GAIN | 0.7896 → 0.7982; raw +1.1% (95%: +0.8% to +1.4%), +0.0086 in the gauge's unit; GAIN | 0.7893 → 0.7977; raw +1.1% (95%: +0.8% to +1.3%), +0.0084 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.21 | 5.21 | 5.212 → 5.212; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | 5.531 → 5.519; raw −0.2% (95%: −0.5% to +0.1%); STEADY | 5.213 → 5.216; raw +0.1% (95%: −0.2% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 99th percentile (ms) | 5.25 | 5.25 | 5.254 → 5.252; raw ±0.0% (95%: −0.8% to +0.7%); STEADY | 5.603 → 5.598; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | 5.258 → 5.264; raw +0.1% (95%: ±0.0% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, mean (ms) | 1.17 | 1.12 | 1.17 → 1.121; raw −4.2% (95%: −6.1% to −2.2%); GAIN | 1.238 → 1.19; raw −3.9% (95%: −5.2% to −2.6%); GAIN | 1.171 → 1.128; raw −3.7% (95%: −4.4% to −3.0%); GAIN | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.5 | 64 → 65.52; raw +2.4% (95%: +1.6% to +3.2%); power given | 64 → 65.62; raw +2.5% (95%: +1.4% to +3.7%); power given | 64 → 65.61; raw +2.5% (95%: +0.5% to +4.6%); power given | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.3 | 61.19 → 62.25; raw +1.7% (95%: +1.1% to +2.4%); power given | 61.19 → 62.29; raw +1.8% (95%: +0.5% to +3.0%); power given | 61.19 → 62.34; raw +1.9% (95%: +0.4% to +3.4%); power given | **power given in all three of our runs** |
| keys evicted | 138,229 | 133,460 | 1.382e+05 → 1.335e+05; raw −3.5% (95%: −5.6% to −1.3%) | 1.38e+05 → 1.336e+05; raw −3.2% (95%: −5.0% to −1.4%) | 1.382e+05 → 1.334e+05; raw −3.5% (95%: −4.5% to −2.5%) | shown, not judged |
| host CPU busy (share of the run) | 0.0676 | 0.0636 | 0.06761 → 0.06361; raw −5.9% (95%: −90.4% to +78.5%), −0.0040 in the gauge's unit; GAIN | 0.09919 → 0.1082; raw +9.1% (95%: −9.0% to +27.1%), +0.0090 in the gauge's unit; power given | 0.0695 → 0.06137; raw −11.7% (95%: −69.6% to +46.3%), −0.0081 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 120.7 | 112.7 | 120.7 → 112.7; raw −6.6% (95%: −96.5% to +83.3%); GAIN | 173.8 → 191.7; raw +10.3% (95%: −9.6% to +30.2%); power given | 123.9 → 108.3; raw −12.6% (95%: −74.2% to +49.0%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.227 | 0.21 | 0.2268 → 0.2096; raw −7.6% (95%: −97.0% to +81.8%), −0.0172 in the gauge's unit; GAIN | 0.3262 → 0.3558; raw +9.1% (95%: −10.6% to +28.8%), +0.0297 in the gauge's unit; power given | 0.233 → 0.2014; raw −13.5% (95%: −74.9% to +47.8%), −0.0315 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.0 | 0 → 21; raw +21.0000 in the gauge's unit (95%: +16.0313 to +25.9687) | 0 → 24; raw +24.0000 in the gauge's unit (95%: +21.5157 to +26.4843) | 0 → 21; raw +21.0000 in the gauge's unit (95%: +21.0000 to +21.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); left native (12 trials, 0 allowed, 1 refused); run B: acting: 56 to 72 (15 trials, 2 allowed, 0 refused); acting: 56 to 72 (12 trials, 2 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (15 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 1 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | 1076 → 1076; raw −0.1% (95%: −0.2% to +0.1%); STEADY | 1075 → 1075; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1077 → 1075; raw −0.1% (95%: −0.4% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | 0.7178 → 0.7175; raw ±0.0% (95%: −0.2% to +0.1%), −0.0003 in the gauge's unit; STEADY | 0.7176 → 0.7175; raw ±0.0% (95%: −0.1% to +0.1%), −0.0001 in the gauge's unit; STEADY | 0.7179 → 0.7172; raw −0.1% (95%: −0.4% to +0.2%), −0.0007 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 5.75 | 5.75 | 5.746 → 5.751; raw +0.1% (95%: −0.3% to +0.5%); STEADY | 5.215 → 5.217; raw ±0.0% (95%: −0.5% to +0.6%); STEADY | 5.576 → 5.597; raw +0.4% (95%: −1.1% to +1.9%); STEADY | STEADY, under the floor (the three runs' mean 0.17%) |
| latency, 99th percentile (ms) | 5.8 | 5.82 | 5.805 → 5.824; raw +0.3% (95%: −0.7% to +1.3%); STEADY | 5.262 → 5.27; raw +0.1% (95%: −1.1% to +1.4%); STEADY | 5.634 → 5.673; raw +0.7% (95%: −1.6% to +3.0%); LOSS | STEADY, under the floor (the three runs' mean 0.39%) |
| latency, mean (ms) | 1.74 | 1.75 | 1.741 → 1.752; raw +0.6% (95%: −0.3% to +1.5%); LOSS | 1.536 → 1.535; raw ±0.0% (95%: −0.5% to +0.4%); STEADY | 1.632 → 1.648; raw +0.9% (95%: −2.8% to +4.7%); LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.2 | 64 → 62.16; raw −2.9% (95%: −7.9% to +2.2%); GAIN | 64 → 62.58; raw −2.2% (95%: −3.2% to −1.3%); GAIN | 64 → 62.55; raw −2.3% (95%: −2.6% to −1.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 57.2 | 56.0 | 57.16 → 56.03; raw −2.0% (95%: −6.8% to +2.9%); GAIN | 57.15 → 56.68; raw −0.8% (95%: −2.1% to +0.5%); GAIN | 57.15 → 56.65; raw −0.9% (95%: −1.4% to −0.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 71,703 | 71,795 | 7.17e+04 → 7.18e+04; raw +0.1% (95%: −0.3% to +0.6%) | 7.171e+04 → 7.176e+04; raw +0.1% (95%: −0.3% to +0.4%) | 7.165e+04 → 7.184e+04; raw +0.3% (95%: −0.5% to +1.1%) | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.132 | 0.1313 → 0.1318; raw +0.4% (95%: −14.4% to +15.2%), +0.0005 in the gauge's unit; STEADY | 0.05367 → 0.05378; raw +0.2% (95%: −95.5% to +95.9%), +0.0001 in the gauge's unit; STEADY | 0.1213 → 0.1162; raw −4.2% (95%: −17.9% to +9.4%), −0.0051 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 87.6 | 87.8 | 87.56 → 87.75; raw +0.2% (95%: −16.4% to +16.9%); STEADY | 37.51 → 37.76; raw +0.7% (95%: −101.8% to +103.1%); power given | 86.19 → 81.51; raw −5.4% (95%: −20.9% to +10.0%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.452 | 0.453 | 0.4519 → 0.4531; raw +0.3% (95%: −16.2% to +16.8%), +0.0012 in the gauge's unit; STEADY | 0.1939 → 0.1952; raw +0.7% (95%: −101.7% to +103.1%), +0.0013 in the gauge's unit; power given | 0.4448 → 0.4211; raw −5.3% (95%: −20.9% to +10.2%), −0.0238 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 7.33 | 0 → 7.333; raw +7.3333 in the gauge's unit (95%: +1.5960 to +13.0707) | 0 → 5.333; raw +5.3333 in the gauge's unit (95%: +2.4647 to +8.2020) | 0 → 6; raw +6.0000 in the gauge's unit (95%: +6.0000 to +6.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 1 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,289 | 1268 → 1289; raw +1.7% (95%: +1.5% to +1.9%); GAIN | 1267 → 1288; raw +1.7% (95%: +1.6% to +1.8%); GAIN | 1267 → 1283; raw +1.3% (95%: +0.5% to +2.1%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.86 | 0.8453 → 0.8596; raw +1.7% (95%: +1.5% to +1.9%), +0.0143 in the gauge's unit; GAIN | 0.8448 → 0.8591; raw +1.7% (95%: +1.6% to +1.8%), +0.0143 in the gauge's unit; GAIN | 0.8446 → 0.8557; raw +1.3% (95%: +0.5% to +2.1%), +0.0111 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.49 | 5.5 | 5.485 → 5.5; raw +0.3% (95%: −0.9% to +1.4%); STEADY | 5.506 → 5.499; raw −0.1% (95%: −0.6% to +0.3%); STEADY | 5.746 → 5.743; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 99th percentile (ms) | 5.65 | 5.67 | 5.655 → 5.669; raw +0.2% (95%: −0.4% to +0.9%); STEADY | 5.611 → 5.611; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 5.809 → 5.815; raw +0.1% (95%: −0.1% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, mean (ms) | 0.941 | 0.871 | 0.9406 → 0.8709; raw −7.4% (95%: −8.0% to −6.8%), −0.0698 in the gauge's unit; GAIN | 0.9598 → 0.8845; raw −7.8% (95%: −8.4% to −7.3%), −0.0753 in the gauge's unit; GAIN | 1.053 → 0.9965; raw −5.4% (95%: −8.2% to −2.5%); GAIN | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | 64 → 65.4; raw +2.2% (95%: +1.7% to +2.7%); power given | 64 → 65.71; raw +2.7% (95%: ±0.0% to +5.4%); power given | 64 → 63.64; raw −0.6% (95%: −7.4% to +6.2%); GAIN | **the runs disagree** |
| memory used, mean (MB) | 61.3 | 62.4 | 61.3 → 62.41; raw +1.8% (95%: +1.6% to +2.0%); power given | 61.3 → 62.45; raw +1.9% (95%: ±0.0% to +3.8%); power given | 61.3 → 60.51; raw −1.3% (95%: −8.2% to +5.6%); GAIN | **the runs disagree** |
| keys evicted | 103,173 | 93,754 | 1.032e+05 → 9.375e+04; raw −9.1% (95%: −10.0% to −8.2%) | 1.035e+05 → 9.395e+04; raw −9.2% (95%: −9.6% to −8.9%) | 1.036e+05 → 9.656e+04; raw −6.8% (95%: −11.7% to −1.9%) | shown, not judged |
| host CPU busy (share of the run) | 0.0904 | 0.0806 | 0.09042 → 0.08065; raw −10.8% (95%: −70.9% to +49.3%), −0.0098 in the gauge's unit; GAIN | 0.1047 → 0.09472; raw −9.5% (95%: −71.5% to +52.4%), −0.0100 in the gauge's unit; GAIN | 0.1066 → 0.1167; raw +9.5% (95%: −25.9% to +44.9%), +0.0101 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 159.9 | 141.8 | 159.9 → 141.8; raw −11.3% (95%: −76.0% to +53.3%); GAIN | 185 → 165.5; raw −10.5% (95%: −78.6% to +57.5%); GAIN | 175.6 → 194.9; raw +11.0% (95%: −29.0% to +51.0%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.244 | 0.2803 → 0.2444; raw −12.8% (95%: −76.1% to +50.5%), −0.0359 in the gauge's unit; GAIN | 0.3244 → 0.2855; raw −12.0% (95%: −79.4% to +55.4%), −0.0389 in the gauge's unit; GAIN | 0.3081 → 0.3374; raw +9.5% (95%: −29.1% to +48.2%), +0.0294 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 19.3 | 0 → 19.33; raw +19.3333 in the gauge's unit (95%: +17.8990 to +20.7677) | 0 → 20.67; raw +20.6667 in the gauge's unit (95%: +15.4951 to +25.8382) | 0 → 28.33; raw +28.3333 in the gauge's unit (95%: +12.5557 to +44.1110) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (11 trials, 1 allowed, 3 refused); acting: 64 to 72 (10 trials, 1 allowed, 3 refused); acting: 64 to 72 (12 trials, 1 allowed, 2 refused); run B: acting: 56 to 72 (12 trials, 2 allowed, 2 refused); acting: 64 to 72 (12 trials, 1 allowed, 2 refused); acting: 56 to 72 (14 trials, 2 allowed, 1 refused); run C: acting: 48 to 64 (16 trials, 2 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); acting: 48 to 64 (16 trials, 2 allowed, 2 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.8 | 937.3 | 925.8 → 937.3; raw +1.2% (95%: +1.1% to +1.4%); GAIN | 924 → 935.6; raw +1.3% (95%: +1.0% to +1.5%); GAIN | 925.8 → 937.3; raw +1.2% (95%: +1.2% to +1.3%); GAIN | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | 0.6175 → 0.6252; raw +1.2% (95%: +1.1% to +1.4%), +0.0077 in the gauge's unit; GAIN | 0.6172 → 0.6251; raw +1.3% (95%: +1.2% to +1.4%), +0.0079 in the gauge's unit; GAIN | 0.6173 → 0.625; raw +1.2% (95%: +1.2% to +1.3%), +0.0077 in the gauge's unit; GAIN | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.68 | 5.68 | 5.681 → 5.683; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | 5.213 → 5.212; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | 5.624 → 5.637; raw +0.2% (95%: −0.5% to +1.0%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| latency, 99th percentile (ms) | 5.74 | 5.74 | 5.736 → 5.745; raw +0.2% (95%: +0.1% to +0.2%); STEADY | 5.362 → 5.505; raw +2.7% (95%: −3.5% to +8.8%); LOSS | 5.685 → 5.704; raw +0.3% (95%: −0.3% to +1.0%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 2.26 | 2.22 | 2.258 → 2.219; raw −1.7% (95%: −1.8% to −1.6%); GAIN | 2.056 → 2.021; raw −1.7% (95%: −3.1% to −0.3%); GAIN | 2.184 → 2.157; raw −1.2% (95%: −3.0% to +0.6%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | 64 → 65.4; raw +2.2% (95%: +1.8% to +2.5%); power given | 64 → 65.33; raw +2.1% (95%: +1.6% to +2.5%); power given | 64 → 65.36; raw +2.1% (95%: +1.8% to +2.5%); power given | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.8 | 60.7 → 61.85; raw +1.9% (95%: +1.5% to +2.3%); power given | 60.7 → 61.9; raw +2.0% (95%: +1.6% to +2.3%); power given | 60.7 → 61.94; raw +2.0% (95%: +1.9% to +2.2%); power given | **power given in all three of our runs** |
| keys evicted | 243,066 | 237,940 | 2.431e+05 → 2.379e+05; raw −2.1% (95%: −5.2% to +0.9%) | 2.432e+05 → 2.358e+05; raw −3.1% (95%: −5.1% to −1.0%) | 2.432e+05 → 2.348e+05; raw −3.4% (95%: −3.5% to −3.4%) | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.15 | 0.1313 → 0.1498; raw +14.1% (95%: −0.8% to +29.0%), +0.0185 in the gauge's unit; power given | 0.07422 → 0.05981; raw −19.4% (95%: −105.1% to +66.2%), −0.0144 in the gauge's unit; GAIN | 0.1249 → 0.1232; raw −1.4% (95%: −27.7% to +25.0%), −0.0017 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 218.0 | 254.5 | 218 → 254.5; raw +16.7% (95%: −0.6% to +34.0%); power given | 132.2 → 104.8; raw −20.7% (95%: −110.9% to +69.6%); GAIN | 221.3 → 216.5; raw −2.2% (95%: −33.6% to +29.2%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.523 | 0.603 | 0.5232 → 0.6032; raw +15.3% (95%: −1.7% to +32.3%), +0.0799 in the gauge's unit; power given | 0.3179 → 0.249; raw −21.7% (95%: −111.6% to +68.3%), −0.0689 in the gauge's unit; GAIN | 0.5312 → 0.5132; raw −3.4% (95%: −34.7% to +27.9%), −0.0181 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 14.3 | 0 → 14.33; raw +14.3333 in the gauge's unit (95%: +10.5384 to +18.1282) | 0 → 12; raw +12.0000 in the gauge's unit (95%: +9.5157 to +14.4843) | 0 → 13.67; raw +13.6667 in the gauge's unit (95%: +7.9293 to +19.4040) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused); run C: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused).

**Across 3 untouched workloads: 9 gauge-rows GAIN, 2 LOSS, 2 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 STEADY, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
