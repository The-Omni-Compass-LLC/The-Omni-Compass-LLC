# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 194 | +2.6% | -0.102 to 9.8 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.1% | -3.22 to 2.82 | STEADY, no difference beyond the noise |
| queries a second | 3,935 | 3,931 | -0.1% | -64.3 to 56.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.79 | 7.26 | -25.9% | -3.15 to -1.93 | GAIN |
| latency, 99th percentile (ms) | 17.8 | 13.5 | -24.2% | -9.97 to 1.35 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 5.81 | 5.19 | -10.7% | -1.17 to -0.0705 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,177 | +129.8% | 580 to 749 | power given |
| pages holding data, mean (MB) | 461 | 1,003 | +117.4% | 528 to 555 | power given |
| pages read from disk into the pool (misses) | 620,354 | 92,602 | -85.1% | -560,059 to -495,445 | shown, not judged |
| host CPU busy (share of the run) | 0.283 | 0.261 | -7.7% | -0.0317 to -0.012 | GAIN |
| host CPU-seconds | 497 | 459 | -7.7% | -56.3 to -20.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.74 | 5.17 | -10.0% | -0.791 to -0.362 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
