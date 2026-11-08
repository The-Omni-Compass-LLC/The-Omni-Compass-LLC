# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | -0.0% | -5.45 to 3.81 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,906 | +0.0% | -3.19 to 3.24 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.359 | 0.338 | -5.8% | -0.0341 to -0.00785 | GAIN |
| latency, 99th percentile (ms) | 0.616 | 0.609 | -1.1% | -0.016 to 0.00196 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.163 | 0.157 | -3.8% | -0.00805 to -0.00421 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,578 | +208.2% | 915 to 1,218 | power given |
| bytes in the cache, mean (MB) | 417 | 1,218 | +192.1% | 686 to 916 | power given |
| pages read into the cache (misses) | 680,277 | 122,555 | -82.0% | -592,417 to -523,026 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.211 | +9.7% | -0.0157 to 0.0529 | STEADY, no difference beyond the noise |
| host CPU-seconds | 343 | 388 | +13.2% | -33.2 to 124 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.258 | 0.292 | +13.2% | -0.025 to 0.0932 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 16 |  | 7.39 to 24.6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 197 | 185 | -6.0% | -12.9 to -10.6 | GAIN |
| the server's own CPU-seconds (mongod) | 194 | 182 | -6.4% | -13.5 to -11.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 3.14 | +26.4% | 0.475 to 0.836 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 343 | 388 | +13.2% | -33.2 to 124 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 8.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
