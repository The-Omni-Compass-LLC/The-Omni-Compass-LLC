# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,465 | +15.8% | 196 to 204 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00945 to -0.00132 | LOSS |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.13 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.227 | -96.0% | -5.52 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.72 | -1.2% | -0.101 to -0.0368 | GAIN |
| latency, mean (ms) | 1.05 | 0.304 | -71.1% | -0.774 to -0.719 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.2% | 271 to 276 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,612 | 2,638 | -97.5% | -103,144 to -98,805 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.119 | -16.8% | -0.0612 to 0.0131 | STEADY, no difference beyond the noise |
| host CPU-seconds | 245 | 205 | -16.5% | -114 to 32.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.431 | 0.31 | -27.9% | -0.236 to -0.00471 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.7 |  | 27.2 to 30.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 277 | 239 | -13.7% | -40.8 to -35.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.8 | 31.4 | -12.2% | -4.62 to -4.13 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 242 | 206 | -14.6% | -38.3 to -32 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.45 |  | 1.17 to 1.74 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.226 | 0.211 | -6.8% | -0.022 to -0.00872 | shown, not judged |
| host CPU-seconds without steal | 245 | 205 | -16.5% | -114 to 32.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
