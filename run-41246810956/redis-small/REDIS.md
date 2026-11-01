# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `4082deec8fda`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 247 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0365 to 0.0383 | STEADY, the same |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.61 | 5.57 | -0.8% | -0.0576 to -0.0281 | GAIN |
| latency, 99th percentile (ms) | 5.69 | 5.67 | -0.4% | -0.0297 to -0.0101 | GAIN |
| latency, mean (ms) | 2.19 | 1.3 | -40.8% | -0.902 to -0.884 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +389.6% | 245 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,136 | 0 | -100.0% | -243,379 to -242,893 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.114 | -18.2% | -0.0645 to 0.014 | STEADY, no difference beyond the noise |
| host CPU-seconds | 249 | 202 | -18.9% | -124 to 30.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.598 | 0.383 | -36.0% | -0.362 to -0.0689 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 15.5 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 233 | 207 | -11.1% | -32.1 to -19.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 22 | 19 | -13.5% | -3.39 to -2.55 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 211 | 187 | -11.4% | -29.8 to -18 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.16 |  | 1.07 to 1.24 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.173 | 0.173 | +0.1% | -0.00181 to 0.00215 | shown, not judged |
| host CPU-seconds without steal | 249 | 202 | -18.9% | -124 to 30.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
