# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,665 | 5,677 | +0.2% | -7.7 to 31 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,682 | 5,694 | +0.2% | -6.92 to 30.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.435 | 0.429 | -1.3% | -0.0157 to 0.00437 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.661 | 0.659 | -0.4% | -0.0273 to 0.0227 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.249 | 0.244 | -1.7% | -0.0102 to 0.00197 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,389 | +171.3% | 619 to 1,135 | power given |
| bytes in the cache, mean (MB) | 416 | 1,087 | +161.0% | 471 to 870 | power given |
| pages read into the cache (misses) | 679,186 | 239,938 | -64.7% | -462,435 to -416,060 | shown, not judged |
| host CPU busy (share of the run) | 0.327 | 0.327 | +0.1% | -0.00558 to 0.00621 | EVEN, no difference beyond the noise |
| host CPU-seconds | 589 | 593 | +0.6% | -6.65 to 13.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.224 | +0.4% | -0.00377 to 0.00548 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.33 |  | 2.54 to 10.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 356 | 349 | -2.0% | -12.6 to -1.51 | GAIN |
| the server's own CPU-seconds (mongod) | 352 | 344 | -2.2% | -13.3 to -2.43 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.36 | 5.13 | +17.9% | 0.589 to 0.967 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 589 | 593 | +0.6% | -6.61 to 13.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
