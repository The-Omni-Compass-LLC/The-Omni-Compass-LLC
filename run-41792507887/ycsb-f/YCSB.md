# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,677 | 5,683 | +0.1% | -6.31 to 19 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,693 | 5,699 | +0.1% | -6.29 to 18.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.434 | 0.426 | -1.9% | -0.0146 to -0.00208 | GAIN |
| latency, 99th percentile (ms) | 0.654 | 0.649 | -0.8% | -0.023 to 0.0123 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.248 | 0.243 | -2.1% | -0.0105 to 0.000249 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,430 | +179.3% | 672 to 1,164 | power given |
| bytes in the cache, mean (MB) | 417 | 1,118 | +168.5% | 520 to 884 | power given |
| pages read into the cache (misses) | 678,352 | 257,341 | -62.1% | -620,630 to -221,393 | shown, not judged |
| host CPU busy (share of the run) | 0.331 | 0.326 | -1.4% | -0.0119 to 0.00229 | STEADY, no difference beyond the noise |
| host CPU-seconds | 599 | 590 | -1.6% | -30 to 11.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.222 | -1.7% | -0.0113 to 0.00383 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 357 | 347 | -2.6% | -18.1 to -0.566 | GAIN |
| the server's own CPU-seconds (mongod) | 352 | 342 | -2.9% | -18.7 to -1.34 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.54 | 5.26 | +15.7% | 0.542 to 0.889 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 599 | 590 | -1.6% | -29.9 to 11.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
