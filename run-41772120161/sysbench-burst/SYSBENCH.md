# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 291 | -0.8% | -10.5 to 5.57 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.5% | -9.18 to 6.19 | STEADY, no difference beyond the noise |
| queries a second | 4,724 | 4,701 | -0.5% | -147 to 99.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.25 | 5.37 | +2.4% | -0.365 to 0.619 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.39 | 7.89 | +6.8% | 0.273 to 0.739 | LOSS |
| latency, mean (ms) | 3.32 | 3.25 | -2.0% | -0.19 to 0.0574 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 978 | +664.0% | 443 to 1,256 | power given |
| pages holding data, mean (MB) | 121 | 846 | +598.9% | 434 to 1,015 | power given |
| pages read from disk into the pool (misses) | 606,111 | 111,211 | -81.7% | -508,435 to -481,365 | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.247 | -2.8% | -0.0181 to 0.00362 | STEADY, no difference beyond the noise |
| host CPU-seconds | 151 | 147 | -3.0% | -10.8 to 1.86 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.36 | 3.29 | -2.0% | -0.157 to 0.0209 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
