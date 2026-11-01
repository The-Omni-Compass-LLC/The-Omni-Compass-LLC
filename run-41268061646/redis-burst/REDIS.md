# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `e0fab23c2615`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0718 to -0.0262 | LOSS |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.72 | -0.7% | -0.0426 to -0.0326 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.8 | -0.3% | -0.0362 to 0.00246 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 0.821 | -53.0% | -0.953 to -0.899 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.3% | 164 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,734 | 79.3 | -99.9% | -72,576 to -70,733 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.105 | -32.2% | -0.131 to 0.0318 | STEADY, no difference beyond the noise |
| host CPU-seconds | 105 | 69.6 | -33.7% | -99.5 to 28.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.542 | 0.292 | -46.2% | -0.562 to 0.0616 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | -3.02 to 24.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 125 | 106 | -15.0% | -21.8 to -15.6 | GAIN |
| the server's own CPU-seconds (redis-server) | 15.3 | 13 | -15.4% | -2.66 to -2.06 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 109 | 92.1 | -15.7% | -20.4 to -13.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.744 |  | 0.536 to 0.951 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0956 | 0.0925 | -3.2% | -0.00717 to 0.00112 | shown, not judged |
| host CPU-seconds without steal | 105 | 69.6 | -33.7% | -99.5 to 28.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
