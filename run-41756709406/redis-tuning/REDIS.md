# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 195 to 210 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.059 to 0.0212 | STEADY, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.2% | 0.131 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.68 | -0.9% | -0.0619 to -0.0437 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.77 | -0.4% | -0.0349 to -0.0101 | GAIN |
| latency, mean (ms) | 1.34 | 0.586 | -56.2% | -0.78 to -0.723 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +446.9% | 272 to 300 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,004 | 2,386 | -98.3% | -138,976 to -132,260 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.106 | -23.3% | -0.0509 to -0.0134 | GAIN |
| host CPU-seconds | 234 | 178 | -23.9% | -90.2 to -21.6 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.438 | 0.285 | -35.0% | -0.2 to -0.107 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 285 | 249 | -12.3% | -37 to -33.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 35 | 31.2 | -10.8% | -3.97 to -3.61 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 249 | 216 | -13.2% | -34.5 to -31.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.51 |  | 1.16 to 1.85 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.226 | 0.217 | -4.0% | -0.0183 to 0.000374 | shown, not judged |
| host CPU-seconds without steal | 234 | 178 | -23.9% | -90.2 to -21.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
