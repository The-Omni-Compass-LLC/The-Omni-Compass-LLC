# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.7% | 197 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0132 to 0.00199 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.8% | 0.132 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.247 | -95.7% | -5.51 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.74 | -1.4% | -0.0882 to -0.07 | GAIN |
| latency, mean (ms) | 1.06 | 0.314 | -70.3% | -0.755 to -0.733 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +428.1% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 314 | +411.8% | 248 to 257 | power given |
| keys evicted | 103,625 | 2,579 | -97.5% | -102,070 to -100,022 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.113 | -26.5% | -0.0624 to -0.0189 | GAIN |
| host CPU-seconds | 264 | 191 | -27.8% | -116 to -30.7 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.464 | 0.29 | -37.6% | -0.244 to -0.104 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 287 | 249 | -13.1% | -40.7 to -34.6 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.9 | 34.2 | -9.7% | -4.46 to -2.91 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 248 | 213 | -14.3% | -38.7 to -32.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.58 |  | 1.27 to 1.88 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.225 | -3.6% | -0.0128 to -0.00394 | shown, not judged |
| host CPU-seconds without steal | 264 | 191 | -27.8% | -116 to -30.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
