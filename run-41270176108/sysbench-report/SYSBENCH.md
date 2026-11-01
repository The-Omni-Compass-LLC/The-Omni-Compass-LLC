# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.4% | -4.07 to 6.17 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.3% | -4.3 to 6.01 | STEADY, no difference beyond the noise |
| queries a second | 4,727 | 4,741 | +0.3% | -68.9 to 96.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.88 | +1.8% | -0.077 to 0.179 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.46 | 4.44 | -0.6% | -0.257 to 0.206 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.34 | -1.0% | -0.0289 to 0.00118 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 447 | 448 | +0.1% | -1.1 to 1.58 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,762 | 248,512 | +0.7% | -4,384 to 7,885 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.103 | -0.3% | -0.00512 to 0.00459 | STEADY, no difference beyond the noise |
| host CPU-seconds | 61.8 | 61.6 | -0.3% | -3.19 to 2.84 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.37 | 1.37 | -0.6% | -0.0606 to 0.0443 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 295 | -0.6% | -4.13 to 0.294 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 295 | -0.7% | -3.99 to 0.0894 | STEADY, no difference beyond the noise |
| queries a second | 4,758 | 4,726 | -0.7% | -63.8 to 1.43 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.89 | 1.86 | -1.8% | -0.2 to 0.133 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.62 | 3.41 | -5.8% | -0.569 to 0.149 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.32 | 1.31 | -0.9% | -0.0652 to 0.0423 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 462 | 458 | -0.7% | -16.7 to 10.5 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,523 | 653,535 | -0.3% | -8,046 to 4,071 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.106 | -0.8% | -0.00637 to 0.00467 | STEADY, no difference beyond the noise |
| host CPU-seconds | 192 | 190 | -0.8% | -11.4 to 8.29 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.42 | 1.42 | -0.2% | -0.0653 to 0.0605 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 132 | 140 | +6.1% | -22 to 38.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.0% | -1.79 to 1.72 | STEADY, no difference beyond the noise |
| queries a second | 3,934 | 3,933 | -0.0% | -35.8 to 34.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 166 | 107 | -35.5% | -91 to -26.8 | GAIN |
| latency, 99th percentile (ms) | 425 | 240 | -43.5% | -533 to 164 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 32.8 | 21.4 | -34.7% | -18.9 to -3.87 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,283 | +150.5% | 724 to 817 | power given |
| pages holding data, mean (MB) | 463 | 1,029 | +122.3% | 553 to 579 | power given |
| pages read from disk into the pool (misses) | 618,330 | 82,765 | -86.6% | -572,299 to -498,833 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.166 | -10.9% | -0.023 to -0.0175 | GAIN |
| host CPU-seconds | 331 | 295 | -11.0% | -40.9 to -31.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.52 | 4.67 | -15.4% | -1.83 to 0.124 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 2.68 to 18.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,948 | +0.1% | -1.91 to 8.31 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,951 | 2,954 | +0.1% | -3.65 to 9.12 | STEADY, no difference beyond the noise |
| queries a second | 2,951 | 2,954 | +0.1% | -3.65 to 9.12 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.307 | -3.8% | -0.0378 to 0.0138 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.445 | -1.3% | -0.0179 to 0.00659 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.192 | -1.3% | -0.0128 to 0.00786 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -16.9 to 10.3 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,046 | 365,829 | -0.3% | -15,356 to 12,921 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.157 | -0.5% | -0.0103 to 0.0086 | STEADY, no difference beyond the noise |
| host CPU-seconds | 278 | 277 | -0.5% | -18.5 to 15.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.207 | 0.205 | -0.6% | -0.0139 to 0.0112 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 18.5 | 21.8 | +17.8% | -4.74 to 11.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 986 | 983 | -0.3% | -13.3 to 8.29 | STEADY, no difference beyond the noise |
| queries a second | 986 | 983 | -0.3% | -13.3 to 8.29 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.78 | 1.73 | -3.2% | -0.37 to 0.256 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.91 | 3.86 | -1.2% | -0.253 to 0.157 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.04 | -1.5% | -0.107 to 0.0755 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.3% | 702 to 745 | power given |
| pages holding data, mean (MB) | 458 | 888 | +93.9% | 412 to 448 | power given |
| pages read from disk into the pool (misses) | 188,282 | 71,680 | -61.9% | -135,609 to -97,593 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.218 | -2.9% | -0.0355 to 0.0223 | STEADY, no difference beyond the noise |
| host CPU-seconds | 393 | 382 | -2.9% | -61.7 to 38.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 47.8 | 38.3 | -19.9% | -38.8 to 19.7 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
