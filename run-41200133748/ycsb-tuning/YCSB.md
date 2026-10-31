# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,899 | -0.0% | -6.67 to 4.34 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,909 | -0.0% | -8.25 to 6.63 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.337 | 0.325 | -3.5% | -0.0217 to -0.00163 | GAIN |
| latency, 99th percentile (ms) | 0.567 | 0.564 | -0.4% | -0.0427 to 0.0381 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.155 | 0.148 | -4.5% | -0.00939 to -0.00443 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,490 | +191.0% | 890 to 1,065 | power given |
| bytes in the cache, mean (MB) | 417 | 1,163 | +178.8% | 687 to 805 | power given |
| pages read into the cache (misses) | 682,438 | 168,077 | -75.4% | -624,224 to -404,497 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.199 | +0.8% | -0.0538 to 0.0569 | EVEN, no difference beyond the noise |
| host CPU-seconds | 360 | 364 | +1.3% | -116 to 125 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.27 | 0.274 | +1.4% | -0.0867 to 0.0941 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 11 |  | 3.55 to 18.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 176 | -5.3% | -11.5 to -8.17 | GAIN |
| the server's own CPU-seconds (mongod) | 184 | 173 | -5.7% | -12.2 to -8.79 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.37 | 3.02 | +27.4% | 0.435 to 0.866 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 360 | 364 | +1.3% | -116 to 125 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
