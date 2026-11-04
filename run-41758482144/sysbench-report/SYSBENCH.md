# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.2% | -5.3 to 6.52 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.5% | -4.68 to 7.83 | STEADY, no difference beyond the noise |
| queries a second | 4,693 | 4,719 | +0.5% | -74.9 to 125 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5 | 4.94 | -1.2% | -0.393 to 0.278 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.67 | 7.1 | +6.4% | -0.754 to 1.61 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.26 | 3.16 | -3.0% | -0.221 to 0.0244 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 809 | +532.4% | 114 to 1,249 | power given |
| pages holding data, mean (MB) | 121 | 715 | +491.9% | 171 to 1,017 | power given |
| pages read from disk into the pool (misses) | 600,374 | 150,590 | -74.9% | -555,709 to -343,860 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.245 | -2.4% | -0.0148 to 0.00282 | STEADY, no difference beyond the noise |
| host CPU-seconds | 149 | 146 | -2.4% | -8.7 to 1.57 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.33 | 3.24 | -2.6% | -0.219 to 0.0458 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 295 | -0.2% | -7.11 to 5.89 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.2% | -6.18 to 5.22 | STEADY, no difference beyond the noise |
| queries a second | 4,746 | 4,738 | -0.2% | -98.8 to 83.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.63 | 2.54 | -3.5% | -0.0948 to -0.0919 | GAIN |
| latency, 99th percentile (ms) | 4.1 | 4.11 | +0.2% | -0.653 to 0.668 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.17 | 2.11 | -2.9% | -0.431 to 0.306 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,035 | +708.3% | 714 to 1,099 | power given |
| pages holding data, mean (MB) | 120 | 877 | +629.1% | 578 to 936 | power given |
| pages read from disk into the pool (misses) | 2,025,066 | 376,625 | -81.4% | -2,468,452 to -828,431 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.153 | -5.6% | -0.0158 to -0.00241 | GAIN |
| host CPU-seconds | 291 | 275 | -5.5% | -27.9 to -4.39 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.04 | -5.4% | -0.162 to -0.0701 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 9.67 |  | 3.93 to 15.4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 4.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 195 | +2.9% | 1.94 to 8.88 | GAIN |
| throughput (transactions a second) | 196 | 196 | -0.2% | -4.38 to 3.66 | STEADY, no difference beyond the noise |
| queries a second | 3,921 | 3,914 | -0.2% | -87.7 to 73.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.73 | 5.28 | -45.8% | -4.69 to -4.22 | GAIN |
| latency, 99th percentile (ms) | 14.7 | 7.94 | -45.8% | -8.86 to -4.58 | GAIN |
| latency, mean (ms) | 4.68 | 3.81 | -18.6% | -0.928 to -0.813 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,172 | +815.4% | 929 to 1,158 | power given |
| pages holding data, mean (MB) | 121 | 977 | +704.4% | 741 to 970 | power given |
| pages read from disk into the pool (misses) | 1,672,875 | 132,845 | -92.1% | -1,595,976 to -1,484,084 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.187 | -15.1% | -0.0385 to -0.0279 | GAIN |
| host CPU-seconds | 400 | 340 | -15.0% | -69.5 to -51 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.59 | 3.8 | -17.4% | -0.891 to -0.705 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 7.46 to 13.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,939 | 2,935 | -0.1% | -15.9 to 8.64 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,942 | 2,940 | -0.1% | -15.1 to 10.2 | STEADY, no difference beyond the noise |
| queries a second | 2,942 | 2,940 | -0.1% | -15.1 to 10.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.272 | 0.303 | +11.5% | 0.00477 to 0.0579 | LOSS |
| latency, 99th percentile (ms) | 0.409 | 0.424 | +3.6% | -0.00398 to 0.0333 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.173 | 0.173 | +0.4% | -0.00203 to 0.0035 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 287 | +124.0% | -12.1 to 330 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 274 | +126.2% | -5.68 to 312 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,028,664 | 684,094 | -33.5% | -633,170 to -55,970 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.149 | +0.5% | -0.00131 to 0.0027 | STEADY, no difference beyond the noise |
| host CPU-seconds | 268 | 270 | +0.5% | -2.26 to 4.89 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.199 | 0.2 | +0.6% | -0.00066 to 0.00313 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 131 | 175 | +34.1% | 32.6 to 56.6 | GAIN |
| throughput (transactions a second) | 981 | 980 | -0.1% | -4.52 to 2.47 | STEADY, no difference beyond the noise |
| queries a second | 981 | 980 | -0.1% | -4.52 to 2.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.31 | 1.16 | -11.9% | -0.286 to -0.0271 | GAIN |
| latency, 99th percentile (ms) | 1.95 | 1.78 | -8.7% | -0.612 to 0.274 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.839 | 0.82 | -2.2% | -0.0672 to 0.0303 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,300 | +915.3% | 1,170 to 1,173 | power given |
| pages holding data, mean (MB) | 118 | 879 | +648.4% | 754 to 770 | power given |
| pages read from disk into the pool (misses) | 415,691 | 70,906 | -82.9% | -360,391 to -329,179 | shown, not judged |
| host CPU busy (share of the run) | 0.219 | 0.199 | -9.1% | -0.0375 to -0.00245 | GAIN |
| host CPU-seconds | 400 | 363 | -9.1% | -68.5 to -4.29 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.77 | 4.54 | -32.9% | -4.23 to -0.225 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
