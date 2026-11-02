# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,936 | -0.0% | -3.12 to 2.71 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,940 | -0.0% | -3.66 to 2.52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.143 | 0.148 | +3.5% | -0.0237 to 0.0337 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.383 | 0.386 | +1.0% | -0.0315 to 0.0388 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0792 | 0.0778 | -1.8% | -0.00552 to 0.00274 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 724 | +41.4% | -289 to 713 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 579 | +38.4% | -218 to 540 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 684,138 | 496,788 | -27.4% | -610,078 to 235,378 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.0859 | -19.3% | -0.0517 to 0.0106 | STEADY, no difference beyond the noise |
| host CPU-seconds | 193 | 151 | -21.5% | -109 to 26.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.144 | 0.113 | -21.5% | -0.0814 to 0.0196 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -2.97 to 6.97 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 101 | 101 | +0.6% | -7.93 to 9.2 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 99.1 | 99.2 | +0.1% | -8.42 to 8.63 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.56 | 2.09 | +34.0% | 0.478 to 0.582 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 193 | 151 | -21.5% | -109 to 26.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
