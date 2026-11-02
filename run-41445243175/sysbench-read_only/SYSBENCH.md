# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.0% | -3.25 to 3.19 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.0% | -2.9 to 3 | STEADY, no difference beyond the noise |
| queries a second | 4,704 | 4,705 | +0.0% | -46.4 to 48.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.91 | 3.89 | -0.6% | -0.297 to 0.246 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.68 | 5.71 | +0.5% | -0.505 to 0.565 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.7 | 2.67 | -1.2% | -0.0903 to 0.0275 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 613 | +379.2% | 15.6 to 955 | power given |
| pages holding data, mean (MB) | 120 | 553 | +360.9% | 22.5 to 844 | power given |
| pages read from disk into the pool (misses) | 1,978,071 | 531,099 | -73.2% | -1,935,536 to -958,408 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.213 | -1.5% | -0.00477 to -0.00181 | GAIN |
| host CPU-seconds | 392 | 387 | -1.5% | -8.24 to -3.22 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.91 | 2.87 | -1.5% | -0.085 to -0.000323 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
