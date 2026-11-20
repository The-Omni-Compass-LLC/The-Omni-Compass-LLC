# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.3% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00818 to 0.0157 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.57 | 5.47 | -1.8% | -0.114 to -0.0843 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.6 | -0.3% | -0.0254 to -0.0113 | GAIN |
| latency, mean (ms) | 1.63 | 0.738 | -54.8% | -0.914 to -0.877 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 240 | +274.4% | 168 to 183 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,704 | 72.7 | -99.9% | -72,643 to -70,620 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0925 | -17.0% | -0.0605 to 0.0226 | STEADY, no difference beyond the noise |
| host CPU-seconds | 78 | 64.7 | -17.0% | -45.2 to 18.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.402 | 0.271 | -32.7% | -0.271 to 0.00758 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 82.9 | 72.3 | -12.9% | -11.8 to -9.59 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.1 | 9.02 | -11.1% | -1.36 to -0.882 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 72.7 | 62.7 | -13.8% | -11 to -9.15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.502 |  | 0.406 to 0.598 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0671 | 0.0645 | -3.9% | -0.00353 to -0.00172 | shown, not judged |
| host CPU-seconds without steal | 78 | 64.7 | -17.0% | -45.2 to 18.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 198 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.000504 to 2.38e-05 | STEADY, the same |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.63 | 0.226 | -96.0% | -5.42 to -5.39 | GAIN |
| latency, 99th percentile (ms) | 5.73 | 5.61 | -2.1% | -0.133 to -0.11 | GAIN |
| latency, mean (ms) | 0.993 | 0.266 | -73.2% | -0.73 to -0.724 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.7% | 272 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.2% | 249 to 254 | power given |
| keys evicted | 103,463 | 2,691 | -97.4% | -101,347 to -100,199 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.117 | -4.5% | -0.0518 to 0.0407 | STEADY, no difference beyond the noise |
| host CPU-seconds | 217 | 209 | -3.7% | -101 to 85.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.381 | 0.317 | -16.8% | -0.228 to 0.1 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 222 | 197 | -11.0% | -29.3 to -19.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.1 | 22.4 | -10.6% | -3.7 to -1.61 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 196 | 173 | -11.7% | -26.8 to -19 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.17 |  | 1.02 to 1.31 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.182 | 0.182 | +0.0% | -0.0084 to 0.00853 | shown, not judged |
| host CPU-seconds without steal | 217 | 209 | -3.7% | -101 to 85.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,174 | +26.8% | 247 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0259 to 0.0198 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.43 | -1.5% | -0.0937 to -0.0721 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.6 | -0.4% | -0.0231 to -0.0191 | GAIN |
| latency, mean (ms) | 2.11 | 1.24 | -41.0% | -0.872 to -0.858 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +388.0% | 243 to 253 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,300 | 0 | -100.0% | -243,675 to -242,925 | shown, not judged |
| host CPU busy (share of the run) | 0.0982 | 0.0839 | -14.5% | -0.0609 to 0.0323 | STEADY, no difference beyond the noise |
| host CPU-seconds | 175 | 148 | -15.0% | -116 to 64 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.419 | 0.281 | -33.0% | -0.351 to 0.0747 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 14.7 to 23.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 177 | 159 | -9.9% | -20.4 to -14.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 21.5 | 19.3 | -10.0% | -3.01 to -1.27 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 155 | 139 | -10.6% | -18.7 to -14.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.07 |  | 1.02 to 1.13 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.173 | 0.165 | -4.5% | -0.011 to -0.00462 | shown, not judged |
| host CPU-seconds without steal | 175 | 148 | -15.0% | -116 to 64 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,386 | +17.2% | 196 to 211 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.111 to 0.104 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.926 | +17.3% | 0.132 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.2 | -0.3% | -0.0276 to -0.00767 | GAIN |
| latency, 99th percentile (ms) | 5.26 | 5.24 | -0.5% | -0.0502 to -0.00177 | GAIN |
| latency, mean (ms) | 1.17 | 0.469 | -60.0% | -0.744 to -0.663 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +447.1% | 271 to 301 | power given |
| memory used, mean (MB) | 61.2 | 322 | +425.9% | 246 to 275 | power given |
| keys evicted | 138,253 | 2,050 | -98.5% | -138,818 to -133,588 | shown, not judged |
| host CPU busy (share of the run) | 0.053 | 0.0495 | -6.7% | -0.0457 to 0.0386 | STEADY, no difference beyond the noise |
| host CPU-seconds | 92.5 | 86.4 | -6.6% | -82.8 to 70.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.174 | 0.139 | -20.3% | -0.172 to 0.102 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.7 |  | 15.5 to 25.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 121 | 113 | -7.0% | -14.4 to -2.59 | GAIN |
| the server's own CPU-seconds (redis-server) | 16.6 | 14.5 | -12.4% | -2.27 to -1.87 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 104 | 96.7 | -7.3% | -13 to -2.15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.16 |  | 0.808 to 1.52 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.124 | 0.118 | -4.8% | -0.0091 to -0.00274 | shown, not judged |
| host CPU-seconds without steal | 92.5 | 86.4 | -6.6% | -82.8 to 70.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
