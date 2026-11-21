# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | +0.0% | -3.44 to 3.65 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.0% | -3.54 to 3.78 | EVEN, no difference beyond the noise |
| queries a second | 4,741 | 4,743 | +0.0% | -56.7 to 60.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.78 | 1.76 | -1.2% | -0.117 to 0.0727 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.25 | 3.13 | -3.6% | -0.493 to 0.259 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.25 | +0.5% | -0.0519 to 0.0646 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 330 | -35.6% | -277 to -88.1 | GAIN |
| pages holding data, mean (MB) | 462 | 297 | -35.7% | -243 to -86.5 | GAIN |
| pages read from disk into the pool (misses) | 655,100 | 1,180,080 | +80.1% | 119,379 to 930,582 | shown, not judged |
| host CPU busy (share of the run) | 0.0987 | 0.0994 | +0.7% | -0.00273 to 0.00406 | EVEN, no difference beyond the noise |
| host CPU-seconds | 177 | 179 | +0.7% | -4.85 to 7.28 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.31 | 1.32 | +0.7% | -0.0503 to 0.0674 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 2.41 to 14.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
