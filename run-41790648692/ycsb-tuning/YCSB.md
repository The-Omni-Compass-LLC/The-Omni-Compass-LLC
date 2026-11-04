# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,895 | -0.0% | -6.72 to 5.32 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,906 | -0.0% | -4.97 to 4.53 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.352 | 0.335 | -4.8% | -0.0278 to -0.00617 | GAIN |
| latency, 99th percentile (ms) | 0.602 | 0.598 | -0.7% | -0.043 to 0.035 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.161 | 0.153 | -4.9% | -0.0136 to -0.00202 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,501 | +193.1% | 718 to 1,260 | power given |
| bytes in the cache, mean (MB) | 417 | 1,162 | +178.5% | 534 to 956 | power given |
| pages read into the cache (misses) | 676,404 | 134,739 | -80.1% | -641,125 to -442,205 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.193 | +0.3% | -0.0312 to 0.0325 | STEADY, no difference beyond the noise |
| host CPU-seconds | 344 | 349 | +1.4% | -69.8 to 79.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.262 | +1.4% | -0.0521 to 0.0595 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 15 |  | 6.39 to 23.6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 193 | 181 | -6.4% | -21.6 to -3.15 | GAIN |
| the server's own CPU-seconds (mongod) | 191 | 178 | -6.8% | -22.1 to -3.84 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 3.11 | +25.1% | 0.434 to 0.812 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 344 | 349 | +1.4% | -69.9 to 79.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
