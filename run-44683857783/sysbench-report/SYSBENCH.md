# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 291 | -0.3% | -5.83 to 3.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | -0.1% | -4.26 to 3.63 | STEADY, no difference beyond the noise |
| queries a second | 4,678 | 4,673 | -0.1% | -68.1 to 58.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.57 | 4.6 | +0.5% | -0.282 to 0.331 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 7.08 | +4.3% | 0.134 to 0.447 | LOSS |
| latency, mean (ms) | 2.36 | 2.34 | -0.9% | -0.0948 to 0.0539 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 883 | +589.6% | 104 to 1,405 | power given |
| pages holding data, mean (MB) | 121 | 751 | +522.4% | 241 to 1,019 | power given |
| pages read from disk into the pool (misses) | 602,356 | 138,227 | -77.1% | -612,007 to -316,251 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.188 | -1.3% | -0.00994 to 0.00492 | STEADY, no difference beyond the noise |
| host CPU-seconds | 116 | 115 | -1.3% | -5.98 to 2.91 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.59 | 2.57 | -1.0% | -0.109 to 0.0597 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 2.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.1% | -2.55 to 3.16 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.3% | -5.74 to 4.22 | STEADY, no difference beyond the noise |
| queries a second | 4,742 | 4,730 | -0.3% | -91.8 to 67.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.9 | 2.79 | -3.5% | -0.325 to 0.12 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 30.1 | 12.1 | -59.9% | -57.7 to 21.6 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 2.61 | -18.1% | -1.12 to -0.0318 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,113 | +769.7% | 919 to 1,051 | power given |
| pages holding data, mean (MB) | 120 | 942 | +683.2% | 799 to 844 | power given |
| pages read from disk into the pool (misses) | 2,004,148 | 114,100 | -94.3% | -1,997,197 to -1,782,899 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.161 | -5.7% | -0.0124 to -0.00713 | GAIN |
| host CPU-seconds | 306 | 288 | -5.7% | -22.1 to -12.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.3 | 2.16 | -5.8% | -0.179 to -0.0883 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 6.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 182 | 196 | +7.6% | 11.9 to 16 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.5% | 0.518 to 1.42 | GAIN |
| queries a second | 3,927 | 3,947 | +0.5% | 10.4 to 28.3 | GAIN |
| latency, 95th percentile (ms) | 11.9 | 6.96 | -41.7% | -5.72 to -4.24 | GAIN |
| latency, 99th percentile (ms) | 16.7 | 9.4 | -43.7% | -9.56 to -5.06 | GAIN |
| latency, mean (ms) | 5.98 | 4.88 | -18.5% | -1.65 to -0.556 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,020 | +697.1% | 807 to 977 | power given |
| pages holding data, mean (MB) | 118 | 925 | +680.5% | 741 to 871 | power given |
| pages read from disk into the pool (misses) | 1,665,006 | 169,638 | -89.8% | -1,610,706 to -1,380,030 | shown, not judged |
| host CPU busy (share of the run) | 0.318 | 0.274 | -14.0% | -0.0649 to -0.0239 | GAIN |
| host CPU-seconds | 559 | 481 | -14.0% | -114 to -42.1 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.69 | 5.35 | -20.1% | -1.83 to -0.856 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,950 | 2,946 | -0.1% | -15.8 to 8.04 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,955 | 2,951 | -0.1% | -15.9 to 9.2 | STEADY, no difference beyond the noise |
| queries a second | 2,955 | 2,951 | -0.1% | -15.9 to 9.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.316 | -0.6% | -0.0192 to 0.0152 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.424 | 0.435 | +2.4% | 0.000293 to 0.0204 | LOSS |
| latency, mean (ms) | 0.192 | 0.19 | -0.7% | -0.00601 to 0.00318 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 460 | +259.2% | 117 to 547 | power given |
| pages holding data, mean (MB) | 121 | 435 | +258.6% | 114 to 513 | power given |
| pages read from disk into the pool (misses) | 1,030,880 | 440,514 | -57.3% | -836,225 to -344,507 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.155 | -0.2% | -0.0048 to 0.00416 | STEADY, no difference beyond the noise |
| host CPU-seconds | 274 | 273 | -0.2% | -8.5 to 7.68 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.203 | 0.203 | -0.0% | -0.00528 to 0.00516 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | -0.484 to 4.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7.74 | 2.09 | -73.1% | -38.1 to 26.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 974 | 980 | +0.6% | -19.6 to 31.4 | STEADY, no difference beyond the noise |
| queries a second | 974 | 980 | +0.6% | -19.6 to 31.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.51 | 2.76 | -21.2% | -2.11 to 0.621 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 831 | 22.2 | -97.3% | -4,288 to 2,672 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 23.5 | 1.8 | -92.3% | -114 to 71 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,255 | +880.1% | 1,028 to 1,225 | power given |
| pages holding data, mean (MB) | 119 | 864 | +627.8% | 713 to 777 | power given |
| pages read from disk into the pool (misses) | 416,190 | 88,010 | -78.9% | -365,480 to -290,880 | shown, not judged |
| host CPU busy (share of the run) | 0.29 | 0.272 | -6.2% | -0.075 to 0.0393 | STEADY, no difference beyond the noise |
| host CPU-seconds | 507 | 477 | -6.0% | -131 to 70.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1,393 | 548 | -60.7% | -4,553 to 2,864 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
