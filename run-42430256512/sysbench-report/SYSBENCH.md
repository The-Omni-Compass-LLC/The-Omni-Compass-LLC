# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.1% | -9.58 to 9.97 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 291 | 292 | +0.3% | -10.3 to 12.2 | STEADY, no difference beyond the noise |
| queries a second | 4,663 | 4,678 | +0.3% | -165 to 195 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.08 | 4.1 | +0.6% | -0.0826 to 0.133 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.92 | +4.4% | -0.301 to 0.798 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.54 | 2.76 | +8.4% | -0.934 to 1.36 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 805 | +528.7% | -125 to 1,478 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 689 | +470.0% | 51 to 1,085 | power given |
| pages read from disk into the pool (misses) | 601,165 | 158,642 | -73.6% | -559,702 to -325,343 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.2 | -1.5% | -0.0111 to 0.00524 | STEADY, no difference beyond the noise |
| host CPU-seconds | 124 | 122 | -1.4% | -7.27 to 3.83 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.77 | 2.73 | -1.5% | -0.248 to 0.165 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -3.57 to 3.53 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -3.36 to 3.54 | STEADY, no difference beyond the noise |
| queries a second | 4,725 | 4,727 | +0.0% | -53.8 to 56.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 4.1 | +2.4% | -0.00627 to 0.2 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.31 | 5.57 | +4.9% | -0.114 to 0.636 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.13 | 3.1 | -0.8% | -0.0644 to 0.0158 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 686 | +436.2% | 143 to 974 | power given |
| pages holding data, mean (MB) | 120 | 616 | +413.0% | 154 to 838 | power given |
| pages read from disk into the pool (misses) | 1,985,185 | 409,084 | -79.4% | -2,030,899 to -1,121,303 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.246 | -0.6% | -0.00281 to -0.000323 | GAIN |
| host CPU-seconds | 439 | 436 | -0.6% | -5.17 to -0.541 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.25 | 3.23 | -0.7% | -0.069 to 0.0266 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 177 | 188 | +6.0% | -1.31 to 22.6 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.3% | -0.811 to -0.349 | LOSS |
| queries a second | 3,957 | 3,945 | -0.3% | -16.2 to -6.98 | LOSS |
| latency, 95th percentile (ms) | 42.3 | 11.1 | -73.8% | -95.6 to 33.1 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 281 | 89.5 | -68.2% | -474 to 91 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 13.7 | 6.72 | -50.9% | -16.5 to 2.56 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,229 | +859.8% | 1,032 to 1,169 | power given |
| pages holding data, mean (MB) | 121 | 1,011 | +736.8% | 848 to 933 | power given |
| pages read from disk into the pool (misses) | 1,672,169 | 96,814 | -94.2% | -1,664,677 to -1,486,033 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.168 | -17.6% | -0.0401 to -0.0319 | GAIN |
| host CPU-seconds | 361 | 298 | -17.6% | -71.1 to -56.1 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.48 | 3.48 | -22.3% | -1.34 to -0.648 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 9.03 to 19 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 6.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,936 | 2,940 | +0.1% | -23.3 to 31.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | -0.0% | -8.24 to 7.63 | STEADY, no difference beyond the noise |
| queries a second | 2,953 | 2,953 | -0.0% | -8.24 to 7.63 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.387 | 0.356 | -7.8% | -0.134 to 0.0735 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.553 | 0.536 | -3.1% | -0.0902 to 0.0562 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.22 | 0.208 | -5.7% | -0.0441 to 0.019 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 516 | +303.3% | 255 to 522 | power given |
| pages holding data, mean (MB) | 121 | 478 | +294.1% | 241 to 472 | power given |
| pages read from disk into the pool (misses) | 1,030,271 | 377,639 | -63.3% | -756,382 to -548,883 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.165 | -5.0% | -0.0292 to 0.012 | STEADY, no difference beyond the noise |
| host CPU-seconds | 305 | 290 | -4.9% | -50.3 to 20.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.227 | 0.216 | -5.0% | -0.0397 to 0.0171 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -1.2 to 4.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 17.7 | 28.4 | +60.2% | 8.16 to 13.2 | GAIN |
| throughput (transactions a second) | 984 | 984 | +0.1% | -3 to 4.38 | STEADY, no difference beyond the noise |
| queries a second | 984 | 984 | +0.1% | -3 to 4.38 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.96 | 1.6 | -18.5% | -0.514 to -0.212 | GAIN |
| latency, 99th percentile (ms) | 3.13 | 2.74 | -12.4% | -0.685 to -0.0894 | GAIN |
| latency, mean (ms) | 1.07 | 0.992 | -7.2% | -0.141 to -0.014 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,282 | +901.6% | 1,083 to 1,225 | power given |
| pages holding data, mean (MB) | 118 | 871 | +639.2% | 726 to 780 | power given |
| pages read from disk into the pool (misses) | 417,474 | 78,014 | -81.3% | -354,510 to -324,409 | shown, not judged |
| host CPU busy (share of the run) | 0.26 | 0.231 | -10.9% | -0.0511 to -0.00528 | GAIN |
| host CPU-seconds | 455 | 406 | -10.9% | -88.4 to -10.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 56.7 | 31.4 | -44.6% | -39 to -11.5 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
