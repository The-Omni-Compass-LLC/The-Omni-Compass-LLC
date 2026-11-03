# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 196 | +3.1% | 3.68 to 8.05 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.3% | -1.64 to 2.78 | STEADY, no difference beyond the noise |
| queries a second | 3,930 | 3,941 | +0.3% | -32.8 to 55.6 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.56 | 7.43 | -22.3% | -2.62 to -1.64 | GAIN |
| latency, 99th percentile (ms) | 14.3 | 10.1 | -29.4% | -4.75 to -3.66 | GAIN |
| latency, mean (ms) | 5.47 | 5.09 | -7.0% | -0.427 to -0.336 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,087 | +112.3% | 481 to 670 | power given |
| pages holding data, mean (MB) | 462 | 967 | +109.2% | 442 to 567 | power given |
| pages read from disk into the pool (misses) | 617,916 | 116,575 | -81.1% | -603,046 to -399,636 | shown, not judged |
| host CPU busy (share of the run) | 0.284 | 0.268 | -5.8% | -0.0223 to -0.0104 | GAIN |
| host CPU-seconds | 499 | 470 | -5.8% | -39.3 to -18.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.74 | 5.25 | -8.6% | -0.597 to -0.395 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
