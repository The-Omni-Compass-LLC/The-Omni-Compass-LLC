# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 291 | -0.7% | -7.25 to 2.88 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.5% | -7.22 to 4.41 | STEADY, no difference beyond the noise |
| queries a second | 4,712 | 4,689 | -0.5% | -116 to 70.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.1 | 5.25 | +3.0% | -0.186 to 0.489 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.13 | 7.57 | +6.1% | 0.31 to 0.567 | LOSS |
| latency, mean (ms) | 3.25 | 3.29 | +1.3% | -0.384 to 0.468 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 908 | +609.7% | 277 to 1,283 | power given |
| pages holding data, mean (MB) | 121 | 774 | +539.6% | 139 to 1,166 | power given |
| pages read from disk into the pool (misses) | 605,970 | 132,857 | -78.1% | -528,918 to -417,310 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.249 | +0.1% | -0.0282 to 0.0286 | STEADY, no difference beyond the noise |
| host CPU-seconds | 148 | 148 | +0.0% | -16.6 to 16.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.29 | 3.31 | +0.7% | -0.383 to 0.432 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.0% | -3.25 to 3.19 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.0% | -2.9 to 3 | STEADY, no difference beyond the noise |
| queries a second | 4,704 | 4,705 | +0.0% | -46.4 to 48.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.91 | 3.89 | -0.6% | -0.297 to 0.246 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.68 | 5.71 | +0.5% | -0.505 to 0.565 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.7 | 2.67 | -1.2% | -0.0903 to 0.0275 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 613 | +379.2% | 15.6 to 955 | power given |
| pages holding data, mean (MB) | 120 | 553 | +360.9% | 22.5 to 844 | power given |
| pages read from disk into the pool (misses) | 1,978,071 | 531,099 | -73.2% | -1,935,536 to -958,408 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.213 | -1.5% | -0.00477 to -0.00181 | GAIN |
| host CPU-seconds | 392 | 387 | -1.5% | -8.24 to -3.22 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.91 | 2.87 | -1.5% | -0.085 to -0.000323 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 2.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 113 | 131 | +15.2% | -2.33 to 36.7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.0% | -2.44 to 2.29 | STEADY, no difference beyond the noise |
| queries a second | 3,943 | 3,941 | -0.0% | -48.8 to 45.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 442 | 180 | -59.3% | -579 to 54.9 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 930 | 801 | -13.9% | -2,137 to 1,879 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 84.3 | 47.4 | -43.7% | -116 to 42.3 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,289 | +907.1% | 1,064 to 1,259 | power given |
| pages holding data, mean (MB) | 122 | 1,025 | +739.6% | 896 to 910 | power given |
| pages read from disk into the pool (misses) | 1,665,556 | 83,141 | -95.0% | -1,643,847 to -1,520,983 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.167 | -21.9% | -0.0557 to -0.0376 | GAIN |
| host CPU-seconds | 380 | 297 | -21.9% | -100 to -66.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 7.45 | 5.01 | -32.7% | -4.29 to -0.588 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 11.9 to 14.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 12.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,953 | +0.1% | -11.6 to 16.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,956 | +0.1% | -11 to 16.4 | STEADY, no difference beyond the noise |
| queries a second | 2,953 | 2,956 | +0.1% | -11 to 16.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.311 | 0.305 | -1.8% | -0.0342 to 0.0229 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.407 | 0.412 | +1.1% | -0.00537 to 0.0147 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.184 | -2.7% | -0.0196 to 0.00947 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 408 | +219.0% | 98.4 to 462 | power given |
| pages holding data, mean (MB) | 121 | 385 | +217.5% | 104 to 423 | power given |
| pages read from disk into the pool (misses) | 1,029,452 | 489,446 | -52.5% | -807,100 to -272,912 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.148 | -2.1% | -0.0143 to 0.00792 | STEADY, no difference beyond the noise |
| host CPU-seconds | 267 | 262 | -2.1% | -25 to 14 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.198 | 0.194 | -2.1% | -0.0195 to 0.011 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `e5cfa2afd8ec`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 169 | 212 | +25.3% | -7.5 to 93.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 989 | 988 | -0.0% | -6.94 to 6.47 | STEADY, no difference beyond the noise |
| queries a second | 989 | 988 | -0.0% | -6.94 to 6.47 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 66.1 | 31.8 | -51.8% | -304 to 235 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 218 | 162 | -25.7% | -682 to 570 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 11.4 | 7.02 | -38.5% | -41.1 to 32.3 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,271 | +892.6% | 1,053 to 1,232 | power given |
| pages holding data, mean (MB) | 118 | 884 | +648.4% | 760 to 771 | power given |
| pages read from disk into the pool (misses) | 418,743 | 71,024 | -83.0% | -363,569 to -331,868 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.143 | -13.9% | -0.0277 to -0.0186 | GAIN |
| host CPU-seconds | 291 | 251 | -13.9% | -48.8 to -32.3 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.93 | 2.64 | -32.8% | -2.88 to 0.306 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
