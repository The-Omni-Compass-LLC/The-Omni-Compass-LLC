# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,880 | -0.0% | -6.17 to 4.98 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -6.39 to 4.66 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.433 | 0.433 | +0.1% | -0.0109 to 0.0115 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.612 | 0.605 | -1.1% | -0.0436 to 0.0296 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.217 | 0.219 | +0.8% | -0.000375 to 0.00372 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 402 | 403 | +0.1% | -15.4 to 16.3 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 263,950 | 277,379 | +5.1% | -1,767 to 28,625 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.192 | +3.3% | -0.0426 to 0.0548 | STEADY, no difference beyond the noise |
| host CPU-seconds | 128 | 132 | +3.3% | -36.3 to 44.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.241 | 0.249 | +3.4% | -0.0681 to 0.0843 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 81.8 | 82.6 | +1.0% | 0.135 to 1.44 | power given |
| the server's own CPU-seconds (mongod) | 80.8 | 81.3 | +0.7% | -0.013 to 1.13 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.23 | +22.6% | 0.146 to 0.309 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 128 | 132 | +3.3% | -36.4 to 44.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
