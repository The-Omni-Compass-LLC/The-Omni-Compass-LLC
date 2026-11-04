# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,877 | 2,875 | -0.1% | -6.84 to 2.91 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,885 | -0.1% | -6.4 to 1.61 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.363 | 0.351 | -3.2% | -0.0303 to 0.00698 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.584 | 0.568 | -2.7% | -0.0323 to 0.000291 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.214 | -3.4% | -0.0214 to 0.00623 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,357 | +165.1% | 248 to 1,442 | power given |
| bytes in the cache, mean (MB) | 418 | 1,064 | +154.9% | 200 to 1,093 | power given |
| pages read into the cache (misses) | 670,909 | 258,673 | -61.4% | -681,362 to -143,110 | shown, not judged |
| host CPU busy (share of the run) | 0.259 | 0.253 | -2.2% | -0.0646 to 0.0531 | STEADY, no difference beyond the noise |
| host CPU-seconds | 458 | 450 | -1.7% | -139 to 123 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.345 | 0.339 | -1.7% | -0.104 to 0.0923 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 0.162 to 10.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 275 | 264 | -3.9% | -31.5 to 10.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 272 | 261 | -4.2% | -32 to 9.3 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.54 | 3.15 | +24.1% | 0.342 to 0.882 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 458 | 450 | -1.7% | -139 to 123 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
