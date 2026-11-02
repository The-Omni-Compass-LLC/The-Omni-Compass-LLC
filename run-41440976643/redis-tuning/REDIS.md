# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `159b34031f41`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 196 to 210 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0726 to 0.0245 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.131 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.69 | -1.0% | -0.0613 to -0.0513 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.78 | -0.5% | -0.0441 to -0.0104 | GAIN |
| latency, mean (ms) | 1.35 | 0.594 | -55.9% | -0.78 to -0.725 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +447.9% | 274 to 299 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.7% | 244 to 274 | power given |
| keys evicted | 138,228 | 2,376 | -98.3% | -139,361 to -132,341 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.124 | -7.9% | -0.0403 to 0.0189 | STEADY, no difference beyond the noise |
| host CPU-seconds | 227 | 212 | -6.4% | -71.9 to 42.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.426 | 0.34 | -20.1% | -0.189 to 0.0178 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 291 | 255 | -12.3% | -37.9 to -33.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.3 | 31.5 | -10.6% | -4.54 to -2.95 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 222 | -13.2% | -36.1 to -31.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.89 |  | 1.39 to 2.38 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.251 | 0.245 | -2.5% | -0.0141 to 0.00178 | shown, not judged |
| host CPU-seconds without steal | 227 | 212 | -6.4% | -71.9 to 42.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
