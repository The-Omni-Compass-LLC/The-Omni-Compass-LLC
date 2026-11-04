# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.1% | -4.69 to 5.42 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.0% | -4.15 to 4.2 | STEADY, no difference beyond the noise |
| queries a second | 4,689 | 4,690 | +0.0% | -66.5 to 67.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.03 | 4.94 | -1.9% | -0.539 to 0.353 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.17 | 6.92 | -3.4% | -1.4 to 0.903 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.29 | 3.27 | -0.7% | -0.207 to 0.158 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 813 | +58.9% | 45.3 to 558 | power given |
| pages holding data, mean (MB) | 455 | 736 | +61.8% | 56.5 to 505 | power given |
| pages read from disk into the pool (misses) | 246,079 | 153,053 | -37.8% | -161,342 to -24,710 | shown, not judged |
| host CPU busy (share of the run) | 0.255 | 0.255 | -0.0% | -0.0142 to 0.0141 | STEADY, no difference beyond the noise |
| host CPU-seconds | 151 | 151 | +0.0% | -8.23 to 8.24 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.39 | 3.38 | -0.1% | -0.158 to 0.151 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 295 | -0.2% | -1.19 to -0.135 | LOSS |
| throughput (transactions a second) | 296 | 295 | -0.3% | -1.41 to -0.0706 | LOSS |
| queries a second | 4,734 | 4,722 | -0.3% | -22.6 to -1.13 | LOSS |
| latency, 95th percentile (ms) | 4.05 | 4.05 | +0.0% | -0.181 to 0.181 | STEADY, the same |
| latency, 99th percentile (ms) | 5.5 | 5.47 | -0.6% | -0.177 to 0.11 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.1 | 3.08 | -0.6% | -0.147 to 0.108 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 605 | +18.2% | -150 to 337 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 545 | +17.6% | -146 to 309 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,851 | 499,899 | -23.9% | -543,648 to 229,744 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.244 | -0.9% | -0.0105 to 0.00593 | STEADY, no difference beyond the noise |
| host CPU-seconds | 438 | 434 | -0.9% | -18.5 to 10.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.24 | 3.22 | -0.7% | -0.127 to 0.0823 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | -1.48 to 3.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 195 | +1.7% | -0.209 to 6.56 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.5% | -3.34 to 1.34 | STEADY, no difference beyond the noise |
| queries a second | 3,937 | 3,917 | -0.5% | -66.9 to 26.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.63 | 6.79 | -21.4% | -2.29 to -1.4 | GAIN |
| latency, 99th percentile (ms) | 12.8 | 8.69 | -32.3% | -5.26 to -3.03 | GAIN |
| latency, mean (ms) | 5.2 | 4.85 | -6.8% | -0.435 to -0.27 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,025 | +100.2% | 396 to 630 | power given |
| pages holding data, mean (MB) | 462 | 914 | +97.5% | 336 to 566 | power given |
| pages read from disk into the pool (misses) | 618,992 | 122,527 | -80.2% | -517,507 to -475,423 | shown, not judged |
| host CPU busy (share of the run) | 0.278 | 0.259 | -6.8% | -0.028 to -0.00952 | GAIN |
| host CPU-seconds | 489 | 456 | -6.8% | -49.1 to -17.4 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.55 | 5.09 | -8.3% | -0.562 to -0.363 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,947 | +0.0% | -9.34 to 10.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% | -8.08 to 8.36 | STEADY, no difference beyond the noise |
| queries a second | 2,953 | 2,953 | +0.0% | -8.08 to 8.36 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.303 | 0.308 | +1.8% | -0.00835 to 0.019 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.459 | 0.456 | -0.6% | -0.0141 to 0.00881 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.205 | 0.191 | -6.8% | -0.0809 to 0.0533 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -17.5 to 10.9 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,464 | 366,289 | -0.6% | -10,686 to 6,336 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.156 | +1.8% | -0.00158 to 0.00712 | STEADY, no difference beyond the noise |
| host CPU-seconds | 270 | 275 | +1.8% | -2.83 to 12.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.2 | 0.204 | +1.8% | -0.00252 to 0.00973 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 213 | 235 | +10.2% | -70.6 to 114 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | +0.0% | -3.96 to 4.89 | STEADY, no difference beyond the noise |
| queries a second | 988 | 988 | +0.0% | -3.96 to 4.89 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.65 | 5.05 | +8.5% | -3.3 to 4.09 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.1 | 15.3 | +8.3% | -7.71 to 10.1 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.46 | 1.48 | +0.8% | -0.603 to 0.628 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,234 | +141.1% | 711 to 733 | power given |
| pages holding data, mean (MB) | 455 | 890 | +95.6% | 409 to 461 | power given |
| pages read from disk into the pool (misses) | 190,104 | 71,340 | -62.5% | -130,294 to -107,234 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.112 | -3.4% | -0.0261 to 0.0183 | STEADY, no difference beyond the noise |
| host CPU-seconds | 204 | 198 | -3.3% | -45.7 to 32.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.23 | 1.87 | -16.0% | -1.92 to 1.2 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
