# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,752 | 5,753 | +0.0% | -3.78 to 5.43 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,767 | 5,768 | +0.0% | -2.53 to 4.71 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.311 | -2.2% | -0.0136 to -0.000427 | GAIN |
| latency, 99th percentile (ms) | 0.48 | 0.473 | -1.5% | -0.0276 to 0.0129 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.178 | -1.4% | -0.0036 to -0.00133 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 996 | +94.6% | 298 to 670 | power given |
| bytes in the cache, mean (MB) | 418 | 785 | +87.7% | 232 to 502 | power given |
| pages read into the cache (misses) | 687,160 | 307,967 | -55.2% | -523,974 to -234,411 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.246 | +0.2% | -0.0297 to 0.0307 | STEADY, no difference beyond the noise |
| host CPU-seconds | 444 | 447 | +0.7% | -68.6 to 74.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.166 | 0.167 | +0.7% | -0.0255 to 0.0277 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | -2.84 to 11.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 271 | 265 | -2.1% | -7.23 to -4.32 | GAIN |
| the server's own CPU-seconds (mongod) | 268 | 261 | -2.3% | -7.74 to -4.78 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.45 | 3.93 | +14.1% | 0.267 to 0.704 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 444 | 447 | +0.7% | -68.6 to 74.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
