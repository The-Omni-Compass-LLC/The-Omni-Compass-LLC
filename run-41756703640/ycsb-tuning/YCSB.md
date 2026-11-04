# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,873 | -0.0% | -8.39 to 7.47 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -9.2 to 7.88 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.375 | 0.365 | -2.7% | -0.0312 to 0.0112 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.661 | 0.654 | -1.0% | -0.0592 to 0.0458 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.22 | -2.2% | -0.0133 to 0.0033 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,274 | +148.8% | 273 to 1,251 | power given |
| bytes in the cache, mean (MB) | 417 | 1,003 | +140.2% | 211 to 959 | power given |
| pages read into the cache (misses) | 678,110 | 325,806 | -52.0% | -509,336 to -195,271 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.255 | -4.8% | -0.0539 to 0.028 | STEADY, no difference beyond the noise |
| host CPU-seconds | 478 | 449 | -6.1% | -129 to 70.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.361 | 0.339 | -6.1% | -0.0966 to 0.0524 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.67 |  | -1.5 to 12.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 277 | 270 | -2.5% | -20.4 to 6.59 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 275 | 267 | -2.8% | -21.1 to 5.9 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.29 | +26.4% | 0.617 to 0.758 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 478 | 449 | -6.1% | -129 to 70.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
