# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.96 | 5.38 | +8.4% | -6.41 to 7.24 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -5.96 to 3.88 | EVEN, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -5.96 to 3.88 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.75 | 1.72 | -1.4% | -0.226 to 0.177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.37 | 3.43 | +1.7% | -0.34 to 0.455 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.07 | 1.07 | -0.2% | -0.102 to 0.0991 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 515 | +0.6% | -15.9 to 21.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 447 | -1.4% | -14.2 to 1.31 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,589 | 189,422 | +0.4% | -18,328 to 19,994 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.121 | -4.3% | -0.033 to 0.0222 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 186 | -4.2% | -49.8 to 33.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 142 | 81.4 | -42.6% | -284 to 164 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 3.29 to 23.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
