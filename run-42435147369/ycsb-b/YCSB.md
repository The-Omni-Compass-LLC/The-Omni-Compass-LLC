# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,903 | 2,901 | -0.1% | -4.61 to 0.776 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,908 | -0.0% | -3.51 to 2.88 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.333 | 0.339 | +2.0% | -0.0258 to 0.0391 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.546 | 0.566 | +3.7% | -0.0671 to 0.107 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.138 | 0.14 | +1.3% | -0.0057 to 0.00936 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -122 to 196 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 447 | +6.6% | -94.4 to 150 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 704,357 | 641,076 | -9.0% | -221,819 to 95,258 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.167 | +9.0% | -0.0247 to 0.0523 | STEADY, no difference beyond the noise |
| host CPU-seconds | 274 | 304 | +10.9% | -52.2 to 112 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.206 | 0.228 | +10.9% | -0.0393 to 0.0843 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 126 | 128 | +1.2% | -3.84 to 6.96 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 124 | 125 | +0.7% | -4.53 to 6.22 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 3.22 | +28.7% | 0.624 to 0.808 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 274 | 304 | +10.9% | -52.2 to 112 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
