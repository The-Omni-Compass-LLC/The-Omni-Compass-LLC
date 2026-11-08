# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,838 | 5,839 | +0.0% | -15.9 to 17.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,847 | 5,847 | +0.0% | -16.2 to 17.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.156 | 0.157 | +0.9% | -0.00492 to 0.00759 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.363 | 0.362 | -0.4% | -0.0486 to 0.0459 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0817 | 0.0823 | +0.8% | -0.00302 to 0.00432 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 669 | +30.7% | -181 to 495 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 536 | +27.9% | -138 to 372 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 711,499 | 535,137 | -24.8% | -519,964 to 167,242 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.145 | +16.0% | -0.00244 to 0.0424 | STEADY, no difference beyond the noise |
| host CPU-seconds | 226 | 268 | +18.5% | -6.56 to 90.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0845 | 0.1 | +18.4% | -0.00235 to 0.0335 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -2.84 to 7.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 117 | 120 | +1.8% | -3.43 to 7.56 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 114 | 116 | +1.3% | -3.65 to 6.72 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.03 | 3.56 | +17.5% | 0.207 to 0.85 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 226 | 268 | +18.5% | -6.58 to 90.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
