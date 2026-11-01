# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,877 | 2,876 | -0.0% | -7.12 to 6.35 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -1.2 to 0.787 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.508 | 0.513 | +0.9% | -0.0162 to 0.0255 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.671 | 0.685 | +2.0% | -0.0787 to 0.106 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.227 | 0.229 | +0.9% | -0.00644 to 0.0104 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 547 | +6.8% | -40.4 to 110 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 400 | 431 | +7.7% | -23.8 to 85.2 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 272,417 | 266,553 | -2.2% | -55,177 to 43,449 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.207 | +0.2% | -0.0885 to 0.0894 | STEADY, no difference beyond the noise |
| host CPU-seconds | 147 | 146 | -0.2% | -80 to 79.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.276 | -0.2% | -0.15 to 0.149 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 81.3 | 82.3 | +1.3% | -2.94 to 4.99 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 80.2 | 81 | +1.0% | -3.08 to 4.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.25 | +23.6% | 0.0895 to 0.388 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 147 | 146 | -0.2% | -80 to 79.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
