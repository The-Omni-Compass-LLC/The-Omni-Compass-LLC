# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,963 | 2,965 | +0.1% | -5.07 to 8.81 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,966 | +0.0% | -5.86 to 8.74 | STEADY, no difference beyond the noise |
| queries a second | 2,964 | 2,966 | +0.0% | -5.86 to 8.74 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.213 | 0.228 | +7.2% | -0.0423 to 0.0729 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.361 | 0.363 | +0.6% | -0.00661 to 0.0106 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.14 | 0.14 | -0.4% | -0.00588 to 0.00464 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 168 | +31.0% | -131 to 210 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 160 | +31.9% | -128 to 205 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,030,077 | 937,868 | -9.0% | -482,591 to 298,173 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.112 | +0.6% | 0.000256 to 0.000984 | power given |
| host CPU-seconds | 197 | 199 | +0.6% | 0.3 to 1.96 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.146 | 0.147 | +0.5% | 0.000197 to 0.0013 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
