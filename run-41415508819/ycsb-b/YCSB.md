# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,885 | -0.0% | -3.84 to 1.98 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -3.99 to 2.16 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.322 | 0.33 | +2.3% | -0.0115 to 0.0261 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.592 | 0.595 | +0.6% | -0.0143 to 0.021 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.202 | +0.7% | -0.00372 to 0.00646 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 532 | +3.9% | -65.6 to 105 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 433 | +3.6% | -59.5 to 89.8 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 708,007 | 689,861 | -2.6% | -46,896 to 10,605 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.19 | +12.0% | -0.0341 to 0.0747 | STEADY, no difference beyond the noise |
| host CPU-seconds | 286 | 328 | +14.5% | -74.6 to 158 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.246 | +14.6% | -0.056 to 0.119 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 199 | 202 | +1.4% | -2.53 to 8.04 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 196 | 198 | +1.1% | -3.04 to 7.24 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.44 | 3.1 | +26.8% | 0.485 to 0.823 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 286 | 328 | +14.5% | -74.6 to 158 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
