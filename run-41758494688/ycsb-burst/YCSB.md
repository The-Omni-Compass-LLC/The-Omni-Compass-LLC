# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,880 | +0.0% | -1.32 to 2.52 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,889 | +0.0% | -2.44 to 4.68 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.448 | 0.451 | +0.7% | -0.00357 to 0.00957 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.636 | 0.635 | -0.1% | -0.0481 to 0.0474 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.215 | +0.1% | -0.00526 to 0.00559 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,511 | 1,511 | +0.0% | -1.66 to 2.17 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,651 | 77,754 | +0.1% | -75.6 to 281 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.185 | -4.7% | -0.0665 to 0.0484 | STEADY, no difference beyond the noise |
| host CPU-seconds | 136 | 128 | -5.9% | -56.9 to 40.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.257 | 0.242 | -5.9% | -0.107 to 0.077 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 77.8 | 77.8 | -0.0% | -1.73 to 1.71 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 76.8 | 76.7 | -0.1% | -1.77 to 1.68 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.988 | 1.02 | +3.4% | -0.0206 to 0.0876 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 136 | 128 | -5.9% | -56.9 to 40.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
