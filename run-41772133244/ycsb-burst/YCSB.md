# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,887 | +0.1% | -8.85 to 15.8 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,895 | +0.1% | -7.48 to 13.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.438 | 0.443 | +1.0% | -0.022 to 0.0307 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.662 | 0.659 | -0.5% | -0.0386 to 0.0319 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.161 | 0.161 | -0.0% | -0.00784 to 0.00781 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,510 | 1,510 | -0.0% | -1.73 to 1.43 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,633 | 77,650 | +0.0% | -512 to 545 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.147 | -1.2% | -0.129 to 0.126 | STEADY, no difference beyond the noise |
| host CPU-seconds | 107 | 105 | -1.3% | -107 to 104 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.201 | 0.199 | -1.3% | -0.203 to 0.197 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 50.9 | 50.5 | -0.9% | -3.28 to 2.38 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 49.9 | 49.4 | -1.0% | -3.31 to 2.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.06 | +5.3% | 0.00895 to 0.0974 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 107 | 105 | -1.3% | -107 to 104 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
