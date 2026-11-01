# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,384 | +17.1% | 201 to 203 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.041 to 0.0366 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.1% | 0.134 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.3% | -0.0328 to -0.00233 | GAIN |
| latency, 99th percentile (ms) | 5.28 | 5.25 | -0.6% | -0.0728 to 0.0147 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 0.48 | -59.3% | -0.711 to -0.687 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 346 | +440.9% | 281 to 284 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.9% | 255 to 256 | power given |
| keys evicted | 138,236 | 3,059 | -97.8% | -135,832 to -134,522 | shown, not judged |
| host CPU busy (share of the run) | 0.059 | 0.055 | -6.7% | -0.0372 to 0.0293 | STEADY, no difference beyond the noise |
| host CPU-seconds | 103 | 96.7 | -6.3% | -68.3 to 55.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.194 | 0.155 | -20.0% | -0.141 to 0.0634 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 19 to 19 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 125 | 116 | -7.7% | -16.1 to -3.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.2 | 15 | -12.9% | -3.2 to -1.22 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 99.3 | -8.0% | -14.3 to -2.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.2 |  | 0.939 to 1.45 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.126 | 0.124 | -1.4% | -0.00682 to 0.00327 | shown, not judged |
| host CPU-seconds without steal | 103 | 96.7 | -6.3% | -68.3 to 55.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
