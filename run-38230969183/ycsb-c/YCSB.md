# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,911 | -0.0% | -18.7 to 15.8 | no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% | -17.9 to 14.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.255 | +0.5% | -0.0152 to 0.0179 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.383 | 0.391 | +2.3% | -0.00502 to 0.0223 | no difference beyond the noise |
| latency, mean (ms) | 0.0864 | 0.0884 | +2.2% | -0.00603 to 0.00985 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -20 to 9.4 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 414 | -1.1% | -22 to 12.6 | no difference beyond the noise |
| pages read into the cache (misses) | 458,458 | 490,998 | +7.1% | -86,843 to 151,924 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0869 | -21.6% | -0.139 to 0.091 | no difference beyond the noise |
| host CPU-seconds | 136 | 102 | -24.7% | -191 to 124 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.153 | 0.115 | -24.7% | -0.215 to 0.139 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
