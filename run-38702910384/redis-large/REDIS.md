# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,355 | +7.0% | 85.5 to 91.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00207 to 0.00117 | EVEN, the same |
| cache hit rate | 0.845 | 0.904 | +7.0% | 0.0573 to 0.0609 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.45 | -1.1% | -0.1 to -0.0201 | GAIN |
| latency, 99th percentile (ms) | 5.6 | 5.58 | -0.4% | -0.0301 to -0.00961 | GAIN |
| latency, mean (ms) | 0.961 | 0.645 | -32.9% | -0.331 to -0.3 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 76.9 | +20.1% | 9.24 to 16.5 | power given |
| memory used, mean (MB) | 61.3 | 69.4 | +13.2% | 7.98 to 8.19 | power given |
| keys evicted | 103,609 | 64,170 | -38.1% | -40,964 to -37,912 | shown, not judged |
| host CPU busy (share of the run) | 0.0833 | 0.094 | +12.9% | -0.00818 to 0.0296 | EVEN, no difference beyond the noise |
| host CPU-seconds | 143 | 165 | +15.0% | -16.1 to 59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.251 | 0.27 | +7.4% | -0.0422 to 0.0797 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 47.3 |  | 38.6 to 56.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
