# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `f3b70b287c67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,174 | 1,174 | +0.0% | -0.0508 to 0.0634 | STEADY, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00202 to 0.00158 | STEADY, the same |
| cache hit rate | 0.783 | 0.783 | -0.0% | -1.26e-05 to 1.24e-05 | STEADY, the same |
| latency, 95th percentile (ms) | 5.58 | 5.57 | -0.0% | -0.00269 to -0.0019 | GAIN |
| latency, 99th percentile (ms) | 5.66 | 5.66 | -0.0% | -0.00628 to 0.00562 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.29 | -0.0% | -0.0075 to 0.00736 | STEADY, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0151 to 0.0297 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.119 | +4.2% | -0.0693 to 0.0787 | STEADY, no difference beyond the noise |
| host CPU-seconds | 204 | 214 | +4.7% | -138 to 158 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.386 | 0.404 | +4.8% | -0.262 to 0.299 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 192 | 192 | +0.4% | -6.35 to 7.83 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 20 | 20.1 | +0.4% | -0.561 to 0.714 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 171 | 172 | +0.4% | -5.8 to 7.12 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.193 | 0.192 | -0.4% | -0.00911 to 0.0076 | shown, not judged |
| host CPU-seconds without steal | 204 | 214 | +4.7% | -138 to 158 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
