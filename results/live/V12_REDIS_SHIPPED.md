# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39382995467 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| B | 39414279979 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| C | 39461540163 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | 1393 → 1393; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1392 → 1392; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1393 → 1393; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.929 | 0.929 | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.69 | 5.69 | 5.688 → 5.695; raw +0.1% (95%: ±0.0% to +0.2%); STEADY | 5.687 → 5.683; raw −0.1% (95%: −0.3% to +0.1%); STEADY | 5.677 → 5.676; raw ±0.0% (95%: −0.6% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.8 | 5.81 | 5.8 → 5.809; raw +0.2% (95%: ±0.0% to +0.3%); STEADY | 5.785 → 5.779; raw −0.1% (95%: −0.3% to +0.1%); STEADY | 5.766 → 5.766; raw ±0.0% (95%: −0.7% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, mean (ms) | 0.576 | 0.575 | 0.5755 → 0.5751; raw −0.1% (95%: −1.3% to +1.2%), −0.0004 in the gauge's unit; STEADY | 0.576 → 0.5766; raw +0.1% (95%: −1.0% to +1.1%), +0.0006 in the gauge's unit; STEADY | 0.5676 → 0.5659; raw −0.3% (95%: −1.4% to +0.8%), −0.0016 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.09%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 333.1 | 333.1 | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.0933 | 0.095 | 0.09334 → 0.09498; raw +1.8% (95%: −11.1% to +14.6%), +0.0016 in the gauge's unit; power given | 0.09709 → 0.1016; raw +4.6% (95%: −67.2% to +76.5%), +0.0045 in the gauge's unit; power given | 0.09878 → 0.09275; raw −6.1% (95%: −29.2% to +17.0%), −0.0060 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 155.8 | 158.6 | 155.8 → 158.6; raw +1.8% (95%: −12.4% to +16.1%); power given | 162.7 → 170.5; raw +4.8% (95%: −74.9% to +84.5%); power given | 166.2 → 154.9; raw −6.8% (95%: −32.7% to +19.1%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.249 | 0.253 | 0.2486 → 0.2531; raw +1.8% (95%: −12.4% to +16.0%), +0.0045 in the gauge's unit; power given | 0.2597 → 0.2721; raw +4.8% (95%: −74.9% to +84.5%), +0.0124 in the gauge's unit; power given | 0.2653 → 0.2472; raw −6.8% (95%: −32.7% to +19.1%), −0.0180 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | 1327 → 1327; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1327 → 1327; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1327 → 1327; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.885 | 0.885 | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.5 | 5.5 | 5.496 → 5.496; raw ±0.0% (95%: −0.8% to +0.8%); STEADY | 5.711 → 5.707; raw −0.1% (95%: −0.3% to +0.2%); STEADY | 5.393 → 5.296; raw −1.8% (95%: −5.5% to +1.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 5.61 | 5.61 | 5.607 → 5.61; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | 5.777 → 5.771; raw −0.1% (95%: −0.4% to +0.2%); STEADY | 5.62 → 5.601; raw −0.3% (95%: −1.1% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.13%) |
| latency, mean (ms) | 0.738 | 0.74 | 0.7378 → 0.7395; raw +0.2% (95%: −1.9% to +2.4%), +0.0017 in the gauge's unit; STEADY | 0.8085 → 0.8076; raw −0.1% (95%: −0.5% to +0.3%), −0.0009 in the gauge's unit; STEADY | 0.7133 → 0.708; raw −0.7% (95%: −3.2% to +1.7%), −0.0053 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.21%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 199.8 | 199.9 | 199.8 → 199.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 199.8 → 199.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 199.8 → 199.8; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.0876 | 0.101 | 0.08758 → 0.1009; raw +15.2% (95%: −22.0% to +52.5%), +0.0133 in the gauge's unit; power given | 0.1136 → 0.09171; raw −19.2% (95%: −65.1% to +26.6%), −0.0218 in the gauge's unit; GAIN | 0.08338 → 0.07447; raw −10.7% (95%: −105.3% to +83.9%), −0.0089 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 61.2 | 71.4 | 61.21 → 71.43; raw +16.7% (95%: −24.7% to +58.0%); power given | 77.16 → 60.71; raw −21.3% (95%: −72.8% to +30.1%); GAIN | 59.56 → 52.62; raw −11.7% (95%: −111.5% to +88.2%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.256 | 0.299 | 0.2562 → 0.299; raw +16.7% (95%: −24.7% to +58.1%), +0.0427 in the gauge's unit; power given | 0.3229 → 0.2541; raw −21.3% (95%: −72.7% to +30.1%), −0.0688 in the gauge's unit; GAIN | 0.2493 → 0.2202; raw −11.7% (95%: −111.5% to +88.2%), −0.0290 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,470 | 1471 → 1470; raw −0.1% (95%: −0.5% to +0.4%); STEADY | 1471 → 1471; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | 1472 → 1472; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.981 | 0.981 | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.236 | 0.257 | 0.2361 → 0.2565; raw +8.7% (95%: −42.5% to +59.9%), +0.0205 in the gauge's unit; LOSS | 0.1672 → 0.1648; raw −1.5% (95%: −3.5% to +0.5%), −0.0025 in the gauge's unit; GAIN | 0.1995 → 0.2011; raw +0.8% (95%: −0.2% to +1.7%), +0.0015 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 5.73 | 5.76 | 5.733 → 5.759; raw +0.5% (95%: −2.0% to +2.9%); STEADY | 5.488 → 5.481; raw −0.1% (95%: −0.3% to +0.1%); STEADY | 5.657 → 5.66; raw +0.1% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.13%) |
| latency, mean (ms) | 0.288 | 0.302 | 0.2879 → 0.3015; raw +4.8% (95%: −25.0% to +34.5%), +0.0137 in the gauge's unit; LOSS | 0.2331 → 0.2318; raw −0.6% (95%: −2.1% to +1.0%), −0.0013 in the gauge's unit; GAIN | 0.2608 → 0.2606; raw −0.1% (95%: −0.1% to −0.1%), −0.0002 in the gauge's unit; STEADY | **the runs disagree** |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 348.5 | 348.5 | 348.5 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 348.4 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 348.4 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.115 | 0.1192 → 0.1152; raw −3.4% (95%: −67.9% to +61.2%), −0.0040 in the gauge's unit; GAIN | 0.09675 → 0.08208; raw −15.2% (95%: −51.8% to +21.5%), −0.0147 in the gauge's unit; GAIN | 0.1152 → 0.102; raw −11.5% (95%: −43.8% to +20.8%), −0.0132 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 204.1 | 196.3 | 204.1 → 196.3; raw −3.8% (95%: −74.8% to +67.1%); GAIN | 171.1 → 142.8; raw −16.5% (95%: −56.3% to +23.3%); GAIN | 201.6 → 175.8; raw −12.8% (95%: −48.9% to +23.4%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.308 | 0.297 | 0.3083 → 0.2968; raw −3.7% (95%: −74.9% to +67.4%), −0.0115 in the gauge's unit; GAIN | 0.2585 → 0.2158; raw −16.5% (95%: −56.3% to +23.3%), −0.0426 in the gauge's unit; GAIN | 0.3043 → 0.2654; raw −12.8% (95%: −48.9% to +23.3%), −0.0389 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | 1173 → 1173; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1173 → 1173; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1173 → 1173; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.783 | 0.783 | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.65 | 5.65 | 5.647 → 5.647; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 5.658 → 5.659; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 5.668 → 5.668; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 99th percentile (ms) | 5.72 | 5.72 | 5.717 → 5.718; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 5.729 → 5.727; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 5.735 → 5.735; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, mean (ms) | 1.35 | 1.35 | 1.348 → 1.349; raw +0.1% (95%: −0.2% to +0.4%); STEADY | 1.354 → 1.353; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | 1.363 → 1.362; raw ±0.0% (95%: −0.6% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 257.3 | 257.3 | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.131 | 0.126 → 0.1311; raw +4.1% (95%: −20.6% to +28.8%), +0.0052 in the gauge's unit; power given | 0.1335 → 0.124; raw −7.1% (95%: −15.3% to +1.1%), −0.0095 in the gauge's unit; GAIN | 0.1227 → 0.1138; raw −7.2% (95%: −28.4% to +13.9%), −0.0089 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 213.4 | 223.6 | 213.4 → 223.6; raw +4.8% (95%: −24.0% to +33.6%); power given | 227 → 208.5; raw −8.1% (95%: −17.7% to +1.4%); GAIN | 206.9 → 190.2; raw −8.1% (95%: −32.0% to +15.8%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.404 | 0.424 | 0.4041 → 0.4235; raw +4.8% (95%: −24.0% to +33.6%), +0.0194 in the gauge's unit; power given | 0.4297 → 0.3948; raw −8.1% (95%: −17.7% to +1.4%), −0.0349 in the gauge's unit; GAIN | 0.3917 → 0.3601; raw −8.1% (95%: −32.0% to +15.8%), −0.0317 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 4 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 24 STEADY, 8 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
