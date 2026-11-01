# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,669 | 5,743 | +1.3% | -167 to 315 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,687 | 5,761 | +1.3% | -163 to 311 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.323 | 0.318 | -1.3% | -0.0119 to 0.00326 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.496 | -0.1% | -0.0666 to 0.0653 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.189 | -3.3% | -0.0197 to 0.00665 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,176 | +129.6% | 159 to 1,168 | power given |
| bytes in the cache, mean (MB) | 413 | 911 | +120.5% | 116 to 880 | power given |
| pages read into the cache (misses) | 688,416 | 227,820 | -66.9% | -661,684 to -259,508 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.245 | +1.8% | -0.0135 to 0.0222 | STEADY, no difference beyond the noise |
| host CPU-seconds | 434 | 443 | +2.1% | -37.7 to 55.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.166 | +0.7% | -0.0235 to 0.0258 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 14 |  | 9.7 to 18.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 270 | 269 | -0.2% | -18.5 to 17.6 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 266 | 265 | -0.4% | -18.8 to 16.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.44 | 4.12 | +19.5% | 0.277 to 1.07 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 434 | 443 | +2.1% | -37.7 to 55.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
