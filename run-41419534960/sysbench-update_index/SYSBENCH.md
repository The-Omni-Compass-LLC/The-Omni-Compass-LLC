# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.05 | 6.04 | +49.2% | -0.218 to 4.2 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.1% | -8.37 to 6.09 | STEADY, no difference beyond the noise |
| queries a second | 985 | 984 | -0.1% | -8.37 to 6.09 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.26 | 1.83 | -19.0% | -0.56 to -0.299 | GAIN |
| latency, 99th percentile (ms) | 4.68 | 4.39 | -6.2% | -1.35 to 0.778 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.19 | -7.1% | -0.128 to -0.0546 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,267 | +890.0% | 1,081 to 1,197 | power given |
| pages holding data, mean (MB) | 118 | 866 | +632.8% | 724 to 772 | power given |
| pages read from disk into the pool (misses) | 418,725 | 83,544 | -80.0% | -359,881 to -310,481 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.208 | -12.7% | -0.055 to -0.00572 | GAIN |
| host CPU-seconds | 419 | 366 | -12.7% | -95.3 to -11.2 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 239 | 133 | -44.4% | -275 to 63.4 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
