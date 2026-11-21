# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,874 | -0.2% | -9.39 to -0.91 | LOSS |
| throughput (operations a second) | 2,892 | 2,887 | -0.2% | -8.45 to -1.14 | LOSS |
| latency, 95th percentile (ms) | 0.445 | 0.442 | -0.7% | -0.0388 to 0.0328 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.701 | 0.695 | -0.8% | -0.0578 to 0.0465 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.241 | -0.4% | -0.00975 to 0.00761 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -5.98 to -2.18 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -3.32 to -0.712 | GAIN |
| pages read into the cache (misses) | 680,376 | 677,945 | -0.4% | -37,315 to 32,453 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.24 | +2.5% | -0.0684 to 0.0799 | EVEN, no difference beyond the noise |
| host CPU-seconds | 398 | 410 | +3.1% | -149 to 174 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.3 | 0.31 | +3.2% | -0.113 to 0.132 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
