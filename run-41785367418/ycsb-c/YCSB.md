# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,903 | 2,904 | +0.0% | -0.127 to 0.99 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,906 | +0.0% | 0.0941 to 0.706 | GAIN |
| latency, 95th percentile (ms) | 0.275 | 0.275 | -0.2% | -0.00826 to 0.00692 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.456 | +0.1% | -0.0393 to 0.04 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.145 | 0.145 | -0.4% | -0.00421 to 0.00302 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | -0.0% | -3.07 to 2.48 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,678 | 61,650 | -0.0% | -138 to 82.2 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.181 | +22.8% | 0.00787 to 0.0595 | power given |
| host CPU-seconds | 262 | 335 | +28.0% | 12.3 to 134 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.251 | +28.0% | 0.00916 to 0.101 | power given |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 132 | 132 | -0.2% | -3.29 to 2.83 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 129 | 129 | -0.2% | -3.26 to 2.64 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 2.63 | +3.1% | -0.0337 to 0.192 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 262 | 335 | +28.0% | 12.3 to 134 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
