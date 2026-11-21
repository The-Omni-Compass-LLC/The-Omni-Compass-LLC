# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,394 | 2,437 | +1.8% | -578 to 663 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,408 | 2,452 | +1.8% | -576 to 662 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.347 | 0.341 | -1.5% | -0.0289 to 0.0183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.639 | 0.63 | -1.4% | -0.122 to 0.104 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.308 | 0.302 | -1.8% | -0.102 to 0.0911 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.6% | -13.6 to -3.11 | GAIN |
| bytes in the cache, mean (MB) | 393 | 381 | -3.1% | -20.3 to -3.94 | GAIN |
| pages read into the cache (misses) | 193,345 | 198,219 | +2.5% | -93,066 to 102,816 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.114 | -6.0% | -0.0649 to 0.0505 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.4 | 80.7 | -6.6% | -49.2 to 37.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.18 | -8.6% | -0.113 to 0.0795 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
