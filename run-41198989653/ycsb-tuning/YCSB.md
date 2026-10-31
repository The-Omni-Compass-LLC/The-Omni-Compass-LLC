# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,871 | 2,872 | +0.0% | -20.9 to 23.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,883 | 2,884 | +0.0% | -19.4 to 21.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.379 | 0.365 | -3.9% | -0.0223 to -0.00708 | GAIN |
| latency, 99th percentile (ms) | 0.653 | 0.647 | -0.8% | -0.0219 to 0.0112 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.219 | -1.9% | -0.00792 to -0.000811 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,435 | +180.2% | 824 to 1,022 | power given |
| bytes in the cache, mean (MB) | 417 | 1,119 | +168.2% | 614 to 789 | power given |
| pages read into the cache (misses) | 671,116 | 232,465 | -65.4% | -496,959 to -380,341 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.252 | -1.6% | -0.0547 to 0.0466 | EVEN, no difference beyond the noise |
| host CPU-seconds | 453 | 446 | -1.6% | -124 to 109 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.342 | 0.336 | -1.6% | -0.0909 to 0.0799 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.67 |  | 2.5 to 12.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 267 | -2.4% | -19.2 to 5.91 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 271 | 263 | -2.7% | -19.8 to 5.26 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 3.17 | +25.7% | 0.598 to 0.698 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 453 | 446 | -1.6% | -124 to 109 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
