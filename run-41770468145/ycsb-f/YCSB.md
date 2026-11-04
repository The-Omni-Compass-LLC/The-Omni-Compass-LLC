# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,747 | 5,717 | -0.5% | -174 to 114 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,763 | 5,733 | -0.5% | -165 to 106 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.318 | -1.8% | -0.0103 to -0.0017 | GAIN |
| latency, 99th percentile (ms) | 0.488 | 0.485 | -0.7% | -0.0402 to 0.0335 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.185 | -2.0% | -0.0211 to 0.0137 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,135 | +121.7% | 369 to 878 | power given |
| bytes in the cache, mean (MB) | 416 | 865 | +107.7% | 298 to 599 | power given |
| pages read into the cache (misses) | 687,090 | 250,042 | -63.6% | -513,043 to -361,054 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.246 | +0.8% | -0.0248 to 0.0289 | STEADY, no difference beyond the noise |
| host CPU-seconds | 439 | 446 | +1.7% | -50.8 to 65.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.168 | +2.2% | -0.0148 to 0.0221 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 15.7 |  | -7.42 to 38.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 274 | 266 | -2.6% | -14.2 to -0.193 | GAIN |
| the server's own CPU-seconds (mongod) | 270 | 262 | -2.9% | -14.5 to -0.999 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.54 | 4.08 | +15.3% | 0.272 to 0.807 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 439 | 446 | +1.7% | -50.8 to 65.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
