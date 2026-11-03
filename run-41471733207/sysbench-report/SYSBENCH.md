# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -3.44 to 1.63 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.0% | -2.67 to 2.47 | STEADY, no difference beyond the noise |
| queries a second | 4,703 | 4,702 | -0.0% | -42.7 to 39.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.06 | 4.97 | -1.9% | -0.688 to 0.5 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.92 | 7.34 | +6.1% | -0.0252 to 0.874 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.95 | 2.87 | -2.8% | -0.149 to -0.0162 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 849 | +563.2% | 19 to 1,423 | power given |
| pages holding data, mean (MB) | 121 | 721 | +496.3% | 163 to 1,037 | power given |
| pages read from disk into the pool (misses) | 611,583 | 149,677 | -75.5% | -610,274 to -313,540 | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.225 | -2.6% | -0.00983 to -0.00214 | GAIN |
| host CPU-seconds | 140 | 137 | -2.6% | -5.74 to -1.6 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 3.04 | -2.3% | -0.0923 to -0.0494 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.2% | -1.43 to 2.45 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -1.31 to 2.63 | STEADY, no difference beyond the noise |
| queries a second | 4,715 | 4,726 | +0.2% | -21 to 42.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.23 | 4.18 | -1.2% | -0.16 to 0.0583 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.21 | 6.21 | -0.0% | -0.278 to 0.276 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.16 | 3.09 | -2.3% | -0.173 to 0.0306 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 871 | +580.7% | 732 to 755 | power given |
| pages holding data, mean (MB) | 120 | 777 | +547.8% | 653 to 661 | power given |
| pages read from disk into the pool (misses) | 1,976,786 | 192,808 | -90.2% | -1,786,014 to -1,781,942 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.242 | -1.8% | -0.0143 to 0.00566 | STEADY, no difference beyond the noise |
| host CPU-seconds | 438 | 430 | -1.8% | -25.3 to 9.81 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.25 | 3.19 | -2.0% | -0.172 to 0.0453 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 0.427 to 13.6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 183 | 196 | +6.8% | 9.45 to 15.7 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.31 to 2.62 | STEADY, no difference beyond the noise |
| queries a second | 3,931 | 3,934 | +0.1% | -46.1 to 52.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 11.7 | 6.91 | -41.0% | -5.25 to -4.38 | GAIN |
| latency, 99th percentile (ms) | 16.2 | 9.28 | -42.8% | -7.41 to -6.46 | GAIN |
| latency, mean (ms) | 5.82 | 4.86 | -16.4% | -1.03 to -0.877 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 950 | +642.0% | 769 to 875 | power given |
| pages holding data, mean (MB) | 120 | 852 | +612.8% | 698 to 767 | power given |
| pages read from disk into the pool (misses) | 1,665,540 | 185,825 | -88.8% | -1,585,424 to -1,374,007 | shown, not judged |
| host CPU busy (share of the run) | 0.306 | 0.265 | -13.5% | -0.0531 to -0.0294 | GAIN |
| host CPU-seconds | 538 | 465 | -13.5% | -93.8 to -51.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.42 | 5.19 | -19.1% | -1.44 to -1.01 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 2.87 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,953 | 2,955 | +0.1% | -5.12 to 10 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,965 | +0.0% | -5.44 to 5.52 | STEADY, no difference beyond the noise |
| queries a second | 2,965 | 2,965 | +0.0% | -5.44 to 5.52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.25 | 0.23 | -8.0% | -0.0462 to 0.00617 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.367 | 0.365 | -0.6% | -0.0203 to 0.0156 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.345 | 0.239 | -30.8% | -0.23 to 0.0167 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,145 | +794.3% | 967 to 1,066 | power given |
| pages holding data, mean (MB) | 121 | 911 | +651.4% | 766 to 813 | power given |
| pages read from disk into the pool (misses) | 1,029,903 | 86,724 | -91.6% | -968,451 to -917,907 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.112 | -5.2% | -0.0185 to 0.00618 | STEADY, no difference beyond the noise |
| host CPU-seconds | 210 | 199 | -5.2% | -32.7 to 11 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.148 | -5.3% | -0.0241 to 0.00769 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 1.43 to 14.6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 5.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.21 | 5.6 | +74.4% | 0.581 to 4.19 | GAIN |
| throughput (transactions a second) | 982 | 982 | +0.0% | -2.97 to 3.13 | STEADY, no difference beyond the noise |
| queries a second | 982 | 982 | +0.0% | -2.97 to 3.13 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.94 | 1.68 | -13.7% | -0.608 to 0.075 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 38.8 | 5.71 | -85.3% | -176 to 110 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.61 | 1.58 | -39.3% | -4.27 to 2.21 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,283 | +902.3% | 1,082 to 1,227 | power given |
| pages holding data, mean (MB) | 118 | 880 | +644.3% | 754 to 769 | power given |
| pages read from disk into the pool (misses) | 415,434 | 70,963 | -82.9% | -359,527 to -329,415 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.166 | -10.3% | -0.0337 to -0.00457 | GAIN |
| host CPU-seconds | 335 | 300 | -10.4% | -60.7 to -8.91 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 240 | 121 | -49.9% | -253 to 13 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
