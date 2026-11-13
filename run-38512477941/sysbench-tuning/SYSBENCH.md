# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,948 | -0.1% | -8.82 to 2.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,950 | -0.1% | -7.84 to 3.08 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,950 | -0.1% | -7.84 to 3.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.316 | +0.0% | -0.0258 to 0.0258 | EVEN, the same |
| latency, 99th percentile (ms) | 0.412 | 0.409 | -0.6% | -0.0313 to 0.0267 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.197 | +2.3% | -0.00759 to 0.0164 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 470 | -8.2% | -195 to 111 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 427 | -7.8% | -145 to 72.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,278 | 440,630 | +20.3% | -160,595 to 309,299 | shown, not judged |
| host CPU busy (share of the run) | 0.093 | 0.0987 | +6.1% | -0.0103 to 0.0217 | EVEN, no difference beyond the noise |
| host CPU-seconds | 154 | 164 | +6.5% | -17.6 to 37.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.114 | 0.121 | +6.6% | -0.0131 to 0.0281 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 2.13 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
