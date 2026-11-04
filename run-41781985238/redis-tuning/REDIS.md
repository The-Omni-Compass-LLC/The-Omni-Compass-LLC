# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 197 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0149 to 0.00656 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.53 | -2.2% | -0.181 to -0.0707 | GAIN |
| latency, 99th percentile (ms) | 5.73 | 5.69 | -0.7% | -0.0505 to -0.0277 | GAIN |
| latency, mean (ms) | 1.28 | 0.541 | -57.8% | -0.764 to -0.718 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +444.9% | 277 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.6% | 250 to 265 | power given |
| keys evicted | 138,135 | 2,701 | -98.0% | -137,841 to -133,027 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.121 | +0.1% | -0.0652 to 0.0655 | STEADY, no difference beyond the noise |
| host CPU-seconds | 214 | 218 | +2.0% | -130 to 139 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.402 | 0.35 | -12.9% | -0.295 to 0.191 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 212 | 183 | -13.7% | -34 to -23.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 22.9 | 20 | -12.7% | -3.7 to -2.13 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 188 | 161 | -14.5% | -31.6 to -22.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.26 |  | 1.23 to 1.3 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.201 | 0.199 | -1.3% | -0.00894 to 0.00387 | shown, not judged |
| host CPU-seconds without steal | 214 | 218 | +2.0% | -130 to 139 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
