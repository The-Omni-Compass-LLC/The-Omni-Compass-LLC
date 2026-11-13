# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,233 | +4.1% | -2.61 to 100 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00753 to 0.00501 | EVEN, the same |
| cache hit rate | 0.789 | 0.822 | +4.1% | -0.00159 to 0.067 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.72 | -0.1% | -0.0106 to 0.00198 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.78 | +0.1% | -0.00316 to 0.00902 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.16 | -13.2% | -0.367 to 0.0148 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 76.3 | +19.3% | -4.52 to 29.2 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 70.4 | +15.0% | -1.44 to 19.8 | EVEN, no difference beyond the noise |
| keys evicted | 138,178 | 118,310 | -14.4% | -41,832 to 2,096 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.107 | -4.0% | -0.0427 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 184 | 177 | -3.8% | -79.1 to 65 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.346 | 0.32 | -7.6% | -0.148 to 0.0957 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 34 |  | 16.8 to 51.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
