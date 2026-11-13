# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,901 | 2,899 | -0.1% | -5.18 to 1.12 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,908 | -0.1% | -6.78 to 2.62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.347 | 0.347 | +0.1% | -0.0054 to 0.00607 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.605 | 0.601 | -0.8% | -0.0104 to 0.00107 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.156 | 0.157 | +0.7% | -0.00668 to 0.00889 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 449 | -12.2% | -62.6 to -62.6 | GAIN |
| bytes in the cache, mean (MB) | 417 | 369 | -11.6% | -49.5 to -47.4 | GAIN |
| pages read into the cache (misses) | 682,942 | 760,814 | +11.4% | 50,194 to 105,550 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.194 | +6.3% | -0.0246 to 0.0474 | EVEN, no difference beyond the noise |
| host CPU-seconds | 326 | 352 | +7.8% | -56.2 to 107 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.245 | 0.264 | +7.8% | -0.0423 to 0.0804 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
