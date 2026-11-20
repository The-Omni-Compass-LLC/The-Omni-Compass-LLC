# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 144 | 143 | -0.7% | -32.3 to 30.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.4% | -2.83 to 1.3 | STEADY, no difference beyond the noise |
| queries a second | 3,957 | 3,942 | -0.4% | -56.5 to 25.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 177 | 154 | -12.8% | -215 to 170 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 501 | 336 | -32.9% | -922 to 592 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 35.7 | 29.2 | -18.0% | -47.5 to 34.6 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,266 | +147.4% | 729 to 780 | power given |
| pages holding data, mean (MB) | 466 | 1,028 | +120.4% | 549 to 574 | power given |
| pages read from disk into the pool (misses) | 617,450 | 84,584 | -86.3% | -576,415 to -489,317 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.173 | -10.0% | -0.0374 to -0.00115 | GAIN |
| host CPU-seconds | 343 | 308 | -10.0% | -68.4 to 0.104 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.25 | 4.77 | -9.1% | -1.81 to 0.847 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 5.5 to 15.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
