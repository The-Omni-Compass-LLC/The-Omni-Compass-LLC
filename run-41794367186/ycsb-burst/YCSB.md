# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,881 | -0.0% | -4.22 to 3.63 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -2.85 to 2.08 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.411 | 0.411 | +0.0% | -0.00248 to 0.00248 | STEADY, the same |
| latency, 99th percentile (ms) | 0.575 | 0.579 | +0.7% | -0.0367 to 0.0447 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.215 | -0.4% | -0.00632 to 0.00454 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 405 | 406 | +0.2% | -11.9 to 13.4 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 270,478 | 266,331 | -1.5% | -48,805 to 40,511 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.202 | -11.0% | -0.111 to 0.0604 | STEADY, no difference beyond the noise |
| host CPU-seconds | 165 | 142 | -14.0% | -102 to 55.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.31 | 0.266 | -14.0% | -0.192 to 0.105 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.5 | 81.9 | -0.6% | -2.85 to 1.78 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81.5 | 80.7 | -1.0% | -3.12 to 1.57 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.25 | +23.8% | 0.198 to 0.285 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 165 | 142 | -14.0% | -102 to 55.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
