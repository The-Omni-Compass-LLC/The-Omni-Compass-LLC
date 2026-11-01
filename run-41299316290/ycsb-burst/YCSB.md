# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,881 | +0.0% | -4.16 to 5.82 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,890 | +0.0% | -1.64 to 3.71 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.461 | 0.459 | -0.4% | -0.0171 to 0.0131 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.686 | 0.683 | -0.4% | -0.0317 to 0.0257 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.211 | 0.212 | +0.5% | -0.00305 to 0.00529 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 403 | 404 | +0.2% | -3.55 to 5.34 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 259,438 | 272,203 | +4.9% | -10,913 to 36,444 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.185 | +18.6% | -0.00314 to 0.0612 | STEADY, no difference beyond the noise |
| host CPU-seconds | 105 | 129 | +22.8% | -1.36 to 49.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.243 | +22.8% | -0.0023 to 0.0923 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 75.9 | 76.9 | +1.3% | -1.06 to 2.97 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 74.9 | 75.7 | +1.0% | -1.21 to 2.72 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.99 | 1.19 | +20.2% | 0.15 to 0.25 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 105 | 129 | +22.8% | -1.35 to 49.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
