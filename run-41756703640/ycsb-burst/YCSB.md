# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,883 | -0.0% | -1.03 to 0.846 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | +0.0% | -1.22 to 1.72 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.416 | 0.423 | +1.7% | -0.0182 to 0.0322 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.573 | +0.9% | -0.0171 to 0.0271 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.213 | +1.6% | -0.000884 to 0.00745 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| bytes in the cache, mean (MB) | 404 | 403 | -0.3% | -27.1 to 25 | STEADY, no difference beyond the noise |
| pages read into the cache (misses) | 274,066 | 277,616 | +1.3% | -47,765 to 54,866 | shown, not judged |
| host CPU busy (share of the run) | 0.205 | 0.212 | +3.5% | -0.19 to 0.205 | STEADY, no difference beyond the noise |
| host CPU-seconds | 146 | 154 | +5.3% | -174 to 190 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.274 | 0.289 | +5.3% | -0.327 to 0.356 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 79.1 | 81.3 | +2.7% | -1.88 to 6.17 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 78.1 | 80.1 | +2.5% | -2.08 to 5.94 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.977 | 1.19 | +21.8% | 0.173 to 0.253 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 146 | 154 | +5.3% | -174 to 190 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
