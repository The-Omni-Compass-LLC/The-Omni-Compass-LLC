# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0103 to 0.0314 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.71 | -0.6% | -0.0389 to -0.0256 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.78 | -0.3% | -0.0303 to -0.00855 | GAIN |
| latency, mean (ms) | 1.74 | 0.811 | -53.3% | -0.938 to -0.911 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.0% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,763 | 77 | -99.9% | -72,496 to -70,876 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.119 | -17.9% | -0.11 to 0.0576 | STEADY, no difference beyond the noise |
| host CPU-seconds | 98.4 | 81.2 | -17.5% | -82.1 to 47.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.508 | 0.34 | -33.1% | -0.467 to 0.131 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 119 | 102 | -14.2% | -18.1 to -15.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.5 | 12.8 | -11.6% | -2.43 to -0.942 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 105 | 88.8 | -15.2% | -16.3 to -15.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.602 |  | 0.515 to 0.688 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0902 | 0.0856 | -5.2% | -0.00965 to 0.000316 | shown, not judged |
| host CPU-seconds without steal | 98.4 | 81.2 | -17.5% | -82.1 to 47.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
