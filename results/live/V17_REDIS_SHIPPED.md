# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40005925354 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40024478954 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40038802348 | `d02c7052ae50` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,391 | 1,392 | 1391 → 1392; raw +0.1% (95%: ±0.0% to +0.1%); STEADY | 1393 → 1393; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1392 → 1392; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.929 | 0.929 | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.61 | 5.61 | 5.612 → 5.613; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | 5.496 → 5.484; raw −0.2% (95%: −0.9% to +0.5%); STEADY | 5.674 → 5.674; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 99th percentile (ms) | 5.7 | 5.7 | 5.701 → 5.703; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 5.682 → 5.68; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 5.767 → 5.762; raw −0.1% (95%: −0.3% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, mean (ms) | 0.547 | 0.544 | 0.5473 → 0.544; raw −0.6% (95%: −1.1% to −0.1%), −0.0033 in the gauge's unit; GAIN | 0.5095 → 0.5091; raw −0.1% (95%: −1.4% to +1.2%), −0.0004 in the gauge's unit; STEADY | 0.5698 → 0.5683; raw −0.3% (95%: −0.8% to +0.3%), −0.0015 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.32%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 333.1 | 333.1 | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.118 | 0.109 → 0.1181; raw +8.3% (95%: −57.4% to +74.0%), +0.0091 in the gauge's unit; power given | 0.09642 → 0.09973; raw +3.4% (95%: −47.1% to +53.9%), +0.0033 in the gauge's unit; power given | 0.08675 → 0.09034; raw +4.1% (95%: −20.3% to +28.6%), +0.0036 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 189.1 | 207.3 | 189.1 → 207.3; raw +9.6% (95%: −65.8% to +85.0%); power given | 171.5 → 178; raw +3.8% (95%: −51.8% to +59.3%); power given | 143.7 → 150.6; raw +4.8% (95%: −22.5% to +32.1%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.302 | 0.331 | 0.302 → 0.3309; raw +9.6% (95%: −65.8% to +85.0%), +0.0289 in the gauge's unit; power given | 0.2737 → 0.284; raw +3.8% (95%: −51.8% to +59.3%), +0.0103 in the gauge's unit; power given | 0.2294 → 0.2403; raw +4.8% (95%: −22.5% to +32.0%), +0.0110 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,328 | 1,327 | 1328 → 1327; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1327 → 1327; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 1327 → 1327; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.885 | 0.885 | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.57 | 5.55 | 5.566 → 5.552; raw −0.3% (95%: −0.8% to +0.3%); STEADY | 5.745 → 5.75; raw +0.1% (95%: −0.4% to +0.6%); STEADY | 5.716 → 5.714; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 99th percentile (ms) | 5.68 | 5.67 | 5.679 → 5.668; raw −0.2% (95%: −0.9% to +0.5%); STEADY | 5.837 → 5.828; raw −0.2% (95%: −2.1% to +1.8%); STEADY | 5.785 → 5.783; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.13%) |
| latency, mean (ms) | 0.752 | 0.746 | 0.7522 → 0.7457; raw −0.9% (95%: −3.2% to +1.5%), −0.0064 in the gauge's unit; GAIN | 0.8317 → 0.8241; raw −0.9% (95%: −7.3% to +5.5%), −0.0076 in the gauge's unit; GAIN | 0.8112 → 0.8116; raw +0.1% (95%: −1.1% to +1.2%), +0.0004 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 199.8 | 199.8 | 199.8 → 199.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 199.9 → 199.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 199.9 → 199.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.0995 | 0.0786 | 0.09947 → 0.0786; raw −21.0% (95%: −93.5% to +51.5%), −0.0209 in the gauge's unit; GAIN | 0.09611 → 0.1178; raw +22.6% (95%: −82.0% to +127.1%), +0.0217 in the gauge's unit; power given | 0.1126 → 0.127; raw +12.7% (95%: −42.3% to +67.8%), +0.0144 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 71.0 | 54.7 | 70.95 → 54.69; raw −22.9% (95%: −103.5% to +57.6%); GAIN | 63.28 → 79.93; raw +26.3% (95%: −91.5% to +144.1%); power given | 76.27 → 87.33; raw +14.5% (95%: −47.7% to +76.7%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.297 | 0.229 | 0.2969 → 0.2289; raw −22.9% (95%: −103.5% to +57.6%), −0.0681 in the gauge's unit; GAIN | 0.2649 → 0.3345; raw +26.3% (95%: −91.4% to +144.0%), +0.0696 in the gauge's unit; power given | 0.3192 → 0.3655; raw +14.5% (95%: −47.7% to +76.7%), +0.0463 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | 1472 → 1472; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1472 → 1472; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1472 → 1472; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.981 | 0.981 | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.204 | 0.202 | 0.2036 → 0.2019; raw −0.8% (95%: −1.9% to +0.3%), −0.0017 in the gauge's unit; GAIN | 0.2299 → 0.2312; raw +0.6% (95%: −2.8% to +4.0%), +0.0013 in the gauge's unit; LOSS | 0.194 → 0.2179; raw +12.3% (95%: −13.8% to +38.4%), +0.0238 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 5.66 | 5.66 | 5.659 → 5.657; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | 5.721 → 5.723; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 5.531 → 5.524; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, mean (ms) | 0.264 | 0.263 | 0.2639 → 0.2629; raw −0.4% (95%: −1.3% to +0.5%), −0.0010 in the gauge's unit; STEADY | 0.2876 → 0.2879; raw +0.1% (95%: −1.5% to +1.7%), +0.0003 in the gauge's unit; STEADY | 0.2436 → 0.2466; raw +1.2% (95%: ±0.0% to +2.5%), +0.0030 in the gauge's unit; LOSS | STEADY, under the floor (the three runs' mean 0.31%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 348.4 | 348.5 | 348.4 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 348.5 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 348.4 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.0988 | 0.1119 → 0.09882; raw −11.7% (95%: −26.2% to +2.8%), −0.0131 in the gauge's unit; GAIN | 0.0841 → 0.09564; raw +13.7% (95%: −37.0% to +64.4%), +0.0115 in the gauge's unit; power given | 0.0893 → 0.09863; raw +10.5% (95%: −51.6% to +72.5%), +0.0093 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 195.5 | 170.2 | 195.5 → 170.2; raw −12.9% (95%: −28.7% to +2.9%); GAIN | 139.9 → 160.9; raw +15.1% (95%: −41.1% to +71.3%); power given | 157.1 → 175.1; raw +11.4% (95%: −57.7% to +80.6%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.295 | 0.257 | 0.2952 → 0.257; raw −12.9% (95%: −28.7% to +2.9%), −0.0381 in the gauge's unit; GAIN | 0.2112 → 0.2431; raw +15.1% (95%: −41.1% to +71.3%), +0.0319 in the gauge's unit; power given | 0.2372 → 0.2643; raw +11.4% (95%: −57.7% to +80.6%), +0.0271 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | 1173 → 1173; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1174 → 1174; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1173 → 1173; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.782 | 0.782 | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.66 | 5.65 | 5.655 → 5.648; raw −0.1% (95%: −0.6% to +0.3%); STEADY | 5.505 → 5.5; raw −0.1% (95%: −0.4% to +0.2%); STEADY | 5.462 → 5.464; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 99th percentile (ms) | 5.72 | 5.71 | 5.722 → 5.714; raw −0.1% (95%: −0.4% to +0.1%); STEADY | 5.605 → 5.6; raw −0.1% (95%: −0.4% to +0.2%); STEADY | 5.556 → 5.557; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, mean (ms) | 1.36 | 1.35 | 1.358 → 1.354; raw −0.3% (95%: −1.0% to +0.3%); STEADY | 1.265 → 1.262; raw −0.2% (95%: −0.5% to ±0.0%); STEADY | 1.267 → 1.266; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.20%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 257.3 | 257.3 | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 257.2 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.116 | 0.1144 → 0.1156; raw +1.1% (95%: −4.6% to +6.9%), +0.0013 in the gauge's unit; power given | 0.1009 → 0.0954; raw −5.5% (95%: −60.7% to +49.7%), −0.0055 in the gauge's unit; GAIN | 0.09003 → 0.09702; raw +7.8% (95%: −19.1% to +34.6%), +0.0070 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 191.3 | 194.4 | 191.3 → 194.4; raw +1.6% (95%: −4.7% to +8.0%); power given | 180.5 → 169.9; raw −5.8% (95%: −66.7% to +55.0%); GAIN | 157 → 170.6; raw +8.6% (95%: −21.5% to +38.8%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.362 | 0.368 | 0.3622 → 0.3681; raw +1.6% (95%: −4.7% to +8.0%), +0.0058 in the gauge's unit; power given | 0.3417 → 0.3218; raw −5.8% (95%: −66.7% to +55.0%), −0.0200 in the gauge's unit; GAIN | 0.2974 → 0.3231; raw +8.6% (95%: −21.5% to +38.8%), +0.0257 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 1 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 25 STEADY, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
