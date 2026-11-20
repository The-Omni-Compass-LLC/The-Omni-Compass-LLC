# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.5% | -2.11 to 4.81 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.5% | -2.36 to 5.13 | STEADY, no difference beyond the noise |
| queries a second | 4,694 | 4,716 | +0.5% | -37.7 to 82 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.23 | 4.18 | -1.2% | -0.161 to 0.0587 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.99 | 5.85 | -2.4% | -0.307 to 0.0206 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.7 | 2.67 | -1.2% | -0.097 to 0.0348 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 678 | +32.5% | 22.5 to 310 | power given |
| pages holding data, mean (MB) | 452 | 611 | +35.3% | 22.6 to 296 | power given |
| pages read from disk into the pool (misses) | 244,134 | 192,120 | -21.3% | -93,977 to -10,051 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.221 | +0.2% | -0.00663 to 0.00772 | STEADY, no difference beyond the noise |
| host CPU-seconds | 132 | 132 | +0.1% | -4.13 to 4.47 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.94 | 2.94 | -0.2% | -0.0672 to 0.0539 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
