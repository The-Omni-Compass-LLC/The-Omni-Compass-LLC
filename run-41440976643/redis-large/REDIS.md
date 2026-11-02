# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `159b34031f41`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,465 | +15.6% | 197 to 198 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.018 to 0.00218 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.6% | 0.132 to 0.133 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 0.239 | -95.8% | -5.52 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.74 | -1.3% | -0.0875 to -0.0652 | GAIN |
| latency, mean (ms) | 1.05 | 0.308 | -70.5% | -0.744 to -0.732 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.7% | 270 to 278 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.8% | 248 to 256 | power given |
| keys evicted | 103,121 | 2,635 | -97.4% | -100,977 to -99,997 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.118 | -12.2% | -0.0524 to 0.0196 | STEADY, no difference beyond the noise |
| host CPU-seconds | 228 | 202 | -11.1% | -95.8 to 45 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.399 | 0.307 | -23.1% | -0.204 to 0.0198 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 28 to 28 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 282 | 246 | -13.0% | -39.1 to -34.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.1 | 32.9 | -11.3% | -4.29 to -4.1 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 245 | 211 | -13.9% | -36.7 to -31.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.58 |  | 1.2 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.23 | 0.224 | -2.5% | -0.0138 to 0.00246 | shown, not judged |
| host CPU-seconds without steal | 228 | 202 | -11.1% | -95.8 to 45 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
