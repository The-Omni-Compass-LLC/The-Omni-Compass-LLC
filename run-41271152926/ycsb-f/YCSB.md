# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,678 | 5,673 | -0.1% | -35.7 to 25.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,695 | 5,690 | -0.1% | -32.7 to 23.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.436 | 0.432 | -1.0% | -0.0161 to 0.00741 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.657 | 0.658 | +0.1% | -0.0346 to 0.0352 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.25 | 0.246 | -1.4% | -0.00911 to 0.00229 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,321 | +158.0% | 348 to 1,270 | power given |
| bytes in the cache, mean (MB) | 416 | 1,036 | +148.8% | 275 to 964 | power given |
| pages read into the cache (misses) | 680,364 | 287,126 | -57.8% | -606,540 to -179,936 | shown, not judged |
| host CPU busy (share of the run) | 0.333 | 0.334 | +0.2% | -0.0144 to 0.0158 | STEADY, no difference beyond the noise |
| host CPU-seconds | 603 | 608 | +0.8% | -24.4 to 33.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.229 | +0.8% | -0.0097 to 0.0135 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 358 | 352 | -1.6% | -12.7 to 1.14 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 354 | 347 | -1.8% | -12.9 to -0.172 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.47 | 5.23 | +17.0% | 0.21 to 1.31 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 603 | 608 | +0.8% | -24.4 to 33.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
