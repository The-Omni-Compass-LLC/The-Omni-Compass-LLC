# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,386 | +17.2% | 196 to 211 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.111 to 0.104 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.926 | +17.3% | 0.132 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.2 | -0.3% | -0.0276 to -0.00767 | GAIN |
| latency, 99th percentile (ms) | 5.26 | 5.24 | -0.5% | -0.0502 to -0.00177 | GAIN |
| latency, mean (ms) | 1.17 | 0.469 | -60.0% | -0.744 to -0.663 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +447.1% | 271 to 301 | power given |
| memory used, mean (MB) | 61.2 | 322 | +425.9% | 246 to 275 | power given |
| keys evicted | 138,253 | 2,050 | -98.5% | -138,818 to -133,588 | shown, not judged |
| host CPU busy (share of the run) | 0.053 | 0.0495 | -6.7% | -0.0457 to 0.0386 | STEADY, no difference beyond the noise |
| host CPU-seconds | 92.5 | 86.4 | -6.6% | -82.8 to 70.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.174 | 0.139 | -20.3% | -0.172 to 0.102 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.7 |  | 15.5 to 25.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 121 | 113 | -7.0% | -14.4 to -2.59 | GAIN |
| the server's own CPU-seconds (redis-server) | 16.6 | 14.5 | -12.4% | -2.27 to -1.87 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 104 | 96.7 | -7.3% | -13 to -2.15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.16 |  | 0.808 to 1.52 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.124 | 0.118 | -4.8% | -0.0091 to -0.00274 | shown, not judged |
| host CPU-seconds without steal | 92.5 | 86.4 | -6.6% | -82.8 to 70.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
