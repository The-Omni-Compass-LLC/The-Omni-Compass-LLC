# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.1% | -1.95 to 2.37 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.1% | -1.4 to 1.98 | STEADY, no difference beyond the noise |
| queries a second | 4,682 | 4,687 | +0.1% | -22.4 to 31.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.97 | 4.88 | -1.8% | -0.0949 to -0.0824 | GAIN |
| latency, 99th percentile (ms) | 7.08 | 7.04 | -0.6% | -0.407 to 0.323 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.19 | 3.17 | -0.6% | -0.0934 to 0.0567 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 745 | +45.5% | 91.6 to 374 | power given |
| pages holding data, mean (MB) | 451 | 672 | +48.9% | 90.6 to 351 | power given |
| pages read from disk into the pool (misses) | 245,006 | 170,897 | -30.2% | -116,482 to -31,736 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.245 | -0.3% | -0.00488 to 0.00364 | STEADY, no difference beyond the noise |
| host CPU-seconds | 146 | 145 | -0.3% | -2.97 to 2.17 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.27 | 3.26 | -0.3% | -0.0721 to 0.0501 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.3% | -3.19 to 1.33 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.3% | -3.11 to 1.29 | STEADY, no difference beyond the noise |
| queries a second | 4,750 | 4,735 | -0.3% | -49.7 to 20.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.75 | 1.77 | +1.0% | -0.305 to 0.341 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.54 | 3.64 | +2.9% | -0.55 to 0.754 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.2 | -0.4% | -0.217 to 0.206 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 599 | +17.0% | -287 to 460 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 537 | +16.3% | -266 to 417 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 657,388 | 573,600 | -12.7% | -410,600 to 243,024 | shown, not judged |
| host CPU busy (share of the run) | 0.0965 | 0.0956 | -1.0% | -0.0179 to 0.0161 | STEADY, no difference beyond the noise |
| host CPU-seconds | 174 | 172 | -1.0% | -32.3 to 29 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.28 | 1.28 | -0.6% | -0.244 to 0.227 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 194 | +0.9% | -5.5 to 9.11 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.1% | -3.44 to 3.97 | STEADY, no difference beyond the noise |
| queries a second | 3,945 | 3,951 | +0.1% | -68.8 to 79.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.71 | 5.34 | -20.5% | -6.77 to 4.01 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 27.3 | 14.2 | -47.9% | -52.3 to 26.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.56 | 2.88 | -19.1% | -1.28 to -0.0861 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,184 | +131.2% | 640 to 703 | power given |
| pages holding data, mean (MB) | 462 | 988 | +113.7% | 508 to 543 | power given |
| pages read from disk into the pool (misses) | 618,034 | 127,022 | -79.4% | -517,649 to -464,376 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.122 | -8.2% | -0.0145 to -0.00725 | GAIN |
| host CPU-seconds | 236 | 217 | -8.2% | -25.7 to -13.1 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.7 | 2.46 | -9.1% | -0.327 to -0.165 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 2.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,943 | +0.0% | -9.69 to 10.9 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,963 | 2,968 | +0.2% | -9.05 to 18.7 | STEADY, no difference beyond the noise |
| queries a second | 2,963 | 2,968 | +0.2% | -9.05 to 18.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.25 | 0.232 | -7.5% | -0.0526 to 0.0152 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.543 | 3.7 | +581.2% | -10.4 to 16.7 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.595 | 0.724 | +21.7% | -0.376 to 0.634 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,160 | +126.6% | 605 to 691 | power given |
| pages holding data, mean (MB) | 464 | 927 | +99.9% | 434 to 493 | power given |
| pages read from disk into the pool (misses) | 365,860 | 76,967 | -79.0% | -303,451 to -274,335 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.115 | -1.5% | -0.0085 to 0.00499 | STEADY, no difference beyond the noise |
| host CPU-seconds | 208 | 205 | -1.6% | -15.4 to 8.75 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.155 | 0.153 | -1.5% | -0.0111 to 0.00639 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 6.23 to 9.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 7.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 25.6 | 30.2 | +17.8% | -5.14 to 14.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.1% | -5.23 to 2.96 | STEADY, no difference beyond the noise |
| queries a second | 985 | 984 | -0.1% | -5.23 to 2.96 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.72 | 1.66 | -3.7% | -0.353 to 0.224 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.91 | 3.88 | -0.6% | -0.126 to 0.0782 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.02 | 1 | -1.7% | -0.0838 to 0.0481 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 703 to 744 | power given |
| pages holding data, mean (MB) | 457 | 888 | +94.4% | 409 to 454 | power given |
| pages read from disk into the pool (misses) | 192,818 | 71,401 | -63.0% | -130,316 to -112,519 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.215 | -2.6% | -0.0332 to 0.0216 | STEADY, no difference beyond the noise |
| host CPU-seconds | 386 | 376 | -2.6% | -57.5 to 37.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 34.9 | 27.4 | -21.4% | -31.2 to 16.2 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
