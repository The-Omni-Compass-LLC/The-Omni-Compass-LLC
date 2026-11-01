# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 18.5 | 21.8 | +17.8% | -4.74 to 11.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 986 | 983 | -0.3% | -13.3 to 8.29 | STEADY, no difference beyond the noise |
| queries a second | 986 | 983 | -0.3% | -13.3 to 8.29 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.78 | 1.73 | -3.2% | -0.37 to 0.256 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.91 | 3.86 | -1.2% | -0.253 to 0.157 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.04 | -1.5% | -0.107 to 0.0755 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.3% | 702 to 745 | power given |
| pages holding data, mean (MB) | 458 | 888 | +93.9% | 412 to 448 | power given |
| pages read from disk into the pool (misses) | 188,282 | 71,680 | -61.9% | -135,609 to -97,593 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.218 | -2.9% | -0.0355 to 0.0223 | STEADY, no difference beyond the noise |
| host CPU-seconds | 393 | 382 | -2.9% | -61.7 to 38.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 47.8 | 38.3 | -19.9% | -38.8 to 19.7 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
