# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -4.82 to 2.99 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.3% | -4.17 to 2.36 | EVEN, no difference beyond the noise |
| queries a second | 4,707 | 4,692 | -0.3% | -66.7 to 37.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.44 | 5.47 | +0.6% | -0.532 to 0.601 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.3 | 7.26 | -0.6% | -0.792 to 0.707 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.54 | 3.52 | -0.6% | -0.372 to 0.328 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 143 | +11.5% | 13.6 to 15.8 | power given |
| pages holding data, mean (MB) | 121 | 141 | +16.6% | 10.9 to 29.3 | power given |
| pages read from disk into the pool (misses) | 593,558 | 541,827 | -8.7% | -128,249 to 24,788 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.214 | -1.3% | -0.0354 to 0.03 | EVEN, no difference beyond the noise |
| host CPU-seconds | 121 | 119 | -1.3% | -20.8 to 17.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.68 | 2.66 | -1.0% | -0.489 to 0.436 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
