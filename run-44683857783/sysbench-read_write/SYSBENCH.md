# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 182 | 196 | +7.6% | 11.9 to 16 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.5% | 0.518 to 1.42 | GAIN |
| queries a second | 3,927 | 3,947 | +0.5% | 10.4 to 28.3 | GAIN |
| latency, 95th percentile (ms) | 11.9 | 6.96 | -41.7% | -5.72 to -4.24 | GAIN |
| latency, 99th percentile (ms) | 16.7 | 9.4 | -43.7% | -9.56 to -5.06 | GAIN |
| latency, mean (ms) | 5.98 | 4.88 | -18.5% | -1.65 to -0.556 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,020 | +697.1% | 807 to 977 | power given |
| pages holding data, mean (MB) | 118 | 925 | +680.5% | 741 to 871 | power given |
| pages read from disk into the pool (misses) | 1,665,006 | 169,638 | -89.8% | -1,610,706 to -1,380,030 | shown, not judged |
| host CPU busy (share of the run) | 0.318 | 0.274 | -14.0% | -0.0649 to -0.0239 | GAIN |
| host CPU-seconds | 559 | 481 | -14.0% | -114 to -42.1 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.69 | 5.35 | -20.1% | -1.83 to -0.856 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
