# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,684 | 5,692 | +0.1% | -24 to 40.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,699 | 5,707 | +0.1% | -23.8 to 40.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.416 | -1.2% | -0.0164 to 0.00638 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.619 | 0.619 | +0.0% | -0.0131 to 0.0131 | STEADY, the same |
| latency, mean (ms) | 0.242 | 0.238 | -1.4% | -0.0132 to 0.00626 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,278 | +149.6% | 284 to 1,248 | power given |
| bytes in the cache, mean (MB) | 417 | 1,006 | +141.4% | 225 to 953 | power given |
| pages read into the cache (misses) | 678,592 | 290,724 | -57.2% | -565,147 to -210,588 | shown, not judged |
| host CPU busy (share of the run) | 0.323 | 0.319 | -1.2% | -0.0125 to 0.00506 | STEADY, no difference beyond the noise |
| host CPU-seconds | 583 | 575 | -1.4% | -26.4 to 10.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.216 | -1.6% | -0.0109 to 0.00395 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 0.538 to 8.13 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 349 | 343 | -1.7% | -22 to 9.94 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 345 | 338 | -2.0% | -22.5 to 9.06 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.29 | 4.97 | +16.0% | 0.32 to 1.05 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 583 | 575 | -1.4% | -26.4 to 10.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
