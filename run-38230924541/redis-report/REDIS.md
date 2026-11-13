# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,046 | 1,045 | -0.1% | -2.28 to 0.367 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0193 to 0.019 | same |
| cache hit rate | 0.697 | 0.697 | -0.1% | -0.00153 to 0.00034 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0157 to 0.0108 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.001 to 0.0222 | no difference beyond the noise |
| latency, mean (ms) | 1.86 | 1.87 | +0.3% | -0.007 to 0.0194 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.7 | -2.0% | -2.84 to 0.229 | no difference beyond the noise |
| memory used, mean (MB) | 56.9 | 56.4 | -0.9% | -1.77 to 0.756 | no difference beyond the noise |
| keys evicted | 49,961 | 50,454 | +1.0% | -369 to 1,355 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.133 | -1.4% | -0.1 to 0.0964 | no difference beyond the noise |
| host CPU-seconds | 59.8 | 59 | -1.4% | -50.9 to 49.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.477 | 0.47 | -1.3% | -0.406 to 0.394 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 4.67 |  | -1.07 to 10.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,250 | 1,298 | +3.9% | 6.78 to 90.1 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.045 to 0.0298 | no difference beyond the noise |
| cache hit rate | 0.835 | 0.868 | +4.0% | 0.00483 to 0.0613 | better |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.1% | -0.0106 to 0.000149 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.27 | -0.0% | -0.0175 to 0.0137 | no difference beyond the noise |
| latency, mean (ms) | 0.947 | 0.782 | -17.4% | -0.308 to -0.0215 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 72.1 | +12.7% | -7.27 to 23.5 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 66.2 | +8.0% | -4.78 to 14.6 | no difference beyond the noise |
| keys evicted | 73,205 | 58,499 | -20.1% | -27,685 to -1,727 | shown, not judged |
| host CPU busy (share of the run) | 0.056 | 0.0629 | +12.3% | -0.00775 to 0.0215 | no difference beyond the noise |
| host CPU-seconds | 65.2 | 73.8 | +13.2% | -9.45 to 26.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.174 | 0.19 | +9.0% | -0.0373 to 0.0687 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 18 to 28 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 7.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 832 | 827 | -0.6% | -6.15 to -4.44 | **WORSE** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0449 to 0.0241 | no difference beyond the noise |
| cache hit rate | 0.555 | 0.552 | -0.6% | -0.00413 to -0.00272 | **WORSE** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.1% | 0.000296 to 0.0137 | **WORSE** |
| latency, 99th percentile (ms) | 5.73 | 5.75 | +0.3% | 0.00409 to 0.036 | **WORSE** |
| latency, mean (ms) | 2.6 | 2.62 | +1.0% | 0.0174 to 0.0326 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.2 | +0.3% | 0.0983 to 0.327 | **WORSE** |
| memory used, mean (MB) | 60.3 | 60 | -0.5% | -0.326 to -0.261 | better |
| keys evicted | 184,960 | 188,233 | +1.8% | 3,082 to 3,464 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.155 | +11.2% | -0.0313 to 0.0626 | no difference beyond the noise |
| host CPU-seconds | 154 | 175 | +13.1% | -40.5 to 80.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.618 | 0.704 | +13.8% | -0.158 to 0.329 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 9 |  | 9 to 9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 3.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,131 | 1,130 | -0.1% | -1.87 to 0.476 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00364 to 0.00429 | same |
| cache hit rate | 0.754 | 0.753 | -0.1% | -0.00167 to 0.000561 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.64 | 5.65 | +0.1% | -0.0415 to 0.0508 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.71 | +0.1% | -0.0275 to 0.0441 | no difference beyond the noise |
| latency, mean (ms) | 1.48 | 1.48 | +0.4% | -0.028 to 0.0389 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64 | -0.0% | -0.0929 to 0.0396 | no difference beyond the noise |
| memory used, mean (MB) | 61.1 | 60.7 | -0.7% | -0.544 to -0.274 | better |
| keys evicted | 106,689 | 107,752 | +1.0% | 590 to 1,535 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.122 | -5.0% | -0.0564 to 0.0435 | no difference beyond the noise |
| host CPU-seconds | 152 | 143 | -5.8% | -76.7 to 59.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.447 | 0.422 | -5.7% | -0.226 to 0.174 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.3 |  | 18.5 to 24.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
