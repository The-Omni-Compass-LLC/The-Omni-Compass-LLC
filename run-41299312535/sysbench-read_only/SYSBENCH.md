# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 295 | -0.4% | -5.01 to 2.65 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.3% | -4.26 to 2.27 | STEADY, no difference beyond the noise |
| queries a second | 4,744 | 4,729 | -0.3% | -68.1 to 36.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.66 | 2.69 | +1.2% | -0.108 to 0.173 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.89 | 4 | +3.1% | -0.29 to 0.528 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.07 | 2.15 | +3.7% | -0.135 to 0.289 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 577 | +12.7% | -214 to 344 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 518 | +12.1% | -204 to 316 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,379 | 548,027 | -16.4% | -558,445 to 343,741 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.164 | +0.4% | -0.00271 to 0.004 | STEADY, no difference beyond the noise |
| host CPU-seconds | 294 | 295 | +0.4% | -4.65 to 7.08 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.18 | 2.19 | +0.8% | -0.0548 to 0.0903 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
