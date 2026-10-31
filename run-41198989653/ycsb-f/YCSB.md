# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,679 | 5,682 | +0.1% | -33 to 40.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,695 | 5,699 | +0.1% | -33.8 to 41.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.439 | 0.431 | -2.0% | -0.0187 to 0.00137 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.694 | 0.691 | -0.4% | -0.0168 to 0.0108 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.245 | 0.239 | -2.2% | -0.0133 to 0.00231 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,401 | +173.7% | 702 to 1,077 | power given |
| bytes in the cache, mean (MB) | 416 | 1,095 | +163.2% | 535 to 823 | power given |
| pages read into the cache (misses) | 686,562 | 244,982 | -64.3% | -495,465 to -387,695 | shown, not judged |
| host CPU busy (share of the run) | 0.322 | 0.315 | -2.1% | -0.0171 to 0.00364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 584 | 570 | -2.3% | -40.1 to 13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.215 | -2.4% | -0.0158 to 0.0053 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 349 | 338 | -3.0% | -23.6 to 2.65 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 344 | 333 | -3.2% | -24.4 to 2.22 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.44 | 5.04 | +13.5% | 0.364 to 0.831 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 584 | 570 | -2.3% | -40.1 to 13 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
