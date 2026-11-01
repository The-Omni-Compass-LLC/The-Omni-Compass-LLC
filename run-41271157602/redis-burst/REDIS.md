# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 248 to 253 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0154 to 0.0395 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.2% | 0.165 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.49 | -1.6% | -0.107 to -0.0693 | GAIN |
| latency, 99th percentile (ms) | 5.63 | 5.61 | -0.5% | -0.0332 to -0.0199 | GAIN |
| latency, mean (ms) | 1.64 | 0.741 | -54.8% | -0.909 to -0.891 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 238 | +271.9% | 169 to 179 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.0% | 141 to 144 | power given |
| keys evicted | 71,695 | 162 | -99.8% | -72,220 to -70,846 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.0931 | -19.0% | -0.0826 to 0.0389 | STEADY, no difference beyond the noise |
| host CPU-seconds | 80.7 | 65.4 | -19.0% | -63 to 32.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.417 | 0.274 | -34.3% | -0.357 to 0.0715 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.67 |  | 3.87 to 11.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 84 | 72.2 | -14.1% | -13.4 to -10.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.5 | 9.15 | -13.2% | -2.16 to -0.627 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 73.4 | 62.5 | -14.9% | -12.2 to -9.66 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.498 |  | 0.419 to 0.577 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0668 | 0.0637 | -4.7% | -0.00496 to -0.00133 | shown, not judged |
| host CPU-seconds without steal | 80.7 | 65.4 | -19.0% | -63 to 32.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
