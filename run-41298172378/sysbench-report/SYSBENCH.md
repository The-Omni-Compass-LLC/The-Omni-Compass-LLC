# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 294 | -0.7% | -6.28 to 1.91 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 294 | -0.7% | -4.94 to 0.779 | STEADY, no difference beyond the noise |
| queries a second | 4,741 | 4,707 | -0.7% | -79 to 12.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.78 | 2.81 | +1.2% | -0.329 to 0.397 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.29 | 4.3 | +0.4% | -0.854 to 0.892 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.35 | +2.1% | -0.268 to 0.324 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 778 | +52.0% | -378 to 910 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 665 | +48.7% | -229 to 665 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,426 | 184,520 | -23.9% | -204,773 to 88,961 | shown, not judged |
| host CPU busy (share of the run) | 0.0998 | 0.101 | +1.1% | -0.0117 to 0.014 | STEADY, no difference beyond the noise |
| host CPU-seconds | 59.9 | 60.6 | +1.2% | -6.95 to 8.35 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.33 | 1.36 | +1.9% | -0.163 to 0.213 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -3.5 to 6.84 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | +0.1% | -0.493 to 1.22 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.1% | -0.558 to 1.27 | STEADY, no difference beyond the noise |
| queries a second | 4,738 | 4,744 | +0.1% | -8.92 to 20.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.83 | 2.1 | +14.9% | -0.712 to 1.26 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.72 | 4.15 | +11.4% | -0.346 to 1.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.32 | +6.6% | -0.199 to 0.362 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 462 | 459 | -0.7% | -18.1 to 11.4 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,529 | 655,276 | -0.0% | -3,059 to 2,553 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.107 | +6.7% | -0.0175 to 0.0309 | STEADY, no difference beyond the noise |
| host CPU-seconds | 180 | 192 | +6.7% | -31.3 to 55.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.33 | 1.42 | +6.5% | -0.236 to 0.41 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 179 | 179 | +0.0% | -16 to 16.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -1.79 to 2 | STEADY, no difference beyond the noise |
| queries a second | 3,952 | 3,954 | +0.1% | -35.8 to 40 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 47.2 | 48.2 | +1.9% | -63 to 64.8 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 177 | 158 | -10.6% | -125 to 87.5 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 10.9 | 10.2 | -7.1% | -7.18 to 5.63 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,252 | +144.6% | 731 to 750 | power given |
| pages holding data, mean (MB) | 463 | 1,023 | +121.0% | 548 to 572 | power given |
| pages read from disk into the pool (misses) | 621,075 | 86,841 | -86.0% | -586,237 to -482,230 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.169 | -9.0% | -0.0181 to -0.0155 | GAIN |
| host CPU-seconds | 330 | 301 | -9.0% | -33.1 to -26.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.05 | 3.69 | -9.0% | -0.698 to -0.0339 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 11.7 |  | 7.87 to 15.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 8.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,957 | 2,952 | -0.2% | -13.5 to 3.39 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,963 | -0.1% | -9.29 to 4.5 | STEADY, no difference beyond the noise |
| queries a second | 2,965 | 2,963 | -0.1% | -9.29 to 4.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.214 | 0.209 | -2.0% | -0.0503 to 0.0416 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.377 | 0.386 | +2.3% | -0.0325 to 0.0498 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.237 | +13.2% | 0.00125 to 0.0541 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,161 | +126.8% | 604 to 694 | power given |
| pages holding data, mean (MB) | 470 | 920 | +95.7% | 418 to 482 | power given |
| pages read from disk into the pool (misses) | 369,952 | 78,494 | -78.8% | -300,883 to -282,033 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.111 | -2.4% | -0.00985 to 0.00441 | STEADY, no difference beyond the noise |
| host CPU-seconds | 202 | 197 | -2.4% | -17.5 to 7.65 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.146 | -2.3% | -0.0132 to 0.00644 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | -0.505 to 13.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 17.4 | 19.4 | +11.6% | -19.3 to 23.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 982 | 982 | -0.0% | -11.6 to 11.2 | STEADY, no difference beyond the noise |
| queries a second | 982 | 982 | -0.0% | -11.6 to 11.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 175 | 102 | -41.4% | -525 to 380 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 906 | 805 | -11.2% | -995 to 792 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 33.6 | 27.3 | -18.9% | -52.9 to 40.2 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,239 | +142.1% | 702 to 752 | power given |
| pages holding data, mean (MB) | 457 | 896 | +96.1% | 412 to 466 | power given |
| pages read from disk into the pool (misses) | 191,696 | 72,145 | -62.4% | -130,719 to -108,383 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.209 | -11.8% | -0.11 to 0.0543 | STEADY, no difference beyond the noise |
| host CPU-seconds | 417 | 368 | -11.7% | -192 to 94.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 105 | 42.8 | -59.2% | -343 to 219 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
