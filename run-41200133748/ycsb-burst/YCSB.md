# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,934 | +0.0% | -4.12 to 4.94 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,938 | +0.0% | -4.95 to 7.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.256 | 0.258 | +0.9% | -0.0449 to 0.0496 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.425 | 0.43 | +1.2% | -0.0657 to 0.0757 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0831 | 0.0838 | +0.9% | -0.0116 to 0.0132 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 716 | +39.8% | -309 to 717 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 563 | +39.1% | -243 to 559 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 262,990 | 225,494 | -14.3% | -85,604 to 10,612 | shown, not judged |
| host CPU busy (share of the run) | 0.077 | 0.0745 | -3.2% | -0.0838 to 0.0789 | EVEN, no difference beyond the noise |
| host CPU-seconds | 55.3 | 53.2 | -3.8% | -64.8 to 60.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.103 | 0.0995 | -3.8% | -0.121 to 0.113 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1 |  | -1.48 to 3.48 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 26.6 | 25.4 | -4.6% | -8.4 to 5.95 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 25.9 | 24.5 | -5.3% | -8.4 to 5.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.676 | 0.835 | +23.5% | 0.00361 to 0.314 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 55.3 | 53.2 | -3.8% | -64.8 to 60.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
