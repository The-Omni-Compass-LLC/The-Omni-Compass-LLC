# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 190 | +0.1% | -1.69 to 2.01 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.2% | -0.706 to -0.00714 | LOSS |
| queries a second | 3,928 | 3,921 | -0.2% | -14.1 to -0.143 | LOSS |
| latency, 95th percentile (ms) | 9.45 | 9.22 | -2.4% | -0.71 to 0.259 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.3 | 14 | -2.0% | -3.69 to 3.13 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.79 | 5.56 | -4.0% | -1.54 to 1.08 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 571 | +11.5% | -24.2 to 142 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 502 | +8.5% | -30.3 to 109 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,623 | 532,653 | -13.5% | -225,646 to 59,706 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.21 | -2.6% | -0.0155 to 0.00439 | EVEN, no difference beyond the noise |
| host CPU-seconds | 348 | 339 | -2.5% | -24.7 to 7.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.99 | 3.89 | -2.5% | -0.287 to 0.0836 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 13.5 to 19.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
