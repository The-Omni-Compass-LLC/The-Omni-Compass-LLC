# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,936 | +0.0% | -6.25 to 6.49 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,937 | +0.0% | -6.34 to 6.59 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0953 | 0.0993 | +4.2% | -0.00461 to 0.0126 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.29 | 0.295 | +1.7% | -0.0332 to 0.0432 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0599 | 0.061 | +1.8% | -0.00158 to 0.00379 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 420 | 421 | +0.3% | -5.18 to 7.41 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 703,259 | 716,327 | +1.9% | -59,573 to 85,707 | shown, not judged |
| host CPU busy (share of the run) | 0.0879 | 0.0861 | -2.1% | -0.0156 to 0.0119 | STEADY, no difference beyond the noise |
| host CPU-seconds | 161 | 157 | -2.4% | -30.7 to 22.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.12 | 0.117 | -2.4% | -0.023 to 0.0172 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 52 | 53.3 | +2.7% | -2.06 to 4.84 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 50 | 50.9 | +1.8% | -2.24 to 4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.96 | 2.47 | +26.1% | 0.178 to 0.843 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 161 | 157 | -2.4% | -30.7 to 22.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
