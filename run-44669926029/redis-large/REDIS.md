# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,468 | 1,470 | +0.1% | -4.46 to 7.89 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00659 to 0.00552 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -5.13e-06 to 6.12e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.31 | 0.235 | -24.3% | -0.224 to 0.073 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.51 | 5.53 | +0.4% | -0.118 to 0.166 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.256 | 0.251 | -2.1% | -0.0388 to 0.0279 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 349 | 348 | -0.0% | -0.136 to 0.124 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.106 | +1.1% | -0.042 to 0.0444 | STEADY, no difference beyond the noise |
| host CPU-seconds | 185 | 187 | +1.2% | -83.8 to 88 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.282 | +1.0% | -0.126 to 0.132 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 187 | 190 | +1.5% | -42.3 to 48 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 25 | 25.6 | +2.3% | -6.89 to 8.03 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 162 | 164 | +1.4% | -35.5 to 40.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.184 | 0.184 | +0.2% | -0.0415 to 0.0424 | shown, not judged |
| host CPU-seconds without steal | 185 | 187 | +1.2% | -83.8 to 88 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
