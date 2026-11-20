# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,910 | +0.0% | -0.613 to 1.52 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,913 | +0.0% | -0.469 to 1.36 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.282 | 0.28 | -0.6% | -0.0174 to 0.0141 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.477 | 0.477 | +0.1% | -0.027 to 0.0277 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.125 | 0.124 | -0.6% | -0.0026 to 0.00107 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 418 | -0.7% | -6.54 to 0.381 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 726,283 | 701,537 | -3.4% | -101,242 to 51,749 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.145 | -11.8% | -0.0489 to 0.0102 | STEADY, no difference beyond the noise |
| host CPU-seconds | 303 | 261 | -13.7% | -103 to 19.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.196 | -13.7% | -0.0771 to 0.015 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 115 | 115 | -0.4% | -2.62 to 1.69 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 113 | 112 | -0.9% | -3.18 to 1.08 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.33 | 2.92 | +25.1% | 0.491 to 0.683 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 303 | 261 | -13.7% | -103 to 19.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
