# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,893 | -0.1% | -4.25 to 1.05 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% | -3.91 to 0.794 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.343 | 0.342 | -0.1% | -0.00832 to 0.00765 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.51 | 0.509 | -0.3% | -0.0166 to 0.0133 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.205 | -0.5% | -0.00649 to 0.00459 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -18.3 to 7.88 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 415 | -0.7% | -20.5 to 15 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 708,387 | 710,318 | +0.3% | -153,992 to 157,856 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.181 | +0.0% | -0.0456 to 0.0457 | EVEN, no difference beyond the noise |
| host CPU-seconds | 306 | 306 | +0.0% | -92.2 to 92.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.23 | +0.0% | -0.0692 to 0.0694 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
