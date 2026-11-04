# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.2% | -5.3 to 6.52 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.5% | -4.68 to 7.83 | STEADY, no difference beyond the noise |
| queries a second | 4,693 | 4,719 | +0.5% | -74.9 to 125 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5 | 4.94 | -1.2% | -0.393 to 0.278 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.67 | 7.1 | +6.4% | -0.754 to 1.61 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.26 | 3.16 | -3.0% | -0.221 to 0.0244 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 809 | +532.4% | 114 to 1,249 | power given |
| pages holding data, mean (MB) | 121 | 715 | +491.9% | 171 to 1,017 | power given |
| pages read from disk into the pool (misses) | 600,374 | 150,590 | -74.9% | -555,709 to -343,860 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.245 | -2.4% | -0.0148 to 0.00282 | STEADY, no difference beyond the noise |
| host CPU-seconds | 149 | 146 | -2.4% | -8.7 to 1.57 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.33 | 3.24 | -2.6% | -0.219 to 0.0458 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
