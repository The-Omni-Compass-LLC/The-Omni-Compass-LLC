# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -2.84 to 2.71 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -2.97 to 2.87 | STEADY, no difference beyond the noise |
| queries a second | 4,720 | 4,719 | -0.0% | -47.5 to 45.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.34 | 3.32 | -0.6% | -0.106 to 0.0661 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.6 | 4.54 | -1.2% | -0.292 to 0.182 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.58 | 2.55 | -0.9% | -0.0477 to 0.000686 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 625 | +22.0% | -130 to 355 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 562 | +21.8% | -107 to 308 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,078 | 492,569 | -24.7% | -519,163 to 196,146 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.208 | -0.7% | -0.00443 to 0.00145 | STEADY, no difference beyond the noise |
| host CPU-seconds | 375 | 372 | -0.7% | -7.62 to 2.24 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.78 | 2.76 | -0.7% | -0.033 to -0.00526 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
