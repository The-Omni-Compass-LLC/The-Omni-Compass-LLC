# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,464 | +15.6% | 197 to 199 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00665 to 0.00416 | STEADY, the same |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.133 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.268 | -95.4% | -5.56 to -5.43 | GAIN |
| latency, 99th percentile (ms) | 5.84 | 5.75 | -1.6% | -0.126 to -0.0602 | GAIN |
| latency, mean (ms) | 1.06 | 0.317 | -70.2% | -0.753 to -0.737 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.6% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.5% | 248 to 254 | power given |
| keys evicted | 103,593 | 2,770 | -97.3% | -100,958 to -100,687 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.109 | -25.7% | -0.0578 to -0.0173 | GAIN |
| host CPU-seconds | 249 | 183 | -26.6% | -107 to -25.9 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.437 | 0.278 | -36.5% | -0.228 to -0.0912 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 291 | 252 | -13.3% | -41.9 to -35.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.8 | 34 | -12.2% | -5.65 to -3.79 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 252 | 216 | -14.1% | -38.2 to -32.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.63 |  | 1.28 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.232 | -3.1% | -0.0114 to -0.00347 | shown, not judged |
| host CPU-seconds without steal | 249 | 183 | -26.6% | -107 to -25.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
