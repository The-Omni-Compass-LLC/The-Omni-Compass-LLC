# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,354 | +6.9% | 84.1 to 91.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00237 to 0.00272 | EVEN, the same |
| cache hit rate | 0.845 | 0.904 | +7.0% | 0.0559 to 0.062 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.45 | -1.1% | -0.0664 to -0.0588 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.3% | -0.0276 to -0.0101 | GAIN |
| latency, mean (ms) | 0.967 | 0.653 | -32.4% | -0.325 to -0.302 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 75.9 | +18.7% | 9.89 to 14 | power given |
| memory used, mean (MB) | 61.3 | 69.3 | +13.1% | 7.64 to 8.41 | power given |
| keys evicted | 103,463 | 64,151 | -38.0% | -41,556 to -37,068 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0986 | -11.4% | -0.0308 to 0.00546 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 173 | -12.2% | -60.6 to 12.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.347 | 0.285 | -17.9% | -0.129 to 0.00459 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 48 |  | 48 to 48 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
