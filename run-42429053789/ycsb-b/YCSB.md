# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,910 | -0.0% | -2.02 to 1.29 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,915 | -0.0% | -0.546 to -0.124 | LOSS |
| latency, 95th percentile (ms) | 0.207 | 0.208 | +0.5% | -0.0119 to 0.0139 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.37 | 0.374 | +1.3% | -0.00654 to 0.0159 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.145 | 0.144 | -0.7% | -0.00915 to 0.00719 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 531 | +3.8% | -64.2 to 103 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 433 | +3.2% | -47.7 to 74.8 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 699,004 | 654,138 | -6.4% | -240,067 to 150,334 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.145 | -1.3% | -0.0216 to 0.0179 | STEADY, no difference beyond the noise |
| host CPU-seconds | 261 | 257 | -1.4% | -43.4 to 36.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.195 | 0.193 | -1.4% | -0.0326 to 0.0272 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 149 | 149 | -0.0% | -3.15 to 3.07 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 147 | 146 | -0.4% | -3.78 to 2.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.01 | 2.56 | +27.3% | 0.433 to 0.667 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 261 | 257 | -1.4% | -43.4 to 36.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
