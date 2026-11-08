# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,912 | -0.0% | -1.38 to 0.825 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,916 | +0.0% | -0.578 to 0.693 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.206 | 0.207 | +0.5% | -0.00397 to 0.00597 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.394 | 0.399 | +1.2% | -0.0202 to 0.0296 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.142 | 0.144 | +1.3% | -0.00616 to 0.00998 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 417 | 419 | +0.7% | -0.0588 to 5.56 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 705,773 | 722,217 | +2.3% | -100,979 to 133,868 | shown, not judged |
| host CPU busy (share of the run) | 0.176 | 0.162 | -7.8% | -0.0757 to 0.0481 | STEADY, no difference beyond the noise |
| host CPU-seconds | 325 | 294 | -9.6% | -174 to 112 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.244 | 0.22 | -9.6% | -0.13 to 0.0835 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 151 | 152 | +0.8% | -2.14 to 4.47 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 149 | 149 | +0.4% | -2.6 to 3.88 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.97 | 2.5 | +26.7% | 0.45 to 0.604 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 325 | 294 | -9.6% | -174 to 112 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
