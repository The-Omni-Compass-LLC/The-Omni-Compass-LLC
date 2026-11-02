# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,385 | +17.2% | 198 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0714 to 0.0322 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.133 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.65 | -0.8% | -0.0899 to 0.00385 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.73 | -0.3% | -0.0506 to 0.0178 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 0.586 | -56.1% | -0.787 to -0.708 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +446.2% | 278 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,343 | 2,688 | -98.1% | -137,396 to -133,913 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.116 | -14.1% | -0.0523 to 0.0142 | STEADY, no difference beyond the noise |
| host CPU-seconds | 231 | 198 | -14.3% | -96.1 to 30 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.435 | 0.318 | -26.8% | -0.238 to 0.0046 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 266 | 239 | -10.3% | -48.9 to -6.25 | GAIN |
| the server's own CPU-seconds (redis-server) | 31.9 | 28.6 | -10.2% | -6.4 to -0.134 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 234 | 208 | -11.0% | -44 to -7.75 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.57 |  | 1.3 to 1.84 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.223 | 0.226 | +1.4% | -0.0155 to 0.0217 | shown, not judged |
| host CPU-seconds without steal | 231 | 198 | -14.3% | -96.1 to 30 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
