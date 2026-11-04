# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.0222 to 0.197 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0015 to 0.00486 | STEADY, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | +0.0% | -2.2e-06 to 5.16e-06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.48 | 5.48 | +0.0% | -0.0119 to 0.0132 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.57 | -0.0% | -0.0182 to 0.0154 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.27 | 1.27 | -0.1% | -0.0063 to 0.00414 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00571 to 0.0358 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.0951 | -10.7% | -0.0126 to -0.0102 | GAIN |
| host CPU-seconds | 188 | 166 | -11.8% | -23.7 to -20.5 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.314 | -11.8% | -0.0449 to -0.0388 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 189 | 188 | -0.3% | -4.22 to 3.17 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 22.7 | 22.6 | -0.5% | -0.667 to 0.433 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 166 | 165 | -0.2% | -3.6 to 2.79 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.167 | 0.166 | -0.5% | -0.00568 to 0.00385 | shown, not judged |
| host CPU-seconds without steal | 188 | 166 | -11.8% | -23.7 to -20.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
