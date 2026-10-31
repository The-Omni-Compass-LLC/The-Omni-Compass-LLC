# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39150490855 | `c1c1b59711b1` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| B | 39159008310 | `3cb376bb3284` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| C | 39167582853 | `e2d5958834f5` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,392 | 1393 → 1392; raw −0.1% (95%: −0.4% to +0.3%); STEADY | 1393 → 1393; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1392 → 1393; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.929 | 0.929 | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.52 | 5.55 | 5.522 → 5.548; raw +0.5% (95%: −1.6% to +2.5%); STEADY | 5.503 → 5.499; raw −0.1% (95%: −0.2% to +0.1%); STEADY | 5.672 → 5.671; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, 99th percentile (ms) | 5.69 | 5.8 | 5.693 → 5.805; raw +2.0% (95%: −6.4% to +10.3%); LOSS | 5.663 → 5.664; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 5.758 → 5.76; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.514 | 0.539 | 0.5137 → 0.5389; raw +4.9% (95%: −14.3% to +24.1%), +0.0252 in the gauge's unit; LOSS | 0.523 → 0.5238; raw +0.2% (95%: ±0.0% to +0.4%), +0.0008 in the gauge's unit; STEADY | 0.5669 → 0.5655; raw −0.2% (95%: −1.0% to +0.5%), −0.0014 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 333.1 | 333.1 | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.0897 | 0.107 | 0.08965 → 0.1067; raw +19.0% (95%: −45.7% to +83.7%), +0.0171 in the gauge's unit; power given | 0.1105 → 0.09547; raw −13.6% (95%: −32.8% to +5.5%), −0.0151 in the gauge's unit; GAIN | 0.09387 → 0.1025; raw +9.2% (95%: −10.7% to +29.1%), +0.0087 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 157.9 | 190.2 | 157.9 → 190.2; raw +20.5% (95%: −51.3% to +92.3%); power given | 198.1 → 168.1; raw −15.2% (95%: −36.8% to +6.5%); GAIN | 157.2 → 173.1; raw +10.2% (95%: −11.3% to +31.6%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.252 | 0.304 | 0.2519 → 0.3038; raw +20.6% (95%: −51.2% to +92.4%), +0.0519 in the gauge's unit; power given | 0.3161 → 0.2681; raw −15.2% (95%: −36.8% to +6.5%), −0.0480 in the gauge's unit; GAIN | 0.2508 → 0.2763; raw +10.1% (95%: −11.3% to +31.6%), +0.0254 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | 1327 → 1327; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1327 → 1327; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1327 → 1327; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.885 | 0.885 | 0.8851 → 0.885; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.71 | 5.71 | 5.705 → 5.709; raw +0.1% (95%: −0.1% to +0.2%); STEADY | 5.716 → 5.709; raw −0.1% (95%: −0.5% to +0.2%); STEADY | 5.718 → 5.723; raw +0.1% (95%: −0.3% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.77 | 5.77 | 5.769 → 5.773; raw +0.1% (95%: ±0.0% to +0.2%); STEADY | 5.785 → 5.774; raw −0.2% (95%: −0.7% to +0.3%); STEADY | 5.783 → 5.792; raw +0.2% (95%: −0.3% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, mean (ms) | 0.809 | 0.81 | 0.809 → 0.8096; raw +0.1% (95%: −0.9% to +1.0%), +0.0006 in the gauge's unit; STEADY | 0.811 → 0.8097; raw −0.2% (95%: −1.0% to +0.7%), −0.0013 in the gauge's unit; STEADY | 0.8108 → 0.8142; raw +0.4% (95%: −1.3% to +2.1%), +0.0034 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 199.9 | 199.9 | 199.9 → 199.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 199.9 → 199.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 199.9 → 199.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.0993 | 0.0949 | 0.09932 → 0.09494; raw −4.4% (95%: −43.0% to +34.1%), −0.0044 in the gauge's unit; GAIN | 0.09495 → 0.109; raw +14.8% (95%: −28.8% to +58.4%), +0.0141 in the gauge's unit; power given | 0.1172 → 0.1066; raw −9.0% (95%: −72.7% to +54.7%), −0.0106 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 66.4 | 63.4 | 66.42 → 63.39; raw −4.6% (95%: −47.0% to +37.9%); GAIN | 62.98 → 73.82; raw +17.2% (95%: −32.5% to +67.0%); power given | 79.64 → 71.73; raw −9.9% (95%: −79.3% to +59.4%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.278 | 0.265 | 0.278 → 0.2653; raw −4.6% (95%: −47.0% to +37.9%), −0.0127 in the gauge's unit; GAIN | 0.2636 → 0.3089; raw +17.2% (95%: −32.5% to +67.0%), +0.0454 in the gauge's unit; power given | 0.3333 → 0.3002; raw −9.9% (95%: −79.3% to +59.4%), −0.0331 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | 1472 → 1472; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1472 → 1472; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1469 → 1470; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.981 | 0.981 | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.159 | 0.168 | 0.1594 → 0.1676; raw +5.1% (95%: −6.4% to +16.6%), +0.0081 in the gauge's unit; LOSS | 0.2311 → 0.2284; raw −1.2% (95%: −3.3% to +0.9%), −0.0027 in the gauge's unit; GAIN | 0.1068 → 0.1028; raw −3.7% (95%: −16.0% to +8.6%), −0.0039 in the gauge's unit; GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 5.42 | 5.46 | 5.423 → 5.465; raw +0.8% (95%: −1.6% to +3.1%); LOSS | 5.721 → 5.716; raw −0.1% (95%: −0.4% to +0.2%); STEADY | 5.209 → 5.207; raw ±0.0% (95%: −0.4% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.22%) |
| latency, mean (ms) | 0.214 | 0.218 | 0.2137 → 0.2177; raw +1.9% (95%: −2.9% to +6.6%), +0.0040 in the gauge's unit; LOSS | 0.2868 → 0.2852; raw −0.5% (95%: −3.0% to +2.0%), −0.0015 in the gauge's unit; GAIN | 0.1804 → 0.1806; raw +0.1% (95%: −2.7% to +2.9%), +0.0002 in the gauge's unit; STEADY | **the runs disagree** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 348.4 | 348.4 | 348.4 → 348.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 348.5 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 348.4 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.0768 | 0.078 | 0.07681 → 0.07796; raw +1.5% (95%: −20.6% to +23.6%), +0.0011 in the gauge's unit; power given | 0.09176 → 0.08584; raw −6.5% (95%: −52.0% to +39.0%), −0.0059 in the gauge's unit; GAIN | 0.04818 → 0.07276; raw +51.0% (95%: −20.7% to +122.7%), +0.0246 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 136.2 | 137.9 | 136.2 → 137.9; raw +1.2% (95%: −21.9% to +24.3%); power given | 153.8 → 143.3; raw −6.8% (95%: −56.9% to +43.2%); GAIN | 84.63 → 131.4; raw +55.3% (95%: −22.6% to +133.2%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.206 | 0.208 | 0.2056 → 0.2081; raw +1.2% (95%: −21.9% to +24.3%), +0.0025 in the gauge's unit; power given | 0.2322 → 0.2163; raw −6.8% (95%: −56.9% to +43.3%), −0.0159 in the gauge's unit; GAIN | 0.128 → 0.1987; raw +55.3% (95%: −22.6% to +133.1%), +0.0707 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,174 | 1,174 | 1174 → 1174; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1173 → 1173; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1173 → 1173; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.783 | 0.783 | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.54 | 5.55 | 5.54 → 5.554; raw +0.2% (95%: −0.8% to +1.2%); STEADY | 5.653 → 5.649; raw −0.1% (95%: −0.4% to +0.2%); STEADY | 5.662 → 5.664; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 99th percentile (ms) | 5.63 | 5.64 | 5.632 → 5.645; raw +0.2% (95%: −0.7% to +1.1%); STEADY | 5.716 → 5.713; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | 5.726 → 5.729; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, mean (ms) | 1.29 | 1.29 | 1.286 → 1.292; raw +0.4% (95%: −0.9% to +1.7%); STEADY | 1.353 → 1.351; raw −0.1% (95%: −0.5% to +0.3%); STEADY | 1.36 → 1.36; raw ±0.0% (95%: −0.4% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 257.3 | 257.3 | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.109 | 0.111 → 0.1093; raw −1.5% (95%: −32.6% to +29.5%), −0.0017 in the gauge's unit; GAIN | 0.115 → 0.1135; raw −1.4% (95%: −14.8% to +12.1%), −0.0016 in the gauge's unit; GAIN | 0.1147 → 0.1153; raw +0.6% (95%: −36.5% to +37.6%), +0.0006 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 198.5 | 194.6 | 198.5 → 194.6; raw −2.0% (95%: −36.1% to +32.1%); GAIN | 193.5 → 190.6; raw −1.5% (95%: −16.9% to +13.9%); GAIN | 192.1 → 193.1; raw +0.5% (95%: −41.6% to +42.7%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.376 | 0.368 | 0.3759 → 0.3684; raw −2.0% (95%: −36.1% to +32.1%), −0.0075 in the gauge's unit; GAIN | 0.3664 → 0.3608; raw −1.5% (95%: −16.9% to +13.9%), −0.0056 in the gauge's unit; GAIN | 0.3637 → 0.3657; raw +0.5% (95%: −41.6% to +42.7%), +0.0020 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 0 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 25 STEADY, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
