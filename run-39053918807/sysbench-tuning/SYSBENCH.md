# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,943 | 2,947 | +0.1% | -2.15 to 10.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,951 | 2,954 | +0.1% | -3.39 to 10.8 | EVEN, no difference beyond the noise |
| queries a second | 2,951 | 2,954 | +0.1% | -3.39 to 10.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.314 | -1.3% | -0.0268 to 0.0188 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.462 | 0.451 | -2.4% | -0.0218 to -0.000171 | GAIN |
| latency, mean (ms) | 0.198 | 0.198 | +0.3% | -3.13e-05 to 0.00123 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 489 | -4.5% | -75.8 to 29.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 440 | -5.1% | -62.9 to 15.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 364,912 | 381,592 | +4.6% | -64,810 to 98,169 | shown, not judged |
| host CPU busy (share of the run) | 0.0946 | 0.0971 | +2.7% | -0.00315 to 0.00831 | EVEN, no difference beyond the noise |
| host CPU-seconds | 156 | 161 | +2.9% | -5.39 to 14.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.116 | 0.12 | +2.8% | -0.00405 to 0.0105 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 8.41 to 20.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
