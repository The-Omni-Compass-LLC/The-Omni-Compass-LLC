# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,829 | 5,835 | +0.1% | -10.6 to 22.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,834 | 5,840 | +0.1% | -11 to 22.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.166 | 0.167 | +1.0% | -0.0198 to 0.0231 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.376 | 0.385 | +2.5% | -0.0114 to 0.03 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0833 | 0.0824 | -1.2% | -0.0074 to 0.00547 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,365 | +0.1% | -7.41 to 9.26 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,269 | 63,470 | +0.3% | -202 to 604 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.125 | +2.4% | -0.0259 to 0.0317 | STEADY, no difference beyond the noise |
| host CPU-seconds | 221 | 228 | +2.9% | -49.9 to 63 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0826 | 0.085 | +2.9% | -0.0187 to 0.0235 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 107 | 105 | -1.9% | -12.4 to 8.27 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 104 | 102 | -1.9% | -11.8 to 7.9 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.51 | 3.4 | -3.2% | -0.626 to 0.398 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 221 | 228 | +2.9% | -50 to 63 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
