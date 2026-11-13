# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,927 | 2,921 | -0.2% | -11.9 to 0.255 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,934 | 2,930 | -0.1% | -6.46 to -0.83 | LOSS |
| latency, 95th percentile (ms) | 0.243 | 0.262 | +8.0% | -0.0137 to 0.0524 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.418 | 0.466 | +11.5% | -0.0369 to 0.133 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.108 | 0.117 | +8.8% | -0.00822 to 0.0271 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -75.6 to -52.7 | GAIN |
| bytes in the cache, mean (MB) | 418 | 369 | -11.7% | -53.9 to -44.1 | GAIN |
| pages read into the cache (misses) | 687,029 | 767,242 | +11.7% | 40,868 to 119,559 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.149 | +17.0% | -0.0823 to 0.125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 229 | 271 | +18.6% | -173 to 258 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.171 | 0.203 | +18.7% | -0.13 to 0.194 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
