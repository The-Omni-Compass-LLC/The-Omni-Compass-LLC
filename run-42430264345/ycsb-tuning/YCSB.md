# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,881 | +0.0% | -0.568 to 1.49 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,887 | +0.0% | -0.241 to 2.09 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.343 | 0.346 | +1.1% | -0.01 to 0.0173 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.539 | 0.547 | +1.5% | -0.0205 to 0.0371 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.209 | -0.5% | -0.00925 to 0.00729 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,362 | -0.0% | -11.5 to 10.2 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 63,230 | 63,163 | -0.1% | -442 to 307 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.218 | -12.4% | -0.192 to 0.13 | STEADY, no difference beyond the noise |
| host CPU-seconds | 447 | 378 | -15.3% | -439 to 302 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.336 | 0.285 | -15.3% | -0.33 to 0.228 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 237 | 234 | -1.1% | -14.6 to 9.18 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 234 | 231 | -1.2% | -14.6 to 9.02 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.6 | 2.68 | +3.0% | -0.0768 to 0.234 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 447 | 378 | -15.3% | -439 to 302 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
