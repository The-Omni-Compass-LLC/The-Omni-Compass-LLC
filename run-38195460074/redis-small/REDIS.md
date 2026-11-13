# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 832 | 829 | -0.3% | -11.2 to 6 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0306 to 0.0289 | same |
| cache hit rate | 0.555 | 0.553 | -0.3% | -0.00747 to 0.0041 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.1% | -0.00115 to 0.00818 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.2% | -0.000905 to 0.0282 | no difference beyond the noise |
| latency, mean (ms) | 2.61 | 2.62 | +0.5% | -0.0139 to 0.0381 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.2 | +0.2% | -0.0156 to 0.317 | no difference beyond the noise |
| memory used, mean (MB) | 60.3 | 60.2 | -0.2% | -0.746 to 0.465 | no difference beyond the noise |
| keys evicted | 185,177 | 187,327 | +1.2% | -3,325 to 7,624 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.142 | -6.6% | -0.0124 to -0.00765 | better |
| host CPU-seconds | 170 | 157 | -7.7% | -15.9 to -10.2 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.683 | 0.632 | -7.4% | -0.057 to -0.0436 | better |
| ceiling changes written (the knob's moves) | 0 | 7.67 |  | 3.87 to 11.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
