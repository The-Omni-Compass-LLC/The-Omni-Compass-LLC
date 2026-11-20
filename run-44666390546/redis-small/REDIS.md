# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
