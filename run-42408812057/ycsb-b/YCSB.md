# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% | -1.7 to 1.27 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | -0.0% | -1.53 to 1.32 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.334 | +0.4% | -0.0044 to 0.00707 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.495 | 0.498 | +0.6% | -0.0121 to 0.0181 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.202 | +0.6% | -0.00141 to 0.00367 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 418 | +0.1% | -5.37 to 5.92 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 696,620 | 723,470 | +3.9% | -78,964 to 132,663 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.207 | +10.2% | -0.0329 to 0.0712 | STEADY, no difference beyond the noise |
| host CPU-seconds | 322 | 362 | +12.5% | -71.7 to 152 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.272 | +12.5% | -0.0539 to 0.114 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 202 | 204 | +0.9% | -2.87 to 6.49 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 200 | 201 | +0.6% | -3.56 to 5.85 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.54 | 3.2 | +26.0% | 0.61 to 0.71 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 322 | 362 | +12.5% | -71.7 to 152 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
