# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 1,172 | +26.8% | 247 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0166 to 0.021 | STEADY, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.165 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.47 | -0.7% | -0.0487 to -0.0317 | GAIN |
| latency, 99th percentile (ms) | 5.58 | 5.57 | -0.3% | -0.0235 to -0.00478 | GAIN |
| latency, mean (ms) | 2.15 | 1.27 | -40.8% | -0.885 to -0.866 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 312 | +387.0% | 246 to 249 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,180 | 0 | -100.0% | -243,639 to -242,721 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0983 | -11.3% | -0.0413 to 0.0162 | STEADY, no difference beyond the noise |
| host CPU-seconds | 193 | 172 | -10.9% | -78.3 to 36 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.465 | 0.326 | -29.8% | -0.235 to -0.0412 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 15.5 to 23.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 211 | 189 | -10.3% | -26.5 to -16.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.9 | 22.3 | -10.7% | -3.26 to -2.06 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 186 | 166 | -10.9% | -24.4 to -16.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.29 |  | 0.986 to 1.6 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.171 | 0.166 | -2.7% | -0.0129 to 0.00357 | shown, not judged |
| host CPU-seconds without steal | 193 | 172 | -10.9% | -78.3 to 36 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
