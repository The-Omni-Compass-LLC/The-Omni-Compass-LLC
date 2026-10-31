# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,907 | +0.0% | -1.49 to 1.82 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,912 | +0.0% | 0.0601 to 0.468 | GAIN |
| latency, 95th percentile (ms) | 0.236 | 0.23 | -2.5% | -0.0473 to 0.0353 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.4 | 0.396 | -1.0% | -0.0464 to 0.0384 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.149 | -3.0% | -0.0133 to 0.00389 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 893 | +74.4% | 151 to 610 | power given |
| bytes in the cache, mean (MB) | 417 | 709 | +70.1% | 111 to 473 | power given |
| pages read into the cache (misses) | 703,721 | 412,165 | -41.4% | -407,916 to -175,195 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.152 | -4.6% | -0.0588 to 0.0443 | EVEN, no difference beyond the noise |
| host CPU-seconds | 287 | 271 | -5.4% | -130 to 98.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.203 | -5.4% | -0.0972 to 0.0738 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | -0.462 to 7.13 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 153 | 148 | -3.3% | -7.42 to -2.82 | GAIN |
| the server's own CPU-seconds (mongod) | 151 | 146 | -3.8% | -8.01 to -3.39 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.1 | 2.67 | +27.6% | 0.533 to 0.623 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 287 | 271 | -5.4% | -130 to 98.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
