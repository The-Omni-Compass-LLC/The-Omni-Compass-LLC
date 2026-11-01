# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,957 | 2,952 | -0.2% | -13.5 to 3.39 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,963 | -0.1% | -9.29 to 4.5 | STEADY, no difference beyond the noise |
| queries a second | 2,965 | 2,963 | -0.1% | -9.29 to 4.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.214 | 0.209 | -2.0% | -0.0503 to 0.0416 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.377 | 0.386 | +2.3% | -0.0325 to 0.0498 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.237 | +13.2% | 0.00125 to 0.0541 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,161 | +126.8% | 604 to 694 | power given |
| pages holding data, mean (MB) | 470 | 920 | +95.7% | 418 to 482 | power given |
| pages read from disk into the pool (misses) | 369,952 | 78,494 | -78.8% | -300,883 to -282,033 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.111 | -2.4% | -0.00985 to 0.00441 | STEADY, no difference beyond the noise |
| host CPU-seconds | 202 | 197 | -2.4% | -17.5 to 7.65 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.146 | -2.3% | -0.0132 to 0.00644 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | -0.505 to 13.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
