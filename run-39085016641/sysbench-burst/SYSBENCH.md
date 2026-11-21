# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.3% | -3.15 to 5.12 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.3% | -3.34 to 5.26 | EVEN, no difference beyond the noise |
| queries a second | 4,694 | 4,710 | +0.3% | -53.4 to 84.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.41 | 5.41 | +0.0% | -0.241 to 0.241 | EVEN, the same |
| latency, 99th percentile (ms) | 7.34 | 7.34 | -0.0% | -0.328 to 0.326 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.44 | 3.44 | -0.1% | -0.103 to 0.0992 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 146 | +14.1% | -1.14 to 37.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 141 | +17.2% | 6.49 to 34.9 | power given |
| pages read from disk into the pool (misses) | 580,471 | 528,125 | -9.0% | -178,365 to 73,673 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.207 | +1.3% | -0.0101 to 0.0154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 115 | +1.4% | -5.74 to 8.88 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.53 | 2.55 | +1.0% | -0.132 to 0.181 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
