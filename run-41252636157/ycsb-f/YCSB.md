# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `f3b70b287c67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,767 | 5,771 | +0.1% | -5.48 to 11.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,777 | 5,781 | +0.1% | -4.75 to 12.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.28 | 0.283 | +1.2% | -0.0108 to 0.0175 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.505 | +1.5% | -0.0251 to 0.0405 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.142 | 0.144 | +0.9% | -0.00372 to 0.00639 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,362 | -0.2% | -4.54 to -0.644 | GAIN |
| pages read into the cache (misses) | 63,113 | 62,998 | -0.2% | -953 to 723 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.204 | -0.7% | -0.0114 to 0.00849 | STEADY, no difference beyond the noise |
| host CPU-seconds | 376 | 373 | -0.9% | -23.5 to 16.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.141 | 0.14 | -0.9% | -0.00874 to 0.00625 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 179 | 179 | -0.0% | -6.2 to 6.04 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 176 | 175 | -0.1% | -6.21 to 5.89 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.83 | 3.92 | +2.2% | -0.101 to 0.267 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 376 | 373 | -0.9% | -23.5 to 16.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
