# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0358 to 0.0138 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.67 | 5.64 | -0.6% | -0.1 to 0.0354 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.75 | +0.2% | -0.105 to 0.13 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.7 | 0.791 | -53.3% | -0.925 to -0.884 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 244 | +281.3% | 162 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,702 | 73 | -99.9% | -72,430 to -70,829 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.133 | +0.8% | -0.0142 to 0.0164 | STEADY, no difference beyond the noise |
| host CPU-seconds | 92.3 | 94.9 | +2.8% | -10.3 to 15.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.477 | 0.398 | -16.6% | -0.126 to -0.0319 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10.7 |  | -3.02 to 24.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 98.9 | 89.6 | -9.4% | -12.5 to -6.05 | GAIN |
| the server's own CPU-seconds (redis-server) | 11.6 | 10.6 | -8.9% | -1.45 to -0.603 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 87.2 | 78.4 | -10.1% | -11.5 to -6.13 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.575 |  | 0.447 to 0.704 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0825 | 0.0828 | +0.4% | -0.00989 to 0.0105 | shown, not judged |
| host CPU-seconds without steal | 92.3 | 94.9 | +2.8% | -10.3 to 15.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
