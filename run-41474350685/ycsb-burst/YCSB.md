# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7484 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,809 | 2,808 | -0.0% | -48.9 to 46.6 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,826 | 2,825 | -0.0% | -44.2 to 41.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.528 | 0.529 | +0.1% | -0.0194 to 0.0207 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.863 | 0.866 | +0.4% | -0.077 to 0.0837 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.246 | 0.246 | -0.1% | -0.0109 to 0.0102 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,484 | 7,484 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,472 | 1,471 | -0.1% | -35.6 to 33.6 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,421 | 77,413 | -0.0% | -365 to 349 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.221 | +3.4% | -0.103 to 0.117 | STEADY, no difference beyond the noise |
| host CPU-seconds | 150 | 157 | +4.5% | -87.8 to 101 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.289 | 0.301 | +4.4% | -0.167 to 0.192 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 81.9 | 81.7 | -0.3% | -7.79 to 7.38 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 80.6 | 80.4 | -0.3% | -7.78 to 7.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.27 | 1.29 | +2.0% | -0.0234 to 0.0747 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 150 | 157 | +4.5% | -87.8 to 101 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
