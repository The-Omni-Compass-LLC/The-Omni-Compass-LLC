# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,469 | 1,470 | +0.0% | -1.31 to 1.64 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0389 to 0.025 | STEADY, no difference beyond the noise |
| cache hit rate | 0.981 | 0.981 | -0.0% | -4.03e-06 to 3.88e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.107 | 0.099 | -7.9% | -0.0159 to -0.000954 | GAIN |
| latency, 99th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0139 to -0.000257 | GAIN |
| latency, mean (ms) | 0.182 | 0.179 | -2.0% | -0.00869 to 0.00132 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0119 to 0.0458 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0582 | 0.0623 | +7.0% | -0.0478 to 0.0559 | STEADY, no difference beyond the noise |
| host CPU-seconds | 103 | 111 | +7.4% | -89.3 to 105 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.156 | 0.168 | +7.4% | -0.135 to 0.158 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 109 | 106 | -3.2% | -4.49 to -2.57 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.7 | 14.1 | -4.1% | -1.76 to 0.571 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 94.6 | 91.7 | -3.1% | -3.37 to -2.49 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.125 | 0.118 | -5.0% | -0.0188 to 0.00646 | shown, not judged |
| host CPU-seconds without steal | 103 | 111 | +7.4% | -89.3 to 105 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
