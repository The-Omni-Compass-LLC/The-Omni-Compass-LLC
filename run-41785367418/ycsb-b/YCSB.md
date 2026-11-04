# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | -0.0% | -1.58 to 1.41 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -0.901 to -0.00749 | LOSS |
| latency, 95th percentile (ms) | 0.325 | 0.325 | +0.1% | -0.0356 to 0.0363 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.521 | 0.523 | +0.5% | -0.0156 to 0.021 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.192 | +0.4% | -0.00651 to 0.00813 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -0.285 to 0.781 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 61,767 | 61,860 | +0.2% | -280 to 468 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.198 | +8.8% | -0.0468 to 0.0787 | STEADY, no difference beyond the noise |
| host CPU-seconds | 314 | 348 | +10.7% | -98.9 to 166 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.236 | 0.261 | +10.7% | -0.0744 to 0.125 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 187 | +0.5% | -4.19 to 5.95 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 184 | +0.4% | -4.37 to 5.98 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 2.59 | +2.9% | -0.0604 to 0.205 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 314 | 348 | +10.7% | -98.9 to 166 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
