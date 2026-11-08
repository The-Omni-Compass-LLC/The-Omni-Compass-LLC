# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% | -21.8 to 17.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,907 | -0.1% | -12.9 to 9.83 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.322 | 0.327 | +1.6% | -0.0398 to 0.0498 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.54 | 0.551 | +2.0% | -0.065 to 0.087 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.174 | 0.179 | +2.9% | 0.000571 to 0.00957 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 715 | +39.6% | 70.5 to 335 | power given |
| bytes in the cache, mean (MB) | 404 | 557 | +38.0% | 59.1 to 248 | power given |
| pages read into the cache (misses) | 277,488 | 227,924 | -17.9% | -87,240 to -11,889 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.151 | -17.0% | -0.114 to 0.0518 | STEADY, no difference beyond the noise |
| host CPU-seconds | 133 | 107 | -19.7% | -97.7 to 45.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.25 | 0.201 | -19.7% | -0.183 to 0.0845 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -0.484 to 4.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 65.1 | 64.9 | -0.3% | -3.8 to 3.45 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 64.2 | 63.8 | -0.6% | -4.07 to 3.25 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.894 | 1.12 | +25.7% | 0.194 to 0.267 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 133 | 107 | -19.7% | -97.7 to 45.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
