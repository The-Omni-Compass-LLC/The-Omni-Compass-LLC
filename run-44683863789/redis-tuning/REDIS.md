# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | -0.0% | -0.438 to 0.365 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00252 to 0.000448 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -6.12e-06 to 5.13e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.63 | 5.63 | -0.0% | -0.0101 to 0.00998 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.72 | +0.1% | -0.0125 to 0.0187 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.547 | 0.55 | +0.7% | -0.00177 to 0.00928 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.0308 to 0.0462 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.127 | +9.0% | -0.0435 to 0.0646 | STEADY, no difference beyond the noise |
| host CPU-seconds | 203 | 223 | +10.1% | -86.6 to 127 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.324 | 0.356 | +10.1% | -0.138 to 0.203 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 225 | 227 | +1.1% | -1.08 to 5.85 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 27.7 | 27.8 | +0.4% | -0.222 to 0.462 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 197 | 199 | +1.1% | -1.31 to 5.85 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.22 | 0.219 | -0.5% | -0.00307 to 0.00108 | shown, not judged |
| host CPU-seconds without steal | 203 | 223 | +10.1% | -86.6 to 127 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
