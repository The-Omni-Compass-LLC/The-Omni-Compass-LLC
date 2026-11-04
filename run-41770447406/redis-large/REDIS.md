# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.6% | 197 to 198 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00554 to -0.00243 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.242 | -95.8% | -5.53 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.74 | -1.4% | -0.116 to -0.0499 | GAIN |
| latency, mean (ms) | 1.05 | 0.31 | -70.6% | -0.747 to -0.737 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.6% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.7% | 248 to 255 | power given |
| keys evicted | 103,286 | 2,645 | -97.4% | -101,061 to -100,221 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.106 | -29.7% | -0.073 to -0.0161 | GAIN |
| host CPU-seconds | 259 | 178 | -31.0% | -134 to -26.6 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.453 | 0.271 | -40.3% | -0.266 to -0.0993 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 284 | 244 | -14.0% | -50.2 to -29.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.1 | 32.4 | -12.7% | -5.88 to -3.58 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 246 | 210 | -14.8% | -46.4 to -26.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.6 |  | 1.23 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.232 | 0.223 | -3.6% | -0.0229 to 0.00607 | shown, not judged |
| host CPU-seconds without steal | 259 | 178 | -31.0% | -134 to -26.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
