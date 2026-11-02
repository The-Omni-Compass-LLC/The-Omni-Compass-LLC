# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,870 | 2,872 | +0.1% | -10.4 to 14.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,882 | 2,885 | +0.1% | -9.66 to 14.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.377 | 0.362 | -4.1% | -0.0191 to -0.0115 | GAIN |
| latency, 99th percentile (ms) | 0.658 | 0.663 | +0.8% | -0.00587 to 0.0165 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.222 | -1.3% | -0.0056 to -0.000424 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,485 | +190.0% | 720 to 1,225 | power given |
| bytes in the cache, mean (MB) | 417 | 1,158 | +177.4% | 567 to 914 | power given |
| pages read into the cache (misses) | 678,094 | 211,037 | -68.9% | -669,278 to -264,836 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.254 | +5.6% | -0.034 to 0.061 | STEADY, no difference beyond the noise |
| host CPU-seconds | 415 | 447 | +7.9% | -77.3 to 143 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.313 | 0.337 | +7.8% | -0.0598 to 0.109 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 8.67 |  | -3.07 to 20.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 274 | 269 | -1.8% | -9.4 to -0.691 | GAIN |
| the server's own CPU-seconds (mongod) | 272 | 266 | -2.1% | -10.3 to -1.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.56 | 3.32 | +29.7% | 0.528 to 0.991 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 415 | 447 | +7.9% | -77.3 to 143 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
