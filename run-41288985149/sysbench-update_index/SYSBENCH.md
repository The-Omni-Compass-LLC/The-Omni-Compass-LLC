# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 277 | 288 | +4.1% | -135 to 157 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 989 | 989 | +0.1% | -5.63 to 7.5 | STEADY, no difference beyond the noise |
| queries a second | 989 | 989 | +0.1% | -5.63 to 7.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.34 | 3.28 | -1.8% | -2.26 to 2.14 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.89 | 9.06 | +1.9% | -10.3 to 10.6 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.13 | -5.9% | -0.781 to 0.638 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 705 to 743 | power given |
| pages holding data, mean (MB) | 455 | 887 | +95.1% | 399 to 465 | power given |
| pages read from disk into the pool (misses) | 191,953 | 71,337 | -62.8% | -128,197 to -113,035 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.108 | -2.7% | -0.0233 to 0.0173 | STEADY, no difference beyond the noise |
| host CPU-seconds | 195 | 189 | -2.7% | -40.6 to 30.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.62 | 1.47 | -9.7% | -1.46 to 1.15 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
