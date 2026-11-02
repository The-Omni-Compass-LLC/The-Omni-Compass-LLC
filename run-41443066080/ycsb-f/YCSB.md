# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,649 | 5,657 | +0.1% | -28.8 to 44.3 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,669 | 5,676 | +0.1% | -30.3 to 44.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.45 | 0.442 | -1.7% | -0.0213 to 0.00602 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.692 | 0.685 | -1.0% | -0.0244 to 0.0104 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.256 | 0.25 | -2.2% | -0.0116 to 0.000427 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,418 | +177.0% | 855 to 957 | power given |
| bytes in the cache, mean (MB) | 416 | 1,108 | +166.5% | 658 to 726 | power given |
| pages read into the cache (misses) | 677,651 | 260,086 | -61.6% | -453,417 to -381,713 | shown, not judged |
| host CPU busy (share of the run) | 0.346 | 0.336 | -2.7% | -0.0129 to -0.00607 | GAIN |
| host CPU-seconds | 631 | 610 | -3.3% | -31.4 to -10 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.231 | -3.4% | -0.0135 to -0.00258 | GAIN |
| cache size changes written (the knob's moves) | 0 | 5.67 |  | 2.8 to 8.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 366 | 357 | -2.5% | -20.9 to 2.7 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 361 | 352 | -2.7% | -21.4 to 1.95 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.73 | 5.38 | +13.6% | 0.517 to 0.773 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 631 | 610 | -3.3% | -31.4 to -10 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
