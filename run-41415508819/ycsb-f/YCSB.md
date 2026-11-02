# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,736 | 5,739 | +0.1% | -15.4 to 22.5 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,758 | 5,761 | +0.1% | -11.7 to 17.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.354 | 0.348 | -1.8% | -0.0101 to -0.00254 | GAIN |
| latency, 99th percentile (ms) | 0.647 | 0.637 | -1.5% | -0.0214 to 0.00207 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.169 | 0.164 | -2.8% | -0.0078 to -0.00154 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,034 | +102.0% | -348 to 1,393 | STEADY, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 820 | +96.6% | -271 to 1,076 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 690,552 | 383,703 | -44.4% | -537,058 to -76,639 | shown, not judged |
| host CPU busy (share of the run) | 0.242 | 0.249 | +2.9% | -0.0163 to 0.0301 | STEADY, no difference beyond the noise |
| host CPU-seconds | 445 | 463 | +4.1% | -38.2 to 74.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.167 | 0.174 | +4.0% | -0.0139 to 0.0274 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | -4.06 to 13.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 232 | 227 | -2.2% | -12.1 to 1.85 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 228 | 222 | -2.5% | -12.7 to 1.11 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.08 | 4.72 | +15.5% | 0.514 to 0.753 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 445 | 463 | +4.1% | -38.2 to 74.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
