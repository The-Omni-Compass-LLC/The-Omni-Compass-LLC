# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,702 | 5,703 | +0.0% | -19.1 to 22.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,717 | 5,719 | +0.0% | -19.5 to 23.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.429 | 0.429 | -0.1% | -0.00607 to 0.0054 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.633 | 0.629 | -0.5% | -0.0161 to 0.00942 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.249 | 0.249 | +0.1% | -0.00235 to 0.00279 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -6.86 to -3.51 | GAIN |
| bytes in the cache, mean (MB) | 417 | 414 | -0.7% | -5.71 to -0.0769 | GAIN |
| pages read into the cache (misses) | 683,118 | 689,155 | +0.9% | -5,836 to 17,909 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.284 | +1.2% | -0.0119 to 0.0188 | EVEN, no difference beyond the noise |
| host CPU-seconds | 477 | 484 | +1.6% | -26.7 to 41.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.18 | 0.182 | +1.4% | -0.0109 to 0.0161 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
