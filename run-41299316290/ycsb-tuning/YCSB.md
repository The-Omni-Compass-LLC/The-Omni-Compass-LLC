# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,897 | -0.0% | -7.05 to 5.66 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,909 | +0.0% | -3.39 to 5.37 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.239 | 0.231 | -3.6% | -0.034 to 0.0167 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.455 | 0.453 | -0.4% | -0.0473 to 0.0433 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.174 | 0.172 | -1.1% | -0.0217 to 0.0179 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,114 | +117.5% | -134 to 1,338 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 844 | +102.2% | -76.3 to 929 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 676,860 | 262,877 | -61.2% | -744,610 to -83,355 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.215 | +8.3% | -0.0894 to 0.123 | STEADY, no difference beyond the noise |
| host CPU-seconds | 355 | 398 | +12.2% | -193 to 280 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.266 | 0.299 | +12.2% | -0.145 to 0.211 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 25.7 |  | -5.79 to 57.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 218 | 211 | -3.4% | -18.1 to 3.12 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 216 | 208 | -3.7% | -18.6 to 2.52 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.2 | 2.75 | +24.6% | 0.285 to 0.801 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 355 | 398 | +12.2% | -193 to 280 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
