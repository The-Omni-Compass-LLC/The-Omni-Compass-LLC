# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 246 to 253 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00853 to 0.0182 | STEADY, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.72 | -0.8% | -0.0611 to -0.0298 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.79 | -0.6% | -0.0687 to -0.00594 | GAIN |
| latency, mean (ms) | 1.75 | 0.821 | -53.1% | -0.946 to -0.914 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 240 | +274.2% | 167 to 184 | power given |
| memory used, mean (MB) | 57.2 | 200 | +249.7% | 140 to 145 | power given |
| keys evicted | 71,811 | 161 | -99.8% | -72,474 to -70,826 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.126 | -13.5% | -0.0955 to 0.0562 | STEADY, no difference beyond the noise |
| host CPU-seconds | 97.9 | 85.2 | -12.9% | -72.6 to 47.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.506 | 0.357 | -29.4% | -0.466 to 0.169 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 5.23 to 8.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 105 | -14.6% | -21.3 to -14.6 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.9 | 12.9 | -13.2% | -2.52 to -1.42 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 91.4 | -15.4% | -19.6 to -13.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.601 |  | 0.465 to 0.738 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0955 | 0.0897 | -6.1% | -0.0123 to 0.00073 | shown, not judged |
| host CPU-seconds without steal | 97.9 | 85.2 | -13.0% | -72.6 to 47.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
