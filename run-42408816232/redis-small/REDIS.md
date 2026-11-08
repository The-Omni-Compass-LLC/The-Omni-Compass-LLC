# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0424 to 0.0426 | STEADY, the same |
| cache hit rate | 0.617 | 0.782 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.68 | -0.4% | -0.033 to -0.0136 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.1% | -0.000752 to 0.0104 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 1.37 | -39.6% | -0.907 to -0.891 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.9% | 243 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,191 | 0 | -100.0% | -243,862 to -242,519 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.147 | -7.4% | -0.0603 to 0.037 | STEADY, no difference beyond the noise |
| host CPU-seconds | 267 | 250 | -6.1% | -113 to 80.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.64 | 0.474 | -25.9% | -0.374 to 0.0424 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 321 | 286 | -10.7% | -40.9 to -27.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 37.2 | 33.7 | -9.2% | -4.25 to -2.6 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 283 | 251 | -11.5% | -38.5 to -26.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.69 |  | 1.4 to 1.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.243 | 0.234 | -3.4% | -0.0129 to -0.00377 | shown, not judged |
| host CPU-seconds without steal | 267 | 250 | -6.1% | -113 to 80.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
