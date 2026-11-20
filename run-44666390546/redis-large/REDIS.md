# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 196 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00965 to 0.00677 | STEADY, the same |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 0.109 | -97.9% | -5.13 to -5.1 | GAIN |
| latency, 99th percentile (ms) | 5.27 | 5.22 | -0.8% | -0.111 to 0.022 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.88 | 0.194 | -78.0% | -0.702 to -0.67 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.8% | 272 to 274 | power given |
| memory used, mean (MB) | 61.3 | 313 | +411.2% | 252 to 252 | power given |
| keys evicted | 103,299 | 2,616 | -97.5% | -101,716 to -99,650 | shown, not judged |
| host CPU busy (share of the run) | 0.0544 | 0.0563 | +3.5% | -0.00754 to 0.0113 | STEADY, no difference beyond the noise |
| host CPU-seconds | 95 | 99.4 | +4.6% | -13.3 to 22 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.167 | 0.151 | -9.6% | -0.0496 to 0.0175 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 27.7 |  | 26.2 to 29.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 120 | 107 | -10.6% | -21.4 to -3.88 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.2 | 14.7 | -14.3% | -3.93 to -0.989 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 103 | 91.3 | -11.0% | -18.3 to -4.16 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.07 |  | 0.741 to 1.41 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.123 | 0.118 | -4.6% | -0.0128 to 0.00146 | shown, not judged |
| host CPU-seconds without steal | 95 | 99.4 | +4.6% | -13.3 to 22 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
