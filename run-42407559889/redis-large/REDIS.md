# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,464 | +15.6% | 195 to 199 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0405 to 0.0142 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.78 | 0.286 | -95.1% | -5.52 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.87 | 5.78 | -1.6% | -0.0974 to -0.0921 | GAIN |
| latency, mean (ms) | 1.08 | 0.334 | -69.0% | -0.752 to -0.733 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.6% | 271 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,482 | 2,646 | -97.4% | -101,731 to -99,940 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.123 | -13.1% | -0.0376 to 0.000418 | STEADY, no difference beyond the noise |
| host CPU-seconds | 237 | 207 | -12.5% | -67.8 to 8.56 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.416 | 0.315 | -24.3% | -0.172 to -0.0298 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 29 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 301 | 265 | -12.1% | -37.9 to -35 | GAIN |
| the server's own CPU-seconds (redis-server) | 38.5 | 35.4 | -8.3% | -5.16 to -1.23 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 262 | 227 | -13.4% | -38.4 to -32.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 2.01 |  | 1.8 to 2.22 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.287 | 0.284 | -1.1% | -0.0182 to 0.0119 | shown, not judged |
| host CPU-seconds without steal | 237 | 207 | -12.5% | -67.8 to 8.56 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
