# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,895 | +0.3% | -42.4 to 59.4 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,901 | 2,909 | +0.3% | -46.9 to 62.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.336 | 0.341 | +1.6% | -0.022 to 0.0327 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.546 | 0.547 | +0.2% | -0.0938 to 0.0958 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.18 | -5.4% | -0.0262 to 0.00565 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 966 | +88.6% | 140 to 767 | power given |
| bytes in the cache, mean (MB) | 398 | 753 | +89.3% | 112 to 598 | power given |
| pages read into the cache (misses) | 261,535 | 196,138 | -25.0% | -92,140 to -38,653 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.162 | +8.1% | -0.0369 to 0.0611 | STEADY, no difference beyond the noise |
| host CPU-seconds | 107 | 117 | +9.6% | -30.4 to 50.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.201 | 0.22 | +9.3% | -0.0581 to 0.0956 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 62.2 | 61.6 | -1.0% | -3.43 to 2.22 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 61.4 | 60.6 | -1.3% | -3.65 to 2.02 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.782 | 0.987 | +26.2% | 0.145 to 0.265 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 107 | 117 | +9.6% | -30.4 to 50.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
