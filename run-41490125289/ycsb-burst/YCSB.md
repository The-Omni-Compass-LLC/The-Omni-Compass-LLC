# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,877 | 2,879 | +0.0% | -8.92 to 11.8 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,887 | +0.0% | -8.65 to 10.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.447 | 0.445 | -0.4% | -0.0231 to 0.0198 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.623 | 0.62 | -0.4% | -0.0623 to 0.057 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.221 | -0.1% | -0.0102 to 0.0098 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 565 | +10.3% | -175 to 281 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 399 | 441 | +10.5% | -141 to 225 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 274,517 | 248,517 | -9.5% | -76,749 to 24,749 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.227 | +11.2% | -0.0122 to 0.0581 | STEADY, no difference beyond the noise |
| host CPU-seconds | 143 | 163 | +14.3% | -10.7 to 51.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.269 | 0.307 | +14.2% | -0.02 to 0.0966 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 83.2 | 83.1 | -0.2% | -6.8 to 6.53 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 82.2 | 81.8 | -0.5% | -6.99 to 6.22 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.05 | 1.31 | +24.3% | 0.167 to 0.343 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 143 | 163 | +14.3% | -10.7 to 51.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
