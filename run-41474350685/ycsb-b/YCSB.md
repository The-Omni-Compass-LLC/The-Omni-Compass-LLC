# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,936 | -0.1% | -9.13 to 4.35 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,938 | -0.1% | -8.85 to 4.25 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.133 | 0.143 | +7.5% | -0.0276 to 0.0476 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.323 | 0.324 | +0.4% | -0.0322 to 0.0349 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.061 | 0.0634 | +3.9% | -0.00583 to 0.0106 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,367 | +0.0% | -2.82 to 3.97 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,740 | 61,851 | +0.2% | -144 to 366 | shown, not judged |
| host CPU busy (share of the run) | 0.0811 | 0.0864 | +6.5% | -0.091 to 0.102 | STEADY, no difference beyond the noise |
| host CPU-seconds | 149 | 157 | +5.5% | -183 to 199 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.111 | 0.117 | +5.6% | -0.136 to 0.149 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 52 | 54.3 | +4.6% | -7.94 to 12.7 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 50.4 | 52.6 | +4.5% | -7.82 to 12.3 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.6 | 1.72 | +7.2% | -0.127 to 0.357 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 149 | 157 | +5.5% | -183 to 199 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
