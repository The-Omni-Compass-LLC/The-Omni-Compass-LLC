# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,907 | -0.0% | -6.4 to 4.83 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,910 | -0.0% | -5.7 to 4.63 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.302 | +0.3% | -0.0358 to 0.0378 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.502 | 0.515 | +2.5% | -0.0104 to 0.0358 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.131 | 0.129 | -1.3% | -0.0113 to 0.00794 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 742 | +45.0% | 116 to 345 | power given |
| bytes in the cache, mean (MB) | 418 | 594 | +42.2% | 90 to 263 | power given |
| pages read into the cache (misses) | 720,324 | 468,486 | -35.0% | -364,204 to -139,472 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.154 | +3.3% | -0.038 to 0.0478 | STEADY, no difference beyond the noise |
| host CPU-seconds | 269 | 280 | +4.2% | -83.1 to 106 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.21 | +4.2% | -0.0623 to 0.0793 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 120 | 116 | -3.0% | -14 to 6.83 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 117 | 113 | -3.6% | -14.5 to 5.99 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.4 | 3.07 | +27.9% | 0.463 to 0.875 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 269 | 280 | +4.2% | -83.1 to 106 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
