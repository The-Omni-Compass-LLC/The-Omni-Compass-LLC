# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 297 | +0.6% | -3.2 to 6.85 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 297 | +0.6% | -3.19 to 6.78 | STEADY, no difference beyond the noise |
| queries a second | 4,722 | 4,751 | +0.6% | -51.1 to 109 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.98 | 3.96 | -0.6% | -0.127 to 0.0793 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.47 | 5.37 | -1.8% | -0.103 to -0.0925 | GAIN |
| latency, mean (ms) | 3.05 | 3.03 | -0.7% | -0.1 to 0.0587 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 642 | +25.4% | -220 to 481 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 576 | +24.5% | -199 to 426 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,782 | 454,211 | -30.6% | -700,914 to 299,772 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.242 | +0.2% | -0.00829 to 0.00939 | STEADY, no difference beyond the noise |
| host CPU-seconds | 429 | 429 | +0.2% | -14.6 to 16.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.18 | 3.16 | -0.4% | -0.0893 to 0.064 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | -1.48 to 3.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
