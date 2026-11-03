# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,883 | +0.1% | -5.71 to 11.2 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,891 | +0.1% | -5.56 to 10.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.337 | -2.0% | -0.0136 to -0.000427 | GAIN |
| latency, 99th percentile (ms) | 0.535 | 0.517 | -3.4% | -0.0392 to 0.00323 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.203 | -3.2% | -0.0106 to -0.00296 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,403 | +174.1% | 800 to 983 | power given |
| bytes in the cache, mean (MB) | 418 | 1,101 | +163.7% | 616 to 751 | power given |
| pages read into the cache (misses) | 673,212 | 280,769 | -58.3% | -464,525 to -320,361 | shown, not judged |
| host CPU busy (share of the run) | 0.258 | 0.252 | -2.4% | -0.0885 to 0.0761 | STEADY, no difference beyond the noise |
| host CPU-seconds | 465 | 453 | -2.6% | -207 to 183 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.35 | 0.341 | -2.7% | -0.157 to 0.138 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 3.9 to 6.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 264 | -3.1% | -14.1 to -2.81 | GAIN |
| the server's own CPU-seconds (mongod) | 270 | 261 | -3.4% | -14.6 to -3.62 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.57 | 3.25 | +26.3% | 0.542 to 0.814 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 465 | 453 | -2.6% | -207 to 183 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
