# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,906 | +0.0% | -2.47 to 3.73 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,909 | +0.0% | -2.51 to 3.87 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.282 | 0.287 | +1.7% | -0.0198 to 0.0292 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.517 | 0.518 | +0.3% | -0.0166 to 0.0193 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.119 | 0.119 | -0.0% | -0.00286 to 0.00284 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -0.94 to 1.09 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,770 | 61,847 | +0.1% | -220 to 375 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.118 | -14.9% | -0.0569 to 0.0156 | STEADY, no difference beyond the noise |
| host CPU-seconds | 250 | 207 | -17.0% | -116 to 31.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.155 | -17.0% | -0.0872 to 0.0234 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 103 | 103 | +0.0% | -2.89 to 2.97 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 101 | 101 | -0.1% | -2.94 to 2.84 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.39 | 2.49 | +3.9% | -0.017 to 0.205 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 250 | 207 | -17.0% | -116 to 31.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
