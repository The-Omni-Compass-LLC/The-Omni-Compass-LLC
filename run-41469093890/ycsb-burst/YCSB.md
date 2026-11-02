# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,901 | 2,899 | -0.1% | -12.6 to 7.34 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,912 | -0.1% | -13 to 7.43 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.305 | 0.309 | +1.5% | -0.016 to 0.0254 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.483 | 0.483 | -0.0% | -0.0805 to 0.0805 | STEADY, the same |
| latency, mean (ms) | 0.166 | 0.166 | +0.1% | -0.0128 to 0.013 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,014 | +98.1% | -433 to 1,438 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 790 | +95.3% | -322 to 1,093 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 271,762 | 199,590 | -26.6% | -222,196 to 77,851 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.15 | -6.6% | -0.0245 to 0.00339 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 108 | -7.5% | -22.7 to 5.21 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.219 | 0.202 | -7.5% | -0.0426 to 0.00997 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 61.6 | 60.6 | -1.7% | -5.53 to 3.46 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 60.8 | 59.6 | -2.0% | -5.77 to 3.34 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.789 | 0.971 | +23.1% | 0.109 to 0.255 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 116 | 108 | -7.5% | -22.7 to 5.24 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
