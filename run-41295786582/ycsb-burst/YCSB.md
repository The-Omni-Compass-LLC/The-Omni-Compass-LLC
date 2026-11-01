# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,890 | +0.0% | -2.04 to 3.02 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,893 | +0.0% | -2.17 to 3.42 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.363 | 0.365 | +0.5% | 0.000232 to 0.0031 | LOSS |
| latency, 99th percentile (ms) | 0.487 | 0.488 | +0.2% | -0.00796 to 0.00996 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.193 | +0.2% | -0.00283 to 0.00353 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 405 | 404 | -0.2% | -11.2 to 9.87 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 279,363 | 268,800 | -3.8% | -39,352 to 18,227 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.22 | +6.3% | -0.0461 to 0.0721 | STEADY, no difference beyond the noise |
| host CPU-seconds | 150 | 161 | +7.7% | -41.7 to 64.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.303 | +7.7% | -0.0782 to 0.121 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 78 | 77.9 | -0.1% | -0.948 to 0.83 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 77 | 76.8 | -0.4% | -1.13 to 0.585 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.959 | 1.17 | +22.4% | 0.17 to 0.258 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 150 | 161 | +7.7% | -41.7 to 64.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
