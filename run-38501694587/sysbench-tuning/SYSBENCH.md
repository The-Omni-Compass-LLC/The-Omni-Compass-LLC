# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,946 | -0.0% | -6.27 to 3.33 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,953 | -0.0% | -6.34 to 3.65 | EVEN, no difference beyond the noise |
| queries a second | 2,954 | 2,953 | -0.0% | -6.34 to 3.65 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.338 | -0.6% | -0.0248 to 0.0208 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.47 | 0.461 | -1.8% | -0.0298 to 0.0125 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.208 | +1.1% | -0.000806 to 0.00538 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 446 | -12.8% | -176 to 45 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 398 | -14.2% | -162 to 29.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,197 | 476,058 | +29.6% | -74,899 to 292,621 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.108 | +2.6% | 0.000289 to 0.00513 | power given |
| host CPU-seconds | 175 | 180 | +2.8% | 0.689 to 8.99 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.13 | 0.134 | +2.8% | 0.000353 to 0.00696 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | 12.2 to 15.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
