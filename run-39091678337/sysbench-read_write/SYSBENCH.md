# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 193 | +0.3% | -0.611 to 1.76 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.3% | -1.55 to 2.75 | EVEN, no difference beyond the noise |
| queries a second | 3,935 | 3,947 | +0.3% | -31.1 to 55 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.53 | 8.43 | -1.2% | -0.881 to 0.685 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.7 | 12.7 | +0.1% | -1.12 to 1.14 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.27 | 5.25 | -0.4% | -0.217 to 0.175 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 549 | +7.3% | -53.3 to 128 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 489 | +5.8% | -47.6 to 101 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 618,717 | 545,386 | -11.9% | -234,061 to 87,397 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.207 | -1.1% | -0.011 to 0.00637 | EVEN, no difference beyond the noise |
| host CPU-seconds | 336 | 332 | -1.1% | -17.4 to 10.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.81 | 3.76 | -1.4% | -0.201 to 0.0966 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 14 to 24 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
