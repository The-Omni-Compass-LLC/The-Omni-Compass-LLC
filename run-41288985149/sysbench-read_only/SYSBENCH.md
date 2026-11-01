# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 294 | +0.6% | -0.557 to 4.21 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.1% | -1.83 to 1.14 | STEADY, no difference beyond the noise |
| queries a second | 4,744 | 4,739 | -0.1% | -29.3 to 18.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.84 | 2.57 | -9.7% | -0.4 to -0.15 | GAIN |
| latency, 99th percentile (ms) | 24.5 | 5.73 | -76.6% | -40.3 to 2.73 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.1 | 2.38 | -23.1% | -1.39 to -0.0462 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,197 | +133.8% | 518 to 852 | power given |
| pages holding data, mean (MB) | 465 | 967 | +108.1% | 469 to 535 | power given |
| pages read from disk into the pool (misses) | 657,109 | 82,363 | -87.5% | -589,358 to -560,136 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.158 | -5.4% | -0.0119 to -0.0063 | GAIN |
| host CPU-seconds | 300 | 283 | -5.4% | -21.6 to -11 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.25 | 2.12 | -6.0% | -0.163 to -0.108 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 2.39 to 19.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
