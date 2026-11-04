# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.1% | -0.761 to 1.59 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -0.622 to 1.57 | STEADY, no difference beyond the noise |
| queries a second | 4,715 | 4,722 | +0.2% | -9.95 to 25.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.08 | 4.1 | +0.6% | -0.258 to 0.306 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.77 | +1.8% | -0.155 to 0.362 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.07 | 3.09 | +0.6% | -0.0643 to 0.104 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 849 | +65.8% | 129 to 545 | power given |
| pages holding data, mean (MB) | 463 | 755 | +63.1% | 103 to 482 | power given |
| pages read from disk into the pool (misses) | 655,428 | 215,242 | -67.2% | -585,695 to -294,677 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.244 | +1.1% | -0.00365 to 0.00881 | STEADY, no difference beyond the noise |
| host CPU-seconds | 429 | 434 | +1.1% | -6.66 to 15.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.19 | 3.22 | +0.9% | -0.0415 to 0.0987 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
