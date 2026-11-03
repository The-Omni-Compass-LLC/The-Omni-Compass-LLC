# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.4% | -2.64 to 5.02 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.4% | -2.58 to 4.69 | STEADY, no difference beyond the noise |
| queries a second | 4,718 | 4,735 | +0.4% | -41.3 to 75 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.3 | 4.15 | -3.6% | -0.347 to 0.0408 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.28 | 6.06 | -3.5% | -0.227 to -0.216 | GAIN |
| latency, mean (ms) | 3.15 | 3.04 | -3.3% | -0.272 to 0.0648 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 860 | +68.0% | 239 to 458 | power given |
| pages holding data, mean (MB) | 463 | 760 | +63.9% | 207 to 386 | power given |
| pages read from disk into the pool (misses) | 656,189 | 201,840 | -69.2% | -534,828 to -373,871 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.24 | -2.5% | -0.0206 to 0.00852 | STEADY, no difference beyond the noise |
| host CPU-seconds | 437 | 426 | -2.4% | -36.3 to 15 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.25 | 3.15 | -2.8% | -0.261 to 0.0776 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
