# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.6% | 246 to 247 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0358 to 0.0392 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.7% | 0.165 to 0.165 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.68 | -0.4% | -0.0441 to -0.0064 | GAIN |
| latency, 99th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0152 to 0.0109 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 1.37 | -39.6% | -0.905 to -0.892 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +390.3% | 244 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,046 | 0 | -100.0% | -243,532 to -242,561 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.128 | -18.0% | -0.0446 to -0.0114 | GAIN |
| host CPU-seconds | 262 | 214 | -18.3% | -79.7 to -16.4 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.63 | 0.406 | -35.5% | -0.289 to -0.157 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 317 | 281 | -11.3% | -39 to -32.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.5 | 32.7 | -10.4% | -4.57 to -3.03 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 280 | 246 | -12.0% | -36.8 to -30.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.89 |  | 1.66 to 2.11 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.242 | 0.233 | -3.5% | -0.0194 to 0.00264 | shown, not judged |
| host CPU-seconds without steal | 262 | 214 | -18.3% | -79.7 to -16.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
