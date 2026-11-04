# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 199 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.053 to 0.0173 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.62 | -1.0% | -0.0601 to -0.0486 | GAIN |
| latency, 99th percentile (ms) | 5.73 | 5.71 | -0.4% | -0.0281 to -0.0175 | GAIN |
| latency, mean (ms) | 1.32 | 0.567 | -56.9% | -0.766 to -0.731 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +445.5% | 278 to 292 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,067 | 2,694 | -98.0% | -137,167 to -133,578 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.113 | -14.0% | -0.0687 to 0.0319 | STEADY, no difference beyond the noise |
| host CPU-seconds | 227 | 197 | -13.1% | -127 to 67.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.426 | 0.316 | -25.8% | -0.266 to 0.0459 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 259 | 224 | -13.3% | -37.3 to -31.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 31.2 | 27.1 | -13.2% | -4.62 to -3.6 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 227 | 196 | -13.9% | -35.1 to -28.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.42 |  | 1.18 to 1.66 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.219 | 0.21 | -4.3% | -0.0104 to -0.00858 | shown, not judged |
| host CPU-seconds without steal | 227 | 197 | -13.1% | -127 to 67.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
