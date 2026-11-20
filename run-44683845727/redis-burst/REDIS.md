# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,327 | +23.3% | 247 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0267 to -0.00128 | LOSS |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.59 | 5.52 | -1.3% | -0.111 to -0.0369 | GAIN |
| latency, 99th percentile (ms) | 5.64 | 5.62 | -0.2% | -0.0325 to 0.00521 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.65 | 0.745 | -54.8% | -0.928 to -0.875 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 240 | +274.2% | 170 to 181 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,694 | 72.7 | -99.9% | -72,458 to -70,784 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.1 | -13.0% | -0.0771 to 0.047 | STEADY, no difference beyond the noise |
| host CPU-seconds | 80.6 | 70.4 | -12.7% | -58.2 to 37.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.416 | 0.295 | -29.2% | -0.353 to 0.11 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 86.3 | 74.8 | -13.4% | -15.6 to -7.58 | GAIN |
| the server's own CPU-seconds (redis-server) | 10.6 | 9.35 | -12.1% | -1.57 to -0.995 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 75.6 | 64.8 | -14.3% | -14.5 to -7.12 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.524 |  | 0.416 to 0.633 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0685 | 0.0667 | -2.6% | -0.00571 to 0.00218 | shown, not judged |
| host CPU-seconds without steal | 80.6 | 70.4 | -12.7% | -58.2 to 37.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
