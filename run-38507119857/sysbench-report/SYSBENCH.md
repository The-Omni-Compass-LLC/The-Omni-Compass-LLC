# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 273 | 272 | -0.3% | -12.8 to 11.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.0% | -3.22 to 3.02 | EVEN, no difference beyond the noise |
| queries a second | 4,734 | 4,732 | -0.0% | -51.5 to 48.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 41.9 | 50.3 | +20.1% | -119 to 136 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 286 | 308 | +7.8% | -1,107 to 1,151 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 11.1 | 12.2 | +9.3% | -30.8 to 32.9 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 346 | -32.4% | -336 to 3.85 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 297 | -33.6% | -298 to -2.58 | GAIN |
| pages read from disk into the pool (misses) | 247,150 | 317,887 | +28.6% | -9,939 to 151,413 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.167 | +1.5% | -0.00188 to 0.00671 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.5 | 100 | +1.5% | -1.18 to 4.16 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.41 | +1.7% | -0.104 to 0.185 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.7 to 12.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.2% | -4.33 to 5.38 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.2% | -4.3 to 5.4 | EVEN, no difference beyond the noise |
| queries a second | 4,700 | 4,709 | +0.2% | -68.9 to 86.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.45 | 2.42 | -1.2% | -0.152 to 0.0947 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.86 | 3.84 | -0.6% | -0.12 to 0.0749 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.79 | 1.78 | -0.8% | -0.12 to 0.0907 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 375 | -26.7% | -238 to -35.3 | GAIN |
| pages holding data, mean (MB) | 461 | 348 | -24.6% | -200 to -26.8 | GAIN |
| pages read from disk into the pool (misses) | 654,443 | 1,047,640 | +60.1% | -17,500 to 803,894 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.142 | -0.6% | -0.00805 to 0.0064 | EVEN, no difference beyond the noise |
| host CPU-seconds | 259 | 258 | -0.6% | -14.5 to 11.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.92 | 1.91 | -0.8% | -0.128 to 0.0987 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 0.99 to 21.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 120 | 118 | -2.0% | -21.6 to 16.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -1.98 to 2.25 | EVEN, no difference beyond the noise |
| queries a second | 3,933 | 3,936 | +0.1% | -39.6 to 45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 348 | 347 | -0.1% | -335 to 334 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,572 | 1,006 | -36.0% | -4,985 to 3,852 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 83.6 | 70.9 | -15.2% | -131 to 106 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 482 | -5.8% | -115 to 55.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 460 | 436 | -5.3% | -89.6 to 40.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,119 | 692,311 | +12.4% | -143,157 to 295,540 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.194 | +1.4% | -0.00413 to 0.00932 | EVEN, no difference beyond the noise |
| host CPU-seconds | 341 | 346 | +1.4% | -8.1 to 17.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.24 | 6.47 | +3.7% | -1.01 to 1.48 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.7 |  | 16.9 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,943 | 2,945 | +0.0% | -5.1 to 7.67 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,954 | +0.0% | -4.81 to 4.99 | EVEN, no difference beyond the noise |
| queries a second | 2,954 | 2,954 | +0.0% | -4.81 to 4.99 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.324 | +1.9% | -0.00891 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.517 | 0.508 | -1.8% | -0.0329 to 0.0143 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.2 | +0.6% | -0.00419 to 0.00643 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 456 | -10.9% | -120 to 8.83 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 418 | -10.0% | -110 to 17.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,788 | 433,294 | +17.8% | -46,768 to 177,779 | shown, not judged |
| host CPU busy (share of the run) | 0.0955 | 0.0969 | +1.5% | -0.00632 to 0.00913 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 161 | +1.6% | -10.4 to 15.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.118 | 0.119 | +1.5% | -0.00787 to 0.0115 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 4.87 to 12.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7.73 | 6.01 | -22.3% | -3.88 to 0.431 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 984 | +0.1% | -2.98 to 4.66 | EVEN, no difference beyond the noise |
| queries a second | 983 | 984 | +0.1% | -2.98 to 4.66 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.67 | 1.71 | +2.8% | -0.356 to 0.45 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.82 | 2.7 | -4.2% | -0.756 to 0.52 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.07 | +2.5% | -0.133 to 0.185 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 482 | -5.9% | -98.6 to 37.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 407 | -10.2% | -115 to 22.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,694 | 218,629 | +15.3% | 5,870 to 51,999 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.167 | +36.1% | -0.0414 to 0.13 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 258 | +36.2% | -64.3 to 201 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 76.4 | 403 | +428.2% | -1,006 to 1,660 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 25.3 |  | 6.36 to 44.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
