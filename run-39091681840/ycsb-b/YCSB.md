# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,916 | 2,914 | -0.1% | -10.4 to 6.81 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,920 | 2,918 | -0.1% | -10.2 to 6.43 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.274 | 0.26 | -5.2% | -0.0293 to 0.000642 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.421 | 0.418 | -0.6% | -0.0238 to 0.0185 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.16 | 0.159 | -0.6% | -0.0119 to 0.0101 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -22.5 to 10.7 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 416 | -1.1% | -16.4 to 7.15 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 726,395 | 695,459 | -4.3% | -51,286 to -10,586 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.16 | -5.3% | -0.0381 to 0.0202 | EVEN, no difference beyond the noise |
| host CPU-seconds | 307 | 288 | -6.0% | -84.1 to 47.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.216 | -6.0% | -0.0634 to 0.0357 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
