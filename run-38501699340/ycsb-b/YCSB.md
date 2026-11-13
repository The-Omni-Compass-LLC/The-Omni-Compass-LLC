# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,919 | 2,917 | -0.1% | -6.01 to 2.07 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,923 | 2,921 | -0.1% | -5.76 to 1.84 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.25 | -1.3% | -0.031 to 0.0244 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.385 | 0.381 | -1.0% | -0.0106 to 0.00257 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.159 | 0.155 | -2.4% | -0.0193 to 0.0116 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 471 | -8.1% | -127 to 44.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 389 | -6.7% | -92.4 to 36.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,399 | 822,973 | +17.7% | 13,463 to 233,686 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.174 | +2.9% | -0.0443 to 0.0541 | EVEN, no difference beyond the noise |
| host CPU-seconds | 308 | 319 | +3.7% | -99.6 to 122 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.239 | +3.7% | -0.0743 to 0.0914 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
