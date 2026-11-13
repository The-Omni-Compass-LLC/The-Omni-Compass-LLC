# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,131 | 1,130 | -0.1% | -1.87 to 0.476 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00364 to 0.00429 | same |
| cache hit rate | 0.754 | 0.753 | -0.1% | -0.00167 to 0.000561 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.64 | 5.65 | +0.1% | -0.0415 to 0.0508 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.71 | +0.1% | -0.0275 to 0.0441 | no difference beyond the noise |
| latency, mean (ms) | 1.48 | 1.48 | +0.4% | -0.028 to 0.0389 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64 | -0.0% | -0.0929 to 0.0396 | no difference beyond the noise |
| memory used, mean (MB) | 61.1 | 60.7 | -0.7% | -0.544 to -0.274 | better |
| keys evicted | 106,689 | 107,752 | +1.0% | 590 to 1,535 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.122 | -5.0% | -0.0564 to 0.0435 | no difference beyond the noise |
| host CPU-seconds | 152 | 143 | -5.8% | -76.7 to 59.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.447 | 0.422 | -5.7% | -0.226 to 0.174 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.3 |  | 18.5 to 24.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
