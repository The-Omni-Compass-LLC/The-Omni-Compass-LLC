# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.2% | 198 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00705 to -0.000293 | LOSS |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.43 | -1.8% | -0.119 to -0.085 | GAIN |
| latency, 99th percentile (ms) | 5.6 | 5.57 | -0.5% | -0.0321 to -0.0239 | GAIN |
| latency, mean (ms) | 1.25 | 0.521 | -58.2% | -0.749 to -0.702 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 347 | +442.3% | 272 to 294 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,226 | 2,703 | -98.0% | -137,739 to -133,307 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.0974 | -8.8% | -0.039 to 0.0202 | STEADY, no difference beyond the noise |
| host CPU-seconds | 188 | 172 | -8.4% | -73.1 to 41.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.352 | 0.275 | -21.8% | -0.18 to 0.0266 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 194 | 174 | -10.6% | -25.4 to -16 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.2 | 21.3 | -12.0% | -3.09 to -2.69 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 170 | 151 | -11.2% | -23.3 to -14.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.18 |  | 0.949 to 1.4 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.16 | -2.1% | -0.00608 to -0.000955 | shown, not judged |
| host CPU-seconds without steal | 188 | 172 | -8.4% | -73.1 to 41.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
