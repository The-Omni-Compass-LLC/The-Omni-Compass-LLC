# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,888 | +0.1% | -0.454 to 3.42 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,892 | +0.0% | -0.473 to 3.14 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.309 | +0.2% | -0.0116 to 0.0129 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.485 | -0.3% | -0.00546 to 0.00213 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.19 | -0.1% | -0.00178 to 0.00149 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 419 | +0.0% | -4.69 to 4.7 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 689,983 | 672,749 | -2.5% | -104,765 to 70,297 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.2 | +6.9% | -0.0581 to 0.084 | STEADY, no difference beyond the noise |
| host CPU-seconds | 323 | 353 | +9.3% | -127 to 187 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.243 | 0.265 | +9.3% | -0.0951 to 0.14 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 188 | +1.0% | -4.23 to 8.11 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 185 | +0.7% | -4.97 to 7.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 3.13 | +24.5% | 0.47 to 0.76 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 323 | 353 | +9.3% | -127 to 187 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
