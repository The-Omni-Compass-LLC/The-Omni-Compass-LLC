# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 289 | -0.5% | -30.8 to 28 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -3.91 to 2.89 | STEADY, no difference beyond the noise |
| queries a second | 4,727 | 4,719 | -0.2% | -62.6 to 46.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.01 | 5.03 | +25.3% | -7.09 to 9.12 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 805 | 36.2 | -95.5% | -4,279 to 2,741 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 25.5 | 3.9 | -84.7% | -125 to 82 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 723 | +465.1% | -129 to 1,320 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 657 | +445.8% | -55.2 to 1,128 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 602,058 | 244,198 | -59.4% | -582,529 to -133,191 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.163 | -2.7% | -0.00812 to -0.000936 | GAIN |
| host CPU-seconds | 100 | 97.6 | -2.7% | -4.77 to -0.667 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.22 | -2.2% | -0.237 to 0.135 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 291 | +0.1% | -5.76 to 6.45 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.1% | -3.34 to 2.84 | STEADY, no difference beyond the noise |
| queries a second | 4,744 | 4,740 | -0.1% | -53.4 to 45.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.98 | 2.81 | -5.8% | -0.448 to 0.0989 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 55.5 | 45.7 | -17.7% | -119 to 99.8 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.84 | 3.32 | -13.4% | -2.91 to 1.88 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,153 | +800.6% | 941 to 1,109 | power given |
| pages holding data, mean (MB) | 120 | 947 | +688.6% | 807 to 847 | power given |
| pages read from disk into the pool (misses) | 2,004,091 | 101,578 | -94.9% | -1,915,359 to -1,889,668 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.16 | -6.2% | -0.0194 to -0.00162 | GAIN |
| host CPU-seconds | 306 | 287 | -6.2% | -35.4 to -2.6 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.31 | 2.17 | -6.3% | -0.298 to 0.00874 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 1.58 to 26.4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 10.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 180 | 195 | +8.4% | 10.5 to 19.8 | GAIN |
| throughput (transactions a second) | 197 | 197 | -0.0% | -5.91 to 5.79 | STEADY, no difference beyond the noise |
| queries a second | 3,932 | 3,931 | -0.0% | -118 to 116 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.6 | 7.13 | -43.4% | -6.28 to -4.67 | GAIN |
| latency, 99th percentile (ms) | 17.9 | 9.57 | -46.4% | -11.5 to -5.08 | GAIN |
| latency, mean (ms) | 6.36 | 5.02 | -21.1% | -2.76 to 0.0798 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,043 | +715.1% | 630 to 1,200 | power given |
| pages holding data, mean (MB) | 118 | 919 | +676.8% | 608 to 993 | power given |
| pages read from disk into the pool (misses) | 1,668,763 | 163,223 | -90.2% | -1,653,818 to -1,357,263 | shown, not judged |
| host CPU busy (share of the run) | 0.309 | 0.264 | -14.7% | -0.0588 to -0.0319 | GAIN |
| host CPU-seconds | 544 | 464 | -14.8% | -103 to -57.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.59 | 5.18 | -21.4% | -1.52 to -1.3 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.7 to 12.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 2.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,952 | +0.0% | -11.7 to 12.7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,967 | +0.1% | -3.09 to 7.15 | STEADY, no difference beyond the noise |
| queries a second | 2,965 | 2,967 | +0.1% | -3.09 to 7.15 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.218 | -13.9% | -0.0643 to -0.00633 | GAIN |
| latency, 99th percentile (ms) | 0.4 | 0.398 | -0.5% | -0.0565 to 0.0525 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.276 | 0.317 | +14.9% | -0.0695 to 0.152 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,171 | +815.2% | 994 to 1,093 | power given |
| pages holding data, mean (MB) | 121 | 916 | +655.4% | 774 to 815 | power given |
| pages read from disk into the pool (misses) | 1,030,485 | 90,032 | -91.3% | -992,601 to -888,305 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.109 | -7.6% | -0.0193 to 0.00134 | STEADY, no difference beyond the noise |
| host CPU-seconds | 209 | 193 | -7.6% | -33.9 to 2.27 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.156 | 0.144 | -7.6% | -0.0257 to 0.00208 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 7.9 to 10.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 7.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 44.7 | 58.1 | +29.8% | -12.2 to 38.9 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -4.15 to 1.96 | STEADY, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -4.15 to 1.96 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 587 | 390 | -33.6% | -1,153 to 758 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,576 | 1,002 | -36.4% | -4,144 to 2,997 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 110 | 77.7 | -29.3% | -153 to 88.4 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,286 | +904.7% | 1,084 to 1,232 | power given |
| pages holding data, mean (MB) | 119 | 885 | +641.5% | 764 to 767 | power given |
| pages read from disk into the pool (misses) | 419,571 | 71,215 | -83.0% | -360,885 to -335,826 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.129 | -21.8% | -0.0493 to -0.0228 | GAIN |
| host CPU-seconds | 292 | 229 | -21.6% | -87 to -38.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 16.3 | 8.99 | -44.7% | -23.7 to 9.11 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
