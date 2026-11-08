# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,886 | -0.5% | -69.9 to 41.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,897 | -0.4% | -68.3 to 42.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.227 | 0.225 | -0.9% | -0.0232 to 0.0192 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.429 | 0.437 | +2.0% | -0.00359 to 0.0209 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.178 | 0.174 | -2.3% | -0.0269 to 0.0185 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,200 | +134.3% | 386 to 989 | power given |
| bytes in the cache, mean (MB) | 416 | 901 | +116.8% | 309 to 662 | power given |
| pages read into the cache (misses) | 682,025 | 223,246 | -67.3% | -573,035 to -344,523 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.195 | +1.1% | -0.0148 to 0.019 | STEADY, no difference beyond the noise |
| host CPU-seconds | 344 | 350 | +1.8% | -31.4 to 43.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.258 | 0.264 | +2.4% | -0.0231 to 0.0353 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 30 |  | -5.22 to 65.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 215 | 208 | -3.0% | -12.5 to -0.329 | GAIN |
| the server's own CPU-seconds (mongod) | 213 | 206 | -3.3% | -13 to -1.04 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.17 | 2.82 | +29.6% | 0.569 to 0.719 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 344 | 350 | +1.8% | -31.5 to 43.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
