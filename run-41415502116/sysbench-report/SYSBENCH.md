# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 288 | 288 | -0.3% | -7.55 to 6.03 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 293 | -0.7% | -7.4 to 3.39 | STEADY, no difference beyond the noise |
| queries a second | 4,724 | 4,692 | -0.7% | -118 to 54.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.25 | 6.11 | -2.3% | -0.272 to -0.0191 | GAIN |
| latency, 99th percentile (ms) | 10.9 | 10.5 | -2.8% | -5.52 to 4.9 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.86 | 4.36 | +13.1% | -2.25 to 3.26 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,041 | +103.4% | 240 to 818 | power given |
| pages holding data, mean (MB) | 457 | 921 | +101.5% | 254 to 674 | power given |
| pages read from disk into the pool (misses) | 249,435 | 97,902 | -60.8% | -214,489 to -88,576 | shown, not judged |
| host CPU busy (share of the run) | 0.276 | 0.272 | -1.4% | -0.0143 to 0.00648 | STEADY, no difference beyond the noise |
| host CPU-seconds | 164 | 162 | -1.4% | -8.68 to 4.09 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.71 | 3.67 | -1.1% | -0.265 to 0.182 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -0.101 to 2.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.2% | -2.81 to 3.73 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.1% | -2.73 to 3.58 | STEADY, no difference beyond the noise |
| queries a second | 4,722 | 4,729 | +0.1% | -43.6 to 57.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.96 | 3.89 | -1.8% | -0.422 to 0.281 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.34 | 5.25 | -1.8% | -0.505 to 0.316 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.03 | 2.99 | -1.3% | -0.315 to 0.236 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 631 | +23.2% | -140 to 378 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 569 | +23.2% | -115 to 329 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,576 | 471,980 | -27.8% | -587,896 to 224,704 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.238 | -0.8% | -0.0205 to 0.0167 | STEADY, no difference beyond the noise |
| host CPU-seconds | 426 | 423 | -0.7% | -35.7 to 29.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.16 | 3.13 | -0.9% | -0.298 to 0.24 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -1.54 to 4.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 195 | +0.2% | -6.39 to 7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.0% | -4.84 to 4.74 | STEADY, no difference beyond the noise |
| queries a second | 3,928 | 3,927 | -0.0% | -96.9 to 94.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.59 | 5.04 | -23.6% | -2.64 to -0.472 | GAIN |
| latency, 99th percentile (ms) | 11.2 | 9.5 | -15.1% | -10.4 to 6.99 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.79 | 3.52 | -7.1% | -0.486 to -0.0555 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,205 | +135.4% | 639 to 748 | power given |
| pages holding data, mean (MB) | 463 | 1,012 | +118.5% | 522 to 576 | power given |
| pages read from disk into the pool (misses) | 620,349 | 109,475 | -82.4% | -598,979 to -422,768 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.171 | -7.6% | -0.0175 to -0.0105 | GAIN |
| host CPU-seconds | 336 | 310 | -7.6% | -31.7 to -19.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.76 | 3.47 | -7.7% | -0.444 to -0.138 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | -0.573 to 12.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,947 | -0.0% | -3.95 to 3.57 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,954 | +0.0% | -5.35 to 6.2 | STEADY, no difference beyond the noise |
| queries a second | 2,953 | 2,954 | +0.0% | -5.35 to 6.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.307 | 0.307 | +0.0% | -0.0371 to 0.0371 | STEADY, the same |
| latency, 99th percentile (ms) | 0.448 | 0.453 | +1.2% | -0.0176 to 0.0283 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.191 | +1.0% | -0.00957 to 0.0134 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -17.9 to 11.1 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,879 | 366,451 | -0.4% | -12,993 to 10,136 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.155 | +0.8% | -0.00683 to 0.00932 | STEADY, no difference beyond the noise |
| host CPU-seconds | 270 | 272 | +0.8% | -11.8 to 16.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.2 | 0.202 | +0.8% | -0.00856 to 0.0118 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `4b160a642eb2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 23.3 | 21.5 | -7.7% | -13.5 to 9.94 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | +0.0% | -4.91 to 5.07 | STEADY, no difference beyond the noise |
| queries a second | 983 | 983 | +0.0% | -4.91 to 5.07 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.66 | 1.67 | +0.3% | -0.31 to 0.319 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.7 | 2.75 | +1.7% | -0.403 to 0.496 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.01 | 1 | -1.1% | -0.0751 to 0.0532 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,230 | +140.2% | 677 to 758 | power given |
| pages holding data, mean (MB) | 457 | 888 | +94.1% | 412 to 449 | power given |
| pages read from disk into the pool (misses) | 192,385 | 71,745 | -62.7% | -127,250 to -114,031 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.231 | -1.1% | -0.0357 to 0.0305 | STEADY, no difference beyond the noise |
| host CPU-seconds | 409 | 405 | -1.1% | -61.5 to 52.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 40.5 | 41.6 | +2.9% | -27.1 to 29.5 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
