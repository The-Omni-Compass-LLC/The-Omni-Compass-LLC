# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,938 | 2,941 | +0.1% | -38.9 to 43.5 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,965 | -0.0% | -21.2 to 19.7 | STEADY, no difference beyond the noise |
| queries a second | 2,966 | 2,965 | -0.0% | -21.2 to 19.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.286 | -13.8% | -0.131 to 0.0397 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.581 | 1.38 | +137.9% | -3.39 to 4.99 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.552 | 0.7 | +26.8% | -1.67 to 1.97 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,205 | +135.4% | 683 to 704 | power given |
| pages holding data, mean (MB) | 464 | 922 | +98.8% | 446 to 470 | power given |
| pages read from disk into the pool (misses) | 368,156 | 76,708 | -79.2% | -300,652 to -282,243 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.127 | -7.9% | -0.0265 to 0.0047 | STEADY, no difference beyond the noise |
| host CPU-seconds | 244 | 225 | -7.8% | -46.9 to 8.62 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.182 | 0.168 | -7.9% | -0.0356 to 0.00693 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 8.9 to 11.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
