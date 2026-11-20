# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,884 | +0.0% | -0.456 to 2.87 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,888 | +0.0% | -0.426 to 2.72 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.337 | -0.1% | -0.0055 to 0.00484 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.494 | 0.494 | +0.0% | -0.00497 to 0.00497 | STEADY, the same |
| latency, mean (ms) | 0.203 | 0.204 | +0.1% | -0.0032 to 0.00359 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,363 | -0.1% | -6.5 to 4.3 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,348 | 62,975 | -0.6% | -1,316 to 570 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.219 | +3.9% | -0.0263 to 0.0428 | STEADY, no difference beyond the noise |
| host CPU-seconds | 358 | 376 | +5.2% | -55.6 to 93 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.269 | 0.283 | +5.2% | -0.0417 to 0.0697 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 233 | 234 | +0.3% | -1.5 to 3.04 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 230 | 231 | +0.3% | -1.62 to 2.94 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.53 | 2.64 | +4.4% | 0.0367 to 0.185 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 358 | 376 | +5.2% | -55.6 to 93 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
