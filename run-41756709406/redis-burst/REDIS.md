# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.2% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0145 to 0.0342 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.2% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.56 | 5.47 | -1.6% | -0.101 to -0.0722 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.4% | -0.0325 to -0.00933 | GAIN |
| latency, mean (ms) | 1.62 | 0.732 | -54.9% | -0.911 to -0.872 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 238 | +272.1% | 169 to 180 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.0% | 141 to 144 | power given |
| keys evicted | 71,663 | 159 | -99.8% | -72,414 to -70,595 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.099 | -4.3% | -0.0322 to 0.0232 | STEADY, no difference beyond the noise |
| host CPU-seconds | 72.1 | 70 | -2.9% | -24.4 to 20.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.372 | 0.293 | -21.2% | -0.172 to 0.0141 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 81.4 | 71.3 | -12.4% | -10.5 to -9.71 | GAIN |
| the server's own CPU-seconds (redis-server) | 9.96 | 8.72 | -12.4% | -1.56 to -0.909 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 71.3 | 62 | -13.1% | -9.43 to -9.25 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.498 |  | 0.391 to 0.605 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0662 | 0.0624 | -5.7% | -0.00432 to -0.00325 | shown, not judged |
| host CPU-seconds without steal | 72.1 | 70 | -2.9% | -24.4 to 20.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
