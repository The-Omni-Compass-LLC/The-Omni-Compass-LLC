# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.2% | -2.31 to 3.18 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.0% | -0.74 to 0.873 | EVEN, no difference beyond the noise |
| queries a second | 3,930 | 3,932 | +0.0% | -14.8 to 17.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.38 | 8.18 | -2.4% | -0.972 to 0.578 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.3 | 12.1 | -1.8% | -1.87 to 1.43 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.24 | 5.24 | -0.0% | -0.27 to 0.266 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 570 | +11.3% | -22 to 137 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 508 | +9.9% | -24.9 to 116 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,895 | 513,919 | -16.7% | -256,600 to 50,647 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.21 | -0.1% | -0.0144 to 0.0137 | EVEN, no difference beyond the noise |
| host CPU-seconds | 338 | 338 | -0.0% | -22.4 to 22.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.84 | 3.83 | -0.3% | -0.311 to 0.291 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 4.83 to 29.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
