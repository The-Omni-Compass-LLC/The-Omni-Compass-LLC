# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,808 | 5,806 | -0.0% | -8.69 to 4.19 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,820 | 5,817 | -0.0% | -8.57 to 3.39 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.239 | 0.237 | -0.8% | -0.0128 to 0.00883 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.452 | 0.449 | -0.7% | -0.0158 to 0.00917 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.12 | 0.118 | -1.0% | -0.00465 to 0.00221 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 446 | -12.8% | -77.7 to -53.4 | GAIN |
| bytes in the cache, mean (MB) | 418 | 367 | -12.3% | -60.1 to -43.2 | GAIN |
| pages read into the cache (misses) | 694,723 | 795,695 | +14.5% | 52,562 to 149,380 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.158 | -6.7% | -0.0932 to 0.0708 | EVEN, no difference beyond the noise |
| host CPU-seconds | 307 | 285 | -7.1% | -196 to 153 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.115 | 0.107 | -7.1% | -0.0735 to 0.0571 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
