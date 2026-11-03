# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.4% | -2.5 to 4.86 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.3% | -0.533 to 2.06 | STEADY, no difference beyond the noise |
| queries a second | 4,727 | 4,739 | +0.3% | -8.52 to 33 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.19 | 3.08 | -3.7% | -0.883 to 0.646 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.94 | 4.57 | -7.4% | -1.86 to 1.13 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.52 | 1.49 | -1.7% | -0.215 to 0.164 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 674 | +31.7% | -104 to 429 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 605 | +34.8% | -90.6 to 403 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 248,700 | 194,960 | -21.6% | -126,786 to 19,305 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.115 | +0.2% | -0.0056 to 0.00617 | STEADY, no difference beyond the noise |
| host CPU-seconds | 68.8 | 69 | +0.3% | -3.25 to 3.66 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.53 | 1.53 | -0.1% | -0.0799 to 0.0761 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.4% | -2.64 to 5.02 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.4% | -2.58 to 4.69 | STEADY, no difference beyond the noise |
| queries a second | 4,718 | 4,735 | +0.4% | -41.3 to 75 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.3 | 4.15 | -3.6% | -0.347 to 0.0408 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.28 | 6.06 | -3.5% | -0.227 to -0.216 | GAIN |
| latency, mean (ms) | 3.15 | 3.04 | -3.3% | -0.272 to 0.0648 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 860 | +68.0% | 239 to 458 | power given |
| pages holding data, mean (MB) | 463 | 760 | +63.9% | 207 to 386 | power given |
| pages read from disk into the pool (misses) | 656,189 | 201,840 | -69.2% | -534,828 to -373,871 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.24 | -2.5% | -0.0206 to 0.00852 | STEADY, no difference beyond the noise |
| host CPU-seconds | 437 | 426 | -2.4% | -36.3 to 15 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.25 | 3.15 | -2.8% | -0.261 to 0.0776 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 196 | +3.1% | 3.68 to 8.05 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.3% | -1.64 to 2.78 | STEADY, no difference beyond the noise |
| queries a second | 3,930 | 3,941 | +0.3% | -32.8 to 55.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.56 | 7.43 | -22.3% | -2.62 to -1.64 | GAIN |
| latency, 99th percentile (ms) | 14.3 | 10.1 | -29.4% | -4.75 to -3.66 | GAIN |
| latency, mean (ms) | 5.47 | 5.09 | -7.0% | -0.427 to -0.336 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,087 | +112.3% | 481 to 670 | power given |
| pages holding data, mean (MB) | 462 | 967 | +109.2% | 442 to 567 | power given |
| pages read from disk into the pool (misses) | 617,916 | 116,575 | -81.1% | -603,046 to -399,636 | shown, not judged |
| host CPU busy (share of the run) | 0.284 | 0.268 | -5.8% | -0.0223 to -0.0104 | GAIN |
| host CPU-seconds | 499 | 470 | -5.8% | -39.3 to -18.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.74 | 5.25 | -8.6% | -0.597 to -0.395 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,955 | 2,950 | -0.2% | -16.9 to 6.94 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,956 | 2,951 | -0.2% | -16.4 to 6.64 | STEADY, no difference beyond the noise |
| queries a second | 2,956 | 2,951 | -0.2% | -16.4 to 6.64 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.28 | 0.278 | -0.6% | -0.00884 to 0.0055 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.381 | 0.381 | +0.0% | 0 to 0 | STEADY, the same |
| latency, mean (ms) | 0.172 | 0.172 | -0.0% | -0.00123 to 0.0011 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -17 to 10.4 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,310 | 366,030 | -0.6% | -14,037 to 9,478 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.143 | +0.0% | 7.28e-06 to 9.34e-05 | power given |
| host CPU-seconds | 252 | 252 | +0.0% | -0.119 to 0.172 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.187 | 0.187 | +0.2% | -0.00044 to 0.00107 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 81.3 | 93.4 | +14.9% | -16.9 to 41.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 986 | +0.1% | -5.7 to 8.06 | STEADY, no difference beyond the noise |
| queries a second | 985 | 986 | +0.1% | -5.7 to 8.06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 277 | 281 | +1.2% | -352 to 359 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 759 | 724 | -4.7% | -1,458 to 1,387 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 59.7 | 57.9 | -3.0% | -78.2 to 74.6 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,241 | +142.4% | 694 to 765 | power given |
| pages holding data, mean (MB) | 458 | 895 | +95.5% | 403 to 472 | power given |
| pages read from disk into the pool (misses) | 191,118 | 69,763 | -63.5% | -129,800 to -112,910 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.123 | -4.8% | -0.0314 to 0.0189 | STEADY, no difference beyond the noise |
| host CPU-seconds | 229 | 218 | -4.8% | -52.6 to 30.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.4 | 5.15 | -19.6% | -5.23 to 2.73 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
