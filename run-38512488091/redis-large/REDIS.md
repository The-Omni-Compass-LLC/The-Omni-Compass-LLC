# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,318 | +4.0% | -25 to 126 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0107 to 0.00776 | EVEN, the same |
| cache hit rate | 0.845 | 0.879 | +4.0% | -0.0167 to 0.0843 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.72 | 5.71 | -0.3% | -0.0396 to 0.0084 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.2% | -0.0261 to 0.00646 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.04 | 0.858 | -17.8% | -0.459 to 0.0863 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 68.9 | +7.6% | -6.26 to 16 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 64 | +4.4% | -4.99 to 10.3 | EVEN, no difference beyond the noise |
| keys evicted | 103,266 | 80,926 | -21.6% | -55,943 to 11,263 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.11 | -4.6% | -0.0348 to 0.0241 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 185 | -4.6% | -65.6 to 47.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.341 | 0.312 | -8.3% | -0.109 to 0.0531 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 35 |  | 13.5 to 56.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
