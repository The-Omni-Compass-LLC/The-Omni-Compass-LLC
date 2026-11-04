# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% | -0.0665 to 0.0765 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00274 to 0.000735 | STEADY, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.68e-06 to 3.68e-06 | STEADY, the same |
| latency, 95th percentile (ms) | 5.41 | 5.4 | -0.1% | -0.0508 to 0.0446 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.58 | -0.1% | -0.00968 to 0.00287 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.499 | 0.498 | -0.3% | -0.00151 to -0.00126 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.00579 to 0.0441 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0863 | 0.0785 | -9.0% | -0.0359 to 0.0203 | STEADY, no difference beyond the noise |
| host CPU-seconds | 151 | 136 | -9.8% | -68.8 to 39.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.241 | 0.217 | -9.8% | -0.11 to 0.0628 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 170 | 169 | -0.1% | -1.5 to 1.06 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22 | 21.7 | -1.6% | -0.957 to 0.257 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 147 | 148 | +0.1% | -0.859 to 1.11 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.165 | +0.8% | -0.00215 to 0.00471 | shown, not judged |
| host CPU-seconds without steal | 151 | 136 | -9.8% | -68.8 to 39.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
