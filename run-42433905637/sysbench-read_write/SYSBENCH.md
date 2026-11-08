# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 174 | 167 | -4.1% | -20.2 to 6.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.31 to 2.9 | STEADY, no difference beyond the noise |
| queries a second | 3,943 | 3,949 | +0.1% | -46.1 to 58 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 45.2 | 86.7 | +91.6% | 7.27 to 75.6 | LOSS |
| latency, 99th percentile (ms) | 146 | 245 | +68.0% | 54.6 to 144 | LOSS |
| latency, mean (ms) | 10.2 | 16.6 | +62.2% | 2.77 to 9.94 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,256 | +145.3% | 705 to 783 | power given |
| pages holding data, mean (MB) | 463 | 1,027 | +121.6% | 544 to 583 | power given |
| pages read from disk into the pool (misses) | 617,848 | 83,314 | -86.5% | -571,698 to -497,372 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.168 | -9.4% | -0.0202 to -0.0147 | GAIN |
| host CPU-seconds | 329 | 298 | -9.3% | -35.5 to -25.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.15 | 3.92 | -5.6% | -0.509 to 0.0441 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 6.08 to 18.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 10.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
