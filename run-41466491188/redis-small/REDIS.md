# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,171 | +26.8% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0798 to 0.0549 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.94 | 5.75 | -3.2% | -0.538 to 0.163 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 6.81 | -5.5% | -1.15 to 0.361 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.36 | 1.43 | -39.5% | -0.994 to -0.865 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 315 | +391.6% | 246 to 256 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.6% | 196 to 198 | power given |
| keys evicted | 243,285 | 0 | -100.0% | -243,843 to -242,726 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.142 | -15.5% | -0.034 to -0.0177 | GAIN |
| host CPU-seconds | 280 | 237 | -15.4% | -56.8 to -29.8 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.675 | 0.45 | -33.3% | -0.265 to -0.184 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 17.9 to 20.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 342 | 304 | -11.2% | -55.1 to -21.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.9 | 34.5 | -11.4% | -6.94 to -1.9 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 303 | 267 | -11.7% | -49.9 to -21.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.76 |  | 1.42 to 2.09 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.258 | 0.246 | -4.4% | -0.0303 to 0.00748 | shown, not judged |
| host CPU-seconds without steal | 280 | 237 | -15.4% | -56.8 to -29.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
