# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | -0.3% | -4.15 to 2.98 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.1% | -1.47 to 1.18 | EVEN, no difference beyond the noise |
| queries a second | 3,909 | 3,906 | -0.1% | -29.5 to 23.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.25 | 7.63 | +5.2% | -1.03 to 1.79 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.8 | 11.3 | +4.1% | -2.36 to 3.24 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.18 | 4.28 | +2.3% | -0.314 to 0.506 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 493 | -3.7% | -150 to 112 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 432 | -6.4% | -149 to 90.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,319 | 692,308 | +12.5% | -208,450 to 362,428 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.198 | +0.1% | -0.00795 to 0.00826 | EVEN, no difference beyond the noise |
| host CPU-seconds | 357 | 357 | +0.1% | -14.3 to 15 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4 | 4.02 | +0.4% | -0.183 to 0.215 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.3 |  | 10.9 to 29.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
