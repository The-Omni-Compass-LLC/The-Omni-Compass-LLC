# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,385 | +17.0% | 198 to 206 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0442 to 0.0136 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.924 | +17.1% | 0.133 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.2 | -0.4% | -0.0275 to -0.0192 | GAIN |
| latency, 99th percentile (ms) | 5.26 | 5.24 | -0.4% | -0.0259 to -0.0167 | GAIN |
| latency, mean (ms) | 1.17 | 0.469 | -59.7% | -0.718 to -0.675 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 346 | +440.6% | 277 to 287 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.8% | 255 to 256 | power given |
| keys evicted | 138,224 | 3,054 | -97.8% | -136,191 to -134,150 | shown, not judged |
| host CPU busy (share of the run) | 0.0688 | 0.0524 | -23.9% | -0.0409 to 0.008 | STEADY, no difference beyond the noise |
| host CPU-seconds | 122 | 92.1 | -24.4% | -76.1 to 16.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.229 | 0.148 | -35.4% | -0.162 to -0.000206 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 124 | 111 | -10.8% | -15.1 to -11.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 17.2 | 14.6 | -15.0% | -2.82 to -2.33 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 107 | 94.8 | -11.2% | -13.6 to -10.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.11 |  | 0.913 to 1.31 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.124 | 0.12 | -3.1% | -0.0105 to 0.00288 | shown, not judged |
| host CPU-seconds without steal | 122 | 92.1 | -24.4% | -76.1 to 16.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
