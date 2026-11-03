# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,877 | -0.1% | -9.62 to 6.57 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -7.53 to 4.97 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.373 | 0.359 | -3.8% | -0.0399 to 0.0119 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.643 | 0.644 | +0.2% | -0.0283 to 0.0303 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.215 | -3.6% | -0.0133 to -0.00266 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,379 | +169.3% | 709 to 1,025 | power given |
| bytes in the cache, mean (MB) | 417 | 1,083 | +159.6% | 548 to 783 | power given |
| pages read into the cache (misses) | 674,052 | 259,260 | -61.5% | -435,792 to -393,791 | shown, not judged |
| host CPU busy (share of the run) | 0.263 | 0.241 | -8.1% | -0.0374 to -0.00508 | GAIN |
| host CPU-seconds | 469 | 423 | -9.8% | -79.7 to -12 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.353 | 0.319 | -9.7% | -0.0594 to -0.0094 | GAIN |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 261 | -4.4% | -18.7 to -5.44 | GAIN |
| the server's own CPU-seconds (mongod) | 270 | 258 | -4.7% | -19.2 to -6.12 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 3.12 | +24.0% | 0.44 to 0.767 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 469 | 423 | -9.8% | -79.7 to -12 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
