# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.1% | -3.74 to 4.16 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 297 | +0.0% | -3.95 to 4.22 | STEADY, no difference beyond the noise |
| queries a second | 4,745 | 4,748 | +0.0% | -63.2 to 67.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.82 | 1.78 | -2.4% | -0.139 to 0.0507 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.68 | 3.55 | -3.5% | -0.553 to 0.298 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.25 | 1.23 | -1.1% | -0.0978 to 0.0713 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 462 | 458 | -0.7% | -16.4 to 9.86 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 658,716 | 656,912 | -0.3% | -11,464 to 7,856 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.1 | -0.2% | -0.00728 to 0.0069 | STEADY, no difference beyond the noise |
| host CPU-seconds | 181 | 180 | -0.2% | -13 to 12.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.34 | 1.33 | -0.2% | -0.0838 to 0.0774 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
