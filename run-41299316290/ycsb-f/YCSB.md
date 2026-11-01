# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,679 | 5,673 | -0.1% | -31.7 to 21.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,696 | 5,690 | -0.1% | -33 to 22 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.43 | 0.423 | -1.6% | -0.0136 to -0.000427 | GAIN |
| latency, 99th percentile (ms) | 0.655 | 0.648 | -1.0% | -0.0194 to 0.00608 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.246 | 0.242 | -1.8% | -0.00734 to -0.00173 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,404 | +174.1% | 761 to 1,023 | power given |
| bytes in the cache, mean (MB) | 416 | 1,098 | +163.6% | 582 to 781 | power given |
| pages read into the cache (misses) | 685,459 | 257,458 | -62.4% | -480,534 to -375,468 | shown, not judged |
| host CPU busy (share of the run) | 0.328 | 0.324 | -1.4% | -0.038 to 0.029 | STEADY, no difference beyond the noise |
| host CPU-seconds | 597 | 588 | -1.4% | -95.8 to 78.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.225 | 0.222 | -1.3% | -0.0349 to 0.0289 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 353 | 344 | -2.6% | -19.1 to 0.943 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 349 | 339 | -2.8% | -19.5 to 0.0751 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.45 | 5.09 | +14.3% | 0.333 to 0.944 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 597 | 588 | -1.4% | -95.8 to 78.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
