# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 187 | 189 | +0.9% | -3.67 to 6.95 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | +0.4% | -1.39 to 2.83 | EVEN, no difference beyond the noise |
| queries a second | 3,892 | 3,907 | +0.4% | -27.8 to 56.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.74 | 9.51 | -2.4% | -2.19 to 1.71 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.7 | 14 | -5.3% | -1.93 to 0.372 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.89 | 4.79 | -2.1% | -0.458 to 0.256 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 554 | +8.1% | 16.1 to 66.9 | power given |
| pages holding data, mean (MB) | 461 | 488 | +5.7% | -13.3 to 66.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,010 | 558,755 | -9.0% | -107,640 to -2,868 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.222 | -1.4% | -0.00406 to -0.00226 | GAIN |
| host CPU-seconds | 406 | 400 | -1.4% | -7.54 to -3.91 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.7 | 4.6 | -2.3% | -0.234 to 0.0217 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.3 |  | 15.2 to 25.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
