# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,888 | -0.0% | -3.89 to 2.52 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -3.76 to 3.01 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.311 | +0.6% | -0.00545 to 0.00945 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.477 | 0.481 | +0.8% | -0.000969 to 0.00897 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.188 | 0.189 | +0.3% | -0.00565 to 0.00695 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 538 | +5.0% | -84.5 to 136 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 438 | +4.4% | -63.7 to 101 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 681,010 | 656,875 | -3.5% | -186,961 to 138,691 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.173 | -3.3% | -0.0727 to 0.0607 | STEADY, no difference beyond the noise |
| host CPU-seconds | 309 | 296 | -4.4% | -157 to 130 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.222 | -4.4% | -0.118 to 0.0972 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 185 | 186 | +0.4% | -8.69 to 10.1 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 183 | 183 | +0.1% | -9.29 to 9.51 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.45 | 3.06 | +25.0% | 0.576 to 0.65 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 309 | 296 | -4.4% | -157 to 129 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
