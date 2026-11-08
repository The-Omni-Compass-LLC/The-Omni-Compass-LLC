# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 181 | 196 | +8.6% | 14.4 to 16.5 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.3% | 0.633 to 0.637 | GAIN |
| queries a second | 3,921 | 3,934 | +0.3% | 12.7 to 12.7 | GAIN |
| latency, 95th percentile (ms) | 12.3 | 6.96 | -43.4% | -5.71 to -4.97 | GAIN |
| latency, 99th percentile (ms) | 17.4 | 9.01 | -48.3% | -10.8 to -6 | GAIN |
| latency, mean (ms) | 6.3 | 4.96 | -21.4% | -2.54 to -0.152 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,054 | +723.7% | 796 to 1,057 | power given |
| pages holding data, mean (MB) | 118 | 942 | +695.3% | 711 to 936 | power given |
| pages read from disk into the pool (misses) | 1,663,345 | 131,214 | -92.1% | -1,719,309 to -1,344,953 | shown, not judged |
| host CPU busy (share of the run) | 0.313 | 0.267 | -14.8% | -0.0579 to -0.0348 | GAIN |
| host CPU-seconds | 551 | 469 | -14.9% | -103 to -61 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.66 | 5.22 | -21.6% | -1.67 to -1.21 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 5.23 to 8.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
