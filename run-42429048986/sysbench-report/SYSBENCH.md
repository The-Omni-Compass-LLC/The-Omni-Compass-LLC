# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.5% | -6.88 to 3.91 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 293 | -0.5% | -6.73 to 3.68 | STEADY, no difference beyond the noise |
| queries a second | 4,716 | 4,692 | -0.5% | -108 to 58.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.85 | 4.74 | -2.4% | -0.24 to 0.00981 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 6.59 | -3.0% | -0.371 to -0.0294 | GAIN |
| latency, mean (ms) | 3.15 | 3.11 | -1.3% | -0.0985 to 0.0157 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 712 | +39.0% | 198 to 202 | power given |
| pages holding data, mean (MB) | 451 | 642 | +42.3% | 188 to 194 | power given |
| pages read from disk into the pool (misses) | 247,487 | 181,007 | -26.9% | -70,155 to -62,805 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.242 | -2.0% | -0.0086 to -0.00115 | GAIN |
| host CPU-seconds | 147 | 144 | -2.1% | -4.68 to -1.44 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.27 | 3.22 | -1.5% | -0.0764 to -0.0214 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.6% | -10.4 to 14.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.1% | -2.36 to 3.02 | STEADY, no difference beyond the noise |
| queries a second | 4,739 | 4,745 | +0.1% | -37.8 to 48.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.09 | 2.74 | -11.1% | -1.28 to 0.592 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 549 | 21.8 | -96.0% | -2,840 to 1,786 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 12.6 | 2.86 | -77.3% | -52.6 to 33.2 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,175 | +129.5% | 562 to 764 | power given |
| pages holding data, mean (MB) | 467 | 958 | +105.1% | 477 to 505 | power given |
| pages read from disk into the pool (misses) | 659,968 | 84,303 | -87.2% | -596,137 to -555,191 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.161 | -3.4% | -0.0107 to -0.000831 | GAIN |
| host CPU-seconds | 298 | 288 | -3.4% | -19.2 to -1.35 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.25 | 2.16 | -4.1% | -0.248 to 0.0635 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 4.08 to 16.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 5.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 196 | +2.2% | 1.23 to 7.35 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.1% | -2.26 to 2.67 | STEADY, no difference beyond the noise |
| queries a second | 3,929 | 3,933 | +0.1% | -45.1 to 53.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.58 | 6.71 | -21.8% | -2.47 to -1.28 | GAIN |
| latency, 99th percentile (ms) | 12.7 | 8.63 | -31.9% | -4.66 to -3.42 | GAIN |
| latency, mean (ms) | 5.17 | 4.8 | -7.2% | -0.523 to -0.218 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 997 | +94.7% | 375 to 595 | power given |
| pages holding data, mean (MB) | 463 | 890 | +92.3% | 321 to 533 | power given |
| pages read from disk into the pool (misses) | 616,842 | 136,760 | -77.8% | -529,990 to -430,173 | shown, not judged |
| host CPU busy (share of the run) | 0.276 | 0.258 | -6.8% | -0.0235 to -0.0141 | GAIN |
| host CPU-seconds | 486 | 453 | -6.8% | -41.6 to -24.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.53 | 5.04 | -8.9% | -0.66 to -0.322 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,926 | 2,926 | -0.0% | -7.96 to 7.89 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,929 | 2,929 | -0.0% | -13.2 to 12.5 | STEADY, no difference beyond the noise |
| queries a second | 2,929 | 2,929 | -0.0% | -13.2 to 12.5 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.225 | 0.222 | -1.3% | -0.0347 to 0.0287 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.417 | 0.414 | -0.6% | -0.0313 to 0.0267 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.141 | 0.145 | +2.9% | -0.0368 to 0.0451 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 661 | +29.2% | -493 to 792 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 586 | +26.5% | -425 to 671 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,252 | 279,075 | -24.2% | -454,411 to 276,056 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.127 | -2.2% | -0.0195 to 0.0138 | STEADY, no difference beyond the noise |
| host CPU-seconds | 240 | 235 | -2.3% | -38.1 to 27 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.178 | 0.174 | -2.3% | -0.0282 to 0.0201 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 511 | 538 | +5.3% | -100 to 154 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 988 | 989 | +0.1% | -3.16 to 4.89 | STEADY, no difference beyond the noise |
| queries a second | 988 | 989 | +0.1% | -3.16 to 4.89 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.54 | 2.6 | +2.3% | -0.383 to 0.5 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.49 | -1.8% | -1.92 to 1.72 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.02 | 0.86 | -15.8% | -0.825 to 0.501 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,210 | +136.4% | 574 to 822 | power given |
| pages holding data, mean (MB) | 455 | 887 | +94.9% | 403 to 461 | power given |
| pages read from disk into the pool (misses) | 192,180 | 71,355 | -62.9% | -128,129 to -113,522 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.097 | -3.6% | -0.0201 to 0.0127 | STEADY, no difference beyond the noise |
| host CPU-seconds | 177 | 171 | -3.6% | -35 to 22.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.781 | 0.699 | -10.5% | -0.454 to 0.29 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
