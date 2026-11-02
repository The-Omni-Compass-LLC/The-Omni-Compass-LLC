# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 195 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.019 to 0.0109 | STEADY, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.13 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 0.217 | -96.2% | -5.5 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.77 | 5.7 | -1.2% | -0.0721 to -0.0612 | GAIN |
| latency, mean (ms) | 1.03 | 0.297 | -71.3% | -0.749 to -0.725 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +427.0% | 270 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 247 to 256 | power given |
| keys evicted | 103,454 | 2,692 | -97.4% | -102,303 to -99,223 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.111 | -7.8% | -0.0485 to 0.0296 | STEADY, no difference beyond the noise |
| host CPU-seconds | 203 | 190 | -6.2% | -87.5 to 62.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.289 | -18.9% | -0.192 to 0.0574 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 267 | 232 | -13.3% | -38.6 to -32.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.4 | 30.9 | -10.1% | -4.1 to -2.83 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 233 | 199 | -14.4% | -35.7 to -31.4 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.38 |  | 1.13 to 1.62 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.219 | 0.207 | -5.5% | -0.0163 to -0.00775 | shown, not judged |
| host CPU-seconds without steal | 203 | 190 | -6.2% | -87.5 to 62.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
