# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,693 | 5,695 | +0.0% | -44 to 47.7 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,716 | 5,720 | +0.1% | -34.3 to 42.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.424 | 0.426 | +0.4% | -0.0328 to 0.0361 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.719 | 0.734 | +2.1% | -0.0755 to 0.106 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.224 | -0.4% | -0.0168 to 0.0149 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,281 | +150.2% | 372 to 1,166 | power given |
| bytes in the cache, mean (MB) | 416 | 1,006 | +141.7% | 294 to 886 | power given |
| pages read into the cache (misses) | 684,189 | 295,772 | -56.8% | -468,725 to -308,109 | shown, not judged |
| host CPU busy (share of the run) | 0.315 | 0.309 | -1.9% | -0.0431 to 0.0311 | STEADY, no difference beyond the noise |
| host CPU-seconds | 584 | 567 | -2.8% | -106 to 73.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.214 | -2.8% | -0.0416 to 0.0291 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.33 |  | 4.9 to 7.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 318 | 314 | -1.1% | -23.4 to 16.4 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 312 | 308 | -1.4% | -24 to 15 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 5.38 | 6.37 | +18.5% | 0.488 to 1.5 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 584 | 567 | -2.8% | -106 to 73.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
