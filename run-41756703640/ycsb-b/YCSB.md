# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,935 | -0.0% | -5.4 to 4.19 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,937 | -0.0% | -4.74 to 3.61 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.186 | 0.199 | +7.2% | -0.0433 to 0.07 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.37 | 0.376 | +1.5% | -0.0143 to 0.0256 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0716 | 0.072 | +0.6% | -0.0061 to 0.00694 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 419 | -0.4% | -7.46 to 3.71 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 715,724 | 716,371 | +0.1% | -117,519 to 118,813 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.0767 | -29.7% | -0.124 to 0.0596 | STEADY, no difference beyond the noise |
| host CPU-seconds | 202 | 136 | -32.6% | -253 to 122 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.151 | 0.102 | -32.5% | -0.189 to 0.0909 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 66.3 | 67.4 | +1.7% | -6.02 to 8.29 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 64.5 | 65.1 | +0.9% | -6.32 to 7.52 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.78 | 2.32 | +30.1% | 0.301 to 0.771 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 202 | 136 | -32.6% | -253 to 122 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
