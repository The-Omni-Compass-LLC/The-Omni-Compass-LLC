# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,927 | 2,933 | +0.2% | 0.285 to 11.7 | GAIN |
| throughput (operations a second) | 2,933 | 2,937 | +0.1% | -0.761 to 7.62 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.254 | 0.258 | +1.4% | -0.0362 to 0.0435 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.418 | 0.405 | -3.2% | -0.0937 to 0.067 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0827 | 0.0786 | -5.0% | -0.0161 to 0.00793 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,519 | 1,520 | +0.0% | -3.18 to 4.31 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,653 | 77,732 | +0.1% | -89.2 to 246 | shown, not judged |
| host CPU busy (share of the run) | 0.092 | 0.0915 | -0.5% | -0.0793 to 0.0784 | STEADY, no difference beyond the noise |
| host CPU-seconds | 67.1 | 66.9 | -0.3% | -63.3 to 62.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.125 | 0.125 | -0.5% | -0.118 to 0.117 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 24 | 23.3 | -3.3% | -4.48 to 2.9 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 23.2 | 22.4 | -3.4% | -4.37 to 2.81 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.813 | 0.803 | -1.2% | -0.134 to 0.114 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 67.1 | 66.9 | -0.3% | -63.3 to 62.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
