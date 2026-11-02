# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,386 | +17.0% | 200 to 203 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0105 to 0.0112 | STEADY, the same |
| cache hit rate | 0.79 | 0.924 | +17.0% | 0.134 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.55 | 5.29 | -4.8% | -0.268 to -0.262 | GAIN |
| latency, 99th percentile (ms) | 5.67 | 5.62 | -0.8% | -0.0508 to -0.0367 | GAIN |
| latency, mean (ms) | 1.23 | 0.517 | -58.0% | -0.719 to -0.708 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 346 | +440.1% | 276 to 287 | power given |
| memory used, mean (MB) | 61.2 | 317 | +417.9% | 255 to 256 | power given |
| keys evicted | 137,996 | 3,083 | -97.8% | -135,522 to -134,303 | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.0801 | -19.8% | -0.0608 to 0.0212 | STEADY, no difference beyond the noise |
| host CPU-seconds | 178 | 141 | -20.5% | -115 to 42.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.227 | -32.1% | -0.244 to 0.0296 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 176 | 158 | -10.3% | -19.9 to -16.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 20 | 17.8 | -10.6% | -2.63 to -1.62 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 156 | 139 | -11.0% | -19.4 to -15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.14 |  | 1.05 to 1.23 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.178 | 0.177 | -0.4% | -0.00967 to 0.00814 | shown, not judged |
| host CPU-seconds without steal | 178 | 141 | -20.5% | -115 to 42.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
