# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,909 | 2,907 | -0.1% | -11.3 to 8.07 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,911 | -0.1% | -10.1 to 7.15 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.193 | 0.187 | -3.3% | -0.0115 to -0.00116 | GAIN |
| latency, 99th percentile (ms) | 0.365 | 0.361 | -1.0% | -0.0298 to 0.0224 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.148 | 0.146 | -1.7% | -0.0135 to 0.00848 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 962 | +87.9% | 13.8 to 887 | power given |
| bytes in the cache, mean (MB) | 419 | 762 | +81.9% | -8.12 to 694 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 734,491 | 343,090 | -53.3% | -410,076 to -372,725 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.163 | +3.3% | -0.0425 to 0.0528 | STEADY, no difference beyond the noise |
| host CPU-seconds | 285 | 298 | +4.5% | -90.9 to 117 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.223 | +4.6% | -0.0677 to 0.0873 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -1.13 to 6.46 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 142 | 135 | -4.8% | -9 to -4.73 | GAIN |
| the server's own CPU-seconds (mongod) | 140 | 133 | -5.3% | -9.56 to -5.25 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.07 | 2.61 | +26.1% | 0.392 to 0.691 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 285 | 298 | +4.5% | -90.9 to 117 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
