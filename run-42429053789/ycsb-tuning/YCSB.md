# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,877 | -0.0% | -2.08 to 0.345 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,887 | -0.0% | -2.29 to 1.07 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.36 | 0.352 | -2.4% | -0.0223 to 0.00502 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.557 | 0.559 | +0.2% | -0.0303 to 0.033 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.219 | 0.214 | -2.3% | -0.0148 to 0.00462 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,387 | +170.9% | 549 to 1,201 | power given |
| bytes in the cache, mean (MB) | 418 | 1,088 | +160.2% | 430 to 909 | power given |
| pages read into the cache (misses) | 678,934 | 264,738 | -61.0% | -578,087 to -250,304 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.242 | +2.4% | -0.0772 to 0.0888 | STEADY, no difference beyond the noise |
| host CPU-seconds | 408 | 424 | +4.0% | -166 to 199 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.307 | 0.32 | +4.0% | -0.125 to 0.15 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.33 |  | 3.46 to 9.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 264 | -3.5% | -23.9 to 4.88 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 271 | 260 | -3.7% | -24.4 to 4.19 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.49 | 3.13 | +25.5% | 0.576 to 0.695 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 408 | 424 | +4.0% | -166 to 199 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
