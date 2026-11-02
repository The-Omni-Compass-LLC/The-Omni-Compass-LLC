# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.7% | 197 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00849 to 0.00596 | STEADY, the same |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 0.18 | -96.7% | -5.37 to -5.34 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.49 | -2.3% | -0.148 to -0.111 | GAIN |
| latency, mean (ms) | 0.972 | 0.255 | -73.8% | -0.731 to -0.705 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.4% | 273 to 274 | power given |
| memory used, mean (MB) | 61.3 | 313 | +411.4% | 252 to 252 | power given |
| keys evicted | 103,430 | 2,631 | -97.5% | -101,579 to -100,019 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.0928 | -10.3% | -0.0289 to 0.00762 | STEADY, no difference beyond the noise |
| host CPU-seconds | 180 | 163 | -9.7% | -52.7 to 17.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.317 | 0.247 | -22.0% | -0.12 to -0.0187 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 28 to 28 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 199 | 175 | -11.9% | -27.8 to -19.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 26.3 | 23.1 | -12.4% | -3.97 to -2.54 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 173 | 151 | -12.6% | -25.9 to -17.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.23 |  | 0.893 to 1.57 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.172 | 0.168 | -2.6% | -0.0105 to 0.0017 | shown, not judged |
| host CPU-seconds without steal | 180 | 163 | -9.7% | -52.7 to 17.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
