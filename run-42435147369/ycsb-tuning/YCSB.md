# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,899 | +0.0% | -2.47 to 3.33 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,909 | +0.0% | -2.82 to 3.77 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.324 | -4.8% | -0.0201 to -0.0125 | GAIN |
| latency, 99th percentile (ms) | 0.589 | 0.583 | -1.1% | -0.0246 to 0.012 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.157 | 0.149 | -5.0% | -0.00958 to -0.00624 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,613 | +215.1% | 1,083 to 1,119 | power given |
| bytes in the cache, mean (MB) | 417 | 1,244 | +198.5% | 814 to 841 | power given |
| pages read into the cache (misses) | 683,696 | 115,297 | -83.1% | -598,271 to -538,528 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.183 | -6.6% | -0.0404 to 0.0144 | STEADY, no difference beyond the noise |
| host CPU-seconds | 356 | 329 | -7.5% | -88 to 34.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.268 | 0.248 | -7.5% | -0.0663 to 0.026 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 16 |  | 11 to 21 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 177 | -5.8% | -13.9 to -7.93 | GAIN |
| the server's own CPU-seconds (mongod) | 185 | 174 | -6.2% | -14.7 to -8.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.38 | 3.02 | +26.8% | 0.476 to 0.803 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 356 | 329 | -7.5% | -88 to 34.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
