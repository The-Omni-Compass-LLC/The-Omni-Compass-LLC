# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,897 | +0.1% | -2.86 to 5.95 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,907 | +0.0% | -5.03 to 7.03 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.346 | 0.34 | -1.8% | -0.0101 to -0.00254 | GAIN |
| latency, 99th percentile (ms) | 0.596 | 0.587 | -1.4% | -0.0545 to 0.0378 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.162 | 0.154 | -4.8% | -0.0106 to -0.00489 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,454 | +184.0% | 743 to 1,141 | power given |
| bytes in the cache, mean (MB) | 417 | 1,119 | +168.1% | 519 to 884 | power given |
| pages read into the cache (misses) | 679,376 | 168,063 | -75.3% | -595,550 to -427,077 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.183 | -10.4% | -0.116 to 0.0735 | STEADY, no difference beyond the noise |
| host CPU-seconds | 372 | 326 | -12.6% | -267 to 174 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.28 | 0.245 | -12.6% | -0.201 to 0.131 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 20.3 |  | 6.21 to 34.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 194 | 183 | -5.6% | -15.8 to -6.01 | GAIN |
| the server's own CPU-seconds (mongod) | 192 | 180 | -6.0% | -16.5 to -6.62 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.45 | 3.12 | +27.3% | 0.611 to 0.728 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 372 | 326 | -12.6% | -268 to 174 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
