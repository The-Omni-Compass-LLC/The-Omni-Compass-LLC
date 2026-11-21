# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 192 | -0.3% | -2.05 to 0.717 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.0% | -1.81 to 1.62 | EVEN, no difference beyond the noise |
| queries a second | 3,928 | 3,926 | -0.0% | -36.2 to 32.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.18 | 8.43 | +3.0% | 0.0439 to 0.451 | LOSS |
| latency, 99th percentile (ms) | 12.1 | 12.4 | +3.0% | 0.057 to 0.677 | LOSS |
| latency, mean (ms) | 5.16 | 5.21 | +1.0% | -0.16 to 0.261 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -40.1 to 29 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 458 | -1.0% | -33.2 to 24.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 617,045 | 621,648 | +0.7% | -58,543 to 67,747 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.208 | +0.9% | -0.0161 to 0.0198 | EVEN, no difference beyond the noise |
| host CPU-seconds | 332 | 335 | +1.0% | -26.3 to 33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.76 | 3.81 | +1.4% | -0.305 to 0.407 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 10.7 to 26.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
