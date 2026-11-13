# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,045 | 1,044 | -0.1% | -4.23 to 2.13 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.84 to 0.522 | no difference beyond the noise |
| cache hit rate | 0.698 | 0.697 | -0.1% | -0.00169 to 0.000536 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.0% | -0.00449 to 0.00605 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.27 | +0.2% | -0.0871 to 0.109 | no difference beyond the noise |
| latency, mean (ms) | 1.64 | 1.65 | +0.8% | -0.0387 to 0.0663 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.4 | -0.9% | -0.595 to -0.595 | better |
| memory used, mean (MB) | 56.9 | 57 | +0.1% | 0.036 to 0.0987 | **WORSE** |
| keys evicted | 49,833 | 50,572 | +1.5% | 501 to 978 | shown, not judged |
| host CPU busy (share of the run) | 0.0484 | 0.0639 | +32.0% | 0.00198 to 0.029 | **WORSE** |
| host CPU-seconds | 22.5 | 30.1 | +34.1% | 1.12 to 14.2 | **WORSE** |
| host CPU-seconds per 1,000 requests inside the line | 0.179 | 0.24 | +34.2% | 0.00866 to 0.114 | **WORSE** |
| ceiling changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,253 | 1,303 | +4.0% | 2.67 to 98.3 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00107 to 0.0017 | same |
| cache hit rate | 0.836 | 0.869 | +4.0% | 0.00318 to 0.0634 | better |
| latency, 95th percentile (ms) | 5.75 | 5.73 | -0.3% | -0.0756 to 0.0465 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.98 | 5.81 | -2.9% | -0.968 to 0.616 | no difference beyond the noise |
| latency, mean (ms) | 1.11 | 0.922 | -17.3% | -0.421 to 0.0359 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 70.1 | +9.5% | -3.31 to 15.5 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 65.4 | +6.8% | -2.59 to 10.9 | no difference beyond the noise |
| keys evicted | 72,703 | 58,038 | -20.2% | -28,357 to -974 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.112 | -13.9% | -0.0708 to 0.0347 | no difference beyond the noise |
| host CPU-seconds | 146 | 124 | -15.0% | -86.8 to 43 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.318 | -18.2% | -0.247 to 0.105 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 16.6 to 39.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 832 | 829 | -0.3% | -11.2 to 6 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0306 to 0.0289 | same |
| cache hit rate | 0.555 | 0.553 | -0.3% | -0.00747 to 0.0041 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.1% | -0.00115 to 0.00818 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.2% | -0.000905 to 0.0282 | no difference beyond the noise |
| latency, mean (ms) | 2.61 | 2.62 | +0.5% | -0.0139 to 0.0381 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.2 | +0.2% | -0.0156 to 0.317 | no difference beyond the noise |
| memory used, mean (MB) | 60.3 | 60.2 | -0.2% | -0.746 to 0.465 | no difference beyond the noise |
| keys evicted | 185,177 | 187,327 | +1.2% | -3,325 to 7,624 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.142 | -6.6% | -0.0124 to -0.00765 | better |
| host CPU-seconds | 170 | 157 | -7.7% | -15.9 to -10.2 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.683 | 0.632 | -7.4% | -0.057 to -0.0436 | better |
| ceiling changes written (the knob's moves) | 0 | 7.67 |  | 3.87 to 11.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 2.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,129 | 1,130 | +0.1% | -5.85 to 8.28 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0658 to 0.0448 | no difference beyond the noise |
| cache hit rate | 0.754 | 0.755 | +0.1% | -0.00391 to 0.00563 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.1% | -0.0134 to 0.00358 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.27 | -0.2% | -0.0318 to 0.0122 | no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.35 | -0.6% | -0.0375 to 0.0211 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +0.9% | -1.59 to 2.69 | no difference beyond the noise |
| memory used, mean (MB) | 61.1 | 61.3 | +0.3% | -1.76 to 2.13 | no difference beyond the noise |
| keys evicted | 106,699 | 106,859 | +0.1% | -3,142 to 3,462 | shown, not judged |
| host CPU busy (share of the run) | 0.0633 | 0.0587 | -7.3% | -0.0387 to 0.0295 | no difference beyond the noise |
| host CPU-seconds | 74.4 | 68.7 | -7.7% | -48.3 to 36.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.22 | 0.203 | -7.8% | -0.143 to 0.109 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 11.1 to 23.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
