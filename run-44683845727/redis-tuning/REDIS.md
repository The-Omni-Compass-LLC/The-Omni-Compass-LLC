# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,387 | +17.2% | 196 to 211 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0398 to 0.038 | STEADY, the same |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.69 | -1.1% | -0.0839 to -0.0411 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.78 | -0.6% | -0.0543 to -0.0141 | GAIN |
| latency, mean (ms) | 1.35 | 0.592 | -56.3% | -0.8 to -0.726 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +447.8% | 273 to 300 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,351 | 2,405 | -98.3% | -139,487 to -132,405 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.112 | -25.5% | -0.0413 to -0.0351 | GAIN |
| host CPU-seconds | 255 | 188 | -26.4% | -73.5 to -61.1 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.479 | 0.301 | -37.2% | -0.197 to -0.159 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 293 | 252 | -13.8% | -46.5 to -34.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.8 | 31.9 | -11.0% | -6.95 to -0.904 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 257 | 219 | -14.8% | -41.3 to -34.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.58 |  | 1.35 to 1.81 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.238 | 0.227 | -4.6% | -0.0162 to -0.0059 | shown, not judged |
| host CPU-seconds without steal | 255 | 188 | -26.4% | -73.4 to -61.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
