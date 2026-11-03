# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,953 | 2,955 | +0.1% | -5.12 to 10 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,965 | +0.0% | -5.44 to 5.52 | STEADY, no difference beyond the noise |
| queries a second | 2,965 | 2,965 | +0.0% | -5.44 to 5.52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.25 | 0.23 | -8.0% | -0.0462 to 0.00617 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.367 | 0.365 | -0.6% | -0.0203 to 0.0156 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.345 | 0.239 | -30.8% | -0.23 to 0.0167 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,145 | +794.3% | 967 to 1,066 | power given |
| pages holding data, mean (MB) | 121 | 911 | +651.4% | 766 to 813 | power given |
| pages read from disk into the pool (misses) | 1,029,903 | 86,724 | -91.6% | -968,451 to -917,907 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.112 | -5.2% | -0.0185 to 0.00618 | STEADY, no difference beyond the noise |
| host CPU-seconds | 210 | 199 | -5.2% | -32.7 to 11 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.148 | -5.3% | -0.0241 to 0.00769 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 1.43 to 14.6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
