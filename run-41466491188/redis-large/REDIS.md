# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.7% | 198 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00515 to -0.00198 | LOSS |
| cache hit rate | 0.844 | 0.978 | +15.8% | 0.132 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.233 | -95.9% | -5.52 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.73 | -1.3% | -0.0994 to -0.0572 | GAIN |
| latency, mean (ms) | 1.05 | 0.308 | -70.7% | -0.75 to -0.736 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.9% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.0% | 249 to 254 | power given |
| keys evicted | 103,704 | 2,688 | -97.4% | -102,005 to -100,027 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.102 | -18.8% | -0.0815 to 0.0343 | STEADY, no difference beyond the noise |
| host CPU-seconds | 211 | 172 | -18.4% | -150 to 72.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.37 | 0.261 | -29.5% | -0.288 to 0.0698 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 27.9 to 30.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 281 | 243 | -13.6% | -45.2 to -31 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.6 | 32.9 | -10.1% | -4.25 to -3.15 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 244 | 208 | -14.7% | -42.6 to -29.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.48 |  | 0.979 to 1.98 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.229 | 0.214 | -6.5% | -0.0246 to -0.00532 | shown, not judged |
| host CPU-seconds without steal | 211 | 172 | -18.4% | -150 to 72.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
