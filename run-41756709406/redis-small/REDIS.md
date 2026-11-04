# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,173 | +26.7% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000316 to 0.0205 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.4% | -0.0345 to -0.0159 | GAIN |
| latency, 99th percentile (ms) | 5.76 | 5.76 | -0.1% | -0.0246 to 0.0145 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 1.37 | -39.7% | -0.911 to -0.892 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 243 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,172 | 0 | -100.0% | -243,674 to -242,670 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.136 | -11.1% | -0.0601 to 0.0262 | STEADY, no difference beyond the noise |
| host CPU-seconds | 256 | 230 | -10.3% | -111 to 58.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.616 | 0.436 | -29.3% | -0.363 to 0.0026 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 318 | 282 | -11.1% | -40.7 to -30.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.4 | 32.8 | -10.0% | -4.13 to -3.13 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 281 | 248 | -11.9% | -38.5 to -28.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.62 |  | 1.36 to 1.87 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.229 | -4.5% | -0.0165 to -0.00497 | shown, not judged |
| host CPU-seconds without steal | 256 | 230 | -10.3% | -111 to 58.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
