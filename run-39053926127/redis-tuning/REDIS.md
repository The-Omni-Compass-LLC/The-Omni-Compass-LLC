# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,196 | +1.1% | 6.03 to 19.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00475 to 0.00321 | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00376 to 0.013 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.00636 to 0.00349 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.34 | 5.31 | -0.5% | -0.133 to 0.0817 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.11 | -3.9% | -0.0638 to -0.0258 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.4% | 0.493 to 2.64 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.9% | 0.0598 to 2.21 | power given |
| keys evicted | 138,120 | 133,296 | -3.5% | -7,944 to -1,705 | shown, not judged |
| host CPU busy (share of the run) | 0.0536 | 0.0479 | -10.7% | -0.0311 to 0.0197 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.6 | 83.9 | -11.3% | -57.1 to 35.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.178 | 0.156 | -12.2% | -0.11 to 0.0662 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
