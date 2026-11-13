# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,846 | 2,831 | -0.5% | -54.2 to 24.3 | no difference beyond the noise |
| throughput (operations a second) | 2,856 | 2,843 | -0.5% | -52.2 to 25.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.466 | 0.475 | +2.0% | -0.0223 to 0.041 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.706 | 0.73 | +3.4% | -0.0239 to 0.0712 | no difference beyond the noise |
| latency, mean (ms) | 0.245 | 0.247 | +1.1% | -0.00496 to 0.0103 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 496 | -3.2% | -61.3 to 29 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 398 | 381 | -4.2% | -46.6 to 12.9 | no difference beyond the noise |
| pages read into the cache (misses) | 187,469 | 176,894 | -5.6% | -26,368 to 5,219 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.192 | -1.3% | -0.0979 to 0.093 | no difference beyond the noise |
| host CPU-seconds | 87.4 | 85.6 | -2.0% | -55.2 to 51.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.249 | 0.245 | -1.6% | -0.157 to 0.149 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
