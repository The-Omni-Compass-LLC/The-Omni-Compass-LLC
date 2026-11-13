# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.0% | -1.35 to 1.52 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.1% | -1.6 to 2.25 | EVEN, no difference beyond the noise |
| queries a second | 4,688 | 4,693 | +0.1% | -25.7 to 36.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.09 | 5.09 | +0.0% | -0.454 to 0.458 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.87 | 7 | +1.9% | -0.803 to 1.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.33 | 3.35 | +0.5% | -0.0304 to 0.0616 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 435 | -15.0% | -278 to 124 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 377 | -15.8% | -204 to 62.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,563 | 254,733 | +5.0% | -77,992 to 102,333 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.198 | +1.5% | -0.00485 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 108 | 110 | +1.6% | -3.05 to 6.59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.41 | 2.45 | +1.6% | -0.0772 to 0.154 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 3.5 to 13.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.0% | -0.645 to 0.893 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -0.584 to 0.0845 | EVEN, no difference beyond the noise |
| queries a second | 4,738 | 4,734 | -0.1% | -9.34 to 1.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.93 | 1.82 | -5.4% | -0.419 to 0.21 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.16 | 3.66 | -11.9% | -1.63 to 0.643 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.37 | 1.27 | -6.9% | -0.426 to 0.238 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 361 | -29.5% | -186 to -117 | GAIN |
| pages holding data, mean (MB) | 462 | 332 | -28.0% | -154 to -105 | GAIN |
| pages read from disk into the pool (misses) | 653,430 | 1,126,566 | +72.4% | 295,271 to 651,002 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.101 | -0.4% | -0.00184 to 0.00109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 181 | -0.3% | -3.28 to 2.04 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.34 | -0.4% | -0.0288 to 0.0175 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 4.08 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 187 | 189 | +0.9% | -3.67 to 6.95 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | +0.4% | -1.39 to 2.83 | EVEN, no difference beyond the noise |
| queries a second | 3,892 | 3,907 | +0.4% | -27.8 to 56.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.74 | 9.51 | -2.4% | -2.19 to 1.71 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.7 | 14 | -5.3% | -1.93 to 0.372 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.89 | 4.79 | -2.1% | -0.458 to 0.256 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 554 | +8.1% | 16.1 to 66.9 | power given |
| pages holding data, mean (MB) | 461 | 488 | +5.7% | -13.3 to 66.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,010 | 558,755 | -9.0% | -107,640 to -2,868 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.222 | -1.4% | -0.00406 to -0.00226 | GAIN |
| host CPU-seconds | 406 | 400 | -1.4% | -7.54 to -3.91 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.7 | 4.6 | -2.3% | -0.234 to 0.0217 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.3 |  | 15.2 to 25.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,945 | -0.1% | -17 to 8.59 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,956 | 2,953 | -0.1% | -5.3 to -1.64 | LOSS |
| queries a second | 2,956 | 2,953 | -0.1% | -5.3 to -1.64 | LOSS |
| latency, 95th percentile (ms) | 0.315 | 0.309 | -1.8% | -0.0193 to 0.00802 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.425 | 0.415 | -2.2% | -0.0639 to 0.0452 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.197 | +1.1% | -0.0183 to 0.0224 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 455 | -11.2% | -114 to -0.729 | GAIN |
| pages holding data, mean (MB) | 464 | 407 | -12.2% | -124 to 11.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,116 | 455,361 | +24.0% | -4,524 to 181,014 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.153 | -0.4% | -0.0087 to 0.00762 | EVEN, no difference beyond the noise |
| host CPU-seconds | 272 | 271 | -0.3% | -15.5 to 13.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.202 | 0.201 | -0.2% | -0.0119 to 0.011 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 12.9 to 20.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 90.7 | 77.4 | -14.7% | -36.4 to 9.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 986 | -0.2% | -11.3 to 8.28 | EVEN, no difference beyond the noise |
| queries a second | 987 | 986 | -0.2% | -11.3 to 8.28 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 149 | 130 | -13.1% | -180 to 141 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 330 | 271 | -17.8% | -556 to 438 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 28.6 | 25.1 | -12.1% | -45.7 to 38.7 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 428 | -16.3% | -182 to 15.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 363 | -20.1% | -210 to 28 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,832 | 248,827 | +31.1% | -12,819 to 130,808 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.143 | +6.6% | -0.00346 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 237 | 253 | +6.5% | -4.36 to 35.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.14 | 7.48 | +21.8% | 0.643 to 2.04 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 4.58 to 30.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
