# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,875 | -0.1% | -12.7 to 6.67 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,885 | -0.0% | -6.14 to 4.04 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.468 | 0.474 | +1.2% | -0.00468 to 0.016 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.65 | 0.679 | +4.5% | -0.0377 to 0.0957 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.228 | +1.7% | -0.00903 to 0.0167 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 523 | +2.1% | -35 to 56.3 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 410 | +2.1% | -24.8 to 41.7 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 268,149 | 261,793 | -2.4% | -25,709 to 12,996 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.221 | +10.1% | -0.0179 to 0.0584 | STEADY, no difference beyond the noise |
| host CPU-seconds | 140 | 158 | +12.9% | -14.1 to 50.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.297 | +13.0% | -0.0262 to 0.0945 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 82.7 | 83.6 | +1.0% | -5.76 to 7.46 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 81.7 | 82.3 | +0.7% | -5.91 to 7.11 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.04 | 1.29 | +24.6% | 0.155 to 0.355 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 140 | 158 | +12.9% | -14.1 to 50.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
