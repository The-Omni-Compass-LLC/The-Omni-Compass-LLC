# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,882 | +0.1% | -8.26 to 14.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,892 | +0.1% | -8.54 to 14.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.373 | 0.375 | +0.5% | -0.000484 to 0.00448 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.578 | 0.581 | +0.4% | -0.0122 to 0.0169 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.226 | -0.1% | -0.00653 to 0.00602 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -16.3 to 1.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 413 | -1.1% | -12.2 to 2.84 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 669,409 | 683,571 | +2.1% | -9,290 to 37,615 | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.229 | +6.4% | -0.0383 to 0.066 | EVEN, no difference beyond the noise |
| host CPU-seconds | 361 | 393 | +8.6% | -88.3 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.296 | +8.5% | -0.0678 to 0.114 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
