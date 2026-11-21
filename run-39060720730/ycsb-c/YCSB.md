# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,933 | 2,934 | +0.0% | -4.46 to 5.59 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,935 | 2,936 | +0.0% | -4.74 to 5.83 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.2 | 0.199 | -0.2% | -0.0535 to 0.0528 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.347 | 0.344 | -0.9% | -0.044 to 0.038 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0784 | 0.0781 | -0.5% | -0.0044 to 0.00366 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 489 | -4.4% | -110 to 64.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 402 | -4.5% | -89 to 51.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 719,708 | 719,992 | +0.0% | -232,882 to 233,450 | shown, not judged |
| host CPU busy (share of the run) | 0.0856 | 0.0917 | +7.1% | -0.0693 to 0.0815 | EVEN, no difference beyond the noise |
| host CPU-seconds | 154 | 166 | +7.4% | -138 to 161 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.115 | 0.124 | +7.3% | -0.103 to 0.12 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
