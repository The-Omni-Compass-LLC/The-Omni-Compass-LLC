# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39826081107 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| B | 39846960314 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| C | 39866161041 | `5f430c111d90` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | 1393 → 1393; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1391 → 1391; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 1393 → 1393; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.929 | 0.929 | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9286 → 0.9286; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.68 | 5.67 | 5.683 → 5.671; raw −0.2% (95%: −0.4% to ±0.0%); STEADY | 5.195 → 5.19; raw −0.1% (95%: −0.2% to +0.1%); STEADY | 5.678 → 5.682; raw +0.1% (95%: −0.1% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 99th percentile (ms) | 5.78 | 5.76 | 5.776 → 5.759; raw −0.3% (95%: −0.7% to +0.1%); STEADY | 5.224 → 5.226; raw ±0.0% (95%: −0.8% to +0.9%); STEADY | 5.767 → 5.773; raw +0.1% (95%: −0.2% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 0.568 | 0.564 | 0.568 → 0.5642; raw −0.7% (95%: −1.8% to +0.5%), −0.0038 in the gauge's unit; GAIN | 0.4458 → 0.4473; raw +0.3% (95%: −5.4% to +6.1%), +0.0015 in the gauge's unit; STEADY | 0.5687 → 0.5687; raw ±0.0% (95%: −1.4% to +1.3%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 333.1 | 333.1 | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 333 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 333.1 → 333.1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.0883 | 0.0904 | 0.0883 → 0.09043; raw +2.4% (95%: −45.3% to +50.1%), +0.0021 in the gauge's unit; power given | 0.06016 → 0.05806; raw −3.5% (95%: −55.1% to +48.1%), −0.0021 in the gauge's unit; GAIN | 0.1055 → 0.0944; raw −10.6% (95%: −30.5% to +9.4%), −0.0111 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 146.6 | 150.9 | 146.6 → 150.9; raw +2.9% (95%: −49.2% to +55.0%); power given | 106.9 → 103.3; raw −3.4% (95%: −58.1% to +51.3%); GAIN | 178.6 → 158; raw −11.5% (95%: −32.6% to +9.5%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.234 | 0.241 | 0.2339 → 0.2407; raw +2.9% (95%: −49.2% to +55.0%), +0.0068 in the gauge's unit; power given | 0.1707 → 0.165; raw −3.3% (95%: −58.2% to +51.6%), −0.0057 in the gauge's unit; GAIN | 0.285 → 0.2521; raw −11.5% (95%: −32.6% to +9.5%), −0.0329 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | 1327 → 1327; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1327 → 1327; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | 1325 → 1325; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.885 | 0.885 | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.8851 → 0.8851; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.74 | 5.75 | 5.737 → 5.747; raw +0.2% (95%: −0.4% to +0.8%); STEADY | 5.715 → 5.717; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | 5.207 → 5.208; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| latency, 99th percentile (ms) | 5.81 | 5.83 | 5.815 → 5.826; raw +0.2% (95%: −0.3% to +0.7%); STEADY | 5.78 → 5.784; raw +0.1% (95%: −0.1% to +0.2%); STEADY | 5.242 → 5.243; raw ±0.0% (95%: −0.5% to +0.6%); STEADY | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, mean (ms) | 0.819 | 0.823 | 0.8189 → 0.823; raw +0.5% (95%: −0.1% to +1.1%), +0.0041 in the gauge's unit; STEADY | 0.8114 → 0.8119; raw +0.1% (95%: −0.5% to +0.7%), +0.0005 in the gauge's unit; STEADY | 0.6796 → 0.675; raw −0.7% (95%: −3.4% to +2.0%), −0.0046 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.04%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 199.9 | 199.9 | 199.9 → 199.9; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 199.9 → 199.9; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | 199.9 → 199.9; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.128 | 0.1045 → 0.1277; raw +22.2% (95%: −10.8% to +55.2%), +0.0232 in the gauge's unit; power given | 0.1026 → 0.1122; raw +9.3% (95%: −69.8% to +88.5%), +0.0096 in the gauge's unit; power given | 0.07193 → 0.06769; raw −5.9% (95%: −81.2% to +69.4%), −0.0042 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 69.9 | 87.2 | 69.89 → 87.25; raw +24.8% (95%: −11.2% to +60.9%); power given | 68.84 → 76.09; raw +10.5% (95%: −79.0% to +100.1%); power given | 51.64 → 48.35; raw −6.4% (95%: −86.7% to +74.0%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.293 | 0.365 | 0.2926 → 0.3652; raw +24.8% (95%: −11.2% to +60.9%), +0.0727 in the gauge's unit; power given | 0.2881 → 0.3184; raw +10.5% (95%: −79.0% to +100.0%), +0.0303 in the gauge's unit; power given | 0.2165 → 0.2027; raw −6.4% (95%: −86.8% to +74.1%), −0.0138 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | 1472 → 1472; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1472 → 1472; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1470 → 1470; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.981 | 0.981 | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.9814 → 0.9814; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.165 | 0.167 | 0.165 → 0.1673; raw +1.4% (95%: −5.8% to +8.5%), +0.0023 in the gauge's unit; LOSS | 0.2303 → 0.2341; raw +1.7% (95%: −3.4% to +6.7%), +0.0038 in the gauge's unit; LOSS | 0.1129 → 0.1142; raw +1.2% (95%: −1.0% to +3.4%), +0.0013 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 5.48 | 5.48 | 5.476 → 5.477; raw ±0.0% (95%: −0.4% to +0.5%); STEADY | 5.723 → 5.721; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 5.223 → 5.219; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, mean (ms) | 0.229 | 0.229 | 0.2286 → 0.2291; raw +0.2% (95%: −1.8% to +2.2%), +0.0006 in the gauge's unit; STEADY | 0.2882 → 0.2884; raw +0.1% (95%: −1.4% to +1.6%), +0.0002 in the gauge's unit; STEADY | 0.1815 → 0.1813; raw −0.1% (95%: −2.8% to +2.6%), −0.0002 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 348.4 | 348.4 | 348.4 → 348.4; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 348.5 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 348.4 → 348.5; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.0816 | 0.0865 | 0.08159 → 0.08647; raw +6.0% (95%: −60.8% to +72.7%), +0.0049 in the gauge's unit; power given | 0.0934 → 0.07966; raw −14.7% (95%: −73.3% to +43.9%), −0.0137 in the gauge's unit; GAIN | 0.04716 → 0.06437; raw +36.5% (95%: +12.4% to +60.6%), +0.0172 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 142.0 | 151.1 | 142 → 151.1; raw +6.4% (95%: −66.6% to +79.5%); power given | 157.2 → 131.7; raw −16.2% (95%: −79.9% to +47.4%); GAIN | 82.68 → 115.1; raw +39.2% (95%: +10.4% to +67.9%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.214 | 0.228 | 0.2143 → 0.2281; raw +6.4% (95%: −66.6% to +79.5%), +0.0138 in the gauge's unit; power given | 0.2374 → 0.1989; raw −16.2% (95%: −79.9% to +47.4%), −0.0385 in the gauge's unit; GAIN | 0.125 → 0.1739; raw +39.2% (95%: +10.4% to +67.9%), +0.0489 in the gauge's unit; power given | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,172 | 1172 → 1172; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1172 → 1173; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1172 → 1172; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (requests a second) | 1,500 | 1,500 | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 1500 → 1500; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.783 | 0.783 | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | 0.7825 → 0.7825; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.21 | 5.2 | 5.207 → 5.204; raw −0.1% (95%: −0.1% to ±0.0%); STEADY | 5.199 → 5.2; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | 5.204 → 5.208; raw +0.1% (95%: −0.2% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 99th percentile (ms) | 5.26 | 5.25 | 5.257 → 5.252; raw −0.1% (95%: −0.6% to +0.4%); STEADY | 5.233 → 5.239; raw +0.1% (95%: −0.4% to +0.6%); STEADY | 5.257 → 5.265; raw +0.2% (95%: −0.8% to +1.1%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, mean (ms) | 1.2 | 1.2 | 1.204 → 1.202; raw −0.2% (95%: −1.3% to +1.0%); STEADY | 1.192 → 1.192; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 1.202 → 1.204; raw +0.1% (95%: −0.8% to +1.1%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| failed requests | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY | STEADY, the same |
| memory used, mean (MB) | 257.3 | 257.3 | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 257.3 → 257.3; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |
| host CPU busy (share of the run) | 0.0677 | 0.0586 | 0.06771 → 0.05858; raw −13.5% (95%: −55.1% to +28.2%), −0.0091 in the gauge's unit; GAIN | 0.05586 → 0.06286; raw +12.5% (95%: −1.3% to +26.4%), +0.0070 in the gauge's unit; power given | 0.05495 → 0.05429; raw −1.2% (95%: −118.3% to +115.8%), −0.0007 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 120.0 | 102.8 | 120 → 102.8; raw −14.3% (95%: −58.6% to +30.0%); GAIN | 98.51 → 111.5; raw +13.2% (95%: −1.3% to +27.7%); power given | 96.52 → 95.15; raw −1.4% (95%: −123.8% to +121.0%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.227 | 0.195 | 0.2274 → 0.1949; raw −14.3% (95%: −58.7% to +30.1%), −0.0325 in the gauge's unit; GAIN | 0.1867 → 0.2114; raw +13.2% (95%: −1.3% to +27.8%), +0.0247 in the gauge's unit; power given | 0.1829 → 0.1804; raw −1.4% (95%: −123.7% to +120.9%), −0.0026 in the gauge's unit; GAIN | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 0 gauge-rows GAIN, 1 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 26 STEADY, 9 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
