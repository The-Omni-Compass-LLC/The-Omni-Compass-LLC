# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,680 | 5,677 | -0.0% | -25.6 to 20.4 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,696 | 5,694 | -0.0% | -27.3 to 22 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.431 | 0.425 | -1.2% | -0.0147 to 0.00407 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.637 | 0.636 | -0.2% | -0.0165 to 0.0145 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.247 | 0.244 | -1.2% | -0.00773 to 0.0017 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,421 | +177.5% | 777 to 1,040 | power given |
| bytes in the cache, mean (MB) | 416 | 1,112 | +167.1% | 604 to 788 | power given |
| pages read into the cache (misses) | 680,718 | 243,687 | -64.2% | -490,913 to -383,150 | shown, not judged |
| host CPU busy (share of the run) | 0.327 | 0.329 | +0.5% | -0.0197 to 0.0227 | STEADY, no difference beyond the noise |
| host CPU-seconds | 589 | 596 | +1.2% | -44.2 to 58.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.222 | 0.225 | +1.3% | -0.0169 to 0.0225 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.67 |  | 0.415 to 12.9 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 356 | 350 | -1.9% | -15.3 to 1.99 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 352 | 345 | -2.1% | -15.9 to 1.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.46 | 5.15 | +15.3% | 0.51 to 0.859 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 589 | 596 | +1.2% | -44.3 to 58.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
