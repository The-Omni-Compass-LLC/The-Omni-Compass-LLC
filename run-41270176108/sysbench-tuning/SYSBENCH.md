# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,948 | +0.1% | -1.91 to 8.31 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,951 | 2,954 | +0.1% | -3.65 to 9.12 | STEADY, no difference beyond the noise |
| queries a second | 2,951 | 2,954 | +0.1% | -3.65 to 9.12 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.307 | -3.8% | -0.0378 to 0.0138 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.445 | -1.3% | -0.0179 to 0.00659 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.192 | -1.3% | -0.0128 to 0.00786 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -16.9 to 10.3 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,046 | 365,829 | -0.3% | -15,356 to 12,921 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.157 | -0.5% | -0.0103 to 0.0086 | STEADY, no difference beyond the noise |
| host CPU-seconds | 278 | 277 | -0.5% | -18.5 to 15.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.207 | 0.205 | -0.6% | -0.0139 to 0.0112 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
