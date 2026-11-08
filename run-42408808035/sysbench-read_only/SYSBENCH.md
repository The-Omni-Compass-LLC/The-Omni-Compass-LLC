# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.6% | -4.56 to 8.14 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.2% | -1.92 to 3.1 | STEADY, no difference beyond the noise |
| queries a second | 4,742 | 4,751 | +0.2% | -30.8 to 49.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.73 | 2.55 | -6.4% | -0.361 to 0.0114 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 17.2 | 6.42 | -62.7% | -54.5 to 33 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.69 | 2.44 | -9.3% | -1.14 to 0.646 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,183 | +131.1% | 587 to 755 | power given |
| pages holding data, mean (MB) | 464 | 957 | +106.4% | 482 to 505 | power given |
| pages read from disk into the pool (misses) | 653,826 | 85,954 | -86.9% | -591,632 to -544,112 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.155 | -3.2% | -0.00974 to -0.000436 | GAIN |
| host CPU-seconds | 286 | 277 | -3.2% | -17.3 to -0.975 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.15 | 2.07 | -3.8% | -0.108 to -0.0535 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 7.7 to 16.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
