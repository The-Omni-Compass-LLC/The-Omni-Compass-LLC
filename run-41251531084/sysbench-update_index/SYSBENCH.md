# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 12.8 | 20.8 | +62.9% | 4.53 to 11.5 | GAIN |
| throughput (transactions a second) | 985 | 982 | -0.2% | -4.52 to 0.372 | STEADY, no difference beyond the noise |
| queries a second | 985 | 982 | -0.2% | -4.52 to 0.372 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.2 | 1.74 | -20.9% | -0.599 to -0.321 | GAIN |
| latency, 99th percentile (ms) | 3.86 | 3.59 | -7.0% | -0.443 to -0.0949 | GAIN |
| latency, mean (ms) | 1.13 | 1.03 | -8.4% | -0.168 to -0.022 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,284 | +902.8% | 1,084 to 1,227 | power given |
| pages holding data, mean (MB) | 118 | 873 | +637.3% | 719 to 789 | power given |
| pages read from disk into the pool (misses) | 418,220 | 77,896 | -81.4% | -355,097 to -325,550 | shown, not judged |
| host CPU busy (share of the run) | 0.25 | 0.218 | -13.1% | -0.0602 to -0.00519 | GAIN |
| host CPU-seconds | 439 | 382 | -13.0% | -105 to -9.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 87.7 | 41.2 | -53.0% | -146 to 53.1 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
