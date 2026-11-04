# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.4% | -4.95 to 2.32 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.5% | -5.08 to 2.02 | STEADY, no difference beyond the noise |
| queries a second | 4,705 | 4,681 | -0.5% | -81.3 to 32.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.03 | 5 | -0.6% | -0.164 to 0.102 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.22 | 7.05 | -2.3% | -0.322 to -0.0152 | GAIN |
| latency, mean (ms) | 3.19 | 3.17 | -0.8% | -0.0978 to 0.0451 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 846 | +65.3% | 183 to 486 | power given |
| pages holding data, mean (MB) | 455 | 766 | +68.4% | 183 to 439 | power given |
| pages read from disk into the pool (misses) | 248,050 | 143,221 | -42.3% | -149,144 to -60,515 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.245 | -0.5% | -0.00829 to 0.00585 | STEADY, no difference beyond the noise |
| host CPU-seconds | 146 | 146 | -0.5% | -5.09 to 3.71 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.27 | 3.27 | -0.0% | -0.0573 to 0.0549 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 297 | +0.6% | -3.2 to 6.85 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 297 | +0.6% | -3.19 to 6.78 | STEADY, no difference beyond the noise |
| queries a second | 4,722 | 4,751 | +0.6% | -51.1 to 109 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.98 | 3.96 | -0.6% | -0.127 to 0.0793 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.47 | 5.37 | -1.8% | -0.103 to -0.0925 | GAIN |
| latency, mean (ms) | 3.05 | 3.03 | -0.7% | -0.1 to 0.0587 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 642 | +25.4% | -220 to 481 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 576 | +24.5% | -199 to 426 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,782 | 454,211 | -30.6% | -700,914 to 299,772 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.242 | +0.2% | -0.00829 to 0.00939 | STEADY, no difference beyond the noise |
| host CPU-seconds | 429 | 429 | +0.2% | -14.6 to 16.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.18 | 3.16 | -0.4% | -0.0893 to 0.064 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | -1.48 to 3.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 196 | +2.0% | 2.48 to 5.04 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.1% | -0.954 to 1.4 | STEADY, no difference beyond the noise |
| queries a second | 3,927 | 3,932 | +0.1% | -19.1 to 28 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.38 | 6.63 | -20.9% | -2.31 to -1.19 | GAIN |
| latency, 99th percentile (ms) | 12.8 | 8.69 | -31.8% | -5.26 to -2.86 | GAIN |
| latency, mean (ms) | 5.09 | 4.77 | -6.2% | -0.431 to -0.202 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,004 | +96.1% | 275 to 709 | power given |
| pages holding data, mean (MB) | 462 | 892 | +92.9% | 224 to 635 | power given |
| pages read from disk into the pool (misses) | 617,379 | 134,424 | -78.2% | -546,506 to -419,404 | shown, not judged |
| host CPU busy (share of the run) | 0.273 | 0.257 | -5.9% | -0.0195 to -0.0125 | GAIN |
| host CPU-seconds | 480 | 451 | -5.9% | -34.6 to -21.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.45 | 5.03 | -7.7% | -0.513 to -0.325 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,927 | 2,927 | -0.0% | -7.45 to 6.59 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,931 | 2,931 | +0.0% | -6.07 to 6.4 | STEADY, no difference beyond the noise |
| queries a second | 2,931 | 2,931 | +0.0% | -6.07 to 6.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.222 | 0.25 | +12.8% | 0.00525 to 0.0514 | LOSS |
| latency, 99th percentile (ms) | 0.404 | 0.43 | +6.3% | -0.0191 to 0.0698 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.158 | 0.165 | +4.0% | -0.0407 to 0.0533 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 909 | +77.5% | 183 to 611 | power given |
| pages holding data, mean (MB) | 465 | 798 | +71.7% | 188 to 479 | power given |
| pages read from disk into the pool (misses) | 367,617 | 170,536 | -53.6% | -277,971 to -116,191 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.131 | +4.9% | -0.00824 to 0.0205 | STEADY, no difference beyond the noise |
| host CPU-seconds | 231 | 243 | +5.0% | -15.5 to 38.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.172 | 0.18 | +5.0% | -0.0116 to 0.0289 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.92 | 10.4 | +49.8% | 1.9 to 4.99 | GAIN |
| throughput (transactions a second) | 981 | 979 | -0.2% | -10.4 to 6.82 | STEADY, no difference beyond the noise |
| queries a second | 981 | 979 | -0.2% | -10.4 to 6.82 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.84 | 1.76 | -4.0% | -0.746 to 0.6 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.14 | 4.03 | -2.6% | -0.729 to 0.515 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.1 | 1.07 | -2.4% | -0.124 to 0.0705 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,235 | +141.2% | 702 to 744 | power given |
| pages holding data, mean (MB) | 455 | 888 | +95.2% | 407 to 459 | power given |
| pages read from disk into the pool (misses) | 191,690 | 71,520 | -62.7% | -127,474 to -112,867 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.159 | -3.2% | -0.0216 to 0.0111 | STEADY, no difference beyond the noise |
| host CPU-seconds | 297 | 287 | -3.2% | -38.3 to 19.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 94.4 | 60.4 | -35.9% | -67.2 to -0.663 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
