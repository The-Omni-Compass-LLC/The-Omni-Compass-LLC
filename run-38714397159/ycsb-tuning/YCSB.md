# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,882 | +0.1% | -11.5 to 17 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,891 | +0.1% | -11.8 to 15.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.375 | 0.374 | -0.4% | -0.0136 to 0.0109 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.583 | 0.575 | -1.4% | -0.0277 to 0.0117 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.227 | +0.2% | -0.0118 to 0.0126 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 445 | -13.0% | -75.8 to -57.8 | GAIN |
| bytes in the cache, mean (MB) | 417 | 366 | -12.2% | -55.2 to -46.8 | GAIN |
| pages read into the cache (misses) | 675,237 | 774,154 | +14.6% | 90,194 to 107,640 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.239 | -2.6% | -0.0474 to 0.0347 | EVEN, no difference beyond the noise |
| host CPU-seconds | 427 | 412 | -3.5% | -108 to 78.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.322 | 0.311 | -3.6% | -0.0806 to 0.0572 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
