# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 291 | -0.7% | -7.25 to 2.88 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.5% | -7.22 to 4.41 | STEADY, no difference beyond the noise |
| queries a second | 4,712 | 4,689 | -0.5% | -116 to 70.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.1 | 5.25 | +3.0% | -0.186 to 0.489 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.13 | 7.57 | +6.1% | 0.31 to 0.567 | LOSS |
| latency, mean (ms) | 3.25 | 3.29 | +1.3% | -0.384 to 0.468 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 908 | +609.7% | 277 to 1,283 | power given |
| pages holding data, mean (MB) | 121 | 774 | +539.6% | 139 to 1,166 | power given |
| pages read from disk into the pool (misses) | 605,970 | 132,857 | -78.1% | -528,918 to -417,310 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.249 | +0.1% | -0.0282 to 0.0286 | STEADY, no difference beyond the noise |
| host CPU-seconds | 148 | 148 | +0.0% | -16.6 to 16.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.29 | 3.31 | +0.7% | -0.383 to 0.432 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
