# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,871 | 2,870 | -0.0% | -3.59 to 1.01 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,883 | 2,882 | -0.0% | -4.96 to 2.96 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.521 | 0.521 | -0.1% | -0.0147 to 0.014 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.724 | 0.727 | +0.4% | -0.0247 to 0.0307 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.233 | 0.231 | -0.7% | -0.00818 to 0.00477 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 653 | +27.5% | -240 to 521 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 400 | 509 | +27.2% | -169 to 387 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 270,370 | 247,535 | -8.4% | -68,973 to 23,303 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.197 | -13.3% | -0.0971 to 0.0368 | STEADY, no difference beyond the noise |
| host CPU-seconds | 163 | 136 | -16.4% | -86.5 to 33 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.307 | 0.257 | -16.4% | -0.163 to 0.0627 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 83.6 | 82.4 | -1.5% | -3.92 to 1.49 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 82.5 | 81.1 | -1.8% | -4.26 to 1.33 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.08 | 1.33 | +23.1% | 0.132 to 0.368 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 163 | 136 | -16.4% | -86.5 to 33 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
