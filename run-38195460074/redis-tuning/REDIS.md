# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,129 | 1,130 | +0.1% | -5.85 to 8.28 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0658 to 0.0448 | no difference beyond the noise |
| cache hit rate | 0.754 | 0.755 | +0.1% | -0.00391 to 0.00563 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.1% | -0.0134 to 0.00358 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.27 | -0.2% | -0.0318 to 0.0122 | no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.35 | -0.6% | -0.0375 to 0.0211 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +0.9% | -1.59 to 2.69 | no difference beyond the noise |
| memory used, mean (MB) | 61.1 | 61.3 | +0.3% | -1.76 to 2.13 | no difference beyond the noise |
| keys evicted | 106,699 | 106,859 | +0.1% | -3,142 to 3,462 | shown, not judged |
| host CPU busy (share of the run) | 0.0633 | 0.0587 | -7.3% | -0.0387 to 0.0295 | no difference beyond the noise |
| host CPU-seconds | 74.4 | 68.7 | -7.7% | -48.3 to 36.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.22 | 0.203 | -7.8% | -0.143 to 0.109 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 11.1 to 23.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
