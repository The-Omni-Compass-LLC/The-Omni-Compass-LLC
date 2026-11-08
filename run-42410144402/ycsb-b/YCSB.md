# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,943 | 2,943 | +0.0% | -0.941 to 1.25 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,944 | 2,945 | +0.0% | -1.01 to 1.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.093 | 0.0963 | +3.6% | -0.00787 to 0.0145 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.235 | 0.25 | +6.4% | -0.0484 to 0.0784 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.0504 | 0.0512 | +1.5% | -0.00333 to 0.00487 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,367 | 1,367 | -0.1% | -1.51 to -0.0529 | GAIN |
| pages read into the cache (misses) | 61,809 | 61,844 | +0.1% | -261 to 330 | shown, not judged |
| host CPU busy (share of the run) | 0.0641 | 0.0884 | +38.0% | 0.00547 to 0.0433 | power given |
| host CPU-seconds | 115 | 164 | +41.7% | 10.7 to 85.6 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.0861 | 0.122 | +41.7% | 0.00792 to 0.0639 | power given |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 43.3 | 43.5 | +0.6% | -1.87 to 2.36 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 41.7 | 42 | +0.5% | -1.9 to 2.33 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.56 | 1.59 | +1.8% | 0.00525 to 0.0515 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 115 | 164 | +41.7% | 10.7 to 85.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
