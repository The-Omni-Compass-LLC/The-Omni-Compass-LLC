# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.1% | -4.09 to 4.48 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.1% | -4.23 to 4.62 | EVEN, no difference beyond the noise |
| queries a second | 4,676 | 4,679 | +0.1% | -67.7 to 73.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.74 | 2.63 | -4.1% | -0.294 to 0.069 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.41 | 4.15 | -5.8% | -0.551 to 0.038 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.07 | 2.01 | -3.2% | -0.235 to 0.103 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 412 | -19.5% | -251 to 51.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 375 | -18.8% | -206 to 33.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,056 | 908,265 | +38.7% | -143,687 to 650,105 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.157 | -1.7% | -0.00975 to 0.00446 | EVEN, no difference beyond the noise |
| host CPU-seconds | 292 | 287 | -1.7% | -17.8 to 8.02 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.13 | -1.7% | -0.164 to 0.0893 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 8.93 to 20.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
