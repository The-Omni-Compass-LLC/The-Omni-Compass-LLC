# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,881 | +0.0% | -2.83 to 5.02 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,886 | +0.0% | -2.89 to 4.84 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.346 | 0.344 | -0.4% | -0.015 to 0.0123 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.54 | 0.537 | -0.6% | -0.0138 to 0.00783 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.206 | -0.8% | -0.00933 to 0.00593 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,363 | -0.1% | -2.74 to 1.11 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,264 | 63,188 | -0.1% | -540 to 390 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.233 | +1.4% | -0.0469 to 0.0531 | STEADY, no difference beyond the noise |
| host CPU-seconds | 402 | 410 | +1.9% | -103 to 118 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.303 | 0.308 | +1.9% | -0.0772 to 0.0888 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 237 | 234 | -1.1% | -12.9 to 7.58 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 234 | 231 | -1.2% | -12.9 to 7.42 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 2.69 | +3.2% | -0.0462 to 0.211 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 402 | 410 | +1.9% | -103 to 118 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
