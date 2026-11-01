# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,753 | 5,755 | +0.0% | -6.96 to 11.9 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,764 | 5,766 | +0.0% | -4.56 to 9.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.31 | 0.312 | +0.6% | -0.00297 to 0.00697 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.462 | +2.4% | -0.052 to 0.074 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.179 | 0.179 | +0.0% | -0.0109 to 0.011 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,363 | -0.1% | -8.24 to 5.6 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,191 | 63,084 | -0.2% | -865 to 652 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.239 | -0.3% | -0.0706 to 0.0691 | STEADY, no difference beyond the noise |
| host CPU-seconds | 442 | 440 | -0.3% | -172 to 170 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.166 | 0.165 | -0.3% | -0.0646 to 0.0635 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 242 | 242 | +0.3% | -4.89 to 6.51 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 238 | 239 | +0.3% | -4.69 to 6.21 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.47 | 3.52 | +1.5% | -0.203 to 0.306 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 442 | 440 | -0.3% | -172 to 170 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
