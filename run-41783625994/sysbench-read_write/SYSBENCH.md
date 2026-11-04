# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
