# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.6% | 197 to 199 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0143 to 0.00142 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 0.239 | -95.8% | -5.52 to -5.49 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.74 | -1.2% | -0.0784 to -0.0602 | GAIN |
| latency, mean (ms) | 1.05 | 0.308 | -70.6% | -0.751 to -0.728 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.0% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 249 to 254 | power given |
| keys evicted | 103,241 | 2,689 | -97.4% | -101,276 to -99,828 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.109 | -14.6% | -0.0852 to 0.0478 | STEADY, no difference beyond the noise |
| host CPU-seconds | 215 | 186 | -13.6% | -156 to 97.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.378 | 0.282 | -25.2% | -0.295 to 0.105 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 281 | 244 | -13.3% | -45.8 to -28.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.4 | 32.3 | -11.4% | -5.86 to -2.44 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 244 | 210 | -14.2% | -41.8 to -27.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.59 |  | 1.26 to 1.93 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.231 | 0.223 | -3.6% | -0.019 to 0.00229 | shown, not judged |
| host CPU-seconds without steal | 215 | 186 | -13.6% | -156 to 97.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
