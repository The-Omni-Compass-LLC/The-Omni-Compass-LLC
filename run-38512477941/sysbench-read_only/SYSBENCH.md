# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -1.82 to 2.51 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -1.76 to 2.51 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,726 | +0.1% | -28.2 to 40.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 3.96 | -1.2% | -0.151 to 0.0553 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.54 | 5.47 | -1.2% | -0.348 to 0.217 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.12 | 3.11 | -0.3% | -0.0563 to 0.0388 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 453 | -11.4% | -199 to 81.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 409 | -11.5% | -165 to 58.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,477 | 799,412 | +22.1% | -366,952 to 656,823 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.186 | +0.8% | -0.00739 to 0.0103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 305 | 308 | +1.0% | -12.6 to 18.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.26 | 2.28 | +0.8% | -0.0818 to 0.119 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20 |  | 10.1 to 29.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
