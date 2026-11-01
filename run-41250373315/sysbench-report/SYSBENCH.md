# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | +0.1% | -2.77 to 3.09 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.0% | -3.14 to 3.35 | STEADY, no difference beyond the noise |
| queries a second | 4,740 | 4,742 | +0.0% | -50.3 to 53.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.9 | 2.88 | -0.7% | -0.443 to 0.404 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.6 | 4.49 | -2.4% | -0.835 to 0.614 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.44 | 1.4 | -3.0% | -0.182 to 0.0961 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 545 | +6.5% | -111 to 177 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 480 | +6.9% | -98.7 to 160 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 247,827 | 237,258 | -4.3% | -57,685 to 36,545 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.108 | -1.9% | -0.0114 to 0.00727 | STEADY, no difference beyond the noise |
| host CPU-seconds | 66.2 | 64.9 | -1.9% | -6.85 to 4.35 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.47 | 1.44 | -1.9% | -0.16 to 0.103 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -2.84 to 2.71 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -2.97 to 2.87 | STEADY, no difference beyond the noise |
| queries a second | 4,720 | 4,719 | -0.0% | -47.5 to 45.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.34 | 3.32 | -0.6% | -0.106 to 0.0661 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.6 | 4.54 | -1.2% | -0.292 to 0.182 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.58 | 2.55 | -0.9% | -0.0477 to 0.000686 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 625 | +22.0% | -130 to 355 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 562 | +21.8% | -107 to 308 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,078 | 492,569 | -24.7% | -519,163 to 196,146 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.208 | -0.7% | -0.00443 to 0.00145 | STEADY, no difference beyond the noise |
| host CPU-seconds | 375 | 372 | -0.7% | -7.62 to 2.24 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.78 | 2.76 | -0.7% | -0.033 to -0.00526 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.0% | -3.5 to 3.66 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.2% | -0.886 to 0.114 | STEADY, no difference beyond the noise |
| queries a second | 3,950 | 3,942 | -0.2% | -17.7 to 2.28 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.4 | 5.6 | -12.5% | -3.56 to 1.96 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 20.8 | 16.5 | -20.6% | -13.1 to 4.58 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.41 | 3.21 | -5.8% | -0.898 to 0.501 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,199 | +134.1% | 573 to 801 | power given |
| pages holding data, mean (MB) | 463 | 990 | +113.7% | 480 to 574 | power given |
| pages read from disk into the pool (misses) | 617,268 | 146,327 | -76.3% | -526,851 to -415,031 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.12 | -6.4% | -0.00881 to -0.00755 | GAIN |
| host CPU-seconds | 228 | 214 | -6.4% | -15.4 to -13.6 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.6 | 2.43 | -6.4% | -0.21 to -0.123 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 9.67 |  | 2.49 to 16.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 3.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,958 | 2,959 | +0.1% | -7.41 to 10.6 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,966 | +0.1% | -2.37 to 5.95 | STEADY, no difference beyond the noise |
| queries a second | 2,964 | 2,966 | +0.1% | -2.37 to 5.95 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.197 | 0.192 | -2.4% | -0.0188 to 0.00946 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.348 | 0.346 | -0.6% | -0.0248 to 0.0208 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.17 | 0.168 | -1.2% | -0.104 to 0.1 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,131 | +120.8% | 413 to 825 | power given |
| pages holding data, mean (MB) | 466 | 912 | +95.7% | 417 to 475 | power given |
| pages read from disk into the pool (misses) | 368,941 | 79,494 | -78.5% | -307,287 to -271,607 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.105 | -1.7% | -0.0022 to -0.00136 | GAIN |
| host CPU-seconds | 189 | 186 | -1.6% | -3.74 to -2.45 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.14 | 0.138 | -1.7% | -0.00283 to -0.00192 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 225 | 275 | +22.1% | -125 to 225 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 989 | 988 | -0.1% | -3.68 to 1.04 | STEADY, no difference beyond the noise |
| queries a second | 989 | 988 | -0.1% | -3.68 to 1.04 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.7 | 4.16 | -11.5% | -6.69 to 5.6 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.7 | 12.7 | +0.4% | -21.3 to 21.4 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.49 | 1.41 | -5.2% | -1.23 to 1.08 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,224 | +139.1% | 649 to 775 | power given |
| pages holding data, mean (MB) | 454 | 887 | +95.3% | 404 to 462 | power given |
| pages read from disk into the pool (misses) | 192,114 | 71,492 | -62.8% | -127,681 to -113,561 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.109 | -6.3% | -0.0307 to 0.0162 | STEADY, no difference beyond the noise |
| host CPU-seconds | 204 | 191 | -6.2% | -53.7 to 28.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.04 | 1.57 | -23.1% | -2.25 to 1.31 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
