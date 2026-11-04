# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,181 | 1,384 | +17.2% | 203 to 204 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0166 to 0.00864 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.1% | 0.135 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.33 | 5.3 | -0.6% | -0.151 to 0.0856 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.55 | 5.5 | -0.8% | -0.558 to 0.468 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 0.496 | -58.7% | -0.768 to -0.643 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 347 | +441.7% | 277 to 289 | power given |
| memory used, mean (MB) | 61.2 | 317 | +418.0% | 255 to 256 | power given |
| keys evicted | 138,415 | 3,080 | -97.8% | -135,719 to -134,950 | shown, not judged |
| host CPU busy (share of the run) | 0.0705 | 0.0754 | +6.9% | -0.00644 to 0.0162 | STEADY, no difference beyond the noise |
| host CPU-seconds | 124 | 133 | +7.8% | -11.9 to 31.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.233 | 0.214 | -8.0% | -0.075 to 0.0377 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 139 | 135 | -2.9% | -47.2 to 39.2 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 18.1 | 16.7 | -7.8% | -6.45 to 3.62 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 121 | 117 | -3.1% | -42.1 to 34.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.19 |  | 1.09 to 1.29 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.134 | 0.142 | +6.2% | -0.0273 to 0.0439 | shown, not judged |
| host CPU-seconds without steal | 124 | 133 | +7.8% | -11.9 to 31.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
