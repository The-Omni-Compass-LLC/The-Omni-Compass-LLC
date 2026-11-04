# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.7% | 196 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.017 to 0.0044 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.244 | -95.8% | -5.53 to -5.49 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.75 | -1.3% | -0.0931 to -0.0607 | GAIN |
| latency, mean (ms) | 1.05 | 0.312 | -70.4% | -0.751 to -0.735 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.6% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,439 | 2,638 | -97.5% | -102,064 to -99,538 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.115 | -15.0% | -0.0606 to 0.0202 | STEADY, no difference beyond the noise |
| host CPU-seconds | 227 | 194 | -14.4% | -111 to 45.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.398 | 0.295 | -26.0% | -0.236 to 0.029 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 288 | 250 | -13.3% | -40.9 to -35.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.2 | 34.3 | -10.3% | -4.66 to -3.22 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 249 | 214 | -14.4% | -38.2 to -33.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.58 |  | 1.28 to 1.88 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.227 | -3.5% | -0.0179 to 0.00113 | shown, not judged |
| host CPU-seconds without steal | 227 | 194 | -14.4% | -111 to 45.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
