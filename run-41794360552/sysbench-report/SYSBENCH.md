# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 289 | +0.3% | -3.71 to 5.31 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.1% | -6.07 to 6.7 | STEADY, no difference beyond the noise |
| queries a second | 4,673 | 4,678 | +0.1% | -97.1 to 107 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.2 | 4.18 | -0.6% | -0.505 to 0.451 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 59.6 | 8.75 | -85.3% | -272 to 170 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.82 | 2.65 | -30.5% | -7.29 to 4.96 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 446 | 446 | +0.1% | -2.8 to 3.35 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,315 | 246,784 | +1.0% | -5,404 to 10,342 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.179 | +0.6% | -0.00781 to 0.00977 | STEADY, no difference beyond the noise |
| host CPU-seconds | 109 | 110 | +0.5% | -4.63 to 5.79 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.45 | 2.46 | +0.3% | -0.118 to 0.132 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.1% | -2.45 to 2.06 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -2.35 to 2.08 | STEADY, no difference beyond the noise |
| queries a second | 4,718 | 4,716 | -0.0% | -37.7 to 33.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.98 | 3.93 | -1.2% | -0.321 to 0.224 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.54 | 5.54 | -0.0% | -0.25 to 0.249 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.02 | 2.99 | -1.2% | -0.164 to 0.0883 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 724 | +41.5% | -79.7 to 504 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 651 | +40.4% | -61.1 to 436 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,057 | 347,976 | -47.0% | -722,459 to 106,297 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.236 | -1.1% | -0.0115 to 0.00618 | STEADY, no difference beyond the noise |
| host CPU-seconds | 425 | 420 | -1.1% | -20.6 to 11 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.15 | 3.12 | -1.1% | -0.172 to 0.105 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 196 | +1.7% | 2.07 to 4.67 | GAIN |
| throughput (transactions a second) | 196 | 196 | -0.0% | -2.56 to 2.46 | STEADY, no difference beyond the noise |
| queries a second | 3,927 | 3,926 | -0.0% | -51.2 to 49.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.18 | 6.55 | -19.9% | -2.32 to -0.94 | GAIN |
| latency, 99th percentile (ms) | 12.2 | 8.38 | -31.5% | -5.07 to -2.63 | GAIN |
| latency, mean (ms) | 5.06 | 4.74 | -6.4% | -0.464 to -0.187 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 993 | +94.0% | 360 to 602 | power given |
| pages holding data, mean (MB) | 463 | 884 | +91.1% | 300 to 543 | power given |
| pages read from disk into the pool (misses) | 617,084 | 145,571 | -76.4% | -536,997 to -406,028 | shown, not judged |
| host CPU busy (share of the run) | 0.276 | 0.259 | -6.0% | -0.0219 to -0.0112 | GAIN |
| host CPU-seconds | 485 | 455 | -6.0% | -38.6 to -19.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.5 | 5.07 | -7.7% | -0.504 to -0.338 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,939 | 2,940 | +0.0% | -7.82 to 9.53 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,941 | 2,942 | +0.0% | -9.02 to 10.2 | STEADY, no difference beyond the noise |
| queries a second | 2,941 | 2,942 | +0.0% | -9.02 to 10.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.292 | 0.28 | -4.2% | -0.0203 to -0.00435 | GAIN |
| latency, 99th percentile (ms) | 0.422 | 0.414 | -1.8% | -0.0276 to 0.0123 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.182 | 0.178 | -2.5% | -0.0122 to 0.00297 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -18.5 to 11.6 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,123 | 366,420 | -0.5% | -10,207 to 6,801 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.154 | -1.8% | -0.00886 to 0.00331 | STEADY, no difference beyond the noise |
| host CPU-seconds | 283 | 279 | -1.7% | -15.6 to 5.88 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.21 | 0.206 | -1.7% | -0.011 to 0.00363 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 63.7 | 74.1 | +16.4% | -47 to 67.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.1% | -6.89 to 5.76 | STEADY, no difference beyond the noise |
| queries a second | 985 | 984 | -0.1% | -6.89 to 5.76 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.36 | 1.31 | -3.4% | -0.405 to 0.312 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.35 | 2.31 | -1.6% | -1.17 to 1.09 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.901 | 0.89 | -1.1% | -0.138 to 0.118 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,219 | +138.0% | 621 to 792 | power given |
| pages holding data, mean (MB) | 457 | 890 | +94.5% | 407 to 457 | power given |
| pages read from disk into the pool (misses) | 190,662 | 70,617 | -63.0% | -128,277 to -111,814 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.222 | -2.8% | -0.0452 to 0.0324 | STEADY, no difference beyond the noise |
| host CPU-seconds | 404 | 392 | -2.8% | -80.1 to 57.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 15.2 | 12 | -20.9% | -21.2 to 14.9 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
