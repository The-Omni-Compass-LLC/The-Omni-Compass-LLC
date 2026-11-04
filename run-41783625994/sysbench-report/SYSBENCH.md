# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | -0.0% | -4.8 to 4.75 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | -0.1% | -4.78 to 4.27 | STEADY, no difference beyond the noise |
| queries a second | 4,677 | 4,673 | -0.1% | -76.5 to 68.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.01 | 5.07 | +1.1% | -0.185 to 0.297 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.09 | -1.7% | -0.429 to 0.178 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.25 | 3.26 | +0.4% | -0.109 to 0.135 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 880 | +71.9% | 70.8 to 665 | power given |
| pages holding data, mean (MB) | 457 | 794 | +73.9% | 98.5 to 576 | power given |
| pages read from disk into the pool (misses) | 244,265 | 134,193 | -45.1% | -190,751 to -29,392 | shown, not judged |
| host CPU busy (share of the run) | 0.248 | 0.252 | +1.4% | -0.0121 to 0.0193 | STEADY, no difference beyond the noise |
| host CPU-seconds | 148 | 150 | +1.6% | -8.01 to 12.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.32 | 3.36 | +1.5% | -0.172 to 0.269 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.0% | -3.97 to 4.16 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.1% | -3.3 to 2.61 | STEADY, no difference beyond the noise |
| queries a second | 4,699 | 4,693 | -0.1% | -52.8 to 41.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.58 | 2.58 | +0.0% | 0 to 0 | STEADY, the same |
| latency, 99th percentile (ms) | 4.01 | 3.98 | -0.7% | -0.397 to 0.344 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.76 | 1.89 | -31.4% | -4.33 to 2.59 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 588 | +14.9% | -252 to 405 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 520 | +12.4% | -210 to 324 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 657,053 | 537,120 | -18.3% | -605,078 to 365,212 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.156 | -1.8% | -0.0115 to 0.00587 | STEADY, no difference beyond the noise |
| host CPU-seconds | 290 | 285 | -1.8% | -20.7 to 10.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.12 | -1.7% | -0.129 to 0.0532 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | -3.3 to 5.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 193 | +0.9% | -0.548 to 3.99 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 195 | 196 | +0.2% | -0.952 to 1.8 | STEADY, no difference beyond the noise |
| queries a second | 3,904 | 3,913 | +0.2% | -19 to 36 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.92 | 4.79 | -30.7% | -2.81 to -1.44 | GAIN |
| latency, 99th percentile (ms) | 67.8 | 30.3 | -55.3% | -149 to 74.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 6.17 | 5.22 | -15.3% | -3.19 to 1.29 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,184 | +131.2% | 441 to 902 | power given |
| pages holding data, mean (MB) | 461 | 989 | +114.3% | 409 to 646 | power given |
| pages read from disk into the pool (misses) | 616,483 | 107,700 | -82.5% | -559,399 to -458,166 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.171 | -7.4% | -0.0247 to -0.00263 | GAIN |
| host CPU-seconds | 335 | 310 | -7.4% | -44.9 to -4.69 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.81 | 3.5 | -8.2% | -0.49 to -0.134 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | -7.01 to 21.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 7.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,947 | -0.0% | -13.9 to 12.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,955 | 2,954 | -0.0% | -12.7 to 11.3 | STEADY, no difference beyond the noise |
| queries a second | 2,955 | 2,954 | -0.0% | -12.7 to 11.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.334 | -2.3% | -0.0252 to 0.00921 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.473 | 0.464 | -1.8% | -0.0283 to 0.0116 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.207 | 0.205 | -1.1% | -0.0158 to 0.0111 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -18.2 to 11.4 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,663 | 365,943 | -0.7% | -11,074 to 5,634 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.167 | -0.9% | -0.0112 to 0.00815 | STEADY, no difference beyond the noise |
| host CPU-seconds | 296 | 293 | -0.9% | -19.6 to 14.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.219 | 0.217 | -0.9% | -0.0154 to 0.0115 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 19.5 | 24 | +23.1% | -22.2 to 31.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 983 | -0.2% | -6.97 to 3.51 | STEADY, no difference beyond the noise |
| queries a second | 985 | 983 | -0.2% | -6.97 to 3.51 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.56 | 1.48 | -4.8% | -0.368 to 0.218 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.41 | 2.27 | -6.0% | -0.692 to 0.403 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.977 | 0.956 | -2.1% | -0.122 to 0.0808 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.3% | 705 to 742 | power given |
| pages holding data, mean (MB) | 458 | 888 | +94.1% | 411 to 450 | power given |
| pages read from disk into the pool (misses) | 192,717 | 70,141 | -63.6% | -134,797 to -110,355 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.222 | -2.1% | -0.0305 to 0.0208 | STEADY, no difference beyond the noise |
| host CPU-seconds | 399 | 390 | -2.1% | -53.3 to 36.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 47.2 | 43.5 | -7.8% | -35.2 to 27.8 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
