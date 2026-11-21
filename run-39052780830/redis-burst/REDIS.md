# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,075 | -0.1% | -1.97 to -0.164 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0197 to 0.0278 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00115 to -5.62e-05 | LOSS |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0162 to 0.0156 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.00386 to 0.0232 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.5% | 0.00611 to 0.0123 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.1% | -2.2 to -0.527 | GAIN |
| memory used, mean (MB) | 57.2 | 56.7 | -0.8% | -1.22 to 0.249 | EVEN, no difference beyond the noise |
| keys evicted | 71,687 | 71,866 | +0.3% | 9.42 to 350 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.121 | -12.7% | -0.0826 to 0.0476 | EVEN, no difference beyond the noise |
| host CPU-seconds | 92.9 | 79.2 | -14.7% | -63.1 to 35.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.479 | 0.409 | -14.7% | -0.325 to 0.184 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
