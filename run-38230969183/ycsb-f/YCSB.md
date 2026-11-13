# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,328 | 5,250 | -1.5% | -665 to 509 | no difference beyond the noise |
| throughput (operations a second) | 5,348 | 5,270 | -1.5% | -663 to 506 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.348 | 0.346 | -0.4% | -0.00892 to 0.00626 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.572 | 0.573 | +0.1% | -0.0378 to 0.0392 | no difference beyond the noise |
| latency, mean (ms) | 0.236 | 0.241 | +2.3% | -0.0292 to 0.04 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -15.6 to 3.19 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 411 | 406 | -1.2% | -16.2 to 6.62 | no difference beyond the noise |
| pages read into the cache (misses) | 434,372 | 445,422 | +2.5% | -24,785 to 46,884 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.249 | -2.5% | -0.0549 to 0.0419 | no difference beyond the noise |
| host CPU-seconds | 311 | 302 | -2.8% | -85.2 to 67.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.188 | 0.186 | -1.5% | -0.0567 to 0.0511 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -1.46 to 6.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
