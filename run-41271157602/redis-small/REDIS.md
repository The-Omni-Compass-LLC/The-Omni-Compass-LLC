# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.7% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0303 to 0.0338 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.5% | -0.0517 to -0.00257 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.75 | -0.3% | -0.0983 to 0.065 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 1.37 | -39.8% | -0.925 to -0.881 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +389.0% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,172 | 0 | -100.0% | -243,652 to -242,692 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.127 | -17.8% | -0.053 to -0.00207 | GAIN |
| host CPU-seconds | 262 | 214 | -18.2% | -96.1 to 0.706 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.628 | 0.405 | -35.5% | -0.334 to -0.111 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 19 to 19 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 315 | 281 | -10.7% | -43.9 to -23.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.4 | 32.3 | -11.4% | -6.4 to -1.87 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 279 | 247 | -11.2% | -38.9 to -23.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.53 |  | 1.33 to 1.72 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.237 | 0.228 | -3.9% | -0.0167 to -0.00176 | shown, not judged |
| host CPU-seconds without steal | 262 | 214 | -18.2% | -96.1 to 0.706 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
