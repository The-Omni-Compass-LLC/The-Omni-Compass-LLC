# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 290 | -0.7% | -4.99 to 0.652 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.2% | -4.45 to 5.37 | EVEN, no difference beyond the noise |
| queries a second | 4,737 | 4,745 | +0.2% | -71.3 to 86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 4.2 | +4.9% | -0.181 to 0.574 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 15.6 | 34.3 | +119.8% | -35.4 to 72.7 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.81 | 3.16 | +12.4% | -1.39 to 2.09 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.7% | 6.89 to 7.83 | power given |
| pages holding data, mean (MB) | 120 | 131 | +8.8% | 6.09 to 14.9 | power given |
| pages read from disk into the pool (misses) | 580,654 | 557,572 | -4.0% | -95,524 to 49,362 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.169 | +0.7% | -0.00508 to 0.00757 | EVEN, no difference beyond the noise |
| host CPU-seconds | 100 | 101 | +0.8% | -3.01 to 4.57 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.24 | 2.28 | +1.5% | -0.0562 to 0.125 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.3% | -0.6 to 2.45 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -1.18 to 2.81 | EVEN, no difference beyond the noise |
| queries a second | 4,738 | 4,751 | +0.3% | -18.9 to 45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.84 | 1.85 | +0.6% | -0.282 to 0.304 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.64 | 3.64 | +0.1% | -0.323 to 0.328 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.27 | -0.5% | -0.208 to 0.196 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 133 | +3.9% | -1.21 to 11.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 131 | +9.1% | -2.3 to 24.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,995,560 | 2,015,127 | +1.0% | -191,860 to 230,994 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.101 | +0.5% | -0.0148 to 0.0158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 181 | 182 | +0.5% | -26.4 to 28.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.34 | 1.34 | +0.2% | -0.201 to 0.206 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 179 | 179 | -0.1% | -4.56 to 4.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.2% | -3.11 to 3.96 | EVEN, no difference beyond the noise |
| queries a second | 3,919 | 3,928 | +0.2% | -62.2 to 79.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.8 | 12.9 | +1.2% | -0.179 to 0.491 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 17.8 | 18.3 | +2.5% | -0.506 to 1.38 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.24 | 6.31 | +1.0% | -0.0436 to 0.164 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 143 | +11.5% | 4.89 to 24.5 | power given |
| pages holding data, mean (MB) | 121 | 133 | +9.9% | 0.0332 to 23.9 | power given |
| pages read from disk into the pool (misses) | 1,662,865 | 1,587,322 | -4.5% | -103,467 to -47,618 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.249 | +0.7% | -0.0115 to 0.015 | EVEN, no difference beyond the noise |
| host CPU-seconds | 399 | 402 | +0.8% | -17.1 to 23.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.86 | 4.91 | +0.9% | -0.249 to 0.334 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,944 | 2,944 | +0.0% | -1 to 2.25 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,953 | +0.0% | -1.02 to 3.08 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,953 | +0.0% | -1.02 to 3.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.346 | 0.344 | -0.6% | -0.033 to 0.029 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.467 | 0.467 | +0.1% | -0.0355 to 0.0362 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.207 | -0.4% | -0.0183 to 0.0167 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.8% | -10.4 to 32.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 136 | +12.1% | -5.89 to 35.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,028,813 | 999,144 | -2.9% | -70,488 to 11,150 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.11 | -0.7% | -0.0153 to 0.0138 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 183 | -0.8% | -25.6 to 22.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.137 | 0.136 | -0.8% | -0.019 to 0.0168 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.41 | 4.39 | -0.4% | -4.61 to 4.57 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 985 | +0.1% | -5.45 to 7.97 | EVEN, no difference beyond the noise |
| queries a second | 984 | 985 | +0.1% | -5.45 to 7.97 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.53 | 2.53 | -0.0% | -0.852 to 0.85 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.55 | 4.46 | -2.0% | -1.72 to 1.54 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.26 | 1.26 | +0.3% | -0.254 to 0.26 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 141 | +10.2% | 4.11 to 22 | power given |
| pages holding data, mean (MB) | 119 | 126 | +6.5% | 1.46 to 13.9 | power given |
| pages read from disk into the pool (misses) | 415,847 | 408,415 | -1.8% | -10,383 to -4,480 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.245 | +25.7% | -0.0852 to 0.185 | EVEN, no difference beyond the noise |
| host CPU-seconds | 301 | 379 | +26.0% | -133 to 289 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 446 | 210 | -52.8% | -1,546 to 1,076 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
