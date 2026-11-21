# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,960 | 2,957 | -0.1% | -19.1 to 13.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,964 | -0.1% | -15.8 to 12.3 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,964 | -0.1% | -15.8 to 12.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.225 | 0.227 | +1.2% | -0.0375 to 0.0428 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.346 | 0.342 | -1.2% | -0.075 to 0.067 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.103 | 0.0967 | -6.0% | -0.0334 to 0.0211 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.0% | 0.0566 to 17.7 | power given |
| pages holding data, mean (MB) | 121 | 134 | +10.2% | 5.14 to 19.6 | power given |
| pages read from disk into the pool (misses) | 1,029,702 | 1,001,627 | -2.7% | -68,056 to 11,907 | shown, not judged |
| host CPU busy (share of the run) | 0.075 | 0.0731 | -2.6% | -0.016 to 0.0122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 134 | 131 | -2.6% | -28.8 to 21.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0998 | 0.0973 | -2.5% | -0.0217 to 0.0168 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
