# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,252 | +5.8% | 64.7 to 72.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00258 to 0.00369 | EVEN, the same |
| cache hit rate | 0.789 | 0.835 | +5.8% | 0.0431 to 0.0485 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.2% | -0.0155 to -0.00295 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.79 | -0.0% | -0.0102 to 0.00845 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.09 | -18.8% | -0.269 to -0.237 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 87.2 | +36.3% | 22 to 24.5 | power given |
| memory used, mean (MB) | 61.2 | 79.3 | +29.6% | 18 to 18.2 | power given |
| keys evicted | 138,104 | 108,285 | -21.6% | -30,478 to -29,160 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.119 | -0.3% | -0.0175 to 0.0168 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 201 | +0.6% | -30.9 to 33.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.375 | 0.357 | -4.9% | -0.0747 to 0.038 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 53 |  | 39.9 to 66.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
