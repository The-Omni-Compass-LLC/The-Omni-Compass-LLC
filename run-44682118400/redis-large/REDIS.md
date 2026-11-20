# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.6% | 197 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00907 to 0.00216 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.977 | +15.6% | 0.131 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 0.172 | -96.9% | -5.37 to -5.37 | GAIN |
| latency, 99th percentile (ms) | 5.63 | 5.51 | -2.1% | -0.121 to -0.116 | GAIN |
| latency, mean (ms) | 0.967 | 0.253 | -73.9% | -0.72 to -0.709 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.0% | 270 to 276 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.5% | 248 to 254 | power given |
| keys evicted | 103,200 | 2,765 | -97.3% | -100,877 to -99,993 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.0946 | -10.6% | -0.0683 to 0.046 | STEADY, no difference beyond the noise |
| host CPU-seconds | 185 | 166 | -10.1% | -131 to 93.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.325 | 0.252 | -22.3% | -0.262 to 0.117 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 200 | 175 | -12.3% | -26.9 to -22.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 26.6 | 23.4 | -12.0% | -3.91 to -2.48 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 173 | 151 | -13.0% | -24.7 to -20.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.17 |  | 0.931 to 1.41 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.169 | 0.165 | -2.7% | -0.00641 to -0.00269 | shown, not judged |
| host CPU-seconds without steal | 185 | 166 | -10.1% | -131 to 93.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
