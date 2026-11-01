# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,899 | +0.0% | -3.69 to 4.12 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,904 | 2,904 | -0.0% | -1.06 to 0.659 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.357 | 0.354 | -0.8% | -0.0307 to 0.0247 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.584 | 0.572 | -2.1% | -0.0495 to 0.0255 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.169 | 0.169 | -0.4% | -0.00697 to 0.00559 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -4.92 to 3.16 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 709,624 | 702,712 | -1.0% | -80,603 to 66,779 | shown, not judged |
| host CPU busy (share of the run) | 0.174 | 0.17 | -2.1% | -0.0229 to 0.0156 | STEADY, no difference beyond the noise |
| host CPU-seconds | 311 | 303 | -2.6% | -48.7 to 32.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.227 | -2.6% | -0.0366 to 0.0245 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 160 | 161 | +0.3% | -5.12 to 6.04 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 158 | 158 | -0.1% | -5.69 to 5.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.27 | +25.0% | 0.491 to 0.817 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 311 | 303 | -2.6% | -48.7 to 32.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
