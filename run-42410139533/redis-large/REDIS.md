# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,471 | -0.0% | -0.758 to 0.185 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000631 to 0.0015 | STEADY, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -6.37e-06 to 6.37e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 0.163 | 0.166 | +1.9% | -0.00848 to 0.0147 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.48 | 5.48 | +0.1% | -0.033 to 0.0459 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.231 | 0.233 | +0.6% | -0.00384 to 0.0065 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.00183 to 0.0532 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.082 | 0.0962 | +17.3% | -0.0471 to 0.0755 | STEADY, no difference beyond the noise |
| host CPU-seconds | 142 | 171 | +19.7% | -90.4 to 147 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.215 | 0.258 | +19.8% | -0.137 to 0.222 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 173 | 173 | -0.1% | -4.13 to 3.72 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 23.2 | 23.4 | +0.5% | -0.338 to 0.564 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 150 | 150 | -0.2% | -3.79 to 3.15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.174 | 0.176 | +1.5% | -0.00234 to 0.0075 | shown, not judged |
| host CPU-seconds without steal | 142 | 171 | +19.7% | -90.4 to 147 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
