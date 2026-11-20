# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 199 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0309 to 0.00146 | STEADY, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.1% | 0.132 to 0.137 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 5.44 | -1.9% | -0.116 to -0.0949 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.4% | -0.0311 to -0.0182 | GAIN |
| latency, mean (ms) | 1.25 | 0.524 | -58.0% | -0.737 to -0.71 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 348 | +443.5% | 275 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.8% | 250 to 265 | power given |
| keys evicted | 137,980 | 2,674 | -98.1% | -137,013 to -133,599 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.0847 | -24.3% | -0.123 to 0.0685 | STEADY, no difference beyond the noise |
| host CPU-seconds | 197 | 148 | -25.2% | -234 to 135 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.371 | 0.237 | -36.1% | -0.45 to 0.183 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 15.5 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 196 | 175 | -10.8% | -23.6 to -19 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.7 | 21.8 | -11.5% | -3.49 to -2.18 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 172 | 152 | -11.5% | -21.4 to -18 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.22 |  | 1.03 to 1.4 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.167 | 0.165 | -1.1% | -0.00708 to 0.00325 | shown, not judged |
| host CPU-seconds without steal | 197 | 148 | -25.1% | -234 to 135 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
