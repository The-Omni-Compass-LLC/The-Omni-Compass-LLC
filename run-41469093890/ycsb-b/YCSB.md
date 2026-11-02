# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,882 | -0.1% | -5.64 to 2.14 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -3.65 to 0.693 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.337 | 0.346 | +2.6% | -0.0103 to 0.0276 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.596 | 0.599 | +0.6% | -0.0118 to 0.0185 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.205 | +1.2% | -0.00403 to 0.00869 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 418 | -0.0% | -8.99 to 8.61 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 717,521 | 716,850 | -0.1% | -21,254 to 19,910 | shown, not judged |
| host CPU busy (share of the run) | 0.205 | 0.202 | -1.5% | -0.053 to 0.0469 | STEADY, no difference beyond the noise |
| host CPU-seconds | 361 | 353 | -2.1% | -116 to 101 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.271 | 0.266 | -2.0% | -0.0875 to 0.0765 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 202 | 204 | +1.2% | -2.96 to 7.92 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 199 | 201 | +0.9% | -3.73 to 7.31 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 3.24 | +27.0% | 0.56 to 0.818 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 361 | 353 | -2.1% | -116 to 101 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
