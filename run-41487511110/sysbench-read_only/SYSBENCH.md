# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.4% | -7.29 to 9.51 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 297 | 297 | -0.0% | -2.26 to 1.98 | STEADY, no difference beyond the noise |
| queries a second | 4,748 | 4,745 | -0.0% | -36.1 to 31.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.79 | 2.65 | -5.3% | -0.273 to -0.0218 | GAIN |
| latency, 99th percentile (ms) | 29.9 | 13.8 | -53.9% | -105 to 73.2 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.02 | 2.67 | -11.6% | -2.93 to 2.23 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,193 | +133.0% | 469 to 892 | power given |
| pages holding data, mean (MB) | 461 | 960 | +108.0% | 487 to 510 | power given |
| pages read from disk into the pool (misses) | 658,615 | 79,723 | -87.9% | -582,843 to -574,941 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.158 | -3.4% | -0.00984 to -0.00122 | GAIN |
| host CPU-seconds | 294 | 284 | -3.4% | -17.6 to -2.23 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.21 | 2.12 | -3.7% | -0.139 to -0.0255 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 1.99 to 22.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 5.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
