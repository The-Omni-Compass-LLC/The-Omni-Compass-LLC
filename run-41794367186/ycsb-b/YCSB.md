# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% | -3.31 to 2.68 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,889 | -0.0% | -3.1 to 2.57 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.335 | 0.336 | +0.2% | -0.00692 to 0.00826 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.523 | 0.523 | +0.1% | -0.0122 to 0.0128 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.199 | +0.2% | -0.00313 to 0.0038 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 417 | 418 | +0.3% | -3.74 to 6.08 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 695,381 | 710,117 | +2.1% | -31,488 to 60,960 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.217 | +14.3% | -0.0294 to 0.0836 | STEADY, no difference beyond the noise |
| host CPU-seconds | 328 | 387 | +18.0% | -63 to 181 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.247 | 0.291 | +18.0% | -0.0473 to 0.136 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 201 | 202 | +0.3% | -3.83 to 4.92 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 199 | 198 | -0.0% | -4.51 to 4.33 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.57 | 3.2 | +24.7% | 0.584 to 0.683 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 328 | 387 | +18.0% | -63 to 181 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
