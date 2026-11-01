# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,933 | -0.0% | -3.48 to 0.88 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,937 | -0.0% | -3.63 to 1.71 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.151 | 0.157 | +4.2% | -0.0219 to 0.0346 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.349 | 0.359 | +2.8% | -0.0305 to 0.0498 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0796 | 0.0802 | +0.8% | -0.00646 to 0.00776 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 745 | +45.5% | 82.9 to 383 | power given |
| bytes in the cache, mean (MB) | 419 | 595 | +41.9% | 68.6 to 283 | power given |
| pages read into the cache (misses) | 696,189 | 462,299 | -33.6% | -366,542 to -101,238 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.115 | -13.3% | -0.0924 to 0.0571 | STEADY, no difference beyond the noise |
| host CPU-seconds | 245 | 207 | -15.5% | -192 to 116 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.183 | 0.155 | -15.5% | -0.143 to 0.0865 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 105 | 106 | +1.1% | -10.8 to 13 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 103 | 104 | +0.5% | -11.3 to 12.2 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.63 | 2.29 | +40.4% | 0.445 to 0.875 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 245 | 207 | -15.5% | -192 to 116 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
