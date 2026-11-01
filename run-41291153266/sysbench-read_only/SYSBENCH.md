# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `078cb4ce8aeb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 291 | +0.1% | -5.76 to 6.45 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.1% | -3.34 to 2.84 | STEADY, no difference beyond the noise |
| queries a second | 4,744 | 4,740 | -0.1% | -53.4 to 45.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.98 | 2.81 | -5.8% | -0.448 to 0.0989 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 55.5 | 45.7 | -17.7% | -119 to 99.8 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.84 | 3.32 | -13.4% | -2.91 to 1.88 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,153 | +800.6% | 941 to 1,109 | power given |
| pages holding data, mean (MB) | 120 | 947 | +688.6% | 807 to 847 | power given |
| pages read from disk into the pool (misses) | 2,004,091 | 101,578 | -94.9% | -1,915,359 to -1,889,668 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.16 | -6.2% | -0.0194 to -0.00162 | GAIN |
| host CPU-seconds | 306 | 287 | -6.2% | -35.4 to -2.6 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.31 | 2.17 | -6.3% | -0.298 to 0.00874 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 1.58 to 26.4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 10.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
