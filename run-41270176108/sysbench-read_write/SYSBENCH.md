# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 132 | 140 | +6.1% | -22 to 38.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.0% | -1.79 to 1.72 | STEADY, no difference beyond the noise |
| queries a second | 3,934 | 3,933 | -0.0% | -35.8 to 34.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 166 | 107 | -35.5% | -91 to -26.8 | GAIN |
| latency, 99th percentile (ms) | 425 | 240 | -43.5% | -533 to 164 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 32.8 | 21.4 | -34.7% | -18.9 to -3.87 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,283 | +150.5% | 724 to 817 | power given |
| pages holding data, mean (MB) | 463 | 1,029 | +122.3% | 553 to 579 | power given |
| pages read from disk into the pool (misses) | 618,330 | 82,765 | -86.6% | -572,299 to -498,833 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.166 | -10.9% | -0.023 to -0.0175 | GAIN |
| host CPU-seconds | 331 | 295 | -11.0% | -40.9 to -31.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.52 | 4.67 | -15.4% | -1.83 to 0.124 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 2.68 to 18.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
