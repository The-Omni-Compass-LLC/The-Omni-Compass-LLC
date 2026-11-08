# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | +0.0% | -0.679 to 0.734 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00413 to 0.00499 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -2.62e-06 to 1.63e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.46 | 5.46 | +0.0% | -0.0145 to 0.018 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.1% | -0.0115 to 0.0204 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.509 | 0.51 | +0.0% | -0.00753 to 0.00763 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0467 to 0.0772 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0901 | 0.0874 | -3.0% | -0.0247 to 0.0192 | STEADY, no difference beyond the noise |
| host CPU-seconds | 157 | 152 | -3.3% | -46.4 to 36 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.251 | 0.243 | -3.3% | -0.0741 to 0.0575 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 177 | 179 | +0.9% | -3.67 to 6.99 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22 | 22.1 | +0.6% | -0.804 to 1.06 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 155 | 157 | +1.0% | -2.86 to 5.92 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.172 | 0.173 | +0.3% | -0.0066 to 0.00772 | shown, not judged |
| host CPU-seconds without steal | 157 | 152 | -3.3% | -46.4 to 36 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
