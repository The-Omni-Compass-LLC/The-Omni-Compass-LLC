# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 295 | -0.2% | -7.11 to 5.89 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.2% | -6.18 to 5.22 | STEADY, no difference beyond the noise |
| queries a second | 4,746 | 4,738 | -0.2% | -98.8 to 83.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.63 | 2.54 | -3.5% | -0.0948 to -0.0919 | GAIN |
| latency, 99th percentile (ms) | 4.1 | 4.11 | +0.2% | -0.653 to 0.668 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.17 | 2.11 | -2.9% | -0.431 to 0.306 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,035 | +708.3% | 714 to 1,099 | power given |
| pages holding data, mean (MB) | 120 | 877 | +629.1% | 578 to 936 | power given |
| pages read from disk into the pool (misses) | 2,025,066 | 376,625 | -81.4% | -2,468,452 to -828,431 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.153 | -5.6% | -0.0158 to -0.00241 | GAIN |
| host CPU-seconds | 291 | 275 | -5.5% | -27.9 to -4.39 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.04 | -5.4% | -0.162 to -0.0701 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 9.67 |  | 3.93 to 15.4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
