# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,909 | +1.0% | -103 to 163 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,915 | +1.0% | -104 to 163 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.212 | 0.207 | -2.4% | -0.014 to 0.00396 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.383 | 0.379 | -1.0% | -0.0113 to 0.00392 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.157 | 0.155 | -1.2% | -0.0396 to 0.0358 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 801 | +56.4% | -162 to 739 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 637 | +53.3% | -125 to 568 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 717,967 | 453,049 | -36.9% | -633,808 to 103,971 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.151 | -5.1% | -0.0425 to 0.0262 | EVEN, no difference beyond the noise |
| host CPU-seconds | 288 | 270 | -6.1% | -89.7 to 54.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.218 | 0.202 | -7.1% | -0.0761 to 0.045 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | -5.01 to 15.7 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 149 | 146 | -1.5% | -6.96 to 2.37 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 147 | 144 | -1.9% | -7.36 to 1.79 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.01 | 2.5 | +24.7% | 0.405 to 0.585 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 288 | 270 | -6.1% | -89.7 to 54.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
