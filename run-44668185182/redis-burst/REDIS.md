# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.3% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00818 to 0.0157 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.57 | 5.47 | -1.8% | -0.114 to -0.0843 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.6 | -0.3% | -0.0254 to -0.0113 | GAIN |
| latency, mean (ms) | 1.63 | 0.738 | -54.8% | -0.914 to -0.877 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 240 | +274.4% | 168 to 183 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,704 | 72.7 | -99.9% | -72,643 to -70,620 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0925 | -17.0% | -0.0605 to 0.0226 | STEADY, no difference beyond the noise |
| host CPU-seconds | 78 | 64.7 | -17.0% | -45.2 to 18.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.402 | 0.271 | -32.7% | -0.271 to 0.00758 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 82.9 | 72.3 | -12.9% | -11.8 to -9.59 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.1 | 9.02 | -11.1% | -1.36 to -0.882 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 72.7 | 62.7 | -13.8% | -11 to -9.15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.502 |  | 0.406 to 0.598 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0671 | 0.0645 | -3.9% | -0.00353 to -0.00172 | shown, not judged |
| host CPU-seconds without steal | 78 | 64.7 | -17.0% | -45.2 to 18.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
