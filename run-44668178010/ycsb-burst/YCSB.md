# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,880 | -0.0% | -3.58 to 1.07 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -3.14 to 0.475 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.429 | 0.432 | +0.7% | 0.000516 to 0.00548 | LOSS |
| latency, 99th percentile (ms) | 0.596 | 0.597 | +0.3% | -0.0258 to 0.0291 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.216 | +0.4% | -0.00778 to 0.00945 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 533 | +4.1% | -70.1 to 113 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 420 | +4.5% | -57.8 to 93.7 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 264,367 | 254,011 | -3.9% | -38,257 to 17,545 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.191 | -9.3% | -0.115 to 0.0758 | STEADY, no difference beyond the noise |
| host CPU-seconds | 150 | 132 | -11.7% | -99 to 64 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.282 | 0.249 | -11.7% | -0.186 to 0.12 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80.8 | 80.9 | +0.1% | -6.32 to 6.45 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 79.8 | 79.6 | -0.2% | -6.52 to 6.19 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.03 | 1.26 | +22.3% | 0.192 to 0.266 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 150 | 132 | -11.7% | -99 to 64 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
