# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.4% | -4.95 to 2.32 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.5% | -5.08 to 2.02 | STEADY, no difference beyond the noise |
| queries a second | 4,705 | 4,681 | -0.5% | -81.3 to 32.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.03 | 5 | -0.6% | -0.164 to 0.102 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.22 | 7.05 | -2.3% | -0.322 to -0.0152 | GAIN |
| latency, mean (ms) | 3.19 | 3.17 | -0.8% | -0.0978 to 0.0451 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 846 | +65.3% | 183 to 486 | power given |
| pages holding data, mean (MB) | 455 | 766 | +68.4% | 183 to 439 | power given |
| pages read from disk into the pool (misses) | 248,050 | 143,221 | -42.3% | -149,144 to -60,515 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.245 | -0.5% | -0.00829 to 0.00585 | STEADY, no difference beyond the noise |
| host CPU-seconds | 146 | 146 | -0.5% | -5.09 to 3.71 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.27 | 3.27 | -0.0% | -0.0573 to 0.0549 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
