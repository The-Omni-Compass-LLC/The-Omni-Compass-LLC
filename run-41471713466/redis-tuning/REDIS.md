# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.2% | 196 to 211 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0165 to 0.00611 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.69 | -1.0% | -0.076 to -0.034 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.78 | -0.4% | -0.0552 to 0.00317 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 0.593 | -56.2% | -0.797 to -0.722 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +447.5% | 273 to 300 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,309 | 2,371 | -98.3% | -139,160 to -132,717 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.12 | -18.5% | -0.0607 to 0.00611 | STEADY, no difference beyond the noise |
| host CPU-seconds | 251 | 204 | -18.8% | -112 to 17.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.471 | 0.326 | -30.7% | -0.264 to -0.0258 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 17 to 17 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 290 | 254 | -12.5% | -44.7 to -27.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.4 | 31.1 | -12.0% | -5 to -3.48 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 221 | -13.2% | -41.4 to -26.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.64 |  | 1.45 to 1.83 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.226 | -3.5% | -0.0256 to 0.00917 | shown, not judged |
| host CPU-seconds without steal | 251 | 204 | -18.8% | -112 to 17.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
