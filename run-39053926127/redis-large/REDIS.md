# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% | 7.49 to 25.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00401 to 0.00228 | EVEN, the same |
| cache hit rate | 0.845 | 0.856 | +1.3% | 0.00495 to 0.0172 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0113 to 0.0047 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.1% | -0.0096 to 0.0155 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.998 | -5.5% | -0.0889 to -0.0278 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.2% | -1.89 to 3.46 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.4% | -2.37 to 2.82 | EVEN, no difference beyond the noise |
| keys evicted | 103,434 | 96,191 | -7.0% | -11,386 to -3,098 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.125 | +5.5% | -0.0434 to 0.0563 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 210 | +6.2% | -81.2 to 106 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.346 | 0.363 | +4.9% | -0.145 to 0.179 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24 |  | 6.61 to 41.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
