# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00715 to 0.014 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.51 | -1.3% | -0.0725 to -0.0678 | GAIN |
| latency, 99th percentile (ms) | 5.63 | 5.61 | -0.4% | -0.0323 to -0.0164 | GAIN |
| latency, mean (ms) | 1.65 | 0.747 | -54.7% | -0.918 to -0.883 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 238 | +272.1% | 169 to 180 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.0% | 141 to 145 | power given |
| keys evicted | 71,724 | 163 | -99.8% | -72,369 to -70,751 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.0716 | -38.1% | -0.103 to 0.0146 | STEADY, no difference beyond the noise |
| host CPU-seconds | 81 | 49.2 | -39.3% | -74.8 to 11.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.418 | 0.206 | -50.7% | -0.384 to -0.0398 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 85.5 | 74.3 | -13.0% | -11.7 to -10.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.6 | 9.21 | -12.8% | -1.45 to -1.25 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 74.8 | 64.6 | -13.7% | -10.9 to -9.68 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.511 |  | 0.409 to 0.613 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0675 | 0.0676 | +0.1% | -0.0014 to 0.00153 | shown, not judged |
| host CPU-seconds without steal | 81 | 49.2 | -39.3% | -74.8 to 11.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
