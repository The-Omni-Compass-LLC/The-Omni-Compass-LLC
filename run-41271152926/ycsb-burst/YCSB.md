# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,884 | -0.1% | -6.71 to 2.05 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.1% | -4.23 to 1.05 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.486 | 0.493 | +1.4% | 0.000415 to 0.0129 | LOSS |
| latency, 99th percentile (ms) | 0.619 | 0.628 | +1.5% | -0.00415 to 0.0221 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.216 | +0.8% | -0.00336 to 0.00661 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 617 | +20.5% | -158 to 368 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 404 | 485 | +20.0% | -117 to 279 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 275,028 | 248,572 | -9.6% | -118,459 to 65,548 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.173 | -2.8% | -0.103 to 0.0929 | STEADY, no difference beyond the noise |
| host CPU-seconds | 123 | 119 | -3.7% | -86.6 to 77.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.223 | -3.6% | -0.162 to 0.146 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 77.7 | 77.7 | +0.1% | -4.14 to 4.24 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 76.8 | 76.6 | -0.2% | -4.4 to 4.07 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.92 | 1.13 | +23.2% | 0.147 to 0.28 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 123 | 119 | -3.7% | -86.5 to 77.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
