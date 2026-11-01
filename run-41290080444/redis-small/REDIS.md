# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00659 to 0.0177 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.66 | -0.5% | -0.0311 to -0.0248 | GAIN |
| latency, 99th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.00763 to -0.00551 | GAIN |
| latency, mean (ms) | 2.26 | 1.36 | -39.8% | -0.907 to -0.892 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.8% | 243 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,215 | 0 | -100.0% | -243,500 to -242,930 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.13 | -15.7% | -0.0573 to 0.00916 | STEADY, no difference beyond the noise |
| host CPU-seconds | 260 | 220 | -15.6% | -107 to 25.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.625 | 0.416 | -33.4% | -0.341 to -0.0765 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 308 | 273 | -11.4% | -37.3 to -33 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.1 | 31.6 | -9.9% | -4.74 to -2.18 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 273 | 240 | -12.2% | -35 to -31.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.67 |  | 1.42 to 1.92 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.231 | 0.22 | -5.0% | -0.0158 to -0.00731 | shown, not judged |
| host CPU-seconds without steal | 260 | 220 | -15.6% | -107 to 25.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
