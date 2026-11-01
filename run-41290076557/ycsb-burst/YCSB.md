# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,880 | +0.0% | -3.04 to 3.31 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -3.02 to 3.08 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.454 | 0.448 | -1.2% | -0.0282 to 0.0169 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.644 | 0.636 | -1.2% | -0.0246 to 0.00924 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.212 | -1.8% | -0.00907 to 0.00126 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 401 | 399 | -0.4% | -7.22 to 3.83 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 280,336 | 262,105 | -6.5% | -34,071 to -2,392 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.161 | -22.3% | -0.0856 to -0.00665 | GAIN |
| host CPU-seconds | 148 | 108 | -26.5% | -76.4 to -1.81 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.204 | -26.5% | -0.144 to -0.00347 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80.1 | 77.9 | -2.8% | -4.9 to 0.44 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 79.1 | 76.7 | -3.1% | -5.17 to 0.256 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.999 | 1.22 | +22.6% | 0.145 to 0.306 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 148 | 108 | -26.5% | -76.4 to -1.83 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
