# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,887 | +0.1% | -0.621 to 3.96 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,891 | +0.1% | -0.63 to 3.69 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.405 | 0.402 | -0.8% | -0.0145 to 0.00787 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.543 | 0.546 | +0.6% | -0.0108 to 0.0175 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.192 | +0.0% | -0.0047 to 0.00478 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,515 | 1,517 | +0.1% | -2.72 to 6.25 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,606 | 77,735 | +0.2% | 6.96 to 251 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.185 | -5.0% | -0.0232 to 0.0037 | STEADY, no difference beyond the noise |
| host CPU-seconds | 139 | 131 | -6.0% | -19.7 to 2.96 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.262 | 0.246 | -6.1% | -0.0372 to 0.00556 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 74.2 | 73.9 | -0.4% | -1.77 to 1.21 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 73.2 | 72.9 | -0.4% | -1.77 to 1.17 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.977 | 0.999 | +2.3% | -0.0298 to 0.0744 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 139 | 131 | -6.0% | -19.8 to 2.99 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
