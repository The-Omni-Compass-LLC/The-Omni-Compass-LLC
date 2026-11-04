# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 195 | +1.7% | -0.209 to 6.56 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.5% | -3.34 to 1.34 | STEADY, no difference beyond the noise |
| queries a second | 3,937 | 3,917 | -0.5% | -66.9 to 26.8 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.63 | 6.79 | -21.4% | -2.29 to -1.4 | GAIN |
| latency, 99th percentile (ms) | 12.8 | 8.69 | -32.3% | -5.26 to -3.03 | GAIN |
| latency, mean (ms) | 5.2 | 4.85 | -6.8% | -0.435 to -0.27 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,025 | +100.2% | 396 to 630 | power given |
| pages holding data, mean (MB) | 462 | 914 | +97.5% | 336 to 566 | power given |
| pages read from disk into the pool (misses) | 618,992 | 122,527 | -80.2% | -517,507 to -475,423 | shown, not judged |
| host CPU busy (share of the run) | 0.278 | 0.259 | -6.8% | -0.028 to -0.00952 | GAIN |
| host CPU-seconds | 489 | 456 | -6.8% | -49.1 to -17.4 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.55 | 5.09 | -8.3% | -0.562 to -0.363 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
