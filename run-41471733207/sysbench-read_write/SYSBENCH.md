# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 183 | 196 | +6.8% | 9.45 to 15.7 | GAIN |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.31 to 2.62 | STEADY, no difference beyond the noise |
| queries a second | 3,931 | 3,934 | +0.1% | -46.1 to 52.3 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 11.7 | 6.91 | -41.0% | -5.25 to -4.38 | GAIN |
| latency, 99th percentile (ms) | 16.2 | 9.28 | -42.8% | -7.41 to -6.46 | GAIN |
| latency, mean (ms) | 5.82 | 4.86 | -16.4% | -1.03 to -0.877 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 950 | +642.0% | 769 to 875 | power given |
| pages holding data, mean (MB) | 120 | 852 | +612.8% | 698 to 767 | power given |
| pages read from disk into the pool (misses) | 1,665,540 | 185,825 | -88.8% | -1,585,424 to -1,374,007 | shown, not judged |
| host CPU busy (share of the run) | 0.306 | 0.265 | -13.5% | -0.0531 to -0.0294 | GAIN |
| host CPU-seconds | 538 | 465 | -13.5% | -93.8 to -51.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.42 | 5.19 | -19.1% | -1.44 to -1.01 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 2.87 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
