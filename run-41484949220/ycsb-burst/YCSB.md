# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,890 | -0.3% | -45.7 to 30.6 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,902 | -0.3% | -45 to 29.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.314 | 0.32 | +2.0% | -0.0279 to 0.0406 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.495 | -0.3% | -0.0731 to 0.0704 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.168 | 0.173 | +2.6% | -0.00622 to 0.0149 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 729 | +42.5% | -290 to 725 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 571 | +42.1% | -229 to 567 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 259,774 | 231,982 | -10.7% | -115,749 to 60,165 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.141 | -11.0% | -0.105 to 0.0697 | STEADY, no difference beyond the noise |
| host CPU-seconds | 114 | 99.7 | -12.8% | -87.4 to 58.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.188 | -12.7% | -0.165 to 0.11 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.33 |  | -1.54 to 4.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 63.3 | 63.3 | +0.0% | -0.641 to 0.655 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 62.5 | 62.2 | -0.4% | -0.896 to 0.456 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.824 | 1.05 | +27.5% | 0.176 to 0.278 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 114 | 99.7 | -12.8% | -87.4 to 58.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
