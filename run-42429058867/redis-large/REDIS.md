# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.7% | 195 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0127 to 0.00479 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.252 | -95.6% | -5.51 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.75 | -1.4% | -0.0988 to -0.0618 | GAIN |
| latency, mean (ms) | 1.06 | 0.316 | -70.1% | -0.753 to -0.732 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.5% | 270 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +411.0% | 248 to 256 | power given |
| keys evicted | 103,605 | 2,644 | -97.4% | -101,967 to -99,955 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.126 | -7.0% | -0.0449 to 0.0259 | STEADY, no difference beyond the noise |
| host CPU-seconds | 229 | 217 | -5.3% | -80.5 to 56.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.401 | 0.328 | -18.1% | -0.194 to 0.0485 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 290 | 252 | -13.1% | -39.2 to -37.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.5 | 33.5 | -10.7% | -5.11 to -2.95 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 253 | 217 | -14.2% | -36.4 to -35.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.72 |  | 1.46 to 1.99 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.261 | 0.255 | -2.3% | -0.00877 to -0.00313 | shown, not judged |
| host CPU-seconds without steal | 229 | 217 | -5.3% | -80.5 to 56.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
