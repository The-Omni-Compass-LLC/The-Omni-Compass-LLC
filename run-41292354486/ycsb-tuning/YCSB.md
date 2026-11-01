# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,936 | +0.0% | -5.03 to 5.48 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,938 | +0.0% | -4.64 to 5.14 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.138 | 0.144 | +4.8% | -0.0194 to 0.0328 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.344 | 0.362 | +5.3% | -0.0399 to 0.0766 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0735 | 0.0742 | +0.9% | -0.0014 to 0.00278 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,364 | -0.1% | -6.15 to 4.02 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,506 | 63,447 | -0.1% | -1,247 to 1,129 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.0925 | -20.4% | -0.132 to 0.0846 | STEADY, no difference beyond the noise |
| host CPU-seconds | 216 | 165 | -23.5% | -283 to 181 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.161 | 0.124 | -23.5% | -0.211 to 0.135 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 83.8 | 83.8 | +0.0% | -3.64 to 3.71 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 82 | 82 | -0.1% | -3.46 to 3.37 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.74 | 1.82 | +4.6% | -0.185 to 0.345 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 216 | 165 | -23.5% | -283 to 181 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
