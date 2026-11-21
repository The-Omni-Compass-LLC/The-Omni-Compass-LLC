# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 195 | +0.4% | 0.369 to 1.25 | GAIN |
| throughput (transactions a second) | 196 | 196 | +0.4% | 0.134 to 1.49 | GAIN |
| queries a second | 3,911 | 3,928 | +0.4% | 2.68 to 29.8 | GAIN |
| latency, 95th percentile (ms) | 7.7 | 7.7 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 10.3 | 10.3 | +0.0% | -0.462 to 0.462 | EVEN, the same |
| latency, mean (ms) | 4.26 | 4.27 | +0.3% | -0.0168 to 0.0386 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.6% | 7.53 to 14.4 | power given |
| pages holding data, mean (MB) | 121 | 131 | +8.3% | 6.65 to 13.4 | power given |
| pages read from disk into the pool (misses) | 1,659,948 | 1,614,504 | -2.7% | -126,737 to 35,848 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.228 | +0.2% | -0.00174 to 0.00278 | EVEN, no difference beyond the noise |
| host CPU-seconds | 409 | 410 | +0.2% | -3.06 to 4.73 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.59 | 4.58 | -0.2% | -0.0489 to 0.0315 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 5.8 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
