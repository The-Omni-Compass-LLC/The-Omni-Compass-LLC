# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.3% | -3.15 to 5.12 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.3% | -3.34 to 5.26 | EVEN, no difference beyond the noise |
| queries a second | 4,694 | 4,710 | +0.3% | -53.4 to 84.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.41 | 5.41 | +0.0% | -0.241 to 0.241 | EVEN, the same |
| latency, 99th percentile (ms) | 7.34 | 7.34 | -0.0% | -0.328 to 0.326 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.44 | 3.44 | -0.1% | -0.103 to 0.0992 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 146 | +14.1% | -1.14 to 37.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 141 | +17.2% | 6.49 to 34.9 | power given |
| pages read from disk into the pool (misses) | 580,471 | 528,125 | -9.0% | -178,365 to 73,673 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.207 | +1.3% | -0.0101 to 0.0154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 115 | +1.4% | -5.74 to 8.88 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.53 | 2.55 | +1.0% | -0.132 to 0.181 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -5 to 3.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.3% | -4.86 to 2.95 | EVEN, no difference beyond the noise |
| queries a second | 4,734 | 4,719 | -0.3% | -77.8 to 47.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.33 | 4.3 | -0.6% | -0.32 to 0.268 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.32 | 6.28 | -0.6% | -0.2 to 0.124 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.29 | 3.25 | -1.2% | -0.138 to 0.0583 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.5% | 4.82 to 11.7 | power given |
| pages holding data, mean (MB) | 120 | 135 | +12.2% | 10.5 to 18.9 | power given |
| pages read from disk into the pool (misses) | 1,996,380 | 1,919,358 | -3.9% | -170,145 to 16,102 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.199 | -2.0% | -0.0146 to 0.00656 | EVEN, no difference beyond the noise |
| host CPU-seconds | 338 | 331 | -2.0% | -24.6 to 11 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.5 | 2.46 | -1.7% | -0.143 to 0.0573 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 180 | 179 | -0.3% | -4.39 to 3.17 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.1% | -1.13 to 0.779 | EVEN, no difference beyond the noise |
| queries a second | 3,931 | 3,928 | -0.1% | -22.5 to 15.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.7 | 12.8 | +1.2% | -0.723 to 1.03 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 18.9 | 18.8 | -0.0% | -4.47 to 4.46 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.51 | 6.87 | +5.6% | -1.42 to 2.15 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 145 | +13.3% | 12 to 22.1 | power given |
| pages holding data, mean (MB) | 121 | 137 | +12.9% | 8.85 to 22.4 | power given |
| pages read from disk into the pool (misses) | 1,668,342 | 1,579,428 | -5.3% | -149,991 to -27,838 | shown, not judged |
| host CPU busy (share of the run) | 0.252 | 0.254 | +0.6% | -0.00464 to 0.00754 | EVEN, no difference beyond the noise |
| host CPU-seconds | 407 | 410 | +0.7% | -6.21 to 11.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.95 | 5 | +1.0% | -0.135 to 0.232 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.7 |  | 10.2 to 13.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,961 | +0.0% | -15.4 to 15.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,966 | +0.0% | -12.3 to 12.4 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,966 | +0.0% | -12.3 to 12.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.17 | 0.178 | +4.7% | -0.145 to 0.161 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.307 | 0.296 | -3.8% | -0.0737 to 0.0504 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0847 | 0.082 | -3.2% | -0.0299 to 0.0245 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 133 | +3.9% | -0.972 to 10.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 130 | +7.1% | 3.77 to 13.5 | power given |
| pages read from disk into the pool (misses) | 1,029,919 | 1,015,856 | -1.4% | -35,913 to 7,787 | shown, not judged |
| host CPU busy (share of the run) | 0.0651 | 0.0632 | -2.9% | -0.0243 to 0.0205 | EVEN, no difference beyond the noise |
| host CPU-seconds | 117 | 113 | -2.9% | -43.4 to 36.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0867 | 0.0842 | -2.9% | -0.0324 to 0.0273 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 159 | 160 | +0.9% | -48.2 to 51 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -4.05 to 1.76 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -4.05 to 1.76 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.41 | 2.19 | -9.3% | -1.35 to 0.9 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.05 | 6.26 | -11.2% | -13.2 to 11.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.89 | 1.1 | -41.9% | -4.46 to 2.87 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.8% | -4.72 to 19.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 118 | 123 | +4.2% | -3.32 to 13.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 415,427 | 410,068 | -1.3% | -20,333 to 9,616 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.138 | -1.1% | -0.012 to 0.00884 | EVEN, no difference beyond the noise |
| host CPU-seconds | 246 | 243 | -1.1% | -21.4 to 15.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.46 | 3.35 | -3.4% | -1.31 to 1.08 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
