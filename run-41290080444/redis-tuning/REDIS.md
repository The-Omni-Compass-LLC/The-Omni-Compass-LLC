# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.1% | 199 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0442 to 0.0127 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.69 | -0.9% | -0.0583 to -0.0446 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.78 | -0.4% | -0.0406 to -0.00804 | GAIN |
| latency, mean (ms) | 1.35 | 0.595 | -55.9% | -0.761 to -0.749 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +446.3% | 278 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.8% | 250 to 265 | power given |
| keys evicted | 138,224 | 2,715 | -98.0% | -137,450 to -133,568 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.112 | -28.5% | -0.0585 to -0.0306 | GAIN |
| host CPU-seconds | 270 | 188 | -30.2% | -108 to -55.1 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.507 | 0.302 | -40.4% | -0.25 to -0.159 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 287 | 252 | -12.1% | -40.8 to -28.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.7 | 30.9 | -11.0% | -4.42 to -3.18 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 252 | 219 | -12.9% | -38.7 to -26.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.66 |  | 1.39 to 1.93 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.23 | 0.223 | -3.4% | -0.012 to -0.00352 | shown, not judged |
| host CPU-seconds without steal | 270 | 188 | -30.2% | -108 to -55.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
