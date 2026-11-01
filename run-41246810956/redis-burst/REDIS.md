# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `4082deec8fda`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,324 | +23.2% | 245 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0695 to 0.101 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.165 to 0.168 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0158 to 0.00337 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.25 | -0.4% | -0.0517 to 0.00952 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.54 | 0.683 | -55.6% | -0.879 to -0.835 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 236 | +269.5% | 170 to 175 | power given |
| memory used, mean (MB) | 57.2 | 199 | +248.7% | 141 to 143 | power given |
| keys evicted | 71,686 | 231 | -99.7% | -72,048 to -70,861 | shown, not judged |
| host CPU busy (share of the run) | 0.0586 | 0.0624 | +6.6% | -0.0874 to 0.0951 | STEADY, no difference beyond the noise |
| host CPU-seconds | 41.4 | 44.2 | +6.7% | -66 to 71.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.214 | 0.185 | -13.4% | -0.367 to 0.309 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 7.23 to 10.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 49.2 | 46.4 | -5.8% | -6.27 to 0.57 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 6.94 | 6.28 | -9.6% | -1.36 to 0.0291 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 42.2 | 39.5 | -6.3% | -5.29 to -0.0544 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.492 |  | 0.349 to 0.635 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0483 | 0.0468 | -3.2% | -0.00343 to 0.000311 | shown, not judged |
| host CPU-seconds without steal | 41.4 | 44.2 | +6.7% | -66 to 71.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
