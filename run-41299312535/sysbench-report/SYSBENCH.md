# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.2% | -5.53 to 6.72 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.2% | -5.69 to 7.14 | STEADY, no difference beyond the noise |
| queries a second | 4,699 | 4,711 | +0.2% | -91.1 to 114 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.29 | 5.38 | +1.6% | -0.516 to 0.688 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.76 | 7.9 | +1.8% | -0.191 to 0.464 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.19 | 3.22 | +0.9% | -0.0888 to 0.145 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 880 | +71.9% | 71.4 to 665 | power given |
| pages holding data, mean (MB) | 456 | 794 | +74.1% | 97.4 to 578 | power given |
| pages read from disk into the pool (misses) | 248,302 | 137,227 | -44.7% | -190,253 to -31,897 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.245 | +0.8% | -0.0149 to 0.0187 | STEADY, no difference beyond the noise |
| host CPU-seconds | 145 | 146 | +0.8% | -8.66 to 10.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.24 | 3.26 | +0.6% | -0.137 to 0.174 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 295 | -0.4% | -5.01 to 2.65 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.3% | -4.26 to 2.27 | STEADY, no difference beyond the noise |
| queries a second | 4,744 | 4,729 | -0.3% | -68.1 to 36.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.66 | 2.69 | +1.2% | -0.108 to 0.173 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.89 | 4 | +3.1% | -0.29 to 0.528 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.07 | 2.15 | +3.7% | -0.135 to 0.289 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 577 | +12.7% | -214 to 344 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 518 | +12.1% | -204 to 316 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,379 | 548,027 | -16.4% | -558,445 to 343,741 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.164 | +0.4% | -0.00271 to 0.004 | STEADY, no difference beyond the noise |
| host CPU-seconds | 294 | 295 | +0.4% | -4.65 to 7.08 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.18 | 2.19 | +0.8% | -0.0548 to 0.0903 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 195 | +1.9% | 0.892 to 6.57 | GAIN |
| throughput (transactions a second) | 197 | 196 | -0.3% | -3.69 to 2.37 | STEADY, no difference beyond the noise |
| queries a second | 3,931 | 3,918 | -0.3% | -73.7 to 47.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.69 | 6.79 | -21.8% | -2.29 to -1.5 | GAIN |
| latency, 99th percentile (ms) | 13 | 8.69 | -33.1% | -4.93 to -3.65 | GAIN |
| latency, mean (ms) | 5.2 | 4.86 | -6.6% | -0.483 to -0.202 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,025 | +100.2% | 407 to 619 | power given |
| pages holding data, mean (MB) | 462 | 914 | +97.6% | 358 to 545 | power given |
| pages read from disk into the pool (misses) | 617,344 | 122,531 | -80.2% | -579,246 to -410,381 | shown, not judged |
| host CPU busy (share of the run) | 0.277 | 0.259 | -6.2% | -0.0234 to -0.0108 | GAIN |
| host CPU-seconds | 486 | 456 | -6.2% | -40.5 to -19.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.54 | 5.09 | -8.0% | -0.594 to -0.294 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,938 | 2,941 | +0.1% | -38.9 to 43.5 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,965 | -0.0% | -21.2 to 19.7 | STEADY, no difference beyond the noise |
| queries a second | 2,966 | 2,965 | -0.0% | -21.2 to 19.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.286 | -13.8% | -0.131 to 0.0397 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.581 | 1.38 | +137.9% | -3.39 to 4.99 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.552 | 0.7 | +26.8% | -1.67 to 1.97 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,205 | +135.4% | 683 to 704 | power given |
| pages holding data, mean (MB) | 464 | 922 | +98.8% | 446 to 470 | power given |
| pages read from disk into the pool (misses) | 368,156 | 76,708 | -79.2% | -300,652 to -282,243 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.127 | -7.9% | -0.0265 to 0.0047 | STEADY, no difference beyond the noise |
| host CPU-seconds | 244 | 225 | -7.8% | -46.9 to 8.62 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.182 | 0.168 | -7.9% | -0.0356 to 0.00693 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 8.9 to 11.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 3.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 257 | 298 | +16.0% | -2.99 to 85.5 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 990 | 988 | -0.1% | -6.38 to 3.87 | STEADY, no difference beyond the noise |
| queries a second | 990 | 988 | -0.1% | -6.38 to 3.87 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 26.2 | 25.7 | -1.7% | -42.7 to 41.8 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 130 | 100 | -22.9% | -174 to 114 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 6.1 | 5.21 | -14.5% | -7.42 to 5.65 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,237 | +141.7% | 706 to 745 | power given |
| pages holding data, mean (MB) | 456 | 892 | +95.5% | 406 to 465 | power given |
| pages read from disk into the pool (misses) | 191,598 | 71,737 | -62.6% | -129,713 to -110,008 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.135 | -3.6% | -0.0248 to 0.0148 | STEADY, no difference beyond the noise |
| host CPU-seconds | 245 | 236 | -3.6% | -42.6 to 25 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.19 | 1.8 | -17.9% | -1.09 to 0.303 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
