# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,904 | +0.0% | -1.19 to 1.19 | STEADY, the same |
| throughput (operations a second) | 2,908 | 2,908 | +0.0% | -0.909 to 0.974 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.323 | 0.323 | +0.0% | -0.0151 to 0.0151 | STEADY, the same |
| latency, 99th percentile (ms) | 0.544 | 0.544 | +0.1% | -0.0124 to 0.0131 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.135 | 0.134 | -0.8% | -0.00509 to 0.00285 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -122 to 196 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 446 | +6.7% | -92.2 to 148 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 698,018 | 650,083 | -6.9% | -228,300 to 132,431 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.158 | +7.9% | -0.0415 to 0.0647 | STEADY, no difference beyond the noise |
| host CPU-seconds | 261 | 285 | +9.5% | -86.6 to 136 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.214 | +9.5% | -0.0649 to 0.102 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 124 | 123 | -0.7% | -5.05 to 3.43 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 121 | 120 | -1.2% | -5.73 to 2.79 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.49 | 3.16 | +26.6% | 0.555 to 0.771 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 261 | 285 | +9.5% | -86.6 to 136 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
