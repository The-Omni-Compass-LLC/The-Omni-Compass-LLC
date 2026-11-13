# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,856 | 2,856 | +0.0% | -1.17 to 1.3 | no difference beyond the noise |
| throughput (operations a second) | 2,864 | 2,864 | -0.0% | -0.687 to 0.378 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.462 | 0.461 | -0.3% | -0.015 to 0.0123 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.617 | 0.614 | -0.4% | -0.0149 to 0.00959 | no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.215 | -0.6% | -0.00903 to 0.0063 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.8% | -22.8 to 4.68 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 407 | -2.3% | -19.3 to 0.266 | no difference beyond the noise |
| pages read into the cache (misses) | 502,850 | 447,904 | -10.9% | -62,655 to -47,237 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.213 | +0.1% | -0.0568 to 0.057 | no difference beyond the noise |
| host CPU-seconds | 244 | 244 | -0.0% | -82.3 to 82.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.276 | -0.0% | -0.0935 to 0.0933 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
