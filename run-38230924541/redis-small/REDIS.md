# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 832 | 827 | -0.6% | -6.15 to -4.44 | **WORSE** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0449 to 0.0241 | no difference beyond the noise |
| cache hit rate | 0.555 | 0.552 | -0.6% | -0.00413 to -0.00272 | **WORSE** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.1% | 0.000296 to 0.0137 | **WORSE** |
| latency, 99th percentile (ms) | 5.73 | 5.75 | +0.3% | 0.00409 to 0.036 | **WORSE** |
| latency, mean (ms) | 2.6 | 2.62 | +1.0% | 0.0174 to 0.0326 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.2 | +0.3% | 0.0983 to 0.327 | **WORSE** |
| memory used, mean (MB) | 60.3 | 60 | -0.5% | -0.326 to -0.261 | better |
| keys evicted | 184,960 | 188,233 | +1.8% | 3,082 to 3,464 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.155 | +11.2% | -0.0313 to 0.0626 | no difference beyond the noise |
| host CPU-seconds | 154 | 175 | +13.1% | -40.5 to 80.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.618 | 0.704 | +13.8% | -0.158 to 0.329 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 9 |  | 9 to 9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
