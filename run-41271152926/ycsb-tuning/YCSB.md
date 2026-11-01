# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,873 | -0.0% | -7.05 to 5.66 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -6.22 to 3.99 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.381 | 0.362 | -4.8% | -0.0555 to 0.0189 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.641 | 0.631 | -1.6% | -0.0436 to 0.0236 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.219 | -2.3% | -0.0198 to 0.00956 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,439 | +181.1% | 821 to 1,034 | power given |
| bytes in the cache, mean (MB) | 417 | 1,127 | +170.2% | 627 to 793 | power given |
| pages read into the cache (misses) | 678,061 | 237,748 | -64.9% | -515,556 to -365,070 | shown, not judged |
| host CPU busy (share of the run) | 0.259 | 0.245 | -5.7% | -0.0817 to 0.052 | STEADY, no difference beyond the noise |
| host CPU-seconds | 459 | 427 | -6.9% | -182 to 119 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.346 | 0.322 | -6.9% | -0.136 to 0.0887 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.67 |  | 1.87 to 9.46 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 275 | 268 | -2.7% | -26 to 10.9 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 272 | 264 | -3.0% | -26.3 to 10 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.18 | +21.9% | 0.275 to 0.867 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 459 | 427 | -6.9% | -182 to 119 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
