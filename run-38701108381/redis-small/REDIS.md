# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -1.72 to -1.48 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0856 to 0.0364 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00107 to -0.000854 | LOSS |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.1% | -0.00334 to 0.0101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% | 0.0129 to 0.0205 | LOSS |
| latency, mean (ms) | 2.26 | 2.27 | +0.4% | 0.00577 to 0.0139 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.551 to 1.19 | power given |
| memory used, mean (MB) | 60.7 | 60.6 | -0.1% | -0.816 to 0.695 | EVEN, no difference beyond the noise |
| keys evicted | 243,122 | 244,896 | +0.7% | -2,801 to 6,349 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.138 | -4.4% | -0.0355 to 0.0228 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 230 | -5.3% | -69.9 to 44.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.582 | 0.552 | -5.1% | -0.167 to 0.107 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23.3 |  | 17.1 to 29.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
