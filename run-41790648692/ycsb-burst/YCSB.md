# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,937 | -0.0% | -5.21 to 4.01 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,940 | -0.0% | -5.41 to 4.14 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.235 | 0.241 | +2.6% | -0.0157 to 0.0277 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.369 | 0.393 | +6.4% | 0.00502 to 0.0423 | LOSS |
| latency, mean (ms) | 0.0762 | 0.0785 | +3.0% | 0.000151 to 0.00446 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 405 | 406 | +0.2% | -11.9 to 13.6 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 259,371 | 264,783 | +2.1% | 1,220 to 9,604 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.0656 | -41.4% | -0.193 to 0.1 | STEADY, no difference beyond the noise |
| host CPU-seconds | 85.7 | 46.4 | -45.9% | -164 to 85.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.16 | 0.0866 | -45.9% | -0.307 to 0.16 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 24.4 | 25.3 | +3.9% | 0.346 to 1.57 | power given |
| the server's own CPU-seconds (mongod) | 23.8 | 24.5 | +3.2% | 0.177 to 1.33 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.629 | 0.832 | +32.2% | 0.162 to 0.243 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 85.7 | 46.4 | -45.9% | -164 to 85.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
