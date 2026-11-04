# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,712 | 5,570 | -2.5% | -772 to 487 | STEADY, no difference beyond the noise |
| throughput (operations a second) | 5,730 | 5,590 | -2.4% | -768 to 488 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.323 | 0.318 | -1.7% | -0.0171 to 0.00641 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.506 | 0.521 | +3.0% | -0.0639 to 0.0939 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.198 | +1.6% | -0.0358 to 0.042 | STEADY, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 1,348 | +163.3% | 353 to 1,319 | power given |
| bytes in the cache, mean (MB) | 414 | 961 | +131.9% | 361 to 732 | power given |
| pages read into the cache (misses) | 695,485 | 188,954 | -72.8% | -625,058 to -388,005 | shown, not judged |
| host CPU busy (share of the run) | 0.248 | 0.242 | -2.5% | -0.0568 to 0.0443 | STEADY, no difference beyond the noise |
| host CPU-seconds | 450 | 440 | -2.3% | -114 to 93.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.17 | 0.17 | +0.2% | -0.0249 to 0.0255 | STEADY, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 37.7 |  | 7.61 to 67.7 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 273 | 260 | -4.7% | -44.4 to 18.5 | STEADY, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 270 | 256 | -5.0% | -44.6 to 17.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.49 | 4.11 | +17.8% | 0.0857 to 1.16 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 450 | 440 | -2.3% | -114 to 93.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 10.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
