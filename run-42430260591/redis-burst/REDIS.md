# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.191 to 0.207 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0146 to 0.0116 | STEADY, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | STEADY, the same |
| latency, 95th percentile (ms) | 5.72 | 5.71 | -0.1% | -0.041 to 0.0245 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.2% | -0.0488 to 0.0308 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.806 | 0.805 | -0.2% | -0.0136 to 0.011 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0237 to 0.0751 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.115 | -1.6% | -0.101 to 0.0976 | STEADY, no difference beyond the noise |
| host CPU-seconds | 79.7 | 77.7 | -2.5% | -76.9 to 72.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.325 | -2.5% | -0.322 to 0.305 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 104 | 103 | -1.1% | -5.62 to 3.31 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 12.9 | 12.8 | -1.0% | -1.01 to 0.757 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 91.4 | 90.4 | -1.1% | -4.79 to 2.74 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.093 | 0.0903 | -2.9% | -0.00406 to -0.0013 | shown, not judged |
| host CPU-seconds without steal | 79.7 | 77.7 | -2.5% | -76.9 to 72.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
