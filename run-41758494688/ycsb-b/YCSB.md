# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,887 | +0.0% | -3.01 to 3.37 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -2.51 to 2.79 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.316 | +2.5% | -0.0103 to 0.0256 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.507 | 0.506 | -0.2% | -0.0227 to 0.0207 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.186 | 0.188 | +1.3% | -0.00341 to 0.00834 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.1% | 0.0294 to 1.79 | power given |
| pages read into the cache (misses) | 61,737 | 61,844 | +0.2% | -167 to 381 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.186 | +7.9% | -0.0357 to 0.0629 | STEADY, no difference beyond the noise |
| host CPU-seconds | 294 | 323 | +9.7% | -76.9 to 134 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.242 | +9.7% | -0.058 to 0.101 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 181 | 185 | +2.1% | -3.25 to 10.9 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 178 | 182 | +2.1% | -3.47 to 11 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.56 | 2.63 | +2.7% | -0.0855 to 0.222 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 294 | 323 | +9.7% | -76.9 to 134 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
