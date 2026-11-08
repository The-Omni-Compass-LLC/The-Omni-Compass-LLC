# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,834 | 5,832 | -0.0% | -13.5 to 8.72 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,842 | 5,840 | -0.0% | -10.8 to 6.39 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.157 | 0.157 | +0.4% | -0.00692 to 0.00826 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.341 | 0.338 | -1.0% | -0.0268 to 0.0201 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.082 | 0.0824 | +0.5% | -0.0068 to 0.00768 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 717 | +40.0% | -272 to 682 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 575 | +37.3% | -211 to 523 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 694,218 | 510,732 | -26.4% | -628,183 to 261,210 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.128 | +2.7% | -0.0356 to 0.0423 | STEADY, no difference beyond the noise |
| host CPU-seconds | 226 | 233 | +3.1% | -78 to 92.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0845 | 0.0872 | +3.1% | -0.029 to 0.0343 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | -2.13 to 5.46 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 120 | 121 | +0.6% | -6.09 to 7.59 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 117 | 117 | +0.2% | -6.22 to 6.58 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.26 | 3.83 | +17.4% | 0.0535 to 1.08 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 226 | 233 | +3.1% | -77.9 to 92.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
