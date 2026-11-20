# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,174 | +26.8% | 247 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0259 to 0.0198 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.43 | -1.5% | -0.0937 to -0.0721 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.6 | -0.4% | -0.0231 to -0.0191 | GAIN |
| latency, mean (ms) | 2.11 | 1.24 | -41.0% | -0.872 to -0.858 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +388.0% | 243 to 253 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,300 | 0 | -100.0% | -243,675 to -242,925 | shown, not judged |
| host CPU busy (share of the run) | 0.0982 | 0.0839 | -14.5% | -0.0609 to 0.0323 | STEADY, no difference beyond the noise |
| host CPU-seconds | 175 | 148 | -15.0% | -116 to 64 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.419 | 0.281 | -33.0% | -0.351 to 0.0747 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 14.7 to 23.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 177 | 159 | -9.9% | -20.4 to -14.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 21.5 | 19.3 | -10.0% | -3.01 to -1.27 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 155 | 139 | -10.6% | -18.7 to -14.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.07 |  | 1.02 to 1.13 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.173 | 0.165 | -4.5% | -0.011 to -0.00462 | shown, not judged |
| host CPU-seconds without steal | 175 | 148 | -15.0% | -116 to 64 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
