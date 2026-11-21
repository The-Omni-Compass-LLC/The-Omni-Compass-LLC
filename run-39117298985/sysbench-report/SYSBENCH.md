# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.2% | -4.08 to 2.71 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.2% | -4.37 to 2.99 | EVEN, no difference beyond the noise |
| queries a second | 4,706 | 4,695 | -0.2% | -69.9 to 47.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.06 | 5.03 | -0.6% | -0.291 to 0.231 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.67 | 6.71 | +0.6% | -0.133 to 0.214 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 3.29 | -0.7% | -0.052 to 0.00723 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.3% | -0.974 to 19.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 132 | +9.8% | 4.63 to 18.8 | power given |
| pages read from disk into the pool (misses) | 580,063 | 542,938 | -6.4% | -118,034 to 43,784 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.194 | -1.1% | -0.00517 to 0.000836 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 107 | -1.2% | -2.72 to 0.164 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.42 | 2.39 | -1.0% | -0.0458 to -0.000166 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -2.41 to 1.29 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -2.64 to 1.4 | EVEN, no difference beyond the noise |
| queries a second | 4,724 | 4,714 | -0.2% | -42.3 to 22.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.13 | 4.1 | -0.6% | -0.133 to 0.0826 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.71 | +0.6% | -0.113 to 0.182 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.23 | 3.21 | -0.7% | -0.0312 to -0.0153 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.2% | 7.37 to 13.7 | power given |
| pages holding data, mean (MB) | 120 | 137 | +13.7% | 11.9 to 21.1 | power given |
| pages read from disk into the pool (misses) | 1,980,194 | 1,885,284 | -4.8% | -159,555 to -30,265 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.198 | -0.9% | -0.00361 to 0.000106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 332 | 329 | -0.9% | -6.29 to 0.314 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.46 | 2.45 | -0.7% | -0.0301 to -0.00467 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 195 | +0.4% | 0.369 to 1.25 | GAIN |
| throughput (transactions a second) | 196 | 196 | +0.4% | 0.134 to 1.49 | GAIN |
| queries a second | 3,911 | 3,928 | +0.4% | 2.68 to 29.8 | GAIN |
| latency, 95th percentile (ms) | 7.7 | 7.7 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 10.3 | 10.3 | +0.0% | -0.462 to 0.462 | EVEN, the same |
| latency, mean (ms) | 4.26 | 4.27 | +0.3% | -0.0168 to 0.0386 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.6% | 7.53 to 14.4 | power given |
| pages holding data, mean (MB) | 121 | 131 | +8.3% | 6.65 to 13.4 | power given |
| pages read from disk into the pool (misses) | 1,659,948 | 1,614,504 | -2.7% | -126,737 to 35,848 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.228 | +0.2% | -0.00174 to 0.00278 | EVEN, no difference beyond the noise |
| host CPU-seconds | 409 | 410 | +0.2% | -3.06 to 4.73 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.59 | 4.58 | -0.2% | -0.0489 to 0.0315 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 5.8 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,960 | 2,957 | -0.1% | -19.1 to 13.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,964 | -0.1% | -15.8 to 12.3 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,964 | -0.1% | -15.8 to 12.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.225 | 0.227 | +1.2% | -0.0375 to 0.0428 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.346 | 0.342 | -1.2% | -0.075 to 0.067 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.103 | 0.0967 | -6.0% | -0.0334 to 0.0211 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.0% | 0.0566 to 17.7 | power given |
| pages holding data, mean (MB) | 121 | 134 | +10.2% | 5.14 to 19.6 | power given |
| pages read from disk into the pool (misses) | 1,029,702 | 1,001,627 | -2.7% | -68,056 to 11,907 | shown, not judged |
| host CPU busy (share of the run) | 0.075 | 0.0731 | -2.6% | -0.016 to 0.0122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 134 | 131 | -2.6% | -28.8 to 21.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0998 | 0.0973 | -2.5% | -0.0217 to 0.0168 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 101 | 108 | +6.9% | -9.07 to 23 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 987 | -0.1% | -1.33 to 0.301 | EVEN, no difference beyond the noise |
| queries a second | 987 | 987 | -0.1% | -1.33 to 0.301 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 149 | 119 | -20.1% | -144 to 84.6 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 343 | 339 | -1.2% | -481 to 473 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 26.2 | 23.1 | -11.9% | -28.2 to 22 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.6% | 1.97 to 20.1 | power given |
| pages holding data, mean (MB) | 119 | 125 | +4.8% | -2.42 to 13.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 419,034 | 411,249 | -1.9% | -23,677 to 8,108 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.163 | -1.5% | -0.00768 to 0.00276 | EVEN, no difference beyond the noise |
| host CPU-seconds | 292 | 287 | -1.6% | -14.4 to 5.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 7.28 | 6.39 | -12.2% | -3.9 to 2.12 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
