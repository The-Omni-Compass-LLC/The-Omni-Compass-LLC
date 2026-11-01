# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -2.79 to 0.972 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.4% | -3.01 to 0.806 | STEADY, no difference beyond the noise |
| queries a second | 4,730 | 4,712 | -0.4% | -48.1 to 12.9 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.33 | 2.29 | -1.9% | -0.324 to 0.237 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.77 | 3.73 | -1.2% | -0.588 to 0.494 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.15 | -1.1% | -0.0552 to 0.0291 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 447 | 447 | +0.1% | -3.5 to 4.33 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,931 | 246,757 | +1.2% | -4,471 to 10,124 | shown, not judged |
| host CPU busy (share of the run) | 0.0894 | 0.0893 | -0.1% | -0.0034 to 0.0032 | STEADY, no difference beyond the noise |
| host CPU-seconds | 53.7 | 53.6 | -0.2% | -2.05 to 1.87 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.19 | 1.2 | +0.2% | -0.0384 to 0.0426 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.1% | -3.74 to 4.16 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 297 | +0.0% | -3.95 to 4.22 | STEADY, no difference beyond the noise |
| queries a second | 4,745 | 4,748 | +0.0% | -63.2 to 67.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.82 | 1.78 | -2.4% | -0.139 to 0.0507 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.68 | 3.55 | -3.5% | -0.553 to 0.298 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.25 | 1.23 | -1.1% | -0.0978 to 0.0713 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 462 | 458 | -0.7% | -16.4 to 9.86 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 658,716 | 656,912 | -0.3% | -11,464 to 7,856 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.1 | -0.2% | -0.00728 to 0.0069 | STEADY, no difference beyond the noise |
| host CPU-seconds | 181 | 180 | -0.2% | -13 to 12.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.34 | 1.33 | -0.2% | -0.0838 to 0.0774 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | -0.2% | -3.45 to 2.68 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.27 to 2.6 | STEADY, no difference beyond the noise |
| queries a second | 3,945 | 3,949 | +0.1% | -45.4 to 52 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.9 | 5.86 | -0.8% | -3.12 to 3.03 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 16.9 | 15.1 | -10.2% | -10.7 to 7.21 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.88 | 2.77 | -3.7% | -0.215 to 0.00313 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,280 | +150.1% | 619 to 918 | power given |
| pages holding data, mean (MB) | 463 | 1,017 | +119.5% | 547 to 560 | power given |
| pages read from disk into the pool (misses) | 616,991 | 101,027 | -83.6% | -580,221 to -451,706 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.11 | -7.4% | -0.0113 to -0.00631 | GAIN |
| host CPU-seconds | 211 | 195 | -7.4% | -19.9 to -11.4 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.22 | -7.2% | -0.245 to -0.102 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 1.43 to 14.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,940 | 2,939 | -0.0% | -11.7 to 10.7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,954 | +0.1% | -2.26 to 9.4 | STEADY, no difference beyond the noise |
| queries a second | 2,950 | 2,954 | +0.1% | -2.26 to 9.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.339 | +4.5% | -0.0551 to 0.0845 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.475 | 0.509 | +7.2% | -0.0549 to 0.123 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.203 | +4.4% | -0.0143 to 0.0316 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 804 | +57.0% | -446 to 1,029 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 682 | +47.1% | -287 to 724 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,475 | 246,048 | -32.9% | -392,074 to 151,221 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.162 | +4.3% | -0.00841 to 0.0217 | STEADY, no difference beyond the noise |
| host CPU-seconds | 274 | 285 | +4.3% | -14.5 to 37.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.204 | 0.212 | +4.3% | -0.0115 to 0.0288 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | -1.48 to 3.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 9.26 | 14.9 | +61.4% | -8.54 to 19.9 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.1% | -8.15 to 6.92 | STEADY, no difference beyond the noise |
| queries a second | 985 | 984 | -0.1% | -8.15 to 6.92 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.72 | 1.67 | -3.2% | -0.288 to 0.179 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.15 | 3.49 | +10.8% | -0.521 to 1.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.27 | +21.1% | -0.787 to 1.23 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 704 to 744 | power given |
| pages holding data, mean (MB) | 457 | 888 | +94.6% | 409 to 455 | power given |
| pages read from disk into the pool (misses) | 191,050 | 71,535 | -62.6% | -131,947 to -107,084 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.221 | -4.2% | -0.0339 to 0.0143 | STEADY, no difference beyond the noise |
| host CPU-seconds | 404 | 387 | -4.2% | -58.7 to 24.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 99.8 | 69.3 | -30.5% | -109 to 48.4 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
