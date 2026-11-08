# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,672 | 5,674 | +0.0% | -32.2 to 37.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,690 | 5,693 | +0.0% | -31.8 to 36.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.451 | 0.445 | -1.3% | -0.0137 to 0.00232 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.714 | 0.711 | -0.4% | -0.00892 to 0.00359 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.25 | 0.247 | -1.4% | -0.00389 to -0.00322 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,425 | +178.3% | 688 to 1,137 | power given |
| bytes in the cache, mean (MB) | 416 | 1,111 | +167.1% | 526 to 865 | power given |
| pages read into the cache (misses) | 679,199 | 241,999 | -64.4% | -553,246 to -321,155 | shown, not judged |
| host CPU busy (share of the run) | 0.331 | 0.33 | -0.1% | -0.0146 to 0.0141 | STEADY, no difference beyond the noise |
| host CPU-seconds | 598 | 600 | +0.3% | -30 to 33.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.226 | +0.2% | -0.013 to 0.0141 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.33 |  | -7.01 to 21.7 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 358 | 351 | -1.9% | -10.1 to -3.73 | GAIN |
| the server's own CPU-seconds (mongod) | 354 | 346 | -2.2% | -10.6 to -4.61 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.51 | 5.18 | +15.0% | 0.455 to 0.895 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 598 | 600 | +0.3% | -30 to 33.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
