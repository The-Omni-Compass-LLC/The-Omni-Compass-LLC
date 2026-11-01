# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,265 | 1,463 | +15.6% | 193 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.04 to 0.0606 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 0.12 | -97.7% | -5.15 to -5.07 | GAIN |
| latency, 99th percentile (ms) | 5.26 | 5.22 | -0.8% | -0.0689 to -0.0105 | GAIN |
| latency, mean (ms) | 0.891 | 0.207 | -76.7% | -0.707 to -0.66 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.8% | 272 to 274 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 251 to 253 | power given |
| keys evicted | 103,231 | 2,621 | -97.5% | -101,675 to -99,547 | shown, not judged |
| host CPU busy (share of the run) | 0.0654 | 0.0537 | -17.9% | -0.0598 to 0.0364 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 94.5 | -18.2% | -110 to 67.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.203 | 0.144 | -29.3% | -0.199 to 0.0807 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 28 to 28 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 114 | -7.1% | -21.2 to 3.58 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 17.3 | 15.2 | -12.5% | -4.22 to -0.0953 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 106 | 98 | -7.3% | -17.7 to 2.29 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.09 |  | 0.714 to 1.47 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.121 | 0.12 | -0.9% | -0.0327 to 0.0305 | shown, not judged |
| host CPU-seconds without steal | 116 | 94.5 | -18.2% | -110 to 67.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
