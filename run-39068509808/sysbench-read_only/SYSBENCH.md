# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 296 | +0.4% | -0.366 to 2.66 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.4% | -0.373 to 2.79 | EVEN, no difference beyond the noise |
| queries a second | 4,714 | 4,733 | +0.4% | -5.97 to 44.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.03 | 3.98 | -1.2% | -0.151 to 0.0553 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.37 | 5.28 | -1.8% | -0.096 to -0.096 | GAIN |
| latency, mean (ms) | 3.17 | 3.15 | -0.6% | -0.0554 to 0.015 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -36.4 to 25.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 452 | -2.1% | -18.8 to -0.636 | GAIN |
| pages read from disk into the pool (misses) | 653,146 | 655,666 | +0.4% | -62,478 to 67,519 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.189 | +0.2% | -0.00539 to 0.00599 | EVEN, no difference beyond the noise |
| host CPU-seconds | 312 | 313 | +0.2% | -9.84 to 11.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.31 | -0.2% | -0.0841 to 0.0763 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 9.55 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
