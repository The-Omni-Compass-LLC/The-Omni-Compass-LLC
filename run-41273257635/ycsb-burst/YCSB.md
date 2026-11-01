# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,877 | +0.0% | -6.5 to 8.61 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,886 | +0.1% | -3.68 to 7.06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.468 | 0.465 | -0.5% | -0.0397 to 0.035 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.668 | 0.671 | +0.4% | -0.121 to 0.127 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.219 | 0.217 | -1.0% | -0.0104 to 0.00611 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,508 | 1,510 | +0.2% | 1.34 to 3.46 | power given |
| pages read into the cache (misses) | 77,560 | 77,723 | +0.2% | -319 to 647 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.194 | +0.0% | -0.11 to 0.11 | STEADY, no difference beyond the noise |
| host CPU-seconds | 135 | 136 | +0.2% | -95.5 to 95.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.255 | +0.1% | -0.179 to 0.18 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 79.3 | 77.5 | -2.4% | -3.26 to -0.494 | GAIN |
| the server's own CPU-seconds (mongod) | 78.3 | 76.4 | -2.4% | -3.24 to -0.541 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.06 | 1.07 | +1.4% | -0.0233 to 0.0522 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 135 | 136 | +0.2% | -95.5 to 95.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
