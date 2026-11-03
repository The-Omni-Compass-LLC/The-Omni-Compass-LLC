# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,744 | 5,749 | +0.1% | -39.2 to 48 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,760 | 5,765 | +0.1% | -37.6 to 47.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.322 | 0.319 | -0.9% | -0.0105 to 0.00445 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.499 | 0.501 | +0.5% | -0.0475 to 0.0529 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.186 | 0.185 | -0.3% | -0.0146 to 0.0137 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 794 | +55.2% | 185 to 380 | power given |
| bytes in the cache, mean (MB) | 417 | 623 | +49.3% | 145 to 267 | power given |
| pages read into the cache (misses) | 685,866 | 416,109 | -39.3% | -351,292 to -188,223 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.256 | +1.6% | -0.0219 to 0.03 | STEADY, no difference beyond the noise |
| host CPU-seconds | 457 | 469 | +2.4% | -54.7 to 77.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.172 | 0.176 | +2.4% | -0.0216 to 0.0298 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 10.3 |  | 2.74 to 17.9 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 274 | 271 | -1.1% | -7.58 to 1.56 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 271 | 267 | -1.3% | -8.14 to 1.03 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.49 | 4.04 | +15.6% | 0.377 to 0.716 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 458 | 469 | +2.4% | -54.7 to 77 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
