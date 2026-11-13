# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,934 | -0.0% | -9.53 to 8.18 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,936 | 2,936 | -0.0% | -8.91 to 7.38 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.209 | 0.206 | -1.4% | -0.0509 to 0.0449 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.364 | 0.361 | -0.9% | -0.0597 to 0.053 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.084 | 0.0833 | -0.8% | -0.0104 to 0.00909 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.8% | -78.3 to -52.6 | GAIN |
| bytes in the cache, mean (MB) | 419 | 366 | -12.6% | -56.3 to -49.7 | GAIN |
| pages read into the cache (misses) | 679,972 | 752,389 | +10.6% | 3,198 to 141,635 | shown, not judged |
| host CPU busy (share of the run) | 0.0791 | 0.0929 | +17.4% | -0.014 to 0.0415 | EVEN, no difference beyond the noise |
| host CPU-seconds | 140 | 167 | +19.1% | -27.4 to 80.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.105 | 0.124 | +19.1% | -0.0203 to 0.0603 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
