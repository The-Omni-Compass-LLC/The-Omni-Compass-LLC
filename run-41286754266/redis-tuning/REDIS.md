# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 197 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00901 to 0.00164 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.51 | -2.3% | -0.172 to -0.0823 | GAIN |
| latency, 99th percentile (ms) | 5.72 | 5.68 | -0.7% | -0.0667 to -0.00848 | GAIN |
| latency, mean (ms) | 1.27 | 0.538 | -57.7% | -0.762 to -0.707 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +444.9% | 277 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.6% | 250 to 265 | power given |
| keys evicted | 138,156 | 2,695 | -98.0% | -137,981 to -132,941 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.113 | -7.8% | -0.0614 to 0.0425 | STEADY, no difference beyond the noise |
| host CPU-seconds | 218 | 203 | -7.1% | -118 to 87.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.409 | 0.325 | -20.7% | -0.263 to 0.0943 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 205 | 180 | -12.3% | -37.5 to -12.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 22.4 | 19.9 | -11.2% | -3.31 to -1.71 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 182 | 158 | -13.1% | -35.4 to -12.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.24 |  | 1.18 to 1.31 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.2 | 0.197 | -1.9% | -0.0183 to 0.0108 | shown, not judged |
| host CPU-seconds without steal | 218 | 203 | -7.1% | -118 to 87.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
