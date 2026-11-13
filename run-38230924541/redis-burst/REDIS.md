# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,046 | 1,045 | -0.1% | -2.28 to 0.367 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0193 to 0.019 | same |
| cache hit rate | 0.697 | 0.697 | -0.1% | -0.00153 to 0.00034 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0157 to 0.0108 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.001 to 0.0222 | no difference beyond the noise |
| latency, mean (ms) | 1.86 | 1.87 | +0.3% | -0.007 to 0.0194 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.7 | -2.0% | -2.84 to 0.229 | no difference beyond the noise |
| memory used, mean (MB) | 56.9 | 56.4 | -0.9% | -1.77 to 0.756 | no difference beyond the noise |
| keys evicted | 49,961 | 50,454 | +1.0% | -369 to 1,355 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.133 | -1.4% | -0.1 to 0.0964 | no difference beyond the noise |
| host CPU-seconds | 59.8 | 59 | -1.4% | -50.9 to 49.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.477 | 0.47 | -1.3% | -0.406 to 0.394 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 4.67 |  | -1.07 to 10.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
