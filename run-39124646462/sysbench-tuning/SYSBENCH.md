# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,936 | 2,936 | -0.0% | -13.7 to 13.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,952 | -0.0% | -13.7 to 12.9 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,952 | -0.0% | -13.7 to 12.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.374 | 0.372 | -0.6% | -0.0124 to 0.00771 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.553 | 0.549 | -0.6% | -0.032 to 0.0254 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.225 | -1.3% | -0.00985 to 0.00401 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +8.2% | -1.64 to 22.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 133 | +10.0% | 0.907 to 23.3 | power given |
| pages read from disk into the pool (misses) | 1,029,474 | 997,579 | -3.1% | -78,108 to 14,318 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.118 | -1.1% | -0.00397 to 0.00135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 197 | -1.1% | -6.67 to 2.24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.147 | -1.1% | -0.00501 to 0.00172 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 0.929 to 12.4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
