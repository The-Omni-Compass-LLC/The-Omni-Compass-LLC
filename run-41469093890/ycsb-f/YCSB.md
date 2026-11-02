# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,731 | 5,712 | -0.3% | -167 to 130 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,747 | 5,729 | -0.3% | -168 to 132 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.316 | -2.4% | -0.0115 to -0.00387 | GAIN |
| latency, 99th percentile (ms) | 0.493 | 0.492 | -0.3% | -0.0125 to 0.00987 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.19 | +0.4% | -0.0199 to 0.0213 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,063 | +107.6% | -152 to 1,255 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 775 | +86.3% | -28.3 to 746 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 687,343 | 316,731 | -53.9% | -686,369 to -54,855 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.249 | -2.4% | -0.0447 to 0.0326 | STEADY, no difference beyond the noise |
| host CPU-seconds | 467 | 456 | -2.2% | -103 to 82.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.175 | 0.172 | -1.9% | -0.0361 to 0.0294 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 24 |  | -24.9 to 72.9 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 275 | 268 | -2.6% | -19.5 to 4.98 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 272 | 264 | -2.9% | -20.4 to 4.82 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.6 | 4.15 | +15.1% | 0.0941 to 0.997 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 467 | 456 | -2.2% | -103 to 82.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
