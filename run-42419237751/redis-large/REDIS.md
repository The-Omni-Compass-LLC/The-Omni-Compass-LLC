# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.6% | 194 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0128 to 0.000853 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 0.238 | -95.9% | -5.52 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.73 | -1.3% | -0.089 to -0.0614 | GAIN |
| latency, mean (ms) | 1.05 | 0.308 | -70.5% | -0.76 to -0.714 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 339 | +429.8% | 270 to 280 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,446 | 2,643 | -97.4% | -102,000 to -99,608 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.119 | -4.8% | -0.0826 to 0.0706 | STEADY, no difference beyond the noise |
| host CPU-seconds | 210 | 204 | -3.2% | -156 to 143 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.369 | 0.309 | -16.3% | -0.318 to 0.198 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 30.7 |  | 23.5 to 37.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 281 | 245 | -12.6% | -38.9 to -31.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.6 | 33.3 | -9.0% | -4.91 to -1.65 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 244 | 210 | -13.8% | -36.8 to -30.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.64 |  | 1.53 to 1.76 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.233 | 0.225 | -3.3% | -0.0195 to 0.00432 | shown, not judged |
| host CPU-seconds without steal | 210 | 204 | -3.2% | -156 to 143 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
