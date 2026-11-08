# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,265 | 1,463 | +15.7% | 195 to 201 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00571 to 0.00246 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.977 | +15.6% | 0.13 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 0.11 | -97.9% | -5.13 to -5.09 | GAIN |
| latency, 99th percentile (ms) | 5.25 | 5.22 | -0.6% | -0.0606 to -0.00445 | GAIN |
| latency, mean (ms) | 0.886 | 0.202 | -77.2% | -0.698 to -0.669 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 336 | +425.6% | 270 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.4% | 248 to 254 | power given |
| keys evicted | 103,251 | 2,753 | -97.3% | -102,176 to -98,821 | shown, not judged |
| host CPU busy (share of the run) | 0.0468 | 0.0578 | +23.5% | -0.0328 to 0.0549 | STEADY, no difference beyond the noise |
| host CPU-seconds | 81.5 | 102 | +25.6% | -60.5 to 102 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.143 | 0.155 | +8.6% | -0.124 to 0.148 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 119 | 109 | -7.9% | -18.5 to -0.297 | GAIN |
| the server's own CPU-seconds (redis-server) | 16.7 | 14.6 | -12.5% | -3.45 to -0.741 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 102 | 93.7 | -8.1% | -15.9 to -0.765 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.991 |  | 0.626 to 1.36 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.123 | 0.116 | -5.3% | -0.0145 to 0.00143 | shown, not judged |
| host CPU-seconds without steal | 81.5 | 102 | +25.6% | -60.5 to 102 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
