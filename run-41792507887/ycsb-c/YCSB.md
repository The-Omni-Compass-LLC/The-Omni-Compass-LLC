# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,890 | -0.0% | -0.725 to 0.0919 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | -0.0% | -0.843 to 0.476 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.306 | 0.308 | +0.5% | -0.00213 to 0.00546 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.476 | 0.481 | +1.0% | -0.0327 to 0.042 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.192 | -0.2% | -0.00137 to 0.000504 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 421 | 417 | -0.8% | -8.97 to 2.49 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 706,662 | 711,309 | +0.7% | -122,476 to 131,770 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.182 | +0.4% | -0.105 to 0.106 | STEADY, no difference beyond the noise |
| host CPU-seconds | 312 | 313 | +0.3% | -219 to 221 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.235 | +0.3% | -0.164 to 0.166 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 188 | 188 | -0.2% | -4.31 to 3.63 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 186 | 185 | -0.5% | -4.94 to 3.11 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.43 | 3.01 | +23.8% | 0.502 to 0.654 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 312 | 313 | +0.3% | -219 to 221 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
