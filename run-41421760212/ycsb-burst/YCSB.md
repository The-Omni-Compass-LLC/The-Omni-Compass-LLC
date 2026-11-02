# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,877 | +0.0% | -3.1 to 5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,886 | +0.0% | -1.75 to 3.49 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.528 | 0.528 | -0.1% | -0.0258 to 0.0252 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.681 | 0.683 | +0.2% | -0.0356 to 0.039 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.226 | +0.5% | -0.00614 to 0.00827 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,502 | 1,502 | +0.0% | -6.68 to 7.83 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 77,627 | 77,635 | +0.0% | -380 to 396 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.213 | +16.8% | -0.0619 to 0.123 | STEADY, no difference beyond the noise |
| host CPU-seconds | 126 | 152 | +20.6% | -54.2 to 106 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.286 | +20.6% | -0.102 to 0.199 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 78.2 | 78.3 | +0.1% | -2.8 to 2.96 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 77.2 | 77.2 | +0.1% | -2.78 to 2.91 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.02 | 1.04 | +1.7% | -0.0167 to 0.0521 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 126 | 152 | +20.6% | -54.2 to 106 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
