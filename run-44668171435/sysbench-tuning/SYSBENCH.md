# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,960 | 2,961 | +0.0% | -9.69 to 12.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,968 | 2,968 | -0.0% | -11.4 to 11.2 | STEADY, no difference beyond the noise |
| queries a second | 2,968 | 2,968 | -0.0% | -11.4 to 11.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.21 | 0.197 | -6.3% | -0.0283 to 0.00164 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.352 | 0.344 | -2.3% | -0.0308 to 0.0148 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.191 | +5.9% | -0.0736 to 0.095 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,127 | +120.2% | 511 to 719 | power given |
| pages holding data, mean (MB) | 466 | 915 | +96.2% | 441 to 456 | power given |
| pages read from disk into the pool (misses) | 368,497 | 78,326 | -78.7% | -301,518 to -278,824 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.109 | -2.4% | -0.00306 to -0.00233 | GAIN |
| host CPU-seconds | 198 | 193 | -2.4% | -5.28 to -4.22 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.143 | -2.5% | -0.00431 to -0.00289 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 0.495 to 10.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 5.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
