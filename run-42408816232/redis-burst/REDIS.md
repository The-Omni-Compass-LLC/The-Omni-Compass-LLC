# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,325 | +23.2% | 245 to 253 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0822 to 0.0351 | STEADY, no difference beyond the noise |
| cache hit rate | 0.718 | 0.884 | +23.2% | 0.164 to 0.168 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.22 | -0.2% | -0.0248 to 0.00511 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.25 | -0.4% | -0.0665 to 0.0227 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 0.68 | -55.7% | -0.882 to -0.828 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 235 | +267.9% | 167 to 176 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.3% | 142 to 143 | power given |
| keys evicted | 71,639 | 258 | -99.6% | -71,979 to -70,783 | shown, not judged |
| host CPU busy (share of the run) | 0.0496 | 0.0421 | -15.0% | -0.0517 to 0.0368 | STEADY, no difference beyond the noise |
| host CPU-seconds | 34.3 | 29.2 | -14.9% | -37.5 to 27.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.177 | 0.122 | -30.9% | -0.205 to 0.0958 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.67 |  | 6.23 to 9.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 51.2 | 46.7 | -8.8% | -8.46 to -0.53 | GAIN |
| the server's own CPU-seconds (redis-server) | 7.27 | 6.31 | -13.2% | -1.48 to -0.444 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 43.9 | 39.9 | -9.2% | -7.54 to -0.539 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.507 |  | 0.409 to 0.606 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.051 | 0.0491 | -3.7% | -0.0063 to 0.00255 | shown, not judged |
| host CPU-seconds without steal | 34.3 | 29.2 | -14.9% | -37.5 to 27.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
