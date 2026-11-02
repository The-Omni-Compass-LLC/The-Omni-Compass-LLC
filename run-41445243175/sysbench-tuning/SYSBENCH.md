# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,953 | +0.1% | -11.6 to 16.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,956 | +0.1% | -11 to 16.4 | STEADY, no difference beyond the noise |
| queries a second | 2,953 | 2,956 | +0.1% | -11 to 16.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.311 | 0.305 | -1.8% | -0.0342 to 0.0229 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.407 | 0.412 | +1.1% | -0.00537 to 0.0147 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.184 | -2.7% | -0.0196 to 0.00947 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 408 | +219.0% | 98.4 to 462 | power given |
| pages holding data, mean (MB) | 121 | 385 | +217.5% | 104 to 423 | power given |
| pages read from disk into the pool (misses) | 1,029,452 | 489,446 | -52.5% | -807,100 to -272,912 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.148 | -2.1% | -0.0143 to 0.00792 | STEADY, no difference beyond the noise |
| host CPU-seconds | 267 | 262 | -2.1% | -25 to 14 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.198 | 0.194 | -2.1% | -0.0195 to 0.011 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
