# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7.73 | 6.01 | -22.3% | -3.88 to 0.431 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 984 | +0.1% | -2.98 to 4.66 | EVEN, no difference beyond the noise |
| queries a second | 983 | 984 | +0.1% | -2.98 to 4.66 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.67 | 1.71 | +2.8% | -0.356 to 0.45 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.82 | 2.7 | -4.2% | -0.756 to 0.52 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.07 | +2.5% | -0.133 to 0.185 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 482 | -5.9% | -98.6 to 37.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 407 | -10.2% | -115 to 22.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,694 | 218,629 | +15.3% | 5,870 to 51,999 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.167 | +36.1% | -0.0414 to 0.13 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 258 | +36.2% | -64.3 to 201 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 76.4 | 403 | +428.2% | -1,006 to 1,660 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 25.3 |  | 6.36 to 44.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
