# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,932 | 2,932 | -0.0% | -5.25 to 3.91 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,934 | 2,933 | -0.0% | -5.06 to 3.84 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.197 | 0.198 | +0.2% | -0.0011 to 0.00177 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.406 | 0.409 | +0.6% | -0.0166 to 0.0213 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.111 | 0.11 | -0.3% | -0.00338 to 0.00265 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 417 | 418 | +0.1% | -4.37 to 4.78 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 712,252 | 671,684 | -5.7% | -164,409 to 83,273 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.124 | +3.2% | -0.0143 to 0.0221 | STEADY, no difference beyond the noise |
| host CPU-seconds | 220 | 227 | +3.5% | -28.7 to 44.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.164 | 0.17 | +3.5% | -0.0215 to 0.0331 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 85.3 | 85.7 | +0.5% | -1.47 to 2.32 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 83.4 | 83.3 | -0.2% | -2.03 to 1.74 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.92 | 2.49 | +29.7% | 0.547 to 0.594 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 220 | 227 | +3.5% | -28.7 to 44.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
