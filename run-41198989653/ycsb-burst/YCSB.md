# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,796 | 2,897 | +3.6% | -293 to 495 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,810 | 2,911 | +3.6% | -290 to 491 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.322 | +1.2% | -0.0278 to 0.0351 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.53 | 0.52 | -1.9% | -0.117 to 0.0969 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.18 | -8.0% | -0.0592 to 0.0276 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 952 | +85.8% | 140 to 739 | power given |
| bytes in the cache, mean (MB) | 394 | 742 | +88.1% | 101 to 594 | power given |
| pages read into the cache (misses) | 249,373 | 193,790 | -22.3% | -150,687 to 39,521 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.17 | +9.0% | -0.179 to 0.207 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 126 | +12.2% | -160 to 187 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.238 | +7.6% | -0.342 to 0.375 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 60.7 | 62.9 | +3.7% | -6.08 to 10.5 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 59.9 | 61.9 | +3.3% | -6.29 to 10.2 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.813 | 1.06 | +29.8% | 0.193 to 0.292 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 113 | 126 | +12.2% | -160 to 187 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
