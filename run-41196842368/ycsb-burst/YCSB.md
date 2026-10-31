# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,878 | -0.0% | -3.56 to 2.78 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,886 | -0.0% | -3.18 to 2.93 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.431 | 0.437 | +1.2% | 0.0039 to 0.00677 | LOSS |
| latency, 99th percentile (ms) | 0.601 | 0.614 | +2.1% | -0.0115 to 0.0368 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.22 | 0.223 | +1.0% | -0.000514 to 0.0049 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 399 | 403 | +1.2% | -4.31 to 13.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 258,674 | 256,453 | -0.9% | -7,699 to 3,257 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.219 | +9.4% | -0.0357 to 0.0732 | EVEN, no difference beyond the noise |
| host CPU-seconds | 140 | 156 | +11.4% | -31.8 to 63.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.293 | +11.4% | -0.0596 to 0.12 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 83 | 84.3 | +1.6% | -0.9 to 3.51 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 82 | 83 | +1.3% | -1.16 to 3.26 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.05 | 1.3 | +23.9% | 0.157 to 0.343 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 140 | 156 | +11.4% | -31.8 to 63.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
