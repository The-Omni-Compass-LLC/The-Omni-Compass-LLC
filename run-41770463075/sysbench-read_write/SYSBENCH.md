# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 197 | +2.2% | 1.36 to 7.24 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.35 to 2.6 | STEADY, no difference beyond the noise |
| queries a second | 3,937 | 3,939 | +0.1% | -47.1 to 52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.58 | 6.87 | -19.9% | -1.82 to -1.59 | GAIN |
| latency, 99th percentile (ms) | 12.8 | 8.79 | -31.5% | -4.32 to -3.76 | GAIN |
| latency, mean (ms) | 5.21 | 4.86 | -6.7% | -0.471 to -0.227 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,040 | +103.2% | 513 to 544 | power given |
| pages holding data, mean (MB) | 463 | 930 | +101.1% | 443 to 492 | power given |
| pages read from disk into the pool (misses) | 616,632 | 119,616 | -80.6% | -560,422 to -433,610 | shown, not judged |
| host CPU busy (share of the run) | 0.279 | 0.261 | -6.4% | -0.0307 to -0.00519 | GAIN |
| host CPU-seconds | 491 | 459 | -6.5% | -53.7 to -10.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.58 | 5.1 | -8.5% | -0.643 to -0.31 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
