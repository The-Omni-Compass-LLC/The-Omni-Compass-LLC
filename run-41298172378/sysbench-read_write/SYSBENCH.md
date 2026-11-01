# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 179 | 179 | +0.0% | -16 to 16.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -1.79 to 2 | STEADY, no difference beyond the noise |
| queries a second | 3,952 | 3,954 | +0.1% | -35.8 to 40 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 47.2 | 48.2 | +1.9% | -63 to 64.8 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 177 | 158 | -10.6% | -125 to 87.5 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 10.9 | 10.2 | -7.1% | -7.18 to 5.63 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,252 | +144.6% | 731 to 750 | power given |
| pages holding data, mean (MB) | 463 | 1,023 | +121.0% | 548 to 572 | power given |
| pages read from disk into the pool (misses) | 621,075 | 86,841 | -86.0% | -586,237 to -482,230 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.169 | -9.0% | -0.0181 to -0.0155 | GAIN |
| host CPU-seconds | 330 | 301 | -9.0% | -33.1 to -26.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.05 | 3.69 | -9.0% | -0.698 to -0.0339 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 11.7 |  | 7.87 to 15.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
