# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | -0.0% | -6.56 to 6.45 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -5.69 to 5.32 | STEADY, no difference beyond the noise |
| queries a second | 4,700 | 4,697 | -0.1% | -91.1 to 85.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.64 | 3.57 | -1.9% | -0.554 to 0.417 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 35.6 | 5.78 | -83.7% | -159 to 99.4 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.03 | 2.26 | -25.5% | -4.81 to 3.27 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 490 | +282.5% | 172 to 551 | power given |
| pages holding data, mean (MB) | 121 | 442 | +266.7% | 77.2 to 566 | power given |
| pages read from disk into the pool (misses) | 599,656 | 288,306 | -51.9% | -376,330 to -246,370 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.162 | -2.6% | -0.0098 to 0.00116 | STEADY, no difference beyond the noise |
| host CPU-seconds | 102 | 99.2 | -2.6% | -6.12 to 0.878 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.21 | -2.6% | -0.182 to 0.0655 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -1.2 to 4.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
