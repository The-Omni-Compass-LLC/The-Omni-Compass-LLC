# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.38, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,902 | -0.1% | -12.2 to 5.64 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,914 | 2,911 | -0.1% | -14 to 8.41 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.222 | 0.22 | -1.2% | -0.0216 to 0.0163 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.42 | 0.418 | -0.6% | -0.0229 to 0.0176 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.161 | 0.16 | -0.4% | -0.00908 to 0.00775 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 772 | +50.8% | -621 to 1,142 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 592 | +41.4% | -394 to 741 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 677,544 | 494,846 | -27.0% | -749,978 to 384,582 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.174 | -15.5% | -0.0509 to -0.0128 | GAIN |
| host CPU-seconds | 374 | 304 | -18.6% | -118 to -20.8 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.28 | 0.228 | -18.5% | -0.0882 to -0.0155 | GAIN |
| cache size changes written (the knob's moves) | 0 | 13.7 |  | -43 to 70.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 212 | 209 | -1.4% | -14.9 to 9.05 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 210 | 206 | -1.7% | -15.5 to 8.6 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.04 | 2.57 | +26.2% | 0.446 to 0.622 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 374 | 304 | -18.6% | -118 to -20.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
