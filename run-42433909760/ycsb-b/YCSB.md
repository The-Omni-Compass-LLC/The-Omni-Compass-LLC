# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,909 | +0.1% | -4.51 to 8.92 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,914 | +0.1% | -4.13 to 8.73 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.221 | 0.215 | -2.4% | -0.0222 to 0.0116 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.388 | 0.389 | +0.3% | -0.00557 to 0.00757 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.15 | 0.143 | -4.4% | -0.0144 to 0.00108 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 981 | +91.6% | 297 to 641 | power given |
| bytes in the cache, mean (MB) | 416 | 779 | +87.1% | 232 to 493 | power given |
| pages read into the cache (misses) | 711,088 | 340,676 | -52.1% | -511,491 to -229,333 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.159 | +6.6% | 0.00333 to 0.0163 | power given |
| host CPU-seconds | 266 | 288 | +8.3% | 10.5 to 33.8 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.199 | 0.215 | +8.3% | 0.00756 to 0.0255 | power given |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 152 | 146 | -4.3% | -8.81 to -4.3 | GAIN |
| the server's own CPU-seconds (mongod) | 150 | 143 | -4.7% | -9.28 to -4.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.08 | 2.56 | +23.3% | 0.349 to 0.618 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 266 | 288 | +8.3% | 10.5 to 33.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
