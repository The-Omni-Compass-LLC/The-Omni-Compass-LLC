# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.2% | 199 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0172 to 0.00671 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.133 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 5.44 | -1.8% | -0.111 to -0.0907 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.4% | -0.0266 to -0.0196 | GAIN |
| latency, mean (ms) | 1.25 | 0.527 | -57.9% | -0.74 to -0.708 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +444.6% | 275 to 294 | power given |
| memory used, mean (MB) | 61.2 | 320 | +422.4% | 252 to 265 | power given |
| keys evicted | 138,378 | 2,448 | -98.2% | -137,942 to -133,917 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.105 | +3.2% | -0.0186 to 0.0252 | STEADY, no difference beyond the noise |
| host CPU-seconds | 177 | 186 | +5.1% | -33.2 to 51.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.332 | 0.298 | -10.3% | -0.111 to 0.0426 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 197 | 177 | -9.9% | -21.1 to -17.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.2 | 21.6 | -10.7% | -2.91 to -2.24 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 172 | 154 | -10.5% | -19.8 to -16.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.25 |  | 1.04 to 1.45 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.169 | 0.168 | -0.6% | -0.00629 to 0.00422 | shown, not judged |
| host CPU-seconds without steal | 177 | 186 | +5.1% | -33.2 to 51.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
