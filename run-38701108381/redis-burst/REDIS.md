# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.78 to 1.3 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0568 to 0.0954 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00146 to 0.00114 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% | 0.000237 to 0.0083 | LOSS |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.2% | 0.00476 to 0.0203 | LOSS |
| latency, mean (ms) | 1.74 | 1.75 | +0.4% | -0.00419 to 0.017 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 60.9 | -4.9% | -3.38 to -2.87 | GAIN |
| memory used, mean (MB) | 57.2 | 55 | -3.8% | -2.29 to -2.04 | GAIN |
| keys evicted | 71,705 | 71,758 | +0.1% | -264 to 369 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.139 | +25.4% | -0.0346 to 0.0909 | EVEN, no difference beyond the noise |
| host CPU-seconds | 72.4 | 93.5 | +29.1% | -26.8 to 69 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.374 | 0.483 | +29.2% | -0.139 to 0.357 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
