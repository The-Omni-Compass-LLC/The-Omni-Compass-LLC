# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -5 to 3.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.3% | -4.86 to 2.95 | EVEN, no difference beyond the noise |
| queries a second | 4,734 | 4,719 | -0.3% | -77.8 to 47.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.33 | 4.3 | -0.6% | -0.32 to 0.268 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.32 | 6.28 | -0.6% | -0.2 to 0.124 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.29 | 3.25 | -1.2% | -0.138 to 0.0583 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.5% | 4.82 to 11.7 | power given |
| pages holding data, mean (MB) | 120 | 135 | +12.2% | 10.5 to 18.9 | power given |
| pages read from disk into the pool (misses) | 1,996,380 | 1,919,358 | -3.9% | -170,145 to 16,102 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.199 | -2.0% | -0.0146 to 0.00656 | EVEN, no difference beyond the noise |
| host CPU-seconds | 338 | 331 | -2.0% | -24.6 to 11 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.5 | 2.46 | -1.7% | -0.143 to 0.0573 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
