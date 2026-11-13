# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -1.39 to 1.25 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0703 to 0.109 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | +0.0% | -0.000203 to 0.000207 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00373 to 0.00451 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.29 | +0.4% | -0.0661 to 0.111 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 1.54 | +0.3% | -0.0248 to 0.0352 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -4.35 to 1.45 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.1 | 56.2 | -1.6% | -2.99 to 1.14 | EVEN, no difference beyond the noise |
| keys evicted | 71,712 | 71,698 | -0.0% | -112 to 84.2 | shown, not judged |
| host CPU busy (share of the run) | 0.0601 | 0.0516 | -14.2% | -0.0539 to 0.0368 | EVEN, no difference beyond the noise |
| host CPU-seconds | 42.5 | 36 | -15.4% | -40.2 to 27.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.22 | 0.186 | -15.5% | -0.208 to 0.14 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
