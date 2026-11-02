# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,386 | +17.2% | 200 to 207 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0152 to -0.0012 | LOSS |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.133 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.46 | -2.3% | -0.132 to -0.123 | GAIN |
| latency, 99th percentile (ms) | 5.7 | 5.63 | -1.2% | -0.0919 to -0.0466 | GAIN |
| latency, mean (ms) | 1.27 | 0.539 | -57.7% | -0.75 to -0.72 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 347 | +442.5% | 272 to 294 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,280 | 2,700 | -98.0% | -137,413 to -133,749 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.115 | -12.7% | -0.0399 to 0.00651 | STEADY, no difference beyond the noise |
| host CPU-seconds | 235 | 205 | -12.7% | -77.5 to 18 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.442 | 0.329 | -25.5% | -0.201 to -0.0244 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 209 | 183 | -12.5% | -28.2 to -24.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 29.6 | 25.7 | -13.3% | -5.99 to -1.92 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 179 | 156 | -13.1% | -25.3 to -21.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.28 |  | 1.14 to 1.41 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.176 | 0.171 | -2.7% | -0.00955 to -7.19e-05 | shown, not judged |
| host CPU-seconds without steal | 235 | 205 | -12.7% | -77.5 to 18 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
