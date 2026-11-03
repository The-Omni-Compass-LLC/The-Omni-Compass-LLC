# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 195 | -0.1% | -1.82 to 1.25 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.3% | -2.79 to 1.45 | STEADY, no difference beyond the noise |
| queries a second | 3,929 | 3,915 | -0.3% | -55.7 to 29 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.63 | 5.88 | -11.3% | -1.17 to -0.329 | GAIN |
| latency, 99th percentile (ms) | 9.33 | 8.03 | -13.9% | -1.87 to -0.728 | GAIN |
| latency, mean (ms) | 4.28 | 4.21 | -1.8% | -0.284 to 0.125 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 923 | +80.2% | 71.2 to 750 | power given |
| pages holding data, mean (MB) | 461 | 826 | +79.1% | 66.5 to 663 | power given |
| pages read from disk into the pool (misses) | 619,556 | 209,079 | -66.3% | -525,983 to -294,971 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.237 | -3.0% | -0.0136 to -0.000789 | GAIN |
| host CPU-seconds | 443 | 430 | -3.1% | -23.4 to -3.84 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.93 | 4.79 | -2.9% | -0.22 to -0.0694 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
