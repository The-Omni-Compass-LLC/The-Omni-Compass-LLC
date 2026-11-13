# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,253 | 1,303 | +4.0% | 2.67 to 98.3 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00107 to 0.0017 | same |
| cache hit rate | 0.836 | 0.869 | +4.0% | 0.00318 to 0.0634 | better |
| latency, 95th percentile (ms) | 5.75 | 5.73 | -0.3% | -0.0756 to 0.0465 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.98 | 5.81 | -2.9% | -0.968 to 0.616 | no difference beyond the noise |
| latency, mean (ms) | 1.11 | 0.922 | -17.3% | -0.421 to 0.0359 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 70.1 | +9.5% | -3.31 to 15.5 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 65.4 | +6.8% | -2.59 to 10.9 | no difference beyond the noise |
| keys evicted | 72,703 | 58,038 | -20.2% | -28,357 to -974 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.112 | -13.9% | -0.0708 to 0.0347 | no difference beyond the noise |
| host CPU-seconds | 146 | 124 | -15.0% | -86.8 to 43 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.318 | -18.2% | -0.247 to 0.105 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 16.6 to 39.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
