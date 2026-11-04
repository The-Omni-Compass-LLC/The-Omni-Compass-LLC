# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,172 | +26.8% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0596 to 0.0422 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.2% | -0.0183 to -0.00131 | GAIN |
| latency, 99th percentile (ms) | 5.36 | 5.28 | -1.5% | -0.191 to 0.0275 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.06 | 1.21 | -41.4% | -0.861 to -0.843 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.5% | 243 to 253 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.4% | 196 to 198 | power given |
| keys evicted | 243,076 | 0 | -100.0% | -243,155 to -242,997 | shown, not judged |
| host CPU busy (share of the run) | 0.0734 | 0.0584 | -20.4% | -0.022 to -0.00797 | GAIN |
| host CPU-seconds | 130 | 102 | -21.1% | -41.3 to -13.6 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.312 | 0.194 | -37.8% | -0.152 to -0.0843 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 12.5 to 22.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 131 | 122 | -7.2% | -13.6 to -5.39 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.4 | 15.5 | -11.3% | -2.27 to -1.66 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 114 | 105 | -7.8% | -12.4 to -5.28 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.29 |  | 1.02 to 1.57 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.124 | 0.127 | +2.4% | 0.0017 to 0.00428 | shown, not judged |
| host CPU-seconds without steal | 130 | 102 | -21.1% | -41.3 to -13.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
