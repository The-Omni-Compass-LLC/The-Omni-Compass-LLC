# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,924 | 2,925 | +0.0% | -6.63 to 7.95 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,933 | 2,934 | +0.0% | -9.39 to 9.91 | EVEN, no difference beyond the noise |
| queries a second | 2,933 | 2,934 | +0.0% | -9.39 to 9.91 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.231 | -8.7% | -0.0525 to 0.00853 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.459 | 0.451 | -1.7% | -0.008 to -0.008 | GAIN |
| latency, mean (ms) | 0.185 | 0.146 | -21.2% | -0.184 to 0.106 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 441 | -13.8% | -142 to 1.14 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 404 | -12.8% | -123 to 4.38 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,250 | 447,736 | +21.9% | -17,058 to 178,030 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.111 | -0.9% | -0.00491 to 0.00287 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 201 | -0.9% | -9.3 to 5.46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.151 | 0.15 | -1.0% | -0.00693 to 0.00404 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 5.08 to 17.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
