# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.2% | -4.28 to 5.42 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -4.56 to 5.17 | STEADY, no difference beyond the noise |
| queries a second | 4,707 | 4,712 | +0.1% | -72.9 to 82.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.83 | 4.85 | +0.5% | -0.426 to 0.475 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.09 | 6.83 | -3.6% | -1.12 to 0.606 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.11 | 3.1 | -0.3% | -0.106 to 0.0849 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 813 | +58.8% | 45.1 to 557 | power given |
| pages holding data, mean (MB) | 455 | 735 | +61.6% | 57.2 to 503 | power given |
| pages read from disk into the pool (misses) | 248,431 | 152,927 | -38.4% | -163,072 to -27,934 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.247 | -0.0% | -0.00579 to 0.00555 | STEADY, no difference beyond the noise |
| host CPU-seconds | 147 | 147 | -0.2% | -3.59 to 2.91 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.28 | 3.27 | -0.2% | -0.0505 to 0.0359 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.2% | -2.07 to 3.52 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 297 | +0.0% | -1.21 to 1.43 | STEADY, no difference beyond the noise |
| queries a second | 4,745 | 4,747 | +0.0% | -19.3 to 23 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.68 | 2.62 | -2.4% | -0.137 to 0.00915 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 17.8 | 9.89 | -44.3% | -58.1 to 42.4 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.14 | 2.31 | -26.5% | -3.98 to 2.32 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,121 | +119.0% | 411 to 807 | power given |
| pages holding data, mean (MB) | 466 | 940 | +101.5% | 374 to 573 | power given |
| pages read from disk into the pool (misses) | 658,234 | 103,260 | -84.3% | -624,185 to -485,763 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.155 | -4.5% | -0.0156 to 0.00113 | STEADY, no difference beyond the noise |
| host CPU-seconds | 290 | 277 | -4.5% | -28.2 to 2.37 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.17 | 2.07 | -4.7% | -0.231 to 0.0262 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 |  | 1.16 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 3.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 144 | 143 | -0.7% | -32.3 to 30.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.4% | -2.83 to 1.3 | STEADY, no difference beyond the noise |
| queries a second | 3,957 | 3,942 | -0.4% | -56.5 to 25.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 177 | 154 | -12.8% | -215 to 170 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 501 | 336 | -32.9% | -922 to 592 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 35.7 | 29.2 | -18.0% | -47.5 to 34.6 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,266 | +147.4% | 729 to 780 | power given |
| pages holding data, mean (MB) | 466 | 1,028 | +120.4% | 549 to 574 | power given |
| pages read from disk into the pool (misses) | 617,450 | 84,584 | -86.3% | -576,415 to -489,317 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.173 | -10.0% | -0.0374 to -0.00115 | GAIN |
| host CPU-seconds | 343 | 308 | -10.0% | -68.4 to 0.104 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.25 | 4.77 | -9.1% | -1.81 to 0.847 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 5.5 to 15.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,943 | 2,946 | +0.1% | -2.31 to 7.66 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,951 | 2,953 | +0.1% | -3.04 to 7 | STEADY, no difference beyond the noise |
| queries a second | 2,951 | 2,953 | +0.1% | -3.04 to 7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.328 | 0.324 | -1.2% | -0.0126 to 0.00461 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.459 | 0.456 | -0.6% | -0.0141 to 0.00881 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.198 | -0.9% | -0.00506 to 0.00133 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -17.2 to 10.9 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,160 | 366,689 | -0.4% | -11,239 to 8,298 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.162 | -0.6% | -0.00351 to 0.0014 | STEADY, no difference beyond the noise |
| host CPU-seconds | 288 | 286 | -0.7% | -6.22 to 2.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.214 | 0.212 | -0.7% | -0.00449 to 0.00129 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 33.3 | 39.1 | +17.3% | -4.86 to 16.4 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 985 | -0.0% | -5.95 to 5.08 | STEADY, no difference beyond the noise |
| queries a second | 985 | 985 | -0.0% | -5.95 to 5.08 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.5 | 1.45 | -3.2% | -0.314 to 0.218 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.59 | 2.48 | -4.3% | -0.505 to 0.28 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.954 | 0.939 | -1.6% | -0.0931 to 0.0627 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.3% | 704 to 743 | power given |
| pages holding data, mean (MB) | 459 | 888 | +93.6% | 417 to 442 | power given |
| pages read from disk into the pool (misses) | 187,818 | 71,932 | -61.7% | -134,707 to -97,065 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.227 | -1.4% | -0.0306 to 0.0244 | STEADY, no difference beyond the noise |
| host CPU-seconds | 403 | 398 | -1.3% | -53.1 to 42.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 27.8 | 22.4 | -19.3% | -21.9 to 11.2 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
