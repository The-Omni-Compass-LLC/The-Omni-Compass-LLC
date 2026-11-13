# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 291 | +0.5% | -4.84 to 8.01 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 293 | +0.7% | -3.26 to 7.14 | no difference beyond the noise |
| queries a second | 4,654 | 4,685 | +0.7% | -52.2 to 114 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.77 | 5.91 | +2.4% | -0.0128 to 0.294 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7.61 | 7.85 | +3.1% | -0.509 to 0.983 | no difference beyond the noise |
| latency, mean (ms) | 3.45 | 3.51 | +2.0% | -0.032 to 0.167 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -36.5 to 23.7 | no difference beyond the noise |
| pages holding data, mean (MB) | 444 | 436 | -1.9% | -43.6 to 26.9 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 169,724 | 171,354 | +1.0% | -15,133 to 18,393 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.207 | +3.7% | 0.00669 to 0.00792 | **WORSE** |
| host CPU-seconds | 74.1 | 77 | +3.9% | 2.54 to 3.25 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.48 | 2.56 | +3.3% | 0.0292 to 0.132 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
