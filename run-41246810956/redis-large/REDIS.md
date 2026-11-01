# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `4082deec8fda`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 195 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.011 to -0.000442 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.229 | -96.0% | -5.51 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.73 | -1.2% | -0.0751 to -0.0684 | GAIN |
| latency, mean (ms) | 1.04 | 0.303 | -71.0% | -0.758 to -0.722 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +428.2% | 271 to 278 | power given |
| memory used, mean (MB) | 61.3 | 314 | +411.7% | 248 to 257 | power given |
| keys evicted | 103,483 | 2,569 | -97.5% | -102,384 to -99,445 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.118 | -11.0% | -0.103 to 0.0738 | STEADY, no difference beyond the noise |
| host CPU-seconds | 225 | 203 | -9.9% | -194 to 150 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.395 | 0.307 | -22.1% | -0.369 to 0.194 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 275 | 240 | -12.9% | -41.2 to -29.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.4 | 31.7 | -10.4% | -4.99 to -2.37 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 240 | 206 | -13.9% | -38.2 to -28.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.5 |  | 1.26 to 1.74 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.227 | 0.218 | -3.9% | -0.0169 to -0.000713 | shown, not judged |
| host CPU-seconds without steal | 225 | 203 | -9.9% | -194 to 150 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
