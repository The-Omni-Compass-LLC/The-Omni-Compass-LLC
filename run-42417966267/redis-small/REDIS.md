# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 923 | 1,171 | +26.9% | 246 to 251 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0626 to 0.0208 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.22 | -0.2% | -0.0248 to 0.00248 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.4 | -7.0% | -0.707 to -0.103 | GAIN |
| latency, mean (ms) | 2.08 | 1.22 | -41.5% | -0.879 to -0.845 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,132 | 0 | -100.0% | -243,861 to -242,404 | shown, not judged |
| host CPU busy (share of the run) | 0.0637 | 0.063 | -1.1% | -0.0385 to 0.0371 | STEADY, no difference beyond the noise |
| host CPU-seconds | 111 | 110 | -0.5% | -70.8 to 69.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.267 | 0.209 | -21.6% | -0.202 to 0.0869 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 15.5 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 139 | 129 | -6.8% | -14.7 to -4.13 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.9 | 16.2 | -10.0% | -2.38 to -1.22 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 121 | 112 | -7.5% | -13.8 to -4.19 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.42 |  | 1.29 to 1.55 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.137 | 0.134 | -1.9% | -0.00521 to 0.000124 | shown, not judged |
| host CPU-seconds without steal | 111 | 110 | -0.5% | -70.8 to 69.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
