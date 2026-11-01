# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.0% | -3.5 to 3.66 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.2% | -0.886 to 0.114 | STEADY, no difference beyond the noise |
| queries a second | 3,950 | 3,942 | -0.2% | -17.7 to 2.28 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.4 | 5.6 | -12.5% | -3.56 to 1.96 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 20.8 | 16.5 | -20.6% | -13.1 to 4.58 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.41 | 3.21 | -5.8% | -0.898 to 0.501 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,199 | +134.1% | 573 to 801 | power given |
| pages holding data, mean (MB) | 463 | 990 | +113.7% | 480 to 574 | power given |
| pages read from disk into the pool (misses) | 617,268 | 146,327 | -76.3% | -526,851 to -415,031 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.12 | -6.4% | -0.00881 to -0.00755 | GAIN |
| host CPU-seconds | 228 | 214 | -6.4% | -15.4 to -13.6 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.6 | 2.43 | -6.4% | -0.21 to -0.123 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 9.67 |  | 2.49 to 16.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
