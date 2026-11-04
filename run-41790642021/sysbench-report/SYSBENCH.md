# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.1% | -5.48 to 4.82 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -6.09 to 5.21 | STEADY, no difference beyond the noise |
| queries a second | 4,709 | 4,702 | -0.1% | -97.4 to 83.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.97 | 4.91 | -1.2% | -0.186 to 0.0681 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.13 | -1.2% | -0.269 to 0.0987 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 3.16 | -0.4% | -0.0282 to 0.00026 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 779 | +52.1% | 122 to 412 | power given |
| pages holding data, mean (MB) | 453 | 706 | +55.7% | 123 to 382 | power given |
| pages read from disk into the pool (misses) | 246,152 | 163,198 | -33.7% | -122,987 to -42,922 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.246 | +0.1% | -0.00519 to 0.00544 | STEADY, no difference beyond the noise |
| host CPU-seconds | 146 | 146 | +0.0% | -2.95 to 3.02 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.26 | 3.26 | +0.2% | -0.0114 to 0.0215 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

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

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 197 | +2.2% | 1.5 to 6.99 | GAIN |
| throughput (transactions a second) | 197 | 197 | -0.0% | -0.753 to 0.714 | STEADY, no difference beyond the noise |
| queries a second | 3,944 | 3,943 | -0.0% | -15.1 to 14.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.74 | 6.91 | -20.9% | -2.65 to -1.01 | GAIN |
| latency, 99th percentile (ms) | 12.8 | 8.74 | -31.9% | -4.93 to -3.26 | GAIN |
| latency, mean (ms) | 5.44 | 5.07 | -6.8% | -0.558 to -0.182 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,028 | +100.7% | 393 to 638 | power given |
| pages holding data, mean (MB) | 463 | 911 | +96.9% | 362 to 535 | power given |
| pages read from disk into the pool (misses) | 620,771 | 123,784 | -80.1% | -594,476 to -399,497 | shown, not judged |
| host CPU busy (share of the run) | 0.296 | 0.275 | -7.0% | -0.0215 to -0.0196 | GAIN |
| host CPU-seconds | 519 | 483 | -7.0% | -37.4 to -35.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.89 | 5.36 | -9.0% | -0.603 to -0.459 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,948 | -0.1% | -9.27 to 2.72 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,958 | 2,954 | -0.1% | -9.59 to 2.27 | STEADY, no difference beyond the noise |
| queries a second | 2,958 | 2,954 | -0.1% | -9.59 to 2.27 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.312 | 0.308 | -1.3% | -0.0243 to 0.0163 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.451 | -1.2% | -0.0357 to 0.025 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.191 | -0.8% | -0.0148 to 0.0118 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -17.8 to 11.2 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,962 | 366,020 | -0.8% | -11,990 to 6,105 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.156 | -0.2% | -0.0102 to 0.00967 | STEADY, no difference beyond the noise |
| host CPU-seconds | 275 | 275 | -0.1% | -18 to 17.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.204 | 0.204 | -0.0% | -0.0128 to 0.0126 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 8.83 | 10.1 | +14.7% | -1.33 to 3.93 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.1% | -7.87 to 5.36 | STEADY, no difference beyond the noise |
| queries a second | 985 | 984 | -0.1% | -7.87 to 5.36 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.85 | 1.8 | -2.5% | -0.397 to 0.303 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.86 | 3.84 | -0.6% | -0.451 to 0.408 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.09 | 1.09 | -0.0% | -0.0852 to 0.0847 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 699 to 749 | power given |
| pages holding data, mean (MB) | 457 | 889 | +94.3% | 407 to 456 | power given |
| pages read from disk into the pool (misses) | 192,141 | 71,651 | -62.7% | -128,272 to -112,708 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.232 | -2.1% | -0.032 to 0.0222 | STEADY, no difference beyond the noise |
| host CPU-seconds | 416 | 408 | -2.0% | -56 to 39.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 103 | 89 | -13.7% | -47.1 to 18.8 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
