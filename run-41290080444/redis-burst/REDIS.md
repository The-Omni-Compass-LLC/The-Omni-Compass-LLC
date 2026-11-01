# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,327 | +23.2% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0154 to 0.0132 | STEADY, the same |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.68 | -0.6% | -0.0355 to -0.0277 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.75 | -0.3% | -0.0274 to -0.0085 | GAIN |
| latency, mean (ms) | 1.72 | 0.801 | -53.5% | -0.935 to -0.909 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.0% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,671 | 76.3 | -99.9% | -72,436 to -70,754 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.116 | -22.1% | -0.0722 to 0.00597 | STEADY, no difference beyond the noise |
| host CPU-seconds | 103 | 79.3 | -23.0% | -55.8 to 8.45 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.532 | 0.332 | -37.5% | -0.387 to -0.0118 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 116 | 99.4 | -14.1% | -16.4 to -16.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 13.8 | 12.3 | -11.3% | -1.84 to -1.29 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 102 | 86.4 | -15.0% | -15.6 to -14.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.587 |  | 0.49 to 0.683 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0876 | 0.083 | -5.3% | -0.00585 to -0.00345 | shown, not judged |
| host CPU-seconds without steal | 103 | 79.4 | -23.0% | -55.8 to 8.45 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
