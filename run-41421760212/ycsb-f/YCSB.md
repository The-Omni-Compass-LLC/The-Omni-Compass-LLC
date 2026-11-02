# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,671 | 5,665 | -0.1% | -39.1 to 27.3 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,681 | 5,676 | -0.1% | -35.8 to 26 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.402 | 0.405 | +0.7% | -0.00854 to 0.0139 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.589 | 0.601 | +2.0% | -0.0205 to 0.0445 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.227 | +1.2% | -0.00824 to 0.0137 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,362 | -0.1% | -7.92 to 5.11 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 62,991 | 63,103 | +0.2% | -954 to 1,179 | shown, not judged |
| host CPU busy (share of the run) | 0.288 | 0.297 | +3.0% | -0.0277 to 0.0451 | STEADY, no difference beyond the noise |
| host CPU-seconds | 521 | 542 | +4.0% | -65.9 to 107 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.205 | +4.1% | -0.0246 to 0.0407 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 309 | 312 | +0.9% | -9.52 to 15.3 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 305 | 308 | +0.9% | -9.33 to 14.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.29 | 4.42 | +3.2% | -0.217 to 0.491 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 521 | 542 | +4.0% | -65.9 to 108 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
