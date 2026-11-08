# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 197 to 209 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.055 to 0.00837 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.77 | 5.7 | -1.1% | -0.0889 to -0.0387 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.8 | -0.4% | -0.0586 to 0.0073 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 0.598 | -55.8% | -0.785 to -0.727 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +448.1% | 275 to 299 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.6% | 244 to 274 | power given |
| keys evicted | 138,155 | 2,395 | -98.3% | -138,729 to -132,791 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.132 | -9.5% | -0.0179 to -0.0099 | GAIN |
| host CPU-seconds | 245 | 225 | -8.2% | -29.8 to -10.4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.461 | 0.361 | -21.6% | -0.106 to -0.093 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 17 to 17 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 299 | 260 | -12.8% | -47.4 to -29.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.7 | 32.3 | -12.0% | -6.08 to -2.75 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 262 | 226 | -13.7% | -43.8 to -27.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.93 |  | 1.3 to 2.57 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.245 | 0.239 | -2.5% | -0.0165 to 0.00424 | shown, not judged |
| host CPU-seconds without steal | 245 | 225 | -8.2% | -29.8 to -10.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
