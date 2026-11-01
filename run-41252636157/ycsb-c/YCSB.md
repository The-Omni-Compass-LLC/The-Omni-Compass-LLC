# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `f3b70b287c67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,892 | +0.0% | -2.2 to 3.73 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,894 | +0.0% | -1.77 to 3.02 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.283 | 0.28 | -1.1% | -0.0224 to 0.0164 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.434 | 0.43 | -0.8% | -0.0244 to 0.017 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.164 | 0.163 | -0.9% | -0.00296 to 4.89e-05 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% | -1.73 to 2.21 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,623 | 61,619 | -0.0% | -120 to 112 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.18 | -6.0% | -0.0411 to 0.018 | STEADY, no difference beyond the noise |
| host CPU-seconds | 348 | 323 | -7.4% | -90.5 to 38.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.261 | 0.242 | -7.4% | -0.0678 to 0.0289 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 163 | 162 | -0.7% | -3.54 to 1.15 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 161 | 160 | -0.8% | -3.71 to 1.21 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 2.53 | +2.3% | -0.0594 to 0.175 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 348 | 323 | -7.4% | -90.5 to 38.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
