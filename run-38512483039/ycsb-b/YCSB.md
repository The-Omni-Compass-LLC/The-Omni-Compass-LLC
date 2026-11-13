# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% | -6.11 to 2.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,898 | -0.1% | -5.25 to 2.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.336 | 0.343 | +2.1% | -0.021 to 0.035 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.508 | 0.514 | +1.2% | -0.00715 to 0.0191 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.205 | +0.4% | -0.00511 to 0.00655 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 450 | -12.2% | -63.6 to -61.2 | GAIN |
| bytes in the cache, mean (MB) | 418 | 367 | -12.2% | -60.9 to -41.4 | GAIN |
| pages read into the cache (misses) | 719,000 | 769,240 | +7.0% | -11,450 to 111,930 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.161 | -13.5% | -0.0966 to 0.0462 | EVEN, no difference beyond the noise |
| host CPU-seconds | 319 | 268 | -16.0% | -190 to 88.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.201 | -16.0% | -0.143 to 0.0663 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
