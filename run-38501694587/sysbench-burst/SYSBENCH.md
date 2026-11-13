# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.2% | -7.73 to 6.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -7.08 to 7.03 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,720 | -0.0% | -113 to 112 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.37 | 5.37 | -0.0% | -0.422 to 0.419 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.48 | 7.75 | +3.7% | -0.414 to 0.965 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.36 | 3.39 | +0.8% | -0.00443 to 0.0556 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 445 | -13.1% | -140 to 6.09 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 381 | -14.8% | -155 to 22.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,982 | 257,953 | +5.3% | -42,054 to 67,995 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.2 | +2.4% | 0.00183 to 0.00736 | power given |
| host CPU-seconds | 108 | 111 | +2.7% | 1.19 to 4.67 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.46 | +2.8% | 0.0105 to 0.123 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
