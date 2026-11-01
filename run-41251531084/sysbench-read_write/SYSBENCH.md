# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 195 | +1.1% | 1.6 to 2.72 | GAIN |
| throughput (transactions a second) | 195 | 196 | +0.3% | -0.699 to 1.71 | STEADY, no difference beyond the noise |
| queries a second | 3,900 | 3,911 | +0.3% | -14 to 34.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.99 | 5.95 | -25.5% | -2.59 to -1.47 | GAIN |
| latency, 99th percentile (ms) | 10.8 | 8.48 | -21.3% | -3.51 to -1.08 | GAIN |
| latency, mean (ms) | 4.37 | 3.92 | -10.4% | -0.575 to -0.337 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 563 | +339.8% | 288 to 582 | power given |
| pages holding data, mean (MB) | 121 | 516 | +325.9% | 262 to 527 | power given |
| pages read from disk into the pool (misses) | 1,656,062 | 547,478 | -66.9% | -1,355,358 to -861,809 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.224 | -9.1% | -0.0281 to -0.0166 | GAIN |
| host CPU-seconds | 448 | 407 | -9.1% | -50.8 to -31 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.06 | 4.54 | -10.1% | -0.613 to -0.409 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
