# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 179 | 179 | -0.1% | -4.56 to 4.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.2% | -3.11 to 3.96 | EVEN, no difference beyond the noise |
| queries a second | 3,919 | 3,928 | +0.2% | -62.2 to 79.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.8 | 12.9 | +1.2% | -0.179 to 0.491 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 17.8 | 18.3 | +2.5% | -0.506 to 1.38 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.24 | 6.31 | +1.0% | -0.0436 to 0.164 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 143 | +11.5% | 4.89 to 24.5 | power given |
| pages holding data, mean (MB) | 121 | 133 | +9.9% | 0.0332 to 23.9 | power given |
| pages read from disk into the pool (misses) | 1,662,865 | 1,587,322 | -4.5% | -103,467 to -47,618 | shown, not judged |
| host CPU busy (share of the run) | 0.247 | 0.249 | +0.7% | -0.0115 to 0.015 | EVEN, no difference beyond the noise |
| host CPU-seconds | 399 | 402 | +0.8% | -17.1 to 23.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.86 | 4.91 | +0.9% | -0.249 to 0.334 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
