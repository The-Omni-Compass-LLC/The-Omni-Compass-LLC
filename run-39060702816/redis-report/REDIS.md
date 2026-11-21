# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.3 to 1.06 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0135 to 0.0201 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.000919 to 0.000625 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.57 | +0.0% | -0.0278 to 0.0283 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.63 | +0.1% | -0.0495 to 0.0648 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.63 | +0.0% | -0.0197 to 0.0211 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.76 to -1.2 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -1.0% | -0.854 to -0.293 | GAIN |
| keys evicted | 71,680 | 71,721 | +0.1% | -182 to 264 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.0987 | -7.8% | -0.0913 to 0.0746 | EVEN, no difference beyond the noise |
| host CPU-seconds | 74.9 | 68.6 | -8.3% | -71.1 to 58.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.386 | 0.354 | -8.3% | -0.367 to 0.302 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,286 | +1.7% | 20.8 to 23.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00121 to 0.00077 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0133 to 0.0155 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.0% | -0.00881 to 0.00505 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.24 | +0.0% | -0.0217 to 0.0234 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.89 | 0.812 | -8.8% | -0.0921 to -0.0638 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | -0.0223 to 2.81 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.4 | +1.9% | 0.118 to 2.17 | power given |
| keys evicted | 103,597 | 94,134 | -9.1% | -10,176 to -8,750 | shown, not judged |
| host CPU busy (share of the run) | 0.062 | 0.0571 | -8.0% | -0.0295 to 0.0196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 101 | -8.7% | -57 to 37.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.194 | 0.174 | -10.2% | -0.104 to 0.0641 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 11.5 to 12.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0125 to 0.0199 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00739 to 0.00826 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.49 | +0.0% | -0.00513 to 0.00674 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.57 | +0.1% | 0.000481 to 0.00667 | LOSS |
| latency, mean (ms) | 2.14 | 2.09 | -1.9% | -0.0517 to -0.0311 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.46 to 1.51 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.21 to 1.32 | power given |
| keys evicted | 243,199 | 236,896 | -2.6% | -10,760 to -1,847 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.104 | -6.4% | -0.0248 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 195 | 181 | -7.1% | -48.6 to 20.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.469 | 0.43 | -8.3% | -0.121 to 0.0436 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 12.2 to 15.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.9% | 4.29 to 16.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00706 to 0.0132 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.9% | 0.00281 to 0.0113 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.011 to 0.00803 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | -0.00289 to 0.0132 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.31 | -2.7% | -0.059 to -0.0149 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.199 to 2.4 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | 0.169 to 1.8 | power given |
| keys evicted | 138,204 | 134,253 | -2.9% | -6,835 to -1,068 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.128 | +2.4% | -0.0203 to 0.0263 | EVEN, no difference beyond the noise |
| host CPU-seconds | 209 | 215 | +2.9% | -38 to 50.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.393 | 0.401 | +2.0% | -0.0745 to 0.09 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 10.4 to 27.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
