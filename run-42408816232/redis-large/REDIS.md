# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.6% | 195 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00956 to -0.00193 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 0.234 | -95.9% | -5.52 to -5.49 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.73 | -1.3% | -0.0881 to -0.061 | GAIN |
| latency, mean (ms) | 1.05 | 0.307 | -70.7% | -0.749 to -0.73 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.2% | 270 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,265 | 2,649 | -97.4% | -101,829 to -99,402 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.115 | -14.6% | -0.0651 to 0.0256 | STEADY, no difference beyond the noise |
| host CPU-seconds | 229 | 197 | -13.9% | -121 to 57 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.401 | 0.298 | -25.6% | -0.244 to 0.0385 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 281 | 244 | -13.3% | -39 to -36.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.2 | 32.7 | -9.5% | -4.97 to -1.92 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 245 | 209 | -14.5% | -38.3 to -32.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.48 |  | 1.22 to 1.73 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.235 | 0.225 | -4.2% | -0.014 to -0.00553 | shown, not judged |
| host CPU-seconds without steal | 229 | 197 | -13.9% | -121 to 57 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
