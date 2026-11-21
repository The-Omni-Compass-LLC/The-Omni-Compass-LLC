# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 938 | +1.3% | 11.1 to 13.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.025 to 0.00889 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.3% | 0.00732 to 0.00923 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.1% | -0.0219 to 0.0302 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.77 | +0.3% | -0.0165 to 0.051 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.23 | -1.8% | -0.0612 to -0.0209 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.31 to 1.65 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% | 0.831 to 1.38 | power given |
| keys evicted | 243,204 | 238,739 | -1.8% | -13,000 to 4,068 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.151 | +0.8% | -0.0441 to 0.0463 | EVEN, no difference beyond the noise |
| host CPU-seconds | 252 | 254 | +0.9% | -85.2 to 90 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.604 | 0.602 | -0.4% | -0.212 to 0.207 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 10.7 to 19.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
