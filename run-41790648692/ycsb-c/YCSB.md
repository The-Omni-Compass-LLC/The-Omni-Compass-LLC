# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,907 | +0.0% | -7.46 to 8.59 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,911 | +0.0% | -8.1 to 8.48 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.191 | 0.187 | -2.1% | -0.0171 to 0.00915 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.362 | 0.356 | -1.7% | -0.0275 to 0.0148 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.146 | 0.139 | -4.7% | -0.00964 to -0.00423 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 807 | +57.7% | -157 to 747 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 644 | +55.0% | -111 to 568 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 703,021 | 439,623 | -37.5% | -602,043 to 75,247 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.149 | -0.6% | -0.106 to 0.104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 270 | 269 | -0.2% | -220 to 219 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.202 | -0.3% | -0.165 to 0.164 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -1.46 to 6.13 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 141 | 137 | -2.6% | -10.3 to 3.02 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 139 | 135 | -3.0% | -10.9 to 2.46 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.12 | 2.69 | +26.9% | 0.53 to 0.613 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 270 | 269 | -0.2% | -220 to 219 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
