# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,900 | +0.1% | -2.78 to 8.6 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,910 | +0.1% | -0.264 to 5.63 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.343 | 0.324 | -5.6% | -0.0504 to 0.0117 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.587 | 0.568 | -3.2% | -0.0645 to 0.0265 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.158 | 0.147 | -7.0% | -0.0145 to -0.00749 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,341 | +162.0% | 402 to 1,257 | power given |
| bytes in the cache, mean (MB) | 417 | 1,043 | +150.4% | 306 to 947 | power given |
| pages read into the cache (misses) | 673,134 | 180,558 | -73.2% | -638,145 to -347,008 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.204 | -1.0% | -0.0442 to 0.0399 | STEADY, no difference beyond the noise |
| host CPU-seconds | 379 | 379 | -0.1% | -102 to 101 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.285 | 0.285 | -0.1% | -0.0766 to 0.0759 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 12.3 |  | 2.29 to 22.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 190 | 175 | -7.6% | -24.1 to -4.76 | GAIN |
| the server's own CPU-seconds (mongod) | 187 | 172 | -8.0% | -24.5 to -5.39 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.43 | 2.96 | +21.9% | 0.437 to 0.627 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 379 | 379 | -0.1% | -102 to 101 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
