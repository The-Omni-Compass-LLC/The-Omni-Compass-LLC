# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,894 | -0.1% | -4.24 to -1.73 | LOSS |
| throughput (operations a second) | 2,900 | 2,897 | -0.1% | -4.24 to -1.56 | LOSS |
| latency, 95th percentile (ms) | 0.317 | 0.319 | +0.6% | -0.0023 to 0.0063 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.46 | 0.459 | -0.4% | -0.0299 to 0.0266 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.203 | +1.4% | -0.000432 to 0.00588 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 470 | -8.1% | -129 to 45.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 384 | -8.4% | -118 to 47.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,006 | 753,047 | +7.9% | -152,520 to 262,602 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.187 | +7.9% | -0.0815 to 0.109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 293 | 321 | +9.4% | -169 to 224 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.241 | +9.4% | -0.127 to 0.168 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -0.484 to 4.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
