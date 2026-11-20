# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,327 | +23.3% | 247 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00789 to 0.0133 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 5.56 | 5.49 | -1.4% | -0.0991 to -0.0529 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.6 | -0.3% | -0.0375 to -0.000727 | GAIN |
| latency, mean (ms) | 1.63 | 0.736 | -54.8% | -0.906 to -0.875 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 239 | +273.5% | 171 to 179 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,654 | 72.7 | -99.9% | -72,266 to -70,896 | shown, not judged |
| host CPU busy (share of the run) | 0.0942 | 0.0985 | +4.7% | -0.0486 to 0.0574 | STEADY, no difference beyond the noise |
| host CPU-seconds | 64.8 | 69.3 | +7.0% | -36.2 to 45.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.29 | -13.2% | -0.231 to 0.143 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 81.9 | 72.4 | -11.5% | -13.3 to -5.65 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.2 | 8.9 | -12.6% | -1.64 to -0.925 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 71.6 | 63 | -12.1% | -12.1 to -5.21 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.506 |  | 0.425 to 0.587 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0664 | 0.0636 | -4.2% | -0.0053 to -0.000284 | shown, not judged |
| host CPU-seconds without steal | 64.8 | 69.3 | +7.0% | -36.2 to 45.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 196 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00965 to 0.00677 | STEADY, the same |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 0.109 | -97.9% | -5.13 to -5.1 | GAIN |
| latency, 99th percentile (ms) | 5.27 | 5.22 | -0.8% | -0.111 to 0.022 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.88 | 0.194 | -78.0% | -0.702 to -0.67 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.8% | 272 to 274 | power given |
| memory used, mean (MB) | 61.3 | 313 | +411.2% | 252 to 252 | power given |
| keys evicted | 103,299 | 2,616 | -97.5% | -101,716 to -99,650 | shown, not judged |
| host CPU busy (share of the run) | 0.0544 | 0.0563 | +3.5% | -0.00754 to 0.0113 | STEADY, no difference beyond the noise |
| host CPU-seconds | 95 | 99.4 | +4.6% | -13.3 to 22 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.167 | 0.151 | -9.6% | -0.0496 to 0.0175 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 27.7 |  | 26.2 to 29.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 120 | 107 | -10.6% | -21.4 to -3.88 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.2 | 14.7 | -14.3% | -3.93 to -0.989 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 103 | 91.3 | -11.0% | -18.3 to -4.16 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.07 |  | 0.741 to 1.41 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.123 | 0.118 | -4.6% | -0.0128 to 0.00146 | shown, not judged |
| host CPU-seconds without steal | 95 | 99.4 | +4.6% | -13.3 to 22 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,172 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0117 to 0.0127 | STEADY, the same |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.68 | -0.6% | -0.041 to -0.0267 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.2% | -0.0324 to 0.0133 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.28 | 1.38 | -39.7% | -0.918 to -0.896 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +390.6% | 244 to 256 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,239 | 0 | -100.0% | -243,763 to -242,715 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.145 | -7.6% | -0.0423 to 0.0185 | STEADY, no difference beyond the noise |
| host CPU-seconds | 264 | 248 | -6.0% | -77.2 to 45.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.633 | 0.469 | -25.8% | -0.308 to -0.0186 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 19 to 19 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 322 | 283 | -12.0% | -41.4 to -36 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.1 | 32.6 | -12.2% | -5.96 to -3.07 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 285 | 249 | -12.7% | -38 to -34.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.87 |  | 1.6 to 2.14 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.244 | 0.232 | -5.1% | -0.0186 to -0.00616 | shown, not judged |
| host CPU-seconds without steal | 264 | 248 | -6.0% | -77.2 to 45.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.2% | 198 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00705 to -0.000293 | LOSS |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.43 | -1.8% | -0.119 to -0.085 | GAIN |
| latency, 99th percentile (ms) | 5.6 | 5.57 | -0.5% | -0.0321 to -0.0239 | GAIN |
| latency, mean (ms) | 1.25 | 0.521 | -58.2% | -0.749 to -0.702 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 347 | +442.3% | 272 to 294 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,226 | 2,703 | -98.0% | -137,739 to -133,307 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.0974 | -8.8% | -0.039 to 0.0202 | STEADY, no difference beyond the noise |
| host CPU-seconds | 188 | 172 | -8.4% | -73.1 to 41.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.352 | 0.275 | -21.8% | -0.18 to 0.0266 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 194 | 174 | -10.6% | -25.4 to -16 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.2 | 21.3 | -12.0% | -3.09 to -2.69 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 170 | 151 | -11.2% | -23.3 to -14.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.18 |  | 0.949 to 1.4 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.16 | -2.1% | -0.00608 to -0.000955 | shown, not judged |
| host CPU-seconds without steal | 188 | 172 | -8.4% | -73.1 to 41.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
