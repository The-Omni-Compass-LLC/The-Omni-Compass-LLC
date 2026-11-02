# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.3% | -6.9 to 8.45 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.3% | -6.47 to 8.17 | STEADY, no difference beyond the noise |
| queries a second | 4,681 | 4,694 | +0.3% | -104 to 131 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.1 | 4.13 | +0.6% | -0.256 to 0.302 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.71 | -0.6% | -0.426 to 0.354 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.67 | 2.66 | -0.6% | -0.0533 to 0.0224 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 678 | +32.5% | 22.5 to 310 | power given |
| pages holding data, mean (MB) | 452 | 611 | +35.4% | 26.8 to 293 | power given |
| pages read from disk into the pool (misses) | 247,307 | 190,215 | -23.1% | -110,272 to -3,913 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.213 | -0.4% | -0.00925 to 0.00769 | STEADY, no difference beyond the noise |
| host CPU-seconds | 128 | 128 | -0.5% | -5.61 to 4.24 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.87 | 2.85 | -0.7% | -0.0602 to 0.0224 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 291 | -0.3% | -2.16 to 0.69 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.3% | -4.05 to 2.54 | STEADY, no difference beyond the noise |
| queries a second | 4,744 | 4,732 | -0.3% | -64.8 to 40.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.13 | 2.83 | -9.7% | -0.517 to -0.0917 | GAIN |
| latency, 99th percentile (ms) | 23.1 | 22.4 | -2.9% | -29.5 to 28.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.11 | 2.86 | -7.9% | -0.862 to 0.372 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,186 | +131.7% | 452 to 897 | power given |
| pages holding data, mean (MB) | 465 | 948 | +104.0% | 427 to 540 | power given |
| pages read from disk into the pool (misses) | 657,257 | 83,014 | -87.4% | -595,454 to -553,031 | shown, not judged |
| host CPU busy (share of the run) | 0.174 | 0.165 | -5.4% | -0.0138 to -0.00507 | GAIN |
| host CPU-seconds | 312 | 295 | -5.4% | -24.8 to -9.11 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.22 | -5.2% | -0.178 to -0.0649 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 5.43 to 18.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 7.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 197 | +1.8% | 2.21 to 4.7 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.1% | -0.119 to 0.44 | STEADY, no difference beyond the noise |
| queries a second | 3,936 | 3,940 | +0.1% | -2.38 to 8.81 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.04 | 6.28 | -21.9% | -2.7 to -0.823 | GAIN |
| latency, 99th percentile (ms) | 12 | 8.08 | -32.7% | -4.95 to -2.92 | GAIN |
| latency, mean (ms) | 4.95 | 4.57 | -7.6% | -0.555 to -0.201 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 993 | +94.0% | 402 to 561 | power given |
| pages holding data, mean (MB) | 461 | 888 | +92.6% | 340 to 514 | power given |
| pages read from disk into the pool (misses) | 617,724 | 138,104 | -77.6% | -519,980 to -439,260 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.249 | -7.2% | -0.0205 to -0.0179 | GAIN |
| host CPU-seconds | 472 | 438 | -7.2% | -36.2 to -31.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.33 | 4.86 | -8.8% | -0.533 to -0.408 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,913 | 2,910 | -0.1% | -34.3 to 29.7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,953 | +0.0% | -6.69 to 8.17 | STEADY, no difference beyond the noise |
| queries a second | 2,952 | 2,953 | +0.0% | -6.69 to 8.17 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.44 | 0.443 | +0.6% | -0.0474 to 0.0527 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.663 | 0.669 | +1.0% | -0.104 to 0.116 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.25 | 0.25 | -0.2% | -0.00358 to 0.00255 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 540 | +5.5% | -93.5 to 150 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 488 | +5.2% | -75.3 to 124 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,929 | 342,260 | -7.0% | -136,447 to 85,110 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.194 | -0.2% | -0.00128 to 0.000669 | STEADY, no difference beyond the noise |
| host CPU-seconds | 341 | 341 | -0.2% | -2.56 to 1.36 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.256 | 0.256 | -0.1% | -0.00216 to 0.00177 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 10.7 | 13.4 | +25.6% | -2.97 to 8.43 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -5.46 to 3.7 | STEADY, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -5.46 to 3.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.85 | 1.75 | -5.5% | -0.498 to 0.293 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.85 | 5.79 | -1.0% | -0.916 to 0.796 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.13 | -2.0% | -0.134 to 0.087 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 702 to 746 | power given |
| pages holding data, mean (MB) | 460 | 888 | +93.1% | 413 to 443 | power given |
| pages read from disk into the pool (misses) | 186,090 | 71,492 | -61.6% | -136,558 to -92,638 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.223 | -3.1% | -0.0379 to 0.0238 | STEADY, no difference beyond the noise |
| host CPU-seconds | 404 | 392 | -3.0% | -65.6 to 41.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 87.2 | 64.6 | -25.9% | -89 to 43.8 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
