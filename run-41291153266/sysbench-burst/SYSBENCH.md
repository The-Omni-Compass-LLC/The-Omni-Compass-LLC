# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 289 | -0.5% | -30.8 to 28 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -3.91 to 2.89 | STEADY, no difference beyond the noise |
| queries a second | 4,727 | 4,719 | -0.2% | -62.6 to 46.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.01 | 5.03 | +25.3% | -7.09 to 9.12 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 805 | 36.2 | -95.5% | -4,279 to 2,741 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 25.5 | 3.9 | -84.7% | -125 to 82 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 723 | +465.1% | -129 to 1,320 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 657 | +445.8% | -55.2 to 1,128 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 602,058 | 244,198 | -59.4% | -582,529 to -133,191 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.163 | -2.7% | -0.00812 to -0.000936 | GAIN |
| host CPU-seconds | 100 | 97.6 | -2.7% | -4.77 to -0.667 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.22 | -2.2% | -0.237 to 0.135 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
