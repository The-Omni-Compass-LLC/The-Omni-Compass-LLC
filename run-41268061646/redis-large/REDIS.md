# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `e0fab23c2615`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,463 | +15.7% | 195 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00897 to 0.00589 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 0.127 | -97.6% | -5.11 to -5.1 | GAIN |
| latency, 99th percentile (ms) | 5.27 | 5.23 | -0.7% | -0.0493 to -0.025 | GAIN |
| latency, mean (ms) | 0.897 | 0.209 | -76.7% | -0.696 to -0.68 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 336 | +425.3% | 270 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.4% | 249 to 253 | power given |
| keys evicted | 103,402 | 2,748 | -97.3% | -101,743 to -99,564 | shown, not judged |
| host CPU busy (share of the run) | 0.0541 | 0.0609 | +12.6% | -0.0231 to 0.0367 | STEADY, no difference beyond the noise |
| host CPU-seconds | 94 | 108 | +14.4% | -42.3 to 69.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.165 | 0.163 | -1.2% | -0.0882 to 0.0843 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 127 | 116 | -8.3% | -14.1 to -6.91 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.8 | 15.8 | -11.1% | -2.64 to -1.32 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 109 | 99.3 | -8.9% | -12.8 to -6.56 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.16 |  | 0.94 to 1.38 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.128 | 0.125 | -1.7% | -0.00903 to 0.00465 | shown, not judged |
| host CPU-seconds without steal | 94 | 108 | +14.4% | -42.3 to 69.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
