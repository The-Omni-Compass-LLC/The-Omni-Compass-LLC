# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.1% | -2.43 to 2.12 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.1% | -1.43 to 2.04 | STEADY, no difference beyond the noise |
| queries a second | 4,690 | 4,695 | +0.1% | -22.9 to 32.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.85 | 4.82 | -0.6% | -0.15 to 0.0936 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.55 | 6.79 | +3.7% | -0.0738 to 0.56 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.16 | 3.05 | -3.4% | -0.208 to -0.00659 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 908 | +609.6% | 645 to 916 | power given |
| pages holding data, mean (MB) | 121 | 820 | +576.1% | 591 to 806 | power given |
| pages read from disk into the pool (misses) | 604,140 | 118,321 | -80.4% | -587,438 to -384,199 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.237 | -2.8% | -0.0136 to 8.96e-05 | STEADY, no difference beyond the noise |
| host CPU-seconds | 145 | 141 | -2.8% | -8.07 to 0.0392 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.24 | 3.15 | -2.7% | -0.198 to 0.0224 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | -0.1% | -1.95 to 1.42 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.0% | -2.21 to 1.97 | STEADY, no difference beyond the noise |
| queries a second | 4,711 | 4,709 | -0.0% | -35.4 to 31.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.24 | 3.23 | -0.6% | -0.187 to 0.149 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.46 | 4.52 | +1.2% | -0.182 to 0.292 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.47 | 2.44 | -1.2% | -0.156 to 0.0947 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 456 | +256.4% | 135 to 522 | power given |
| pages holding data, mean (MB) | 120 | 421 | +250.7% | 140 to 461 | power given |
| pages read from disk into the pool (misses) | 1,979,698 | 778,447 | -60.7% | -1,758,600 to -643,902 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.2 | -1.3% | -0.0137 to 0.00842 | STEADY, no difference beyond the noise |
| host CPU-seconds | 369 | 364 | -1.3% | -24.7 to 15.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.73 | 2.7 | -1.2% | -0.173 to 0.107 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | -1.3 to 7.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 185 | 196 | +5.9% | 8.74 to 13 | GAIN |
| throughput (transactions a second) | 197 | 196 | -0.3% | -2.32 to 1.19 | STEADY, no difference beyond the noise |
| queries a second | 3,936 | 3,925 | -0.3% | -46.4 to 23.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 11.4 | 6.59 | -42.1% | -5.04 to -4.53 | GAIN |
| latency, 99th percentile (ms) | 15.6 | 8.69 | -44.5% | -7.65 to -6.26 | GAIN |
| latency, mean (ms) | 5.7 | 4.7 | -17.5% | -1.09 to -0.909 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 978 | +664.3% | 788 to 913 | power given |
| pages holding data, mean (MB) | 121 | 874 | +621.8% | 694 to 811 | power given |
| pages read from disk into the pool (misses) | 1,667,934 | 181,540 | -89.1% | -1,631,298 to -1,341,491 | shown, not judged |
| host CPU busy (share of the run) | 0.303 | 0.257 | -15.1% | -0.0557 to -0.0354 | GAIN |
| host CPU-seconds | 532 | 452 | -15.1% | -98.3 to -62.4 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.29 | 5.04 | -19.8% | -1.38 to -1.11 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 1.87 to 9.46 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,939 | -0.1% | -12.1 to 4.92 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,945 | 2,942 | -0.1% | -10.5 to 4.57 | STEADY, no difference beyond the noise |
| queries a second | 2,945 | 2,942 | -0.1% | -10.5 to 4.57 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.282 | 0.294 | +4.5% | -0.0211 to 0.0464 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.402 | 0.412 | +2.5% | -0.0115 to 0.0315 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.175 | 0.174 | -0.7% | -0.00678 to 0.00419 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 302 | +136.0% | 24.9 to 323 | power given |
| pages holding data, mean (MB) | 121 | 288 | +137.7% | 28.1 to 306 | power given |
| pages read from disk into the pool (misses) | 1,028,741 | 674,230 | -34.5% | -622,224 to -86,797 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.15 | -0.3% | -0.00667 to 0.00568 | STEADY, no difference beyond the noise |
| host CPU-seconds | 272 | 271 | -0.3% | -12.2 to 10.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.201 | 0.201 | -0.2% | -0.00926 to 0.00858 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.05 | 6.04 | +49.2% | -0.218 to 4.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.1% | -8.37 to 6.09 | STEADY, no difference beyond the noise |
| queries a second | 985 | 984 | -0.1% | -8.37 to 6.09 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.26 | 1.83 | -19.0% | -0.56 to -0.299 | GAIN |
| latency, 99th percentile (ms) | 4.68 | 4.39 | -6.2% | -1.35 to 0.778 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.19 | -7.1% | -0.128 to -0.0546 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,267 | +890.0% | 1,081 to 1,197 | power given |
| pages holding data, mean (MB) | 118 | 866 | +632.8% | 724 to 772 | power given |
| pages read from disk into the pool (misses) | 418,725 | 83,544 | -80.0% | -359,881 to -310,481 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.208 | -12.7% | -0.055 to -0.00572 | GAIN |
| host CPU-seconds | 419 | 366 | -12.7% | -95.3 to -11.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 239 | 133 | -44.4% | -275 to 63.4 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
