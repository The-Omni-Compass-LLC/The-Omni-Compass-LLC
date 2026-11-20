# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,903 | -0.0% | -5.48 to 3.46 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,912 | -0.0% | -2.63 to 1.36 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.223 | 0.222 | -0.3% | -0.0206 to 0.0193 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.423 | 0.424 | +0.2% | -0.0272 to 0.0292 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.163 | 0.16 | -1.4% | -0.0132 to 0.00857 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 818 | +59.7% | -15.1 to 626 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 648 | +55.0% | -14.7 to 474 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 676,888 | 417,798 | -38.3% | -472,936 to -45,243 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.2 | +6.1% | -0.0313 to 0.0542 | STEADY, no difference beyond the noise |
| host CPU-seconds | 335 | 361 | +7.7% | -68.7 to 121 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.251 | 0.271 | +7.8% | -0.052 to 0.0909 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.67 |  | -13 to 28.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 212 | 210 | -0.8% | -6.44 to 2.91 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 209 | 207 | -1.1% | -6.95 to 2.32 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.1 | 2.65 | +26.1% | 0.458 to 0.639 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 335 | 361 | +7.7% | -68.7 to 121 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
