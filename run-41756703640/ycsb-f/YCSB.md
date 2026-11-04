# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,841 | 5,838 | -0.0% | -17.1 to 12.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,850 | 5,847 | -0.0% | -17.9 to 12.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.162 | 0.163 | +0.8% | -0.0123 to 0.015 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.375 | 0.373 | -0.4% | -0.0241 to 0.0207 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0848 | 0.085 | +0.2% | -0.00388 to 0.00419 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 699 | +36.6% | -295 to 669 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 562 | +34.2% | -224 to 511 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 690,223 | 536,122 | -22.3% | -568,007 to 259,805 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.13 | -2.0% | -0.0287 to 0.0235 | STEADY, no difference beyond the noise |
| host CPU-seconds | 240 | 235 | -2.5% | -59.7 to 47.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0898 | 0.0876 | -2.5% | -0.0224 to 0.018 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 122 | 124 | +1.1% | -6.59 to 9.32 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 120 | 121 | +0.6% | -6.97 to 8.49 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.62 | 3.22 | +23.1% | 0.38 to 0.829 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 240 | 235 | -2.5% | -59.7 to 47.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
