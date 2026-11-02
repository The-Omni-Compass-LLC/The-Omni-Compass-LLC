# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.6% | 194 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0219 to -0.000169 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.13 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 0.249 | -95.7% | -5.52 to -5.51 | GAIN |
| latency, 99th percentile (ms) | 5.83 | 5.76 | -1.2% | -0.0792 to -0.0624 | GAIN |
| latency, mean (ms) | 1.06 | 0.317 | -70.0% | -0.756 to -0.722 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.7% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.8% | 248 to 256 | power given |
| keys evicted | 103,502 | 2,639 | -97.4% | -102,797 to -98,929 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.134 | -2.0% | -0.0325 to 0.0269 | STEADY, no difference beyond the noise |
| host CPU-seconds | 230 | 232 | +0.7% | -58 to 61.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.404 | 0.352 | -12.9% | -0.146 to 0.0411 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 27.9 to 30.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 289 | 252 | -12.6% | -38.6 to -34.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.3 | 35.3 | -7.8% | -4.56 to -1.45 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 250 | 215 | -14.1% | -38.4 to -32 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.73 |  | 1.27 to 2.19 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.234 | -2.0% | -0.0103 to 0.000488 | shown, not judged |
| host CPU-seconds without steal | 230 | 232 | +0.7% | -58 to 61.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
