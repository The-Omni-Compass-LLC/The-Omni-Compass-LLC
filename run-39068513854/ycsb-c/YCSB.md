# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,934 | -0.1% | -4.38 to 0.75 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,936 | -0.1% | -4.44 to 0.92 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.213 | 0.219 | +2.8% | 0.00103 to 0.011 | LOSS |
| latency, 99th percentile (ms) | 0.409 | 0.408 | -0.2% | -0.00597 to 0.00397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.107 | 0.109 | +1.9% | -0.00205 to 0.00615 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 489 | -4.6% | -105 to 58.1 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 403 | -3.7% | -77 to 46.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 642,545 | 738,450 | +14.9% | -62,237 to 254,047 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.115 | -2.9% | -0.0143 to 0.00759 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 209 | -3.5% | -29.8 to 14.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.162 | 0.156 | -3.5% | -0.0222 to 0.0108 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -1.46 to 6.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
