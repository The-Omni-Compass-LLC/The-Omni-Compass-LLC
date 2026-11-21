# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,697 | 5,531 | -2.9% | -611 to 279 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,713 | 5,548 | -2.9% | -611 to 281 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.327 | 0.336 | +2.7% | -0.0136 to 0.0309 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.506 | 0.53 | +4.6% | -0.0194 to 0.0661 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.219 | +4.2% | -0.00567 to 0.0232 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 490 | -4.3% | -99.4 to 55.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 394 | -4.9% | -79.2 to 38.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,028 | 709,512 | +4.8% | -179,872 to 244,840 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.239 | -0.4% | -0.0505 to 0.0485 | EVEN, no difference beyond the noise |
| host CPU-seconds | 435 | 433 | -0.6% | -102 to 96.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.169 | +2.2% | -0.0284 to 0.0357 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
