# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,250 | 1,298 | +3.9% | 6.78 to 90.1 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.045 to 0.0298 | no difference beyond the noise |
| cache hit rate | 0.835 | 0.868 | +4.0% | 0.00483 to 0.0613 | better |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.1% | -0.0106 to 0.000149 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.27 | -0.0% | -0.0175 to 0.0137 | no difference beyond the noise |
| latency, mean (ms) | 0.947 | 0.782 | -17.4% | -0.308 to -0.0215 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 72.1 | +12.7% | -7.27 to 23.5 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 66.2 | +8.0% | -4.78 to 14.6 | no difference beyond the noise |
| keys evicted | 73,205 | 58,499 | -20.1% | -27,685 to -1,727 | shown, not judged |
| host CPU busy (share of the run) | 0.056 | 0.0629 | +12.3% | -0.00775 to 0.0215 | no difference beyond the noise |
| host CPU-seconds | 65.2 | 73.8 | +13.2% | -9.45 to 26.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.174 | 0.19 | +9.0% | -0.0373 to 0.0687 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 18 to 28 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
