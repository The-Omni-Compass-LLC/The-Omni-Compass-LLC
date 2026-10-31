# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,900 | 2,899 | -0.0% | -4.58 to 3.05 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,910 | +0.0% | -4.9 to 5.56 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.227 | 0.223 | -2.1% | -0.03 to 0.0207 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.434 | 0.436 | +0.3% | -0.0195 to 0.0222 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.178 | 0.172 | -3.7% | -0.0202 to 0.00706 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,116 | +118.0% | -159 to 1,368 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 843 | +103.2% | -80.9 to 937 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 683,989 | 268,529 | -60.7% | -746,532 to -84,388 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.187 | -4.2% | -0.0396 to 0.0234 | EVEN, no difference beyond the noise |
| host CPU-seconds | 350 | 333 | -4.9% | -82.5 to 48.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.25 | -4.8% | -0.0616 to 0.0364 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 23.7 |  | -24.9 to 72.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 212 | 207 | -2.0% | -13.1 to 4.48 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 210 | 205 | -2.3% | -13.8 to 4.04 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.04 | 2.63 | +28.7% | 0.382 to 0.792 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 350 | 333 | -4.9% | -82.5 to 48.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
