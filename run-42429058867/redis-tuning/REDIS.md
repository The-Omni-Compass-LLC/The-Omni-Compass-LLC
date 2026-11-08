# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.2% | 196 to 210 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0291 to 0.00614 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.68 | -1.0% | -0.0617 to -0.0526 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.76 | -0.6% | -0.0358 to -0.0285 | GAIN |
| latency, mean (ms) | 1.34 | 0.585 | -56.3% | -0.785 to -0.727 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +447.6% | 273 to 300 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.6% | 244 to 274 | power given |
| keys evicted | 138,175 | 2,385 | -98.3% | -139,248 to -132,331 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.112 | -13.7% | -0.0497 to 0.0144 | STEADY, no difference beyond the noise |
| host CPU-seconds | 217 | 189 | -12.8% | -88.3 to 32.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.407 | 0.303 | -25.6% | -0.212 to 0.00367 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 286 | 248 | -13.1% | -42.6 to -32.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.4 | 31.2 | -9.5% | -4.17 to -2.35 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 251 | 215 | -14.2% | -40.2 to -31.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.6 |  | 1.31 to 1.88 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.23 | 0.217 | -5.6% | -0.0142 to -0.0116 | shown, not judged |
| host CPU-seconds without steal | 217 | 189 | -12.8% | -88.3 to 32.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
