# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `baaf413e44d9`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | +0.0% | -1.64 to 2.74 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,891 | +0.0% | -0.993 to 2.02 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.404 | 0.406 | +0.7% | -0.0101 to 0.0154 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.547 | 0.547 | +0.1% | -0.0183 to 0.019 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.207 | +1.5% | -0.000321 to 0.00657 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,515 | 1,515 | -0.0% | -3.82 to 3.28 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,639 | 77,692 | +0.1% | -213 to 319 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.217 | +21.3% | -0.0877 to 0.164 | STEADY, no difference beyond the noise |
| host CPU-seconds | 124 | 159 | +28.4% | -80.8 to 151 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.299 | +28.4% | -0.152 to 0.284 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 75.7 | 77.3 | +2.0% | 0.412 to 2.66 | power given |
| the server's own CPU-seconds (mongod) | 74.8 | 76.3 | +2.0% | 0.313 to 2.69 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.983 | 1.02 | +3.3% | -0.0503 to 0.115 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 124 | 159 | +28.4% | -80.8 to 151 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
