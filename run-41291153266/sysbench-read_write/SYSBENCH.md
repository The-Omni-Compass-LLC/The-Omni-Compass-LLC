# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 180 | 195 | +8.4% | 10.5 to 19.8 | GAIN |
| throughput (transactions a second) | 197 | 197 | -0.0% | -5.91 to 5.79 | STEADY, no difference beyond the noise |
| queries a second | 3,932 | 3,931 | -0.0% | -118 to 116 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.6 | 7.13 | -43.4% | -6.28 to -4.67 | GAIN |
| latency, 99th percentile (ms) | 17.9 | 9.57 | -46.4% | -11.5 to -5.08 | GAIN |
| latency, mean (ms) | 6.36 | 5.02 | -21.1% | -2.76 to 0.0798 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,043 | +715.1% | 630 to 1,200 | power given |
| pages holding data, mean (MB) | 118 | 919 | +676.8% | 608 to 993 | power given |
| pages read from disk into the pool (misses) | 1,668,763 | 163,223 | -90.2% | -1,653,818 to -1,357,263 | shown, not judged |
| host CPU busy (share of the run) | 0.309 | 0.264 | -14.7% | -0.0588 to -0.0319 | GAIN |
| host CPU-seconds | 544 | 464 | -14.8% | -103 to -57.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.59 | 5.18 | -21.4% | -1.52 to -1.3 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.7 to 12.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
