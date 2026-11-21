# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,926 | +0.0% | -6 to 6.44 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,931 | 2,931 | -0.0% | -6.07 to 5.65 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.379 | 0.373 | -1.5% | -0.0202 to 0.00889 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.554 | 0.539 | -2.7% | -0.078 to 0.048 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.151 | 0.148 | -2.2% | -0.0112 to 0.0045 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 500 | -2.3% | -25 to 1.7 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 408 | 398 | -2.4% | -31.6 to 12.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,440 | 277,554 | +5.4% | -8,485 to 36,713 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.156 | +8.8% | -0.0679 to 0.0931 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 117 | +11.0% | -58.3 to 81.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.219 | +11.0% | -0.109 to 0.152 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
