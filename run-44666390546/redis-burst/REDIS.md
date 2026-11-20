# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,327 | +23.3% | 247 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00789 to 0.0133 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.169 | GAIN |
| latency, 95th percentile (ms) | 5.56 | 5.49 | -1.4% | -0.0991 to -0.0529 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.6 | -0.3% | -0.0375 to -0.000727 | GAIN |
| latency, mean (ms) | 1.63 | 0.736 | -54.8% | -0.906 to -0.875 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 239 | +273.5% | 171 to 179 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.6% | 142 to 145 | power given |
| keys evicted | 71,654 | 72.7 | -99.9% | -72,266 to -70,896 | shown, not judged |
| host CPU busy (share of the run) | 0.0942 | 0.0985 | +4.7% | -0.0486 to 0.0574 | STEADY, no difference beyond the noise |
| host CPU-seconds | 64.8 | 69.3 | +7.0% | -36.2 to 45.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.29 | -13.2% | -0.231 to 0.143 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 81.9 | 72.4 | -11.5% | -13.3 to -5.65 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.2 | 8.9 | -12.6% | -1.64 to -0.925 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 71.6 | 63 | -12.1% | -12.1 to -5.21 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.506 |  | 0.425 to 0.587 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0664 | 0.0636 | -4.2% | -0.0053 to -0.000284 | shown, not judged |
| host CPU-seconds without steal | 64.8 | 69.3 | +7.0% | -36.2 to 45.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
