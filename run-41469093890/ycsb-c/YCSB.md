# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,939 | -0.0% | -5.54 to 4.26 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,940 | -0.0% | -5.68 to 4.54 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.098 | 0.1 | +2.4% | -0.00992 to 0.0146 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.3 | 0.301 | +0.2% | -0.00651 to 0.00784 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0598 | 0.0599 | +0.2% | -0.00448 to 0.00471 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 419 | -0.2% | -12.7 to 10.8 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 691,570 | 708,191 | +2.4% | -135,893 to 169,135 | shown, not judged |
| host CPU busy (share of the run) | 0.0872 | 0.0718 | -17.6% | -0.046 to 0.0153 | STEADY, no difference beyond the noise |
| host CPU-seconds | 159 | 129 | -19.0% | -90 to 29.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.119 | 0.0963 | -19.0% | -0.0672 to 0.022 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 50.8 | 51.9 | +2.1% | -4.47 to 6.62 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 49.2 | 49.7 | +1.1% | -4.74 to 5.84 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.59 | 2.11 | +32.9% | 0.188 to 0.855 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 159 | 129 | -19.0% | -90 to 29.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
