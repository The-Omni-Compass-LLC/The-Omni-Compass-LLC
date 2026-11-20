# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 198 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.000504 to 2.38e-05 | STEADY, the same |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.63 | 0.226 | -96.0% | -5.42 to -5.39 | GAIN |
| latency, 99th percentile (ms) | 5.73 | 5.61 | -2.1% | -0.133 to -0.11 | GAIN |
| latency, mean (ms) | 0.993 | 0.266 | -73.2% | -0.73 to -0.724 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.7% | 272 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.2% | 249 to 254 | power given |
| keys evicted | 103,463 | 2,691 | -97.4% | -101,347 to -100,199 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.117 | -4.5% | -0.0518 to 0.0407 | STEADY, no difference beyond the noise |
| host CPU-seconds | 217 | 209 | -3.7% | -101 to 85.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.381 | 0.317 | -16.8% | -0.228 to 0.1 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 222 | 197 | -11.0% | -29.3 to -19.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.1 | 22.4 | -10.6% | -3.7 to -1.61 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 196 | 173 | -11.7% | -26.8 to -19 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.17 |  | 1.02 to 1.31 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.182 | 0.182 | +0.0% | -0.0084 to 0.00853 | shown, not judged |
| host CPU-seconds without steal | 217 | 209 | -3.7% | -101 to 85.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
