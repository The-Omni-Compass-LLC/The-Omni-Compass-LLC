# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 131 | 175 | +34.1% | 32.6 to 56.6 | GAIN |
| throughput (transactions a second) | 981 | 980 | -0.1% | -4.52 to 2.47 | STEADY, no difference beyond the noise |
| queries a second | 981 | 980 | -0.1% | -4.52 to 2.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.31 | 1.16 | -11.9% | -0.286 to -0.0271 | GAIN |
| latency, 99th percentile (ms) | 1.95 | 1.78 | -8.7% | -0.612 to 0.274 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.839 | 0.82 | -2.2% | -0.0672 to 0.0303 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,300 | +915.3% | 1,170 to 1,173 | power given |
| pages holding data, mean (MB) | 118 | 879 | +648.4% | 754 to 770 | power given |
| pages read from disk into the pool (misses) | 415,691 | 70,906 | -82.9% | -360,391 to -329,179 | shown, not judged |
| host CPU busy (share of the run) | 0.219 | 0.199 | -9.1% | -0.0375 to -0.00245 | GAIN |
| host CPU-seconds | 400 | 363 | -9.1% | -68.5 to -4.29 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.77 | 4.54 | -32.9% | -4.23 to -0.225 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
