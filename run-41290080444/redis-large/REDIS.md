# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 197 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00426 to 0.00386 | STEADY, the same |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.132 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 0.125 | -97.6% | -5.12 to -5.09 | GAIN |
| latency, 99th percentile (ms) | 5.29 | 5.23 | -1.1% | -0.106 to -0.0131 | GAIN |
| latency, mean (ms) | 0.881 | 0.198 | -77.5% | -0.69 to -0.676 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.0% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.3% | 249 to 254 | power given |
| keys evicted | 103,322 | 2,679 | -97.4% | -101,151 to -100,134 | shown, not judged |
| host CPU busy (share of the run) | 0.0656 | 0.0507 | -22.7% | -0.0725 to 0.0427 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 89.3 | -22.9% | -134 to 80.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.203 | 0.135 | -33.3% | -0.235 to 0.0995 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 28 to 28 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 122 | 111 | -9.1% | -13 to -9.17 | GAIN |
| the server's own CPU-seconds (redis-server) | 18.7 | 16.4 | -12.2% | -3.18 to -1.38 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 103 | 93.6 | -9.6% | -11.1 to -8.73 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.07 |  | 0.789 to 1.35 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.122 | 0.121 | -0.7% | -0.00638 to 0.00458 | shown, not judged |
| host CPU-seconds without steal | 116 | 89.3 | -22.9% | -134 to 80.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
