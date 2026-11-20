# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,725 | 5,724 | -0.0% | -19.7 to 18.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,740 | 5,739 | -0.0% | -19.3 to 17.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.386 | 0.377 | -2.3% | -0.014 to -0.00403 | GAIN |
| latency, 99th percentile (ms) | 0.616 | 0.607 | -1.5% | -0.0198 to 0.00183 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.202 | -2.9% | -0.00861 to -0.00335 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,422 | +177.8% | 844 to 976 | power given |
| bytes in the cache, mean (MB) | 416 | 1,115 | +167.9% | 650 to 748 | power given |
| pages read into the cache (misses) | 688,482 | 239,113 | -65.3% | -478,464 to -420,275 | shown, not judged |
| host CPU busy (share of the run) | 0.303 | 0.286 | -5.6% | -0.0492 to 0.0152 | STEADY, no difference beyond the noise |
| host CPU-seconds | 563 | 522 | -7.2% | -123 to 41.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.197 | -7.2% | -0.0466 to 0.0162 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 299 | 289 | -3.5% | -10.6 to -10 | GAIN |
| the server's own CPU-seconds (mongod) | 294 | 283 | -3.8% | -11.6 to -10.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.87 | 5.69 | +16.7% | 0.608 to 1.02 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 563 | 522 | -7.2% | -123 to 41.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
