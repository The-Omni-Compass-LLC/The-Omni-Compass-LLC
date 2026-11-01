# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,889 | -0.0% | -2.91 to 0.749 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,892 | -0.0% | -3.15 to 1.28 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.314 | +1.9% | -0.00483 to 0.0168 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.46 | +1.8% | 0.000744 to 0.0159 | LOSS |
| latency, mean (ms) | 0.179 | 0.181 | +1.0% | 0.000338 to 0.00323 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 525 | +2.5% | -42.2 to 67.8 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 429 | +2.9% | -30 to 54.5 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 714,973 | 712,157 | -0.4% | -154,134 to 148,504 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.206 | -1.1% | -0.0658 to 0.0612 | STEADY, no difference beyond the noise |
| host CPU-seconds | 378 | 370 | -2.1% | -156 to 141 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.283 | 0.278 | -2.0% | -0.117 to 0.106 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 190 | 193 | +1.5% | -0.74 to 6.35 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 188 | 190 | +1.1% | -1.58 to 5.78 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.43 | 3.13 | +28.9% | 0.539 to 0.863 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 378 | 370 | -2.1% | -156 to 141 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
