# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,897 | -0.0% | -0.803 to -0.317 | LOSS |
| throughput (operations a second) | 2,907 | 2,906 | -0.0% | -1.57 to -0.104 | LOSS |
| latency, 95th percentile (ms) | 0.442 | 0.441 | -0.2% | -0.00692 to 0.00559 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.649 | 0.646 | -0.4% | -0.0141 to 0.00881 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.16 | 0.158 | -1.5% | -0.00766 to 0.003 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 578 | +13.0% | -76.4 to 209 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 404 | 458 | +13.3% | -60.2 to 168 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 273,501 | 256,588 | -6.2% | -48,857 to 15,031 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.121 | -33.4% | -0.222 to 0.101 | STEADY, no difference beyond the noise |
| host CPU-seconds | 139 | 84.7 | -39.0% | -195 to 86.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.261 | 0.159 | -39.0% | -0.366 to 0.162 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 51.2 | 50.6 | -1.1% | -2.78 to 1.64 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 50.2 | 49.4 | -1.6% | -3.02 to 1.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.97 | 1.21 | +24.7% | 0.178 to 0.302 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 139 | 84.7 | -39.0% | -195 to 86.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
