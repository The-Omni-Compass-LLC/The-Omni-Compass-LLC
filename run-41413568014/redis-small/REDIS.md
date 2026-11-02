# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,172 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0219 to 0.019 | STEADY, the same |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.62 | -0.5% | -0.0393 to -0.0211 | GAIN |
| latency, 99th percentile (ms) | 5.7 | 5.69 | -0.2% | -0.015 to -0.00421 | GAIN |
| latency, mean (ms) | 2.24 | 1.34 | -40.2% | -0.913 to -0.889 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +390.2% | 244 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,173 | 0 | -100.0% | -243,528 to -242,818 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.132 | -15.9% | -0.0615 to 0.0114 | STEADY, no difference beyond the noise |
| host CPU-seconds | 273 | 229 | -16.1% | -117 to 29.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.655 | 0.434 | -33.8% | -0.4 to -0.0425 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 15.5 to 23.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 288 | 252 | -12.6% | -40.2 to -32.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 32.3 | 28.2 | -12.9% | -5 to -3.35 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 222 | -13.2% | -36.6 to -30.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.59 |  | 1.29 to 1.9 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.223 | 0.215 | -3.7% | -0.0201 to 0.00354 | shown, not judged |
| host CPU-seconds without steal | 273 | 229 | -16.1% | -117 to 29.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
