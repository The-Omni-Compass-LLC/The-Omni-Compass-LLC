# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,897 | -0.0% | -2.81 to 2.75 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,899 | -0.0% | -2.88 to 2.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.284 | 0.279 | -1.9% | -0.0171 to 0.00641 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.419 | 0.414 | -1.1% | -0.0147 to 0.00537 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.176 | 0.173 | -1.6% | -0.0115 to 0.00578 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 421 | 419 | -0.5% | -4.43 to 0.513 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 746,995 | 668,331 | -10.5% | -130,136 to -27,192 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.171 | -6.3% | -0.1 to 0.0774 | EVEN, no difference beyond the noise |
| host CPU-seconds | 321 | 297 | -7.5% | -214 to 166 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.241 | 0.223 | -7.5% | -0.161 to 0.124 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 176 | 173 | -1.8% | -14.8 to 8.3 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 174 | 170 | -2.2% | -15.2 to 7.75 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.22 | 2.73 | +22.9% | 0.45 to 0.57 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 321 | 297 | -7.5% | -214 to 166 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
