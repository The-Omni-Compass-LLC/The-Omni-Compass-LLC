# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,947 | +0.0% | -9.34 to 10.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% | -8.08 to 8.36 | STEADY, no difference beyond the noise |
| queries a second | 2,953 | 2,953 | +0.0% | -8.08 to 8.36 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.303 | 0.308 | +1.8% | -0.00835 to 0.019 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.459 | 0.456 | -0.6% | -0.0141 to 0.00881 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.205 | 0.191 | -6.8% | -0.0809 to 0.0533 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -17.5 to 10.9 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,464 | 366,289 | -0.6% | -10,686 to 6,336 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.156 | +1.8% | -0.00158 to 0.00712 | STEADY, no difference beyond the noise |
| host CPU-seconds | 270 | 275 | +1.8% | -2.83 to 12.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.2 | 0.204 | +1.8% | -0.00252 to 0.00973 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
