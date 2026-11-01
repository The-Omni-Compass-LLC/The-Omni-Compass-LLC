# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,687 | 5,686 | -0.0% | -33.3 to 31.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,705 | 5,703 | -0.0% | -33.9 to 30.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.43 | 0.425 | -1.2% | -0.0116 to 0.00157 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.663 | 0.657 | -0.8% | -0.0228 to 0.0121 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.246 | 0.242 | -1.6% | -0.00632 to -0.00174 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,293 | +152.5% | 489 to 1,073 | power given |
| bytes in the cache, mean (MB) | 416 | 1,015 | +143.7% | 379 to 818 | power given |
| pages read into the cache (misses) | 684,308 | 301,784 | -55.9% | -418,356 to -346,692 | shown, not judged |
| host CPU busy (share of the run) | 0.323 | 0.322 | -0.6% | -0.0165 to 0.0129 | STEADY, no difference beyond the noise |
| host CPU-seconds | 585 | 582 | -0.6% | -37.7 to 31.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.219 | -0.5% | -0.0152 to 0.0128 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | -0.505 to 9.84 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 351 | 344 | -2.0% | -10 to -4.31 | GAIN |
| the server's own CPU-seconds (mongod) | 347 | 339 | -2.2% | -10.7 to -4.84 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.22 | 4.82 | +14.3% | 0.494 to 0.711 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 585 | 582 | -0.6% | -37.7 to 31.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
