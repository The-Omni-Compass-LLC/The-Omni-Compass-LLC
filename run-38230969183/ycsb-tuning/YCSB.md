# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,830 | 2,836 | +0.2% | -9.09 to 22.3 | no difference beyond the noise |
| throughput (operations a second) | 2,840 | 2,847 | +0.2% | -7.64 to 21.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.401 | 0.401 | +0.2% | -0.00806 to 0.00939 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.598 | 0.601 | +0.6% | -0.0118 to 0.0185 | no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.233 | -0.6% | -0.00551 to 0.00253 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -16 to 0.742 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 411 | -1.2% | -11.9 to 2.23 | no difference beyond the noise |
| pages read into the cache (misses) | 457,352 | 471,381 | +3.1% | -12,996 to 41,054 | shown, not judged |
| host CPU busy (share of the run) | 0.264 | 0.25 | -5.3% | -0.0925 to 0.0646 | no difference beyond the noise |
| host CPU-seconds | 304 | 282 | -7.1% | -143 to 99.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.348 | 0.323 | -7.3% | -0.167 to 0.116 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
