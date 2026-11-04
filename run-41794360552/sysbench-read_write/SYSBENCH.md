# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 196 | +1.7% | 2.07 to 4.67 | GAIN |
| throughput (transactions a second) | 196 | 196 | -0.0% | -2.56 to 2.46 | STEADY, no difference beyond the noise |
| queries a second | 3,927 | 3,926 | -0.0% | -51.2 to 49.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.18 | 6.55 | -19.9% | -2.32 to -0.94 | GAIN |
| latency, 99th percentile (ms) | 12.2 | 8.38 | -31.5% | -5.07 to -2.63 | GAIN |
| latency, mean (ms) | 5.06 | 4.74 | -6.4% | -0.464 to -0.187 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 993 | +94.0% | 360 to 602 | power given |
| pages holding data, mean (MB) | 463 | 884 | +91.1% | 300 to 543 | power given |
| pages read from disk into the pool (misses) | 617,084 | 145,571 | -76.4% | -536,997 to -406,028 | shown, not judged |
| host CPU busy (share of the run) | 0.276 | 0.259 | -6.0% | -0.0219 to -0.0112 | GAIN |
| host CPU-seconds | 485 | 455 | -6.0% | -38.6 to -19.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.5 | 5.07 | -7.7% | -0.504 to -0.338 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
