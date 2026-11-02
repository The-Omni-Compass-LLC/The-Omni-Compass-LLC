# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.7% | 198 to 199 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0218 to 0.00761 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.248 | -95.7% | -5.52 to -5.49 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.74 | -1.4% | -0.119 to -0.0441 | GAIN |
| latency, mean (ms) | 1.06 | 0.312 | -70.5% | -0.756 to -0.734 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.1% | 272 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 249 to 254 | power given |
| keys evicted | 103,603 | 2,694 | -97.4% | -101,506 to -100,312 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.109 | -29.0% | -0.08 to -0.00939 | GAIN |
| host CPU-seconds | 266 | 184 | -30.6% | -151 to -11.4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.466 | 0.28 | -40.0% | -0.304 to -0.0688 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 286 | 247 | -13.6% | -46.1 to -31.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.7 | 33.3 | -11.7% | -6.26 to -2.55 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 248 | 212 | -14.6% | -42.3 to -30.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.69 |  | 1.42 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.238 | 0.23 | -3.4% | -0.014 to -0.00226 | shown, not judged |
| host CPU-seconds without steal | 266 | 184 | -30.6% | -151 to -11.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
