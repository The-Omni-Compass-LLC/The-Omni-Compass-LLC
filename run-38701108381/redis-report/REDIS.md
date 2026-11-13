# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.78 to 1.3 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0568 to 0.0954 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00146 to 0.00114 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% | 0.000237 to 0.0083 | LOSS |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.2% | 0.00476 to 0.0203 | LOSS |
| latency, mean (ms) | 1.74 | 1.75 | +0.4% | -0.00419 to 0.017 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 60.9 | -4.9% | -3.38 to -2.87 | GAIN |
| memory used, mean (MB) | 57.2 | 55 | -3.8% | -2.29 to -2.04 | GAIN |
| keys evicted | 71,705 | 71,758 | +0.1% | -264 to 369 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.139 | +25.4% | -0.0346 to 0.0909 | EVEN, no difference beyond the noise |
| host CPU-seconds | 72.4 | 93.5 | +29.1% | -26.8 to 69 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.374 | 0.483 | +29.2% | -0.139 to 0.357 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,313 | +3.7% | -4.58 to 97.7 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000885 to 0.00384 | EVEN, the same |
| cache hit rate | 0.845 | 0.876 | +3.7% | -0.00283 to 0.0652 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0428 to 0.0224 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.82 | -0.0% | -0.0378 to 0.0374 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.887 | -16.1% | -0.367 to 0.0258 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.6 | +5.6% | -4.3 to 11.5 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 63.8 | +4.0% | -5.3 to 10.2 | EVEN, no difference beyond the noise |
| keys evicted | 103,531 | 83,020 | -19.8% | -43,975 to 2,951 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.123 | +4.1% | -0.0105 to 0.0201 | EVEN, no difference beyond the noise |
| host CPU-seconds | 196 | 207 | +5.4% | -20 to 41.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.344 | 0.35 | +1.7% | -0.0362 to 0.0476 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 33.3 |  | 19.2 to 47.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -1.72 to -1.48 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0856 to 0.0364 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00107 to -0.000854 | LOSS |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.1% | -0.00334 to 0.0101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% | 0.0129 to 0.0205 | LOSS |
| latency, mean (ms) | 2.26 | 2.27 | +0.4% | 0.00577 to 0.0139 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.551 to 1.19 | power given |
| memory used, mean (MB) | 60.7 | 60.6 | -0.1% | -0.816 to 0.695 | EVEN, no difference beyond the noise |
| keys evicted | 243,122 | 244,896 | +0.7% | -2,801 to 6,349 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.138 | -4.4% | -0.0355 to 0.0228 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 230 | -5.3% | -69.9 to 44.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.582 | 0.552 | -5.1% | -0.167 to 0.107 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23.3 |  | 17.1 to 29.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,250 | +5.6% | 59.5 to 73.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00185 to 0.00692 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.834 | +5.6% | 0.0396 to 0.049 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0163 to 0.00346 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.012 to 0.0206 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.1 | -18.1% | -0.263 to -0.226 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 86.4 | +35.0% | 19.7 to 25.1 | power given |
| memory used, mean (MB) | 61.2 | 79 | +29.1% | 17.4 to 18.2 | power given |
| keys evicted | 138,104 | 109,313 | -20.8% | -31,335 to -26,247 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.116 | -9.0% | -0.0425 to 0.0196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 194 | -9.4% | -77.4 to 37.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.401 | 0.344 | -14.2% | -0.157 to 0.0425 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 48.3 |  | 37.1 to 59.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
