# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,885 | +0.0% | -4.76 to 5.67 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,894 | 2,895 | +0.0% | -6.81 to 8.78 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.445 | 0.448 | +0.7% | -0.0144 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.655 | 0.667 | +1.9% | -0.0205 to 0.0451 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.228 | +2.0% | -0.0027 to 0.0117 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 452 | -11.8% | -67.9 to -52.5 | GAIN |
| bytes in the cache, mean (MB) | 401 | 356 | -11.1% | -57.7 to -31 | GAIN |
| pages read into the cache (misses) | 274,416 | 289,980 | +5.7% | -5,487 to 36,615 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.176 | +6.0% | -0.0298 to 0.0497 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 120 | +6.6% | -26.8 to 41.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.226 | +6.6% | -0.0504 to 0.0785 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | -1.97 to 7.97 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
