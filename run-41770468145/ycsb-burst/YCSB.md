# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | -0.0% | -6.05 to 5.52 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,886 | -0.0% | -4.73 to 4.19 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.418 | 0.424 | +1.4% | 0.00352 to 0.00848 | LOSS |
| latency, 99th percentile (ms) | 0.592 | 0.602 | +1.7% | -0.0334 to 0.0541 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.219 | +1.9% | -0.00448 to 0.0128 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 403 | 401 | -0.6% | -11.7 to 7.16 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 267,560 | 268,484 | +0.3% | -27,705 to 29,554 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.197 | +3.4% | -0.0662 to 0.0793 | STEADY, no difference beyond the noise |
| host CPU-seconds | 131 | 136 | +3.8% | -57 to 66.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.246 | 0.256 | +3.8% | -0.107 to 0.126 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82 | 83.6 | +2.0% | -2.48 to 5.73 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81 | 82.3 | +1.7% | -2.81 to 5.53 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.04 | 1.31 | +25.6% | 0.16 to 0.373 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 131 | 136 | +3.8% | -57 to 66.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
