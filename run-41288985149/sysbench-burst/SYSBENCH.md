# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.1% | -4.17 to 4.55 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -4.7 to 4.3 | STEADY, no difference beyond the noise |
| queries a second | 4,710 | 4,707 | -0.1% | -75.2 to 68.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5 | 4.77 | -4.7% | -0.358 to -0.109 | GAIN |
| latency, 99th percentile (ms) | 7.17 | 6.79 | -5.2% | -0.668 to -0.0832 | GAIN |
| latency, mean (ms) | 3.17 | 3.12 | -1.4% | -0.0602 to -0.0296 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 712 | +39.1% | 198 to 202 | power given |
| pages holding data, mean (MB) | 452 | 642 | +42.2% | 189 to 192 | power given |
| pages read from disk into the pool (misses) | 243,921 | 182,422 | -25.2% | -64,633 to -58,365 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.243 | +0.0% | -0.00627 to 0.00652 | STEADY, no difference beyond the noise |
| host CPU-seconds | 145 | 145 | +0.0% | -3.64 to 3.77 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.22 | 3.22 | -0.0% | -0.0376 to 0.0366 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
