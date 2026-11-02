# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.2% | 198 to 210 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.114 to 0.0556 | STEADY, no difference beyond the noise |
| cache hit rate | 0.789 | 0.926 | +17.3% | 0.132 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.69 | -0.8% | -0.0628 to -0.0337 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.78 | -0.3% | -0.031 to -0.00275 | GAIN |
| latency, mean (ms) | 1.34 | 0.589 | -56.2% | -0.781 to -0.728 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 352 | +449.9% | 275 to 301 | power given |
| memory used, mean (MB) | 61.2 | 322 | +426.4% | 248 to 274 | power given |
| keys evicted | 138,192 | 2,009 | -98.5% | -138,956 to -133,410 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.122 | -7.7% | -0.0467 to 0.0263 | STEADY, no difference beyond the noise |
| host CPU-seconds | 222 | 208 | -6.6% | -85 to 55.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.417 | 0.332 | -20.3% | -0.221 to 0.051 | STEADY, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 17 to 17 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 287 | 254 | -11.4% | -39.5 to -25.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.7 | 31.7 | -8.8% | -4.39 to -1.7 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 252 | 221 | -12.4% | -37.6 to -24.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.77 |  | 1.33 to 2.2 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.227 | -2.7% | -0.015 to 0.00222 | shown, not judged |
| host CPU-seconds without steal | 222 | 208 | -6.6% | -85 to 55.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
