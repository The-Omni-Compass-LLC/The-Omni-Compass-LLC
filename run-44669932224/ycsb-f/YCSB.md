# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,749 | 5,753 | +0.1% | -3.46 to 13 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,760 | 5,765 | +0.1% | -0.696 to 12.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.31 | 0.31 | +0.0% | -0.00861 to 0.00861 | STEADY, the same |
| latency, 99th percentile (ms) | 0.471 | 0.479 | +1.6% | -0.0559 to 0.0712 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.175 | 0.179 | +2.1% | -0.0142 to 0.0217 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.0% | -10.9 to 9.54 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,027 | 63,054 | +0.0% | -436 to 490 | shown, not judged |
| host CPU busy (share of the run) | 0.233 | 0.242 | +3.5% | -0.0222 to 0.0386 | STEADY, no difference beyond the noise |
| host CPU-seconds | 421 | 441 | +4.7% | -50.8 to 90.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.158 | 0.165 | +4.7% | -0.019 to 0.0339 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 243 | 243 | -0.1% | -7.75 to 7.19 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 239 | 239 | -0.1% | -7.37 to 6.88 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.59 | 3.55 | -1.0% | -0.396 to 0.326 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 421 | 441 | +4.7% | -50.9 to 90.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
