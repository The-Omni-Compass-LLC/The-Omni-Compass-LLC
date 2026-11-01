# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | -0.0% | -1.75 to 0.697 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | -0.0% | -2.08 to 0.736 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.323 | 0.319 | -1.2% | -0.0178 to 0.00983 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.584 | 0.577 | -1.3% | -0.0174 to 0.00271 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.195 | -2.1% | -0.0103 to 0.00216 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 418 | 418 | +0.1% | -5.17 to 6.08 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 699,368 | 721,068 | +3.1% | -201,597 to 244,996 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.193 | -3.6% | -0.0771 to 0.0629 | STEADY, no difference beyond the noise |
| host CPU-seconds | 351 | 337 | -4.0% | -165 to 137 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.254 | -4.0% | -0.124 to 0.103 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 198 | 193 | -2.5% | -11.3 to 1.34 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 195 | 190 | -2.8% | -11.9 to 0.779 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.47 | 3.05 | +23.4% | 0.528 to 0.63 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 351 | 337 | -4.0% | -165 to 137 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
