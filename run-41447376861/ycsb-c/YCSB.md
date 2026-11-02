# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | -0.0% | -2.66 to 2.61 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -2.11 to 2.34 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.295 | 0.295 | +0.0% | -0.00896 to 0.00896 | STEADY, the same |
| latency, 99th percentile (ms) | 0.5 | 0.503 | +0.6% | -0.00357 to 0.00957 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.183 | 0.184 | +0.4% | -0.00606 to 0.00766 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,348 | -0.0% | -0.861 to -0.137 | GAIN |
| pages read into the cache (misses) | 61,630 | 61,612 | -0.0% | -49.7 to 13.7 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.167 | -12.3% | -0.112 to 0.0654 | STEADY, no difference beyond the noise |
| host CPU-seconds | 337 | 287 | -14.7% | -237 to 138 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.253 | 0.216 | -14.7% | -0.178 to 0.103 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 174 | 176 | +0.7% | -7.77 to 10.3 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 172 | 173 | +0.7% | -7.71 to 10.2 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 2.55 | +2.3% | -0.126 to 0.24 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 337 | 287 | -14.7% | -237 to 138 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
