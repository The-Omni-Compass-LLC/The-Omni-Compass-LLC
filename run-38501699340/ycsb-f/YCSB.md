# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,749 | 5,741 | -0.1% | -27.7 to 12.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,763 | 5,756 | -0.1% | -28 to 13.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.365 | 0.37 | +1.6% | -0.00889 to 0.0202 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.597 | 0.609 | +2.0% | -0.0288 to 0.0521 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.202 | +1.5% | -0.00434 to 0.0102 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 449 | -12.3% | -64.2 to -61.8 | GAIN |
| bytes in the cache, mean (MB) | 417 | 369 | -11.5% | -51.9 to -43.8 | GAIN |
| pages read into the cache (misses) | 693,965 | 788,652 | +13.6% | 59,861 to 129,513 | shown, not judged |
| host CPU busy (share of the run) | 0.27 | 0.276 | +2.0% | -0.0364 to 0.0474 | EVEN, no difference beyond the noise |
| host CPU-seconds | 495 | 505 | +2.1% | -90.4 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.19 | +2.1% | -0.0345 to 0.0425 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
