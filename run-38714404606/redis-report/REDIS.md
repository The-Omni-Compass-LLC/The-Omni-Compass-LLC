# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | +0.0% | -2.26 to 2.48 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0181 to 0.0249 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.000702 to 0.000477 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.1% | -0.0623 to 0.0505 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.23 | 5.84 | -6.3% | -2.19 to 1.41 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.77 | 1.76 | -0.3% | -0.0717 to 0.0593 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 60.9 | -4.8% | -3.37 to -2.73 | GAIN |
| memory used, mean (MB) | 57.2 | 55.1 | -3.7% | -2.58 to -1.63 | GAIN |
| keys evicted | 71,806 | 71,836 | +0.0% | -145 to 206 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.133 | -3.7% | -0.0319 to 0.0216 | EVEN, no difference beyond the noise |
| host CPU-seconds | 92.6 | 88.7 | -4.3% | -25.7 to 17.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.479 | 0.458 | -4.3% | -0.132 to 0.0914 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,354 | +6.9% | 84.1 to 91.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00237 to 0.00272 | EVEN, the same |
| cache hit rate | 0.845 | 0.904 | +7.0% | 0.0559 to 0.062 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.45 | -1.1% | -0.0664 to -0.0588 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.3% | -0.0276 to -0.0101 | GAIN |
| latency, mean (ms) | 0.967 | 0.653 | -32.4% | -0.325 to -0.302 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 75.9 | +18.7% | 9.89 to 14 | power given |
| memory used, mean (MB) | 61.3 | 69.3 | +13.1% | 7.64 to 8.41 | power given |
| keys evicted | 103,463 | 64,151 | -38.0% | -41,556 to -37,068 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0986 | -11.4% | -0.0308 to 0.00546 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 173 | -12.2% | -60.6 to 12.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.347 | 0.285 | -17.9% | -0.129 to 0.00459 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 48 |  | 48 to 48 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 914 | 919 | +0.6% | -17.4 to 27.6 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0858 to 0.0946 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00203 to -0.000707 | LOSS |
| latency, 95th percentile (ms) | 7.3 | 6.36 | -12.9% | -4.43 to 2.55 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.66 | 7.71 | -11.0% | -4.66 to 2.77 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.62 | 2.41 | -7.9% | -0.869 to 0.454 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | 0.244 to 1.93 | power given |
| memory used, mean (MB) | 60.7 | 60.8 | +0.2% | 0.0381 to 0.215 | power given |
| keys evicted | 243,127 | 245,148 | +0.8% | -2,415 to 6,456 | shown, not judged |
| host CPU busy (share of the run) | 0.205 | 0.157 | -23.2% | -0.143 to 0.0485 | EVEN, no difference beyond the noise |
| host CPU-seconds | 342 | 261 | -23.7% | -237 to 74.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.833 | 0.632 | -24.2% | -0.599 to 0.196 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 14.4 to 27.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,252 | +5.8% | 64.7 to 72.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00258 to 0.00369 | EVEN, the same |
| cache hit rate | 0.789 | 0.835 | +5.8% | 0.0431 to 0.0485 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.2% | -0.0155 to -0.00295 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.79 | -0.0% | -0.0102 to 0.00845 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.09 | -18.8% | -0.269 to -0.237 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 87.2 | +36.3% | 22 to 24.5 | power given |
| memory used, mean (MB) | 61.2 | 79.3 | +29.6% | 18 to 18.2 | power given |
| keys evicted | 138,104 | 108,285 | -21.6% | -30,478 to -29,160 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.119 | -0.3% | -0.0175 to 0.0168 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 201 | +0.6% | -30.9 to 33.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.375 | 0.357 | -4.9% | -0.0747 to 0.038 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 53 |  | 39.9 to 66.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
