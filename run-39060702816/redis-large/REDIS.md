# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,286 | +1.7% | 20.8 to 23.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00121 to 0.00077 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0133 to 0.0155 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.0% | -0.00881 to 0.00505 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.24 | +0.0% | -0.0217 to 0.0234 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.89 | 0.812 | -8.8% | -0.0921 to -0.0638 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | -0.0223 to 2.81 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.4 | +1.9% | 0.118 to 2.17 | power given |
| keys evicted | 103,597 | 94,134 | -9.1% | -10,176 to -8,750 | shown, not judged |
| host CPU busy (share of the run) | 0.062 | 0.0571 | -8.0% | -0.0295 to 0.0196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 101 | -8.7% | -57 to 37.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.194 | 0.174 | -10.2% | -0.104 to 0.0641 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
