# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,908 | 2,908 | +0.0% | -1.83 to 1.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,911 | +0.0% | -1.86 to 2.24 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.246 | 0.244 | -0.9% | -0.0151 to 0.0104 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.504 | 0.5 | -0.8% | -0.028 to 0.02 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.111 | 0.112 | +0.5% | -0.00489 to 0.00591 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% | -2.37 to 3.32 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,616 | 61,658 | +0.1% | 1.34 to 83.3 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.134 | +19.2% | -0.015 to 0.0581 | STEADY, no difference beyond the noise |
| host CPU-seconds | 198 | 242 | +21.9% | -30 to 117 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.149 | 0.181 | +21.9% | -0.0226 to 0.0876 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 91.2 | 91.6 | +0.4% | -4.98 to 5.69 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 88.8 | 89.1 | +0.3% | -5.11 to 5.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.4 | 2.48 | +3.5% | 0.0437 to 0.124 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 198 | 242 | +21.9% | -30 to 117 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
