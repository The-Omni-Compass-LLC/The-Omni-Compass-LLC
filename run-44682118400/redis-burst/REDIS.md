# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,049 | 1,299 | +23.9% | 229 to 273 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.351 to 0.265 | STEADY, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.5% | 0.167 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 7.24 | 5.62 | -22.4% | -3.31 to 0.0654 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.5 | 9.15 | -26.8% | -8.18 to 1.47 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 0.973 | -52.5% | -1.44 to -0.707 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 252 | +293.6% | 185 to 191 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.3% | 143 to 143 | power given |
| keys evicted | 72,179 | 0 | -100.0% | -72,628 to -71,730 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.111 | -18.3% | -0.0439 to -0.00584 | GAIN |
| host CPU-seconds | 95.2 | 77.7 | -18.5% | -31.2 to -3.9 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.504 | 0.332 | -34.2% | -0.243 to -0.101 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 16.3 |  | 10.1 to 22.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 96.4 | 82 | -14.9% | -34 to 5.25 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 11.3 | 9.61 | -15.3% | -3.26 to -0.2 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 85 | 71.8 | -15.5% | -31.2 to 4.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.584 |  | 0.464 to 0.703 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0745 | 0.0696 | -6.6% | -0.0358 to 0.026 | shown, not judged |
| host CPU-seconds without steal | 95.2 | 77.7 | -18.5% | -31.2 to -3.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
