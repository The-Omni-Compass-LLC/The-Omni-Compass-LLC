# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,914 | 2,912 | -0.1% | -6.79 to 3.81 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,915 | -0.1% | -6.87 to 3.89 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.178 | 0.178 | +0.2% | -0.00254 to 0.0032 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.34 | 0.341 | +0.3% | -0.0238 to 0.0258 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.127 | 0.128 | +0.7% | -0.00236 to 0.00422 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | -0.1% | -7.02 to 5.24 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,649 | 61,629 | -0.0% | -228 to 187 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.133 | -9.8% | -0.0605 to 0.0316 | STEADY, no difference beyond the noise |
| host CPU-seconds | 268 | 236 | -11.8% | -133 to 69.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.201 | 0.177 | -11.8% | -0.0994 to 0.0523 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 127 | 127 | -0.1% | -3.07 to 2.74 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 125 | 125 | -0.2% | -3.19 to 2.71 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.94 | 2.01 | +4.0% | -0.0332 to 0.187 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 268 | 236 | -11.8% | -133 to 69.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
