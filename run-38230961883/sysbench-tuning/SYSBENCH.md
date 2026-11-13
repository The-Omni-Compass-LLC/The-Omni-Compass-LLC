# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,925 | 2,925 | -0.0% | -8.31 to 7.58 | no difference beyond the noise |
| throughput (transactions a second) | 2,933 | 2,933 | -0.0% | -10.8 to 9.28 | no difference beyond the noise |
| queries a second | 2,933 | 2,933 | -0.0% | -10.8 to 9.28 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.379 | 0.365 | -3.5% | -0.032 to 0.00531 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.485 | 0.47 | -3.1% | -0.0615 to 0.0315 | no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.205 | -3.3% | -0.0219 to 0.00781 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 481 | -6.0% | -115 to 53.6 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 434 | -6.1% | -73.1 to 17.2 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,315 | 282,414 | +7.7% | -66,169 to 106,367 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.105 | -5.5% | -0.0204 to 0.00805 | no difference beyond the noise |
| host CPU-seconds | 124 | 117 | -5.6% | -22.8 to 9.03 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.138 | 0.13 | -5.5% | -0.0253 to 0.00998 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 3.6 to 15.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
