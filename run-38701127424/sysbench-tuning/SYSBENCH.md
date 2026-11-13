# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,958 | -0.1% | -14.9 to 10.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,963 | -0.1% | -12.7 to 9.52 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,963 | -0.1% | -12.7 to 9.52 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.217 | 0.207 | -4.6% | -0.131 to 0.111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.351 | 0.346 | -1.2% | -0.0752 to 0.0666 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0966 | 0.0965 | -0.1% | -0.0307 to 0.0305 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 419 | -18.3% | -156 to -31.3 | GAIN |
| pages holding data, mean (MB) | 464 | 380 | -18.0% | -139 to -28.2 | GAIN |
| pages read from disk into the pool (misses) | 366,829 | 518,677 | +41.4% | 22,316 to 281,378 | shown, not judged |
| host CPU busy (share of the run) | 0.0759 | 0.0754 | -0.6% | -0.0266 to 0.0257 | EVEN, no difference beyond the noise |
| host CPU-seconds | 136 | 135 | -0.6% | -47.6 to 46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.101 | 0.1 | -0.5% | -0.0356 to 0.0345 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 5.43 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
