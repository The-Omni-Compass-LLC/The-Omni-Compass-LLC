# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,869 | 2,870 | +0.0% | -6.8 to 7.84 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,881 | 2,882 | +0.0% | -6.31 to 7.67 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.379 | 0.365 | -3.7% | -0.0239 to -0.00406 | GAIN |
| latency, 99th percentile (ms) | 0.655 | 0.652 | -0.5% | -0.0202 to 0.0142 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.219 | -3.0% | -0.0152 to 0.00158 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,443 | +181.8% | 790 to 1,071 | power given |
| bytes in the cache, mean (MB) | 417 | 1,124 | +169.4% | 600 to 813 | power given |
| pages read into the cache (misses) | 674,421 | 215,796 | -68.0% | -495,363 to -421,887 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.252 | -6.0% | -0.113 to 0.0805 | STEADY, no difference beyond the noise |
| host CPU-seconds | 481 | 445 | -7.5% | -273 to 201 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.364 | 0.336 | -7.5% | -0.206 to 0.151 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 9 |  | 9 to 9 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 276 | 265 | -3.7% | -20.8 to 0.18 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 273 | 262 | -4.0% | -21.5 to -0.487 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.57 | 3.24 | +26.1% | 0.454 to 0.888 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 481 | 445 | -7.5% | -273 to 201 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
