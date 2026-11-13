# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,922 | -0.1% | -9.03 to 1.16 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,933 | 2,929 | -0.1% | -8.12 to 0.839 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.247 | 0.253 | +2.3% | -0.00437 to 0.0157 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.426 | 0.437 | +2.6% | -0.0238 to 0.0458 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.109 | 0.112 | +3.1% | -0.00428 to 0.011 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -75.8 to -52.7 | GAIN |
| bytes in the cache, mean (MB) | 418 | 369 | -11.9% | -59.4 to -39.7 | GAIN |
| pages read into the cache (misses) | 688,326 | 769,819 | +11.8% | 61,386 to 101,600 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.131 | +7.1% | -0.019 to 0.0364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 234 | +7.6% | -37.9 to 71.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.163 | 0.175 | +7.7% | -0.0285 to 0.0535 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
