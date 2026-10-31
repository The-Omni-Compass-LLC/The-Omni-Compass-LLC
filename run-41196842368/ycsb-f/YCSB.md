# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,673 | 5,676 | +0.0% | -26.6 to 32 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,691 | 5,693 | +0.0% | -28.2 to 33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.434 | 0.427 | -1.7% | -0.0102 to -0.00446 | GAIN |
| latency, 99th percentile (ms) | 0.662 | 0.656 | -0.8% | -0.0133 to 0.00265 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.248 | 0.243 | -2.2% | -0.00795 to -0.00315 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,352 | +164.0% | 653 to 1,026 | power given |
| bytes in the cache, mean (MB) | 417 | 1,059 | +154.1% | 500 to 785 | power given |
| pages read into the cache (misses) | 681,694 | 298,319 | -56.2% | -534,578 to -232,173 | shown, not judged |
| host CPU busy (share of the run) | 0.335 | 0.321 | -4.2% | -0.0178 to -0.0106 | GAIN |
| host CPU-seconds | 613 | 579 | -5.6% | -44.6 to -24 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.218 | -5.6% | -0.0179 to -0.00816 | GAIN |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 356 | 347 | -2.7% | -14 to -4.97 | GAIN |
| the server's own CPU-seconds (mongod) | 352 | 342 | -2.9% | -14.6 to -5.72 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.4 | 5.09 | +15.7% | 0.519 to 0.863 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 613 | 579 | -5.6% | -44.6 to -23.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
