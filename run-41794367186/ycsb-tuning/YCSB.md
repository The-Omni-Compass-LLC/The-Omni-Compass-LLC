# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,870 | 2,876 | +0.2% | -5.92 to 17.1 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,884 | 2,886 | +0.1% | -11.8 to 16.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.385 | 0.352 | -8.6% | -0.0903 to 0.0243 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.641 | 0.558 | -12.9% | -0.32 to 0.154 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.229 | 0.212 | -7.4% | -0.0338 to -0.000292 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,325 | +158.9% | 287 to 1,340 | power given |
| bytes in the cache, mean (MB) | 418 | 1,042 | +149.7% | 228 to 1,022 | power given |
| pages read into the cache (misses) | 678,864 | 267,951 | -60.5% | -688,269 to -133,558 | shown, not judged |
| host CPU busy (share of the run) | 0.267 | 0.225 | -15.7% | -0.109 to 0.0257 | STEADY, no difference beyond the noise |
| host CPU-seconds | 474 | 388 | -18.3% | -240 to 65.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.358 | 0.292 | -18.4% | -0.182 to 0.0498 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 279 | 261 | -6.7% | -29 to -8.24 | GAIN |
| the server's own CPU-seconds (mongod) | 277 | 258 | -6.9% | -29.5 to -8.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.07 | +17.7% | 0.282 to 0.64 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 474 | 388 | -18.3% | -240 to 65.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
