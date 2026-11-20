# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.7% | 196 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00889 to -0.00345 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.266 | -95.4% | -5.51 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.84 | 5.75 | -1.4% | -0.102 to -0.0642 | GAIN |
| latency, mean (ms) | 1.06 | 0.318 | -70.1% | -0.761 to -0.729 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +428.0% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +411.2% | 248 to 256 | power given |
| keys evicted | 103,578 | 2,596 | -97.5% | -102,674 to -99,290 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.119 | -17.7% | -0.0907 to 0.0397 | STEADY, no difference beyond the noise |
| host CPU-seconds | 245 | 202 | -17.4% | -167 to 82.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.429 | 0.307 | -28.6% | -0.317 to 0.0721 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 25.5 to 31.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 289 | 252 | -13.0% | -42.1 to -33 | GAIN |
| the server's own CPU-seconds (redis-server) | 38 | 33.9 | -10.7% | -6.35 to -1.79 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 251 | 216 | -14.0% | -37.8 to -32.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.69 |  | 1.43 to 1.95 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.24 | 0.232 | -3.0% | -0.011 to -0.00348 | shown, not judged |
| host CPU-seconds without steal | 245 | 202 | -17.4% | -167 to 82.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
