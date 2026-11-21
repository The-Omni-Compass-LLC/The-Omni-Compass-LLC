# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,888 | -0.0% | -3.43 to 2.23 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% | -4.81 to 2.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.46 | 0.462 | +0.6% | -0.00854 to 0.0139 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.649 | 0.639 | -1.4% | -0.0549 to 0.0362 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.221 | +0.1% | -0.00194 to 0.00235 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 500 | -2.4% | -17.1 to -7.34 | GAIN |
| bytes in the cache, mean (MB) | 402 | 395 | -1.6% | -10.5 to -2.37 | GAIN |
| pages read into the cache (misses) | 261,404 | 276,038 | +5.6% | -46,294 to 75,561 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.183 | +10.6% | -0.154 to 0.189 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 127 | +11.9% | -130 to 157 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.239 | +11.9% | -0.244 to 0.295 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
