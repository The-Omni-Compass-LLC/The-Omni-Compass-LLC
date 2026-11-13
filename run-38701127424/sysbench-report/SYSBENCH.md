# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 287 | 288 | +0.2% | -6.75 to 7.94 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 291 | -0.2% | -10.9 to 9.93 | EVEN, no difference beyond the noise |
| queries a second | 4,668 | 4,660 | -0.2% | -174 to 159 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.6 | 4.42 | -4.1% | -1.64 to 1.26 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 193 | 11.1 | -94.2% | -939 to 576 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.41 | 3.02 | -52.8% | -18.1 to 11.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 312 | -39.0% | -513 to 114 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 443 | 256 | -42.3% | -390 to 14.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,465 | 368,465 | +51.3% | -86,619 to 336,619 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.174 | +2.5% | 0.000965 to 0.00769 | power given |
| host CPU-seconds | 104 | 106 | +2.7% | 0.99 to 4.65 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.39 | +2.4% | 0.0393 to 0.0726 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.3% | -1.71 to 3.25 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.3% | -1.67 to 3.17 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,727 | +0.3% | -26.8 to 50.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.18 | 4.1 | -1.8% | -0.258 to 0.11 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.6 | -2.4% | -0.425 to 0.155 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.21 | 3.2 | -0.5% | -0.0476 to 0.0124 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 456 | -10.9% | -146 to 34.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 413 | -10.7% | -139 to 40.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,695 | 807,256 | +23.7% | -183,894 to 493,016 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.194 | +0.8% | 0.000355 to 0.00274 | power given |
| host CPU-seconds | 319 | 322 | +1.0% | 1.03 to 5.29 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.39 | +0.7% | -0.00407 to 0.0389 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 8.35 to 24.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 194 | +0.6% | -4.37 to 6.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.4% | -2.44 to 0.959 | EVEN, no difference beyond the noise |
| queries a second | 3,950 | 3,935 | -0.4% | -48.9 to 19.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.64 | 5.95 | -10.3% | -3.36 to 1.99 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 20.4 | 13.4 | -34.4% | -30.7 to 16.7 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.37 | 3.24 | -3.9% | -1.31 to 1.05 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 441 | -13.9% | -231 to 88.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 389 | -15.8% | -175 to 29.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 617,340 | 863,672 | +39.9% | -164,831 to 657,495 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.139 | +4.8% | 0.00433 to 0.00824 | power given |
| host CPU-seconds | 236 | 247 | +4.8% | 7.48 to 14.9 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.68 | 2.79 | +4.1% | -0.0076 to 0.228 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 1.85 to 28.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,958 | -0.1% | -14.9 to 10.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,963 | -0.1% | -12.7 to 9.52 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,963 | -0.1% | -12.7 to 9.52 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.217 | 0.207 | -4.6% | -0.131 to 0.111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.351 | 0.346 | -1.2% | -0.0752 to 0.0666 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0966 | 0.0965 | -0.1% | -0.0307 to 0.0305 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 419 | -18.3% | -156 to -31.3 | GAIN |
| pages holding data, mean (MB) | 464 | 380 | -18.0% | -139 to -28.2 | GAIN |
| pages read from disk into the pool (misses) | 366,829 | 518,677 | +41.4% | 22,316 to 281,378 | shown, not judged |
| host CPU busy (share of the run) | 0.0759 | 0.0754 | -0.6% | -0.0266 to 0.0257 | EVEN, no difference beyond the noise |
| host CPU-seconds | 136 | 135 | -0.6% | -47.6 to 46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.101 | 0.1 | -0.5% | -0.0356 to 0.0345 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 5.43 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11.1 | 12.4 | +11.9% | -5.98 to 8.62 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 980 | 981 | +0.0% | -6.16 to 6.39 | EVEN, no difference beyond the noise |
| queries a second | 980 | 981 | +0.0% | -6.16 to 6.39 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.63 | 1.62 | -0.8% | -0.275 to 0.25 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 23.2 | 3 | -87.0% | -110 to 69.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.56 | 1.69 | -34.0% | -4.34 to 2.6 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 384 | -25.1% | -224 to -32.8 | GAIN |
| pages holding data, mean (MB) | 453 | 316 | -30.3% | -224 to -49.8 | GAIN |
| pages read from disk into the pool (misses) | 189,197 | 280,664 | +48.3% | 38,090 to 144,843 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.154 | +0.5% | -0.0154 to 0.0169 | EVEN, no difference beyond the noise |
| host CPU-seconds | 274 | 275 | +0.6% | -27.4 to 30.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 54.8 | 50.9 | -7.1% | -33.3 to 25.5 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 6.04 to 24 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
