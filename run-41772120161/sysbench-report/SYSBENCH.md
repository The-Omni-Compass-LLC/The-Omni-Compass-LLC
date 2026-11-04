# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 291 | -0.8% | -10.5 to 5.57 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.5% | -9.18 to 6.19 | STEADY, no difference beyond the noise |
| queries a second | 4,724 | 4,701 | -0.5% | -147 to 99.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.25 | 5.37 | +2.4% | -0.365 to 0.619 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.39 | 7.89 | +6.8% | 0.273 to 0.739 | LOSS |
| latency, mean (ms) | 3.32 | 3.25 | -2.0% | -0.19 to 0.0574 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 978 | +664.0% | 443 to 1,256 | power given |
| pages holding data, mean (MB) | 121 | 846 | +598.9% | 434 to 1,015 | power given |
| pages read from disk into the pool (misses) | 606,111 | 111,211 | -81.7% | -508,435 to -481,365 | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.247 | -2.8% | -0.0181 to 0.00362 | STEADY, no difference beyond the noise |
| host CPU-seconds | 151 | 147 | -3.0% | -10.8 to 1.86 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.36 | 3.29 | -2.0% | -0.157 to 0.0209 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.1% | -1.58 to 2.42 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.2% | -0.886 to 2.26 | STEADY, no difference beyond the noise |
| queries a second | 4,705 | 4,716 | +0.2% | -14.2 to 36.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.4 | 3.32 | -2.4% | -0.254 to 0.0929 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.54 | 4.57 | +0.6% | -0.443 to 0.496 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.67 | 2.54 | -4.7% | -0.289 to 0.0363 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 674 | +426.7% | 177 to 915 | power given |
| pages holding data, mean (MB) | 120 | 582 | +385.5% | 196 to 728 | power given |
| pages read from disk into the pool (misses) | 1,967,387 | 428,338 | -78.2% | -2,037,565 to -1,040,533 | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.206 | -4.3% | -0.0168 to -0.00189 | GAIN |
| host CPU-seconds | 385 | 369 | -4.3% | -29.8 to -3.63 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.87 | 2.74 | -4.5% | -0.245 to -0.0116 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 195 | +0.6% | -2.01 to 4.42 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | -0.0% | -1.75 to 1.66 | STEADY, no difference beyond the noise |
| queries a second | 3,954 | 3,953 | -0.0% | -35.1 to 33.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 7 | 5.08 | -27.4% | -3.6 to -0.234 | GAIN |
| latency, 99th percentile (ms) | 20.5 | 11.7 | -42.8% | -33.6 to 16 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.46 | 2.96 | -14.6% | -0.647 to -0.362 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,216 | +850.0% | 997 to 1,179 | power given |
| pages holding data, mean (MB) | 121 | 1,003 | +729.3% | 837 to 928 | power given |
| pages read from disk into the pool (misses) | 1,668,277 | 131,346 | -92.1% | -1,572,694 to -1,501,168 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.128 | -13.7% | -0.0317 to -0.00879 | GAIN |
| host CPU-seconds | 264 | 228 | -13.6% | -55.6 to -16.1 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.98 | 2.56 | -14.2% | -0.599 to -0.246 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 1.55 to 16.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,963 | 2,965 | +0.1% | -5.07 to 8.81 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,966 | +0.0% | -5.86 to 8.74 | STEADY, no difference beyond the noise |
| queries a second | 2,964 | 2,966 | +0.0% | -5.86 to 8.74 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.213 | 0.228 | +7.2% | -0.0423 to 0.0729 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.361 | 0.363 | +0.6% | -0.00661 to 0.0106 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.14 | 0.14 | -0.4% | -0.00588 to 0.00464 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 168 | +31.0% | -131 to 210 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 160 | +31.9% | -128 to 205 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,030,077 | 937,868 | -9.0% | -482,591 to 298,173 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.112 | +0.6% | 0.000256 to 0.000984 | power given |
| host CPU-seconds | 197 | 199 | +0.6% | 0.3 to 1.96 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.146 | 0.147 | +0.5% | 0.000197 to 0.0013 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 237 | 289 | +21.9% | -51.9 to 156 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -7.88 to 5.51 | STEADY, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -7.88 to 5.51 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 29.9 | 32.3 | +8.3% | -75.1 to 80.1 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 176 | 152 | -13.8% | -372 to 324 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 7.91 | 6.74 | -14.9% | -16.7 to 14.3 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,300 | +915.6% | 1,160 to 1,184 | power given |
| pages holding data, mean (MB) | 118 | 884 | +648.8% | 759 to 773 | power given |
| pages read from disk into the pool (misses) | 419,290 | 70,851 | -83.1% | -361,635 to -335,244 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.133 | -16.9% | -0.0526 to -0.00164 | GAIN |
| host CPU-seconds | 281 | 233 | -16.8% | -92.2 to -2.34 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.68 | 1.78 | -33.6% | -2.48 to 0.676 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
