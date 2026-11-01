# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `dca8d09bbaa4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 194 | +8.6% | 14.9 to 15.9 | GAIN |
| throughput (transactions a second) | 196 | 196 | +0.1% | -0.576 to 0.842 | STEADY, no difference beyond the noise |
| queries a second | 3,923 | 3,926 | +0.1% | -11.5 to 16.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 13 | 7.52 | -42.1% | -5.77 to -5.15 | GAIN |
| latency, 99th percentile (ms) | 18.4 | 11.5 | -37.4% | -7.24 to -6.5 | GAIN |
| latency, mean (ms) | 6.22 | 5.09 | -18.2% | -1.17 to -1.09 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,054 | +723.1% | 873 to 978 | power given |
| pages holding data, mean (MB) | 119 | 940 | +691.0% | 768 to 875 | power given |
| pages read from disk into the pool (misses) | 1,662,813 | 137,935 | -91.7% | -1,660,640 to -1,389,115 | shown, not judged |
| host CPU busy (share of the run) | 0.309 | 0.263 | -14.9% | -0.0548 to -0.0373 | GAIN |
| host CPU-seconds | 544 | 462 | -15.0% | -96.9 to -66.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.66 | 5.21 | -21.7% | -1.62 to -1.27 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 5.23 to 8.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
