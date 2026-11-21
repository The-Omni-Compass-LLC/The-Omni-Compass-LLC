# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.2% | -9.06 to 7.85 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -9.45 to 8.58 | EVEN, no difference beyond the noise |
| queries a second | 4,708 | 4,701 | -0.1% | -151 to 137 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.34 | 5.41 | +1.2% | -0.0741 to 0.203 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.25 | +0.6% | -0.453 to 0.542 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.44 | 3.43 | -0.2% | -0.018 to 0.00478 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.7% | 13.1 to 14.4 | power given |
| pages holding data, mean (MB) | 120 | 139 | +15.5% | 10.8 to 26.6 | power given |
| pages read from disk into the pool (misses) | 585,367 | 530,171 | -9.4% | -98,911 to -11,480 | shown, not judged |
| host CPU busy (share of the run) | 0.205 | 0.206 | +0.2% | -0.00547 to 0.00626 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 114 | +0.2% | -2.85 to 3.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.53 | 2.55 | +0.5% | -0.0223 to 0.0456 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 294 | -0.5% | -4.29 to 1.43 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.5% | -4.2 to 1.36 | EVEN, no difference beyond the noise |
| queries a second | 4,738 | 4,715 | -0.5% | -67.2 to 21.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.2 | 4.18 | -0.6% | -0.134 to 0.0837 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.256 to 0.256 | EVEN, the same |
| latency, mean (ms) | 3.26 | 3.24 | -0.6% | -0.071 to 0.0293 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.6% | 9.45 to 10.1 | power given |
| pages holding data, mean (MB) | 120 | 136 | +13.0% | 12.5 to 18.7 | power given |
| pages read from disk into the pool (misses) | 1,994,148 | 1,900,649 | -4.7% | -205,393 to 18,395 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.201 | -1.2% | -0.00951 to 0.00458 | EVEN, no difference beyond the noise |
| host CPU-seconds | 339 | 335 | -1.2% | -15.8 to 7.44 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.5 | 2.49 | -0.7% | -0.0838 to 0.0473 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 8 to 8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 191 | -1.3% | -13.7 to 8.68 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.72 to 3.24 | EVEN, no difference beyond the noise |
| queries a second | 3,944 | 3,949 | +0.1% | -54.4 to 64.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.97 | 9.1 | +30.5% | -5.82 to 10.1 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 15.7 | 27.8 | +76.4% | -30.7 to 54.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.29 | 3.78 | +15.0% | -0.784 to 1.77 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.2% | 0.24 to 15.7 | power given |
| pages holding data, mean (MB) | 122 | 128 | +4.9% | -2.38 to 14.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,663,492 | 1,620,330 | -2.6% | -68,587 to -17,736 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.143 | +0.8% | -0.00806 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 253 | 255 | +0.8% | -14.3 to 18.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.87 | 2.93 | +2.1% | -0.0374 to 0.158 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,936 | 2,936 | -0.0% | -13.7 to 13.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,952 | -0.0% | -13.7 to 12.9 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,952 | -0.0% | -13.7 to 12.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.374 | 0.372 | -0.6% | -0.0124 to 0.00771 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.553 | 0.549 | -0.6% | -0.032 to 0.0254 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.225 | -1.3% | -0.00985 to 0.00401 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +8.2% | -1.64 to 22.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 133 | +10.0% | 0.907 to 23.3 | power given |
| pages read from disk into the pool (misses) | 1,029,474 | 997,579 | -3.1% | -78,108 to 14,318 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.118 | -1.1% | -0.00397 to 0.00135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 197 | -1.1% | -6.67 to 2.24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.147 | -1.1% | -0.00501 to 0.00172 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 0.929 to 12.4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 5.53 | 4.42 | -20.2% | -3.81 to 1.57 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 982 | -0.1% | -1.72 to -0.207 | LOSS |
| queries a second | 983 | 982 | -0.1% | -1.72 to -0.207 | LOSS |
| latency, 95th percentile (ms) | 2.09 | 2.31 | +10.6% | -0.457 to 0.901 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.66 | 4.3 | +17.4% | -1.54 to 2.82 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.2 | +4.2% | -0.173 to 0.269 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.7% | 6.34 to 16 | power given |
| pages holding data, mean (MB) | 119 | 125 | +5.2% | 2.28 to 10.2 | power given |
| pages read from disk into the pool (misses) | 415,332 | 407,988 | -1.8% | -19,763 to 5,074 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.301 | +52.7% | -0.0174 to 0.225 | EVEN, no difference beyond the noise |
| host CPU-seconds | 305 | 469 | +53.6% | -24.6 to 352 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 169 | 274 | +62.0% | 69 to 141 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 8 to 8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
