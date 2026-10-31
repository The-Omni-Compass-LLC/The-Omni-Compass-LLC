# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 196 | +2.1% | 2.46 to 5.53 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.46 to 2.97 | EVEN, no difference beyond the noise |
| queries a second | 3,936 | 3,942 | +0.1% | -49.2 to 59.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.48 | 6.59 | -22.3% | -2.5 to -1.28 | GAIN |
| latency, 99th percentile (ms) | 12.8 | 8.58 | -33.1% | -5.26 to -3.24 | GAIN |
| latency, mean (ms) | 5.14 | 4.77 | -7.2% | -0.636 to -0.102 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,036 | +102.3% | 512 to 536 | power given |
| pages holding data, mean (MB) | 463 | 927 | +100.3% | 440 to 489 | power given |
| pages read from disk into the pool (misses) | 618,403 | 126,614 | -79.5% | -529,254 to -454,324 | shown, not judged |
| host CPU busy (share of the run) | 0.277 | 0.257 | -7.2% | -0.0248 to -0.0149 | GAIN |
| host CPU-seconds | 486 | 451 | -7.2% | -43.7 to -26.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.52 | 5.02 | -9.1% | -0.582 to -0.423 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
