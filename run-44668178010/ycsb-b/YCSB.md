# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,909 | -0.0% | -5.66 to 3.43 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,914 | -0.0% | -5.64 to 4.82 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.21 | 0.213 | +1.7% | -0.00432 to 0.0117 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.378 | 0.386 | +2.2% | -0.0125 to 0.0292 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.149 | 0.148 | -0.5% | -0.0166 to 0.0153 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 764 | +49.3% | 45.6 to 459 | power given |
| bytes in the cache, mean (MB) | 419 | 608 | +45.0% | 39.7 to 338 | power given |
| pages read into the cache (misses) | 724,651 | 498,247 | -31.2% | -517,881 to 65,073 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.167 | +7.0% | -0.0234 to 0.0453 | STEADY, no difference beyond the noise |
| host CPU-seconds | 281 | 304 | +8.1% | -48.9 to 94.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.228 | +8.1% | -0.0364 to 0.0707 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 152 | 150 | -1.4% | -5.46 to 1.28 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 150 | 147 | -1.8% | -6.08 to 0.774 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2 | 2.57 | +28.3% | 0.505 to 0.627 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 281 | 304 | +8.1% | -48.9 to 94.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
