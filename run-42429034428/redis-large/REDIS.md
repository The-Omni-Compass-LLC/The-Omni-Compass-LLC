# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.6% | 193 to 203 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00648 to -0.00385 | LOSS |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.13 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.229 | -96.0% | -5.52 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.73 | -1.2% | -0.0866 to -0.0482 | GAIN |
| latency, mean (ms) | 1.04 | 0.304 | -70.8% | -0.761 to -0.717 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.1% | 271 to 275 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 249 to 254 | power given |
| keys evicted | 103,395 | 2,703 | -97.4% | -102,517 to -98,868 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.114 | -18.3% | -0.045 to -0.00607 | GAIN |
| host CPU-seconds | 239 | 195 | -18.2% | -82.3 to -4.74 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.419 | 0.296 | -29.3% | -0.185 to -0.0604 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 278 | 241 | -13.3% | -41.4 to -32.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.5 | 32.3 | -11.5% | -5.2 to -3.19 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 207 | -14.1% | -39.1 to -28.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.44 |  | 1.26 to 1.61 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.217 | -7.9% | -0.0531 to 0.0158 | shown, not judged |
| host CPU-seconds without steal | 239 | 195 | -18.2% | -82.3 to -4.74 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
