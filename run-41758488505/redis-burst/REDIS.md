# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.167 to 0.104 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00837 to 0.00864 | STEADY, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | STEADY, the same |
| latency, 95th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.00533 to 0.00416 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.0% | -0.00856 to 0.0138 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.801 | 0.802 | +0.1% | -0.00571 to 0.00788 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.00931 to 0.0569 | STEADY, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.119 | +8.8% | -0.085 to 0.104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 74.1 | 81.2 | +9.6% | -64.6 to 78.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.31 | 0.34 | +9.6% | -0.27 to 0.33 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 101 | 102 | +0.4% | -1.2 to 1.94 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 12.7 | 12.6 | -0.2% | -0.4 to 0.347 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 88.7 | 89.1 | +0.4% | -1.17 to 1.97 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0886 | 0.0875 | -1.3% | -0.00204 to -0.000173 | shown, not judged |
| host CPU-seconds without steal | 74.1 | 81.2 | +9.6% | -64.6 to 78.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
