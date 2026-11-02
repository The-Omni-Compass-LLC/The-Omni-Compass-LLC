# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,900 | +0.0% | -6.68 to 7.53 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,913 | +0.0% | -3.66 to 4.85 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.312 | +0.8% | -0.0422 to 0.0469 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.508 | 0.488 | -3.9% | -0.126 to 0.0856 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.162 | 0.159 | -1.4% | -0.0246 to 0.0202 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 646 | +26.3% | -155 to 424 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 508 | +25.4% | -128 to 334 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 268,364 | 241,545 | -10.0% | -82,781 to 29,144 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.161 | +15.4% | -0.0636 to 0.107 | STEADY, no difference beyond the noise |
| host CPU-seconds | 97.9 | 117 | +19.8% | -53.7 to 92.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.184 | 0.22 | +19.8% | -0.1 to 0.173 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -1.54 to 4.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 62.4 | 61.7 | -1.0% | -1.9 to 0.61 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 61.6 | 60.7 | -1.3% | -2.07 to 0.414 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.813 | 0.996 | +22.5% | 0.15 to 0.216 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 97.9 | 117 | +19.8% | -53.7 to 92.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
