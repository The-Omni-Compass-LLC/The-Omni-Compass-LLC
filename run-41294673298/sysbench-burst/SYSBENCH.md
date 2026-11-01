# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -2.79 to 0.972 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.4% | -3.01 to 0.806 | STEADY, no difference beyond the noise |
| queries a second | 4,730 | 4,712 | -0.4% | -48.1 to 12.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.33 | 2.29 | -1.9% | -0.324 to 0.237 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.77 | 3.73 | -1.2% | -0.588 to 0.494 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.15 | -1.1% | -0.0552 to 0.0291 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 447 | 447 | +0.1% | -3.5 to 4.33 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,931 | 246,757 | +1.2% | -4,471 to 10,124 | shown, not judged |
| host CPU busy (share of the run) | 0.0894 | 0.0893 | -0.1% | -0.0034 to 0.0032 | STEADY, no difference beyond the noise |
| host CPU-seconds | 53.7 | 53.6 | -0.2% | -2.05 to 1.87 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.19 | 1.2 | +0.2% | -0.0384 to 0.0426 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
