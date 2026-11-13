# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,943 | 2,945 | +0.0% | -5.1 to 7.67 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,954 | +0.0% | -4.81 to 4.99 | EVEN, no difference beyond the noise |
| queries a second | 2,954 | 2,954 | +0.0% | -4.81 to 4.99 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.324 | +1.9% | -0.00891 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.517 | 0.508 | -1.8% | -0.0329 to 0.0143 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.2 | +0.6% | -0.00419 to 0.00643 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 456 | -10.9% | -120 to 8.83 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 418 | -10.0% | -110 to 17.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,788 | 433,294 | +17.8% | -46,768 to 177,779 | shown, not judged |
| host CPU busy (share of the run) | 0.0955 | 0.0969 | +1.5% | -0.00632 to 0.00913 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 161 | +1.6% | -10.4 to 15.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.118 | 0.119 | +1.5% | -0.00787 to 0.0115 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 4.87 to 12.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
