# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.1% | 198 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0517 to 0.0151 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.69 | -1.0% | -0.0611 to -0.0486 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.77 | -0.4% | -0.0393 to -0.00944 | GAIN |
| latency, mean (ms) | 1.34 | 0.59 | -56.0% | -0.772 to -0.733 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +445.9% | 277 to 293 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,113 | 2,701 | -98.0% | -137,449 to -133,376 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.118 | -16.9% | -0.0445 to -0.00357 | GAIN |
| host CPU-seconds | 242 | 201 | -16.7% | -80.3 to -0.273 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.454 | 0.323 | -28.8% | -0.197 to -0.0644 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 289 | 252 | -13.0% | -40 to -35 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.1 | 30.7 | -12.5% | -6.96 to -1.83 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 254 | 219 | -13.7% | -36.3 to -33.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.6 |  | 1.34 to 1.86 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.233 | 0.221 | -5.2% | -0.0174 to -0.00695 | shown, not judged |
| host CPU-seconds without steal | 242 | 201 | -16.7% | -80.3 to -0.273 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
