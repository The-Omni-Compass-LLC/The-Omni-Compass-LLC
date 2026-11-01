# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `f3b70b287c67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,881 | -0.0% | -1.01 to -0.557 | LOSS |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -1.33 to -0.316 | LOSS |
| latency, 95th percentile (ms) | 0.341 | 0.344 | +1.0% | -0.00465 to 0.0113 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.533 | 0.535 | +0.5% | -0.0117 to 0.017 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.205 | 0.205 | +0.0% | -0.00532 to 0.00542 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.1% | -7.79 to 5.92 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,166 | 63,245 | +0.1% | -1,300 to 1,459 | shown, not judged |
| host CPU busy (share of the run) | 0.223 | 0.224 | +0.3% | -0.0643 to 0.0658 | STEADY, no difference beyond the noise |
| host CPU-seconds | 389 | 392 | +0.8% | -145 to 151 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.293 | 0.295 | +0.8% | -0.109 to 0.114 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 233 | 233 | +0.0% | -7.75 to 7.82 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 230 | 230 | -0.0% | -7.8 to 7.63 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 2.6 | +4.8% | 0.0209 to 0.219 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 389 | 392 | +0.7% | -145 to 151 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
