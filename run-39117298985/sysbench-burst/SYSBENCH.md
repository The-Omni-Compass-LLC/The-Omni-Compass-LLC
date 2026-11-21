# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.2% | -4.08 to 2.71 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.2% | -4.37 to 2.99 | EVEN, no difference beyond the noise |
| queries a second | 4,706 | 4,695 | -0.2% | -69.9 to 47.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.06 | 5.03 | -0.6% | -0.291 to 0.231 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.67 | 6.71 | +0.6% | -0.133 to 0.214 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 3.29 | -0.7% | -0.052 to 0.00723 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.3% | -0.974 to 19.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 132 | +9.8% | 4.63 to 18.8 | power given |
| pages read from disk into the pool (misses) | 580,063 | 542,938 | -6.4% | -118,034 to 43,784 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.194 | -1.1% | -0.00517 to 0.000836 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 107 | -1.2% | -2.72 to 0.164 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.42 | 2.39 | -1.0% | -0.0458 to -0.000166 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
