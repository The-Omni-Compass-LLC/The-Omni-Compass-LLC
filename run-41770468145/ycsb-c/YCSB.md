# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | +0.0% | -1.99 to 2.79 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | +0.0% | -1.8 to 2.51 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.311 | 0.309 | -0.4% | -0.00759 to 0.00492 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.471 | 0.467 | -0.7% | -0.0177 to 0.011 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.191 | -0.1% | -0.0045 to 0.00414 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 419 | 421 | +0.4% | -2.36 to 5.91 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 730,234 | 725,901 | -0.6% | -104,806 to 96,138 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.189 | -2.6% | -0.0378 to 0.0277 | STEADY, no difference beyond the noise |
| host CPU-seconds | 339 | 328 | -3.3% | -84.2 to 61.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.246 | -3.4% | -0.0632 to 0.0462 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 189 | 189 | +0.3% | -4.93 to 5.91 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 186 | 186 | -0.0% | -5.36 to 5.18 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.6 | 3.18 | +22.2% | 0.411 to 0.746 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 339 | 328 | -3.3% | -84.2 to 61.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
