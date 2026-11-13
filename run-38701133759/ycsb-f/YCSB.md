# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,646 | 5,654 | +0.1% | -7.24 to 22.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,666 | 5,673 | +0.1% | -10.7 to 25.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.458 | 0.455 | -0.7% | -0.00957 to 0.00357 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.721 | 0.717 | -0.6% | -0.0147 to 0.00537 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.261 | 0.259 | -0.7% | -0.00521 to 0.00164 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -77.8 to -52.5 | GAIN |
| bytes in the cache, mean (MB) | 416 | 365 | -12.1% | -60.3 to -40.8 | GAIN |
| pages read into the cache (misses) | 667,539 | 771,485 | +15.6% | 81,235 to 126,659 | shown, not judged |
| host CPU busy (share of the run) | 0.289 | 0.293 | +1.5% | -0.00159 to 0.01 | EVEN, no difference beyond the noise |
| host CPU-seconds | 490 | 500 | +2.2% | -5.29 to 27 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.19 | +2.0% | -0.00304 to 0.0104 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
